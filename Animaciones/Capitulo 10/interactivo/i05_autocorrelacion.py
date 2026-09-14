"""Interactivo - La autocorrelacion como solapamiento deslizante.

Arriba: la senal y una copia corrida tau, con el producto punto a punto
sombreado. Abajo: R_xx(tau), con el punto marcado en el tau actual. El
slider alfa cambia que tan rapido se descorrelaciona la senal.

    python i05_autocorrelacion.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

T = np.linspace(-7, 7, 1400)
TAU_MAX = 5.0


def senal(alfa):
    rng = np.random.default_rng(9)
    y = np.zeros_like(T)
    for _ in range(80):
        f = rng.uniform(0.05, 1.2) * alfa
        y += np.sin(2 * np.pi * f * T + rng.uniform(0, 2 * np.pi))
    return 1.1 * y / np.std(y)


TAUS = np.linspace(-TAU_MAX, TAU_MAX, 241)

fig = plt.figure(figsize=(12, 6.0))
fig.suptitle("Autocorrelación: la señal contra una copia de sí misma corrida",
             color=TXT, fontsize=12, y=0.97)
ax_t = fig.add_axes([0.07, 0.56, 0.88, 0.33])
ax_r = fig.add_axes([0.07, 0.27, 0.88, 0.22])


def R_de(x):
    n = len(x)
    out = []
    for tau in TAUS:
        k = int(round(tau / (T[1] - T[0])))
        if k >= 0:
            a, b = x[k:], x[:n - k] if k > 0 else x
        else:
            a, b = x[:n + k], x[-k:]
        out.append(np.mean(a * b))
    return np.array(out)


def dibujar(alfa, tau):
    ax_t.clear()
    ax_r.clear()
    x = senal(alfa)
    dt = T[1] - T[0]
    k = int(round(tau / dt))
    xs = np.roll(x, k)
    if k > 0:
        xs[:k] = np.nan
    elif k < 0:
        xs[k:] = np.nan

    ax_t.plot(T, x, color=AZUL, lw=1.6, label=r"$x(t)$")
    ax_t.plot(T, xs, color=AMBAR, lw=1.6, label=r"$x(t+\tau)$")
    prod = x * xs
    ax_t.fill_between(T, 0, prod, color=VERDE, alpha=0.25,
                      label="producto")
    ax_t.set_xlim(-7, 7)
    ax_t.set_ylim(-3, 3)
    ax_t.legend(loc="upper right", fontsize=8, ncol=3)
    ax_t.set_title(fr"$\tau$ = {tau:+.2f}      "
                   fr"$R_{{xx}}(\tau)\approx$ {np.nanmean(prod):+.2f}",
                   color=VERDE, fontsize=10)
    limpiar(ax_t)

    R = R_de(x)
    ax_r.plot(TAUS, R, color=VERDE, lw=2.2)
    ax_r.axvline(tau, color=INK, lw=1.0, ls="--")
    ax_r.plot([tau], [R[np.argmin(np.abs(TAUS - tau))]], "o", color=VERDE,
              ms=7)
    ax_r.axvline(0, color=INK, lw=0.7)
    ax_r.set_xlabel(r"$\tau$")
    ax_r.set_xlim(-TAU_MAX, TAU_MAX)
    ax_r.set_title(r"$R_{xx}(\tau)$: par, y con el máximo en $\tau=0$",
                   color=INK, fontsize=10)
    limpiar(ax_r)
    fig.canvas.draw_idle()


s_a = estilo_slider(Slider(eje_slider(fig, 0.22, 0.13, 0.56),
                           r"$\alpha$ (rapidez)", 0.4, 3.0, valinit=1.0,
                           valfmt="%.2f"))
s_tau = estilo_slider(Slider(eje_slider(fig, 0.22, 0.06, 0.56), r"$\tau$",
                             -TAU_MAX, TAU_MAX, valinit=1.5, valfmt="%.2f"))
s_a.on_changed(lambda v: dibujar(s_a.val, s_tau.val))
s_tau.on_changed(lambda v: dibujar(s_a.val, s_tau.val))

pie(fig, "Más alfa = la señal se descorrelaciona antes = R_xx más angosta = "
         "espectro más ancho (capítulo 11).")
dibujar(s_a.val, s_tau.val)
plt.show()
