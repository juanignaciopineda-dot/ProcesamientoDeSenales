"""Interactivo - La regla MAP.

Mové los a priori y la separación entre hipótesis, y mirá cómo se corre el
umbral. Con p0 = p1 queda justo en el cruce; si una hipótesis se vuelve
más probable, el umbral se corre para exigirle más evidencia a la otra.

    python i02_map.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *

SIGMA = 1.0
R = np.linspace(-5, 9, 1400)


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


fig = plt.figure(figsize=(11.8, 6.0))
fig.suptitle("La regla MAP: decidir por la hipótesis más probable",
             color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.08, 0.36, 0.86, 0.52])


def dibujar(*_):
    p0, d = s_p0.val, s_d.val
    p1 = 1 - p0
    gam = d / 2 + SIGMA ** 2 * np.log(p0 / p1) / d if d > 0 else 0.0

    ax.clear()
    f0, f1 = p0 * g(R, 0), p1 * g(R, d)
    ax.plot(R, f0, color=AZUL, lw=2.6, label=r"$p_0\,f(r|H_0)$")
    ax.plot(R, f1, color=VERDE, lw=2.6, label=r"$p_1\,f(r|H_1)$")
    ax.fill_between(R, 0, f0, color=AZUL, alpha=0.12)
    ax.fill_between(R, 0, f1, color=VERDE, alpha=0.12)
    ax.axvline(gam, color=ROJO, lw=2.4, ls=(0, (4, 3)))

    ymax = max(f0.max(), f1.max()) * 1.25
    ax.set_xlim(-5, 9); ax.set_ylim(0, ymax)
    ax.set_xlabel("r"); ax.set_yticks([])
    ax.text(gam, ymax * 0.97, r"  $\gamma$", color=ROJO, fontsize=13,
            va="top")
    ax.text((-5 + gam) / 2, ymax * 0.88, "decido $H_0$", color=AZUL,
            fontsize=11, ha="center")
    ax.text((9 + gam) / 2, ymax * 0.88, "decido $H_1$", color=VERDE,
            fontsize=11, ha="center")
    ax.legend(loc="upper right", fontsize=10)
    limpiar(ax, ejes=("bottom",))

    pe = p0 * Q(gam / SIGMA) + p1 * (1 - Q((gam - d) / SIGMA))
    ax.text(0.02, 0.95, f"umbral γ = {gam:+.3f}", transform=ax.transAxes,
            color=ROJO, fontsize=10)
    ax.text(0.02, 0.88, f"$P_e$ mínimo = {pe:.4f}", transform=ax.transAxes,
            color=TXT, fontsize=10)
    fig.canvas.draw_idle()


s_p0 = estilo_slider(Slider(eje_slider(fig, 0.20, 0.155, 0.58),
                            r"$p_0$  (a priori de $H_0$)", 0.05, 0.95,
                            valinit=0.5, valfmt="%.2f"))
s_d = estilo_slider(Slider(eje_slider(fig, 0.20, 0.085, 0.58),
                           "separación entre $a_0$ y $a_1$  (SNR)", 0.3, 6.0,
                           valinit=2.6, valfmt="%.2f"))
s_p0.on_changed(dibujar)
s_d.on_changed(dibujar)

pie(fig, "El umbral MAP compara las densidades ESCALADAS por los a priori. "
         "Con p0 = p1 queda en el cruce de las dos curvas.")
dibujar()
plt.show()
