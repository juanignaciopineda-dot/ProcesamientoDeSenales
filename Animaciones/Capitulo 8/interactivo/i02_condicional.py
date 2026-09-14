"""Interactivo - Medir X cambia lo que sé de Y.

Mové rho y el valor observado x. A la izquierda, la nube conjunta con el
corte en X = x; a la derecha, la densidad de Y antes de medir (azul) y
después (naranja), más angosta. El error baja de sigma_Y^2 a sigma_Y^2(1-rho^2).

    python i02_condicional.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

N = 400
SY = 1.0
_rng = np.random.default_rng(4)
Z1 = _rng.normal(0, 1, N)
Z2 = _rng.normal(0, 1, N)
YY = np.linspace(-4, 4, 500)

fig = plt.figure(figsize=(12.0, 5.8))
fig.suptitle("Medir X cambia lo que sé de Y", color=TXT, fontsize=13, y=0.965)
ax_nube = fig.add_axes([0.07, 0.30, 0.42, 0.58])
ax_dens = fig.add_axes([0.58, 0.30, 0.37, 0.58])


def dibujar(rho, xobs):
    ys = rho * Z1 + np.sqrt(max(0.0, 1 - rho ** 2)) * Z2

    ax_nube.clear()
    ax_nube.scatter(Z1, ys, s=8, color=AZUL, alpha=0.45)
    ax_nube.axvline(xobs, color=AMBAR, lw=2.5)
    # media condicional en x
    mc = rho * xobs
    ax_nube.plot(Z1, rho * Z1, color=VERDE, lw=2.2)
    ax_nube.plot([xobs], [mc], "o", color=VERDE, ms=9)
    ax_nube.set_xlim(-3.6, 3.6); ax_nube.set_ylim(-3.6, 3.6)
    ax_nube.set_xlabel("x"); ax_nube.set_ylabel("y")
    ax_nube.set_title("muestras de la conjunta", color=AZUL, pad=8)
    limpiar(ax_nube)

    ax_dens.clear()
    f_marg = np.exp(-0.5 * (YY / SY) ** 2) / (SY * np.sqrt(2 * np.pi))
    sd_c = SY * np.sqrt(max(1e-6, 1 - rho ** 2))
    f_cond = np.exp(-0.5 * ((YY - mc) / sd_c) ** 2) / (sd_c * np.sqrt(2 * np.pi))
    ax_dens.plot(YY, f_marg, color=AZUL, lw=2.2, label=r"$f_Y(y)$  (sin medir)")
    ax_dens.fill_between(YY, 0, f_marg, color=AZUL, alpha=0.10)
    ax_dens.plot(YY, f_cond, color=AMBAR, lw=2.6,
                 label=r"$f_{Y|X}(y|x)$  (midiendo)")
    ax_dens.fill_between(YY, 0, f_cond, color=AMBAR, alpha=0.16)
    ax_dens.axvline(mc, color=VERDE, lw=2, ls=(0, (4, 3)))
    ax_dens.set_xlim(-4, 4); ax_dens.set_ylim(0, 1.75)
    ax_dens.set_xlabel("y"); ax_dens.set_yticks([])
    ax_dens.set_title("la densidad que importa", color=AMBAR, pad=8)
    ax_dens.legend(loc="lower center", fontsize=9)
    limpiar(ax_dens, ejes=("bottom",))

    ax_dens.text(0.02, 0.95,
                 f"sin medir:   MMSE = $\\sigma_Y^2$ = {SY**2:.2f}",
                 transform=ax_dens.transAxes, color=AZUL, fontsize=9.5)
    ax_dens.text(0.02, 0.88,
                 f"midiendo X:  MMSE = $\\sigma_Y^2(1-\\rho^2)$ = {SY**2*(1-rho**2):.3f}",
                 transform=ax_dens.transAxes, color=AMBAR, fontsize=9.5)
    fig.canvas.draw_idle()


s_rho = estilo_slider(Slider(eje_slider(fig, 0.20, 0.145, 0.58),
                             r"$\rho$", -0.95, 0.95, valinit=0.7, valfmt="%.2f"))
s_x = estilo_slider(Slider(eje_slider(fig, 0.20, 0.075, 0.58),
                           "x observado", -2.5, 2.5, valinit=-1.2, valfmt="%.2f"))
upd = lambda _: dibujar(s_rho.val, s_x.val)
s_rho.on_changed(upd)
s_x.on_changed(upd)

pie(fig, "La densidad condicional siempre es más angosta que la marginal "
         "(salvo rho = 0): medir X reduce la incertidumbre.")
dibujar(s_rho.val, s_x.val)
plt.show()
