"""Interactivo - Covarianza, rho y la trampa de la no correlación.

Mové rho para el caso lineal, o elegí uno de los casos patológicos: son
nubes con rho ~ 0 donde Y depende clarísimamente de X. rho solo ve la
parte lineal de la relación.

    python i07_correlacion.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from estilo_int import *

N = 420
CASOS = ["lineal (mové ρ)", "parábola", "anillo", "dos brazos", "abanico"]
_rng = np.random.default_rng(31)


def muestra(caso, rho):
    if caso.startswith("lineal"):
        a, b = _rng.normal(0, 1, N), _rng.normal(0, 1, N)
        r = np.clip(rho, -0.99, 0.99)
        return a, r * a + np.sqrt(1 - r ** 2) * b

    if caso == "parábola":
        # se simetriza la muestra: asi la correlacion con una funcion par
        # de x es exactamente cero, no "casi" cero
        h = _rng.uniform(0.1, 2.1, N // 2)
        x = np.concatenate([h, -h])
        return x, 0.75 * x ** 2 - 1.1 + _rng.normal(0, 0.16, len(x))

    if caso == "anillo":
        t = _rng.uniform(0, 2 * np.pi, N)
        rad = 1.7 + _rng.normal(0, 0.10, N)
        return rad * np.cos(t), rad * np.sin(t)

    if caso == "dos brazos":
        s = _rng.choice([-1, 1], N // 2)
        h = _rng.uniform(0.1, 2.0, N // 2)
        x = np.concatenate([h, -h])
        y = np.concatenate([1.15 * h, 1.15 * h]) * np.concatenate([s, s])
        return x, y + _rng.normal(0, 0.13, len(x))

    # abanico: varianza de Y creciente con |X|, media cero
    h = _rng.uniform(0.05, 2.2, N // 2)
    x = np.concatenate([h, -h])
    e = _rng.normal(0, 1, N // 2)
    return x, np.concatenate([e, e]) * 0.85 * np.concatenate([h, h])


fig = plt.figure(figsize=(12.0, 6.4))
fig.suptitle("ρ solo ve la relación lineal", color=TXT, fontsize=13, y=0.965)

ax = fig.add_axes([0.28, 0.33, 0.42, 0.54])
ax_radio = fig.add_axes([0.025, 0.42, 0.185, 0.34])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)
panel = fig.text(0.80, 0.72, "", ha="left", va="top", fontsize=11, color=INK)
veredicto = fig.text(0.80, 0.50, "", ha="left", va="top", fontsize=11,
                     weight="bold")


def dibujar(*_):
    caso = radio.value_selected
    x, y = muestra(caso, s_rho.val)

    sx, sy = x.std(), y.std()
    cov = float(np.mean((x - x.mean()) * (y - y.mean())))
    rho = cov / (sx * sy) if sx > 0 and sy > 0 else 0.0

    col = AZUL if caso.startswith("lineal") else MAGENTA
    ax.clear()
    ax.scatter(x, y, s=9, color=col, alpha=0.6, linewidths=0)
    ax.axhline(0, color=INK, lw=0.9, alpha=0.55)
    ax.axvline(0, color=INK, lw=0.9, alpha=0.55)

    # la recta de regresión: es lo único que ρ "ve"
    if sx > 0:
        pend = cov / sx ** 2
        xs = np.linspace(-3.2, 3.2, 10)
        ax.plot(xs, y.mean() + pend * (xs - x.mean()), color=AMBAR, lw=2.0,
                ls=(0, (5, 3)))

    ax.set_xlim(-3.4, 3.4); ax.set_ylim(-3.4, 3.4)
    ax.set_xlabel("X"); ax.set_ylabel("Y")
    ax.set_aspect("equal")
    limpiar(ax)

    panel.set_text(f"$\\sigma_X$ = {sx:.3f}\n"
                   f"$\\sigma_Y$ = {sy:.3f}\n\n"
                   f"$\\sigma_{{X,Y}}$ = {cov:+.3f}\n\n"
                   f"ρ = {rho:+.3f}")

    if caso.startswith("lineal"):
        veredicto.set_text("relación lineal:\nρ la captura bien")
        veredicto.set_color(VERDE)
    else:
        veredicto.set_text(f"ρ ≈ {rho:+.2f}\npero Y depende de X\n\n"
                           "la recta naranja es\nplana: no hay\ncomponente lineal")
        veredicto.set_color(ROJO)
    fig.canvas.draw_idle()


radio = RadioButtons(ax_radio, CASOS, active=0, activecolor=AMBAR)
for t in radio.labels:
    t.set_color(TXT); t.set_fontsize(9.5)
radio.on_clicked(dibujar)

s_rho = estilo_slider(Slider(eje_slider(fig, 0.30, 0.14, 0.40), r"$\rho$",
                             -0.98, 0.98, valinit=0.7, valfmt="%.2f"))
s_rho.on_changed(dibujar)

pie(fig, "El slider solo actúa en el caso lineal. Los otros cuatro tienen "
         "dependencia total entre X e Y, y ρ igual da casi cero.")
dibujar()
plt.show()
