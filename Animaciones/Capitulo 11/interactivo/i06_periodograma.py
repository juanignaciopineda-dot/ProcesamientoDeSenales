"""Interactivo - Promediado de periodogramas.

Mové M (cantidad de ventanas) y T (largo de cada una) y mirá cómo cambia
el estimado frente a la PSD verdadera. El botón vuelve a sortear el ruido,
para ver que la dispersión es real y no un capricho de una corrida.

    python i06_periodograma.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from estilo_int import *

# proceso: blanco pasado por un modelador de un polo -> PSD conocida
A = 0.55
_semilla = [7]


def psd_real(w):
    return 1.0 / (1 - 2 * A * np.cos(w) + A ** 2)


def estimar(M, T, semilla):
    rng = np.random.default_rng(semilla)
    acum = np.zeros(T // 2)
    vent = np.hanning(T)
    corr = np.mean(vent ** 2)          # compensa la perdida de potencia
    for _ in range(M):
        w = rng.normal(0, 1, T + 60)
        x = np.zeros(T + 60)
        for n in range(1, T + 60):     # y[n] = A y[n-1] + w[n]
            x[n] = A * x[n - 1] + w[n]
        seg = x[60:]
        X = np.fft.fft(seg * vent)
        acum += (np.abs(X) ** 2 / (T * corr))[: T // 2]
    return acum / M


fig = plt.figure(figsize=(11.8, 6.0))
fig.suptitle("Estimación espectral: promediar periodogramas", color=TXT,
             fontsize=13, y=0.965)
ax = fig.add_axes([0.09, 0.30, 0.86, 0.56])


def dibujar(*_):
    M, T = int(s_M.val), int(2 ** round(s_T.val))
    est = estimar(M, T, _semilla[0])
    w = np.arange(T // 2) / (T // 2) * np.pi

    ax.clear()
    ax.plot(w, est, color=AMBAR, lw=1.6, label=f"estimado (M={M}, T={T})")
    ww = np.linspace(0, np.pi, 600)
    ax.plot(ww, psd_real(ww), color=VERDE, lw=2.6, ls=(0, (5, 3)),
            label="PSD verdadera")
    ax.set_xlim(0, np.pi); ax.set_ylim(0, psd_real(0) * 1.9)
    ax.set_xticks([0, np.pi / 2, np.pi])
    ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$"])
    ax.set_xlabel(r"$\Omega$"); ax.set_ylabel("PSD")
    ax.legend(loc="upper right", fontsize=9.5)
    limpiar(ax)

    err = np.sqrt(np.mean((est - psd_real(w)) ** 2))
    ax.text(0.015, 0.94, f"error cuadrático medio = {err:.3f}",
            transform=ax.transAxes, color=INK, fontsize=9.5)
    ax.text(0.015, 0.87, f"resolución ≈ π/T = {np.pi/T:.4f} rad",
            transform=ax.transAxes, color=AZUL, fontsize=9.5)
    fig.canvas.draw_idle()


s_M = estilo_slider(Slider(eje_slider(fig, 0.18, 0.155, 0.56),
                           "M (ventanas)", 1, 200, valinit=1, valstep=1,
                           valfmt="%d"))
s_T = estilo_slider(Slider(eje_slider(fig, 0.18, 0.085, 0.56),
                           "T (largo, potencia de 2)", 5, 10, valinit=7,
                           valstep=1, valfmt="%d"))
s_M.on_changed(dibujar)
s_T.on_changed(dibujar)

ax_btn = fig.add_axes([0.80, 0.085, 0.15, 0.065])
btn = Button(ax_btn, "otro sorteo", color=PANEL, hovercolor="#2a2f3a")
btn.label.set_color(TXT)


def resortear(_):
    _semilla[0] += 1
    dibujar()


btn.on_clicked(resortear)

pie(fig, "Más M baja la varianza (curva más suave). Más T mejora la resolución. "
         "Con un registro fijo, subir uno obliga a bajar el otro.")
dibujar()
plt.show()
