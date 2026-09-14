"""Interactivo - De blanco a coloreado.

Mové rho (la correlación entre muestras vecinas) y mirá simultáneamente
la realización, la autocovarianza y el espectro. Fuera de |rho| <= 1/2 el
espectro se hace negativo: deja de ser una autocovarianza válida.

    python i05_coloreado.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from estilo_int import *

N = 160
OMEGA = np.linspace(-np.pi, np.pi, 900)
MS = np.arange(-7, 8)
_rng = np.random.default_rng(5)
W_BASE = _rng.choice([-1.0, 1.0], size=N + 1)   # el mismo ruido siempre,
                                                # asi el cambio se debe a rho

fig = plt.figure(figsize=(12.0, 6.2))
fig.suptitle("De blanco a coloreado: el efecto de la memoria", color=TXT,
             fontsize=13, y=0.965)

ax_t = fig.add_axes([0.06, 0.30, 0.40, 0.56])
ax_c = fig.add_axes([0.53, 0.30, 0.19, 0.56])
ax_s = fig.add_axes([0.78, 0.30, 0.19, 0.56])


def dibujar(rho):
    valido = abs(rho) <= 0.5
    col = AMBAR if valido else ROJO

    # modelador de dos taps con a*b = rho*(a^2+b^2), normalizado
    if valido:
        a = np.sqrt((1 + np.sqrt(max(0.0, 1 - 4 * rho ** 2))) / 2)
        b = rho / a if a > 0 else 0.0
    else:                       # fuera de rango no hay filtro real: se ilustra igual
        a, b = 1.0, rho
    x = a * W_BASE[1:] + b * W_BASE[:-1]
    x = x / (np.std(x) if np.std(x) > 0 else 1.0)

    ax_t.clear()
    ax_t.plot(np.arange(N), x, color=col, lw=1.5)
    ax_t.axhline(0, color=INK, lw=0.9, alpha=0.6)
    ax_t.set_title("una realización", color=col, pad=10)
    ax_t.set_xlabel("n"); ax_t.set_ylim(-3.2, 3.2); ax_t.set_yticks([])
    ax_t.set_xlim(0, N - 1)
    limpiar(ax_t, ejes=("bottom",))

    ax_c.clear()
    c = np.where(MS == 0, 1.0, np.where(np.abs(MS) == 1, rho, 0.0))
    ax_c.stem(MS, c, linefmt=col, markerfmt="o", basefmt=" ")
    for ln in ax_c.get_lines():
        ln.set_color(col); ln.set_markersize(4)
    ax_c.axhline(0, color=INK, lw=1.0)
    ax_c.set_title(r"$C_{xx}[m]$", color=col, pad=10)
    ax_c.set_xlabel("m"); ax_c.set_ylim(-0.85, 1.25)
    ax_c.set_yticks([0, 1])
    limpiar(ax_c, ejes=("left",))

    ax_s.clear()
    D = 1 + 2 * rho * np.cos(OMEGA)
    neg = D < 0
    ax_s.plot(OMEGA, D, color=col, lw=2.4)
    ax_s.fill_between(OMEGA, 0, D, where=~neg, color=col, alpha=0.20)
    if neg.any():
        ax_s.fill_between(OMEGA, 0, D, where=neg, color=ROJO, alpha=0.75)
    ax_s.axhline(0, color=INK, lw=1.0, ls=(0, (4, 3)))
    ax_s.set_title(r"$D_{xx}(e^{j\Omega})$", color=col, pad=10)
    ax_s.set_xlabel(r"$\Omega$")
    ax_s.set_xticks([-np.pi, 0, np.pi]); ax_s.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
    ax_s.set_ylim(-1.2, 2.3); ax_s.set_yticks([])
    limpiar(ax_s, ejes=("bottom",))

    if valido:
        msg = ("espectro plano: proceso blanco" if abs(rho) < 1e-3 else
               ("más potencia en baja frecuencia: señal lenta" if rho > 0 else
                "más potencia en alta frecuencia: señal que alterna"))
        cartel.set_text(msg)
        cartel.set_color(INK)
        cartel.set_fontweight("normal")
    else:
        cartel.set_text(r"$|\rho|>\frac{1}{2}$ : el espectro se hace negativo — "
                        "no es una autocovarianza válida")
        cartel.set_color(ROJO)
        cartel.set_fontweight("bold")
    fig.canvas.draw_idle()


# el cartel vive en la figura, no en el eje: asi no se corre encima del slider
cartel = fig.text(0.5, 0.205, "", ha="center", fontsize=10, color=INK)

s_rho = estilo_slider(Slider(eje_slider(fig, 0.25, 0.11, 0.5),
                             r"$\rho$", -0.75, 0.75, valinit=0.4,
                             valfmt="%.3f"))
s_rho.on_changed(dibujar)

pie(fig, "La misma secuencia de ruido en todos los casos: lo único que cambia "
         "es cuánta memoria le mete el filtro.")
dibujar(s_rho.val)
plt.show()
