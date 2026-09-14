"""Interactivo - Del Wiener causal al filtro de Kalman (caso escalar).

Planta en espacio de estados de orden 1:
    q[n+1] = a q[n] + w[n]      y[n] = q[n]      x[n] = y[n] + v[n]

Con r = sigma_w^2 / sigma_v^2, la ecuacion de factorizacion espectral se
reduce a un polinomio monico alpha(z) = z - p con |p| < 1, y el filtro de
Wiener causal es

    H(z) = (alpha(z) - a(z)) / alpha(z) = (a - p) z^-1 / (1 - p z^-1)

que es exactamente un observador con ganancia  l = p - a.  p sale de la
ecuacion de Riccati escalar.

Move el polo de la planta y la relacion de ruidos r.

    python i08_kalman.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

W = np.linspace(-np.pi, np.pi, 1200)

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Wiener causal = observador = filtro de Kalman (orden 1)",
             color=TXT, fontsize=13, y=0.965)

ax_z = fig.add_axes([0.06, 0.34, 0.30, 0.50])
ax_h = fig.add_axes([0.46, 0.34, 0.50, 0.50])


def resolver(a, r):
    """Riccati escalar (sigma_v^2 = 1):  M^2 + M(1 - a^2 - r) - r = 0."""
    c = 1 - a ** 2 - r
    M = (-c + np.sqrt(c ** 2 + 4 * r)) / 2        # raiz positiva
    p = a / (M + 1)                                # polo del observador
    P_filt = M / (M + 1)                           # var. del error filtrado
    l = p - a                                      # ganancia del observador
    return M, p, P_filt, l


def dibujar(*_):
    a = s_a.val
    r = 10 ** s_lr.val
    M, p, P_filt, l = resolver(a, r)

    Hmod = abs(a - p) / np.sqrt(1 + p ** 2 - 2 * p * np.cos(W))

    # ---- plano z
    ax_z.clear()
    th = np.linspace(0, 2 * np.pi, 400)
    ax_z.plot(np.cos(th), np.sin(th), color=INK, lw=1.4)
    ax_z.axhline(0, color=INK, lw=0.8, alpha=0.5)
    ax_z.axvline(0, color=INK, lw=0.8, alpha=0.5)
    ax_z.plot([a], [0], "x", color=AMBAR, ms=13, mew=3,
              label=f"polo planta  a = {a:.2f}")
    ax_z.plot([p], [0], "x", color=AZUL, ms=13, mew=3,
              label=f"polo observador  p = {p:.2f}")
    ax_z.set_aspect("equal")
    ax_z.set_xlim(-1.4, 1.4); ax_z.set_ylim(-1.4, 1.4)
    ax_z.set_xticks([-1, 0, 1]); ax_z.set_yticks([])
    ax_z.set_title("plano $z$", color=TXT, pad=10, fontsize=11)
    ax_z.legend(loc="upper center", bbox_to_anchor=(0.5, -0.03),
                fontsize=8.5, handletextpad=0.4)
    limpiar(ax_z, ejes=())

    # ---- respuesta del filtro
    ax_h.clear()
    ax_h.plot(W, Hmod, color=AZUL, lw=2.8)
    ax_h.fill_between(W, 0, Hmod, color=AZUL, alpha=0.16)
    ax_h.axhline(0, color=INK, lw=1.0)
    ax_h.set_title(r"$|H(e^{j\Omega})|$  del filtro de Wiener causal",
                   color=AZUL, pad=10, fontsize=11)
    ax_h.set_xlabel(r"$\Omega$"); ax_h.set_xlim(-np.pi, np.pi)
    ax_h.set_xticks([-np.pi, 0, np.pi]); ax_h.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_h.set_ylim(0, max(1.2, Hmod.max() * 1.15)); ax_h.set_yticks([])
    limpiar(ax_h, ejes=("bottom",))

    if r > 12:
        reg = "r grande: confio en la medicion; p -> 0, el observador reacciona rapido"
    elif r < 0.08:
        reg = "r chico: la medicion es ruidosa; p -> a, el observador casi no corrige"
    else:
        reg = "regimen intermedio: el observador mezcla modelo y medicion"
    cartel.set_text(reg)
    info.set_text(f"ganancia del observador  l = p - a = {l:.3f}       "
                  f"var. del error filtrado = {P_filt:.3f}       "
                  f"H(z) = ({a - p:.3f}) z^-1 / (1 - ({p:.3f}) z^-1)")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.20, "", ha="center", fontsize=9.6, color=INK)
info = fig.text(0.5, 0.16, "", ha="center", fontsize=9.6, color=VERDE)

s_a = estilo_slider(Slider(eje_slider(fig, 0.24, 0.075, 0.52),
                           "polo de la planta  a", -0.95, 0.95, valinit=0.7,
                           valfmt="%.2f"))
s_lr = estilo_slider(Slider(eje_slider(fig, 0.24, 0.035, 0.52),
                            r"$\log_{10} r$   (con  $r=\sigma_w^2/\sigma_v^2$)",
                            -2.0, 2.0, valinit=0.0, valfmt="%.2f"))
s_a.on_changed(dibujar)
s_lr.on_changed(dibujar)

pie(fig, "El mismo filtro por dos caminos: factorizacion espectral (Wiener) o "
         "LMMSE del estado (Kalman).  Aca alpha(z) = z - p sale de la Riccati "
         "escalar.")
dibujar()
plt.show()
