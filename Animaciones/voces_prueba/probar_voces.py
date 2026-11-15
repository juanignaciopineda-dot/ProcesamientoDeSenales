"""Genera el mismo párrafo con distintas voces de edge-tts para elegir de oído.

Uso:
    python probar_voces.py

Escuchá los .mp3 generados en esta misma carpeta y avisale a Claude cuál te
gustó más (por nombre de archivo, ej. "es-AR-TomasNeural"). Esa voz queda fija
en comun/voz.py para todas las escenas del curso.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

# Párrafo de prueba: el tipo de texto real del curso (una fórmula dicha en
# palabras, siglas y un nombre propio), para juzgar la voz en condiciones reales.
# La voz del curso ya está elegida (Ximena, igual que Programación Concurrente);
# esto queda por si hay que volver a decidir.
TEXTO = (
    "Imagina que grabas el mismo ruido mil veces. Cada grabación es distinta, "
    "pero todas comparten algo: la autocorrelación, R sub equis equis de tau, "
    "que mide cuánto se parece la señal a sí misma corrida tau segundos. "
    "Wiener se preguntó cuál es el mejor filtro lineal para separar la señal "
    "del ruido, y la respuesta depende solo de dos curvas: la densidad "
    "espectral de la señal y la del ruido. Con una relación señal a ruido de "
    "diez decibelios, el error cuadrático medio cae a cero coma uno."
)

VOCES = [
    "es-AR-ElenaNeural",
    "es-AR-TomasNeural",
    "es-MX-DaliaNeural",
    "es-MX-JorgeNeural",
    "es-ES-AlvaroNeural",
    "es-ES-XimenaNeural",
    "es-ES-ElviraNeural",
]

SALIDA = Path(__file__).parent


def generar(voz: str) -> None:
    destino = SALIDA / f"{voz}.mp3"
    sintetizar_mp3(TEXTO, destino, voz=voz)
    print(f"  listo: {destino.name}")


def main() -> None:
    print(f"Generando {len(VOCES)} muestras en {SALIDA} ...")
    for voz in VOCES:
        print(f"- {voz}")
        generar(voz)
    print("\nListo. Escuchá los .mp3 y elegí la que suene más humana.")


if __name__ == "__main__":
    main()
