"""Interactivo - El filtro adaptado en accion: r[n], h[n]=s[-n], g[n].

Elegi una forma de pulso, agregale ruido, y mira la salida del filtro
adaptado g[n] = (r * h)[n]. La muestra en n=0 (bien, en el indice del
pico) se compara contra el umbral gamma.

    python i04_filtro_adaptado.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button
from estilo_int import *

BARKER13 = np.array([1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1], dtype=float)


def chirp(L, f0=0.02, f1=0.45):
    n = np.arange(L)
    f = f0 + (f1 - f0) * n / max(L - 1, 1)
    return np.cos(2 * np.pi * np.cumsum(f))


PULSOS = {
    "rect-13": lambda: np.ones(13),
    "Barker-13": lambda: BARKER13.copy(),
    "chirp-20": lambda: chirp(20),
    "2δ−δ[n−1]": lambda: np.array([2.0, -1.0]),
}

fig = plt.figure(figsize=(12.6, 6.8))
fig.suptitle("Filtro adaptado en acción: r[n] → h[n]=s[−n] → g[n]",
             color=TXT, fontsize=13, y=0.97)

ax_r = fig.add_axes([0.06, 0.40, 0.27, 0.48])
ax_h = fig.add_axes([0.38, 0.40, 0.27, 0.48])
ax_g = fig.add_axes([0.70, 0.40, 0.27, 0.48])

estado = {"seed": 0}


def dibujar(*_):
    sigma = s_sigma.val
    s = PULSOS[radio.value_selected]()
    L = len(s)
    rng = np.random.default_rng(estado["seed"])
    w = rng.normal(0, sigma, L)
    r = s + w
    n = np.arange(L)

    h = s[::-1]
    g = np.convolve(r, h, mode="full")
    k = np.arange(len(g)) - (L - 1)  # k=0 corresponde a la muestra optima
    g0 = g[L - 1]
    E = np.sum(s ** 2)
    gamma = E / 2

    ax_r.clear()
    ax_r.stem(n, r, linefmt=AZUL, markerfmt="o", basefmt=" ")
    ax_r.plot(n, s, color=INK, lw=1.4, ls="--", alpha=0.7)
    ax_r.set_title("r[n] = s[n] + w[n]  (guión: s[n])", color=AZUL, pad=8,
                   fontsize=10)
    ax_r.set_xlabel("n")
    limpiar(ax_r, ejes=("bottom",))

    ax_h.clear()
    ax_h.stem(-n, s, linefmt=MAGENTA, markerfmt="o", basefmt=" ")
    ax_h.set_title("h[k] = s[−k]", color=MAGENTA, pad=8, fontsize=10)
    ax_h.set_xlabel("k")
    limpiar(ax_h, ejes=("bottom",))

    ax_g.clear()
    ax_g.stem(k, g, linefmt=VERDE, markerfmt="o", basefmt=" ")
    ax_g.axhline(gamma, color=ROJO, lw=1.8, ls="--")
    ax_g.plot([0], [g0], "o", color=TXT, ms=11, mfc="none", mew=2.4)
    ax_g.set_title("g[n] = (r * h)[n]", color=VERDE, pad=8, fontsize=10)
    ax_g.set_xlabel("n")
    limpiar(ax_g, ejes=("bottom", "left"))

    veredicto = "H1" if g0 > gamma else "H0"
    col = VERDE if veredicto == "H1" else AZUL
    cartel.set_text(f"g[0] = {g0:.2f}     γ = E/2 = {gamma:.2f}     "
                    f"decide '{veredicto}'")
    cartel.set_color(col)
    fig.canvas.draw_idle()


def nuevo_ruido(_event):
    estado["seed"] += 1
    dibujar()


cartel = fig.text(0.5, 0.24, "", ha="center", fontsize=11)

ax_radio = fig.add_axes([0.06, 0.06, 0.20, 0.20])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)
radio = RadioButtons(ax_radio, list(PULSOS.keys()), active=1)
for lbl in radio.labels:
    lbl.set_color(TXT)
    lbl.set_fontsize(9)
radio.on_clicked(dibujar)

s_sigma = estilo_slider(Slider(eje_slider(fig, 0.36, 0.14, 0.42),
                               r"nivel de ruido $\sigma$", 0.05, 2.5,
                               valinit=0.6, valfmt="%.2f"))
s_sigma.on_changed(dibujar)

ax_btn = fig.add_axes([0.82, 0.10, 0.14, 0.07])
btn = Button(ax_btn, "nuevo ruido", color=PANEL, hovercolor="#2a2f3a")
btn.label.set_color(TXT)
btn.on_clicked(nuevo_ruido)

pie(fig, "h[k]=s[-k]: la respuesta al impulso es el pulso invertido en el "
         "tiempo. g[0] es la muestra optima; se compara contra gamma=E/2.")
dibujar()
plt.show()
