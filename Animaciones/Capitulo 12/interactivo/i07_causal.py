"""Interactivo - Wiener causal / prediccion: el factor de fase minima.

El proceso x[n] = w[n] + b w[n-1] (w blanco, varianza 1). Queremos
predecir x[n+1] con el presente y el pasado.

La pieza clave es F(z), el factor espectral de FASE MINIMA de S_xx: si el
cero de M(z) = 1 + b z^-1 ya esta dentro del circulo unidad, F = M. Si no,
hay que reflejarlo. El error de prediccion es MMSE = f0^2.

Move b y mira el cero cruzar el circulo.

    python i07_causal.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

W = np.linspace(-np.pi, np.pi, 1200)

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Prediccion causal: el factor espectral de fase minima",
             color=TXT, fontsize=13, y=0.965)

ax_z = fig.add_axes([0.06, 0.34, 0.30, 0.50])
ax_s = fig.add_axes([0.46, 0.34, 0.50, 0.50])


def dibujar(*_):
    b = s_b.val
    Sxx = 1 + b ** 2 + 2 * b * np.cos(W)          # |1 + b e^{-jW}|^2
    cero = -b                                      # cero de M(z)
    fuera = abs(b) > 1.0
    if not fuera:
        f0 = 1.0
        cero_mp = cero
        Ftxt = f"F(z) = 1 + ({b:.2f}) z^-1        (M ya es de fase minima)"
    else:
        f0 = abs(b)
        cero_mp = -1.0 / b
        Ftxt = (f"F(z) = {abs(b):.2f} (1 + ({-1/b:.2f}) z^-1)     "
                f"(cero reflejado de {cero:.2f} a {cero_mp:.2f})")
    mmse = f0 ** 2
    var_next = 1 + b ** 2
    rho = b / (1 + b ** 2)

    # ---- plano z
    ax_z.clear()
    th = np.linspace(0, 2 * np.pi, 400)
    ax_z.plot(np.cos(th), np.sin(th), color=INK, lw=1.4)
    ax_z.axhline(0, color=INK, lw=0.8, alpha=0.5)
    ax_z.axvline(0, color=INK, lw=0.8, alpha=0.5)
    if fuera:
        ax_z.plot([cero], [0], "o", color=ROJO, ms=11, mfc="none", mew=2.2,
                  alpha=0.55)
        ax_z.plot([cero_mp], [0], "o", color=AZUL, ms=12, mfc="none", mew=2.6)
        ax_z.annotate("", xy=(cero_mp, 0.12), xytext=(np.clip(cero, -1.9, 1.9), 0.12),
                      arrowprops=dict(arrowstyle="->", color=INK, lw=1.3))
    else:
        ax_z.plot([cero_mp], [0], "o", color=AZUL, ms=12, mfc="none", mew=2.6)
    ax_z.set_aspect("equal")
    ax_z.set_xlim(-2.4, 2.4); ax_z.set_ylim(-1.5, 1.5)
    ax_z.set_xticks([-1, 0, 1]); ax_z.set_yticks([])
    ax_z.set_title("plano $z$: cero de $M(z)$", color=AZUL, pad=10, fontsize=11)
    limpiar(ax_z, ejes=("bottom",))

    # ---- espectro
    ax_s.clear()
    ax_s.plot(W, Sxx, color=AMBAR, lw=2.6)
    ax_s.fill_between(W, 0, Sxx, color=AMBAR, alpha=0.16)
    ax_s.axhline(0, color=INK, lw=1.0)
    ax_s.set_title(r"$S_{xx}(e^{j\Omega}) = |1 + b\,e^{-j\Omega}|^2$",
                   color=AMBAR, pad=10, fontsize=11)
    ax_s.set_xlabel(r"$\Omega$"); ax_s.set_xlim(-np.pi, np.pi)
    ax_s.set_xticks([-np.pi, 0, np.pi]); ax_s.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_s.set_ylim(0, max(4.5, Sxx.max() * 1.15)); ax_s.set_yticks([])
    limpiar(ax_s, ejes=("bottom",))

    col = ROJO if fuera else INK
    cartel.set_text(Ftxt)
    cartel.set_color(col)
    info.set_text(f"MMSE de prediccion = f0^2 = {mmse:.3f}      "
                  f"Var(x[n+1]) = {var_next:.3f}      "
                  f"rho(x[n], x[n+1]) = {rho:.3f}")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.20, "", ha="center", fontsize=10, color=INK)
info = fig.text(0.5, 0.16, "", ha="center", fontsize=10, color=VERDE)

s_b = estilo_slider(Slider(eje_slider(fig, 0.30, 0.075, 0.46),
                           "coeficiente  b", -2.5, 2.5, valinit=0.6,
                           valfmt="%.2f"))
s_b.on_changed(dibujar)

pie(fig, "x[n] = w[n] + b w[n-1].  Con |b| < 1 el cero ya esta adentro: F = M "
         "y la prediccion baja el error de 1+b^2 a 1.  Con |b| > 1 hay que "
         "reflejar el cero y se paga: MMSE = b^2.")
dibujar()
plt.show()
