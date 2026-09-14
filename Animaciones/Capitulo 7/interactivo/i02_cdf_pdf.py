"""Interactivo - CDF y PDF/PMF, los tres tipos de variable.

Elegí el tipo de variable y mové la banda [a, b]: el salto en la CDF y el
área bajo la PDF son la misma probabilidad.

    python i02_cdf_pdf.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from estilo_int import *

X = np.linspace(-4, 4, 3000)
TIPOS = ["continua", "discreta", "mixta"]
SALTOS = [(-1.6, 0.25), (0.0, 0.40), (1.7, 0.35)]
X_MIX, MASA_MIX = 0.8, 0.32


def _phi(x):
    return np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)


# CDF normal por integracion acumulada, sin depender de scipy
_pdf_grid = _phi(X)
_cdf_grid = np.cumsum(_pdf_grid)
_cdf_grid = _cdf_grid / _cdf_grid[-1]


def cdf_cont(xq):
    return np.interp(xq, X, _cdf_grid)


def cdf_disc(xq):
    return np.array([sum(m for p, m in SALTOS if v >= p)
                     for v in np.atleast_1d(xq)])


def cdf_mix(xq):
    v = np.atleast_1d(xq)
    return (1 - MASA_MIX) * cdf_cont(v) + MASA_MIX * (v >= X_MIX)


fig = plt.figure(figsize=(12.2, 6.0))
fig.suptitle("La CDF y su derivada: una definición, tres formas", color=TXT,
             fontsize=13, y=0.965)

ax_F = fig.add_axes([0.24, 0.34, 0.34, 0.52])
ax_f = fig.add_axes([0.64, 0.34, 0.33, 0.52])
ax_radio = fig.add_axes([0.03, 0.46, 0.14, 0.24])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)
lectura = fig.text(0.61, 0.215, "", ha="center", fontsize=11, color=AMBAR)


def dibujar(*_):
    tipo = radio.value_selected
    a, b = s_a.val, s_b.val
    if b < a:
        a, b = b, a

    ax_F.clear(); ax_f.clear()

    if tipo == "continua":
        F = cdf_cont(X)
        ax_F.plot(X, F, color=AZUL, lw=2.4)
        f = _phi(X)
        ax_f.plot(X, f, color=VERDE, lw=2.4)
        ax_f.fill_between(X, 0, f, color=VERDE, alpha=0.15)
        m = (X >= a) & (X <= b)
        ax_f.fill_between(X[m], 0, f[m], color=AMBAR, alpha=0.8)
        prob = cdf_cont(b) - cdf_cont(a)
        ax_f.set_title(r"PDF  $f_X(x)$", color=VERDE, pad=10)
        ax_f.set_ylim(-0.03, 0.48)

    elif tipo == "discreta":
        xs = np.sort(np.concatenate([[-4], [p for p, _ in SALTOS], [4]]))
        ax_F.step(X, cdf_disc(X), where="post", color=MAGENTA, lw=2.4)
        ps = [p for p, _ in SALTOS]; ms = [m for _, m in SALTOS]
        ax_f.stem(ps, ms, linefmt=MAGENTA, markerfmt="o", basefmt=" ")
        for ln in ax_f.get_lines():
            ln.set_color(MAGENTA); ln.set_markersize(6)
        dentro = [(p, m) for p, m in SALTOS if a <= p <= b]
        if dentro:
            ax_f.stem([p for p, _ in dentro], [m for _, m in dentro],
                      linefmt=AMBAR, markerfmt="o", basefmt=" ")
            for ln in ax_f.get_lines()[-2:]:
                ln.set_color(AMBAR); ln.set_markersize(8)
        prob = sum(m for p, m in SALTOS if a < p <= b)
        ax_f.set_title(r"PMF  $p_X(x_j)$", color=MAGENTA, pad=10)
        ax_f.set_ylim(-0.03, 0.55)

    else:                                     # mixta
        Fm = cdf_mix(X)
        izq = X < X_MIX
        ax_F.plot(X[izq], Fm[izq], color=AMBAR, lw=2.4)
        ax_F.plot(X[~izq], Fm[~izq], color=AMBAR, lw=2.4)
        ax_F.plot([X_MIX, X_MIX],
                  [(1 - MASA_MIX) * cdf_cont(X_MIX), cdf_mix(X_MIX)[0]],
                  color=ROJO, lw=3)
        f = (1 - MASA_MIX) * _phi(X)
        ax_f.plot(X, f, color=AMBAR, lw=2.4)
        ax_f.fill_between(X, 0, f, color=AMBAR, alpha=0.15)
        m = (X >= a) & (X <= b)
        ax_f.fill_between(X[m], 0, f[m], color=AMBAR, alpha=0.75)
        ax_f.annotate("", xy=(X_MIX, 0.36), xytext=(X_MIX, 0),
                      arrowprops=dict(arrowstyle="->", color=ROJO, lw=3))
        ax_f.text(X_MIX + 0.12, 0.37, r"$k\,\delta(x-x_0)$", color=ROJO,
                  fontsize=9.5)
        prob = float(cdf_mix(b)[0] - cdf_mix(a)[0])
        ax_f.set_title(r"PDF  $f_X(x)$  (con impulso)", color=AMBAR, pad=10)
        ax_f.set_ylim(-0.03, 0.48)

    # ---- la banda, marcada en las dos vistas
    for ax in (ax_F, ax_f):
        ax.axvline(a, color=AMBAR, ls=(0, (3, 3)), lw=1.3)
        ax.axvline(b, color=AMBAR, ls=(0, (3, 3)), lw=1.3)
        ax.set_xlim(-4, 4)
        ax.set_xlabel("x")
        limpiar(ax)

    Fa = float(np.atleast_1d(
        cdf_cont(a) if tipo == "continua"
        else (cdf_disc(a) if tipo == "discreta" else cdf_mix(a)))[0])
    Fb = float(np.atleast_1d(
        cdf_cont(b) if tipo == "continua"
        else (cdf_disc(b) if tipo == "discreta" else cdf_mix(b)))[0])
    ax_F.plot([a, b], [Fa, Fa], color=AMBAR, ls=(0, (2, 2)), lw=1.2)
    ax_F.plot([b, b], [Fa, Fb], color=AMBAR, lw=4)
    ax_F.axhline(1, color=INK, ls=(0, (4, 3)), lw=1.2)
    ax_F.set_ylim(-0.05, 1.15)
    ax_F.set_yticks([0, 1])
    ax_F.set_title(r"CDF  $F_X(x)$", color=AZUL, pad=10)

    lectura.set_text(f"P(a < X ≤ b)  =  F(b) − F(a)  =  {prob:.4f}")
    fig.canvas.draw_idle()


radio = RadioButtons(ax_radio, TIPOS, active=0, activecolor=AMBAR)
for t in radio.labels:
    t.set_color(TXT); t.set_fontsize(10)
radio.on_clicked(dibujar)

s_a = estilo_slider(Slider(eje_slider(fig, 0.28, 0.115, 0.45), "a",
                           -4.0, 4.0, valinit=-0.7, valfmt="%.2f"))
s_b = estilo_slider(Slider(eje_slider(fig, 0.28, 0.055, 0.45), "b",
                           -4.0, 4.0, valinit=1.3, valfmt="%.2f"))
s_a.on_changed(dibujar); s_b.on_changed(dibujar)

dibujar()
plt.show()
