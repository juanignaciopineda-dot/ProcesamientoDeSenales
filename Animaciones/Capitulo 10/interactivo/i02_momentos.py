"""Interactivo - Momentos de segundo orden.

La media mu_X(t) es el promedio vertical del ensemble. La autocorrelacion
R_XX(t1, t2) es cuanto se parecen los cortes en t1 y en t2: mové las dos
lineas y mirá la nube de dispersion X(t1) contra X(t2). Cuando t2 -> t1 la
nube colapsa sobre la diagonal (correlacion 1).

    python i02_momentos.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

T = np.linspace(0, 8, 400)
K = 300
_rng = np.random.default_rng(3)
FASES = _rng.uniform(-np.pi, np.pi, K)
AMPS = _rng.normal(1.0, 0.25, K)
W0 = 1.6


def ens():
    return AMPS[:, None] * np.sin(W0 * T[None, :] + FASES[:, None])


E = ens()
MU = E.mean(axis=0)

fig = plt.figure(figsize=(12, 5.6))
fig.suptitle("Media y autocorrelación: promedio vertical y parecido entre "
             "dos instantes", color=TXT, fontsize=12, y=0.965)

ax_e = fig.add_axes([0.06, 0.30, 0.54, 0.56])
ax_s = fig.add_axes([0.68, 0.30, 0.28, 0.56])


def dibujar(t1, t2):
    ax_e.clear()
    ax_s.clear()

    for i in range(0, K, 6):
        ax_e.plot(T, E[i], color=INK, lw=0.6, alpha=0.4)
    ax_e.plot(T, MU, color=TXT, lw=2.6, label=r"$\mu_X(t)$")
    ax_e.axvline(t1, color=AZUL, lw=2.0)
    ax_e.axvline(t2, color=AMBAR, lw=2.0)
    ax_e.text(t1, 1.75, "$t_1$", color=AZUL, ha="center", fontsize=11)
    ax_e.text(t2, 1.75, "$t_2$", color=AMBAR, ha="center", fontsize=11)
    ax_e.set_xlabel("t")
    ax_e.set_ylim(-2.0, 2.0)
    ax_e.set_xlim(0, 8)
    ax_e.legend(loc="lower right", fontsize=9)
    limpiar(ax_e)

    i1 = np.argmin(np.abs(T - t1))
    i2 = np.argmin(np.abs(T - t2))
    x1, x2 = E[:, i1], E[:, i2]
    ax_s.scatter(x1, x2, color=MAGENTA, s=8, alpha=0.5)
    lim = 1.7
    ax_s.plot([-lim, lim], [-lim, lim], color=INK, lw=1.0, ls="--")
    ax_s.set_xlabel(r"$X(t_1)$", color=AZUL)
    ax_s.set_ylabel(r"$X(t_2)$", color=AMBAR)
    ax_s.set_xlim(-lim, lim)
    ax_s.set_ylim(-lim, lim)
    ax_s.set_aspect("equal")

    R = np.mean(x1 * x2)
    C = np.mean((x1 - x1.mean()) * (x2 - x2.mean()))
    rho = C / (x1.std() * x2.std() + 1e-9)
    ax_s.set_title(f"$R_{{XX}}(t_1,t_2)$ = {R:+.2f}\n"
                   fr"$\rho$ = {rho:+.2f}", color=MAGENTA, fontsize=10)
    limpiar(ax_s)
    fig.canvas.draw_idle()


s_t1 = estilo_slider(Slider(eje_slider(fig, 0.22, 0.15, 0.56), r"$t_1$",
                            0.2, 7.8, valinit=2.0, valfmt="%.2f"))
s_t2 = estilo_slider(Slider(eje_slider(fig, 0.22, 0.08, 0.56), r"$t_2$",
                            0.2, 7.8, valinit=5.0, valfmt="%.2f"))
s_t1.on_changed(lambda v: dibujar(s_t1.val, s_t2.val))
s_t2.on_changed(lambda v: dibujar(s_t1.val, s_t2.val))

pie(fig, "Con t2 = t1 la nube se pega a la diagonal (rho = 1). Al separarlos "
         "se abre: los cortes se parecen menos.")
dibujar(s_t1.val, s_t2.val)
plt.show()
