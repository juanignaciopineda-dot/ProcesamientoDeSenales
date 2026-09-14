"""Interactivo - Resolución contra varianza, con un registro fijo.

Dos tonos separados por Delta. Mové la separación y T: cuando Delta cae
por debajo de pi/T los picos se funden. Y como el registro total es fijo,
subir T baja M y el estimado se pone más ruidoso.

    python i07_resolucion.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

REGISTRO = 4096
OM0 = 1.20          # frecuencia central de los dos tonos
SNR = 6.0
_rng = np.random.default_rng(11)


ZP = 8      # zero-padding: interpola la DTFT para que la curva se vea
            # suave. NO mejora la resolución, que sigue siendo ~pi/T.


def estimar(sep, T, M):
    nfft = T * ZP
    acum = np.zeros(nfft // 2)
    vent = np.hanning(T)
    for _ in range(M):
        n = np.arange(T)
        fase = _rng.uniform(0, 2 * np.pi, 2)
        x = (np.cos((OM0 - sep / 2) * n + fase[0])
             + np.cos((OM0 + sep / 2) * n + fase[1]))
        x = x * SNR / np.sqrt(2) + _rng.normal(0, 1, T)
        X = np.fft.fft(x * vent, nfft)
        acum += (np.abs(X) ** 2 / T)[: nfft // 2]
    return acum / M


fig = plt.figure(figsize=(11.8, 6.2))
fig.suptitle("Resolución contra varianza: con un registro fijo no se puede todo",
             color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.09, 0.34, 0.86, 0.52])


def dibujar(*_):
    sep = s_sep.val
    T = int(2 ** round(s_T.val))
    M = max(1, REGISTRO // T)
    est = estimar(sep, T, M)
    w = np.arange(len(est)) / len(est) * np.pi

    ax.clear()
    ax.plot(w, est, color=AMBAR, lw=1.7)
    for w0 in (OM0 - sep / 2, OM0 + sep / 2):
        ax.axvline(w0, color=VERDE, lw=1.6, ls=(0, (4, 3)), alpha=0.8)
    ax.set_xlim(max(0, OM0 - 0.55), OM0 + 0.55)
    ax.set_ylim(0, max(est.max() * 1.15, 1))
    ax.set_xlabel(r"$\Omega$"); ax.set_ylabel("periodograma promediado")
    limpiar(ax)

    res = np.pi / T
    resuelve = sep > res
    col = VERDE if resuelve else ROJO
    veredicto = "se resuelven" if resuelve else "NO se resuelven: se funden en uno"
    ax.text(0.015, 0.94, f"T = {T}   →   M = {M}   (registro de {REGISTRO})",
            transform=ax.transAxes, color=INK, fontsize=9.5)
    ax.text(0.015, 0.87,
            f"separación Δ = {sep:.4f}     resolución π/T = {res:.4f}",
            transform=ax.transAxes, color=AZUL, fontsize=9.5)
    ax.text(0.015, 0.79, veredicto, transform=ax.transAxes, color=col,
            fontsize=10.5, weight="bold")
    ax.text(0.985, 0.94, f"zero-padding ×{ZP}: interpola, no resuelve",
            transform=ax.transAxes, color=INK, fontsize=8.5, ha="right")
    fig.canvas.draw_idle()


s_sep = estilo_slider(Slider(eje_slider(fig, 0.18, 0.175, 0.60),
                             "separación Δ", 0.005, 0.35, valinit=0.10,
                             valfmt="%.4f"))
s_T = estilo_slider(Slider(eje_slider(fig, 0.18, 0.105, 0.60),
                           "T (largo, potencia de 2)", 5, 11, valinit=7,
                           valstep=1, valfmt="%d"))
s_sep.on_changed(dibujar)
s_T.on_changed(dibujar)

pie(fig, "Las líneas verdes marcan dónde están los tonos de verdad. Subí T "
         "hasta que se separen, y mirá lo que le pasa a M.")
dibujar()
plt.show()
