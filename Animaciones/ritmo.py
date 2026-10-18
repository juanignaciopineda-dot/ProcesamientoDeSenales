"""Linter de ritmo: dónde cae cada momento anclado y qué huecos quedan sin animación.

    python ritmo.py <carpeta_episodio> [--max 3.0] [--escenas 03,04]

Para cada bloque sintetiza la voz (o la toma del caché de edge-tts), calcula
en qué segundo se dice cada frase anclada y avisa de los tramos de más de
`--max` segundos sin ningún momento: al principio del bloque, entre dos
momentos y del último momento al final del audio.

Es una guía, no una regla ciega: la animación de un momento puede cubrir parte
del hueco que le sigue (una ráfaga de 1,5 s, un contador que corre…).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))

from manim_voiceover.helper import remove_bookmarks  # noqa: E402
from manim_voiceover.modify_audio import get_duration  # noqa: E402
from manim_voiceover.tracker import AUDIO_OFFSET_RESOLUTION  # noqa: E402

from comun.guion import Guion, escenas_del_guion  # noqa: E402
from comun.voz import servicio_voz  # noqa: E402

RE_BM = __import__("re").compile(r"<bookmark mark=\"(\w+)\"/>")


def tiempos_marcas(texto: str, datos: dict, duracion: float) -> dict[str, float]:
    """Misma cuenta que VoiceoverTracker: posición en el texto → segundo."""
    wbs = datos.get("word_boundaries") or []
    xs = [0] + [w["text_offset"] for w in wbs] + [len(remove_bookmarks(texto))]
    ys = [0.0] + [w["audio_offset"] / AUDIO_OFFSET_RESOLUTION for w in wbs] + [duracion]
    import numpy as np
    marcas, limpio, pos = {}, "", 0
    for m in RE_BM.finditer(texto):
        limpio += texto[pos:m.start()]
        marcas[m.group(1)] = float(np.interp(len(limpio), xs, ys))
        pos = m.end()
    return marcas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--max", type=float, default=3.0)
    ap.add_argument("--escenas", default="")
    args = ap.parse_args()

    carpeta = Path(args.carpeta).resolve()
    elegidas = {e.zfill(2) for e in args.escenas.split(",") if e}
    cache = carpeta / "media" / "voiceovers"
    cache.mkdir(parents=True, exist_ok=True)
    servicio = servicio_voz(cache_dir=str(cache))

    total_huecos = 0
    for e in escenas_del_guion(carpeta / "guion.md"):
        if elegidas and e.numero not in elegidas:
            continue
        G = Guion(str(carpeta / "x.py"), e.numero)
        print(f"\n== {e.numero} {e.clase}")
        for b in G:
            texto = " ".join(G.texto(b).split())
            datos = servicio._wrap_generate_from_text(texto)
            dur = get_duration(Path(cache) / datos["final_audio"])
            t = tiempos_marcas(texto, datos, dur)
            puntos = [("inicio", 0.0)] + sorted(t.items(), key=lambda kv: kv[1]) + [("fin", dur)]
            linea = "  ".join(f"{m}@{s:.1f}" for m, s in puntos[1:-1])
            print(f"  {b} ({dur:.1f}s): {linea}")
            for (m1, s1), (m2, s2) in zip(puntos, puntos[1:]):
                if s2 - s1 > args.max:
                    total_huecos += 1
                    print(f"     ! hueco de {s2 - s1:.1f}s entre {m1} y {m2}")
    print(f"\n{total_huecos} huecos de más de {args.max}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
