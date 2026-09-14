"""Interactivo - Sin medir nada, el mejor y-sombrero es la media.

Mové el candidato y-sombrero sobre la densidad de Y y mirá el error
cuadrático medio E[(Y - y)^2] = sigma^2 + (mu - y)^2. El mínimo está
exactamente en la media, y ahí el error vale sigma^2.

    python i01_mmse.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

MU, SD = 1.4, 1.15
YY = np.linspace(-3.5, 6.5, 600)

fig = plt.figure(figsize=(11.0, 5.6))
fig.suptitle("Estimar Y sin medir nada", color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.09, 0.30, 0.62, 0.58])
ax_bar = fig.add_axes([0.82, 0.30, 0.07, 0.58])

MSE_MAX = SD ** 2 + (MU - YY[0]) ** 2


def dibujar(yh):
    f = np.exp(-0.5 * ((YY - MU) / SD) ** 2) / (SD * np.sqrt(2 * np.pi))
    ax.clear()
    ax.plot(YY, f, color=AZUL, lw=2.6)
    ax.fill_between(YY, 0, f, color=AZUL, alpha=0.12)
    ax.axvline(yh, color=AMBAR, lw=2.5, ls=(0, (4, 3)))
    ax.axvline(MU, color=VERDE, lw=1.6, alpha=0.6)
    ax.text(MU, -0.045, r"$\mu_Y$", color=VERDE, ha="center", fontsize=11)
    ax.text(yh, 0.40, r"$\hat{y}$", color=AMBAR, ha="center", fontsize=12)
    ax.set_xlim(YY[0], YY[-1]); ax.set_ylim(-0.06, 0.42)
    ax.set_xlabel("y"); ax.set_yticks([])
    limpiar(ax, ejes=("bottom",))
    ax.text(0.02, 0.95, r"$f_Y(y)$", transform=ax.transAxes, color=AZUL,
            fontsize=11)

    mse = SD ** 2 + (MU - yh) ** 2
    ax_bar.clear()
    ax_bar.bar([0], [mse], width=0.7, color=ROJO, alpha=0.9)
    ax_bar.axhline(SD ** 2, color=VERDE, lw=2, ls=(0, (4, 3)))
    ax_bar.set_ylim(0, MSE_MAX * 1.05); ax_bar.set_xlim(-0.6, 0.6)
    ax_bar.set_xticks([])
    ax_bar.set_title(r"$E[(Y-\hat{y})^2]$", color=ROJO, fontsize=9, pad=8)
    limpiar(ax_bar, ejes=("left",))
    ax_bar.text(0, mse + MSE_MAX * 0.03, f"{mse:.2f}", ha="center", color=ROJO,
                fontsize=10)
    ax_bar.text(0.7, SD ** 2, r"$\sigma_Y^2$", va="center", color=VERDE,
                fontsize=10)
    fig.canvas.draw_idle()


s_yh = estilo_slider(Slider(eje_slider(fig, 0.20, 0.11, 0.55),
                            r"$\hat{y}$", YY[0] + 0.5, YY[-1] - 0.5,
                            valinit=-1.5, valfmt="%.2f"))
s_yh.on_changed(dibujar)

pie(fig, "El error nunca baja de sigma_Y^2. Ese es el precio de no poder "
         "medir nada: te comés la varianza entera.")
dibujar(s_yh.val)
plt.show()
