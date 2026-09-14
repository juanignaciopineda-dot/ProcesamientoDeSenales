"""Interactivo - Compresion de pulso: se resuelven dos ecos o se funden?

Elegi una forma de pulso, la separacion entre dos ecos y el nivel de
ruido, y mira la salida del filtro adaptado: con un pulso rectangular los
ecos cercanos se funden; con Barker-13 o un chirp, se resuelven.

    python i07_compresion.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from estilo_int import *

BARKER13 = np.array([1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1], dtype=float)


def chirp(L, f0=0.02, f1=0.45):
    n = np.arange(L)
    f = f0 + (f1 - f0) * n / max(L - 1, 1)
    return np.cos(2 * np.pi * np.cumsum(f))


PULSOS = {
    "rectangular-13": lambda: np.ones(13),
    "Barker-13": lambda: BARKER13.copy(),
    "chirp-13": lambda: chirp(13),
}

fig = plt.figure(figsize=(12.2, 6.4))
fig.suptitle("Compresión de pulso: ¿se resuelven dos ecos cercanos?",
             color=TXT, fontsize=12.5, y=0.965)

ax_s = fig.add_axes([0.07, 0.62, 0.86, 0.24])
ax_g = fig.add_axes([0.07, 0.30, 0.86, 0.20])

rng = np.random.default_rng(0)


def dibujar(*_):
    D = s_D.val
    sigma = s_sigma.val
    s = PULSOS[radio.value_selected]()
    L = len(s)

    total_len = L + int(abs(D)) + 25
    r = np.zeros(total_len)
    D0, D1 = 5, 5 + int(round(D))
    r[D0:D0 + L] += s
    r[D1:D1 + L] += 0.8 * s
    r += rng.normal(0, sigma, total_len)

    h = s[::-1]
    g = np.convolve(r, h, mode="full")
    k = np.arange(len(g))

    ax_s.clear()
    ax_s.plot(np.arange(total_len), r, color=INK, lw=1.4)
    ax_s.set_title("r[n]: dos ecos + ruido", color=INK, pad=8, fontsize=10.5)
    ax_s.set_xlim(0, total_len)
    limpiar(ax_s, ejes=("bottom",))

    ax_g.clear()
    ax_g.plot(k, g, color=VERDE, lw=2.2)
    pico1_k = D0 + L - 1
    pico2_k = D1 + L - 1
    ax_g.axvline(pico1_k, color=AMBAR, lw=1.2, ls="--", alpha=0.7)
    ax_g.axvline(pico2_k, color=AMBAR, lw=1.2, ls="--", alpha=0.7)
    ax_g.set_title("salida del filtro adaptado g[n]", color=VERDE, pad=8,
                   fontsize=10.5)
    ax_g.set_xlim(0, total_len)
    limpiar(ax_g, ejes=("bottom", "left"))

    # criterio simple de resolucion: hay un valle entre los dos picos teoricos
    lo, hi = sorted([pico1_k, pico2_k])
    if hi > lo + 1:
        valle = g[lo:hi + 1].min()
        picos = max(g[max(lo - 1, 0)], g[min(hi + 1, len(g) - 1)])
        resuelto = valle < 0.75 * picos
    else:
        resuelto = False

    col = VERDE if resuelto else ROJO
    txt = "los dos ecos SE RESUELVEN" if resuelto else "los dos ecos SE CONFUNDEN"
    cartel.set_text(f"separación = {D:.1f} muestras, pulso "
                    f"{radio.value_selected}: {txt}")
    cartel.set_color(col)
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.21, "", ha="center", fontsize=11)

ax_radio = fig.add_axes([0.83, 0.83, 0.14, 0.14])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)
radio = RadioButtons(ax_radio, list(PULSOS.keys()), active=1)
for lbl in radio.labels:
    lbl.set_color(TXT)
    lbl.set_fontsize(8.5)
radio.on_clicked(dibujar)

s_D = estilo_slider(Slider(eje_slider(fig, 0.30, 0.135, 0.45),
                           "separación entre ecos", 1, 14, valinit=4,
                           valfmt="%.0f"))
s_sigma = estilo_slider(Slider(eje_slider(fig, 0.30, 0.085, 0.45),
                               "nivel de ruido", 0.0, 1.2, valinit=0.15,
                               valfmt="%.2f"))
s_D.on_changed(dibujar)
s_sigma.on_changed(dibujar)

pie(fig, "el rectangular tiene un pico ancho: dos ecos cercanos se funden. "
         "Barker-13 y el chirp tienen autocorrelacion angosta: se resuelven "
         "con la MISMA energia.")
dibujar()
plt.show()
