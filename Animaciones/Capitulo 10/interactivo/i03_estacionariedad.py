"""Interactivo - Estacionariedad y la ventana deslizante.

Deslizá la ventana y mirá la media y el desvio locales. Con "deriva" en
cero el proceso es estacionario: los dos numeros no cambian con la
posicion. Al subir la deriva la media se va y la amplitud crece: deja de
ser WSS.

    python i03_estacionariedad.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

T = np.linspace(0, 14, 1400)
_rng = np.random.default_rng(20)
# muchas senoides de igual amplitud y fase aleatoria: la realizacion se ve
# pareja a lo largo de todo el tramo (es lo que uno espera de un WSS)
BASE = np.zeros_like(T)
for _ in range(90):
    f = _rng.uniform(4.0, 10.0)
    BASE += np.sin(2 * np.pi * f * T / T[-1] * 3 + _rng.uniform(0, 2 * np.pi))
BASE = BASE / np.std(BASE)

ANCHO_V = 3.0

fig = plt.figure(figsize=(12, 5.4))
fig.suptitle("Estacionariedad: ¿la media y el desvío locales dependen de "
             "dónde mirás?", color=TXT, fontsize=12, y=0.965)
ax = fig.add_axes([0.07, 0.30, 0.88, 0.56])


def senal(deriva):
    tendencia = deriva * (T - 7) / 7.0
    amplitud = 1.0 + 0.6 * deriva * T / T[-1]
    return tendencia + amplitud * BASE


def dibujar(centro, deriva):
    ax.clear()
    y = senal(deriva)
    ax.plot(T, y, color=AZUL, lw=1.3)

    a, b = centro - ANCHO_V / 2, centro + ANCHO_V / 2
    ax.axvspan(a, b, color=AMBAR, alpha=0.13)
    m = (T >= a) & (T <= b)
    mu, sd = y[m].mean(), y[m].std()
    ax.hlines(mu, a, b, color=TXT, lw=2.5)
    ax.hlines([mu - sd, mu + sd], a, b, color=AMBAR, lw=1.5, ls="--")

    ax.set_xlabel("t")
    ax.set_xlim(0, 14)
    ax.set_ylim(-4.5, 4.5)
    ax.text(0.01, 0.96, f"en la ventana:   media = {mu:+.2f}      "
            f"desvío = {sd:.2f}", transform=ax.transAxes, color=AMBAR,
            fontsize=11, va="top")
    veredicto = ("estacionario: los dos números no se mueven"
                 if deriva < 0.05 else
                 "NO estacionario: cambian con la posición de la ventana")
    col = VERDE if deriva < 0.05 else ROJO
    ax.text(0.01, 0.06, veredicto, transform=ax.transAxes, color=col,
            fontsize=11, va="bottom")
    limpiar(ax)
    fig.canvas.draw_idle()


s_c = estilo_slider(Slider(eje_slider(fig, 0.22, 0.15, 0.56), "centro ventana",
                           ANCHO_V / 2, 14 - ANCHO_V / 2, valinit=2.0,
                           valfmt="%.2f"))
s_d = estilo_slider(Slider(eje_slider(fig, 0.22, 0.08, 0.56), "deriva",
                           0.0, 1.5, valinit=0.0, valfmt="%.2f"))
s_c.on_changed(lambda v: dibujar(s_c.val, s_d.val))
s_d.on_changed(lambda v: dibujar(s_c.val, s_d.val))

pie(fig, "WSS quiere decir: la media es constante y la autocorrelación solo "
         "depende de la separación, no del instante.")
dibujar(s_c.val, s_d.val)
plt.show()
