"""Interactivo - Wiener no causal: el problema se desacopla en frecuencia.

Senal en ruido: x[n] = y[n] + v[n], con v blanco. El filtro optimo es
H = D_yy / (D_yy + D_vv), y se calcula frecuencia por frecuencia sin que
una banda afecte a las otras.

Move la forma del espectro de la senal y el nivel de ruido, y compara la
funcion de coherencia (el "coeficiente de correlacion, banda por banda")
con lo que pasa en el filtro.

    python i04_no_causal.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

W = np.linspace(-np.pi, np.pi, 1200)

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Wiener no causal: cada frecuencia, un problema independiente",
             color=TXT, fontsize=13, y=0.965)

ax_s = fig.add_axes([0.06, 0.34, 0.42, 0.54])
ax_h = fig.add_axes([0.55, 0.34, 0.42, 0.54])


def dibujar(*_):
    w0, bw, sv = s_w0.val, s_bw.val, s_sv.val
    # espectro de la senal: campana centrada en +-w0
    Dyy = 3.2 * (np.exp(-((W - w0) / bw) ** 2) + np.exp(-((W + w0) / bw) ** 2))
    Dyy += 0.15
    Dvv = np.full_like(W, sv)
    Dxx = Dyy + Dvv
    H = Dyy / Dxx
    coh2 = Dyy / Dxx                       # |gamma_yx|^2 = D_yy/D_xx aca
    mmse = np.trapezoid(Dyy * (1 - coh2), W) / (2 * np.pi)
    pot_y = np.trapezoid(Dyy, W) / (2 * np.pi)

    ax_s.clear()
    ax_s.plot(W, Dyy, color=VERDE, lw=2.4, label=r"$D_{yy}$ (senal)")
    ax_s.fill_between(W, 0, Dyy, color=VERDE, alpha=0.16)
    ax_s.plot(W, Dvv, color=ROJO, lw=2.4, label=r"$D_{vv}$ (ruido)")
    ax_s.axhline(0, color=INK, lw=1.0)
    ax_s.set_title("espectros", color=TXT, pad=10)
    ax_s.set_xlabel(r"$\Omega$"); ax_s.set_xlim(-np.pi, np.pi)
    ax_s.set_xticks([-np.pi, 0, np.pi]); ax_s.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_s.set_ylim(0, 7.2); ax_s.set_yticks([])
    ax_s.legend(loc="upper right", fontsize=8.5)
    limpiar(ax_s, ejes=("bottom",))

    ax_h.clear()
    ax_h.plot(W, H, color=AZUL, lw=2.6, label=r"$H = D_{yy}/D_{xx}$")
    ax_h.plot(W, coh2, color=AMBAR, lw=2.0, ls=(0, (4, 3)),
              label=r"$|\gamma_{yx}|^2$")
    ax_h.fill_between(W, 0, H, color=AZUL, alpha=0.14)
    ax_h.axhline(1, color=INK, lw=0.9, alpha=0.5)
    ax_h.set_title("filtro y coherencia", color=AZUL, pad=10)
    ax_h.set_xlabel(r"$\Omega$"); ax_h.set_xlim(-np.pi, np.pi)
    ax_h.set_xticks([-np.pi, 0, np.pi]); ax_h.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_h.set_ylim(0, 1.15); ax_h.set_yticks([0, 0.5, 1])
    ax_h.legend(loc="upper right", fontsize=8.5)
    limpiar(ax_h, ejes=("bottom", "left"))

    cartel.set_text("donde la coherencia se acerca a 1 la estimacion es buena; "
                    "donde cae a 0, el filtro no puede hacer nada")
    info.set_text(f"MMSE = {mmse:.3f}      potencia de la senal = {pot_y:.3f}"
                  f"      (compara con  sigma_Y^2 (1 - rho^2)  del cap. 8)")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.215, "", ha="center", fontsize=9.5, color=INK)
info = fig.text(0.5, 0.175, "", ha="center", fontsize=10, color=VERDE)

s_w0 = estilo_slider(Slider(eje_slider(fig, 0.20, 0.115, 0.6),
                            r"centro de la banda $\Omega_0$", 0.0, 2.6,
                            valinit=1.1, valfmt="%.2f"))
s_bw = estilo_slider(Slider(eje_slider(fig, 0.20, 0.075, 0.6),
                            "ancho de banda", 0.25, 2.0, valinit=0.7,
                            valfmt="%.2f"))
s_sv = estilo_slider(Slider(eje_slider(fig, 0.20, 0.035, 0.6),
                            r"nivel de ruido $\sigma_v^2$", 0.05, 4.0,
                            valinit=0.8, valfmt="%.2f"))
for s in (s_w0, s_bw, s_sv):
    s.on_changed(dibujar)

pie(fig, "El filtro actua de forma independiente en cada frecuencia: lo que "
         "hace en una banda no cambia lo que hace en las demas.")
dibujar()
plt.show()
