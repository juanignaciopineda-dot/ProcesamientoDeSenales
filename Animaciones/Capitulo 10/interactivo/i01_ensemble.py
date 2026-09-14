"""Interactivo - El ensemble y sus dos lecturas.

Un proceso aleatorio es una pila de realizaciones. Cortá en un instante
fijo (linea vertical) y tenés una variable aleatoria: mirá su histograma.
Fijá una realizacion (linea horizontal) y tenés una senal comun y corriente.

    python i01_ensemble.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

T = np.linspace(0, 8, 800)
KMAX = 40
_rng = np.random.default_rng(10)
FASES = _rng.uniform(-np.pi, np.pi, KMAX)
AMPS = _rng.uniform(0.7, 1.5, KMAX)
W0 = 2.2


def realizacion(i):
    return AMPS[i] * np.sin(W0 * T + FASES[i])


fig = plt.figure(figsize=(12, 5.6))
fig.suptitle("El ensemble: cortá en t para ver una variable aleatoria, "
             "seguí una fila para ver una señal", color=TXT, fontsize=12,
             y=0.965)

ax_e = fig.add_axes([0.06, 0.30, 0.56, 0.56])
ax_h = fig.add_axes([0.70, 0.30, 0.26, 0.56])


def dibujar(K, tstar):
    K = int(round(K))
    ax_e.clear()
    ax_h.clear()

    for i in range(K):
        ax_e.plot(T, realizacion(i), color=INK, lw=0.8, alpha=0.55)
    ax_e.plot(T, realizacion(0), color=AZUL, lw=2.0,
              label="una realización fija")
    ax_e.axvline(tstar, color=AMBAR, lw=2.0)

    valores = np.array([realizacion(i)[np.argmin(np.abs(T - tstar))]
                        for i in range(K)])
    ax_e.scatter(np.full(K, tstar), valores, color=AMBAR, s=14, zorder=5)
    ax_e.set_xlabel("t")
    ax_e.set_ylabel("x")
    ax_e.set_xlim(0, 8)
    ax_e.set_ylim(-1.8, 1.8)
    ax_e.set_title(f"{K} realizaciones", color=INK, fontsize=10)
    ax_e.legend(loc="upper right", fontsize=8)
    limpiar(ax_e)

    ax_h.hist(valores, bins=max(6, K // 3), orientation="horizontal",
              color=AMBAR, alpha=0.55, edgecolor=AMBAR)
    ax_h.axhline(valores.mean(), color=TXT, lw=1.8)
    ax_h.set_ylim(-1.8, 1.8)
    ax_h.set_title(r"$x(t^*)$ es una v.a.", color=AMBAR, fontsize=10)
    ax_h.text(0.95, 0.02,
              f"media ≈ {valores.mean():.2f}\ndesv ≈ {valores.std():.2f}",
              transform=ax_h.transAxes, color=INK, fontsize=9, ha="right",
              va="bottom")
    ax_h.set_xticks([])
    limpiar(ax_h, ejes=("left",))
    fig.canvas.draw_idle()


s_k = estilo_slider(Slider(eje_slider(fig, 0.22, 0.15, 0.56), "realizaciones",
                           3, KMAX, valinit=12, valstep=1, valfmt="%d"))
s_t = estilo_slider(Slider(eje_slider(fig, 0.22, 0.08, 0.56), r"$t^*$",
                           0.2, 7.8, valinit=3.0, valfmt="%.2f"))
s_k.on_changed(lambda v: dibujar(s_k.val, s_t.val))
s_t.on_changed(lambda v: dibujar(s_k.val, s_t.val))

pie(fig, "La estadística vertical (sobre el ensemble) es lo que define al "
         "proceso; una sola fila no alcanza para verla.")
dibujar(s_k.val, s_t.val)
plt.show()
