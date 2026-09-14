"""Interactivo - La trampa de la prevalencia.

Mové la prevalencia, la sensibilidad y la especificidad, y mirá qué pasa
con el valor predictivo positivo. Es el resultado más contraintuitivo del
capítulo: un test excelente sobre una enfermedad rara da positivos que
casi no significan nada.

    python i04_medico.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

POB = 100000

fig = plt.figure(figsize=(12.0, 6.4))
fig.suptitle("¿Qué significa realmente un resultado positivo?", color=TXT,
             fontsize=13, y=0.965)

ax_barra = fig.add_axes([0.07, 0.62, 0.55, 0.18])
ax_vpp = fig.add_axes([0.72, 0.34, 0.24, 0.46])
ax_curva = fig.add_axes([0.07, 0.30, 0.55, 0.22])


def dibujar(*_):
    prev = s_prev.val / 100
    sens = s_sens.val / 100
    espec = s_espec.val / 100

    enf = POB * prev
    san = POB - enf
    vp = enf * sens                    # verdaderos positivos
    fn = enf * (1 - sens)              # falsos negativos
    fp = san * (1 - espec)             # falsos positivos
    vn = san * espec                   # verdaderos negativos
    vpp = vp / (vp + fp) if (vp + fp) > 0 else 0
    vpn = vn / (vn + fn) if (vn + fn) > 0 else 0

    # ---- barra apilada de los que dan positivo
    ax_barra.clear()
    tot_pos = vp + fp
    if tot_pos > 0:
        ax_barra.barh([0], [vp / tot_pos * 100], color=MAGENTA, height=0.55,
                      label=f"enfermos ({vp:,.0f})".replace(",", "."))
        ax_barra.barh([0], [fp / tot_pos * 100], left=[vp / tot_pos * 100],
                      color=ROJO, height=0.55,
                      label=f"sanos mal clasificados ({fp:,.0f})".replace(",", "."))
    ax_barra.set_xlim(0, 100); ax_barra.set_ylim(-0.6, 0.9)
    ax_barra.set_yticks([])
    ax_barra.set_xlabel("composición de los que dan POSITIVO (%)", fontsize=9)
    ax_barra.legend(loc="lower center", bbox_to_anchor=(0.5, -1.15), ncols=2,
                    fontsize=9)
    limpiar(ax_barra, ejes=("bottom",))

    # ---- el numero grande
    ax_vpp.clear()
    ax_vpp.set_xticks([]); ax_vpp.set_yticks([])
    limpiar(ax_vpp, ejes=())
    col = VERDE if vpp > 0.5 else (AMBAR if vpp > 0.2 else ROJO)
    ax_vpp.text(0.5, 0.66, f"{vpp*100:.1f}%", ha="center", va="center",
                color=col, fontsize=34, weight="bold")
    ax_vpp.text(0.5, 0.35, "valor predictivo\npositivo", ha="center", va="center",
                color=INK, fontsize=10.5, linespacing=1.4)
    ax_vpp.text(0.5, 0.12, f"VPN = {vpn*100:.2f}%", ha="center", va="center",
                color=INK, fontsize=9.5)
    ax_vpp.text(0.5, 0.90, "Si te da positivo,\nprobabilidad de estar enfermo",
                ha="center", va="center", color=TXT, fontsize=9.5,
                linespacing=1.4)

    # ---- VPP en funcion de la prevalencia
    ax_curva.clear()
    pv = np.logspace(-3, 0, 400)
    v = (pv * sens) / (pv * sens + (1 - pv) * (1 - espec))
    ax_curva.semilogx(pv * 100, v * 100, color=AMBAR, lw=2.2)
    ax_curva.plot([prev * 100], [vpp * 100], "o", color=col, ms=9)
    ax_curva.set_xlim(0.1, 100); ax_curva.set_ylim(0, 105)
    ax_curva.set_xlabel("prevalencia (%)  —  escala logarítmica")
    ax_curva.set_ylabel("VPP (%)", fontsize=9)
    ax_curva.tick_params(labelsize=8.5)
    limpiar(ax_curva)
    fig.canvas.draw_idle()


s_prev = estilo_slider(Slider(eje_slider(fig, 0.22, 0.155, 0.55),
                              "prevalencia (%)", 0.1, 50.0, valinit=0.1,
                              valfmt="%.2f"))
s_sens = estilo_slider(Slider(eje_slider(fig, 0.22, 0.100, 0.55),
                              "sensibilidad (%)", 50.0, 99.9, valinit=99.0,
                              valfmt="%.1f"))
s_espec = estilo_slider(Slider(eje_slider(fig, 0.22, 0.045, 0.55),
                               "especificidad (%)", 50.0, 99.99, valinit=99.0,
                               valfmt="%.2f"))
for s in (s_prev, s_sens, s_espec):
    s.on_changed(dibujar)

pie(fig, "Probá bajar la prevalencia con el test al 99%: el VPP se desploma. "
         "Es el término P(H₁) de la regla MAP haciendo su trabajo.")
dibujar()
plt.show()
