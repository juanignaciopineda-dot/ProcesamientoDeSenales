"""Estilo compartido para las animaciones del capitulo 11.

Misma paleta que las figuras del apunte de Procesamiento de Senales,
para que los videos y el .md se vean de la misma familia.
"""
from manim import *
import numpy as np

# ------------------------------------------------------------------ paleta
INK = "#9aa3b8"      # ejes, texto secundario
AZUL = "#4c8dff"
AMBAR = "#f0883e"
VERDE = "#3fb950"
MAGENTA = "#c86bd8"
ROJO = "#ff6b6b"
FONDO = "#12141a"

TXT = "#e6e9f0"      # texto principal

# El color de fondo tiene que quedar fijado al importar el modulo: si se
# setea dentro de construct() la escena ya se instancio y no lo toma.
config.background_color = FONDO


def configurar():
    """Se conserva por compatibilidad; el fondo ya se fija al importar."""
    config.background_color = FONDO


# ------------------------------------------------------------------ texto
def titulo(txt, color=TXT, scale=0.68):
    """Titulo de escena, arriba a la izquierda."""
    t = Text(txt, color=color, weight=BOLD).scale(scale)
    t.to_corner(UL, buff=0.45)
    return t


def subtitulo(txt, scale=0.55, color=INK):
    return Text(txt, color=color).scale(scale)


def conclusion(txt, color=TXT, scale=0.6):
    """Cartel de cierre, abajo, con un filete de color arriba."""
    t = Text(txt, color=color).scale(scale)
    t.to_edge(DOWN, buff=0.6)
    return t


def nota(txt, scale=0.45, color=INK):
    return Text(txt, color=color, slant=ITALIC).scale(scale)


# ------------------------------------------------------------------ ejes
def ejes(x_rango, y_rango, ancho=6.0, alto=3.2, x_label=None, y_label=None,
         x_nums=None, y_nums=None, tip=True):
    """Ejes con el estilo del apunte: finos, en tinta, con punta de flecha."""
    ax = Axes(
        x_range=x_rango,
        y_range=y_rango,
        x_length=ancho,
        y_length=alto,
        axis_config={
            "color": INK,
            "stroke_width": 2,
            "include_ticks": False,
            "tip_width": 0.16,
            "tip_height": 0.16,
            "include_tip": tip,
        },
    )
    etiquetas = VGroup()
    if x_label is not None:
        lx = MathTex(x_label, color=INK).scale(0.6)
        lx.next_to(ax.x_axis.get_end(), DR, buff=0.12)
        etiquetas.add(lx)
    if y_label is not None:
        ly = MathTex(y_label, color=INK).scale(0.6)
        ly.next_to(ax.y_axis.get_end(), UR, buff=0.08)
        etiquetas.add(ly)
    if x_nums:
        ax.x_axis.add_numbers(x_nums, font_size=22, color=INK)
    if y_nums:
        ax.y_axis.add_numbers(y_nums, font_size=22, color=INK)
    return ax, etiquetas


def marca_x(ax, x, etiqueta, color=INK, scale=0.55, buff=0.15):
    """Tick vertical con etiqueta debajo del eje x."""
    p = ax.c2p(x, 0)
    tick = Line(p + DOWN * 0.09, p + UP * 0.09, color=color, stroke_width=2)
    lab = MathTex(etiqueta, color=color).scale(scale).next_to(tick, DOWN, buff=buff)
    return VGroup(tick, lab)


def curva(ax, f, x_rango=None, color=AZUL, ancho=3.5, **kw):
    return ax.plot(f, x_range=x_rango, color=color, stroke_width=ancho, **kw)


def area(ax, f, x0, x1, color=AZUL, opacidad=0.28):
    return ax.get_area(ax.plot(f, color=color), x_range=(x0, x1),
                       color=color, opacity=opacidad, stroke_width=0)


def linea_datos(ax, xs, ys, color=AZUL, ancho=3.0, suave=False):
    """Dibuja datos arbitrarios (arrays) sobre unos ejes.

    Para senales ruidosas conviene suave=False: interpolar suavizado
    inventa oscilaciones que no estan en los datos.
    """
    pts = [ax.c2p(float(x), float(y)) for x, y in zip(xs, ys)]
    m = VMobject(color=color, stroke_width=ancho)
    if suave:
        m.set_points_smoothly(pts)
    else:
        m.set_points_as_corners(pts)
    return m


