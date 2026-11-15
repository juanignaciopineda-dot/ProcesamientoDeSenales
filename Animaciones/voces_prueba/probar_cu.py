"""Prueba de la letra «cu» aislada (la función Q: «la función cu de equis»).

El texto «cu» tal cual se oye deletreado, «ce u» (Cap. 9, E2).

Uso:  python probar_cu.py
Deja los mp3 en voces_prueba/cu/ (numerados: el usuario elige un número).
Los fonemas solo funcionan con Azure Speech.
"""
import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from comun.voz import (AzureSpeechService, ENV_CLAVE_AZURE, ENV_REGION_AZURE,  # noqa: E402
                       VOZ_POR_DEFECTO)

SALIDA = Path(__file__).parent / "cu"
FRASE = "El área de la cola se llama función {} de equis. {} de uno, cero coma dieciséis."


def ipa(fonemas: str, txt: str = "cu") -> str:
    return f'<phoneme alphabet="ipa" ph="{fonemas}">{txt}</phoneme>'


VARIANTES = {
    "1_cu_actual": "cu",
    "2_cú": "cú",
    "3_ku": "ku",
    "4_kú": "kú",
    "5_ipa_ku": ipa("ˈku"),
    "6_la_cu": "la cu",
}


def main() -> None:
    import azure.cognitiveservices.speech as speechsdk

    SALIDA.mkdir(exist_ok=True)
    servicio = AzureSpeechService(voice=VOZ_POR_DEFECTO, cache_dir=str(SALIDA))
    config = speechsdk.SpeechConfig(subscription=os.environ[ENV_CLAVE_AZURE],
                                    region=os.environ[ENV_REGION_AZURE])
    config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat[servicio.FORMATO])
    sintetizador = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=None)
    partes = [escape(t) for t in FRASE.split("{}")]
    for nombre, variante in VARIANTES.items():
        medio = variante if variante.startswith("<") else escape(variante)
        segundo = medio[0].upper() + medio[1:] if not medio.startswith("<") else medio
        cuerpo = partes[0] + medio + partes[1] + segundo + partes[2]
        ssml = (
            '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            f'xml:lang="{servicio.voice[:5]}"><voice name="{servicio.voice}">'
            f'<prosody rate="{servicio.rate}" pitch="{servicio.pitch}">{cuerpo}</prosody>'
            '</voice></speak>'
        )
        r = sintetizador.speak_ssml_async(ssml).get()
        if r.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"  FALLÓ: {nombre}  ({r.cancellation_details.error_details})")
            continue
        (SALIDA / f"{nombre}.mp3").write_bytes(r.audio_data)
        print(f"  {nombre}.mp3")


if __name__ == "__main__":
    main()
