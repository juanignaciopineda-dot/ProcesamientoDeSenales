"""Variantes de pronunciación de «Bernoulli» para elegir de oído (README §9).

Uso:
    python probar_bernoulli.py
Genera voces_prueba/bernoulli/bernoulli.mp3 (todas las opciones numeradas, con la
frase del guion) y un mp3 por variante; el usuario elige un número.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

SALIDA = Path(__file__).parent / "bernoulli"
FRASE = "La más sencilla es discreta: la de {}. La variable solo puede valer cero o uno, como un bit."
VARIANTES = {
    "1_tal_cual": "Bernoulli",
    "2_bernuli": "Bernuli",
    "3_bernuli_acento": "Bernulí",
    "4_bernuli_dos_eles": "Bernúlli",
    "5_bernoyi": "Bernouyi",
    "6_bernulli": "Bernulli",
}
NUMEROS = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho"]

if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for nombre, v in VARIANTES.items():
        sintetizar_mp3(FRASE.format(v), SALIDA / f"{nombre}.mp3")
        print("listo", nombre, "<-", v)
    texto = " ".join(f"Opción {NUMEROS[i]}: la de {v}." for i, v in enumerate(VARIANTES.values()))
    sintetizar_mp3(texto, SALIDA / "bernoulli.mp3")
    print("listo bernoulli.mp3")
