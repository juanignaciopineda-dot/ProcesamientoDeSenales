"""Interactivo - El test de razón de verosimilitud.

Panel izquierdo: las dos densidades y el umbral en r.
Panel derecho: la razón Λ(r) y el umbral η.
Mové η y mirá cómo se mueve solo el umbral equivalente en r. Cambiar de
criterio no cambia la forma del test, solo dónde se pone η.

    python i05_verosimilitud.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *

SIGMA = 1.0
A0, A1 = 0.0, 2.6
R = np.linspace(-3.5, 7.0, 1200)


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def lam(r):
    return np.exp((A1 - A0) * (r - (A0 + A1) / 2) / SIGMA ** 2)


def r_de_eta(eta):
    return (A0 + A1) / 2 + SIGMA ** 2 * np.log(eta) / (A1 - A0)


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


fig = plt.figure(figsize=(12.0, 5.8))
fig.suptitle("Test de razón de verosimilitud: un umbral η, muchos criterios",
             color=TXT, fontsize=13, y=0.965)
ax_d = fig.add_axes([0.06, 0.34, 0.42, 0.52])
ax_l = fig.add_axes([0.56, 0.34, 0.40, 0.52])


def dibujar(*_):
    eta = 10 ** s_leta.val
    gam = r_de_eta(eta)

    ax_d.clear()
    ax_d.plot(R, g(R, A0), color=AZUL, lw=2.4, label=r"$f(r|H_0)$")
    ax_d.plot(R, g(R, A1), color=VERDE, lw=2.4, label=r"$f(r|H_1)$")
    ax_d.fill_between(R, 0, g(R, A0), where=R >= gam, color=ROJO, alpha=0.5)
    ax_d.fill_between(R, 0, g(R, A1), where=R <= gam, color=AMBAR, alpha=0.5)
    ax_d.axvline(gam, color=ROJO, lw=2.2, ls=(0, (4, 3)))
    ax_d.set_xlim(R[0], R[-1]); ax_d.set_ylim(0, 0.5)
    ax_d.set_xlabel("r"); ax_d.set_yticks([])
    ax_d.set_title("las dos densidades", color=INK, fontsize=11, pad=8)
    ax_d.legend(loc="upper right", fontsize=9.5)
    ax_d.text(gam, 0.47, r"  $\gamma$", color=ROJO, fontsize=12, va="top")
    limpiar(ax_d, ejes=("bottom",))

    ax_l.clear()
    ax_l.plot(R, lam(R), color=AMBAR, lw=2.6)
    ax_l.axhline(min(eta, 60), color=ROJO, lw=2.0, ls=(0, (4, 3)))
    ax_l.axvline(gam, color=ROJO, lw=1.6, ls=(0, (2, 4)))
    ax_l.plot([gam], [min(eta, 60)], "o", color=ROJO, ms=8)
    ax_l.set_xlim(R[0], R[-1]); ax_l.set_ylim(0, 60)
    ax_l.set_xlabel("r"); ax_l.set_yticks([])
    ax_l.set_title(r"$\Lambda(r)=f(r|H_1)/f(r|H_0)$", color=AMBAR,
                   fontsize=11, pad=8)
    ax_l.text(R[0] + 0.1, min(eta, 60) + 1.5, rf"$\eta$ = {eta:.2f}",
              color=ROJO, fontsize=10)
    limpiar(ax_l, ejes=("bottom",))

    pfa, pd = Q((gam - A0) / SIGMA), Q((gam - A1) / SIGMA)
    ax_l.text(0.5, -0.24, f"$P_{{FA}}$ = {pfa:.4f}      $P_D$ = {pd:.4f}",
              transform=ax_l.transAxes, ha="center", color=INK, fontsize=10)
    fig.canvas.draw_idle()


s_leta = estilo_slider(Slider(eje_slider(fig, 0.25, 0.13, 0.5),
                              r"$\log_{10}\eta$", -1.5, 1.5, valinit=0.0,
                              valfmt="%.2f"))
s_leta.on_changed(dibujar)

pie(fig, "Fijar un umbral sobre Λ equivale a fijar uno sobre r. MAP, "
         "Neyman-Pearson y riesgo mínimo son todos este test, con η distinto.")
dibujar()
plt.show()
