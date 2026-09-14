"""Interactivo - Cuánto sirve medir X: todo depende de rho.

Mové rho. La nube se estira, la recta de regresión gira, y la barra de
error cae de sigma_Y^2 (sin medir) a sigma_Y^2(1-rho^2) (midiendo). El
número verde es la fracción de varianza que la medición explica: rho^2.

    python i05_rho.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

N = 300
_rng = np.random.default_rng(31)
Z1 = _rng.normal(0, 1, N)
Z2 = _rng.normal(0, 1, N)

fig = plt.figure(figsize=(11.8, 5.8))
fig.suptitle(r"¿Cuánto sirve medir X?    LMMSE $= \sigma_Y^2\,(1-\rho^2)$",
             color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.07, 0.28, 0.45, 0.60])
ax_bar = fig.add_axes([0.62, 0.28, 0.30, 0.60])


def dibujar(rho):
    ys = rho * Z1 + np.sqrt(max(0.0, 1 - rho ** 2)) * Z2

    ax.clear()
    ax.scatter(Z1, ys, s=9, color=AZUL, alpha=0.5)
    xs = np.array([-3.4, 3.4])
    ax.plot(xs, rho * xs, color=VERDE, lw=2.6)
    ax.set_xlim(-3.4, 3.4); ax.set_ylim(-3.4, 3.4)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title(f"$\\rho$ = {rho:+.2f}", color=AMBAR, pad=8)
    limpiar(ax)

    ax_bar.clear()
    ax_bar.bar([0], [1.0], width=0.55, color=AZUL, alpha=0.9)
    ax_bar.bar([1], [1 - rho ** 2], width=0.55, color=ROJO, alpha=0.9)
    ax_bar.set_xticks([0, 1])
    ax_bar.set_xticklabels(["sin medir\n$\\sigma_Y^2$", "midiendo X\nLMMSE"],
                           fontsize=9)
    ax_bar.set_ylim(0, 1.32); ax_bar.set_yticks([0, 0.5, 1])
    limpiar(ax_bar, ejes=("left",))
    ax_bar.text(1, 1 - rho ** 2 + 0.04, f"$-{100*rho**2:.0f}\\%$",
                ha="center", va="bottom", color=VERDE, fontsize=11)
    ax_bar.text(0.5, 1.22, f"$\\rho^2$ = {rho**2:.2f}  de la varianza de Y",
                ha="center", color=INK, fontsize=9.5)
    fig.canvas.draw_idle()


s_rho = estilo_slider(Slider(eje_slider(fig, 0.25, 0.10, 0.5),
                             r"$\rho$", -0.98, 0.98, valinit=0.0, valfmt="%.2f"))
s_rho.on_changed(dibujar)

pie(fig, "rho = 0: la nube es redonda, medir X no sirve. |rho| = 1: la "
         "relación es exacta, el error se va a cero. Lo que cuenta es rho².")
dibujar(s_rho.val)
plt.show()
