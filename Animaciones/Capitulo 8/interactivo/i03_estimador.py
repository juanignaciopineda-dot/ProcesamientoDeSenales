r"""Interactivo - El estimador es una variable aleatoria.

Con x ya observado, E[Y|X=x] es un número (el punto verde). Pero como X
es aleatoria, el estimador \hat{Y} = E[Y|X] tiene su propia densidad:
\hat{Y} = rho*(sy/sx)*X, asi que \hat{Y} ~ N(0, rho*sy). Move x y mira
como el numero recorre esa densidad.

    python i03_estimador.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

N = 300
_rng = np.random.default_rng(9)
Z1 = _rng.normal(0, 1, N)
Z2 = _rng.normal(0, 1, N)
VV = np.linspace(-3.2, 3.2, 500)

fig = plt.figure(figsize=(11.5, 5.8))
fig.suptitle("La estimación es un número; el estimador, una variable aleatoria",
             color=TXT, fontsize=12.5, y=0.965)
ax_nube = fig.add_axes([0.07, 0.28, 0.40, 0.60])
ax_dens = fig.add_axes([0.56, 0.28, 0.38, 0.60])


def dibujar(rho, xobs):
    ys = rho * Z1 + np.sqrt(max(0.0, 1 - rho ** 2)) * Z2
    mc = rho * xobs
    sd_est = abs(rho) * 1.0

    ax_nube.clear()
    ax_nube.scatter(Z1, ys, s=8, color=AZUL, alpha=0.4)
    ax_nube.plot(Z1, rho * Z1, color=VERDE, lw=2.2)
    ax_nube.plot([xobs, xobs], [-3.2, mc], color=AMBAR, lw=1.8, ls=(0, (4, 3)))
    ax_nube.plot([-3.2, xobs], [mc, mc], color=VERDE, lw=1.8, ls=(0, (4, 3)))
    ax_nube.plot([xobs], [mc], "o", color=VERDE, ms=10)
    ax_nube.set_xlim(-3.2, 3.2); ax_nube.set_ylim(-3.2, 3.2)
    ax_nube.set_xlabel("x"); ax_nube.set_ylabel("y")
    ax_nube.set_title(r"$E[Y|X=x]$ para este $x$", color=VERDE, pad=8)
    limpiar(ax_nube)
    ax_nube.text(0.02, 0.94, f"x = {xobs:+.2f}   →   estimación = {mc:+.2f}",
                 transform=ax_nube.transAxes, color=AMBAR, fontsize=9.5)

    ax_dens.clear()
    if sd_est > 1e-3:
        f = np.exp(-0.5 * (VV / sd_est) ** 2) / (sd_est * np.sqrt(2 * np.pi))
        ax_dens.plot(VV, f, color=AMBAR, lw=2.6)
        ax_dens.fill_between(VV, 0, f, color=AMBAR, alpha=0.16)
        ax_dens.plot([mc], [np.exp(-0.5 * (mc / sd_est) ** 2)
                            / (sd_est * np.sqrt(2 * np.pi))],
                     "o", color=VERDE, ms=10)
    else:
        ax_dens.axvline(0, color=AMBAR, lw=3)
        ax_dens.text(0, 0.5, r"$\rho = 0$:  $\hat{Y}$ es la constante $\mu_Y$",
                     ha="center", color=INK, fontsize=10)
    ax_dens.set_xlim(-3.2, 3.2); ax_dens.set_ylim(0, 1.4)
    ax_dens.set_xlabel(r"$\hat{y}$"); ax_dens.set_yticks([])
    ax_dens.set_title(r"densidad de  $\hat{Y} = E[Y|X]$", color=AMBAR, pad=8)
    limpiar(ax_dens, ejes=("bottom",))
    ax_dens.text(0.02, 0.94,
                 r"$\hat{Y}\sim\mathcal{N}(0,\ \rho\,\sigma_Y)$",
                 transform=ax_dens.transAxes, color=INK, fontsize=10)
    fig.canvas.draw_idle()


s_rho = estilo_slider(Slider(eje_slider(fig, 0.20, 0.14, 0.58),
                             r"$\rho$", -0.95, 0.95, valinit=0.8, valfmt="%.2f"))
s_x = estilo_slider(Slider(eje_slider(fig, 0.20, 0.07, 0.58),
                           "x observado", -2.6, 2.6, valinit=1.6, valfmt="%.2f"))
upd = lambda _: dibujar(s_rho.val, s_x.val)
s_rho.on_changed(upd)
s_x.on_changed(upd)

pie(fig, "Movés x: el punto verde recorre la densidad naranja. El estimador "
         "hereda la aleatoriedad de la medición.")
dibujar(s_rho.val, s_x.val)
plt.show()
