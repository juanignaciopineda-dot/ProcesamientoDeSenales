"""Interactivo - On-off contra antipodal: el precio de X = suma s0[n]s1[n].

Con energias iguales E, Pe = Q(sqrt((E-X)/(2 sigma^2))). Move el SNR
(E/sigma^2, en dB) y X/E entre -1 (antipodal) y +1 (senales identicas,
indistinguibles). X=0 es el caso ortogonal (on-off, salvo un corrimiento).

    python i08_antipodal.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


snr_db_range = np.linspace(-4, 12, 300)

fig = plt.figure(figsize=(12.2, 6.4))
fig.suptitle("On-off contra antipodal: el papel de X = Σ s₀[n]s₁[n]",
             color=TXT, fontsize=12.5, y=0.965)

ax_pe = fig.add_axes([0.07, 0.36, 0.42, 0.52])
ax_x = fig.add_axes([0.57, 0.36, 0.40, 0.52])


def dibujar(*_):
    snr_db, xr = s_snr.val, s_x.val
    snr_lin = 10 ** (snr_db_range / 10)

    def pe_de(snr, x_rel):
        return Q(np.sqrt(snr * (1 - x_rel) / 2))

    pe_actual = np.array([pe_de(s, xr) for s in snr_lin])
    pe_antipodal = np.array([pe_de(s, -1.0) for s in snr_lin])
    pe_ortogonal = np.array([pe_de(s, 0.0) for s in snr_lin])

    snr_pt = 10 ** (snr_db / 10)
    pe_pt = pe_de(snr_pt, xr)

    ax_pe.clear()
    ax_pe.plot(snr_db_range, pe_antipodal, color=VERDE, lw=2.2,
              label="antipodal (X/E=-1)")
    ax_pe.plot(snr_db_range, pe_ortogonal, color=AMBAR, lw=2.2,
              label="ortogonal (X/E=0)")
    ax_pe.plot(snr_db_range, pe_actual, color=AZUL, lw=2.8, ls="--",
              label=f"actual (X/E={xr:.2f})")
    ax_pe.plot([snr_db], [pe_pt], "o", color=TXT, ms=9)
    ax_pe.set_title(r"$P_e$ vs SNR (dB)", color=TXT, pad=10, fontsize=11)
    ax_pe.set_xlabel("E/σ² (dB)"); ax_pe.set_xlim(snr_db_range[0], snr_db_range[-1])
    ax_pe.set_ylim(0, 0.55)
    ax_pe.legend(loc="upper right", fontsize=8.5)
    limpiar(ax_pe, ejes=("bottom", "left"))

    xs = np.linspace(-1, 1, 200)
    pe_vs_x = np.array([pe_de(snr_pt, x) for x in xs])
    ax_x.clear()
    ax_x.plot(xs, pe_vs_x, color=MAGENTA, lw=2.6)
    ax_x.axvline(-1, color=VERDE, lw=1.2, ls="--", alpha=0.7)
    ax_x.axvline(0, color=AMBAR, lw=1.2, ls="--", alpha=0.7)
    ax_x.axvline(1, color=ROJO, lw=1.2, ls="--", alpha=0.7)
    ax_x.plot([xr], [pe_pt], "o", color=TXT, ms=9)
    ax_x.set_title(r"$P_e$ vs $X/E$, a SNR fijo", color=MAGENTA, pad=10,
                   fontsize=11)
    ax_x.set_xlabel("X/E"); ax_x.set_xlim(-1, 1)
    ax_x.set_ylim(0, 0.55)
    limpiar(ax_x, ejes=("bottom", "left"))

    cartel.set_text(f"E/σ² = {snr_db:.1f} dB     X/E = {xr:.2f}     "
                    f"P_e = {pe_pt:.4f}")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.20, "", ha="center", fontsize=10.5, color=INK)

s_snr = estilo_slider(Slider(eje_slider(fig, 0.22, 0.10, 0.56),
                             "SNR = E/σ² (dB)", -4, 12, valinit=4.0,
                             valfmt="%.1f"))
s_x = estilo_slider(Slider(eje_slider(fig, 0.22, 0.055, 0.56),
                           "X/E  (parecido entre s0 y s1)", -1.0, 1.0,
                           valinit=0.0, valfmt="%.2f"))
s_snr.on_changed(dibujar)
s_x.on_changed(dibujar)

pie(fig, "X/E = -1: antipodal, el mejor caso posible (Cauchy-Schwarz). "
         "X/E = +1: s0 = s1, indistinguibles, Pe = 0.5. X/E = 0: ortogonal, "
         "como on-off salvo un corrimiento.")
dibujar()
plt.show()
