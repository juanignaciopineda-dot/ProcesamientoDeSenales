"""Interactivo - Falsa alarma, miss y detección.

Mové el umbral y mirá las cuatro probabilidades cambiar en vivo. Mové
también la separación entre hipótesis (el SNR) y los a priori, y fijate
dónde queda el umbral que minimiza Pe.

    python i03_errores.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *

SIGMA = 1.0
R = np.linspace(-5, 9, 1400)


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


fig = plt.figure(figsize=(12.0, 6.4))
fig.suptitle("Falsa alarma, miss y detección: el compromiso del umbral",
             color=TXT, fontsize=13, y=0.965)
ax = fig.add_axes([0.06, 0.40, 0.60, 0.46])
ax_pe = fig.add_axes([0.73, 0.40, 0.24, 0.46])


def dibujar(*_):
    gam, d, p0 = s_gam.val, s_d.val, s_p0.val
    p1 = 1 - p0

    pfa = Q((gam - 0) / SIGMA)
    pd = Q((gam - d) / SIGMA)
    pm = 1 - pd
    pe = p0 * pfa + p1 * pm

    # umbral optimo (MAP): donde p0*f0 = p1*f1
    gam_opt = d / 2 + SIGMA ** 2 * np.log(p0 / p1) / d if d > 0 else 0.0
    pe_opt = p0 * Q(gam_opt / SIGMA) + p1 * (1 - Q((gam_opt - d) / SIGMA))

    ax.clear()
    f0, f1 = p0 * g(R, 0), p1 * g(R, d)
    ax.plot(R, f0, color=AZUL, lw=2.3, label=r"$p_0 f(r|H_0)$")
    ax.plot(R, f1, color=VERDE, lw=2.3, label=r"$p_1 f(r|H_1)$")
    ax.fill_between(R, 0, f0, where=R >= gam, color=ROJO, alpha=0.65)
    ax.fill_between(R, 0, f1, where=R <= gam, color=AMBAR, alpha=0.65)
    ax.axvline(gam, color=ROJO, lw=2.2, ls=(0, (4, 3)))
    ax.axvline(gam_opt, color=VERDE, lw=1.6, ls=(0, (2, 4)))
    ax.text(gam_opt, ax.get_ylim()[1] * 0.02, "  óptimo", color=VERDE,
            fontsize=8.5, rotation=90, va="bottom")
    ax.set_xlim(-5, 9); ax.set_ylim(0, 0.45)
    ax.set_xlabel("r"); ax.set_yticks([])
    ax.legend(loc="upper right", fontsize=9.5)
    limpiar(ax, ejes=("bottom",))

    txt = (f"$P_{{FA}}$ = {pfa:.4f}      $P_M$ = {pm:.4f}      "
           f"$P_D$ = {pd:.4f}")
    ax.text(0.5, -0.20, txt, transform=ax.transAxes, ha="center",
            color=INK, fontsize=11)

    # ---- Pe en funcion del umbral
    ax_pe.clear()
    gs = np.linspace(-4, 8, 500)
    pes = [p0 * Q(x / SIGMA) + p1 * (1 - Q((x - d) / SIGMA)) for x in gs]
    ax_pe.plot(gs, pes, color=AMBAR, lw=2.2)
    ax_pe.plot([gam], [pe], "o", color=ROJO, ms=9)
    ax_pe.plot([gam_opt], [pe_opt], "o", color=VERDE, ms=7)
    ax_pe.set_xlabel("umbral γ"); ax_pe.set_ylabel("$P_e$")
    ax_pe.set_xlim(-4, 8); ax_pe.set_ylim(0, max(p0, p1) * 1.1)
    limpiar(ax_pe)
    exceso = (pe - pe_opt) / pe_opt * 100 if pe_opt > 0 else 0
    ax_pe.text(0.5, 1.06, f"$P_e$ = {pe:.4f}   (mínimo: {pe_opt:.4f})",
               transform=ax_pe.transAxes, ha="center", color=TXT, fontsize=10)
    if exceso > 1:
        ax_pe.text(0.5, 0.94, f"+{exceso:.0f}% sobre el mínimo",
                   transform=ax_pe.transAxes, ha="center", color=ROJO,
                   fontsize=9)
    fig.canvas.draw_idle()


s_gam = estilo_slider(Slider(eje_slider(fig, 0.20, 0.185, 0.58),
                             "umbral γ", -3.0, 7.0, valinit=1.3, valfmt="%.2f"))
s_d = estilo_slider(Slider(eje_slider(fig, 0.20, 0.120, 0.58),
                           "separación (SNR)", 0.2, 6.0, valinit=2.6,
                           valfmt="%.2f"))
s_p0 = estilo_slider(Slider(eje_slider(fig, 0.20, 0.055, 0.58),
                            r"$p_0$", 0.05, 0.95, valinit=0.5, valfmt="%.2f"))
for s in (s_gam, s_d, s_p0):
    s.on_changed(dibujar)

pie(fig, "Bajar una cola sube la otra. La línea verde marca el umbral MAP, "
         "el que minimiza Pe para esos a priori.")
dibujar()
plt.show()
