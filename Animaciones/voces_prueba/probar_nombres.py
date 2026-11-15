"""Prueba cómo pronuncia la voz elegida los nombres propios del guion, para detectar cuáles necesitan una entrada en comun/pronunciacion.py.

Uso:
    python probar_nombres.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

SALIDA = Path(__file__).parent / "nombres"

# Nombres propios de la materia (los de concurrente ya se decidieron allá).
# Mismo formato: nombre_del_mp3: frase. Para comparar variantes, agregar otra
# entrada con la grafía alternativa (ej. "2_chebyshev_fonetico").
CASOS = {
    "01_bayes": "La regla de Bayes da la vuelta a la pregunta.",
    "02_chebyshev": "La desigualdad de Chebyshev acota la probabilidad de alejarse de la media.",
    "03_gauss": "La campana de Gauss aparece en todas partes.",
    "04_neyman_pearson": "El criterio de Neyman-Pearson fija la falsa alarma y maximiza la detección.",
    "05_wiener": "El filtro de Wiener es el mejor filtro lineal.",
    "06_kalman": "El filtro de Kalman actualiza la estimación con cada muestra nueva.",
    "07_bochner": "El teorema de Bochner dice qué funciones pueden ser una autocorrelación.",
    "08_cauchy_schwarz": "La desigualdad de Cauchy-Schwarz dice cuándo el filtro adaptado gana.",
    "09_welch": "El método de Welch promedia periodogramas.",
    "10_parseval": "Por Parseval, la energía es la misma en el tiempo y en la frecuencia.",
    "11_wiener_khinchin": "El teorema de Wiener-Khinchin une la autocorrelación con el espectro.",
}


def generar(nombre: str, texto: str) -> None:
    destino = SALIDA / f"{nombre}.mp3"
    sintetizar_mp3(texto, destino)
    print(f"  listo: {destino.name}  <-  {texto}")


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    print(f"Generando {len(CASOS)} muestras en {SALIDA} ...")
    for nombre, texto in CASOS.items():
        generar(nombre, texto)
    print("\nListo. Escuchá cada par (tal cual vs. fonético) y decime cuál suena mejor.")


if __name__ == "__main__":
    main()
