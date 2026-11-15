"""Variantes de pronunciación de «Fourier» con la frase del episodio 1 del capítulo 7.

Uso:
    python probar_fourier.py
Deja los mp3 en voces_prueba/fourier/ (numerados: el usuario elige un número).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

SALIDA = Path(__file__).parent / "fourier2"
FRASE = "Eso es la transformada de {}, y el dibujo de cuánto hay de cada frecuencia es el espectro."

VARIANTES = {
    "a_fouriér": "Fouriér",
    "b_furiyé": "Furiyé",
    "c_fu_riér": "Fu-riér",
    "d_furriér": "Furriér",
    "e_fuhriér": "Fuhriér",
    "f_furiê": "Furiê",
    "g_fuyé": "Fuyé",
    "h_fur_yé": "Fur yé",
}


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    for nombre, grafia in VARIANTES.items():
        destino = SALIDA / f"{nombre}.mp3"
        sintetizar_mp3(FRASE.format(grafia), destino)
        print(f"  listo: {destino.name}  <-  {grafia}")


if __name__ == "__main__":
    main()
