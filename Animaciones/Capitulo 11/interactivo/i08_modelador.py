"""Interactivo - Filtro modelador: diseñar un espectro.

Mové el polo (módulo y ángulo) del filtro y mirá qué espectro produce a
partir de ruido blanco, y cómo se ve la señal resultante. Con el polo en
el origen volvés al blanco.

    python i08_modelador.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

N = 400
OMEGA = np.linspace(-np.pi, np.pi, 1200)
_rng = np.random.default_rng(21)
W_BASE = _rng.normal(0, 1, N + 200)     # mismo ruido siempre

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Filtro modelador: del ruido blanco al espectro que quieras",
             color=TXT, fontsize=13, y=0.965)

ax_z = fig.add_axes([0.05, 0.30, 0.235, 0.56])
ax_s = fig.add_axes([0.36, 0.30, 0.28, 0.56])
ax_t = fig.add_axes([0.70, 0.30, 0.27, 0.56])


def dibujar(*_):
    r, th = s_r.val, s_th.val

    # ---- plano z
    ax_z.clear()
    t = np.linspace(0, 2 * np.pi, 400)
    ax_z.plot(np.cos(t), np.sin(t), color=INK, lw=1.4)
    ax_z.axhline(0, color=INK, lw=0.8, alpha=0.5)
    ax_z.axvline(0, color=INK, lw=0.8, alpha=0.5)
    for s in (+1, -1):
        ax_z.plot(r * np.cos(s * th), r * np.sin(s * th), "x", color=ROJO,
                  ms=11, mew=2.4)
    ax_z.set_aspect("equal")
    ax_z.set_xlim(-1.4, 1.4); ax_z.set_ylim(-1.4, 1.4)
    ax_z.set_xticks([]); ax_z.set_yticks([])
    ax_z.set_title("plano $z$: par de polos", color=ROJO, pad=10, fontsize=11)
    limpiar(ax_z, ejes=())
    ax_z.text(0, -1.32, "estable si |polo| < 1", color=INK, fontsize=8.5,
              ha="center")

    # ---- espectro |H|^2 de un par de polos conjugados
    z = np.exp(1j * OMEGA)
    H = 1.0 / ((1 - r * np.exp(1j * th) / z) * (1 - r * np.exp(-1j * th) / z))
    D = np.abs(H) ** 2
    D = D / D.max() * 2.5

    ax_s.clear()
    ax_s.plot(OMEGA, D, color=AMBAR, lw=2.5)
    ax_s.fill_between(OMEGA, 0, D, color=AMBAR, alpha=0.18)
    ax_s.set_xlim(-np.pi, np.pi); ax_s.set_ylim(0, 3.0)
    ax_s.set_xticks([-np.pi, 0, np.pi])
    ax_s.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_s.set_yticks([])
    ax_s.set_xlabel(r"$\Omega$")
    ax_s.set_title(r"$D_{xx}=|H(e^{j\Omega})|^2$", color=AMBAR, pad=10,
                   fontsize=11)
    limpiar(ax_s, ejes=("bottom",))
    for s in (+1, -1):
        ax_s.axvline(s * th, color=ROJO, lw=1.2, ls=(0, (3, 3)), alpha=0.7)

    # ---- realizacion: filtrado recursivo de segundo orden
    a1, a2 = -2 * r * np.cos(th), r ** 2
    x = np.zeros(len(W_BASE))
    for n in range(2, len(W_BASE)):
        x[n] = W_BASE[n] - a1 * x[n - 1] - a2 * x[n - 2]
    # se muestra un tramo corto: con 400 muestras en un panel angosto la
    # oscilacion se empasta y no se ve la resonancia
    x = x[200:400]
    x = x / (np.std(x) if np.std(x) > 0 else 1.0)

    ax_t.clear()
    ax_t.plot(np.arange(len(x)), x, color=VERDE, lw=1.4)
    ax_t.axhline(0, color=INK, lw=0.9, alpha=0.6)
    ax_t.set_xlim(0, len(x) - 1); ax_t.set_ylim(-4.4, 4.4)
    ax_t.set_yticks([]); ax_t.set_xlabel("n")
    ax_t.set_title("la señal que sale", color=VERDE, pad=10, fontsize=11)
    limpiar(ax_t, ejes=("bottom",))

    if r < 0.05:
        msg = "polo casi en el origen: sigue siendo blanco"
    elif th < 0.35:
        msg = "polos cerca de Ω=0: señal lenta, espectro pasabajos"
    elif th > np.pi - 0.35:
        msg = "polos cerca de Ω=π: la señal alterna de signo"
    else:
        msg = f"resonancia en Ω ≈ {th:.2f}: la señal oscila a esa frecuencia"
    # dentro del eje, para no pisar la fila de sliders
    ax_t.text(0.5, 0.955, msg, transform=ax_t.transAxes, color=INK,
              fontsize=8.8, ha="center", va="top")
    fig.canvas.draw_idle()


s_r = estilo_slider(Slider(eje_slider(fig, 0.22, 0.155, 0.55),
                           "módulo del polo", 0.0, 0.97, valinit=0.85,
                           valfmt="%.3f"))
s_th = estilo_slider(Slider(eje_slider(fig, 0.22, 0.085, 0.55),
                            r"ángulo del polo $\theta$", 0.0, np.pi,
                            valinit=0.9, valfmt="%.3f"))
s_r.on_changed(dibujar)
s_th.on_changed(dibujar)

pie(fig, "El mismo ruido blanco entra siempre: todo lo que ves cambiar lo hace "
         "el filtro. Acercá el polo al círculo unidad y mirá la resonancia.")
dibujar()
plt.show()
