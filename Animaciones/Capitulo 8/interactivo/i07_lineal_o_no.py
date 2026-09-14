"""Interactivo - Cuándo la recta alcanza y cuándo no.

Elegí la relación entre X e Y. Se dibuja la nube, la media condicional
E[Y|X] (verde) y la mejor recta LMMSE (naranja). Cuando E[Y|X] ya es una
recta —caso gaussiano— coinciden. Cuando es curva, la recta puede quedar
horizontal aunque X determine Y por completo.

    python i07_lineal_o_no.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, Slider
from estilo_int import *

N = 320
_rng = np.random.default_rng(7)
RELS = ["lineal (gaussiana)", "parábola  Y = X²", "seno  Y = sen(X)",
        "escalón  Y = sign(X)"]


def datos(rel, ruido):
    x = _rng.uniform(-2.6, 2.6, N)
    if rel == RELS[0]:
        rho = 0.75
        xg = _rng.normal(0, 1.1, N)
        yg = rho * xg + np.sqrt(1 - rho ** 2) * _rng.normal(0, 1.1, N)
        return xg, yg + _rng.normal(0, ruido, N), lambda t: rho * (1.1 / 1.1) * t
    if rel == RELS[1]:
        return x, x ** 2 - 2.0 + _rng.normal(0, ruido, N), lambda t: t ** 2 - 2.0
    if rel == RELS[2]:
        return x, 1.8 * np.sin(1.6 * x) + _rng.normal(0, ruido, N), \
            lambda t: 1.8 * np.sin(1.6 * t)
    return x, 1.5 * np.sign(x) + _rng.normal(0, ruido, N), \
        lambda t: 1.5 * np.sign(t)


fig = plt.figure(figsize=(11.0, 6.0))
fig.suptitle("¿Cuándo alcanza con una recta?", color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.30, 0.20, 0.62, 0.68])
ax_radio = fig.add_axes([0.03, 0.42, 0.20, 0.30])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)


def dibujar(*_):
    rel = radio.value_selected
    xs, ys, mc = datos(rel, s_ruido.val)

    ax.clear()
    ax.scatter(xs, ys, s=10, color=AZUL, alpha=0.45)
    t = np.linspace(-2.8, 2.8, 400)
    ax.plot(t, mc(t), color=VERDE, lw=3, label=r"$E[Y|X]$")

    # mejor recta LMMSE: a = cov(x,y)/var(x), b = my - a*mx
    a = np.cov(xs, ys, bias=True)[0, 1] / np.var(xs)
    b = ys.mean() - a * xs.mean()
    ax.plot(t, a * t + b, color=AMBAR, lw=2.5, label=r"$\hat{Y}_\ell$")

    ax.set_xlim(-2.9, 2.9); ax.set_ylim(-4.2, 4.2)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.legend(loc="upper left", fontsize=10)
    limpiar(ax)

    rho = np.corrcoef(xs, ys)[0, 1]
    if abs(a) < 0.12 and rel != RELS[0]:
        msg, col = "la mejor recta es casi horizontal:  ρ ≈ 0", ROJO
    elif rel == RELS[0]:
        msg, col = "E[Y|X] ya es una recta:  LMMSE = MMSE", VERDE
    else:
        msg, col = "la recta capta parte del vínculo, pero se pierde la curva", AMBAR
    ax.text(0.5, 0.03, msg + f"   (ρ = {rho:+.2f}, a = {a:+.2f})",
            transform=ax.transAxes, color=col, fontsize=10, ha="center",
            weight="bold")
    fig.canvas.draw_idle()


radio = RadioButtons(ax_radio, RELS, active=0, activecolor=AMBAR)
for t_ in radio.labels:
    t_.set_color(TXT); t_.set_fontsize(9)
radio.on_clicked(dibujar)

s_ruido = estilo_slider(Slider(eje_slider(fig, 0.36, 0.08, 0.5),
                               "ruido", 0.0, 1.0, valinit=0.35, valfmt="%.2f"))
s_ruido.on_changed(dibujar)

pie(fig, "rho = 0 no significa 'independientes': significa 'sin relación "
         "lineal'. El LMMSE solo ve esa parte del vínculo.")
dibujar()
plt.show()
