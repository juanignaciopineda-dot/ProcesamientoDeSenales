"""Vuelve a armar en 1080p60 todos los episodios de un capítulo (o uno solo).

    python rehacer.py Capitulo07_Probabilidad            # los 7 episodios
    python rehacer.py Capitulo07_Probabilidad E3         # solo el E3
    python rehacer.py Capitulo07_Probabilidad --calidad ql   # borrador rápido

Llama a render.py con cada carpeta E<N>_* del capítulo, en orden. La voz sale
de la caché versionada en <episodio>/media/voiceovers/: si está completa, no se
sintetiza nada (no hace falta internet ni la clave de Azure) y el vídeo queda
igual al subido. Los mp4, .srt y capitulos.txt quedan en <episodio>/salida/.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("capitulo", help="carpeta del capítulo, ej. Capitulo07_Probabilidad")
    ap.add_argument("episodios", nargs="*", help="E1 E3 … (por defecto, todos)")
    ap.add_argument("--calidad", default="qh", choices=["ql", "qm", "qh", "qk"])
    args = ap.parse_args()

    capitulo = (RAIZ / args.capitulo).resolve()
    carpetas = sorted((c for c in capitulo.glob("E*_*") if (c / "guion.md").exists()),
                      key=lambda c: int(c.name.split("_")[0][1:]))
    if args.episodios:
        pedidos = {e.upper() for e in args.episodios}
        carpetas = [c for c in carpetas if c.name.split("_")[0].upper() in pedidos]
    if not carpetas:
        print(f"No encontré episodios en {capitulo}")
        return 1
    if shutil.which("ffmpeg") is None:
        print("Falta ffmpeg en el PATH (winget install Gyan.FFmpeg).")
        return 1

    for c in carpetas:
        voces = c / "media" / "voiceovers" / "cache.json"
        if not voces.exists():
            print(f"Aviso: {c.name} no tiene caché de voz; se sintetiza de nuevo (Azure, .env).")
        print(f"\n=== {c.name} ({args.calidad}) ===", flush=True)
        r = subprocess.run([sys.executable, str(RAIZ / "render.py"), str(c), "--calidad", args.calidad])
        if r.returncode != 0:
            print(f"Falló {c.name}: revisar {c / 'render.log'}")
            return r.returncode
    print("\nListo. Los vídeos están en la carpeta salida/ de cada episodio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
