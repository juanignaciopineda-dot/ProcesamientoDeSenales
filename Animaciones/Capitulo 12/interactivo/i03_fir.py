"""Interactivo - Wiener FIR: las ecuaciones normales, resueltas en vivo.

Predecir x[n+1] a partir de las L muestras pasadas. Elegí el tipo de
proceso y mové su correlacion: el script arma la matriz Toeplitz L x L,
la resuelve y te muestra los pesos h[j] y el error.

La sorpresa: con un proceso "bandeado" (memoria de un paso) el predictor
usa muestras que estan INCORRELADAS con lo que quiere predecir.

    python i03_fir.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
from estilo_int import *

MS = np.arange(-6, 7)

fig = plt.figure(figsize=(12.2, 6.2))
fig.suptitle("Wiener FIR: las ecuaciones normales resueltas en vivo",
             color=TXT, fontsize=13, y=0.965)

ax_c = fig.add_axes([0.24, 0.34, 0.32, 0.54])
ax_h = fig.add_axes([0.64, 0.34, 0.33, 0.54])
ax_radio = fig.add_axes([0.025, 0.44, 0.16, 0.24])
ax_radio.set_facecolor(PANEL)
for lado in ("top", "right", "left", "bottom"):
    ax_radio.spines[lado].set_visible(False)


def cov_de(tipo, rho, L):
    """Autocovarianza C_xx[k] para k = 0..L (normalizada, C[0]=1)."""
    k = np.arange(L + 1)
    if tipo == "exponencial":
        return rho ** k
    # bandeado: MA(1), solo C[0] y C[1] no nulos
    return np.where(k == 0, 1.0, np.where(k == 1, rho, 0.0))


def dibujar(*_):
    tipo = radio.value_selected
    L = int(round(s_L.val))
    rho = s_rho.val
    if tipo == "bandeado" and abs(rho) > 0.5:
        rho = np.sign(rho) * 0.5           # fuera de |rho|<=1/2 no es valido

    c_full = cov_de(tipo, rho, max(L, 8))
    # sistema: R h = r, con R Toeplitz de C[0..L-1] y r = C[1..L]
    R = np.array([[c_full[abs(i - j)] for j in range(L)] for i in range(L)])
    r = c_full[1:L + 1]
    h = np.linalg.solve(R, r)
    mmse = c_full[0] - h @ r
    var_pred = c_full[0]

    # ---- autocovarianza
    ax_c.clear()
    cvals = np.array([cov_de(tipo, rho, 6)[abs(m)] for m in MS])
    ax_c.stem(MS, cvals, linefmt=AMBAR, markerfmt="o", basefmt=" ")
    for ln in ax_c.get_lines():
        ln.set_color(AMBAR); ln.set_markersize(4)
    ax_c.axhline(0, color=INK, lw=1.0)
    ax_c.set_title(r"$C_{xx}[m]$", color=AMBAR, pad=10)
    ax_c.set_xlabel("m"); ax_c.set_ylim(-0.7, 1.25); ax_c.set_yticks([0, 1])
    limpiar(ax_c, ejes=("left",))

    # ---- pesos del filtro
    ax_h.clear()
    js = np.arange(L)
    ax_h.bar(js, h, color=AZUL, width=0.55)
    ax_h.axhline(0, color=INK, lw=1.0)
    ax_h.set_title(r"pesos $h[j]$ del predictor", color=AZUL, pad=10)
    ax_h.set_xlabel("j"); ax_h.set_xticks(js)
    lim = max(1.05, np.abs(h).max() * 1.25)
    ax_h.set_ylim(-lim * 0.5, lim); ax_h.set_yticks([0])
    limpiar(ax_h, ejes=("bottom", "left"))

    if tipo == "exponencial":
        msg = ("solo pesa la ultima muestra: h[0] = rho, el resto ~ 0.  "
               "saber x[n] ya lo dice todo")
    else:
        usa = np.sum(np.abs(h) > 1e-3)
        msg = (f"usa {usa} muestras, aunque x[n-1], x[n-2]... estan "
               "INCORRELADAS con x[n+1].  no correlacionado != inutil")
    cartel.set_text(msg)
    info.set_text(f"MMSE = {mmse:.3f}      Var(x[n+1]) = {var_pred:.3f}      "
                  f"reduccion = {100*(1-mmse/var_pred):.0f} %")
    fig.canvas.draw_idle()


cartel = fig.text(0.5, 0.215, "", ha="center", fontsize=9.5, color=INK)
info = fig.text(0.5, 0.175, "", ha="center", fontsize=10, color=VERDE)

radio = RadioButtons(ax_radio, ["exponencial", "bandeado"], active=0,
                     activecolor=AMBAR)
for t in radio.labels:
    t.set_color(TXT); t.set_fontsize(9.5)
radio.on_clicked(dibujar)

s_rho = estilo_slider(Slider(eje_slider(fig, 0.24, 0.10, 0.32),
                             r"correlacion $\rho$", 0.0, 0.9, valinit=0.6,
                             valfmt="%.2f"))
s_L = estilo_slider(Slider(eje_slider(fig, 0.64, 0.10, 0.30),
                           "taps L", 1, 8, valinit=5, valstep=1,
                           valfmt="%d"))
s_rho.on_changed(dibujar)
s_L.on_changed(dibujar)

pie(fig, "Exponencial: C[m] = rho^|m| (un AR de primer orden).  Bandeado: "
         "C[0]=1, C[1]=rho, resto 0 (un MA de primer orden, valido si "
         "|rho| <= 1/2).")
dibujar()
plt.show()
