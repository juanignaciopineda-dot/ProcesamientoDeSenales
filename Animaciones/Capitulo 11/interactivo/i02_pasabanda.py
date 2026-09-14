"""Interactivo - La PSD como densidad: el filtro pasabanda.

Mové la banda y su ancho: el área sombreada es exactamente la potencia
esperada que el proceso tiene en esa banda.

    python i02_pasabanda.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

ALFA = 3.0
W = np.linspace(-12, 12, 3000)


def S(w):
    return 2 * ALFA / (ALFA ** 2 + w ** 2)


POT_TOTAL = np.trapezoid(S(W), W) / (2 * np.pi)

fig = plt.figure(figsize=(11.5, 6.0))
fig.suptitle("¿Por qué “densidad” espectral de potencia?", color=TXT,
             fontsize=13, y=0.965)

ax = fig.add_axes([0.09, 0.32, 0.62, 0.56])
ax_bar = fig.add_axes([0.80, 0.32, 0.07, 0.56])


def dibujar(w0, bw):
    ax.clear()
    ax.plot(W, S(W), color=AZUL, lw=2.6)
    ax.fill_between(W, 0, S(W), color=AZUL, alpha=0.10)

    pot = 0.0
    for signo in (+1, -1):
        a, b = signo * w0 - bw / 2, signo * w0 + bw / 2
        m = (W >= a) & (W <= b)
        ax.fill_between(W[m], 0, S(W[m]), color=AMBAR, alpha=0.75)
        pot += np.trapezoid(S(W[m]), W[m]) / (2 * np.pi)

    ax.axvline(w0, color=AMBAR, ls=(0, (3, 3)), lw=1.2)
    ax.axvline(-w0, color=AMBAR, ls=(0, (3, 3)), lw=1.2)
    ax.set_xlim(W[0], W[-1]); ax.set_ylim(-0.03, 0.78)
    ax.set_xlabel(r"$\omega$"); ax.set_yticks([])
    ax.set_title(r"$S_{xx}(j\omega)$", color=AZUL, pad=10)
    limpiar(ax, ejes=("bottom",))
    ax.text(0.015, 0.93, f"potencia en la banda = {pot:.4f}",
            transform=ax.transAxes, color=AMBAR, fontsize=10)
    ax.text(0.015, 0.85, f"potencia total = {POT_TOTAL:.4f}",
            transform=ax.transAxes, color=INK, fontsize=9)

    ax_bar.clear()
    ax_bar.bar([0], [pot], width=0.7, color=VERDE, alpha=0.9)
    ax_bar.set_ylim(0, POT_TOTAL * 1.05)
    ax_bar.set_xlim(-0.6, 0.6)
    ax_bar.set_xticks([])
    ax_bar.set_title(r"$E[y^2(t)]$", color=VERDE, fontsize=10, pad=10)
    limpiar(ax_bar, ejes=("left",))
    fig.canvas.draw_idle()


s_w0 = estilo_slider(Slider(eje_slider(fig, 0.18, 0.15, 0.55),
                            r"$\omega_0$", 0.0, 9.0, valinit=5.0, valfmt="%.2f"))
s_bw = estilo_slider(Slider(eje_slider(fig, 0.18, 0.08, 0.55),
                            "ancho de banda", 0.1, 4.0, valinit=1.5,
                            valfmt="%.2f"))
actualizar = lambda _: dibujar(s_w0.val, s_bw.val)
s_w0.on_changed(actualizar)
s_bw.on_changed(actualizar)

pie(fig, "El área de la franja ES la potencia esperada en esa banda, esté donde "
         "esté y sea todo lo angosta que quieras.")
dibujar(s_w0.val, s_bw.val)
plt.show()
