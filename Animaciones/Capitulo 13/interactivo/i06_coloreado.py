"""Interactivo - Deteccion en ruido coloreado: H = S* / (D_vv/sigma^2).

Move el centro de banda de la señal y el color del ruido (polo de un
AR(1)) y mira como el filtro se concentra donde el SNR de entrada es
alto, y como cambia el desempeño E_p/sigma^2 frente al caso de ruido
blanco con la misma energía.

    python i06_coloreado.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

W = np.linspace(-np.pi, np.pi, 1200)


def Smag2(w, centro, ancho=0.30):
    return np.exp(-((w - centro) ** 2) / ancho) + np.exp(-((w + centro) ** 2) / ancho)


def Dvv(w, a):
    return (1 - a ** 2) / (1 - 2 * a * np.cos(w) + a ** 2)


fig = plt.figure(figsize=(12.2, 6.4))
fig.suptitle("Detección en ruido coloreado: H sigue al SNR de entrada, "
             "banda por banda", color=TXT, fontsize=12.5, y=0.965)

ax_s = fig.add_axes([0.07, 0.36, 0.40, 0.52])
ax_h = fig.add_axes([0.57, 0.36, 0.40, 0.52])


def dibujar(*_):
    centro, a = s_centro.val, s_a.val
    S2 = Smag2(W, centro)
    D = Dvv(W, a)
    H = S2 / D

    Ep_coloreado = np.trapezoid(S2 / D, W) / (2 * np.pi)
    Ep_blanco = np.trapezoid(S2, W) / (2 * np.pi)  # mismo caso con D_vv = 1

    ax_s.clear()
    ax_s.plot(W, S2, color=VERDE, lw=2.4, label=r"$|S|^2$")
    ax_s.fill_between(W, 0, S2, color=VERDE, alpha=0.14)
    ax_s.plot(W, D, color=ROJO, lw=2.4, label=r"$D_{vv}$")
    ax_s.set_title("señal y ruido", color=TXT, pad=10, fontsize=11)
    ax_s.set_xlabel(r"$\Omega$"); ax_s.set_xlim(-np.pi, np.pi)
    ax_s.set_xticks([-np.pi, 0, np.pi]); ax_s.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_s.set_ylim(0, 2.3); ax_s.set_yticks([])
    ax_s.legend(loc="upper right", fontsize=9)
    limpiar(ax_s, ejes=("bottom",))

    ax_h.clear()
    ax_h.plot(W, H, color=AZUL, lw=2.8)
    ax_h.fill_between(W, 0, H, color=AZUL, alpha=0.16)
    ax_h.set_title(r"$|H(e^{j\Omega})|\propto |S|^2/D_{vv}$", color=AZUL,
                   pad=10, fontsize=11)
    ax_h.set_xlabel(r"$\Omega$"); ax_h.set_xlim(-np.pi, np.pi)
    ax_h.set_xticks([-np.pi, 0, np.pi]); ax_h.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_h.set_ylim(0, max(4.0, H.max() * 1.15)); ax_h.set_yticks([])
    limpiar(ax_h, ejes=("bottom",))

    cartel.set_text(f"centro de banda de la señal: {centro:.2f} rad     "
                    f"polo del ruido a = {a:.2f}")
    info.set_text(f"E_p/σ² (ruido coloreado) = {Ep_coloreado:.3f}      "
                  f"E_p/σ² (mismo caso, ruido blanco) = {Ep_blanco:.3f}")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.20, "", ha="center", fontsize=10, color=INK)
info = fig.text(0.5, 0.165, "", ha="center", fontsize=10.5, color=AMBAR)

s_centro = estilo_slider(Slider(eje_slider(fig, 0.22, 0.10, 0.56),
                                "centro de banda de la señal", 0.1, 3.0,
                                valinit=1.4, valfmt="%.2f"))
s_a = estilo_slider(Slider(eje_slider(fig, 0.22, 0.055, 0.56),
                           "polo del ruido  a  (color)", -0.9, 0.9,
                           valinit=0.6, valfmt="%.2f"))
s_centro.on_changed(dibujar)
s_a.on_changed(dibujar)

pie(fig, "a > 0: ruido concentrado en baja frecuencia. Si la señal se aleja de "
         "esa banda, el SNR efectivo E_p/sigma^2 SUBE respecto del caso blanco: "
         "ahora la forma importa.")
dibujar()
plt.show()
