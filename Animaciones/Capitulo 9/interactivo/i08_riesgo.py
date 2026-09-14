"""Interactivo - Decisiones de riesgo mínimo.

Asignás un costo a cada tipo de error y el detector minimiza el costo
esperado. Mové los costos de miss y de falsa alarma y mirá el umbral
correrse. Con c_miss = c_fa vuelve la regla MAP.

    python i08_riesgo.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *

SIGMA = 1.0
A0, A1 = 0.0, 2.6
R = np.linspace(-4, 9, 1200)


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


fig = plt.figure(figsize=(11.8, 6.0))
fig.suptitle("Riesgo mínimo: el umbral se corre según cuánto cuesta cada error",
             color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.08, 0.36, 0.86, 0.50])


def dibujar(*_):
    p0, c_fa, c_miss = s_p0.val, s_cfa.val, s_cmiss.val
    p1 = 1 - p0
    # eta = p0*(c10-c00) / (p1*(c01-c11)), con c00=c11=0, c10=c_fa, c01=c_miss
    eta = (p0 * c_fa) / (p1 * c_miss)
    gam = (A0 + A1) / 2 + SIGMA ** 2 * np.log(eta) / (A1 - A0)

    ax.clear()
    ax.plot(R, g(R, A0), color=AZUL, lw=2.5, label=r"$f(r|H_0)$")
    ax.plot(R, g(R, A1), color=VERDE, lw=2.5, label=r"$f(r|H_1)$")
    ax.fill_between(R, 0, g(R, A0), where=R >= gam, color=ROJO, alpha=0.55)
    ax.fill_between(R, 0, g(R, A1), where=R <= gam, color=AMBAR, alpha=0.55)
    ax.axvline(gam, color=ROJO, lw=2.4, ls=(0, (4, 3)))
    # umbral MAP de referencia
    gam_map = (A0 + A1) / 2 + SIGMA ** 2 * np.log(p0 / p1) / (A1 - A0)
    ax.axvline(gam_map, color=INK, lw=1.4, ls=(0, (2, 4)))
    ax.text(gam_map, 0.42, " MAP", color=INK, fontsize=8.5, rotation=90,
            va="top")

    ax.set_xlim(R[0], R[-1]); ax.set_ylim(0, 0.45)
    ax.set_xlabel("r"); ax.set_yticks([])
    ax.legend(loc="upper right", fontsize=10)
    limpiar(ax, ejes=("bottom",))

    pfa, pm = Q((gam - A0) / SIGMA), 1 - Q((gam - A1) / SIGMA)
    riesgo = p0 * c_fa * pfa + p1 * c_miss * pm
    ax.text(0.02, 0.95, f"η = {eta:.3f}       umbral γ = {gam:+.3f}",
            transform=ax.transAxes, color=ROJO, fontsize=10)
    ax.text(0.02, 0.87, f"riesgo esperado = {riesgo:.4f}",
            transform=ax.transAxes, color=TXT, fontsize=10)
    if abs(c_fa - c_miss) < 1e-6:
        ax.text(0.02, 0.79, "c_fa = c_miss  →  vuelve la regla MAP",
                transform=ax.transAxes, color=VERDE, fontsize=9.5)
    fig.canvas.draw_idle()


s_cmiss = estilo_slider(Slider(eje_slider(fig, 0.22, 0.16, 0.56),
                               "costo de un MISS", 0.2, 20.0, valinit=1.0,
                               valfmt="%.1f"))
s_cfa = estilo_slider(Slider(eje_slider(fig, 0.22, 0.10, 0.56),
                             "costo de una FALSA ALARMA", 0.2, 20.0,
                             valinit=1.0, valfmt="%.1f"))
s_p0 = estilo_slider(Slider(eje_slider(fig, 0.22, 0.04, 0.56),
                            r"$p_0$", 0.1, 0.9, valinit=0.5, valfmt="%.2f"))
for s in (s_cmiss, s_cfa, s_p0):
    s.on_changed(dibujar)

pie(fig, "Si un miss cuesta más, el umbral baja: el detector se vuelve "
         "desconfiado. La línea gris marca dónde estaría el umbral MAP.")
dibujar()
plt.show()
