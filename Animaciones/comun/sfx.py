"""Efectos de sonido sintetizados con numpy: nada que descargar ni licenciar.

`ruta(nombre)` devuelve el .wav (lo genera la primera vez en Animaciones/sfx/).
Se usan desde las escenas con `self.sfx("pop")`.

Efectos disponibles: pop, whoosh, tick, tecla, impacto, alarma, exito, error, latido.
Para agregar uno: escribir una función que devuelva un array float en [-1, 1]
a 44100 Hz y registrarla en EFECTOS.
"""
from __future__ import annotations

import wave
from pathlib import Path

import numpy as np

SR = 44100
CARPETA = Path(__file__).resolve().parent.parent / "sfx"


def _t(dur: float) -> np.ndarray:
    return np.linspace(0, dur, int(SR * dur), endpoint=False)


def _env(n: int, ataque: float = 0.005, caida: float = 8.0) -> np.ndarray:
    t = np.arange(n) / SR
    a = np.clip(t / ataque, 0, 1) if ataque > 0 else np.ones(n)
    return a * np.exp(-caida * t)


def _ruido_filtrado(n: int, suavizado: int) -> np.ndarray:
    rng = np.random.default_rng(7)
    r = rng.normal(0, 1, n)
    k = np.ones(suavizado) / suavizado
    return np.convolve(r, k, mode="same")


def pop() -> np.ndarray:
    t = _t(0.12)
    f = 900 * np.exp(-18 * t) + 300          # barrido hacia abajo: "blup"
    fase = 2 * np.pi * np.cumsum(f) / SR
    return 0.8 * np.sin(fase) * _env(len(t), 0.002, 30)


def whoosh() -> np.ndarray:
    t = _t(0.45)
    r = _ruido_filtrado(len(t), 12)
    campana = np.sin(np.pi * t / t[-1]) ** 2
    mod = 0.5 + 0.5 * np.sin(2 * np.pi * 3 * t)
    return 0.5 * r / np.abs(r).max() * campana * mod


def tick() -> np.ndarray:
    t = _t(0.04)
    return 0.6 * np.sin(2 * np.pi * 2200 * t) * _env(len(t), 0.0005, 120)


def tecla() -> np.ndarray:
    t = _t(0.05)
    r = _ruido_filtrado(len(t), 3)
    return 0.6 * r / np.abs(r).max() * _env(len(t), 0.0005, 90)


def impacto() -> np.ndarray:
    t = _t(0.7)
    grave = np.sin(2 * np.pi * (60 + 40 * np.exp(-8 * t)) * t)
    r = _ruido_filtrado(len(t), 30)
    return 0.9 * (0.8 * grave + 0.3 * r / np.abs(r).max()) * _env(len(t), 0.002, 6)


def alarma() -> np.ndarray:
    t = _t(0.8)
    f = np.where((t * 5).astype(int) % 2 == 0, 880, 660)
    fase = 2 * np.pi * np.cumsum(f) / SR
    return 0.35 * np.sign(np.sin(fase)) * _env(len(t), 0.01, 1.5)


def exito() -> np.ndarray:
    notas = [523.25, 659.25, 783.99]          # do-mi-sol
    partes = []
    for i, f in enumerate(notas):
        t = _t(0.11 if i < 2 else 0.3)
        partes.append(0.45 * np.sin(2 * np.pi * f * t) * _env(len(t), 0.003, 10))
    return np.concatenate(partes)


def error() -> np.ndarray:
    t = _t(0.35)
    onda = np.sin(2 * np.pi * 140 * t) + 0.5 * np.sin(2 * np.pi * 147 * t)
    return 0.45 * onda * _env(len(t), 0.005, 5)


def latido() -> np.ndarray:
    def golpe(dur):
        t = _t(dur)
        return np.sin(2 * np.pi * 55 * t) * _env(len(t), 0.003, 25)
    silencio = np.zeros(int(SR * 0.12))
    return 0.9 * np.concatenate([golpe(0.15), silencio, 0.7 * golpe(0.15)])


EFECTOS = {
    "pop": pop, "whoosh": whoosh, "tick": tick, "tecla": tecla, "impacto": impacto,
    "alarma": alarma, "exito": exito, "error": error, "latido": latido,
}


def _guardar(nombre: str, datos: np.ndarray) -> Path:
    CARPETA.mkdir(exist_ok=True)
    destino = CARPETA / f"{nombre}.wav"
    pcm = (np.clip(datos, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(destino), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    return destino


def ruta(nombre: str) -> Path:
    if nombre not in EFECTOS:
        raise KeyError(f"efecto '{nombre}' inexistente. Hay: {sorted(EFECTOS)}")
    destino = CARPETA / f"{nombre}.wav"
    if not destino.exists():
        _guardar(nombre, EFECTOS[nombre]())
    return destino


if __name__ == "__main__":
    for n in EFECTOS:
        print(ruta(n))
