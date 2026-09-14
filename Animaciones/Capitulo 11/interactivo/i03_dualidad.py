"""Interactivo - Dualidad tiempo/frecuencia.

Mové alfa y mirá cómo la autocorrelación y el espectro se deforman al
mismo tiempo en sentidos opuestos. El área total no cambia.

    python i03_dualidad.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

TAU = np.linspace(-4, 4, 900)
W = np.linspace(-14, 14, 1400)

fig = plt.figure(figsize=(11.5, 5.4))
fig.suptitle("Autocorrelación y espectro: el mismo contenido, dos vistas",
             color=TXT, fontsize=13, y=0.965)

ax_r = fig.add_axes([0.07, 0.28, 0.38, 0.56])
ax_s = fig.add_axes([0.56, 0.28, 0.38, 0.56])


def dibujar(alfa):
    for a in (ax_r, ax_s):
        a.clear()

    R = np.exp(-alfa * np.abs(TAU))
    ax_r.plot(TAU, R, color=VERDE, lw=2.4)
    ax_r.fill_between(TAU, 0, R, color=VERDE, alpha=0.16)
    ax_r.set_title(r"$R_{xx}(\tau)=e^{-\alpha|\tau|}$", color=VERDE, pad=10)
    ax_r.set_xlabel(r"$\tau$")
    ax_r.set_ylim(-0.05, 1.15)
    ax_r.set_xlim(TAU[0], TAU[-1])
    ax_r.set_yticks([0, 1])
    limpiar(ax_r)

    S = 2 * alfa / (alfa ** 2 + W ** 2)
    ax_s.plot(W, S, color=AZUL, lw=2.4)
    ax_s.fill_between(W, 0, S, color=AZUL, alpha=0.16)
    ax_s.set_title(r"$S_{xx}(j\omega)=\dfrac{2\alpha}{\alpha^2+\omega^2}$",
                   color=AZUL, pad=10)
    ax_s.set_xlabel(r"$\omega$")
    ax_s.set_ylim(-0.15, 4.4)
    ax_s.set_xlim(W[0], W[-1])
    ax_s.set_yticks([])
    limpiar(ax_s, ejes=("bottom",))

    # ancho a media altura de cada uno, para hacer explicita la dualidad
    t_half = np.log(2) / alfa
    ax_r.axvspan(-t_half, t_half, color=VERDE, alpha=0.10)
    ax_s.axvspan(-alfa, alfa, color=AZUL, alpha=0.10)
    ax_r.text(0.02, 0.94, f"ancho ≈ {2*t_half:.2f}", transform=ax_r.transAxes,
              color=VERDE, fontsize=9)
    ax_s.text(0.02, 0.94, f"ancho ≈ {2*alfa:.2f}", transform=ax_s.transAxes,
              color=AZUL, fontsize=9)

    area = np.trapezoid(S, W) / (2 * np.pi)
    ax_s.text(0.98, 0.94, f"área/2π = {area:.3f}  (= $R_{{xx}}(0)$)",
              transform=ax_s.transAxes, color=INK, fontsize=9, ha="right")
    fig.canvas.draw_idle()


s_alfa = estilo_slider(Slider(eje_slider(fig, 0.25, 0.11, 0.5),
                              r"$\alpha$", 0.3, 5.0, valinit=1.0,
                              valfmt="%.2f"))
s_alfa.on_changed(lambda v: dibujar(v))

pie(fig, "Angosta en tiempo ⇔ ancha en frecuencia. El área total (la potencia) "
         "se mantiene constante.")
dibujar(s_alfa.val)
plt.show()
