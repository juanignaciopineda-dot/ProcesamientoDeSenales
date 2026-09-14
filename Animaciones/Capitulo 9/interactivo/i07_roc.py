"""Interactivo - La curva ROC.

Mové la separación entre hipótesis (el SNR) y mirá cómo la curva ROC se
despega de la diagonal. Mové el umbral para ver el punto de operación
recorrer la curva. La ROC es la calidad del detector; el umbral solo dice
dónde te parás sobre ella.

    python i07_roc.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *

SIGMA = 1.0
R = np.linspace(-4, 9, 1000)


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


fig = plt.figure(figsize=(12.0, 6.0))
fig.suptitle("La curva ROC: el retrato completo del detector", color=TXT,
             fontsize=13, y=0.965)
ax_d = fig.add_axes([0.06, 0.34, 0.44, 0.52])
ax_r = fig.add_axes([0.60, 0.28, 0.36, 0.60])


def dibujar(*_):
    d, gam = s_d.val, s_gam.val
    pfa, pd = Q(gam / SIGMA), Q((gam - d) / SIGMA)

    ax_d.clear()
    ax_d.plot(R, g(R, 0), color=AZUL, lw=2.4, label=r"$f(r|H_0)$")
    ax_d.plot(R, g(R, d), color=VERDE, lw=2.4, label=r"$f(r|H_1)$")
    ax_d.fill_between(R, 0, g(R, 0), where=R >= gam, color=ROJO, alpha=0.55)
    ax_d.fill_between(R, 0, g(R, d), where=R >= gam, color=VERDE, alpha=0.28)
    ax_d.axvline(gam, color=ROJO, lw=2.2, ls=(0, (4, 3)))
    ax_d.set_xlim(R[0], R[-1]); ax_d.set_ylim(0, 0.45)
    ax_d.set_xlabel("r"); ax_d.set_yticks([])
    ax_d.legend(loc="upper right", fontsize=9.5)
    limpiar(ax_d, ejes=("bottom",))

    ax_r.clear()
    gs = np.linspace(-6, 10, 500)
    ax_r.plot([Q(x / SIGMA) for x in gs], [Q((x - d) / SIGMA) for x in gs],
              color=AMBAR, lw=2.6)
    ax_r.plot([0, 1], [0, 1], color=INK, lw=1.5, ls=(0, (4, 3)))
    ax_r.text(0.6, 0.5, "azar", color=INK, fontsize=9, rotation=34)
    ax_r.plot([pfa], [pd], "o", color=ROJO, ms=11)
    ax_r.set_xlim(0, 1); ax_r.set_ylim(0, 1.02)
    ax_r.set_xlabel(r"$P_{FA}$"); ax_r.set_ylabel(r"$P_D$")
    ax_r.set_xticks([0, 0.5, 1]); ax_r.set_yticks([0, 0.5, 1])
    limpiar(ax_r)

    # area bajo la ROC = probabilidad de acierto en 2AFC = Q(-d/sqrt(2))
    a_roc = Q(-d / sqrt(2))
    ax_r.text(0.5, 1.06, f"área bajo la ROC = {a_roc:.3f}",
              transform=ax_r.transAxes, ha="center", color=AMBAR, fontsize=10)
    ax_r.text(0.98, 0.06, f"$P_{{FA}}$ = {pfa:.3f}\n$P_D$ = {pd:.3f}",
              transform=ax_r.transAxes, ha="right", va="bottom", color=INK,
              fontsize=9)
    fig.canvas.draw_idle()


s_d = estilo_slider(Slider(eje_slider(fig, 0.25, 0.13, 0.5),
                           "separación (SNR)", 0.1, 5.0, valinit=2.0,
                           valfmt="%.2f"))
s_gam = estilo_slider(Slider(eje_slider(fig, 0.25, 0.065, 0.5),
                             "umbral γ", -3.0, 8.0, valinit=1.0, valfmt="%.2f"))
s_d.on_changed(dibujar)
s_gam.on_changed(dibujar)

pie(fig, "Cuanto más separadas las hipótesis, más se acerca la ROC a la "
         "esquina superior izquierda. El punto rojo es dónde elegís operar.")
dibujar()
plt.show()
