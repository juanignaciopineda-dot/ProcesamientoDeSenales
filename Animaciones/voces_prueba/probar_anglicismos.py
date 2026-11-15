"""Variantes de pronunciación de anglicismos del guion, para elegir de oído.

Genera un mp3 por palabra en voces_prueba/anglicismos/, con todas sus
variantes numeradas dentro de la misma frase. La elegida va a
comun/pronunciacion.py.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import sintetizar_mp3  # noqa: E402

SALIDA = Path(__file__).parent / "anglicismos"

# palabra: (frase con {} donde va la variante, [variantes])
# Siglas, anglicismos y letras griegas de la materia. Se genera, se manda el mp3
# y el usuario elige un número; la elegida va a comun/pronunciacion.py.
CASOS = {
    "roc": ("la curva {} resume el detector", ["ROC", "R O C", "erre o ce", "roc"]),
    "psd": ("la {} de la señal", ["PSD", "P S D", "pe ese de"]),
    "wss": ("un proceso {}", ["WSS", "W S S", "uve doble ese ese"]),
    "lti": ("un sistema {}", ["LTI", "L T I", "ele te i"]),
    "fir": ("un filtro {}", ["FIR", "F I R", "fir", "efe i erre"]),
    "mmse": ("el estimador {}", ["MMSE", "M M S E", "eme eme ese e"]),
    "lmmse": ("el estimador {}", ["LMMSE", "L M M S E", "ele eme eme ese e"]),
    "map": ("la regla {}", ["MAP", "M A P", "map", "eme a pe"]),
    "snr": ("la {} es de diez decibelios", ["SNR", "S N R", "ese ene erre"]),
    "griegas": ("la letra {}", ["tau", "omega", "sigma", "rho", "mu", "lambda", "theta"]),
}

NUMEROS = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho"]


def main() -> None:
    SALIDA.mkdir(exist_ok=True)
    elegidas = sys.argv[1:] or list(CASOS)  # uso: probar_anglicismos.py [palabra ...]
    for palabra, (frase, variantes) in CASOS.items():
        if palabra not in elegidas:
            continue
        texto = " ".join(f"Opción {NUMEROS[i]}: {frase.format(v)}." for i, v in enumerate(variantes))
        sintetizar_mp3(texto, SALIDA / f"{palabra}.mp3")
        print(f"{palabra}.mp3  <-  " + " | ".join(f"{i + 1}) {v}" for i, v in enumerate(variantes)))


if __name__ == "__main__":
    main()
