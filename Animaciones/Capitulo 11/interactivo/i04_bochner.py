"""Interactivo - Bochner: qué puede ser una autocorrelación.

Elegí una forma para R(tau) y mové su ancho. El script calcula la
transformada y te dice si es una autocorrelación válida, resaltando en
rojo cualquier tramo donde el espectro se hace negativo.

    python i04_bochner.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from estilo_int import *

TAU = np.linspace(-6, 6, 4000)
W = np.linspace(-16, 16, 3000)

FORMAS = ["rectangular", "triangular", "gaussiana", "coseno truncado"]


def R_de(forma, t0):
    if forma == "rectangular":
        return np.where(np.abs(TAU) <= t0, 1.0, 0.0)
    if forma == "triangular":
        return np.clip(1 - np.abs(TAU) / t0, 0, None)
    if forma == "gaussiana":
        return np.exp(-(TAU / t0) ** 2)
    return np.where(np.abs(TAU) <= t0, np.cos(np.pi * TAU / (2 * t0)), 0.0)


def transformada(R):
    """Transformada de Fourier numérica: R es real y par, así que sale real."""
    dt = TAU[1] - TAU[0]
    return np.array([np.sum(R * np.cos(w * TAU)) * dt for w in W])


fig = plt.figure(figsize=(12.0, 5.8))
fig.suptitle("¿Puede esta función ser una autocorrelación?", color=TXT,
             fontsize=13, y=0.965)

ax_r = fig.add_axes([0.24, 0.36, 0.32, 0.52])
ax_s = fig.add_axes([0.64, 0.36, 0.33, 0.52])
ax_radio = fig.add_axes([0.025, 0.42, 0.155, 0.32])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)


def dibujar(*_):
    forma = radio.value_selected
    t0 = s_ancho.val
    R = R_de(forma, t0)
    S = transformada(R)

    ax_r.clear()
    ax_r.plot(TAU, R, color=MAGENTA, lw=2.4)
    ax_r.fill_between(TAU, 0, R, color=MAGENTA, alpha=0.15)
    ax_r.set_title(r"$R(\tau)$", color=MAGENTA, pad=10)
    ax_r.set_xlabel(r"$\tau$"); ax_r.set_xlim(-6, 6)
    ax_r.set_ylim(-0.25, 1.2); ax_r.set_yticks([0, 1])
    limpiar(ax_r)

    ax_s.clear()
    neg = S < -1e-9
    valida = not neg.any()
    # la curva y el relleno positivo van en color neutro; el ROJO queda
    # reservado para la parte negativa, que es lo que invalida a R
    col_curva = VERDE if valida else MAGENTA
    ax_s.plot(W, S, color=col_curva, lw=2.4)
    ax_s.fill_between(W, 0, S, where=~neg, color=col_curva, alpha=0.20)
    if neg.any():
        ax_s.fill_between(W, 0, S, where=neg, color=ROJO, alpha=0.85)
    ax_s.axhline(0, color=INK, lw=1.2, ls=(0, (4, 3)))
    ax_s.set_title(r"$\mathcal{F}\{R\}(\omega)$", color=col_curva, pad=10)
    ax_s.set_xlabel(r"$\omega$"); ax_s.set_xlim(-16, 16)
    lim = max(0.35, S.max() * 1.25)
    ax_s.set_ylim(min(-lim * 0.18, S.min() * 1.35), lim)
    ax_s.set_yticks([0]); ax_s.set_yticklabels(["0"])
    limpiar(ax_s, ejes=("bottom", "left"))

    if valida:
        txt, sub = "AUTOCORRELACIÓN VÁLIDA", "la transformada nunca baja de cero"
    else:
        txt = "NO ES AUTOCORRELACIÓN"
        sub = f"se hace negativa (mínimo = {S.min():.3f})"
    veredicto[0].set_text(txt)
    veredicto[0].set_color(VERDE if valida else ROJO)
    veredicto[1].set_text(sub)
    fig.canvas.draw_idle()


# el veredicto vive en la figura, no en el eje: asi no se corre ni pisa
# la fila de sliders cuando cambian los limites del grafico
veredicto = [
    fig.text(0.70, 0.255, "", ha="center", fontsize=12.5, weight="bold"),
    fig.text(0.70, 0.205, "", ha="center", fontsize=9.5, color=INK),
]

radio = RadioButtons(ax_radio, FORMAS, active=0, activecolor=AMBAR)
for t in radio.labels:
    t.set_color(TXT)
    t.set_fontsize(9.5)
radio.on_clicked(dibujar)

s_ancho = estilo_slider(Slider(eje_slider(fig, 0.22, 0.10, 0.34),
                               r"ancho $\tau_0$", 0.4, 3.0, valinit=1.2,
                               valfmt="%.2f"))
s_ancho.on_changed(dibujar)

pie(fig, "Teorema de Bochner: R(τ) es autocorrelación de un proceso WSS si y "
         "solo si su transformada es real, par y no negativa.")
dibujar()
plt.show()
