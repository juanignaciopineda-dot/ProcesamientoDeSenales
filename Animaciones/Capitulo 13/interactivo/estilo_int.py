"""Estilo compartido de los scripts interactivos del capitulo 13.

Misma paleta que las animaciones de Manim y que las figuras del apunte.
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams

FONDO = "#12141a"
PANEL = "#171a22"
INK = "#9aa3b8"
TXT = "#e6e9f0"
AZUL = "#4c8dff"
AMBAR = "#f0883e"
VERDE = "#3fb950"
MAGENTA = "#c86bd8"
ROJO = "#ff6b6b"

rcParams.update({
    "figure.facecolor": FONDO,
    "axes.facecolor": FONDO,
    "savefig.facecolor": FONDO,
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "text.color": TXT,
    "axes.labelcolor": INK,
    "axes.edgecolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.titlecolor": TXT,
    "axes.linewidth": 1.1,
    "lines.linewidth": 2.0,
    "legend.frameon": False,
    "legend.labelcolor": INK,
    "figure.autolayout": False,
})


def limpiar(ax, ejes=("left", "bottom")):
    for lado in ("top", "right", "left", "bottom"):
        ax.spines[lado].set_visible(lado in ejes)
    return ax


def estilo_slider(s):
    """Colorea un Slider para que combine con el fondo oscuro."""
    s.label.set_color(TXT)
    s.valtext.set_color(AMBAR)
    s.poly.set_color(AMBAR)
    try:
        s.track.set_color("#2a2f3a")
    except AttributeError:
        pass
    return s


def eje_slider(fig, izq, abajo, ancho, alto=0.028):
    ax = fig.add_axes([izq, abajo, ancho, alto])
    ax.set_facecolor(PANEL)
    for lado in ("top", "right", "left", "bottom"):
        ax.spines[lado].set_visible(False)
    return ax


def pie(fig, texto):
    fig.text(0.5, 0.015, texto, ha="center", color=INK, fontsize=9,
             style="italic")
