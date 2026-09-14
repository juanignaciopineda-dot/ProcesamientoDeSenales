"""Interactivo - Ajustar la recta LMMSE a mano.

Mové a (pendiente) y b (ordenada) y mirá el error cuadrático medio. El
botón te lleva al óptimo. Con la nube gaussiana centrada, el óptimo es
a = rho, b = 0.

    python i04_lmmse.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from estilo_int import *

N = 260
RHO = 0.72
_rng = np.random.default_rng(17)
XS = _rng.normal(0, 1, N)
YS = RHO * XS + np.sqrt(1 - RHO ** 2) * _rng.normal(0, 1, N)

A_OPT, B_OPT = RHO, 0.0

fig = plt.figure(figsize=(11.5, 6.0))
fig.suptitle("Ajustar la recta que minimiza el error cuadrático medio",
             color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.09, 0.32, 0.60, 0.55])
ax_bar = fig.add_axes([0.80, 0.32, 0.07, 0.55])

MSE_REF = float(np.mean((YS - (-1.0 * XS + 1.4)) ** 2))


def dibujar(*_):
    a, b = s_a.val, s_b.val
    ax.clear()
    ax.scatter(XS, YS, s=9, color=AZUL, alpha=0.5)
    xs = np.array([-3.4, 3.4])
    ax.plot(xs, a * xs + b, color=AMBAR, lw=3)
    # unos pocos residuos
    for i in range(0, N, 11):
        ax.plot([XS[i], XS[i]], [YS[i], a * XS[i] + b], color=ROJO, lw=1.2,
                alpha=0.7)
    ax.set_xlim(-3.4, 3.4); ax.set_ylim(-3.4, 3.4)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    limpiar(ax)

    mse = float(np.mean((YS - (a * XS + b)) ** 2))
    ax.text(0.02, 0.95, f"a = {a:+.2f}   b = {b:+.2f}", transform=ax.transAxes,
            color=AMBAR, fontsize=10)
    ax.text(0.02, 0.88, f"MSE = {mse:.3f}", transform=ax.transAxes,
            color=ROJO, fontsize=10)
    ax.text(0.02, 0.81,
            f"mínimo posible = $\\sigma_Y^2(1-\\rho^2)$ = {1 - RHO**2:.3f}",
            transform=ax.transAxes, color=VERDE, fontsize=9)

    ax_bar.clear()
    ax_bar.bar([0], [mse], width=0.7, color=ROJO, alpha=0.9)
    ax_bar.axhline(1 - RHO ** 2, color=VERDE, lw=2, ls=(0, (4, 3)))
    ax_bar.set_ylim(0, MSE_REF * 1.05); ax_bar.set_xlim(-0.6, 0.6)
    ax_bar.set_xticks([]); ax_bar.set_title("MSE", color=ROJO, fontsize=10, pad=8)
    limpiar(ax_bar, ejes=("left",))
    fig.canvas.draw_idle()


s_a = estilo_slider(Slider(eje_slider(fig, 0.20, 0.15, 0.48),
                           "a  (pendiente)", -2.0, 2.0, valinit=-0.8,
                           valfmt="%.2f"))
s_b = estilo_slider(Slider(eje_slider(fig, 0.20, 0.075, 0.48),
                           "b  (ordenada)", -2.0, 2.0, valinit=1.2,
                           valfmt="%.2f"))
s_a.on_changed(dibujar)
s_b.on_changed(dibujar)

ax_btn = fig.add_axes([0.80, 0.09, 0.15, 0.065])
btn = Button(ax_btn, "ir al óptimo", color=PANEL, hovercolor="#2a2f3a")
btn.label.set_color(TXT)


def al_optimo(_):
    s_a.set_val(A_OPT)
    s_b.set_val(B_OPT)


btn.on_clicked(al_optimo)

pie(fig, "Cada segmento rojo es un error. El óptimo deja el error "
         "perpendicular a la medición: a = rho, b = 0.")
dibujar()
plt.show()
