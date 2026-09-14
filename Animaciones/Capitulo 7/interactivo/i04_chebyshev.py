"""Interactivo - La desigualdad de Chebyshev.

Mové alfa y cambiá de distribución: la cota 1/alfa^2 siempre se cumple,
pero fijate cuánto le sobra en cada caso. Ese es el precio de que valga
para cualquier distribución.

    python i04_chebyshev.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from estilo_int import *

X = np.linspace(-7, 7, 6000)
FORMAS = ["normal", "uniforme", "Laplace", "dos picos"]


def densidad(forma):
    """Todas normalizadas a media 0 y varianza 1."""
    if forma == "normal":
        return np.exp(-X ** 2 / 2) / np.sqrt(2 * np.pi)
    if forma == "uniforme":
        h = np.sqrt(3.0)
        return np.where(np.abs(X) <= h, 1 / (2 * h), 0.0)
    if forma == "Laplace":
        b = 1 / np.sqrt(2.0)
        return np.exp(-np.abs(X) / b) / (2 * b)
    # dos picos simetricos: es la que mas se acerca a la cota
    s = 0.30
    return 0.5 * (np.exp(-((X - 1) ** 2) / (2 * s ** 2))
                  + np.exp(-((X + 1) ** 2) / (2 * s ** 2))) / (s * np.sqrt(2 * np.pi))


fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Chebyshev: una cota para cualquier distribución", color=TXT,
             fontsize=13, y=0.965)

ax = fig.add_axes([0.21, 0.36, 0.53, 0.50])
ax_bar = fig.add_axes([0.81, 0.36, 0.15, 0.50])
ax_radio = fig.add_axes([0.025, 0.44, 0.145, 0.30])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)
lectura = fig.text(0.48, 0.235, "", ha="center", fontsize=10.5, color=INK)


def dibujar(*_):
    forma = radio.value_selected
    a = s_alfa.val
    f = densidad(forma)
    area = np.trapezoid(f, X)
    f = f / area

    sd = np.sqrt(np.trapezoid(X ** 2 * f, X))     # media 0 por construccion
    lim = a * sd
    colas = (np.abs(X) >= lim)
    real = np.trapezoid(f[colas], X[colas])
    cota = 1 / a ** 2

    ax.clear()
    ax.plot(X, f, color=AZUL, lw=2.4)
    ax.fill_between(X, 0, f, where=~colas, color=AZUL, alpha=0.15)
    ax.fill_between(X, 0, f, where=colas, color=ROJO, alpha=0.85)
    for s in (-1, 1):
        ax.axvline(s * lim, color=AMBAR, ls=(0, (3, 3)), lw=1.4)
    ax.set_xlim(-7, 7); ax.set_ylim(0, f.max() * 1.15)
    ax.set_xlabel("x"); ax.set_yticks([])
    ax.set_title(f"{forma}   ·   media 0, varianza 1", color=TXT, pad=10,
                 fontsize=11)
    ax.text(0.5, 0.92, r"lo rojo es  $P(|X| \geq \alpha\sigma)$",
            transform=ax.transAxes, color=ROJO, ha="center", fontsize=9.5)
    limpiar(ax, ejes=("bottom",))

    ax_bar.clear()
    ax_bar.bar([0], [cota], width=0.6, color=AMBAR, alpha=0.9)
    ax_bar.bar([1], [real], width=0.6, color=ROJO, alpha=0.95)
    ax_bar.set_xticks([0, 1])
    ax_bar.set_xticklabels(["cota\n1/α²", "masa\nreal"], fontsize=9)
    ax_bar.set_ylim(0, max(cota, real) * 1.3 + 1e-3)
    ax_bar.set_title("comparación", color=TXT, pad=10, fontsize=10.5)
    limpiar(ax_bar)
    for x, v in ((0, cota), (1, real)):
        ax_bar.text(x, v + max(cota, real) * 0.05, f"{v:.3f}", ha="center",
                    color=TXT, fontsize=9)

    holgura = cota / real if real > 1e-9 else float("inf")
    txt_h = ("la masa real es 0: la cota sobra por completo"
             if real < 1e-9 else
             f"la cota es {holgura:.1f}× más grande que la masa real")
    lectura.set_text(f"α = {a:.2f}     cota 1/α² = {cota:.4f}     "
                     f"masa real = {real:.4f}          {txt_h}")
    fig.canvas.draw_idle()


radio = RadioButtons(ax_radio, FORMAS, active=0, activecolor=AMBAR)
for t in radio.labels:
    t.set_color(TXT); t.set_fontsize(9.5)
radio.on_clicked(dibujar)

s_alfa = estilo_slider(Slider(eje_slider(fig, 0.28, 0.11, 0.46), r"$\alpha$",
                              1.0, 4.0, valinit=1.5, valfmt="%.2f"))
s_alfa.on_changed(dibujar)

pie(fig, "Probá “dos picos” con α cerca de 1: es el caso que casi alcanza la "
         "cota, y muestra que no se puede mejorar sin saber más.")
dibujar()
plt.show()
