"""Interactivo - Conjunta y marginales.

Mové rho y los desvíos: la conjunta cambia de forma pero las marginales
se quedan quietas mientras no toques sigma. Es la demostración visual de
que las marginales NO determinan la conjunta.

    python i06_conjunta.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

G = np.linspace(-3.6, 3.6, 220)
XX, YY = np.meshgrid(G, G)
_rng = np.random.default_rng(9)
_A = _rng.normal(0, 1, 420)
_B = _rng.normal(0, 1, 420)

fig = plt.figure(figsize=(11.4, 6.6))
fig.suptitle("La conjunta y sus marginales", color=TXT, fontsize=13, y=0.965)

# conjunta al centro, con cada marginal pegada a su eje
ax_j = fig.add_axes([0.30, 0.42, 0.40, 0.46])
ax_mx = fig.add_axes([0.30, 0.285, 0.40, 0.12])
ax_my = fig.add_axes([0.715, 0.42, 0.12, 0.46])


def dibujar(*_):
    rho, sx, sy = s_rho.val, s_sx.val, s_sy.val
    r = np.clip(rho, -0.985, 0.985)

    # ---- conjunta: curvas de nivel y una muestra
    q = (XX ** 2 / sx ** 2 - 2 * r * XX * YY / (sx * sy)
         + YY ** 2 / sy ** 2) / (1 - r ** 2)
    Z = np.exp(-q / 2) / (2 * np.pi * sx * sy * np.sqrt(1 - r ** 2))

    x = sx * _A
    y = sy * (r * _A + np.sqrt(1 - r ** 2) * _B)

    ax_j.clear()
    ax_j.contourf(XX, YY, Z, levels=9, cmap="magma", alpha=0.55)
    ax_j.contour(XX, YY, Z, levels=5, colors=AMBAR, linewidths=1.0, alpha=0.8)
    ax_j.scatter(x, y, s=5, color=AZUL, alpha=0.55, linewidths=0)
    ax_j.axhline(0, color=INK, lw=0.9, alpha=0.5)
    ax_j.axvline(0, color=INK, lw=0.9, alpha=0.5)
    ax_j.set_xlim(-3.6, 3.6); ax_j.set_ylim(-3.6, 3.6)
    ax_j.set_xticks([]); ax_j.set_yticks([])
    ax_j.set_title(r"$f_{X,Y}(x,y)$", color=AMBAR, pad=10)
    limpiar(ax_j, ejes=())
    ax_j.text(0.02, 0.955, f"ρ = {rho:+.2f}", transform=ax_j.transAxes,
              color=AMBAR, fontsize=11, weight="bold")

    # ---- marginal en x
    fx = np.exp(-G ** 2 / (2 * sx ** 2)) / (sx * np.sqrt(2 * np.pi))
    ax_mx.clear()
    ax_mx.plot(G, fx, color=VERDE, lw=2.2)
    ax_mx.fill_between(G, 0, fx, color=VERDE, alpha=0.22)
    ax_mx.set_xlim(-3.6, 3.6); ax_mx.set_ylim(0, 0.85)
    ax_mx.set_xticks([]); ax_mx.set_yticks([])
    # la etiqueta va dentro del eje: como xlabel chocaba con el pie de figura
    ax_mx.text(0.015, 0.82, r"$f_X(x)=\int f_{X,Y}\,dy$", color=VERDE,
               fontsize=9.5, transform=ax_mx.transAxes, va="top")
    limpiar(ax_mx, ejes=())

    # ---- marginal en y (acostada)
    fy = np.exp(-G ** 2 / (2 * sy ** 2)) / (sy * np.sqrt(2 * np.pi))
    ax_my.clear()
    ax_my.plot(fy, G, color=MAGENTA, lw=2.2)
    ax_my.fill_betweenx(G, 0, fy, color=MAGENTA, alpha=0.22)
    ax_my.set_ylim(-3.6, 3.6); ax_my.set_xlim(0, 0.85)
    ax_my.set_xticks([]); ax_my.set_yticks([])
    ax_my.set_title(r"$f_Y(y)$", color=MAGENTA, fontsize=9.5, pad=8)
    limpiar(ax_my, ejes=())

    fig.canvas.draw_idle()


s_rho = estilo_slider(Slider(eje_slider(fig, 0.28, 0.165, 0.45), r"$\rho$",
                             -0.97, 0.97, valinit=0.6, valfmt="%.2f"))
s_sx = estilo_slider(Slider(eje_slider(fig, 0.28, 0.110, 0.45), r"$\sigma_X$",
                            0.4, 1.6, valinit=1.0, valfmt="%.2f"))
s_sy = estilo_slider(Slider(eje_slider(fig, 0.28, 0.055, 0.45), r"$\sigma_Y$",
                            0.4, 1.6, valinit=1.0, valfmt="%.2f"))
for s in (s_rho, s_sx, s_sy):
    s.on_changed(dibujar)

fig.text(0.5, 0.235, "Mové solo ρ: la nube gira y las dos marginales no se "
                     "mueven. Eso es que las marginales no determinan la conjunta.",
         ha="center", color=INK, fontsize=9.5, style="italic")
dibujar()
plt.show()
