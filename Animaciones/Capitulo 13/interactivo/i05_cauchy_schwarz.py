"""Interactivo - Cauchy-Schwarz: por que el filtro adaptado maximiza el SNR.

h[n] se arma como una mezcla de la señal s (normalizada) y una direccion
ORTOGONAL a s, controlada por un angulo theta. SNR_out = SNR_in * cos^2
(theta): maximo solo cuando h es colineal con s (theta = 0), que es
exactamente el filtro adaptado.

    python i05_cauchy_schwarz.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

L = 12
rng = np.random.default_rng(1)
n = np.arange(L)
s = np.array([0.3, 0.9, 1.6, 1.9, 1.5, 0.7, -0.2, -0.6, -0.3, 0.1, 0.2, 0.0])
s_hat = s / np.linalg.norm(s)

# direccion ortogonal a s, fija (Gram-Schmidt sobre un vector aleatorio)
v = rng.normal(0, 1, L)
v_perp = v - np.dot(v, s_hat) * s_hat
v_perp_hat = v_perp / np.linalg.norm(v_perp)

E = np.sum(s ** 2)
sigma = 1.0
snr_in = E / sigma ** 2

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Cauchy-Schwarz: el SNR de salida cae como cos²θ fuera del "
             "filtro adaptado", color=TXT, fontsize=12.5, y=0.965)

ax_h = fig.add_axes([0.06, 0.34, 0.42, 0.54])
ax_snr = fig.add_axes([0.55, 0.34, 0.42, 0.54])

thetas = np.linspace(0, np.pi, 300)
snr_curve = snr_in * np.cos(thetas) ** 2


def dibujar(*_):
    theta = s_theta.val
    h_hat = np.cos(theta) * s_hat + np.sin(theta) * v_perp_hat
    snr_out = snr_in * np.cos(theta) ** 2

    ax_h.clear()
    ax_h.stem(n - 0.12, s_hat, linefmt=AMBAR, markerfmt="o", basefmt=" ",
             label=r"$\hat s[n]$")
    ax_h.stem(n + 0.12, h_hat, linefmt=AZUL, markerfmt="o", basefmt=" ",
             label=r"$h[-n]$")
    ax_h.axhline(0, color=INK, lw=1.0)
    ax_h.set_title("señal (ámbar) contra filtro (azul), ambos de energía 1",
                   color=TXT, pad=10, fontsize=10.5)
    ax_h.set_xlabel("n")
    ax_h.set_ylim(-0.75, 0.75)
    ax_h.legend(loc="upper right", fontsize=9)
    limpiar(ax_h, ejes=("bottom",))

    ax_snr.clear()
    ax_snr.plot(thetas, snr_curve, color=VERDE, lw=2.6)
    ax_snr.axhline(snr_in, color=INK, lw=1.0, ls="--", alpha=0.6)
    ax_snr.plot([theta], [snr_out], "o", color=TXT, ms=10)
    ax_snr.set_title(r"$\text{SNR}_{out}=\text{SNR}_{in}\cos^2\theta$",
                     color=VERDE, pad=10, fontsize=10.5)
    ax_snr.set_xlabel(r"$\theta$ (rad)")
    ax_snr.set_xlim(0, np.pi); ax_snr.set_xticks([0, np.pi / 2, np.pi])
    ax_snr.set_xticklabels(["0", "π/2", "π"])
    ax_snr.set_ylim(0, snr_in * 1.15)
    limpiar(ax_snr, ejes=("bottom", "left"))

    cartel.set_text(f"SNR_in = {snr_in:.2f}     SNR_out = {snr_out:.2f}     "
                    f"({100 * np.cos(theta) ** 2:.0f}% del máximo)")
    if theta < 0.05:
        cartel.set_color(VERDE)
    else:
        cartel.set_color(INK)
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.20, "", ha="center", fontsize=10.5)

s_theta = estilo_slider(Slider(eje_slider(fig, 0.22, 0.10, 0.56),
                               r"ángulo θ entre h y s", 0.0, np.pi,
                               valinit=0.5, valfmt="%.2f"))
s_theta.on_changed(dibujar)

pie(fig, "theta=0: h[-n]=s[n], el filtro adaptado, y el SNR de salida iguala "
         "al de entrada. Cualquier otro angulo pierde SNR sin ganar nada.")
dibujar()
plt.show()
