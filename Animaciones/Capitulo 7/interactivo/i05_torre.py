"""Interactivo - La propiedad de la torre.

Mové las proporciones y las medias de cada grupo, y mirá cómo la media
total es siempre el promedio pesado de las medias por grupo.

    python i05_torre.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

fig = plt.figure(figsize=(11.8, 6.2))
fig.suptitle("La propiedad de la torre:  $E[X] = E\\,[\\,E[X\\mid Y]\\,]$",
             color=TXT, fontsize=13, y=0.965)

ax_b = fig.add_axes([0.08, 0.55, 0.84, 0.22])     # la barra de proporciones
ax_d = fig.add_axes([0.08, 0.26, 0.84, 0.24])     # las densidades por grupo
cuenta = fig.text(0.5, 0.185, "", ha="center", fontsize=12, color=AMBAR)


def dibujar(*_):
    p1 = s_p.val
    p2 = 1 - p1
    m1, m2 = s_m1.val, s_m2.val
    media = p1 * m1 + p2 * m2

    # ---- barra de proporciones
    ax_b.clear()
    ax_b.barh([0], [p1], color=AZUL, alpha=0.55, height=0.6)
    ax_b.barh([0], [p2], left=[p1], color=MAGENTA, alpha=0.55, height=0.6)
    ax_b.text(p1 / 2, 0, f"grupo A\n{p1:.0%}", ha="center", va="center",
              color=TXT, fontsize=10)
    ax_b.text(p1 + p2 / 2, 0, f"grupo B\n{p2:.0%}", ha="center", va="center",
              color=TXT, fontsize=10)
    ax_b.set_xlim(0, 1); ax_b.set_ylim(-0.45, 0.45)
    ax_b.set_xticks([]); ax_b.set_yticks([])
    ax_b.set_title("la variable Y es el grupo", color=INK, pad=8, fontsize=10)
    limpiar(ax_b, ejes=())

    # ---- densidades por grupo, pesadas
    lo, hi = min(m1, m2) - 22, max(m1, m2) + 22
    x = np.linspace(lo, hi, 1200)
    s = 6.0
    g1 = p1 * np.exp(-((x - m1) ** 2) / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))
    g2 = p2 * np.exp(-((x - m2) ** 2) / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))

    ax_d.clear()
    ax_d.plot(x, g1, color=AZUL, lw=2.2)
    ax_d.fill_between(x, 0, g1, color=AZUL, alpha=0.22)
    ax_d.plot(x, g2, color=MAGENTA, lw=2.2)
    ax_d.fill_between(x, 0, g2, color=MAGENTA, alpha=0.22)
    ax_d.plot(x, g1 + g2, color=INK, lw=1.6, ls=(0, (5, 3)))

    for m, c, nom in ((m1, AZUL, "A"), (m2, MAGENTA, "B")):
        ax_d.axvline(m, color=c, ls=(0, (3, 3)), lw=1.3)
        ax_d.text(m, (g1 + g2).max() * 1.04, f"{m:.0f}", color=c,
                  ha="center", fontsize=9.5)
    ax_d.axvline(media, color=AMBAR, lw=2.6)
    ax_d.text(media, (g1 + g2).max() * 1.16, f"E[X] = {media:.2f}",
              color=AMBAR, ha="center", fontsize=11, weight="bold")

    ax_d.set_xlim(lo, hi); ax_d.set_ylim(0, (g1 + g2).max() * 1.32)
    ax_d.set_xlabel("altura (cm)"); ax_d.set_yticks([])
    limpiar(ax_d, ejes=("bottom",))

    cuenta.set_text(f"{p1:.2f} · {m1:.0f}  +  {p2:.2f} · {m2:.0f}  "
                    f"=  {media:.2f} cm")
    fig.canvas.draw_idle()


s_p = estilo_slider(Slider(eje_slider(fig, 0.26, 0.115, 0.48),
                           "proporción del grupo A", 0.02, 0.98,
                           valinit=0.40, valfmt="%.2f"))
s_m1 = estilo_slider(Slider(eje_slider(fig, 0.26, 0.075, 0.48),
                            "media del grupo A", 140, 200, valinit=175,
                            valfmt="%.0f"))
s_m2 = estilo_slider(Slider(eje_slider(fig, 0.26, 0.035, 0.48),
                            "media del grupo B", 140, 200, valinit=162,
                            valfmt="%.0f"))
for s in (s_p, s_m1, s_m2):
    s.on_changed(dibujar)

pie(fig, "La media total siempre cae entre las dos medias de grupo, más cerca "
         "de la del grupo más numeroso.")
dibujar()
plt.show()
