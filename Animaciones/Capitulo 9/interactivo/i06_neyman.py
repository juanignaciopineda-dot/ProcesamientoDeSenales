"""Interactivo - Neyman-Pearson.

Fijás una cota α para la falsa alarma y el detector maximiza PD sujeto a
eso. Mové la cota y la separación entre hipótesis, y mirá el punto de
operación moverse sobre la ROC. Nada de esto usa los a priori.

    python i06_neyman.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *

SIGMA = 1.0
R = np.linspace(-4, 9, 1200)


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


def Qinv(p):
    lo, hi = -8.0, 8.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if Q(mid) > p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


fig = plt.figure(figsize=(12.0, 5.8))
fig.suptitle("Neyman-Pearson: acotar la falsa alarma y maximizar la detección",
             color=TXT, fontsize=13, y=0.965)
ax_d = fig.add_axes([0.06, 0.34, 0.44, 0.52])
ax_r = fig.add_axes([0.60, 0.30, 0.34, 0.58])


def dibujar(*_):
    alfa, d = s_alfa.val, s_d.val
    gam = Qinv(alfa)                    # umbral que da exactamente PFA = alfa
    pd = Q(gam - d)

    ax_d.clear()
    ax_d.plot(R, g(R, 0), color=AZUL, lw=2.4, label=r"$f(r|H_0)$")
    ax_d.plot(R, g(R, d), color=VERDE, lw=2.4, label=r"$f(r|H_1)$")
    ax_d.fill_between(R, 0, g(R, 0), where=R >= gam, color=ROJO, alpha=0.6)
    ax_d.fill_between(R, 0, g(R, d), where=R >= gam, color=VERDE, alpha=0.28)
    ax_d.axvline(gam, color=ROJO, lw=2.2, ls=(0, (4, 3)))
    ax_d.set_xlim(R[0], R[-1]); ax_d.set_ylim(0, 0.45)
    ax_d.set_xlabel("r"); ax_d.set_yticks([])
    ax_d.legend(loc="upper right", fontsize=9.5)
    ax_d.text(0.02, 0.94, f"cota $P_{{FA}} \\leq \\alpha$ = {alfa:.3f}",
              transform=ax_d.transAxes, color=ROJO, fontsize=10)
    ax_d.text(0.02, 0.86, f"$P_D$ alcanzado = {pd:.4f}",
              transform=ax_d.transAxes, color=VERDE, fontsize=10)
    limpiar(ax_d, ejes=("bottom",))

    ax_r.clear()
    ff = np.linspace(1e-4, 1 - 1e-4, 400)
    roc = Q(Qinv(ff.tolist()[0]) - d) if False else [Q(Qinv(f) - d) for f in ff]
    ax_r.plot(ff, roc, color=AMBAR, lw=2.4)
    ax_r.plot([0, 1], [0, 1], color=INK, lw=1.5, ls=(0, (4, 3)))
    ax_r.plot([alfa], [pd], "o", color=ROJO, ms=10)
    ax_r.axvline(alfa, color=ROJO, lw=1.2, ls=(0, (2, 4)), alpha=0.7)
    ax_r.set_xlim(0, 1); ax_r.set_ylim(0, 1.02)
    ax_r.set_xlabel(r"$P_{FA}$"); ax_r.set_ylabel(r"$P_D$")
    ax_r.set_xticks([0, 0.5, 1]); ax_r.set_yticks([0, 0.5, 1])
    ax_r.set_title("punto de operación sobre la ROC", color=INK, fontsize=10,
                   pad=8)
    limpiar(ax_r)
    fig.canvas.draw_idle()


s_alfa = estilo_slider(Slider(eje_slider(fig, 0.25, 0.13, 0.5),
                              r"cota $\alpha$ para $P_{FA}$", 0.005, 0.6,
                              valinit=0.1, valfmt="%.3f"))
s_d = estilo_slider(Slider(eje_slider(fig, 0.25, 0.065, 0.5),
                           "separación (SNR)", 0.5, 5.0, valinit=2.4,
                           valfmt="%.2f"))
s_alfa.on_changed(dibujar)
s_d.on_changed(dibujar)

pie(fig, "Apretás la cota de falsa alarma y la detección se cae con ella. "
         "El umbral se elige sin conocer p0 ni p1.")
dibujar()
plt.show()
