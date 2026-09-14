"""Interactivo - Deconvolucion: por que no alcanza con invertir.

La senal pasa por un sensor G(z) que la borronea y despues se le suma
ruido. El filtro inverso 1/G amplifica el ruido justo donde |G| es chico.
Wiener invierte donde puede y se frena donde no.

Move el polo del sensor (cuanto borronea) y el nivel de ruido.

    python i06_deconvolucion.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

W = np.linspace(-np.pi, np.pi, 1400)

fig = plt.figure(figsize=(12.0, 6.2))
fig.suptitle("Deconvolucion: primero limpiar, despues invertir", color=TXT,
             fontsize=13, y=0.965)

ax = fig.add_axes([0.10, 0.34, 0.82, 0.54])


def dibujar(*_):
    a, sv = s_a.val, s_sv.val
    # G(z) = 1 / (1 - a z^-1): sensor pasabajos
    modG = 1.0 / np.sqrt(1 - 2 * a * np.cos(W) + a ** 2)
    modG2 = modG ** 2
    G0 = 1.0 / np.sqrt(1 - 2 * a + a ** 2)         # |G| en continua
    gan = modG / G0                                 # normalizado a 1 en DC
    Drr = modG2                                     # senal r = G y, con D_yy plano
    inv = 1.0 / modG                                # |1/G|
    wiener = inv * Drr / (Drr + sv)                 # |H_Wiener|
    tope = 6.0
    inv_c = np.minimum(inv / inv.min(), tope)       # escala relativa
    wien_c = np.minimum(wiener / inv.min(), tope)

    ax.clear()
    ax.plot(W, gan * 2.0, color=AMBAR, lw=2.4,
            label=r"$|G|$  (sensor: deja pasar poco en alta frec.)")
    ax.plot(W, inv_c, color=ROJO, lw=2.6,
            label=r"$|1/G|$  (explota donde solo queda ruido)")
    ax.plot(W, wien_c, color=AZUL, lw=3.0,
            label=r"$|H_{Wiener}|$  (invierte donde puede, se frena donde no)")
    ax.axhline(0, color=INK, lw=1.0)
    ax.set_xlabel(r"$\Omega$"); ax.set_xlim(-np.pi, np.pi)
    ax.set_xticks([-np.pi, 0, np.pi]); ax.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax.set_ylim(0, tope + 0.3); ax.set_yticks([])
    ax.legend(loc="upper center", fontsize=9)
    limpiar(ax, ejes=("bottom",))

    cartel.set_text(r"$H = \dfrac{1}{G}\cdot\dfrac{D_{rr}}{D_{rr}+D_{vv}}$"
                    "   :   el segundo factor es el que decide cuanto "
                    "invertir en cada banda")
    info.set_text(f"polo del sensor a = {a:.2f}   (mas cerca de 1 = mas "
                  f"borroneo)        ruido sigma_v^2 = {sv:.2f}")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.205, "", ha="center", fontsize=10.5, color=INK)
info = fig.text(0.5, 0.16, "", ha="center", fontsize=9.5, color=INK)

s_a = estilo_slider(Slider(eje_slider(fig, 0.22, 0.09, 0.56),
                           "polo del sensor  a", 0.0, 0.9, valinit=0.7,
                           valfmt="%.2f"))
s_sv = estilo_slider(Slider(eje_slider(fig, 0.22, 0.045, 0.56),
                            r"nivel de ruido $\sigma_v^2$", 0.02, 3.0,
                            valinit=0.5, valfmt="%.2f"))
s_a.on_changed(dibujar)
s_sv.on_changed(dibujar)

pie(fig, "Con poco ruido, Wiener tiende al filtro inverso.  Con mucho ruido, "
         "se abstiene.  El que manda es el SNR de cada banda.")
dibujar()
plt.show()
