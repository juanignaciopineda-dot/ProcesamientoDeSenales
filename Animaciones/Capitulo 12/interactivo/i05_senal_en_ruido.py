"""Interactivo - Senal en ruido: el filtro reparte ganancia segun el SNR.

x[n] = y[n] + v[n].  El filtro de Wiener H = D_yy / (D_yy + D_vv) no hace
nada mas que darle ganancia a las bandas donde la senal domina y cortarle
a las bandas donde manda el ruido.

Move el color de la senal (rho) y el nivel de ruido, y mira como el filtro
sigue al SNR banda por banda.

    python i05_senal_en_ruido.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

W = np.linspace(-np.pi, np.pi, 1200)
ESC_Y = 2.0

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Senal en ruido: el filtro sigue al SNR, banda por banda",
             color=TXT, fontsize=13, y=0.965)

ax_s = fig.add_axes([0.06, 0.34, 0.42, 0.54])
ax_h = fig.add_axes([0.55, 0.34, 0.42, 0.54])


def dibujar(*_):
    rho, sv = s_rho.val, s_sv.val
    if abs(rho) > 0.5:
        rho = np.sign(rho) * 0.5
    Dyy = ESC_Y * (1 + 2 * rho * np.cos(W))
    Dvv = np.full_like(W, sv)
    H = Dyy / (Dyy + Dvv)
    snr = Dyy / Dvv

    ax_s.clear()
    ax_s.plot(W, Dyy, color=VERDE, lw=2.6, label=r"$D_{yy}$")
    ax_s.fill_between(W, 0, Dyy, color=VERDE, alpha=0.16)
    ax_s.plot(W, Dvv, color=ROJO, lw=2.6, label=r"$D_{vv}$")
    # sombreado: verde donde la senal gana, rojo donde gana el ruido
    ax_s.fill_between(W, 0, np.maximum(Dyy, Dvv), where=Dyy >= Dvv,
                      color=VERDE, alpha=0.08)
    ax_s.fill_between(W, 0, np.maximum(Dyy, Dvv), where=Dyy < Dvv,
                      color=ROJO, alpha=0.10)
    ax_s.axhline(0, color=INK, lw=1.0)
    ax_s.set_title("espectros de senal y ruido", color=TXT, pad=10)
    ax_s.set_xlabel(r"$\Omega$"); ax_s.set_xlim(-np.pi, np.pi)
    ax_s.set_xticks([-np.pi, 0, np.pi]); ax_s.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_s.set_ylim(0, 6.4); ax_s.set_yticks([])
    ax_s.legend(loc="upper right", fontsize=9)
    limpiar(ax_s, ejes=("bottom",))

    ax_h.clear()
    ax_h.plot(W, H, color=AZUL, lw=2.8)
    ax_h.fill_between(W, 0, H, color=AZUL, alpha=0.16)
    ax_h.axhline(1, color=INK, lw=0.9, alpha=0.5)
    ax_h.set_title(r"ganancia del filtro  $H(e^{j\Omega})$", color=AZUL, pad=10)
    ax_h.set_xlabel(r"$\Omega$"); ax_h.set_xlim(-np.pi, np.pi)
    ax_h.set_xticks([-np.pi, 0, np.pi]); ax_h.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_h.set_ylim(0, 1.15); ax_h.set_yticks([0, 0.5, 1])
    limpiar(ax_h, ejes=("bottom", "left"))

    hmin, hmax = H.min(), H.max()
    cartel.set_text(f"H entre {hmin:.2f} y {hmax:.2f}.   "
                    f"D_yy >> D_vv  =>  H -> 1     "
                    f"D_vv >> D_yy  =>  H -> 0")
    info.set_text(f"SNR maximo = {snr.max():.2f}      SNR minimo = {snr.min():.2f}")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.215, "", ha="center", fontsize=9.5, color=INK)
info = fig.text(0.5, 0.175, "", ha="center", fontsize=10, color=AZUL)

s_rho = estilo_slider(Slider(eje_slider(fig, 0.22, 0.10, 0.56),
                             r"color de la senal $\rho$", -0.5, 0.5,
                             valinit=0.4, valfmt="%.2f"))
s_sv = estilo_slider(Slider(eje_slider(fig, 0.22, 0.055, 0.56),
                            r"nivel de ruido $\sigma_v^2$", 0.05, 5.0,
                            valinit=1.0, valfmt="%.2f"))
s_rho.on_changed(dibujar)
s_sv.on_changed(dibujar)

pie(fig, "rho > 0: senal lenta, potencia en baja frecuencia.  rho < 0: senal "
         "que alterna, potencia en alta.  El filtro se acomoda solo.")
dibujar()
plt.show()
