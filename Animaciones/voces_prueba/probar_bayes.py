"""Variantes de pronunciación de «Bayes» para elegir de oído (README §9).

Uso:
    python probar_bayes.py
Genera voces_prueba/bayes/NN_variante.mp3; el usuario elige un número.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

SALIDA = Path(__file__).parent / "bayes"
FRASE = "Esta es la regla de {}. La probabilidad a priori y la probabilidad a posteriori."
VARIANTES = {
    "1_tal_cual": "Bayes",
    "2_beis": "Beis",
    "3_bais": "Bais",
    "4_beyes": "Béyes",
    "5_bayes_acento": "Báyes",
    "6_beyz": "Beiz",
    "7_bellez": "Bayés",
}

if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for nombre, v in VARIANTES.items():
        sintetizar_mp3(FRASE.format(v), SALIDA / f"{nombre}.mp3")
        print("listo", nombre, "<-", v)
