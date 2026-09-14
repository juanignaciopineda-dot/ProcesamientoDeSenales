"""Interactivo - Filtrado LTI de procesos WSS.

S_yy(jw) = |H(jw)|^2 S_xx(jw). Mové el corte del pasabajos y el ancho del
espectro de entrada, y mirá como se forma S_yy como producto punto a punto.
El area de cada espectro (dividida por 2 pi) es la potencia media.

    python i07_filtrado.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

W = np.linspace(-12, 12, 2000)

fig = plt.figure(figsize=(12, 5.6))
fig.suptitle(r"Filtrado LTI:  $S_{yy}(j\omega) = |H(j\omega)|^2\, "
             r"S_{xx}(j\omega)$", color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.07, 0.30, 0.88, 0.56])


def dibujar(wc, ax_in):
    ax.clear()
    Sxx = 2 * ax_in / (ax_in ** 2 + W ** 2)
    H2 = wc ** 2 / (wc ** 2 + W ** 2)
    Syy = H2 * Sxx

    ax.plot(W, Sxx, color=AZUL, lw=2.0, label=r"$S_{xx}(j\omega)$")
    ax.plot(W, H2 * Sxx.max(), color=AMBAR, lw=1.8, ls="--",
            label=r"$|H(j\omega)|^2$ (escalado)")
    ax.plot(W, Syy, color=VERDE, lw=2.8, label=r"$S_{yy}(j\omega)$")
    ax.fill_between(W, 0, Syy, color=VERDE, alpha=0.18)
    ax.axvline(wc, color=AMBAR, lw=1.0, ls=":")
    ax.axvline(-wc, color=AMBAR, lw=1.0, ls=":")

    ax.set_xlabel(r"$\omega$")
    ax.set_xlim(-12, 12)
    ax.set_ylim(0, Sxx.max() * 1.15)
    ax.legend(loc="upper right", fontsize=9)

    pin = np.trapezoid(Sxx, W) / (2 * np.pi)
    pout = np.trapezoid(Syy, W) / (2 * np.pi)
    ax.text(0.01, 0.95, f"potencia entrada  = {pin:.3f}\n"
            f"potencia salida   = {pout:.3f}\n"
            f"fracción que pasa = {pout / pin:.0%}",
            transform=ax.transAxes, color=INK, fontsize=10, va="top",
            family="monospace")
    limpiar(ax)
    fig.canvas.draw_idle()


s_wc = estilo_slider(Slider(eje_slider(fig, 0.28, 0.15, 0.50),
                            r"corte del filtro $\omega_c$", 0.5, 8.0,
                            valinit=2.0, valfmt="%.2f"))
s_ax = estilo_slider(Slider(eje_slider(fig, 0.28, 0.08, 0.50),
                            "ancho del espectro de entrada", 0.4, 6.0,
                            valinit=1.5, valfmt="%.2f"))
s_wc.on_changed(lambda v: dibujar(s_wc.val, s_ax.val))
s_ax.on_changed(lambda v: dibujar(s_wc.val, s_ax.val))

pie(fig, "S_yy = |H|^2 S_xx es idéntico a cómo se filtra la densidad "
         "espectral de energía: por eso S_xx se llama PSD.")
dibujar(s_wc.val, s_ax.val)
plt.show()
