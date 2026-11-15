"""Variantes de pronunciación de «Cauchy-Schwarz» para elegir de oído (README §9).

Uso:
    python probar_cauchy.py
Genera voces_prueba/cauchy/cauchy.mp3 (todas las opciones numeradas, con la frase del
guion) y un mp3 por variante; el usuario elige un número.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

SALIDA = Path(__file__).parent / "cauchy"
FRASE = "Simplificamos, y queda la desigualdad de {}: la covarianza nunca supera el producto de las desviaciones."
VARIANTES = {
    "1_tal_cual": "Cauchy-Schwarz",
    "2_sin_guion": "Cauchy Schwarz",
    "3_coshi_shuarts": "Coshi-Shuarts",
    "4_coshi_chuarts": "Coshi-Chuarts",
    "5_cochi_shuarts": "Cochi-Shuarts",
    "6_cochi_chuarts": "Cochi-Chuarts",
    "7_cauchi_shuarts": "Cauchi-Shuarts",
    "8_cauchy_schwartz": "Cauchy-Schwartz",
}
NUMEROS = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho"]

if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for nombre, v in VARIANTES.items():
        sintetizar_mp3(FRASE.format(v), SALIDA / f"{nombre}.mp3")
        print("listo", nombre, "<-", v)
    texto = " ".join(f"Opción {NUMEROS[i]}: la desigualdad de {v}." for i, v in enumerate(VARIANTES.values()))
    sintetizar_mp3(texto, SALIDA / "cauchy.mp3")
    print("listo cauchy.mp3")
