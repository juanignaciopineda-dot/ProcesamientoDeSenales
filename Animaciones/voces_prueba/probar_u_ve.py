"""Variantes de «dos variables, u y v» (Cap. 7, E7, escena 11) para elegir de oído (README §9).

El problema: con «u y v» la voz lee la «y» como la letra («u, i griega, uve»).

Uso:
    python probar_u_ve.py
Genera voces_prueba/u_ve/u_ve.mp3 (todas las opciones numeradas) y un mp3 por variante.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

SALIDA = Path(__file__).parent / "u_ve"
FRASE = "{} Mira la esperanza de u menos lambda por v, todo al cuadrado."
VARIANTES = {
    "1_tal_cual": "Toma dos variables, u y v, y un número cualquiera, lambda.",
    "2_la_u_y_la_ve": "Toma dos variables, la u y la ve, y un número cualquiera, lambda.",
    "3_u_y_ve": "Toma dos variables, u y ve, y un número cualquiera, lambda.",
    "4_u_coma_ve": "Toma dos variables, que llamaremos u, ve, y un número cualquiera, lambda.",
    "5_u_con_ve": "Toma dos variables, u con ve, y un número cualquiera, lambda.",
    "6_primera_segunda": "Toma dos variables, la u y la ve, y un número cualquiera, que llamaremos lambda.",
}
NUMEROS = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho"]

if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for nombre, v in VARIANTES.items():
        sintetizar_mp3(FRASE.format(v), SALIDA / f"{nombre}.mp3")
        print("listo", nombre, "<-", v)
    texto = " ".join(f"Opción {NUMEROS[i]}: {FRASE.format(v)}" for i, v in enumerate(VARIANTES.values()))
    sintetizar_mp3(texto, SALIDA / "u_ve.mp3")
    print("listo u_ve.mp3")
