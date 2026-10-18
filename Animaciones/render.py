"""Renderiza un episodio completo a partir de su guion.md.

    python render.py <carpeta_episodio> [--calidad ql|qm|qh|qk] [--solo-unir]
                     [--escenas 01,03] [--sin-musica]

1. Lee el orden de las escenas de <carpeta>/guion.md ('# Escena NN — Clase').
2. Renderiza cada una con Manim (archivo sNN_*.py, clase Clase).
3. Concatena en <carpeta>/salida/<carpeta>-<resolucion>.mp4.
4. Une los subtítulos (.srt) corrigiendo los desfasajes.
5. Escribe capitulos.txt con las marcas de tiempo para la descripción de YouTube.
6. Si hay una pista en Animaciones/musica/, la mezcla bajita debajo de la voz.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from comun.guion import escenas_del_guion  # noqa: E402

RESOLUCION = {"ql": "480p15", "qm": "720p30", "qh": "1080p60", "qk": "2160p60"}
VOLUMEN_MUSICA = 0.07   # respecto de la voz (0.07 ≈ -23 dB)


def _duracion(mp4: Path) -> float:
    salida = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)],
        capture_output=True, text=True, check=True).stdout
    return float(salida.strip())


def _archivo_escena(carpeta: Path, numero: str) -> Path:
    candidatos = sorted(carpeta.glob(f"s{numero}_*.py"))
    if not candidatos:
        raise FileNotFoundError(f"no hay archivo s{numero}_*.py en {carpeta}")
    return candidatos[0]


def _mp4_escena(carpeta: Path, archivo: Path, clase: str, res: str) -> Path:
    return carpeta / "media" / "videos" / archivo.stem / res / f"{clase}.mp4"


# ------------------------------------------------------------------ subtítulos

_RE_TIEMPO = re.compile(r"(\d+):(\d+):(\d+),(\d+)")


def _a_seg(m: re.Match) -> float:
    h, mi, s, ms = map(int, m.groups())
    return h * 3600 + mi * 60 + s + ms / 1000


def _a_srt(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    mi, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{mi:02d}:{s:02d},{ms:03d}"


def _unir_srt(partes: list[tuple[Path, float]], destino: Path) -> None:
    bloques, n = [], 1
    for srt, offset in partes:
        if not srt.exists():
            continue
        for bloque in srt.read_text(encoding="utf-8").strip().split("\n\n"):
            lineas = bloque.strip().splitlines()
            if len(lineas) < 3 or "-->" not in lineas[1]:
                continue
            ini, fin = _RE_TIEMPO.findall(lineas[1])[:2]
            t0 = sum(x * y for x, y in zip(map(int, ini), (3600, 60, 1, 0.001))) + offset
            t1 = sum(x * y for x, y in zip(map(int, fin), (3600, 60, 1, 0.001))) + offset
            bloques.append(f"{n}\n{_a_srt(t0)} --> {_a_srt(t1)}\n" + "\n".join(lineas[2:]))
            n += 1
    destino.write_text("\n\n".join(bloques) + "\n", encoding="utf-8")


def _mmss(t: float) -> str:
    t = int(t)
    return f"{t // 60}:{t % 60:02d}" if t < 3600 else f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}"


# ------------------------------------------------------------------ informes

def _resumen_informes(carpeta: Path, escenas) -> int:
    """Muestra lo que anotó EscenaCurso: animaciones atrasadas respecto de la
    voz, silencios de voz, textos encimados y fuera de cuadro."""
    import json
    problemas = 0
    print("\n--- controles automáticos ---")
    for e in escenas:
        ruta = carpeta / "media" / "informes" / f"{e.clase}.json"
        if not ruta.exists():
            continue
        inf = json.loads(ruta.read_text(encoding="utf-8"))
        lineas = []
        for r in inf.get("retrasos", []):
            lineas.append(f"  atraso {r['segundos']:.1f}s en {r['bloque']}/{r['marca']} (voz en {r['t']:.1f}s)")
        for s in inf.get("silencios", []):
            lineas.append(f"  silencio de voz {s['segundos']:.1f}s al final de {s['bloque']} ({s['t']:.1f}s)")
        for x in inf.get("encimados", []):
            lineas.append(f"  encimado en {x['t']:.1f}s: «{x['texto']}» con {x['con']} ({x['solape']:.0%})")
        for f in inf.get("fuera_de_cuadro", []):
            lineas.append(f"  fuera de cuadro en {f['t']:.1f}s: «{f['texto']}»")
        if lineas:
            problemas += len(lineas)
            print(f"{e.numero} {e.clase}:")
            print("\n".join(lineas))
    print(f"--- {problemas} avisos ---\n" if problemas else "--- sin avisos ---\n")
    return problemas


# ------------------------------------------------------------------ principal

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--calidad", default="ql", choices=RESOLUCION)
    ap.add_argument("--solo-unir", action="store_true")
    ap.add_argument("--escenas", default="", help="lista NN separada por comas (solo renderiza esas)")
    ap.add_argument("--sin-musica", action="store_true")
    args = ap.parse_args()

    carpeta = Path(args.carpeta).resolve()
    res = RESOLUCION[args.calidad]
    escenas = escenas_del_guion(carpeta / "guion.md")
    elegidas = {e.zfill(2) for e in args.escenas.split(",") if e}

    entorno = dict(os.environ, PYTHONPATH=str(RAIZ), PYTHONIOENCODING="utf-8")
    log = carpeta / "render.log"

    if not args.solo_unir:
        log.write_text("", encoding="utf-8")
        for i, e in enumerate(escenas, 1):
            if elegidas and e.numero not in elegidas:
                continue
            archivo = _archivo_escena(carpeta, e.numero)
            print(f"[{i}/{len(escenas)}] {e.numero} {e.clase} ...", flush=True)
            with open(log, "a", encoding="utf-8") as f:
                r = subprocess.run([sys.executable, "-m", "manim", f"-{args.calidad}",
                                    archivo.name, e.clase],
                                   cwd=carpeta, env=entorno, stdout=f, stderr=subprocess.STDOUT)
            if r.returncode != 0:
                print(f"  FALLÓ {e.clase}. Últimas líneas de {log.name}:")
                print("\n".join(log.read_text(encoding="utf-8", errors="replace").splitlines()[-30:]))
                return 1

    if not args.solo_unir:
        _resumen_informes(carpeta, [e for e in escenas if not elegidas or e.numero in elegidas])

    if elegidas:
        print("listo (solo las escenas pedidas; para armar el episodio: --solo-unir)")
        return 0

    # ---------------------------------------------------------- concatenar
    salida = carpeta / "salida"
    salida.mkdir(exist_ok=True)
    mp4s, faltan = [], []
    for e in escenas:
        mp4 = _mp4_escena(carpeta, _archivo_escena(carpeta, e.numero), e.clase, res)
        (mp4s if mp4.exists() else faltan).append(mp4)
    if faltan:
        print("Faltan renders en", res, ":", *[f"\n  {m}" for m in faltan])
        return 1

    lista = carpeta / "lista.txt"
    lista.write_text("".join(f"file '{m.as_posix()}'\n" for m in mp4s), encoding="utf-8")
    base = f"{carpeta.name}-{res}"
    video = salida / f"{base}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(lista), "-c", "copy", str(video)], check=True)

    # ---------------------------------------------------------- subtítulos y capítulos
    offsets, t = [], 0.0
    for m in mp4s:
        offsets.append(t)
        t += _duracion(m)
    _unir_srt([(m.with_suffix(".srt"), o) for m, o in zip(mp4s, offsets)], salida / f"{base}.srt")

    capitulos = [(o, e.capitulo) for o, e in zip(offsets, escenas) if e.capitulo]
    if not capitulos or capitulos[0][0] > 0:
        capitulos.insert(0, (0.0, "Intro"))
    (salida / "capitulos.txt").write_text(
        "".join(f"{_mmss(o)} {titulo}\n" for o, titulo in capitulos), encoding="utf-8")

    # ---------------------------------------------------------- música (opcional)
    pistas = sorted((RAIZ / "musica").glob("*.mp3")) + sorted((RAIZ / "musica").glob("*.wav")) \
        if (RAIZ / "musica").exists() else []
    if pistas and not args.sin_musica:
        con_musica = salida / f"{base}-musica.mp4"
        subprocess.run([
            "ffmpeg", "-v", "error", "-y", "-i", str(video), "-stream_loop", "-1", "-i", str(pistas[0]),
            "-filter_complex",
            f"[1:a]volume={VOLUMEN_MUSICA}[m];[0:a][m]amix=inputs=2:duration=first:normalize=0[a]",
            "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-shortest", str(con_musica)], check=True)
        video = con_musica

    print(f"\nlisto: {video}")
    print(f"duración {_mmss(t)}  ·  {video.stat().st_size / 2**20:.1f} MB")
    print(f"subtítulos: {salida / (base + '.srt')}")
    print(f"capítulos:  {salida / 'capitulos.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
