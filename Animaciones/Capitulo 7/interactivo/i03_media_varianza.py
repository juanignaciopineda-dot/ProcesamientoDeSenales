"""Interactivo - Media y varianza.

Mové mu y sigma y mirá el punto de equilibrio y el ancho. Se verifica
numéricamente la identidad sigma^2 = E[X^2] - mu^2.

    python i03_media_varianza.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from estilo_int import *

X = np.linspace(-8, 8, 4000)
FORMAS = ["normal", "uniforme", "exponencial desplazada"]


def densidad(forma, mu, sig):
    if forma == "normal":
        return np.exp(-((X - mu) ** 2) / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    if forma == "uniforme":
        h = sig * np.sqrt(3.0)
        return np.where(np.abs(X - mu) <= h, 1 / (2 * h), 0.0)
    lam = 1 / sig                       # exponencial con media mu, desvio sig
    return np.where(X >= mu - sig, lam * np.exp(-lam * (X - (mu - sig))), 0.0)


fig = plt.figure(figsize=(12.0, 6.0))
fig.suptitle("Media y varianza: el equilibrio y el desparramo", color=TXT,
             fontsize=13, y=0.965)

ax = fig.add_axes([0.22, 0.34, 0.74, 0.52])
ax_radio = fig.add_axes([0.025, 0.44, 0.16, 0.24])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)
lectura = fig.text(0.59, 0.22, "", ha="center", fontsize=10.5, color=INK)


def dibujar(*_):
    forma = radio.value_selected
    mu, sig = s_mu.val, s_sig.val
    f = densidad(forma, mu, sig)

    ax.clear()
    ax.plot(X, f, color=AZUL, lw=2.5)
    ax.fill_between(X, 0, f, color=AZUL, alpha=0.16)

    # momentos calculados sobre la grilla, para verificar la identidad
    area = np.trapezoid(f, X)
    m1 = np.trapezoid(X * f, X) / area
    m2 = np.trapezoid(X ** 2 * f, X) / area
    var = m2 - m1 ** 2
    sd = np.sqrt(max(var, 0.0))

    # el fulcro en la media
    ax.plot([m1], [0], marker="^", ms=14, color=AMBAR, clip_on=False, zorder=5)
    ax.axvline(m1, color=AMBAR, ls=(0, (3, 3)), lw=1.4)
    ax.text(m1, -0.048 * f.max() - 0.012, r"$\mu_X$", color=AMBAR,
            ha="center", va="top", fontsize=11)

    # la banda de +-1 desvio
    ax.axvspan(m1 - sd, m1 + sd, color=VERDE, alpha=0.12)
    ax.annotate("", xy=(m1 + sd, f.max() * 0.9), xytext=(m1 - sd, f.max() * 0.9),
                arrowprops=dict(arrowstyle="<->", color=VERDE, lw=1.8))
    ax.text(m1, f.max() * 0.94, r"$2\sigma_X$", color=VERDE, ha="center",
            fontsize=10.5)

    ax.set_xlim(-8, 8); ax.set_ylim(0, max(f.max() * 1.15, 0.05))
    ax.set_xlabel("x"); ax.set_yticks([])
    ax.set_title(r"$f_X(x)$", color=AZUL, pad=10)
    limpiar(ax, ejes=("bottom",))

    lectura.set_text(
        f"$E[X]$ = {m1:+.3f}      $E[X^2]$ = {m2:.3f}      "
        f"$E[X^2]-\\mu^2$ = {var:.3f}      $\\sigma_X$ = {sd:.3f}")
    fig.canvas.draw_idle()


radio = RadioButtons(ax_radio, FORMAS, active=0, activecolor=AMBAR)
for t in radio.labels:
    t.set_color(TXT); t.set_fontsize(9.5)
radio.on_clicked(dibujar)

s_mu = estilo_slider(Slider(eje_slider(fig, 0.26, 0.125, 0.5), r"$\mu$",
                            -4.0, 4.0, valinit=0.0, valfmt="%.2f"))
s_sig = estilo_slider(Slider(eje_slider(fig, 0.26, 0.062, 0.5), r"$\sigma$",
                             0.3, 3.0, valinit=1.0, valfmt="%.2f"))
s_mu.on_changed(dibujar); s_sig.on_changed(dibujar)

pie(fig, "La media es el punto de equilibrio de la densidad; la varianza, "
         "cuánto se desparrama alrededor.")
dibujar()
plt.show()