def stem(ax, xs, ys, color=AZUL, ancho=3.0, radio=0.045):
    """Grafico de tallos (para senales de tiempo discreto)."""
    g = VGroup()
    for x, y in zip(xs, ys):
        base, punta = ax.c2p(float(x), 0), ax.c2p(float(x), float(y))
        g.add(Line(base, punta, color=color, stroke_width=ancho))
        g.add(Dot(punta, color=color, radius=radio))
    return g


# ------------------------------------------------------------------ senales
def ruido_suave(t, semilla=0, n_arm=7, escala=1.0):
    """Realizacion suave: suma de senoides con fase aleatoria."""
    rng = np.random.default_rng(semilla)
    y = np.zeros_like(t, dtype=float)
    for _ in range(n_arm):
        f = rng.uniform(0.35, 2.6)
        y += rng.normal(0, 1) * np.sin(2 * np.pi * f * t / max(t[-1], 1e-9) * 2
                                       + rng.uniform(0, 2 * np.pi))
    s = np.std(y)
    return escala * y / (s if s > 0 else 1.0)


def bloque(txt, color=AZUL, ancho=1.9, alto=0.95, scale=0.5):
    """Cajita de diagrama de bloques con su rotulo."""
    caja = RoundedRectangle(width=ancho, height=alto, corner_radius=0.12,
                            color=color, stroke_width=2.5,
                            fill_color=color, fill_opacity=0.10)
    rot = MathTex(txt, color=color).scale(scale).move_to(caja)
    return VGroup(caja, rot)


def flecha(inicio, fin, color=INK, ancho=2.2):
    return Arrow(inicio, fin, color=color, stroke_width=ancho,
                 buff=0.12, max_tip_length_to_length_ratio=0.18)


# ------------------------------------------------------------------ veredictos
# Los glifos ✗ / ✓ no estan en todas las fuentes y salen apagados o
# directamente vacios, asi que se dibujan con primitivas.
def cruz(color=ROJO, tam=0.22, ancho=7):
    return Cross(stroke_color=color, stroke_width=ancho).scale(tam)


def tilde(color=VERDE, tam=1.0, ancho=7):
    m = VMobject(stroke_color=color, stroke_width=ancho)
    m.set_points_as_corners([
        np.array([-0.16, 0.02, 0]),
        np.array([-0.04, -0.13, 0]),
        np.array([0.19, 0.19, 0]),
    ])
    return m.scale(tam)


def veredicto(ok, txt, color=None):
    """Marca (cruz o tilde) con su leyenda al lado."""
    color = color or (VERDE if ok else ROJO)
    marca = tilde(color) if ok else cruz(color)
    lab = Text(txt, color=color).scale(0.5)
    return VGroup(marca, lab).arrange(RIGHT, buff=0.22)


# ------------------------------------------------------------------ nubes
def nube(ax, xs, ys, color=AZUL, radio=0.035, opacidad=0.75):
    """Diagrama de dispersion de pares (x, y) sobre unos ejes."""
    return VGroup(*[
        Dot(ax.c2p(float(x), float(y)), radius=radio, color=color,
            fill_opacity=opacidad)
        for x, y in zip(xs, ys)])


def muestras_gauss(n, rho, mu=(0.0, 0.0), sd=(1.0, 1.0), semilla=0):
    """n pares (x, y) gaussianos bivariados con correlacion rho."""
    rng = np.random.default_rng(semilla)
    z1, z2 = rng.normal(0, 1, n), rng.normal(0, 1, n)
    x = mu[0] + sd[0] * z1
    y = mu[1] + sd[1] * (rho * z1 + np.sqrt(max(0.0, 1 - rho ** 2)) * z2)
    return x, y


def gauss(x, mu=0.0, sd=1.0):
    return np.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * np.sqrt(2 * np.pi))


def medidor(alto_max=2.6, ancho=0.5, color=VERDE, marco=INK):
    """Marco de un medidor vertical. El relleno se hace con relleno_medidor."""
    return Rectangle(width=ancho, height=alto_max, color=marco, stroke_width=2)


def relleno_medidor(marco, frac, color=VERDE):
    """Rectangulo de relleno para `marco`, con fraccion `frac` en [0, 1]."""
    frac = float(np.clip(frac, 0.0, 1.0))
    r = Rectangle(width=marco.width, height=max(1e-3, marco.height * frac),
                  stroke_width=0, fill_color=color, fill_opacity=0.85)
    return r.align_to(marco, DOWN).align_to(marco, LEFT)
