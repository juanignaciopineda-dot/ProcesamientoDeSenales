"""Tercera tanda de «Fourier»: en vez de grafías, la pronunciación exacta con
fonemas (SSML <phoneme>, alfabeto IPA) y un par de grafías que faltaban.

Uso:
    python probar_fourier_ipa.py
Deja los mp3 en voces_prueba/fourier3/ (numerados: el usuario elige un número).
Solo funciona con Azure Speech (edge-tts no acepta SSML).
"""
import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import (AzureSpeechService, ENV_CLAVE_AZURE, ENV_REGION_AZURE,  # noqa: E402
                       VOZ_POR_DEFECTO)

SALIDA = Path(__file__).parent / "fourier3"
FRASE = "Eso es la transformada de {}, y el dibujo de cuánto hay de cada frecuencia es el espectro."


def ipa(fonemas: str) -> str:
    return f'<phoneme alphabet="ipa" ph="{fonemas}">Fourier</phoneme>'


# nombre del mp3 -> lo que va en el lugar de «Fourier» (SSML o texto)
VARIANTES = {
    "1_ipa_furié": ipa("fuˈɾje"),          # a la francesa, erre suave, sin erre final
    "2_ipa_furiér": ipa("fuˈɾjeɾ"),        # con erre final
    "3_ipa_fúrier": ipa("ˈfuɾjeɾ"),        # acento en la u
    "4_ipa_fu_ri_é": ipa("fu.ɾiˈe"),       # en tres sílabas: fu-ri-é
    "5_ipa_fu_ri_ér": ipa("fu.ɾiˈeɾ"),     # tres sílabas con erre final
    "6_ipa_furrié": ipa("fuˈrje"),         # erre fuerte
    "7_fúrier": "Fúrier",                  # grafía, acento en la u
    "8_furi_é": "Furi-é",                  # grafía con guion
}


def main() -> None:
    import azure.cognitiveservices.speech as speechsdk

    SALIDA.mkdir(exist_ok=True)
    servicio = AzureSpeechService(voice=VOZ_POR_DEFECTO, cache_dir=str(SALIDA))
    config = speechsdk.SpeechConfig(subscription=os.environ[ENV_CLAVE_AZURE],
                                    region=os.environ[ENV_REGION_AZURE])
    config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat[servicio.FORMATO])
    sintetizador = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=None)
    antes, despues = (escape(t) for t in FRASE.split("{}"))
    for nombre, variante in VARIANTES.items():
        medio = variante if variante.startswith("<") else escape(variante)
        ssml = (
            '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            f'xml:lang="{servicio.voice[:5]}"><voice name="{servicio.voice}">'
            f'<prosody rate="{servicio.rate}" pitch="{servicio.pitch}">{antes}{medio}{despues}</prosody>'
            '</voice></speak>'
        )
        resultado = sintetizador.speak_ssml_async(ssml).get()
        if resultado.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"  FALLÓ: {nombre}  ({resultado.cancellation_details.error_details})")
            continue
        (SALIDA / f"{nombre}.mp3").write_bytes(resultado.audio_data)
        print(f"  listo: {nombre}.mp3")


if __name__ == "__main__":
    main()
