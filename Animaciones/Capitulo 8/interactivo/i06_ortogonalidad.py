"""Interactivo - LMMSE como proyección ortogonal.

Los vectores son las variables centradas: |X~| = sigma_X, |Y~| = sigma_Y,
y el ángulo entre ellos tiene coseno rho. Mové 'a' (el múltiplo de X~) y
mirá el largo del error. El mínimo aparece cuando el error queda
perpendicular a X~.

    python i06_ortogonalidad.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

fig = plt.figure(figsize=(11.5, 6.0))
fig.suptitle("Estimar linealmente = proyectar ortogonalmente", color=TXT,
             fontsize=13, y=0.965)
ax = fig.add_axes([0.06, 0.26, 0.55, 0.62])
ax_bar = fig.add_axes([0.72, 0.26, 0.07, 0.62])


def dibujar(*_):
    sx, sy, rho = s_sx.val, s_sy.val, s_rho.val
    th = np.arccos(np.clip(rho, -0.999, 0.999))
    a = s_a.val

    vx = np.array([sx, 0.0])
    vy = np.array([sy * np.cos(th), sy * np.sin(th)])
    proj = a * vx

    ax.clear()
    ax.axhline(0, color=INK, lw=0.8, alpha=0.4)
    ax.axvline(0, color=INK, lw=0.8, alpha=0.4)
    ax.annotate("", xy=vx, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=AZUL, lw=3))
    ax.annotate("", xy=vy, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=VERDE, lw=3))
    ax.annotate("", xy=proj, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=AMBAR, lw=2.5))
    ax.plot([proj[0], vy[0]], [proj[1], vy[1]], color=ROJO, lw=2.5)

    ax.text(vx[0] + 0.1, -0.18, r"$\tilde{X}$", color=AZUL, fontsize=13)
    ax.text(vy[0] - 0.1, vy[1] + 0.12, r"$\tilde{Y}$", color=VERDE, fontsize=13)
    ax.text(proj[0], -0.22, r"$a\tilde{X}$", color=AMBAR, fontsize=11,
            ha="center")

    lim = max(sx, sy) * 1.25 + 0.4
    ax.set_xlim(-0.6, lim); ax.set_ylim(-0.7, lim)
    ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    limpiar(ax, ejes=())

    err = float(np.linalg.norm(vy - proj))
    a_opt = sy * np.cos(th) / sx
    err_min = sy * np.sin(th)
    perp = abs(a - a_opt) < 0.02
    ax.text(0.02, 0.95, f"|error| = {err:.3f}", transform=ax.transAxes,
            color=ROJO, fontsize=10)
    ax.text(0.02, 0.88,
            f"mínimo = $\\sigma_Y\\sin\\theta$ = {err_min:.3f}",
            transform=ax.transAxes, color=VERDE, fontsize=9.5)
    ax.text(0.02, 0.81, r"$\rho = \cos\theta$" + f" = {np.cos(th):.2f}",
            transform=ax.transAxes, color=MAGENTA, fontsize=9.5)
    if perp:
        ax.text(0.5, 0.03, "error perpendicular a X~   →   este es el óptimo",
                transform=ax.transAxes, color=AMBAR, fontsize=10, ha="center",
                weight="bold")

    ax_bar.clear()
    ax_bar.bar([0], [err], width=0.7, color=ROJO, alpha=0.9)
    ax_bar.axhline(err_min, color=VERDE, lw=2, ls=(0, (4, 3)))
    ax_bar.set_ylim(0, sy * 1.1); ax_bar.set_xlim(-0.6, 0.6)
    ax_bar.set_xticks([]); ax_bar.set_title("|error|", color=ROJO, fontsize=9,
                                            pad=8)
    limpiar(ax_bar, ejes=("left",))
    fig.canvas.draw_idle()


s_a = estilo_slider(Slider(eje_slider(fig, 0.20, 0.15, 0.55),
                           "a", -0.5, 1.6, valinit=0.2, valfmt="%.2f"))
s_rho = estilo_slider(Slider(eje_slider(fig, 0.20, 0.10, 0.55),
                             r"$\rho$", 0.0, 0.95, valinit=0.6, valfmt="%.2f"))
s_sx = estilo_slider(Slider(eje_slider(fig, 0.20, 0.055, 0.24),
                            r"$\sigma_X$", 1.0, 3.0, valinit=2.4, valfmt="%.1f"))
s_sy = estilo_slider(Slider(eje_slider(fig, 0.55, 0.055, 0.20),
                            r"$\sigma_Y$", 1.0, 3.0, valinit=2.2, valfmt="%.1f"))
for s in (s_a, s_rho, s_sx, s_sy):
    s.on_changed(dibujar)

pie(fig, "El error mínimo (Pitágoras) es sigma_Y·sin(theta) = "
         "sqrt(sigma_Y^2 (1 - rho^2)): la misma fórmula del LMMSE.")
dibujar()
plt.show()
