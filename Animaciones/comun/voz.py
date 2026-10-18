"""Servicio de voz para manim-voiceover, y la voz fija de todo el curso.

manim-voiceover no trae un servicio para edge-tts "de fábrica" en la versión
instalada (0.4.0) — sólo Azure, gTTS, ElevenLabs, OpenAI, Gemini y pyttsx3.
Edge-tts es gratis, no pide clave y da mejor calidad que gTTS, así que se
implementa acá un `EdgeTTSService` mínimo siguiendo el mismo patrón que
`manim_voiceover.services.gtts.GTTSService`.

Para cambiar de voz o de motor en TODO el curso, se toca sólo este archivo.
"""
from __future__ import annotations

import asyncio
import os
import time
from pathlib import Path
from xml.sax.saxutils import escape

import edge_tts
from dotenv import load_dotenv
from manim_voiceover._typing import VoiceoverData, WordBoundary
from manim_voiceover.helper import remove_bookmarks
from manim_voiceover.services.base import PathLike, SpeechService, initialize_speech_service, path_to_string

from comun.pronunciacion import con_fonemas, fonemas_en

# ------------------------------------------------------------------------
# La voz elegida a oído entre 7 candidatas gratuitas de edge-tts
# (ver voces_prueba/probar_voces.py). Cambiar acá alcanza para todo el curso.
VOZ_POR_DEFECTO = "es-ES-XimenaNeural"
# Un poco más lenta que la natural: es una clase, y ayuda a llegar a ~10 min
# por episodio sin agregar texto. Cambiarla vuelve a sintetizar todo el audio.
VELOCIDAD = "-5%"

# Azure Speech (servicio oficial, plan gratuito F0): la clave y la región se
# leen de variables de entorno o de `Animaciones/.env` (que no va al repo).
# Si están, se usa Azure; si no, edge-tts.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
ENV_CLAVE_AZURE = "AZURE_SUBSCRIPTION_KEY"
ENV_REGION_AZURE = "AZURE_SERVICE_REGION"


class EdgeTTSService(SpeechService):
    """SpeechService para Microsoft Edge TTS (voces neuronales gratuitas),
    usando la librería `edge-tts`. No requiere API key.
    """

    def __init__(self, voice: str = VOZ_POR_DEFECTO, rate: str = VELOCIDAD,
                 pitch: str = "+0Hz", **kwargs: object) -> None:
        """
        Args:
            voice: nombre de la voz de edge-tts (ej. "es-ES-XimenaNeural").
                Listar todas con `edge-tts --list-voices`.
            rate: ajuste de velocidad relativo, ej. "-10%" para más lento.
            pitch: ajuste de tono relativo, ej. "+2Hz".
        """
        self.voice = voice
        self.rate = rate
        self.pitch = pitch
        initialize_speech_service(self, kwargs)

    def generate_from_text(
        self,
        text: str,
        cache_dir: PathLike | None = None,
        path: PathLike | None = None,
        **kwargs: object,
    ) -> VoiceoverData:
        """"""
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_text = remove_bookmarks(text)
        input_data = self._datos_edge(input_text)

        cached_result = self._del_cache(input_data, text, cache_dir)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_audio_basename(input_data) + ".mp3"
        else:
            audio_path = path_to_string(path)

        destino = Path(cache_dir) / audio_path
        word_boundaries = asyncio.run(self._sintetizar(input_text, destino))

        json_dict: VoiceoverData = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }
        if word_boundaries:
            json_dict["word_boundaries"] = word_boundaries

        return json_dict

    def _datos_edge(self, input_text: str) -> dict:
        return {
            "input_text": input_text,
            "service": "edge-tts",
            "config": {"voice": self.voice, "rate": self.rate, "pitch": self.pitch,
                       "boundary": "word"},
        }

    def _del_cache(self, input_data: dict, text: str, cache_dir: PathLike) -> VoiceoverData | None:
        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            # El caché se indexa por el texto SIN marcas (el audio no depende
            # de ellas), pero las marcas hay que tomarlas del texto actual: si
            # no, un momento agregado al guion no existiría para el tracker.
            cached_result["input_text"] = text
            _desde_el_principio(cached_result.get("word_boundaries"))
        return cached_result

    async def _sintetizar(self, texto: str, destino: Path) -> list[WordBoundary]:
        # edge-tts 7 manda por defecto límites de ORACIÓN; los de palabra hay
        # que pedirlos. Sin ellos las marcas del guion no se pueden ubicar.
        comunicador = edge_tts.Communicate(texto, self.voice, rate=self.rate,
                                           pitch=self.pitch, boundary="WordBoundary")
        palabras: list[tuple[str, int, int]] = []
        with open(destino, "wb") as archivo:
            async for chunk in comunicador.stream():
                if chunk["type"] == "audio":
                    archivo.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    palabras.append((chunk["text"], chunk["offset"], chunk["duration"]))
        return _ubicar_palabras(texto, palabras)


