"""Interactivo - Las variables aleatorias como vectores.

Mové rho y los desvíos: el ángulo entre los vectores es exactamente
arccos(rho). Perpendiculares significa no correlacionadas.

    python i08_vectorial.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

_rng = np.random.default_rng(17)
_A = _rng.normal(0, 1, 380)
_B = _rng.normal(0, 1, 380)

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("ρ es el coseno del ángulo entre los vectores centrados",
             color=TXT, fontsize=13, y=0.965)

ax_v = fig.add_axes([0.06, 0.36, 0.38, 0.52])      # los vectores
ax_n = fig.add_axes([0.52, 0.36, 0.28, 0.52])      # la nube correspondiente
panel = fig.text(0.845, 0.80, "", ha="left", va="top", fontsize=11.5,
                 color=INK)


def dibujar(*_):
    rho, sx, sy = s_rho.val, s_sx.val, s_sy.val
    r = np.clip(rho, -0.999, 0.999)
    th = np.arccos(r)

    # ---- los vectores
    ax_v.clear()
    ax_v.arrow(0, 0, sx, 0, color=AZUL, width=0.018, head_width=0.09,
               head_length=0.13, length_includes_head=True)
    ax_v.text(sx * 1.02, -0.13, r"$\tilde{X}$", color=AZUL, fontsize=13)
    vx, vy = sy * np.cos(th), sy * np.sin(th)
    ax_v.arrow(0, 0, vx, vy, color=VERDE, width=0.018, head_width=0.09,
               head_length=0.13, length_includes_head=True)
    ax_v.text(vx * 1.04, vy * 1.04 + 0.06, r"$\tilde{Y}$", color=VERDE,
              fontsize=13)

    # el arco del angulo
    arco = np.linspace(0, th, 80)
    rad = 0.42
    ax_v.plot(rad * np.cos(arco), rad * np.sin(arco), color=AMBAR, lw=2.0)
    ax_v.text(0.60 * np.cos(th / 2), 0.60 * np.sin(th / 2), r"$\theta$",
              color=AMBAR, fontsize=13, ha="center", va="center")

    # la proyeccion de Y sobre X: eso es lo que el capitulo 8 va a usar
    proy = sy * r
    ax_v.plot([vx, proy], [vy, 0], color=INK, ls=(0, (3, 3)), lw=1.3)
    ax_v.plot([0, proy], [0, 0], color=AMBAR, lw=4.5, alpha=0.55)
    ax_v.text(proy / 2, -0.26, r"$\sigma_Y\cos\theta$", color=AMBAR,
              fontsize=9.5, ha="center")

    lim = max(sx, sy) * 1.35 + 0.25
    ax_v.set_xlim(-lim * 0.55, lim); ax_v.set_ylim(-lim * 0.42, lim)
    ax_v.set_xticks([]); ax_v.set_yticks([])
    ax_v.axhline(0, color=INK, lw=0.8, alpha=0.4)
    ax_v.axvline(0, color=INK, lw=0.8, alpha=0.4)
    ax_v.set_aspect("equal")
    limpiar(ax_v, ejes=())

    # ---- la nube que le corresponde
    x = sx * _A
    y = sy * (r * _A + np.sqrt(1 - r ** 2) * _B)
    ax_n.clear()
    ax_n.scatter(x, y, s=8, color=MAGENTA, alpha=0.55, linewidths=0)
    ax_n.axhline(0, color=INK, lw=0.9, alpha=0.5)
    ax_n.axvline(0, color=INK, lw=0.9, alpha=0.5)
    L = 3.6
    ax_n.set_xlim(-L, L); ax_n.set_ylim(-L, L)
    ax_n.set_xlabel("X"); ax_n.set_ylabel("Y")
    ax_n.set_aspect("equal")
    ax_n.set_title("la nube correspondiente", color=MAGENTA, pad=10,
                   fontsize=10.5)
    limpiar(ax_n)

    orto = "  ⟂  perpendiculares" if abs(r) < 0.02 else ""
    panel.set_text(f"ρ = {rho:+.3f}\n\n"
                   f"θ = {np.degrees(th):.1f}°{orto}\n\n"
                   f"$\\|\\tilde{{X}}\\|=\\sigma_X$ = {sx:.2f}\n"
                   f"$\\|\\tilde{{Y}}\\|=\\sigma_Y$ = {sy:.2f}\n\n"
                   f"$\\sigma_{{X,Y}}=\\sigma_X\\sigma_Y\\cos\\theta$\n"
                   f"     = {sx*sy*r:+.3f}")
    fig.canvas.draw_idle()


s_rho = estilo_slider(Slider(eje_slider(fig, 0.28, 0.175, 0.44), r"$\rho$",
                             -0.99, 0.99, valinit=0.6, valfmt="%.3f"))
s_sx = estilo_slider(Slider(eje_slider(fig, 0.28, 0.120, 0.44), r"$\sigma_X$",
                            0.5, 2.2, valinit=1.6, valfmt="%.2f"))
s_sy = estilo_slider(Slider(eje_slider(fig, 0.28, 0.065, 0.44), r"$\sigma_Y$",
                            0.5, 2.2, valinit=1.2, valfmt="%.2f"))
for s in (s_rho, s_sx, s_sy):
    s.on_changed(dibujar)

pie(fig, "Poné ρ = 0 y mirá el ángulo: 90°. La franja naranja es la proyección "
         "de Ỹ sobre X̃, que en el capítulo 8 va a ser el estimador LMMSE.")
dibujar()
plt.show()
