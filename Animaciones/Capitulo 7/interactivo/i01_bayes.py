"""Interactivo - Bayes y el test médico.

Mové la prevalencia, la sensibilidad y la especificidad, y mirá qué pasa
con la probabilidad de estar realmente enfermo dado un positivo. La
prevalencia pesa muchísimo más de lo que uno espera.

    python i01_bayes.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

N_POB = 10000

fig = plt.figure(figsize=(12.0, 6.4))
fig.suptitle("Bayes: ¿qué probabilidad de estar enfermo tenés con un positivo?",
             color=TXT, fontsize=13, y=0.965)

ax_pob = fig.add_axes([0.06, 0.40, 0.44, 0.46])     # torta de la poblacion
ax_pos = fig.add_axes([0.57, 0.40, 0.38, 0.46])     # barras de los positivos
cartel = fig.text(0.5, 0.30, "", ha="center", fontsize=13, weight="bold")
detalle = fig.text(0.5, 0.245, "", ha="center", fontsize=9.5, color=INK)


def dibujar(*_):
    prev, sens, espec = s_prev.val, s_sens.val, s_espec.val

    enfermos = N_POB * prev
    sanos = N_POB - enfermos
    vp = enfermos * sens                 # verdaderos positivos
    fn = enfermos - vp
    fp = sanos * (1 - espec)             # falsos positivos
    vn = sanos - fp
    vpp = vp / (vp + fp) if (vp + fp) > 0 else 0.0

    # ---- panel izquierdo: la poblacion, en escala
    ax_pob.clear()
    ax_pob.barh([1], [sanos], color=AZUL, alpha=0.45, height=0.55,
                label=f"sanos  ({sanos/N_POB:.1%})")
    ax_pob.barh([0], [enfermos], color=ROJO, alpha=0.95, height=0.55,
                label=f"enfermos  ({prev:.2%})")
    ax_pob.set_xlim(0, N_POB)
    ax_pob.set_ylim(-0.6, 1.6)
    ax_pob.set_yticks([])
    ax_pob.set_xlabel(f"personas (de {N_POB:,})".replace(",", " "))
    ax_pob.set_title("la población", color=TXT, pad=10, fontsize=11)
    # abajo a la derecha: arriba tapaba la barra de los sanos
    ax_pob.legend(loc="lower right", fontsize=9)
    limpiar(ax_pob, ejes=("bottom",))

    # ---- panel derecho: solo los que dieron positivo
    ax_pos.clear()
    ax_pos.bar([0], [vp], color=ROJO, width=0.55, alpha=0.95)
    ax_pos.bar([1], [fp], color=AMBAR, width=0.55, alpha=0.95)
    ax_pos.set_xticks([0, 1])
    ax_pos.set_xticklabels([f"enfermos\n{vp:.0f}", f"sanos\n{fp:.0f}"])
    ax_pos.set_ylim(0, max(vp, fp) * 1.25 + 1)
    ax_pos.set_ylabel("personas")
    ax_pos.set_title("de los que dieron POSITIVO…", color=TXT, pad=10,
                     fontsize=11)
    limpiar(ax_pos)
    for x, v in ((0, vp), (1, fp)):
        ax_pos.text(x, v + max(vp, fp) * 0.04, f"{v/(vp+fp):.1%}",
                    ha="center", color=TXT, fontsize=10, weight="bold")

    col = VERDE if vpp > 0.5 else (AMBAR if vpp > 0.2 else ROJO)
    cartel.set_text(f"P(enfermo | +)  =  {vpp:.1%}")
    cartel.set_color(col)
    if vpp < 0.5:
        detalle.set_text("la mayoría de los positivos son personas sanas: "
                         "los falsos positivos ganan por cantidad")
    else:
        detalle.set_text("acá el test sí es informativo: los verdaderos "
                         "positivos superan a los falsos")
    fig.canvas.draw_idle()


s_prev = estilo_slider(Slider(eje_slider(fig, 0.28, 0.155, 0.46),
                              "prevalencia", 0.0005, 0.5, valinit=0.01,
                              valfmt="%.4f"))
s_sens = estilo_slider(Slider(eje_slider(fig, 0.28, 0.100, 0.46),
                              "sensibilidad  P(+|enf)", 0.50, 1.0,
                              valinit=0.99, valfmt="%.3f"))
s_espec = estilo_slider(Slider(eje_slider(fig, 0.28, 0.045, 0.46),
                               "especificidad  P(−|sano)", 0.50, 1.0,
                               valinit=0.95, valfmt="%.3f"))
for s in (s_prev, s_sens, s_espec):
    s.on_changed(dibujar)

dibujar()
plt.show()