def _ubicar_palabras(texto: str, palabras: list[tuple[str, int, int]]) -> list[WordBoundary]:
    """Arma los límites de palabra a partir de (palabra, offset, duración), con
    offset y duración en unidades de 100 ns (la resolución de manim-voiceover).

    El TTS no dice de forma fiable en qué posición del texto está cada
    palabra: se la busca en orden a partir de la anterior. Si el TTS la
    normalizó distinto y no aparece, se omite (el interpolador de
    manim-voiceover cubre el hueco)."""
    word_boundaries: list[WordBoundary] = []
    cursor = 0
    for palabra, offset, duracion in palabras:
        pos = texto.find(palabra, cursor)
        if pos == -1:
            continue
        cursor = pos + len(palabra)
        word_boundaries.append({
            "audio_offset": offset,
            "duration_milliseconds": duracion // 10_000,
            "text_offset": pos,
            "word_length": len(palabra),
            "text": palabra,
            "boundary_type": "Word",
        })
    _desde_el_principio(word_boundaries)
    return word_boundaries


def _desde_el_principio(word_boundaries: list[WordBoundary] | None) -> None:
    """Si el texto empieza con un signo («¿Qué…», «"Hola…»), la primera palabra
    queda en el offset 1 y una marca al principio del bloque (offset 0) cae
    fuera del rango del interpolador de manim-voiceover, que entonces la manda
    al FINAL del audio. Se ancla la primera palabra al offset 0."""
    if word_boundaries and word_boundaries[0]["text_offset"] > 0:
        word_boundaries[0]["text_offset"] = 0


class AzureSpeechService(EdgeTTSService):
    """La misma voz por el servicio oficial, Azure Speech (plan gratuito F0).

    edge-tts es un acceso no oficial a estas voces y se cae cuando Microsoft
    cambia su token (403). El audio que edge-tts ya dejó en caché se
    reutiliza: solo lo nuevo se sintetiza por Azure, con otra clave de caché
    ("azure-speech")."""

    # El mismo formato que entrega edge-tts, para que todo el curso suene igual.
    FORMATO = "Audio24Khz48KBitRateMonoMp3"

    def generate_from_text(self, text, cache_dir=None, path=None, **kwargs):
        if cache_dir is None:
            cache_dir = self.cache_dir
        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "azure-speech",
                      "config": {"voice": self.voice, "rate": self.rate, "pitch": self.pitch}}
        # Un bloque con palabras dichas por fonemas no vale con el audio viejo
        # (ni con el de edge-tts): los fonemas entran en la clave del caché.
        fonemas = fonemas_en(input_text)
        if fonemas:
            input_data["config"]["fonemas"] = fonemas
        for datos in ((input_data,) if fonemas else (self._datos_edge(input_text), input_data)):
            cached = self._del_cache(datos, text, cache_dir)
            if cached is not None:
                return cached

        audio_path = self.get_audio_basename(input_data) + ".mp3" if path is None else path_to_string(path)
        word_boundaries = self._sintetizar_azure(input_text, Path(cache_dir) / audio_path)
        json_dict: VoiceoverData = {"input_text": text, "input_data": input_data,
                                    "original_audio": audio_path}
        if word_boundaries:
            json_dict["word_boundaries"] = word_boundaries
        return json_dict

    def _sintetizar_azure(self, texto: str, destino: Path) -> list[WordBoundary]:
        import azure.cognitiveservices.speech as speechsdk

        config = speechsdk.SpeechConfig(subscription=os.environ[ENV_CLAVE_AZURE],
                                        region=os.environ[ENV_REGION_AZURE])
        config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat[self.FORMATO])
        # audio_config=None: el audio queda en memoria (no suena por el altavoz).
        sintetizador = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=None)

        eventos = []
        sintetizador.synthesis_word_boundary.connect(eventos.append)
        ssml = (
            '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            f'xml:lang="{self.voice[:5]}"><voice name="{self.voice}">'
            f'<prosody rate="{self.rate}" pitch="{self.pitch}">{con_fonemas(escape(texto))}</prosody>'
            '</voice></speak>'
        )
        # El plan gratuito limita las peticiones por minuto: con varios renders
        # a la vez puede responder 429. Se espera y se reintenta.
        for intento in range(6):
            eventos.clear()
            resultado = sintetizador.speak_ssml_async(ssml).get()
            if resultado.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                break
            detalle = resultado.cancellation_details
            if intento < 5 and any(s in str(detalle.error_details) for s in ("429", "Too many", "Too Many")):
                time.sleep(15)
                continue
            raise RuntimeError(f"Azure Speech no sintetizó el bloque ({detalle.reason}): "
                               f"{detalle.error_details}. Revisar {ENV_CLAVE_AZURE} y "
                               f"{ENV_REGION_AZURE} (variables de entorno o Animaciones/.env).")
        destino.write_bytes(resultado.audio_data)

        # Los eventos traen también la puntuación, y llegan desde otro hilo.
        palabras = sorted(
            (e.audio_offset, e.text, int(e.duration.total_seconds() * 1e7)) for e in eventos
            if e.boundary_type == speechsdk.SpeechSynthesisBoundaryType.Word)
        return _ubicar_palabras(texto, [(t, o, d) for o, t, d in palabras])


