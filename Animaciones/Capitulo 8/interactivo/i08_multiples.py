"""Interactivo - Dos mediciones y las ecuaciones normales.

Estimamos Y con X1 y X2. Mové las tres correlaciones (X1-X2, X1-Y, X2-Y)
y mirá cómo el sistema C_XX a = c_XY reparte los pesos a1, a2. Cuando X1 y
X2 son casi lo mismo (rho12 -> 1), el sistema evita contar dos veces la
misma información.

    python i08_multiples.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

fig = plt.figure(figsize=(11.5, 6.2))
fig.suptitle(r"Dos mediciones:   $C_{XX}\,a = c_{XY}$",
             color=TXT, fontsize=13, y=0.965)
ax_bar = fig.add_axes([0.09, 0.34, 0.42, 0.54])
ax_txt = fig.add_axes([0.56, 0.30, 0.40, 0.58])
ax_txt.axis("off")


def resolver(r12, r1y, r2y):
    C = np.array([[1.0, r12], [r12, 1.0]])
    c = np.array([r1y, r2y])
    try:
        a = np.linalg.solve(C, c)
    except np.linalg.LinAlgError:
        a = np.array([np.nan, np.nan])
    # varianza explicada = c^T a  (con sigma_Y = 1)
    expl = float(c @ a) if np.all(np.isfinite(a)) else np.nan
    return a, np.clip(expl, 0, 1)


def dibujar(*_):
    r12, r1y, r2y = s_r12.val, s_r1y.val, s_r2y.val
    a, expl = resolver(r12, r1y, r2y)

    ax_bar.clear()
    if np.all(np.isfinite(a)):
        ax_bar.bar(["$a_1$", "$a_2$"], a, width=0.5,
                   color=[AZUL, AMBAR], alpha=0.9)
    ax_bar.axhline(0, color=INK, lw=1)
    ax_bar.set_ylim(-1.6, 1.6)
    ax_bar.set_title("pesos que resuelven el sistema", color=TXT, pad=8)
    limpiar(ax_bar, ejes=("left",))

    # comparacion: pesos "ingenuos" si uno ignora la correlacion X1-X2
    a_ing = np.array([r1y, r2y])
    ax_bar.plot([0, 1], a_ing, "o", color=VERDE, ms=9)
    ax_bar.text(0.5, 1.45, "verde = pesos ingenuos (ignorando $\\rho_{12}$)",
                ha="center", color=VERDE, fontsize=9)

    # mathtext (lo que usa ax.text) no soporta \begin{bmatrix};
    # se arma el sistema con lineas de texto monospaciado
    ax_txt.clear(); ax_txt.axis("off")
    a1s = f"{a[0]:+.2f}" if np.isfinite(a[0]) else "  —"
    a2s = f"{a[1]:+.2f}" if np.isfinite(a[1]) else "  —"
    bloque = (
        "sistema  C_XX a = c_XY\n"
        "\n"
        f"   [  1.00   {r12:+.2f} ] [ a1 ]   [ {r1y:+.2f} ]\n"
        f"   [ {r12:+.2f}   1.00 ] [ a2 ] = [ {r2y:+.2f} ]\n"
    )
    ax_txt.text(0.0, 0.95, bloque, transform=ax_txt.transAxes, color=TXT,
                fontsize=11, va="top", family="monospace")
    ax_txt.text(0.0, 0.52, f"a1 = {a1s}     a2 = {a2s}",
                transform=ax_txt.transAxes, color=AMBAR, fontsize=13, va="top",
                family="monospace")
    ax_txt.text(0.0, 0.40, f"varianza de Y explicada:  {100 * expl:.0f}%",
                transform=ax_txt.transAxes, color=VERDE, fontsize=12, va="top")

    if r12 > 0.85:
        ax_txt.text(0.0, 0.26,
                    "X1 y X2 casi idénticas: el sistema reparte\n"
                    "el peso en vez de sumar dos veces la misma\n"
                    "medición",
                    transform=ax_txt.transAxes, color=INK, fontsize=10,
                    va="top")
    fig.canvas.draw_idle()


s_r12 = estilo_slider(Slider(eje_slider(fig, 0.20, 0.155, 0.58),
                             r"$\rho_{X_1 X_2}$", -0.9, 0.95, valinit=0.3,
                             valfmt="%.2f"))
s_r1y = estilo_slider(Slider(eje_slider(fig, 0.20, 0.095, 0.58),
                             r"$\rho_{X_1 Y}$", -0.9, 0.9, valinit=0.6,
                             valfmt="%.2f"))
s_r2y = estilo_slider(Slider(eje_slider(fig, 0.20, 0.035, 0.58),
                             r"$\rho_{X_2 Y}$", -0.9, 0.9, valinit=0.5,
                             valfmt="%.2f"))
for s in (s_r12, s_r1y, s_r2y):
    s.on_changed(dibujar)

pie(fig, "Los pesos ingenuos (verde) ignoran que X1 y X2 se pisan. El "
         "sistema C_XX a = c_XY lo corrige automáticamente.")
dibujar()
plt.show()
