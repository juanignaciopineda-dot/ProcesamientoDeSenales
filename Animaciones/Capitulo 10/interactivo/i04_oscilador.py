"""Interactivo - El oscilador con fase aleatoria.

X(t) = A cos(w0 t + Theta). Con dispersion de fase en cero todas las
realizaciones estan alineadas y la media oscila (NO es WSS). Al abrir la
fase hacia el rango uniforme [-pi, pi] la media se aplana en cero: el
proceso se vuelve WSS.

    python i04_oscilador.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

T = np.linspace(0, 8, 700)
K = 24
_rng = np.random.default_rng(41)
AMPS = _rng.uniform(0.7, 1.5, K)
U = _rng.uniform(-1, 1, K)          # fases base, se escalan con la dispersion

fig = plt.figure(figsize=(12, 5.4))
fig.suptitle("El oscilador: la fase aleatoria es lo que aplana la media",
             color=TXT, fontsize=12, y=0.965)
ax = fig.add_axes([0.07, 0.32, 0.88, 0.54])


def dibujar(w0, disp):
    ax.clear()
    fases = disp * np.pi * U
    ondas = [AMPS[i] * np.cos(w0 * T + fases[i]) for i in range(K)]
    for o in ondas:
        ax.plot(T, o, color=INK, lw=0.7, alpha=0.45)
    mu = np.mean(ondas, axis=0)
    ax.plot(T, mu, color=TXT, lw=3.0, label=r"$\mu_X(t)$")
    ax.axhline(0, color=INK, lw=0.8)

    ax.set_xlabel("t")
    ax.set_xlim(0, 8)
    ax.set_ylim(-1.8, 1.8)
    ax.legend(loc="upper right", fontsize=9)
    pico = np.max(np.abs(mu))
    estado = ("media casi plana  ->  WSS" if pico < 0.15
              else "media que oscila  ->  NO es WSS")
    col = VERDE if pico < 0.15 else ROJO
    ax.text(0.01, 0.05, f"|media| máx = {pico:.2f}     {estado}",
            transform=ax.transAxes, color=col, fontsize=11, va="bottom")
    limpiar(ax)
    fig.canvas.draw_idle()


s_w = estilo_slider(Slider(eje_slider(fig, 0.22, 0.15, 0.56), r"$\omega_0$",
                           1.0, 5.0, valinit=2.6, valfmt="%.2f"))
s_d = estilo_slider(Slider(eje_slider(fig, 0.22, 0.08, 0.56),
                           "dispersión de fase", 0.0, 1.0, valinit=0.0,
                           valfmt="%.2f"))
s_w.on_changed(lambda v: dibujar(s_w.val, s_d.val))
s_d.on_changed(lambda v: dibujar(s_w.val, s_d.val))

pie(fig, "Dispersión 1.0 = fase uniforme en [-pi, pi]: la media se anula y "
         "R_XX pasa a depender solo de t2 - t1.")
dibujar(s_w.val, s_d.val)
plt.show()
