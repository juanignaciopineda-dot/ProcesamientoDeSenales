"""Interactivo - Prediccion lineal LMMSE.

El predictor optimo pesa la ultima medicion con el coeficiente de
correlacion entre el presente y el futuro: peso = alfa^m. Mové el horizonte
m y la correlacion alfa. Cuando el peso se apaga, la prediccion cae a la
media y la banda de incertidumbre se abre hasta la varianza total.

    python i06_prediccion.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

N = 40
NS = np.arange(N)
_rng = np.random.default_rng(77)
N0 = 22
SIGMA = 1.5


def proceso(alfa):
    x = np.zeros(N)
    e = _rng.standard_normal(N)
    for n in range(1, N):
        x[n] = alfa * x[n - 1] + np.sqrt(1 - alfa ** 2) * e[n]
    return SIGMA * x


fig = plt.figure(figsize=(12, 5.4))
fig.suptitle("Predicción lineal: el peso es la correlación entre el presente "
             "y el futuro", color=TXT, fontsize=12, y=0.965)
ax = fig.add_axes([0.07, 0.30, 0.88, 0.56])


def dibujar(m, alfa):
    m = int(round(m))
    ax.clear()
    x = proceso(alfa)
    ax.axhline(0, color=INK, lw=0.8)
    ax.vlines(NS[:N0 + 1], 0, x[:N0 + 1], color=AZUL, lw=2.0)
    ax.plot(NS[:N0 + 1], x[:N0 + 1], "o", color=AZUL, ms=4)
    ax.plot([N0], [x[N0]], "o", color=AMBAR, ms=9, label=r"$x[n_0]$")

    peso = alfa ** m
    pred = peso * x[N0]
    banda = SIGMA * np.sqrt(1 - peso ** 2)
    n = N0 + m
    ax.plot([n], [pred], "o", color=VERDE, ms=9, label=r"$\hat x[n_0+m]$")
    ax.vlines(n, 0, pred, color=VERDE, lw=2.0)
    ax.errorbar([n], [pred], yerr=banda, color=VERDE, capsize=5, lw=1.5)
    ax.axhline(0, color=AMBAR, lw=1.0, ls=":")

    ax.set_xlabel("n")
    ax.set_xlim(-1, N)
    ax.set_ylim(-5, 5)
    ax.legend(loc="upper left", fontsize=9)
    ax.text(0.99, 0.05, f"m = {m}\npeso = $\\alpha^m$ = {peso:.3f}\n"
            f"banda ±{banda:.2f}  (total ±{SIGMA:.2f})",
            transform=ax.transAxes, color=INK, fontsize=10, ha="right",
            va="bottom")
    limpiar(ax)
    fig.canvas.draw_idle()


s_m = estilo_slider(Slider(eje_slider(fig, 0.22, 0.15, 0.56), "horizonte m",
                           1, 16, valinit=3, valstep=1, valfmt="%d"))
s_a = estilo_slider(Slider(eje_slider(fig, 0.22, 0.08, 0.56),
                           r"$\alpha$ (correlación a 1 paso)", 0.0, 0.98,
                           valinit=0.7, valfmt="%.2f"))
s_m.on_changed(lambda v: dibujar(s_m.val, s_a.val))
s_a.on_changed(lambda v: dibujar(s_m.val, s_a.val))

pie(fig, "Con alfa alto la memoria dura y se puede predecir lejos; con alfa "
         "bajo, ya al paso siguiente lo mejor es la media.")
dibujar(s_m.val, s_a.val)
plt.show()
