"""Interactivo - Desempeno del detector: dos gaussianas separadas por E.

g|H0 ~ N(0, sigma^2 E), g|H1 ~ N(E, sigma^2 E). Todo el desempeno depende
del cociente E/sigma^2 y de la probabilidad a priori p1.

Move el SNR (en dB) y p1, y mira como se mueven las campanas, el umbral
optimo y P_FA, P_M, P_e.

    python i03_desempeno.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import erfc, sqrt
from estilo_int import *


def Q(x):
    return 0.5 * erfc(x / sqrt(2))


def gauss(x, mu, sigma):
    return np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))


R = np.linspace(-6, 12, 1400)
snr_db_range = np.linspace(-4, 14, 300)

fig = plt.figure(figsize=(12.2, 6.4))
fig.suptitle("Desempeño del detector: dos gaussianas separadas por E",
             color=TXT, fontsize=13, y=0.965)

ax_g = fig.add_axes([0.07, 0.36, 0.42, 0.52])
ax_c = fig.add_axes([0.56, 0.36, 0.40, 0.52])


def dibujar(*_):
    snr_db, p1 = s_snr.val, s_p1.val
    p0 = 1 - p1
    E = 10 ** (snr_db / 10)
    sigma = 1.0
    sg = sigma * np.sqrt(E)

    # umbral optimo: iguala p0 f(g|H0) = p1 f(g|H1)
    if p0 <= 0:
        gamma = -1e9
    elif p1 <= 0:
        gamma = 1e9
    else:
        gamma = sg ** 2 / E * np.log(p0 / p1) + E / 2

    pfa = Q((gamma - 0) / sg) if sg > 0 else (1.0 if gamma < 0 else 0.0)
    pm = 1 - Q((gamma - E) / sg) if sg > 0 else (0.0 if gamma < E else 1.0)
    pe = p0 * pfa + p1 * pm

    ax_g.clear()
    f0 = gauss(R, 0, sg)
    f1 = gauss(R, E, sg)
    ax_g.plot(R, f0, color=AZUL, lw=2.4, label=r"$f(g|H_0)$")
    ax_g.plot(R, f1, color=VERDE, lw=2.4, label=r"$f(g|H_1)$")
    ax_g.fill_between(R, 0, f0, where=R >= gamma, color=ROJO, alpha=0.35)
    ax_g.fill_between(R, 0, f1, where=R <= gamma, color=AMBAR, alpha=0.35)
    ax_g.axvline(gamma, color=ROJO, lw=1.8, ls="--")
    ax_g.set_title("densidades de g", color=TXT, pad=10)
    ax_g.set_xlabel("g"); ax_g.set_xlim(R[0], R[-1])
    ax_g.set_ylim(0, max(f0.max(), f1.max()) * 1.25); ax_g.set_yticks([])
    ax_g.legend(loc="upper right", fontsize=9)
    limpiar(ax_g, ejes=("bottom",))

    # P_e(SNR) con el umbral optimo de cada punto, para el mismo p1 actual
    snr_lin = 10 ** (snr_db_range / 10)
    pe_curve = []
    for s in snr_lin:
        sgk = sigma * np.sqrt(s)
        if p0 <= 0:
            g_k = -1e9
        elif p1 <= 0:
            g_k = 1e9
        else:
            g_k = sgk ** 2 / s * np.log(p0 / p1) + s / 2
        pfak = Q(g_k / sgk) if sgk > 0 else (1.0 if g_k < 0 else 0.0)
        pmk = 1 - Q((g_k - s) / sgk) if sgk > 0 else (0.0 if g_k < s else 1.0)
        pe_curve.append(p0 * pfak + p1 * pmk)
    pe_curve = np.array(pe_curve)

    ax_c.clear()
    ax_c.plot(snr_db_range, pe_curve, color=AMBAR, lw=2.6)
    ax_c.plot([snr_db], [pe], "o", color=TXT, ms=9)
    ax_c.set_title(r"$P_e$ vs SNR (dB)", color=AMBAR, pad=10)
    ax_c.set_xlabel("SNR (dB)"); ax_c.set_xlim(snr_db_range[0], snr_db_range[-1])
    ax_c.set_ylim(0, 0.55)
    limpiar(ax_c, ejes=("bottom", "left"))

    cartel.set_text(f"γ óptimo = {gamma:.2f}     P_FA = {pfa:.3f}     "
                    f"P_M = {pm:.3f}     P_e = {pe:.3f}")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.20, "", ha="center", fontsize=10, color=INK)

s_snr = estilo_slider(Slider(eje_slider(fig, 0.20, 0.11, 0.60),
                             "SNR = E/σ² (dB)", -4, 14, valinit=6.0,
                             valfmt="%.1f"))
s_p1 = estilo_slider(Slider(eje_slider(fig, 0.20, 0.06, 0.60),
                            "a priori  p1", 0.05, 0.95, valinit=0.5,
                            valfmt="%.2f"))
s_snr.on_changed(dibujar)
s_p1.on_changed(dibujar)

pie(fig, "g|H0 ~ N(0, sigma^2 E), g|H1 ~ N(E, sigma^2 E).  El umbral optimo "
         "se mueve con p1; el desempeno depende solo de E/sigma^2.")
dibujar()
plt.show()