class SinRedService(EdgeTTSService):
    """SOLO PARA REVISAR IMÁGENES cuando edge-tts no responde (403 o sin internet).

    Con `CURSO_VOZ_SIN_RED=1` genera audio MUDO con tiempos de palabra
    estimados (~14 caracteres por segundo). Sirve para renderizar y revisar
    animaciones; no es la voz ni da el ritmo real. Usa otra clave de caché
    ("edge-tts-sin-red"), así que nunca se confunde con la voz verdadera: al
    volver edge-tts, el render final sintetiza todo de nuevo."""

    CARACTERES_POR_SEGUNDO = 14.0

    def generate_from_text(self, text, cache_dir=None, path=None, **kwargs):
        import re
        import subprocess
        if cache_dir is None:
            cache_dir = self.cache_dir
        input_text = remove_bookmarks(text)
        input_data = {"input_text": input_text, "service": "edge-tts-sin-red",
                      "config": {"voice": self.voice, "rate": self.rate}}
        cached = self.get_cached_result(input_data, cache_dir)
        if cached is not None:
            cached["input_text"] = text
            return cached
        audio_path = (self.get_audio_basename(input_data) if path is None else path_to_string(path)) + ".mp3"
        destino = Path(cache_dir) / audio_path
        limites, t = [], 0.0
        for m in re.finditer(r"\S+", input_text):
            dur = max(0.12, len(m.group()) / self.CARACTERES_POR_SEGUNDO) + (0.18 if m.group()[-1] in ".,:;?!" else 0.0)
            limites.append({"audio_offset": int(t * 1e7), "duration_milliseconds": int(dur * 1000),
                            "text_offset": m.start(), "word_length": len(m.group()),
                            "text": m.group(), "boundary_type": "Word"})
            t += dur
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                        "-t", f"{t + 0.3:.2f}", "-q:a", "9", str(destino)], check=True)
        return {"input_text": text, "input_data": input_data, "original_audio": audio_path,
                "word_boundaries": limites}


def sintetizar_mp3(texto: str, destino: PathLike, voz: str = VOZ_POR_DEFECTO) -> None:
    """Un mp3 suelto con el motor de voz del curso, sin marcas ni caché
    (para las pruebas de pronunciación de `voces_prueba/`)."""
    destino = Path(destino)
    con_azure = os.environ.get(ENV_CLAVE_AZURE) and os.environ.get(ENV_REGION_AZURE)
    servicio = (AzureSpeechService if con_azure else EdgeTTSService)(voice=voz, cache_dir=str(destino.parent))
    if con_azure:
        servicio._sintetizar_azure(texto, destino)
    else:
        asyncio.run(servicio._sintetizar(texto, destino))


def servicio_voz(**kwargs) -> EdgeTTSService:
    """Fábrica que usan todas las escenas: `self.set_speech_service(servicio_voz())`.

    Cambiar de motor de voz para TODO el curso es reemplazar acá qué se
    devuelve (por ejemplo, por un `ChatterboxService` local del día que haya
    GPU), sin tocar ninguna escena.
    """
    if os.environ.get("CURSO_VOZ_SIN_RED") == "1":
        return SinRedService(**kwargs)
    if os.environ.get(ENV_CLAVE_AZURE) and os.environ.get(ENV_REGION_AZURE):
        return AzureSpeechService(**kwargs)
    return EdgeTTSService(**kwargs)
