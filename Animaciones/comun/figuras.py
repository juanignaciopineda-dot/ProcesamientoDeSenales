"""Piezas técnicas de Procesamiento de Señales: gráficas, bloques, espectros.

Convenciones (las mismas que `iconos.py`):
- Las partes que las escenas animan por separado quedan como atributos.
- Los métodos que animan reciben la escena o devuelven animaciones; nunca
  llaman `play` por su cuenta sin recibir la escena.
- Las piezas nuevas van al final, en una sección por episodio
  («capítulo NN, episodio N: tema»), y se anotan en el catálogo del README §7.
"""
from __future__ import annotations

from manim import *
import numpy as np

from comun.estilo import *


# ============================================================ base: curvas sobre ejes

def gaussiana(x, mu: float = 0.0, sigma: float = 1.0):
    """Densidad normal N(mu, sigma²) evaluada en x (escalar o arreglo)."""
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


class Curva(VGroup):
    """Ejes con una función dibujada y, si hace falta, un área sombreada.

        c = Curva(lambda x: gaussiana(x, 0, 1), x_rango=(-4, 4), y_max=0.5,
                  x_label="x", y_label="f_X(x)")
        self.play(Create(c.ejes), run_time=0.5)
        self.play(Create(c.grafica), run_time=1.0)
        self.play(FadeIn(c.area(1, 4, ERROR)), run_time=0.5)

    Atributos: `.ejes` (Axes), `.etiquetas` (MathTex de los ejes),
    `.grafica` (la curva). `ejes.c2p(x, y)` da el punto en pantalla.
    """

    def __init__(self, f, x_rango=(-4, 4), y_max: float = 1.0, ancho: float = 8.0,
                 alto: float = 3.6, color=SENAL, x_label=None, y_label=None, **kw):
        super().__init__()
        self.f = f
        self.ejes, self.etiquetas = ejes([x_rango[0], x_rango[1], 1], [0, y_max, y_max / 4],
                                         ancho=ancho, alto=alto,
                                         x_label=x_label, y_label=y_label, **kw)
        self.grafica = self.ejes.plot(f, x_range=[x_rango[0], x_rango[1], 0.02],
                                      color=color, stroke_width=4)
        self.add(self.ejes, self.etiquetas, self.grafica)

    def area(self, desde: float, hasta: float, color=AMBAR, opacidad: float = 0.45) -> VMobject:
        """Área bajo la curva entre `desde` y `hasta` (no se agrega sola al grupo)."""
        return self.ejes.get_area(self.grafica, x_range=[desde, hasta],
                                  color=color, opacity=opacidad)

    def punto(self, x: float, color=AMBAR, radio: float = 0.08) -> Dot:
        """Punto sobre la curva en la abscisa x."""
        return Dot(self.ejes.c2p(x, self.f(x)), radius=radio, color=color)


# ============================================================ capítulo 07
# (las piezas de cada episodio van aquí abajo, en su propia sección)


# ============================================================ capítulo 10, episodio 1: procesos y realizaciones

def serie(semilla: int, n: int = 240, a: float = 0.9) -> np.ndarray:
    """Serie aleatoria de varianza 1 con memoria `a` (a = 0: ruido blanco). Semilla fija."""
    rng = np.random.default_rng(semilla)
    w = rng.normal(0, 1, n)
    y = np.zeros(n)
    y[0] = w[0]
    for k in range(1, n):
        y[k] = a * y[k - 1] + np.sqrt(1 - a * a) * w[k]
    return y


def traza(x, y, color=SENAL, ancho: float = 3.0, opacidad: float = 1.0) -> VMobject:
    """Curva poligonal en coordenadas de pantalla (más rápida que `Axes.plot`)."""
    m = VMobject(stroke_color=color, stroke_width=ancho, stroke_opacity=opacidad)
    m.set_fill(opacity=0)
    m.set_points_as_corners(np.column_stack([x, y, np.zeros(len(x))]))
    return m


class Lienzo:
    """Mapa (t, v) → pantalla para dibujar señales sin ejes de Manim.

        L = Lienzo(ancho=8, alto=2.5, t_rango=(0, 2), v_max=1.5, centro=(0, 0))
        c = L.curva(t, v, color=AZUL)      # la curva
        b = L.base()                       # la línea del tiempo (v = 0)
    """

    def __init__(self, ancho=8.0, alto=2.5, t_rango=(0.0, 1.0), v_max=1.5, centro=(0.0, 0.0)):
        self.ancho, self.alto = ancho, alto
        self.t0, self.t1 = t_rango
        self.v_max = v_max
        self.cx, self.cy = centro

    def x(self, t):
        return self.cx - self.ancho / 2 + (np.asarray(t, dtype=float) - self.t0) / (self.t1 - self.t0) * self.ancho

    def y(self, v):
        return self.cy + np.asarray(v, dtype=float) / self.v_max * self.alto / 2

    def p(self, t, v=0.0) -> np.ndarray:
        return np.array([float(self.x(t)), float(self.y(v)), 0.0])

    def curva(self, t, v, color=SENAL, ancho=3.0, opacidad=1.0) -> VMobject:
        return traza(self.x(t), self.y(v), color, ancho, opacidad)

    def base(self, color=INK, ancho=1.6, opacidad=1.0) -> Line:
        return Line(self.p(self.t0), self.p(self.t1), color=color, stroke_width=ancho,
                    stroke_opacity=opacidad)

    def vertical(self, t, color=AMBAR, ancho=3.0, mitad=None) -> Line:
        h = self.alto / 2 if mitad is None else mitad
        return Line([float(self.x(t)), self.cy + h, 0], [float(self.x(t)), self.cy - h, 0],
                    color=color, stroke_width=ancho)


def pila_de_curvas(lienzo: Lienzo, n: int, semilla: int = 1, a: float = 0.93, puntos: int = 200,
                   color=SENAL, opacidad: float = 0.45, ancho: float = 2.0, escala: float = 0.5) -> VGroup:
    """`n` realizaciones de un mismo proceso (memoria `a`) sobre el mismo lienzo."""
    t = np.linspace(lienzo.t0, lienzo.t1, puntos)
    return VGroup(*[lienzo.curva(t, escala * serie(semilla * 1000 + i, puntos, a), color, ancho, opacidad)
                    for i in range(n)])


def generador(amp: float = 1.0, frec: float = 1.5, fase: float = 0.0, ancho: float = 1.6,
              alto: float = 1.1, color=INK) -> VGroup:
    """Caja de un oscilador con su seno en miniatura. `.caja`, `.seno`."""
    caja_ = RoundedRectangle(corner_radius=0.12, width=ancho, height=alto, color=color,
                             stroke_width=2.5).set_fill(color, 0.12)
    t = np.linspace(0, 1, 90)
    v = amp * np.sin(2 * np.pi * frec * t + fase)
    seno = traza(-ancho * 0.4 + t * ancho * 0.8, v * alto * 0.3, SENAL, 3.0)
    g = VGroup(caja_, seno)
    g.caja, g.seno = caja_, seno
    return g


def dado_n(n: int, color=TXT) -> VGroup:
    """Cara de dado con `n` puntos (1–6). `.cara`, `.puntos`."""
    cara = RoundedRectangle(width=1.0, height=1.0, corner_radius=0.18, color=color,
                            stroke_width=4).set_fill(FONDO, 1)
    d = 0.27
    pos = {1: [(0, 0)], 2: [(-d, d), (d, -d)], 3: [(-d, d), (0, 0), (d, -d)],
           4: [(-d, d), (d, d), (-d, -d), (d, -d)],
           5: [(-d, d), (d, d), (0, 0), (-d, -d), (d, -d)],
           6: [(-d, d), (d, d), (-d, 0), (d, 0), (-d, -d), (d, -d)]}[n]
    puntos = VGroup(*[Circle(radius=0.09, color=color).set_fill(color, 1).set_stroke(width=0).move_to([x, y, 0])
                      for x, y in pos])
    g = VGroup(cara, puntos)
    g.cara, g.puntos = cara, puntos
    return g


def caja_tex(tex: str, color=AZUL, ancho: float = 1.5, alto: float = 0.9, escala: float = 0.9) -> VGroup:
    """Caja con una fórmula dentro. `.caja`, `.tex`."""
    r = RoundedRectangle(corner_radius=0.12, width=ancho, height=alto, color=color,
                         fill_color=color, fill_opacity=0.12, stroke_width=2.5)
    f = MathTex(tex, color=TXT).scale(escala).move_to(r)
    g = VGroup(r, f)
    g.caja, g.tex = r, f
    return g


def tira_pm1(valores, lado: float = 0.62, color=SENAL, escala_txt: float = 0.42) -> VGroup:
    """Fila de casillas +1 / −1 (la moneda). `.celdas` (cada una: cuadrado + texto)."""
    celdas = []
    for v in valores:
        r = Square(side_length=lado, color=color, stroke_width=2.5).set_fill(color, 0.32 if v > 0 else 0.08)
        t = Text("+1" if v > 0 else "−1", color=TXT).scale(escala_txt).move_to(r)
        celdas.append(VGroup(r, t))
    g = VGroup(*celdas).arrange(RIGHT, buff=0.06)
    g.celdas = celdas
    return g


class CuatroCosenos(VGroup):
    """Los cuatro osciladores desfasados (0°, 90°, 180°, 270°), apilados y con la misma escala de tiempo.

    Es el ejemplo que vuelve en todo el capítulo 10: en t = 0 valen 1, 0, −1, 0 y un cuarto
    de período después 0, −1, 0, 1. El tiempo va en períodos (t = 1 es un período).

    Atributos: `.curvas`, `.bases`, `.rotulos` («0°»…), `.fases`. Métodos: `x(t)`, `y(i, v)`,
    `punto(i, t)`, `corte(t)` (línea vertical que atraviesa los cuatro), `valor(i, t)`.
    """
    FASES = (0, 90, 180, 270)

    def __init__(self, ancho=9.0, paso=1.65, amp=0.62, t_rango=(-0.25, 1.75), centro=(1.1, 0.0), color=SENAL):
        super().__init__()
        self.ancho, self.paso, self.amp = ancho, paso, amp
        self.t0, self.t1 = t_rango
        self.cx, self.cy = centro
        t = np.linspace(self.t0, self.t1, 170)
        self.curvas, self.bases, self.rotulos = [], [], VGroup()
        for i, f in enumerate(self.FASES):
            base = Line([self.x(self.t0), self.yc(i), 0], [self.x(self.t1), self.yc(i), 0],
                        color=INK, stroke_width=1.5)
            curva = traza(self.x(t), self.y(i, np.cos(2 * np.pi * t + np.deg2rad(f))), color, 3.2)
            rot = Text(f"{f}°", color=INK).scale(0.5).move_to([self.x(self.t0) - 0.55, self.yc(i), 0])
            self.bases.append(base)
            self.curvas.append(curva)
            self.rotulos.add(rot)
        self.add(*self.bases, *self.curvas, self.rotulos)

    def x(self, t):
        return self.cx - self.ancho / 2 + (np.asarray(t, dtype=float) - self.t0) / (self.t1 - self.t0) * self.ancho

    def yc(self, i: int) -> float:
        return self.cy + (1.5 - i) * self.paso

    def y(self, i: int, v):
        return self.yc(i) + np.asarray(v, dtype=float) * self.amp

    def valor(self, i: int, t: float) -> float:
        return float(np.cos(2 * np.pi * t + np.deg2rad(self.FASES[i])))

    def punto(self, i: int, t: float) -> np.ndarray:
        return np.array([float(self.x(t)), float(self.y(i, self.valor(i, t))), 0.0])

    def corte(self, t: float, color=AMBAR, ancho: float = 3.5) -> Line:
        arriba = self.yc(0) + self.paso * 0.55
        abajo = self.yc(3) - self.paso * 0.55
        return Line([float(self.x(t)), arriba, 0], [float(self.x(t)), abajo, 0],
                    color=color, stroke_width=ancho)


# ============================================================ capítulo 10, episodio 2: media, autocorrelación, autocovarianza

class CuatroEnFase(CuatroCosenos):
    """Los cuatro osciladores que arrancan a la vez (fase 0) con amplitudes 1, 1, 3 y 3.

    Es la variante del ejemplo de los cuatro osciladores: la media da 2 cos(2πt).
    Mismos atributos y métodos que `CuatroCosenos` (`.curvas`, `.bases`, `.rotulos` con «A = 1»…).
    """
    AMPS = (1, 1, 3, 3)

    def __init__(self, ancho=6.0, paso=1.5, amp=0.24, t_rango=(-0.25, 1.75), centro=(3.5, -0.1), color=SENAL):
        VGroup.__init__(self)
        self.ancho, self.paso, self.amp = ancho, paso, amp
        self.t0, self.t1 = t_rango
        self.cx, self.cy = centro
        t = np.linspace(self.t0, self.t1, 170)
        self.curvas, self.bases, self.rotulos = [], [], VGroup()
        for i, a in enumerate(self.AMPS):
            base = Line([self.x(self.t0), self.yc(i), 0], [self.x(self.t1), self.yc(i), 0],
                        color=INK, stroke_width=1.5)
            curva = traza(self.x(t), self.y(i, a * np.cos(2 * np.pi * t)), color, 3.2)
            rot = Text(f"A = {a}", color=INK).scale(0.42).move_to([self.x(self.t0) - 0.55, self.yc(i), 0])
            self.bases.append(base)
            self.curvas.append(curva)
            self.rotulos.add(rot)
        self.add(*self.bases, *self.curvas, self.rotulos)

    def valor(self, i: int, t: float) -> float:
        return float(self.AMPS[i] * np.cos(2 * np.pi * t))


class TablaCortes:
    """Tabla de cortes del ensemble: una fila por realización, una columna por instante o cálculo
    y un renglón final de promedio. Las piezas se crean sueltas (no van en un grupo) para animarlas una a una.

        T = TablaCortes(["0°", "90°", "180°", "270°"])
        self.play(FadeIn(T.armazon()))            # líneas, etiquetas de fila y «promedio»
        self.play(FadeIn(T.enc(0, "t = 0")))      # encabezado de la columna 0
        self.play(FadeIn(T.celda(0, 1, "0")))     # celda (columna 0, fila 1)
        self.pop(T.prom(0, "0"))                  # promedio de la columna 0
    """

    def __init__(self, filas, x0=-6.8, y0=2.4, ancho_col=1.55, alto_fila=0.6, ancho_rot=1.15, n_col=3,
                 titulo_prom="promedio"):
        self.filas, self.x0, self.y0 = list(filas), x0, y0
        self.ancho_col, self.alto, self.ancho_rot, self.n_col = ancho_col, alto_fila, ancho_rot, n_col
        self.titulo_prom = titulo_prom

    def xc(self, j: int) -> float:
        return self.x0 + self.ancho_rot + (j + 0.5) * self.ancho_col

    def yf(self, i: int) -> float:
        return self.y0 - (i + 1) * self.alto

    @property
    def y_prom(self) -> float:
        return self.y0 - (len(self.filas) + 1.3) * self.alto

    def armazon(self) -> VGroup:
        n = len(self.filas)
        x1 = self.x0 + self.ancho_rot + self.n_col * self.ancho_col
        g = VGroup()
        g.add(Line([self.x0, self.y0 - self.alto / 2, 0], [x1, self.y0 - self.alto / 2, 0], color=INK, stroke_width=1.6))
        g.add(Line([self.x0, self.y_prom + self.alto * 0.65, 0], [x1, self.y_prom + self.alto * 0.65, 0],
                   color=INK, stroke_width=1.6))
        g.add(Line([self.x0 + self.ancho_rot, self.y0 - self.alto / 2, 0],
                   [self.x0 + self.ancho_rot, self.yf(n - 1) - self.alto / 2, 0], color=INK, stroke_width=1.6))
        for i, f in enumerate(self.filas):
            g.add(Text(f, color=INK).scale(0.55).move_to([self.x0 + self.ancho_rot / 2, self.yf(i), 0]))
        g.add(Text(self.titulo_prom, color=AMBAR).scale(0.5).move_to([self.x0 + self.ancho_rot / 2, self.y_prom, 0]))
        return g

    def enc(self, j: int, txt: str, color=TXT) -> Text:
        return Text(txt, color=color, weight=BOLD).scale(0.55).move_to([self.xc(j), self.y0, 0])

    def celda(self, j: int, i: int, txt: str, color=TXT) -> Text:
        return Text(txt, color=color).scale(0.68).move_to([self.xc(j), self.yf(i), 0])

    def prom(self, j: int, txt: str, color=AMBAR) -> Text:
        return Text(txt, color=color, weight=BOLD).scale(0.78).move_to([self.xc(j), self.y_prom, 0])

    def marco(self, j: int, color=AMBAR) -> Rectangle:
        arriba = self.y0 - self.alto * 0.55
        abajo = self.y_prom - self.alto * 0.55
        return Rectangle(width=self.ancho_col * 0.92, height=arriba - abajo, color=color, stroke_width=3).move_to(
            [self.xc(j), (arriba + abajo) / 2, 0])


class Rombo(VGroup):
    """Las cuatro parejas (X(0), X(¼ de período)) de los osciladores desfasados como puntos en el plano:
    (1, 0), (0, −1), (−1, 0), (0, 1). Forman un rombo, no una recta. `.ejes`, `.puntos`, `.p(x, y)`."""

    def __init__(self, centro=(0.0, 0.0), radio: float = 1.3, color=SENAL):
        super().__init__()
        self.c, self.r = np.array([centro[0], centro[1], 0.0]), radio
        h = Line(self.c + LEFT * radio * 1.25, self.c + RIGHT * radio * 1.25, color=INK, stroke_width=1.6)
        v = Line(self.c + DOWN * radio * 1.25, self.c + UP * radio * 1.25, color=INK, stroke_width=1.6)
        self.ejes = VGroup(h, v)
        self.puntos = [Dot(self.p(x, y), radius=0.11, color=color) for x, y in ((1, 0), (0, -1), (-1, 0), (0, 1))]
        self.add(self.ejes, *self.puntos)

    def p(self, x: float, y: float) -> np.ndarray:
        return self.c + np.array([x * self.r, y * self.r, 0.0])


class Palitos(VGroup):
    """Gráfica de palitos (una medida contra la separación entre instantes), para autocovarianzas.

        g = Palitos(range(0, 7), [1, .6, .36, ...], ancho=3.6, alto=2.2, v_max=1.0, centro=(-4.5, 0))
    Atributos: `.base` (línea), `.tallos`, `.puntos`, `.eje` (rótulo «separación»). `pos(k)` da la cima del palito k.
    """

    def __init__(self, ks, valores, ancho=3.6, alto=2.2, v_max=1.0, color=SENAL, centro=(0.0, 0.0),
                 rotulo="separación", punto=0.07):
        super().__init__()
        self.ks, self.valores = list(ks), list(valores)
        self.ancho, self.alto, self.v_max = ancho, alto, v_max
        self.cx, self.cy = centro
        self.k0 = self.ks[0]
        self.n = len(self.ks)
        self.base = Line([self.cx - ancho / 2, self.cy, 0], [self.cx + ancho / 2, self.cy, 0], color=INK, stroke_width=1.8)
        self.tallos, self.puntos = [], []
        for k, v in zip(self.ks, self.valores):
            top = self.pos(k, v)
            self.tallos.append(Line([top[0], self.cy, 0], top, color=color, stroke_width=4))
            self.puntos.append(Dot(top, radius=punto, color=color))
        self.eje = Text(rotulo, color=INK).scale(0.5).move_to([self.cx, self.cy - alto / 2 - 0.28, 0])
        self.add(self.base, *self.tallos, *self.puntos, self.eje)

    def pos(self, k, v=None) -> np.ndarray:
        if v is None:
            v = self.valores[self.ks.index(k)]
        x = self.cx - self.ancho / 2 + (k - self.k0 + 0.5) / self.n * self.ancho
        return np.array([x, self.cy + v / self.v_max * self.alto / 2, 0.0])


def termometro(alto: float = 1.7, color=ROJO, nivel: float = 0.6) -> VGroup:
    """Termómetro plano. `.tubo`, `.bulbo`, `.liquido`."""
    tubo = RoundedRectangle(corner_radius=0.1, width=0.22, height=alto, color=TXT, stroke_width=3).set_fill(FONDO, 1)
    bulbo = Circle(radius=0.22, color=TXT, stroke_width=3).set_fill(color, 1).next_to(tubo, DOWN, buff=-0.1)
    liquido = Rectangle(width=0.1, height=alto * nivel, color=color, stroke_width=0).set_fill(color, 1)
    liquido.align_to(tubo, DOWN).shift(UP * 0.06)
    liquido.set_x(tubo.get_x())
    g = VGroup(tubo, liquido, bulbo)
    g.tubo, g.liquido, g.bulbo = tubo, liquido, bulbo
    return g


def balancin() -> VGroup:
    """Regla en equilibrio sobre un punto de apoyo, con una pesa. `.regla`, `.apoyo`, `.pesa`."""
    apoyo = Triangle(color=INK, stroke_width=3).set_fill(INK, 0.5).scale(0.28)
    regla = Line(LEFT * 1.6, RIGHT * 1.6, color=TXT, stroke_width=5).next_to(apoyo, UP, buff=0)
    pesa = Square(side_length=0.36, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.45).next_to(regla, UP, buff=0)
    g = VGroup(apoyo, regla, pesa)
    g.regla, g.apoyo, g.pesa = regla, apoyo, pesa
    return g


# ============================================================ capítulo 10, episodio 3: estacionariedad

def coseno(L: Lienzo, fase_deg: float = 0.0, amp: float = 1.0, color=SENAL, ancho: float = 3.2,
           puntos: int = 170) -> VMobject:
    """Coseno de período 1 (el tiempo del lienzo va en períodos) con la fase dada en grados."""
    t = np.linspace(L.t0, L.t1, puntos)
    return L.curva(t, amp * np.cos(2 * np.pi * t + np.deg2rad(fase_deg)), color, ancho)


def campana_mini(centro=(0.0, 0.0), ancho: float = 1.2, alto: float = 0.8, color=SENAL, grosor: float = 3.0) -> VMobject:
    """Campana de Gauss pequeña sobre su base (para «la densidad de este instante»)."""
    x = np.linspace(-2.6, 2.6, 60)
    return traza(centro[0] + x / 2.6 * ancho / 2, centro[1] - alto / 2 + np.exp(-x ** 2 / 2) * alto, color, grosor)


def rectangulo_mini(centro=(0.0, 0.0), ancho: float = 1.2, alto: float = 0.8, color=AMBAR, grosor: float = 3.0) -> VMobject:
    """Densidad uniforme pequeña (un rectángulo abierto por abajo)."""
    x0, x1 = centro[0] - ancho / 2, centro[0] + ancho / 2
    y0, y1 = centro[1] - alto / 2, centro[1] + alto / 2
    return traza([x0, x0, x1, x1], [y0, y1, y1, y0], color, grosor)


# ============================================================ capítulo 10, episodio 4: la onda telegráfica

CAMBIOS = [0.7, 1.2, 2.6, 3.1, 3.9, 5.0]     # instantes de cambio de la onda que vuelve en todo el episodio


def onda_tel(L: Lienzo, tiempos=CAMBIOS, nivel0: int = 1, color=AMBAR, ancho: float = 4.0,
             t0=None, t1=None) -> VMobject:
    """Onda telegráfica ±1 con saltos en `tiempos` (empieza en `nivel0`), entre t0 y t1 del lienzo."""
    t0 = L.t0 if t0 is None else t0
    t1 = L.t1 if t1 is None else t1
    xs, ys, n = [t0], [nivel0], nivel0
    for t in tiempos:
        if t0 < t < t1:
            xs += [t, t]
            ys += [n, -n]
            n = -n
    xs.append(t1)
    ys.append(n)
    return L.curva(np.array(xs), np.array(ys), color, ancho)


def nivel_en(t: float, tiempos=CAMBIOS, nivel0: int = 1) -> int:
    """Valor (+1 o −1) de la onda en el instante t."""
    return nivel0 * (-1) ** sum(1 for x in tiempos if x <= t)


def marcas_cambio(L: Lienzo, tiempos=CAMBIOS, color=AMBAR, alto: float = 0.22) -> VGroup:
    """Rayitas sobre la línea del tiempo en cada instante de cambio."""
    return VGroup(*[Line(L.p(t, 0) + DOWN * alto, L.p(t, 0) + UP * alto, color=color, stroke_width=4)
                    for t in tiempos])


def interruptor(color=AMBAR) -> VGroup:
    """Interruptor de pared con su palanca. `.cuerpo`, `.palanca`, `.perilla`; `extremo(i, arriba)`."""
    cuerpo = RoundedRectangle(corner_radius=0.14, width=0.9, height=1.5, color=TXT,
                              stroke_width=3.5).set_fill(FONDO, 1)
    g = VGroup(cuerpo)
    g.cuerpo = cuerpo
    a = g.extremo(True)
    g.palanca = Line(ORIGIN, a, color=color, stroke_width=8)
    g.perilla = Dot(a, radius=0.13, color=color)
    g.add(g.palanca, g.perilla)
    return g


def _extremo(self, arriba: bool) -> np.ndarray:
    return self.cuerpo.get_center() + UP * (0.42 if arriba else -0.42)


VGroup.extremo = _extremo


def voltear(g: VGroup, arriba: bool):
    """Animaciones (palanca y perilla) que ponen el interruptor arriba o abajo."""
    a = g.extremo(arriba)
    return [g.palanca.animate.put_start_and_end_on(g.cuerpo.get_center(), a), g.perilla.animate.move_to(a)]


class BarrasK(VGroup):
    """Barras de una distribución sobre k = 0, 1, 2… (Poisson). `.base`, `.barras` (una por k), `.ks` (rótulos).
    `pos(k)` da la cima de la barra k; `crecer(k)` anima su aparición."""

    def __init__(self, valores, ancho=6.0, alto=3.0, v_max=0.7, centro=(0.0, 0.0), color=SENAL):
        super().__init__()
        self.valores, self.ancho, self.alto, self.v_max = list(valores), ancho, alto, v_max
        self.cx, self.cy = centro
        self.n = len(self.valores)
        paso = ancho / self.n
        self.base = Line([self.cx - ancho / 2, self.cy, 0], [self.cx + ancho / 2, self.cy, 0], color=INK, stroke_width=2)
        self.barras, self.ks = [], VGroup()
        for k, v in enumerate(self.valores):
            h = max(v / v_max * alto, 0.04)
            b = Rectangle(width=paso * 0.66, height=h, color=color, stroke_width=2).set_fill(color, 0.5)
            b.move_to([self.cx - ancho / 2 + (k + 0.5) * paso, self.cy + h / 2, 0])
            self.barras.append(b)
            self.ks.add(Text(str(k), color=INK).scale(0.5).move_to([b.get_x(), self.cy - 0.3, 0]))
        self.add(self.base, *self.barras, self.ks)

    def pos(self, k: int) -> np.ndarray:
        b = self.barras[k]
        return np.array([b.get_x(), b.get_top()[1], 0.0])

    def crecer(self, k: int):
        return GrowFromEdge(self.barras[k], DOWN)


# ============================================================ capítulo 10, episodio 6: predecir y filtrar

def sensor_datos(n: int = 44, n0: int = 30, objetivo: float = 3.0) -> np.ndarray:
    """Sensor centrado (x − 20): varianza 4, memoria 0,6 por paso, con x[n0] = objetivo (23 °C). Semilla fija."""
    mejor = None
    for s in range(300):
        y = 2.0 * serie(700 + s, n, 0.6)
        d = abs(y[n0] - objetivo)
        if mejor is None or d < mejor[0]:
            mejor = (d, y)
    y = mejor[1].copy()
    y[n0] = objetivo
    return y


class PanelSensor:
    """La grabación del sensor (centrada en su media, 20 °C) hasta el instante n0.

        P = PanelSensor(centro=(0, -0.3), ancho=9, alto=3.4)
        P.pasado (curva azul) · P.media (línea de 20) · P.rotulo_media (texto «20 °C»)
        P.p(k, v) → punto de pantalla; P.punto(k, v, color) → Dot
    Los valores `v` están centrados: v = 3 es 23 °C.
    """

    def __init__(self, centro=(0.0, 0.0), ancho: float = 9.0, alto: float = 3.4, n: int = 44, n0: int = 30,
                 v_max: float = 6.5):
        self.n, self.n0 = n, n0
        self.L = Lienzo(ancho=ancho, alto=alto, t_rango=(0, n - 1), v_max=v_max, centro=centro)
        self.y = sensor_datos(n, n0)
        t = np.arange(n)
        self.pasado = self.L.curva(t[:n0 + 1], self.y[:n0 + 1], SENAL, 3.5)
        self.media = DashedLine(self.L.p(0, 0), self.L.p(n - 1, 0), color=INK, stroke_width=2.2)
        self.rotulo_media = Text("20 °C", color=INK).scale(0.42).next_to(self.L.p(0, 0), LEFT, buff=0.15)

    def p(self, k, v=0.0) -> np.ndarray:
        return self.L.p(k, v)

    def punto(self, k, v, color=AMBAR, radio: float = 0.1) -> Dot:
        return Dot(self.L.p(k, v), radius=radio, color=color)


def proyeccion_pred(m: int, dato: float = 3.0, rho: float = 0.6) -> tuple[float, float]:
    """Predicción lineal a m pasos del sensor centrado: (x̂ − 20, error cuadrático medio)."""
    r = rho ** m
    return r * dato, 4.0 * (1 - r * r)


class Flechas(VGroup):
    """El dibujo del capítulo 8: la flecha del presente, la del futuro, la sombra de una sobre la otra y el
    error perpendicular. Con ángulo 53,13° y flechas iguales, la sombra mide 0,6 (ρ = 0,6).

    Atributos: `.presente` (azul), `.futuro` (tinta), `.sombra` (ámbar), `.error` (rojo), `.recto` (ángulo
    recto), `.o` (origen), `.fin_sombra`, `.fin_futuro`.
    """

    def __init__(self, origen=(0.0, 0.0), largo: float = 3.0, angulo: float = 53.13,
                 largo_objetivo: float | None = None, color_dato=SENAL, color_objetivo=INK):
        super().__init__()
        th = np.deg2rad(angulo)
        lo = largo if largo_objetivo is None else largo_objetivo
        self.o = np.array([origen[0], origen[1], 0.0])
        self.fin_presente = self.o + np.array([largo, 0.0, 0.0])
        self.fin_futuro = self.o + lo * np.array([np.cos(th), np.sin(th), 0.0])
        self.fin_sombra = self.o + np.array([lo * np.cos(th), 0.0, 0.0])
        self.presente = Arrow(self.o, self.fin_presente, buff=0, color=color_dato, stroke_width=6,
                              max_tip_length_to_length_ratio=0.12)
        self.futuro = Arrow(self.o, self.fin_futuro, buff=0, color=color_objetivo, stroke_width=6,
                            max_tip_length_to_length_ratio=0.12)
        self.sombra = Line(self.o, self.fin_sombra, color=ESTIMACION, stroke_width=11)
        self.error = Line(self.fin_sombra, self.fin_futuro, color=ERROR, stroke_width=5)
        s = 0.22
        self.recto = VMobject(stroke_color=ERROR, stroke_width=3).set_fill(opacity=0)
        self.recto.set_points_as_corners([self.fin_sombra + [-s, 0, 0], self.fin_sombra + [-s, s, 0],
                                          self.fin_sombra + [0, s, 0]])
        self.add(self.presente, self.futuro, self.sombra, self.error, self.recto)


def fraccion(num, den, color=TXT) -> VGroup:
    """Fracción armada a mano con dos piezas (para animar numerador y denominador por separado).
    `.num`, `.barra`, `.den`."""
    barra = Line(LEFT, RIGHT, color=color, stroke_width=2.5)
    ancho = max(num.width, den.width) + 0.2
    barra.put_start_and_end_on(LEFT * ancho / 2, RIGHT * ancho / 2)
    num.next_to(barra, UP, buff=0.1)
    den.next_to(barra, DOWN, buff=0.1)
    g = VGroup(num, barra, den)
    g.num, g.barra, g.den = num, barra, den
    return g


def pila_icono(color=AMBAR) -> VGroup:
    """Pila (batería) plana: cuerpo y polo. `.cuerpo`."""
    cuerpo = RoundedRectangle(corner_radius=0.08, width=1.0, height=0.55, color=color,
                              stroke_width=3.5).set_fill(color, 0.25)
    polo = Rectangle(width=0.12, height=0.25, color=color, stroke_width=0).set_fill(color, 1).next_to(cuerpo, RIGHT, buff=0)
    g = VGroup(cuerpo, polo)
    g.cuerpo = cuerpo
    return g


def banda(L: Lienzo, ks, centro, ancho_v, color=AMBAR, opacidad: float = 0.2) -> VMobject:
    """Banda sombreada alrededor de una curva: `centro` ± `ancho_v` en cada instante de `ks`."""
    ks = np.asarray(ks, dtype=float)
    arriba = np.column_stack([L.x(ks), L.y(np.asarray(centro) + np.asarray(ancho_v)), np.zeros(len(ks))])
    abajo = np.column_stack([L.x(ks), L.y(np.asarray(centro) - np.asarray(ancho_v)), np.zeros(len(ks))])
    m = VMobject(stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)
    m.set_points_as_corners(np.vstack([arriba, abajo[::-1]]))
    return m


# ============================================================ capítulo 10, episodio 7: un filtro sobre procesos

class BloqueLTI(VGroup):
    """Caja de un sistema con su flecha de entrada y su flecha de salida.

        b = BloqueLTI(r"h", centro=(0, 0), ancho=2.2, alto=1.3)
    Atributos: `.caja`, `.rot` (la fórmula de dentro), `.ent`, `.sal`. `p_ent()` y `p_sal()` dan
    el extremo libre de cada flecha (donde empieza la entrada y donde termina la salida).
    """

    def __init__(self, rotulo: str = r"h", centro=(0.0, 0.0), ancho: float = 2.2, alto: float = 1.3,
                 color=AZUL, largo: float = 1.5, escala: float = 0.9):
        super().__init__()
        cx, cy = centro
        self.caja = RoundedRectangle(corner_radius=0.12, width=ancho, height=alto, color=color,
                                     fill_color=color, fill_opacity=0.12, stroke_width=2.5).move_to([cx, cy, 0])
        self.rot = MathTex(rotulo, color=TXT).scale(escala).move_to(self.caja)
        kw = dict(color=INK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.25)
        self.ent = Arrow([cx - ancho / 2 - largo, cy, 0], [cx - ancho / 2, cy, 0], **kw)
        self.sal = Arrow([cx + ancho / 2, cy, 0], [cx + ancho / 2 + largo, cy, 0], **kw)
        self.add(self.ent, self.caja, self.rot, self.sal)

    def p_ent(self) -> np.ndarray:
        return self.ent.get_start()

    def p_sal(self) -> np.ndarray:
        return self.sal.get_end()


class Tallos(VGroup):
    """Secuencia de palitos (una muestra por palito), para h[k], la entrada y la salida.

        g = Tallos([2, 4, 6], centro=(0, 0), paso=0.9, unidad=0.35, color=SENAL, k0=0)
    Atributos: `.base`, `.tallos`, `.puntos`, `.ks` (rótulos de posición, si `indices=True`).
    `pos(i)` da la cima del palito `i` (0 = el primero); `x(i)` su posición horizontal.
    """

    def __init__(self, valores, centro=(0.0, 0.0), paso: float = 0.8, unidad: float = 1.0, color=SENAL,
                 k0: int = 0, indices: bool = False, extra: int = 0):
        super().__init__()
        self.valores = list(valores)
        self.cx, self.cy, self.paso, self.unidad, self.k0 = centro[0], centro[1], paso, unidad, k0
        n = len(self.valores)
        self.base = Line([self.x(-0.6 - extra), self.cy, 0], [self.x(n - 0.4 + extra), self.cy, 0],
                         color=INK, stroke_width=1.8)
        self.tallos, self.puntos = [], []
        self.ks = VGroup()
        for i, v in enumerate(self.valores):
            top = self.pos(i)
            self.tallos.append(Line([top[0], self.cy, 0], [top[0], self.cy + (v * unidad if v else 0.001), 0],
                                    color=color, stroke_width=5))
            self.puntos.append(Dot(top, radius=0.085, color=color))
            if indices:
                self.ks.add(Text(str(k0 + i), color=INK).scale(0.4).move_to([top[0], self.cy - 0.3, 0]))
        self.add(self.base, *self.tallos, *self.puntos, self.ks)

    def x(self, i: float) -> float:
        n = len(self.valores)
        return self.cx + (i - (n - 1) / 2) * self.paso

    def pos(self, i: int) -> np.ndarray:
        return np.array([self.x(i), self.cy + self.valores[i] * self.unidad, 0.0])

    def palito(self, i: int) -> VGroup:
        return VGroup(self.tallos[i], self.puntos[i])


# ============================================================ capítulo 10, episodio 5: pilas, promedios y muestra efectiva

def fila_puntos(n: int, ancho: float = 6.0, centro=(0.0, 0.0), color=SENAL, radio: float = 0.07) -> VGroup:
    """`n` puntos en fila horizontal (muestras sueltas)."""
    xs = np.linspace(centro[0] - ancho / 2, centro[0] + ancho / 2, n)
    return VGroup(*[Dot([x, centro[1], 0], radius=radio, color=color) for x in xs])


def hilos_entre(puntos: VGroup, color=INK, ancho: float = 2.5) -> VGroup:
    """Segmentos entre puntos consecutivos: «cada muestra recuerda a la anterior»."""
    return VGroup(*[Line(a.get_center(), b.get_center(), color=color, stroke_width=ancho)
                    for a, b in zip(puntos[:-1], puntos[1:])])


def ejes_k(n_lados: int, ancho: float = 7.0, alto: float = 2.4, v_max: float = 1.0, centro=(0.0, 0.0)):
    """Barras de una función de k = −n…n. Devuelve `(base, dx, y0, altura_por_unidad)` para armarlas a mano."""
    base = Line([centro[0] - ancho / 2, centro[1], 0], [centro[0] + ancho / 2, centro[1], 0], color=INK, stroke_width=2)
    dx = ancho / (2 * n_lados + 2)
    return base, dx, centro[1], alto / v_max


def barra_k(k: int, valor: float, dx: float, y0: float, esc: float, cx: float = 0.0, color=SENAL) -> Rectangle:
    """Una barra de la función en la posición `k`."""
    h = max(valor * esc, 0.03)
    b = Rectangle(width=dx * 0.7, height=h, color=color, stroke_width=2).set_fill(color, 0.55)
    b.move_to([cx + k * dx, y0 + h / 2, 0])
    return b


VOLTAJES_PILAS = (1, -2, 2, 0)    # los cuatro voltajes del cajón (media 0; varianza de la población real: 4)


def rectas_pilas(L: Lienzo, valores=VOLTAJES_PILAS, color=SENAL, ancho: float = 3.5) -> VGroup:
    """Una recta horizontal por pila (cada realización es una constante). Son `Line`: no disparan el control de encimado."""
    return VGroup(*[Line(L.p(L.t0, v), L.p(L.t1, v), color=color, stroke_width=ancho) for v in valores])


def campana_en(x: float, y: float, ancho: float = 1.0, alto: float = 0.7, color=SENAL) -> VMobject:
    """Mini campana centrada en (x, y) para los cortes verticales de un ensemble."""
    return campana_mini((x, y), ancho, alto, color, 3.0)


# ============================================================ capítulo 11, episodio 3: el color del ruido

ARCOIRIS = [ROJO, AMBAR, "#f2d04b", VERDE, CIAN, AZUL, MAGENTA]


def tele_S(w, alpha: float = 2.0):
    """Densidad espectral de la telegráfica: 2α / (α² + ω²) (con α = 2: 4 / (4 + ω²))."""
    w = np.asarray(w, dtype=float)
    return 2 * alpha / (alpha ** 2 + w ** 2)


def oculta(m: Mobject) -> Mobject:
    """Deja un mobject (o fórmula) en escena pero invisible: sus piezas se revelan con `revelar`."""
    m.set_opacity(0)
    return m


def revelar(*piezas: Mobject) -> list:
    """Animaciones que hacen visibles piezas de un grupo ya agregado y oculto."""
    return [p.animate.set_opacity(1) for p in piezas]


class Espectro(VGroup):
    """Ejes de frecuencia centrados (−ω_max…ω_max) con la altura desde cero. `centro` es la base, en el medio.

        e = Espectro(w_max=8, y_max=1.2, ancho=6.0, alto=3.0, centro=(0, -1.5))
        g = e.curva(tele_S)                       # la curva
        e.area(g, -2, 2, AMBAR)                   # área sombreada
        e.flecha(0, 1.0, ROJO)                    # impulso (flecha vertical) en ω = 0
    Atributos: `.ejes` (Axes), `.etiquetas`. `p(w, y)` da el punto en pantalla.
    """

    def __init__(self, w_max: float = 6.0, y_max: float = 1.2, ancho: float = 6.5, alto: float = 3.0,
                 centro=(0.0, 0.0), x_label=r"\omega", y_label=None):
        super().__init__()
        self.w_max, self.y_max = w_max, y_max
        ax, et = ejes([-w_max, w_max, 1], [0, y_max, y_max / 4], ancho=ancho, alto=alto,
                      x_label=x_label, y_label=y_label)
        d = np.array([centro[0], centro[1], 0.0]) - ax.c2p(0, 0)
        ax.shift(d)
        et.shift(d)
        self.ejes, self.etiquetas = ax, et
        self.add(ax, et)

    def p(self, w: float, y: float = 0.0) -> np.ndarray:
        return self.ejes.c2p(w, y)

    def curva(self, f, color=AMBAR, ancho: float = 4.0, a=None, b=None) -> VMobject:
        a = -self.w_max if a is None else a
        b = self.w_max if b is None else b
        return self.ejes.plot(lambda w: float(f(w)), x_range=[a, b, 0.05], color=color, stroke_width=ancho)

    def area(self, graf, a: float, b: float, color=AMBAR, opacidad: float = 0.4) -> VMobject:
        return self.ejes.get_area(graf, x_range=[a, b], color=color, opacity=opacidad)

    def arcoiris(self, graf, n: int = 7) -> VGroup:
        """El área bajo la curva en franjas verticales de colores (la «luz» del espectro)."""
        bordes = np.linspace(-self.w_max, self.w_max, n + 1)
        return VGroup(*[self.area(graf, bordes[i], bordes[i + 1], ARCOIRIS[i % len(ARCOIRIS)], 0.55)
                        for i in range(n)])

    def flecha(self, w: float, h: float, color=AMBAR, ancho: float = 7.0) -> Arrow:
        return Arrow(self.p(w, 0), self.p(w, h), buff=0, color=color, stroke_width=ancho,
                     max_tip_length_to_length_ratio=0.25)


def prisma(color=CIAN) -> VGroup:
    """Prisma que abre un rayo blanco en siete colores. `.tri`, `.entrada`, `.salidas`."""
    tri = Polygon([-0.8, -0.7, 0], [0.8, -0.7, 0], [0, 0.7, 0], color=TXT, stroke_width=4).set_fill(color, 0.14)
    entrada = Line([-2.4, -0.25, 0], [-0.3, -0.02, 0], color=TXT, stroke_width=5)
    salidas = VGroup(*[Line([0.3, -0.02, 0], [2.4, 0.6 - i * 0.25, 0], color=c, stroke_width=4)
                       for i, c in enumerate(ARCOIRIS)])
    g = VGroup(tri, entrada, salidas)
    g.tri, g.entrada, g.salidas = tri, entrada, salidas
    return g


def resistencia(color=TXT) -> VGroup:
    """Resistencia eléctrica (zigzag con cables)."""
    pts = [(-1.2, 0), (-0.8, 0), (-0.65, 0.3), (-0.35, -0.3), (-0.05, 0.3), (0.25, -0.3), (0.55, 0.3),
           (0.7, 0), (1.2, 0)]
    m = VMobject(stroke_color=color, stroke_width=4).set_fill(opacity=0)
    m.set_points_as_corners([np.array([x, y, 0.0]) for x, y in pts])
    return VGroup(m)


# ============================================================ capítulo 11, episodio 2: espectros que existen y que no

def curva_f(L: Lienzo, f, x0: float, x1: float, color=SENAL, ancho: float = 4.0, n: int = 160) -> VMobject:
    """Gráfica de la función `f` (vectorizada) entre x0 y x1 sobre un lienzo."""
    x = np.linspace(x0, x1, n)
    return L.curva(x, f(x), color, ancho)


def area_f(L: Lienzo, f, x0: float, x1: float, color=AMBAR, opacidad: float = 0.4, n: int = 90,
           piso: float = 0.0) -> VMobject:
    """Región entre la gráfica de `f` y la altura `piso` (sombreada), entre x0 y x1."""
    x = np.linspace(x0, x1, n)
    arriba = np.column_stack([L.x(x), L.y(f(x)), np.zeros(n)])
    abajo = np.column_stack([L.x(x[::-1]), L.y(np.full(n, piso)), np.zeros(n)])
    m = VMobject(stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)
    m.set_points_as_corners(np.vstack([arriba, abajo]))
    return m


def ejes_L(L: Lienzo, v0: float, v1: float, x_eje: float = 0.0, color=INK, ancho: float = 2.0) -> VGroup:
    """Eje horizontal (v = 0) a lo ancho del lienzo y eje vertical en `x_eje` entre v0 y v1. `.h`, `.v`."""
    h = L.base(color, ancho)
    v = Line(L.p(x_eje, v0), L.p(x_eje, v1), color=color, stroke_width=ancho)
    g = VGroup(h, v)
    g.h, g.v = h, v
    return g


def ventana(L: Lienzo, w0: float, w1: float, v1: float, color=AMBAR, opacidad: float = 0.22) -> Rectangle:
    """Ventanita del colador ideal: franja de frecuencias [w0, w1] de altura v1."""
    a, b = L.p(w0, 0), L.p(w1, v1)
    r = Rectangle(width=abs(b[0] - a[0]), height=abs(b[1] - a[1]), color=color, stroke_width=3)
    r.set_fill(color, opacidad).move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])
    return r


def psd_tele(w):
    """Densidad espectral de la telegráfica con α = 2: 4 / (4 + ω²)."""
    w = np.asarray(w, dtype=float)
    return 4.0 / (4.0 + w ** 2)


def r_tele(t):
    """Autocorrelación de la telegráfica con α = 2: e^(−2|τ|)."""
    return np.exp(-2.0 * np.abs(np.asarray(t, dtype=float)))


def sinc2x(w):
    """Transformada del rectángulo de altura 1 entre −1 y 1: 2 sen ω / ω (vale 2 en ω = 0)."""
    w = np.asarray(w, dtype=float)
    return 2.0 * np.sinc(w / np.pi)


def espectro_3b(rho: float):
    """Espectro de las tres barras ρ, 1, ρ: 1 + 2ρ cos Ω."""
    return lambda w: 1.0 + 2.0 * rho * np.cos(np.asarray(w, dtype=float))


def rotulo_tex(tex: str, color=TXT, escala: float = 0.8, pos=(0.0, 0.0)) -> MathTex:
    """Fórmula suelta, centrada en `pos`."""
    return MathTex(tex, color=color).scale(escala).move_to([pos[0], pos[1], 0])


# ============================================================ capítulo 11, episodio 1: espectro y potencia

def seno_t(L: Lienzo, frec: float, amp: float = 1.0, color=SENAL, ancho: float = 3.2,
           puntos: int = 260) -> VMobject:
    """Seno de `frec` hercios sobre un lienzo cuyo tiempo va en segundos."""
    t = np.linspace(L.t0, L.t1, puntos)
    return L.curva(t, amp * np.sin(2 * np.pi * frec * t), color, ancho)


def ruido_t(L: Lienzo, semilla: int = 3, amp: float = 0.5, color=RUIDO, ancho: float = 2.4,
            puntos: int = 200) -> VMobject:
    """Ruido (serie sin memoria) sobre un lienzo, con semilla fija."""
    t = np.linspace(L.t0, L.t1, puntos)
    return L.curva(t, amp * serie(semilla, puntos, 0.0), color, ancho)


def voz_valores(puntos: int = 260) -> np.ndarray:
    """Valores de una «voz»: dos senos con una envolvente que sube y baja (en [−1, 1] aprox.)."""
    u = np.linspace(0, 1, puntos)
    env = np.abs(np.sin(np.pi * u * 2.0)) ** 0.7
    return env * (0.7 * np.sin(2 * np.pi * 3.0 * u * 4) + 0.4 * np.sin(2 * np.pi * 7.0 * u * 4))


def voz_t(L: Lienzo, color=SENAL, ancho: float = 2.6, puntos: int = 260) -> VMobject:
    """Una «voz» sobre un lienzo."""
    t = np.linspace(L.t0, L.t1, puntos)
    return L.curva(t, voz_valores(puntos), color, ancho)


def espectro_ruidoso(centro=(0.0, 0.0), ancho: float = 3.0, alto: float = 1.2, semilla: int = 5,
                     color=RUIDO, n: int = 70) -> VMobject:
    """Un espectro «dentado» (el de una grabación de ruido): picos al azar."""
    rng = np.random.default_rng(semilla)
    x = np.linspace(-ancho / 2, ancho / 2, n)
    y = rng.random(n) ** 1.5
    return traza(centro[0] + x, centro[1] - alto / 2 + y * alto, color, 2.2)


def colador(color=CIAN, ancho: float = 1.3, alto: float = 1.0) -> VGroup:
    """Colador de frecuencias (embudo con agujeritos). `.cuerpo`, `.agujeros`."""
    a = ancho
    cuerpo = Polygon([-a / 2, alto / 2, 0], [a / 2, alto / 2, 0], [a * 0.16, -alto / 2, 0], [-a * 0.16, -alto / 2, 0],
                     color=color, stroke_width=3.5).set_fill(color, 0.15)
    pos = [(-0.28, 0.2), (0.0, 0.2), (0.28, 0.2), (-0.14, -0.05), (0.14, -0.05), (0.0, -0.28)]
    agujeros = VGroup(*[Dot([px * a, py * alto, 0], radius=0.05, color=color) for px, py in pos])
    g = VGroup(cuerpo, agujeros)
    g.cuerpo, g.agujeros = cuerpo, agujeros
    return g


class BarrasF(VGroup):
    """Espectro de barras sobre un eje de frecuencias.

        b = BarrasF([2, 5], [1.0, 0.6], f_max=7, ancho=5.6, alto=2.0, centro=(0, 0), rotulos=["2 Hz", "5 Hz"])
    Atributos: `.base` (el eje), `.barras` (lista de Line), `.puntas` (Dot), `.rot` (rótulos).
    `x(f)` da la abscisa en pantalla; `simetrico=True` pone el cero al centro.
    """

    def __init__(self, frecs, alturas, f_max: float = 7.0, ancho: float = 5.6, alto: float = 2.0,
                 centro=(0.0, 0.0), color=SENAL, rotulos=None, simetrico: bool = False):
        super().__init__()
        self.cx, self.cy = centro
        self.ancho, self.alto, self.f_max, self.simetrico = ancho, alto, f_max, simetrico
        y0 = self.cy - alto / 2
        izq = self.cx - ancho / 2
        self.base = Line([izq, y0, 0], [izq + ancho, y0, 0], color=INK, stroke_width=2.5)
        self.barras, self.puntas, self.rot = [], [], VGroup()
        for i, (f, h) in enumerate(zip(frecs, alturas)):
            xf = self.x(f)
            b = Line([xf, y0, 0], [xf, y0 + h * alto, 0], color=color, stroke_width=7)
            p = Dot([xf, y0 + h * alto, 0], radius=0.09, color=color)
            self.barras.append(b)
            self.puntas.append(p)
            if rotulos:
                self.rot.add(Text(rotulos[i], color=INK).scale(0.45).move_to([xf, y0 - 0.32, 0]))
        self.add(self.base, *self.barras, *self.puntas, self.rot)

    def x(self, f: float) -> float:
        if self.simetrico:
            return self.cx + f / self.f_max * self.ancho / 2
        return self.cx - self.ancho / 2 + f / self.f_max * self.ancho


def area_bajo(L: Lienzo, t, v, color=AMBAR, opacidad: float = 0.4) -> VMobject:
    """Área entre la curva (t, v) y el eje v = 0, como polígono relleno."""
    t = np.asarray(t, dtype=float)
    v = np.asarray(v, dtype=float)
    pts = np.column_stack([L.x(t), L.y(v), np.zeros(len(t))])
    cierre = np.array([[L.x(t[-1]), L.y(0.0), 0.0], [L.x(t[0]), L.y(0.0), 0.0]])
    m = VMobject(stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)
    m.set_points_as_corners(np.vstack([pts, cierre]))
    return m


def psd_tele(w):
    """Densidad espectral de la telegráfica con alfa = 2: 4 / (4 + w²)."""
    return 4.0 / (4.0 + np.asarray(w) ** 2)


def autocorr_tele(t):
    """Autocorrelación de la telegráfica con alfa = 2: e^(−2|t|)."""
    return np.exp(-2.0 * np.abs(np.asarray(t)))


def relleno_bajo(L: Lienzo, t, v, color=AMBAR, opacidad: float = 0.35) -> VMobject:
    """Área entre la curva (t, v) y la línea v = 0 del lienzo, como polígono relleno sin borde."""
    t = np.asarray(t, dtype=float)
    v = np.asarray(v, dtype=float)
    xs = np.concatenate([[t[0]], t, [t[-1]]])
    ys = np.concatenate([[0.0], v, [0.0]])
    m = VMobject(stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)
    m.set_points_as_corners(np.column_stack([L.x(xs), L.y(ys), np.zeros(len(xs))]))
    return m


# ============================================================ capítulo 11, episodio 4: de los datos al espectro

F_TONO_1, F_TONO_2 = 50.0, 50.5      # los dos tonos que vuelven en las escenas 06, 09 y 10 (hercios)


def cambios_tel(semilla: int, t_max: float, tasa: float = 1.0) -> list:
    """Instantes de cambio de una telegráfica (llegadas de Poisson de `tasa` por segundo), con semilla fija."""
    rng = np.random.default_rng(semilla)
    t, out = 0.0, []
    while True:
        t += rng.exponential(1.0 / tasa)
        if t >= t_max:
            return out
        out.append(round(float(t), 3))


def marco_t(L: Lienzo, t0: float, t1: float, v: float = 1.4, color=AMBAR, opacidad: float = 0.12) -> Rectangle:
    """Ventana de observación: franja [t0, t1] sobre un lienzo, de altura ±v."""
    a, b = L.p(t0, -v), L.p(t1, v)
    r = Rectangle(width=abs(b[0] - a[0]), height=abs(b[1] - a[1]), color=color, stroke_width=3.5)
    return r.set_fill(color, opacidad).move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])


def periodograma_blanco(semilla: int, k: int = 80, M: int = 1) -> np.ndarray:
    """Periodograma de la moneda (espectro verdadero = 1) promediado sobre M trozos.
    En cada frecuencia vale la media de M exponenciales de media 1: media 1 y desviación 1/√M."""
    return np.random.default_rng(semilla).exponential(1.0, (M, k)).mean(axis=0)


def bosque_f(L: Lienzo, valores, color=RUIDO, ancho: float = 2.2, opacidad: float = 1.0) -> VMobject:
    """Curva de `valores` repartida a lo ancho de un lienzo (de t0 a t1)."""
    return L.curva(np.linspace(L.t0, L.t1, len(valores)), valores, color, ancho, opacidad)


def tonos_medidos(f, L: float):
    """Lo que se mide de los tonos de 50 y 50,5 Hz con una ventana de L segundos: dos sinc² de ancho 1/L."""
    f = np.asarray(f, dtype=float)
    return 0.9 * (np.sinc(L * (f - F_TONO_1)) ** 2 + np.sinc(L * (f - F_TONO_2)) ** 2)


def tijera(color=TXT) -> VGroup:
    """Tijeras abiertas. `.hojas`, `.anillos`."""
    hojas = VGroup(Line([-0.4, -0.35, 0], [0.45, 0.65, 0], color=color, stroke_width=6),
                   Line([0.4, -0.35, 0], [-0.45, 0.65, 0], color=color, stroke_width=6))
    anillos = VGroup(Circle(radius=0.2, color=AMBAR, stroke_width=5).move_to([-0.42, -0.62, 0]),
                     Circle(radius=0.2, color=AMBAR, stroke_width=5).move_to([0.42, -0.62, 0]))
    g = VGroup(hojas, anillos)
    g.hojas, g.anillos = hojas, anillos
    return g


def perilla(rotulo: str, color=AMBAR, radio: float = 0.7) -> VGroup:
    """Perilla con su rótulo debajo. `.disco`, `.txt`; la aguja es `.aguja` y la escena la agrega aparte
    (se gira con `Rotate(p.aguja, ang, about_point=p.disco.get_center())`)."""
    disco = Circle(radius=radio, color=color, stroke_width=4).set_fill(color, 0.14)
    txt = Text(rotulo, color=color).scale(0.5).next_to(disco, DOWN, buff=0.28)
    g = VGroup(disco, txt)
    g.disco, g.txt = disco, txt
    g.aguja = Line(disco.get_center(), disco.get_center() + UP * radio * 0.85, color=TXT, stroke_width=6)
    return g


def foto(color=INK, nitida: bool = True) -> VGroup:
    """Fotografía (marco, sol y montañas). Con `nitida=False` queda movida: tres copias desplazadas y tenues."""
    def una(dx, op):
        marco = RoundedRectangle(corner_radius=0.1, width=1.5, height=1.1, color=color, stroke_width=3.5,
                                 stroke_opacity=op).set_fill(FONDO, 0)
        sol_ = Circle(radius=0.12, color=AMBAR, stroke_width=0).set_fill(AMBAR, op).move_to([-0.35, 0.25, 0])
        mont = VMobject(stroke_color=SENAL, stroke_width=4, stroke_opacity=op).set_fill(opacity=0)
        mont.set_points_as_corners([np.array(p) for p in
                                    [(-0.7, -0.4, 0), (-0.2, 0.05, 0), (0.1, -0.2, 0), (0.35, 0.1, 0), (0.7, -0.4, 0)]])
        return VGroup(marco, sol_, mont).shift(RIGHT * dx)
    if nitida:
        return una(0, 1.0)
    return VGroup(una(-0.1, 0.3), una(0.0, 0.45), una(0.1, 0.3))


# ============================================================ capítulo 11, episodio 7: dos procesos, frecuencia a frecuencia

def microfono(color=INK) -> VGroup:
    """Micrófono plano de pie (~1 de alto). `.capsula`."""
    cap = RoundedRectangle(corner_radius=0.17, width=0.34, height=0.58, color=color,
                           stroke_width=4).set_fill(color, 0.25).move_to([0, 0.2, 0])
    arco = Arc(radius=0.3, start_angle=PI, angle=PI, color=color, stroke_width=4).move_arc_center_to([0, 0.2, 0])
    pie = Line([0, -0.1, 0], [0, -0.36, 0], color=color, stroke_width=4)
    base = Line([-0.22, -0.36, 0], [0.22, -0.36, 0], color=color, stroke_width=4)
    g = VGroup(cap, arco, pie, base)
    g.capsula = cap
    return g


def flecha_c(o, largo: float, grados: float, color=AMBAR, ancho: float = 6) -> Arrow:
    """Flecha desde `o`, con un largo y un ángulo en grados (un número complejo dibujado)."""
    th = np.deg2rad(grados)
    o = np.array([o[0], o[1], 0.0])
    return Arrow(o, o + largo * np.array([np.cos(th), np.sin(th), 0.0]), buff=0, color=color,
                 stroke_width=ancho, max_tip_length_to_length_ratio=0.2)


def plano_c(centro=(0.0, 0.0), radio: float = 1.6, color=INK) -> VGroup:
    """Plano complejo: dos ejes y la circunferencia del largo `radio`. `.circ`, `.o`."""
    c = np.array([centro[0], centro[1], 0.0])
    h = Line(c + LEFT * (radio + 0.35), c + RIGHT * (radio + 0.35), color=color, stroke_width=2)
    v = Line(c + DOWN * (radio + 0.35), c + UP * (radio + 0.35), color=color, stroke_width=2)
    circ = Circle(radius=radio, color=color, stroke_width=2, stroke_opacity=0.5).move_to(c)
    g = VGroup(h, v, circ)
    g.circ, g.o, g.radio = circ, c, radio
    return g


def parabola_l(centro=(0.0, 0.0), ancho: float = 4.2, alto: float = 2.6, fondo: float = 0.25,
               color=AMBAR, x_eje: float = 0.0) -> VGroup:
    """Parábola sobre un eje horizontal (el del cero). `fondo` es su mínimo, en unidades del eje
    (positivo: por encima del eje; 0: lo toca; negativo: lo corta). `.eje`, `.curva`, `.L`."""
    L = Lienzo(ancho=ancho, alto=alto, t_rango=(-2, 2), v_max=2.0, centro=centro)
    eje = L.base(INK, 2.0)
    f = lambda x: 0.45 * np.asarray(x) ** 2 + fondo
    cur = curva_f(L, f, -1.9, 1.9, color, 4.0)
    g = VGroup(eje, cur)
    g.eje, g.curva, g.L = eje, cur, L
    return g


def nube_puntos(centro=(0.0, 0.0), n: int = 26, ancho: float = 2.6, semilla: int = 4, color=SENAL) -> VGroup:
    """Nube de puntos sin relación (dos coordenadas independientes)."""
    rng = np.random.default_rng(semilla)
    xs, ys = rng.normal(0, 0.45, n), rng.normal(0, 0.45, n)
    return VGroup(*[Dot([centro[0] + x * ancho / 2, centro[1] + y * ancho / 2, 0], radius=0.07, color=color)
                    for x, y in zip(xs, ys)])


# ============================================================ capítulo 11, episodio 5: cortar sin romper

COLOR_VENTANA = {"rect": AMBAR, "hann": VERDE, "blackman": AZUL}
NOMBRE_VENTANA = {"rect": "rectangular", "hann": "Hann", "blackman": "Blackman"}


def tijeras(color=TXT) -> VGroup:
    """Tijeras planas (dos hojas cruzadas y dos aros). `.hojas`, `.aros`."""
    a = Line([-0.5, -0.42, 0], [0.7, 0.4, 0], color=color, stroke_width=5)
    b = Line([-0.5, 0.42, 0], [0.7, -0.4, 0], color=color, stroke_width=5)
    r1 = Circle(radius=0.19, color=AMBAR, stroke_width=4).move_to([-0.72, 0.5, 0])
    r2 = Circle(radius=0.19, color=AMBAR, stroke_width=4).move_to([-0.72, -0.5, 0])
    g = VGroup(a, b, r1, r2)
    g.hojas, g.aros = VGroup(a, b), VGroup(r1, r2)
    return g


def bombilla(color=AMBAR) -> VGroup:
    """Bombilla plana con rayitos (la idea). `.bulbo`."""
    bulbo = Circle(radius=0.34, color=color, stroke_width=4).set_fill(color, 0.25)
    base = Rectangle(width=0.3, height=0.2, color=color, stroke_width=3).set_fill(color, 0.5)
    base.next_to(bulbo, DOWN, buff=-0.04)
    rayos = VGroup(*[Line(bulbo.get_center() + 0.46 * np.array([np.cos(a), np.sin(a), 0]),
                          bulbo.get_center() + 0.64 * np.array([np.cos(a), np.sin(a), 0]),
                          color=color, stroke_width=3) for a in np.deg2rad([20, 60, 100, 140, 180, 0])])
    g = VGroup(bulbo, base, rayos)
    g.bulbo = bulbo
    return g


def lienzo_f(f0: float, f1: float, alto: float, ancho: float = 8.0, cx: float = 0.0, base_y: float = -2.0,
             v_max: float = 1.0) -> Lienzo:
    """Lienzo de frecuencias (Hz): el cero del eje vertical está en `base_y` y `v_max` llega `alto` más arriba."""
    return Lienzo(ancho=ancho, alto=2 * alto, t_rango=(f0, f1), v_max=v_max, centro=(cx, base_y))


def lienzo_db(ancho: float, alto: float, x_max: float, top: float, cx: float = 0.0, db: float = 80.0) -> Lienzo:
    """Lienzo en decibelios: 0 dB arriba (en `top`), −`db` dB `alto` más abajo; el eje horizontal va de 0 a `x_max`."""
    return Lienzo(ancho=ancho, alto=2 * alto, t_rango=(0, x_max), v_max=db, centro=(cx, top))


def sinc_abs(f, f0: float, T: float = 1.0):
    """|sinc| del tono de `f0` hercios recortado `T` segundos: la «raya» que se abre en faldas."""
    return np.abs(np.sinc(T * (np.asarray(f, dtype=float) - f0)))


def valores_ventana(tipo: str, n: int) -> np.ndarray:
    """Ventana de `n` muestras: 'rect', 'hann' o 'blackman' (versión periódica)."""
    k = np.arange(n)
    if tipo == "rect":
        return np.ones(n)
    if tipo == "hann":
        return 0.5 - 0.5 * np.cos(2 * np.pi * k / n)
    return 0.42 - 0.5 * np.cos(2 * np.pi * k / n) + 0.08 * np.cos(4 * np.pi * k / n)


def nucleo_db(tipo: str, x, n: int = 64, piso: float = 80.0):
    """Núcleo de la ventana en decibelios (0 dB en el pico) a `x` «bines» del centro; recortado en −`piso`."""
    w = valores_ventana(tipo, n)
    nfft = n * 64
    W = np.abs(np.fft.rfft(w, nfft))
    W = W / W[0]
    f = np.arange(len(W)) * n / nfft
    db = 20 * np.log10(np.maximum(np.interp(np.abs(np.asarray(x, dtype=float)), f, W), 1e-6))
    return np.maximum(db, -piso)


def ventana_t(L: Lienzo, tipo: str, color=None, ancho: float = 3.5, n: int = 200) -> VMobject:
    """Forma de la ventana en el tiempo sobre un lienzo de t en [0, 1]."""
    t = np.linspace(0, 1, n, endpoint=False)
    return L.curva(t, valores_ventana(tipo, n), color or COLOR_VENTANA[tipo], ancho)


def copias_trozo(L: Lienzo, f: float, i0: int = -2, i1: int = 2, color=SENAL, ancho: float = 3.0,
                 opacidad_vecinas: float = 0.55) -> VGroup:
    """Un trozo de 1 s de coseno de `f` hercios repetido en [i0, i1 + 1]; el del centro (i = 0) es el original."""
    t = np.linspace(0, 1, 40 + int(40 * f), endpoint=False)
    cs = []
    for i in range(i0, i1 + 1):
        cs.append(L.curva(t + i, np.cos(2 * np.pi * f * t), color, ancho, 1.0 if i == 0 else opacidad_vecinas))
    return VGroup(*cs)


def fichas(textos, color=AMBAR, ancho: float = 3.6, alto: float = 0.8, escala: float = 0.5, buff: float = 0.25,
           direccion=DOWN, encendidas: bool = False) -> VGroup:
    """Fila (o columna) de fichas rotuladas, apagadas (borde tenue); `encender(f)` las enciende."""
    g = VGroup(*[caja(t, color, ancho=ancho, alto=alto, scale=escala) for t in textos]).arrange(direccion, buff=buff)
    if not encendidas:
        g.set_opacity(0.0)
    return g


def trozos_solapados(L: Lienzo, n: int = 5, largo: float = 2.4, paso: float = 1.2, con_hann: bool = True,
                     alto: float = 0.9, semilla: int = 5) -> tuple[VMobject, VGroup, VGroup]:
    """Registro `y(t)` partido en `n` trozos de `largo` solapados con `paso`.
    Devuelve `(registro, marcos, campanas)`: el registro, un rectángulo por trozo y su campana de Hann."""
    t0, t1 = L.t0, L.t0 + paso * (n - 1) + largo
    t = np.linspace(t0, t1, 300)
    reg = L.curva(t, 0.45 * serie(semilla, 300, 0.7), SENAL, 2.6)
    marcos, campanas = VGroup(), VGroup()
    colores = [AMBAR, CIAN]
    for i in range(n):
        a = t0 + i * paso
        p0, p1 = L.p(a, 0), L.p(a + largo, 0)
        # los trozos alternan de fila para que se vean los solapes
        dy = (-1 if i % 2 else 1) * (alto * 0.62)
        r = Rectangle(width=p1[0] - p0[0], height=alto, color=colores[i % 2], stroke_width=2.5)
        r.move_to([(p0[0] + p1[0]) / 2, p0[1] + dy + (0.0), 0]).set_fill(colores[i % 2], 0.05)
        marcos.add(r)
        if con_hann:
            u = np.linspace(0, 1, 60)
            campanas.add(traza(p0[0] + u * (p1[0] - p0[0]), p0[1] + dy - alto / 2 + valores_ventana("hann", 60) * alto * 0.9,
                               colores[i % 2], 3.0))
    return reg, marcos, campanas


class ParAlfa:
    """El par autocorrelación ↔ espectro de la telegráfica, movido por un mismo α (`ValueTracker`).

        p = ParAlfa(alfa=2.0)
        self.add(p.auto(), p.espec(), *p.guias())     # curvas que se redibujan solas
        self.play(p.a.animate.set_value(8.0))          # moverlo
    `L` es el lienzo de la autocorrelación (e^{−α|τ|}) y `esp` el espectro (2α/(α²+ω²), α = 0,5…8).
    """

    def __init__(self, alfa: float = 2.0, c_auto=(-3.6, -0.3), c_esp=(3.9, -2.3), ancho: float = 6.0):
        self.a = ValueTracker(alfa)
        self.L = Lienzo(ancho=ancho, alto=2.6, t_rango=(-3, 3), v_max=1.25, centro=c_auto)
        self.esp = Espectro(w_max=16, y_max=4.2, ancho=ancho, alto=3.4, centro=c_esp)
        self.tt = np.linspace(-3, 3, 600)

    def auto(self, color=AMBAR) -> VMobject:
        return always_redraw(lambda: self.L.curva(self.tt, np.exp(-self.a.get_value() * np.abs(self.tt)), color, 4))

    def espec(self, color=AMBAR) -> VMobject:
        return always_redraw(lambda: self.esp.curva(lambda w: tele_S(w, self.a.get_value()), color, 4))

    def area_espec(self, color=AMBAR, opacidad: float = 0.3) -> VMobject:
        return always_redraw(lambda: self.esp.area(self.esp.curva(lambda w: tele_S(w, self.a.get_value())),
                                                   -self.esp.w_max, self.esp.w_max, color, opacidad))

    def mitad(self, color=VERDE) -> VGroup:
        """El punto de media altura (ω = α, S = 1/α) con sus guías."""
        def f():
            al = self.a.get_value()
            p = self.esp.p(al, 1.0 / al)
            return VGroup(Line(self.esp.p(al, 0), p, color=color, stroke_width=3),
                          Line(self.esp.p(0, 1.0 / al), p, color=color, stroke_width=3),
                          Dot(p, color=color, radius=0.1))
        return always_redraw(f)

    def deslizador(self, centro=(-3.6, -3.55), largo: float = 5.0) -> VGroup:
        """Barra con una perilla que sigue a α (escala logarítmica de 0,5 a 8)."""
        x0 = centro[0] - largo / 2
        pista = Line([x0, centro[1], 0], [x0 + largo, centro[1], 0], color=INK, stroke_width=3)
        perilla = always_redraw(lambda: Dot([x0 + largo * (np.log2(self.a.get_value()) + 1) / 4, centro[1], 0],
                                            color=AMBAR, radius=0.13))
        rot = MathTex(r"\alpha", color=AMBAR).scale(0.8).move_to([x0 - 0.4, centro[1], 0])
        a, b = Text("0,5", color=INK).scale(0.4).move_to([x0, centro[1] - 0.35, 0]), \
            Text("8", color=INK).scale(0.4).move_to([x0 + largo, centro[1] - 0.35, 0])
        return VGroup(pista, perilla, rot, a, b)


# ============================================================ capítulo 11, episodio 6: fabricar el color y quitarlo

def psd_eco(w):
    """Densidad espectral del eco (x[n] = 0,6 x[n−1] + w[n], w con varianza 1): 1 / (1,36 − 1,2 cos Ω)."""
    w = np.asarray(w, dtype=float)
    return 1.0 / (1.36 - 1.2 * np.cos(w))


def ecg_t(L: Lienzo, latidos: int = 6, color=VERDE, ancho: float = 2.8, puntos: int = 420) -> VMobject:
    """Un electrocardiograma (un complejo QRS por latido) sobre un lienzo."""
    t = np.linspace(L.t0, L.t1, puntos)
    f = ((t - L.t0) / (L.t1 - L.t0) * latidos) % 1.0
    v = (0.95 * np.exp(-((f - 0.30) / 0.022) ** 2) - 0.22 * np.exp(-((f - 0.26) / 0.02) ** 2)
         - 0.30 * np.exp(-((f - 0.34) / 0.02) ** 2) + 0.16 * np.exp(-((f - 0.60) / 0.07) ** 2))
    return L.curva(t, v, color, ancho)


def pulsaciones_t(L: Lienzo, color=AMBAR, ancho: float = 3.0, puntos: int = 240, ciclos: float = 3.0,
                  semilla: int = 4) -> VMobject:
    """Frecuencia cardíaca instante a instante: una oscilación lenta (la respiración) enterrada en ruido."""
    t = np.linspace(L.t0, L.t1, puntos)
    rng = np.random.default_rng(semilla)
    v = 0.55 * np.sin(2 * np.pi * ciclos * (t - L.t0) / (L.t1 - L.t0)) + 0.38 * rng.normal(0, 1, puntos)
    return L.curva(t, np.clip(v, -0.95, 0.95), color, ancho)


def lentas_t(L: Lienzo, color=AMBAR, ancho: float = 3.0, puntos: int = 240, ciclos: float = 3.0) -> VMobject:
    """La oscilación lenta sola (sin el ruido): ciclo de respiración."""
    t = np.linspace(L.t0, L.t1, puntos)
    return L.curva(t, 0.55 * np.sin(2 * np.pi * ciclos * (t - L.t0) / (L.t1 - L.t0)), color, ancho)


def pecho(color=CIAN) -> VGroup:
    """Tronco visto de frente con dos pulmones que se inflan. `.tronco`, `.pulmones`."""
    tronco = RoundedRectangle(width=1.5, height=1.7, corner_radius=0.5, color=color,
                              stroke_width=4).set_fill(color, 0.1)
    p1 = Ellipse(width=0.55, height=1.0, color=color, stroke_width=3).set_fill(color, 0.35).move_to([-0.33, 0, 0])
    p2 = Ellipse(width=0.55, height=1.0, color=color, stroke_width=3).set_fill(color, 0.35).move_to([0.33, 0, 0])
    pulmones = VGroup(p1, p2)
    g = VGroup(tronco, pulmones)
    g.tronco, g.pulmones = tronco, pulmones
    return g


def altavoz(color=TXT) -> VGroup:
    """Altavoz con tres ondas. `.cuerpo`, `.ondas`."""
    cuerpo = Polygon([-0.3, 0.25, 0], [0.0, 0.25, 0], [0.45, 0.65, 0], [0.45, -0.65, 0], [0.0, -0.25, 0],
                     [-0.3, -0.25, 0], color=color, stroke_width=4).set_fill(color, 0.2)
    ondas = VGroup(*[Arc(radius=0.35 + 0.28 * i, start_angle=-PI / 3.2, angle=2 * PI / 3.2, color=color,
                         stroke_width=4).shift(RIGHT * 0.45) for i in range(1, 4)])
    g = VGroup(cuerpo, ondas)
    g.cuerpo, g.ondas = cuerpo, ondas
    return g


def antena(color=TXT) -> VGroup:
    """Torre de comunicaciones con ondas. `.mastil`, `.ondas`."""
    mastil = Polygon([-0.25, -0.7, 0], [0.25, -0.7, 0], [0, 0.45, 0], color=color, stroke_width=4).set_fill(color, 0.12)
    punta = Dot([0, 0.55, 0], radius=0.09, color=color)
    ondas = VGroup(*[Arc(radius=0.3 * i, start_angle=PI / 4, angle=PI / 2, color=color, stroke_width=4)
                     .shift(UP * 0.55) for i in range(1, 4)])
    ondas2 = VGroup(*[Arc(radius=0.3 * i, start_angle=3 * PI / 4, angle=PI / 2, color=color, stroke_width=4)
                      .shift(UP * 0.55) for i in range(1, 4)])
    g = VGroup(mastil, punta, ondas, ondas2)
    g.mastil, g.ondas = mastil, VGroup(ondas, ondas2)
    return g


def muro(alto: float = 2.0, ancho: float = 0.5, color=ROJO) -> VGroup:
    """Muro de ladrillos (el límite que no se puede cruzar)."""
    r = Rectangle(width=ancho, height=alto, color=color, stroke_width=4).set_fill(color, 0.28)
    lineas = VGroup(*[Line([-ancho / 2, -alto / 2 + alto * k / 4, 0], [ancho / 2, -alto / 2 + alto * k / 4, 0],
                           color=color, stroke_width=2) for k in range(1, 4)])
    g = VGroup(r, lineas)
    return g


def luz_blanca(color_final=MAGENTA, largo: float = 2.4) -> VGroup:
    """Haz de luz blanca que atraviesa un vidrio y sale de color. `.entrada`, `.vidrio`, `.salida`."""
    entrada = Line([-largo, 0, 0], [-0.3, 0, 0], color=TXT, stroke_width=9)
    vidrio = Rectangle(width=0.5, height=1.3, color=color_final, stroke_width=3).set_fill(color_final, 0.45)
    salida = Line([0.3, 0, 0], [largo, 0, 0], color=color_final, stroke_width=9)
    g = VGroup(entrada, vidrio, salida)
    g.entrada, g.vidrio, g.salida = entrada, vidrio, salida
    return g


def barras_imp(valores, centro=(0.0, 0.0), paso: float = 0.9, unidad: float = 0.4, color=SENAL) -> Tallos:
    """Respuesta al impulso (o cualquier secuencia) como palitos: `Tallos` con los valores dados."""
    return Tallos(valores, centro=centro, paso=paso, unidad=unidad, color=color)


def cadena_bloques(rot_ent: str, rot_h: str, rot_sal: str, centro=(0.0, 0.0), color=CIAN, ancho: float = 7.0):
    """Cadena «entrada → [H] → salida» con tres rótulos de texto. Devuelve (grupo, caja, ent, sal)."""
    cx, cy = centro
    b = BloqueLTI(rot_h, centro=(cx, cy), ancho=1.8, alto=1.0, color=color, largo=1.7, escala=0.8)
    ent = Text(rot_ent, color=TXT).scale(0.5).next_to(b.p_ent(), LEFT, buff=0.15)
    sal = Text(rot_sal, color=TXT).scale(0.5).next_to(b.p_sal(), RIGHT, buff=0.15)
    g = VGroup(b, ent, sal)
    return g, b, ent, sal


def medida_tonos(L: float, M: int, semilla: int, n: int = 700):
    """(f, y) de lo que se mide en 49–51,5 Hz con trozos de L segundos promediados M veces: los dos tonos
    desenfocados (ancho 1/L) más un piso de ruido de media 0,35 que tiembla 0,35/√M."""
    f = np.linspace(49.0, 51.5, n)
    return f, tonos_medidos(f, L) + 0.35 * periodograma_blanco(semilla, n, M)


def nucleo_lin(tipo: str, x, n: int = 64):
    """Potencia (lineal, 1 en el pico) del núcleo de la ventana a `x` bines del centro."""
    return 10 ** (nucleo_db(tipo, x, n, piso=120.0) / 10.0)


def datos_dos_tonos(n: int, fs: float = 64.0, f1: float = 10.0, f2: float = 10.6) -> np.ndarray:
    """`n` muestras de dos tonos cercanos (a `fs` muestras por segundo)."""
    k = np.arange(n) / fs
    return np.cos(2 * np.pi * f1 * k) + np.cos(2 * np.pi * f2 * k + 0.7)


def espectro_fft(x, relleno: int = 0, fs: float = 64.0):
    """Módulo de la FFT de `x` con `relleno` ceros al final: devuelve `(f en Hz, |X|)`."""
    n = len(x) + relleno
    X = np.abs(np.fft.rfft(x, n))
    return np.arange(len(X)) * fs / n, X


def regla_db(L: Lienzo, valores=(0, -20, -40, -60), color=INK, escala: float = 0.4, guias: bool = True) -> VGroup:
    """Eje vertical en decibelios a la izquierda del lienzo, con marcas rotuladas (y guías tenues)."""
    g = VGroup()
    eje = Line(L.p(L.t0, min(valores) - 5), L.p(L.t0, 0), color=color, stroke_width=2)
    g.add(eje)
    for v in valores:
        p = L.p(L.t0, v)
        g.add(Line(p + LEFT * 0.08, p + RIGHT * 0.08, color=color, stroke_width=2))
        g.add(Text(f"{v} dB".replace("-", "−"), color=color).scale(escala).move_to(p + LEFT * 0.62))
        if guias:
            g.add(Line(p, L.p(L.t1, v), color=color, stroke_width=1, stroke_opacity=0.25))
    return g


def picos_laterales(tipo: str, x_max: float, n: int = 3000):
    """Posiciones y alturas (dB) de las cimas de los lóbulos laterales del núcleo en [0.3, x_max]."""
    x = np.linspace(0.3, x_max, n)
    y = nucleo_db(tipo, x, piso=120.0)
    idx = [i for i in range(1, n - 1) if y[i] > y[i - 1] and y[i] >= y[i + 1] and y[i] > -80 and x[i] > 0.8]
    return [(float(x[i]), float(y[i])) for i in idx]


# ============================================================ capítulo 12, episodio 1: el mejor filtro lineal

def sensor12(n: int = 40, semilla: int = 31):
    """El sensor del capítulo 12 centrado: y (varianza 4, memoria 0,6), v (ruido blanco de varianza 1) y x = y + v.
    Devuelve `(t, y, v, x)`. Semilla fija."""
    y = 2.0 * serie(semilla, n, 0.6)
    v = serie(semilla + 7, n, 0.0)
    return np.arange(n), y, v, y + v


def suavizada(x, a: float = 0.55) -> np.ndarray:
    """Una versión limpia de `x` (media móvil exponencial): sirve de «estimación» en los dibujos."""
    s = np.zeros(len(x))
    s[0] = x[0]
    for k in range(1, len(x)):
        s[k] = a * s[k - 1] + (1 - a) * x[k]
    return s


def flechas_xy(origen=(0.0, 0.0), largo: float = 3.4, angulo: float = 50.0):
    """El dibujo del capítulo 8 con las letras del capítulo 12: x (cian, el dato), y (azul, lo que se busca),
    ŷ (ámbar, la sombra) y e (rojo, el error). Devuelve `(F, rotulos)`: `F` es un `Flechas` y `rotulos` un
    diccionario de MathTex con las claves `x`, `y`, `yh` y `e`."""
    F = Flechas(origen=origen, largo=largo, angulo=angulo, largo_objetivo=largo * 0.9,
                color_dato=MEDIDA, color_objetivo=SENAL)
    rx = MathTex("x", color=MEDIDA).scale(0.9).next_to(F.fin_presente, RIGHT, buff=0.15)
    ry = MathTex("y", color=SENAL).scale(0.9).next_to(F.fin_futuro, UP, buff=0.15)
    mid = (F.fin_sombra + F.o) / 2
    ryh = MathTex(r"\hat{y}", color=ESTIMACION).scale(0.9).move_to(mid + DOWN * 0.4)
    re = MathTex("e", color=ERROR).scale(0.9).next_to((F.fin_sombra + F.fin_futuro) / 2, RIGHT, buff=0.15)
    return F, {"x": rx, "y": ry, "yh": ryh, "e": re}


class MatrizT(VGroup):
    """Matriz cuadrada de textos (para la de Toeplitz). `valores` es una lista de listas de cadenas.

    Atributos: `.celdas[i][j]` (Text), `.corchetes`, `diag(k)` (las celdas con |i − j| = k) y
    `col(color_por_diagonal)` para pintar cada diagonal con su color. `.p(i, j)` da el centro de la celda."""

    def __init__(self, valores, centro=(0.0, 0.0), lado: float = 1.15, escala: float = 0.75, color=TXT):
        super().__init__()
        self.n = len(valores)
        self.cx, self.cy, self.lado = centro[0], centro[1], lado
        self.celdas = [[None] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                t = Text(valores[i][j], color=color).scale(escala).move_to(self.p(i, j))
                self.celdas[i][j] = t
                self.add(t)
        w = self.n * lado / 2 + 0.1
        h = self.n * lado * 0.8 / 2 + 0.05
        c = np.array([self.cx, self.cy, 0.0])
        izq = VMobject(stroke_color=INK, stroke_width=4).set_fill(opacity=0)
        izq.set_points_as_corners([c + [-w + 0.18, h, 0], c + [-w, h, 0], c + [-w, -h, 0], c + [-w + 0.18, -h, 0]])
        der = VMobject(stroke_color=INK, stroke_width=4).set_fill(opacity=0)
        der.set_points_as_corners([c + [w - 0.18, h, 0], c + [w, h, 0], c + [w, -h, 0], c + [w - 0.18, -h, 0]])
        self.corchetes = VGroup(izq, der)
        self.add(self.corchetes)

    def p(self, i: int, j: int) -> np.ndarray:
        return np.array([self.cx + (j - (self.n - 1) / 2) * self.lado,
                         self.cy - (i - (self.n - 1) / 2) * self.lado * 0.8, 0.0])

    def diag(self, k: int) -> VGroup:
        return VGroup(*[self.celdas[i][j] for i in range(self.n) for j in range(self.n) if abs(i - j) == k])


# ============================================================ capítulo 12, episodio 6: innovación, predecir y filtrar

class Balanza(VGroup):
    """Balanza de dos platillos: `.viga`, `.mastil`, `.izq` y `.der` (platillos con su rótulo en `.rot_izq`, `.rot_der`).
    `inclinar(lado)` devuelve las animaciones para que baje el platillo `lado` ("izq" o "der")."""

    def __init__(self, centro=(0.0, 0.0), semi: float = 2.2, color=INK):
        super().__init__()
        self.c = np.array([centro[0], centro[1], 0.0])
        self.semi = semi
        self.mastil = Line(self.c + DOWN * 1.1, self.c, color=color, stroke_width=5)
        self.base = Line(self.c + DOWN * 1.1 + LEFT * 0.6, self.c + DOWN * 1.1 + RIGHT * 0.6, color=color, stroke_width=5)
        self.viga = Line(self.c + LEFT * semi, self.c + RIGHT * semi, color=TXT, stroke_width=6)
        self.izq = self._platillo(self.c + LEFT * semi)
        self.der = self._platillo(self.c + RIGHT * semi)
        self.add(self.mastil, self.base, self.viga, self.izq, self.der)

    @staticmethod
    def _platillo(extremo) -> VGroup:
        cuerda = VGroup(Line(extremo, extremo + DOWN * 0.7 + LEFT * 0.5, color=INK, stroke_width=2.5),
                        Line(extremo, extremo + DOWN * 0.7 + RIGHT * 0.5, color=INK, stroke_width=2.5))
        copa = Line(extremo + DOWN * 0.7 + LEFT * 0.6, extremo + DOWN * 0.7 + RIGHT * 0.6, color=TXT, stroke_width=6)
        return VGroup(cuerda, copa)

    def inclinar(self, lado: str, ang: float = 0.22) -> list:
        """Animaciones: la viga gira y el platillo `lado` baja, el otro sube."""
        s = 1 if lado == "izq" else -1          # izquierda baja girando en sentido antihorario
        dy = self.semi * np.sin(ang)
        bajar, subir = (self.izq, self.der) if lado == "izq" else (self.der, self.izq)
        return [Rotate(self.viga, s * ang, about_point=self.c),
                bajar.animate.shift(DOWN * dy), subir.animate.shift(UP * dy)]


class FilaMuestras(VGroup):
    """Fila de casillas con rótulo (muestras x[n−2], x[n−1], x[n]…). `.cas[i]`, `.rots[i]`; `x(i)` su posición.
    `marco(i0, i1, color)` devuelve un rectángulo que rodea las casillas i0..i1."""

    def __init__(self, rotulos, centro=(0.0, 0.0), lado: float = 0.9, color=MEDIDA, escala: float = 0.62):
        super().__init__()
        self.lado, self.cy, self.color = lado, centro[1], color
        n = len(rotulos)
        self.x0 = centro[0] - (n - 1) * lado / 2
        self.cas, self.rots = [], []
        for i, r in enumerate(rotulos):
            c = Square(side_length=lado * 0.92, color=color, stroke_width=3).set_fill(color, 0.14)
            c.move_to([self.x0 + i * lado, centro[1], 0])
            t = MathTex(r, color=TXT).scale(escala).move_to(c)
            self.cas.append(c)
            self.rots.append(t)
            self.add(c, t)

    def x(self, i: float) -> float:
        return self.x0 + i * self.lado

    def marco(self, i0: int, i1: int, color=AMBAR, relleno: float = 0.0) -> Rectangle:
        ancho = (i1 - i0 + 1) * self.lado + 0.1
        r = Rectangle(width=ancho, height=self.lado * 1.12, color=color, stroke_width=5)
        r.set_fill(color, relleno).move_to([(self.x(i0) + self.x(i1)) / 2, self.cy, 0])
        return r


def barra_h(valor: float, y: float, x0: float, esc: float, color=ERROR, alto: float = 0.42) -> Rectangle:
    """Barra horizontal que nace en `x0` y mide `valor · esc`."""
    r = Rectangle(width=max(valor * esc, 0.03), height=alto, color=color, stroke_width=0).set_fill(color, 0.85)
    r.move_to([x0 + max(valor * esc, 0.03) / 2, y, 0])
    return r


def eco_x(n: int = 32, semilla: int = 11, a: float = 0.6, sigma: float = 1.6) -> np.ndarray:
    """Realización del eco x[n] = a·x[n−1] + w[n] con w de varianza sigma². Semilla fija."""
    rng = np.random.default_rng(semilla)
    w = rng.normal(0, sigma, n)
    x = np.zeros(n)
    x[0] = w[0]
    for k in range(1, n):
        x[k] = a * x[k - 1] + w[k]
    return x


# ============================================================ capítulo 12, episodio 5: el sensor, de punta a punta

RHO_F = 0.157          # cero de la factorización (y polo del filtro causal)
K_COLAS = 2.826        # valor central de la secuencia de dos colas
H_CAUSAL_5 = (0.7386, 0.1158, 0.0182, 0.0028)   # respuesta al impulso del filtro causal


def dos_colas(centro=(0.0, 0.0), paso: float = 0.62, unidad: float = 0.5, m_min: int = -5, m_max: int = 6,
              indices: bool = True) -> Tallos:
    """Secuencia de dos colas K·0,6^m (m ≥ 0, azul) y K·0,157^|m| (m < 0, magenta), con la barra
    central en ámbar. `.m(k)` da el índice del palito de la posición `k`."""
    ms = list(range(m_min, m_max + 1))
    vals = [K_COLAS * (0.6 ** m if m >= 0 else RHO_F ** (-m)) for m in ms]
    t = Tallos(vals, centro=centro, paso=paso, unidad=unidad, color=SENAL, k0=m_min, indices=indices)
    for i, m in enumerate(ms):
        c = AMBAR if m == 0 else (RUIDO if m < 0 else SENAL)
        t.tallos[i].set_color(c)
        t.puntos[i].set_color(c)
    t.m = lambda k: k - m_min
    t.m_min, t.m_max = m_min, m_max
    return t


def marca_x(pos, color=AMBAR, lado: float = 0.2) -> VGroup:
    """Polo (×) del plano z."""
    p = np.array([pos[0], pos[1], 0.0])
    return VGroup(Line(p + UL * lado, p + DR * lado, color=color, stroke_width=5),
                  Line(p + UR * lado, p + DL * lado, color=color, stroke_width=5))


def marca_o(pos, color=AMBAR, radio: float = 0.14) -> Circle:
    """Cero (○) del plano z."""
    return Circle(radius=radio, color=color, stroke_width=5).move_to([pos[0], pos[1], 0])


class PlanoZ(VGroup):
    """Plano z: ejes y círculo unidad (de radio `radio` en pantalla). `p(x, y)` da el punto de pantalla
    del número complejo x + jy; `.circ` es el círculo unidad."""

    def __init__(self, centro=(0.0, 0.0), radio: float = 1.6, ver_unos: bool = True, ext_der: float | None = None):
        super().__init__()
        self.c = np.array([centro[0], centro[1], 0.0])
        self.R = radio
        ext = radio + 0.45
        self.h = Line(self.c + LEFT * ext, self.c + RIGHT * (ext if ext_der is None else ext_der),
                      color=INK, stroke_width=2)
        self.v = Line(self.c + DOWN * (radio + 0.3), self.c + UP * (radio + 0.3), color=INK, stroke_width=2)
        self.circ = Circle(radius=radio, color=INK, stroke_width=3).move_to(self.c)
        self.add(self.h, self.v, self.circ)
        if ver_unos:
            self.add(Text("1", color=INK).scale(0.4).move_to(self.p(1.0, 0.0) + DR * 0.22))

    def p(self, x: float, y: float = 0.0) -> np.ndarray:
        return self.c + self.R * np.array([x, y, 0.0])


class DiagramaRecursion(VGroup):
    """ŷ[n] = 0,157·ŷ[n−1] + 0,7386·x[n] como bloques. `centro` es el punto medio de la fila de arriba.
    Atributos: `.amp1` (×0,7386), `.suma`, `.retardo` (z⁻¹), `.amp2` (×0,157); flechas `.f_ent`, `.f_amp`,
    `.f_sal`, `.f_baja`, `.f_ret`, `.f_sube`; rótulos `.t_x`, `.t_y`. `P` guarda puntos de referencia."""

    def __init__(self, centro=(0.0, 0.5)):
        super().__init__()
        cx, cy = centro
        kw = dict(color=INK, stroke_width=3.5, buff=0, max_tip_length_to_length_ratio=0.25)
        self.t_x = MathTex("x[n]", color=MEDIDA).scale(0.8).move_to([cx - 5.7, cy, 0])
        self.amp1 = caja("× 0,7386", ESTIMACION, ancho=1.9, alto=0.8, scale=0.5).move_to([cx - 3.3, cy, 0])
        self.suma = VGroup(Circle(radius=0.32, color=TXT, stroke_width=3.5).set_fill(FONDO, 1),
                           MathTex("+", color=TXT).scale(0.8)).move_to([cx - 0.8, cy, 0])
        self.t_y = MathTex(r"\hat y[n]", color=ESTIMACION).scale(0.9).move_to([cx + 3.9, cy, 0])
        self.f_ent = Arrow([cx - 5.0, cy, 0], [cx - 4.3, cy, 0], **kw)
        self.f_amp = Arrow([cx - 2.35, cy, 0], [cx - 1.12, cy, 0], **kw)
        self.f_sal = Arrow([cx - 0.48, cy, 0], [cx + 3.35, cy, 0], **kw)
        by = cy - 1.9
        self.retardo = caja("z⁻¹", TXT, ancho=1.2, alto=0.8, scale=0.6).move_to([cx + 1.6, by, 0])
        self.amp2 = caja("× 0,157", ESTIMACION, ancho=1.9, alto=0.8, scale=0.5).move_to([cx - 0.8, by, 0])
        self.f_baja = Line([cx + 2.4, cy, 0], [cx + 2.4, by, 0], color=INK, stroke_width=3.5)
        self.f_ret = Arrow([cx + 2.4, by, 0], [cx + 2.2, by, 0], **kw)
        self.f_med = Arrow([cx + 1.0, by, 0], [cx + 0.17, by, 0], **kw)
        self.f_sube = Arrow([cx - 0.8, by + 0.4, 0], [cx - 0.8, cy - 0.34, 0], **kw)
        self.punto = Dot([cx + 2.4, cy, 0], radius=0.08, color=INK)
        self.P = dict(suma=self.suma.get_center(), amp1=self.amp1.get_center(), amp2=self.amp2.get_center(),
                      ret=self.retardo.get_center(), sal=self.t_y.get_center(), ent=self.t_x.get_center())
        self.add(self.t_x, self.f_ent, self.amp1, self.f_amp, self.suma, self.f_sal, self.t_y, self.punto,
                 self.f_baja, self.f_ret, self.retardo, self.f_med, self.amp2, self.f_sube)


def ficha_numero(txt: str, color=AMBAR, escala: float = 0.55) -> VGroup:
    """Número dentro de un círculo pequeño (un valor que viaja por un diagrama)."""
    t = Text(txt, color=FONDO, weight=BOLD).scale(escala)
    c = Circle(radius=max(0.3, t.width * 0.6 + 0.05), color=color, stroke_width=0).set_fill(color, 1)
    t.move_to(c)
    return VGroup(c, t)


def barras_error(valores, rotulos, centro=(0.0, -0.5), ancho: float = 7.0, alto: float = 3.0, v_max: float = 4.0,
                 colores=None) -> VGroup:
    """Barras verticales de error (una por tamaño de ventana). `.barras`, `.etiquetas`, `.valores_txt`, `p(i)`."""
    n = len(valores)
    paso = ancho / n
    base_y = centro[1] - alto / 2
    g = VGroup()
    g.barras, g.etiquetas, g.valores_txt = [], [], []
    for i, (v, r) in enumerate(zip(valores, rotulos)):
        x = centro[0] - ancho / 2 + (i + 0.5) * paso
        h = max(0.03, v / v_max * alto)
        col = (colores[i] if colores else ROJO)
        b = Rectangle(width=paso * 0.55, height=h, color=col, stroke_width=0).set_fill(col, 0.85)
        b.move_to([x, base_y + h / 2, 0])
        et = Text(r, color=INK).scale(0.42).move_to([x, base_y - 0.3, 0])
        vt = Text(num(v, 4) if v < 1 else num(v, 2), color=TXT).scale(0.42)
        vt.next_to(b, UP, buff=0.1)
        g.barras.append(b), g.etiquetas.append(et), g.valores_txt.append(vt)
    g.base = Line([centro[0] - ancho / 2, base_y, 0], [centro[0] + ancho / 2, base_y, 0], color=INK, stroke_width=2)
    g.add(g.base, *g.barras, *g.etiquetas)   # los valores los agrega la escena (`valores_txt`)
    return g


# ============================================================ capítulo 12, episodio 4: el futuro no está disponible

H_NO_CAUSAL = [0.017, 0.108, 0.686, 0.108, 0.017]     # filtro no causal del sensor, m = −2…2
H_CAUSAL = [0.7386, 0.1158, 0.0182]                   # filtro causal del sensor, m = 0…2
COLOR_PASO = {1: CIAN, 2: AMBAR, 3: VERDE}            # blanquear · parte causal · deshacer


def corona(color=AMBAR) -> VMobject:
    """Corona plana (~0,9 de ancho): «el mejor»."""
    pts = [(-0.45, -0.22), (-0.45, 0.2), (-0.22, 0.0), (0.0, 0.3), (0.22, 0.0), (0.45, 0.2), (0.45, -0.22)]
    m = Polygon(*[np.array([x, y, 0.0]) for x, y in pts], color=color, stroke_width=4)
    m.set_fill(color, 0.35)
    return m


def tira_blanca(valores=(1, -1, -1, 1, -1, 1, 1, -1), lado: float = 0.52, color=MEDIDA) -> VGroup:
    """La moneda ±1 (mediciones blancas) en una tira corta. `.celdas`."""
    return tira_pm1(list(valores), lado=lado, color=color, escala_txt=0.34)


def eje_muestras(y: float = 0.0, n_pasado: int = 6, n_futuro: int = 5, paso: float = 0.95, color=MEDIDA) -> VGroup:
    """Eje de tiempo con muestras: las ya llegadas (hasta «ahora») encendidas y las del futuro apagadas.
    `.base`, `.pasado` (lista, la última es el presente), `.futuro` (lista)."""
    n = n_pasado + n_futuro
    xs = [(i - (n - 1) / 2) * paso for i in range(n)]
    xs_p, xs_f = xs[:n_pasado], xs[n_pasado:]
    base = Line([xs_p[0] - 0.5, y, 0], [xs_f[-1] + 0.5, y, 0], color=INK, stroke_width=2)
    pas = [Dot([x, y, 0], radius=0.12, color=color) for x in xs_p]
    fut = [Dot([x, y, 0], radius=0.12, color=INK).set_opacity(0.35) for x in xs_f]
    g = VGroup(base, *pas, *fut)
    g.base, g.pasado, g.futuro = base, pas, fut
    return g


def cadena_cajas(rots, centro=(0.0, 0.0), colores=None, ancho: float = 2.3, hueco: float = 0.9,
                 alto: float = 0.9, escala: float = 0.5):
    """Cajas de texto unidas por flechas: «x → [blanquear] → ε». `rots` puede llevar `None` para una flecha sola.
    Devuelve (grupo, cajas, flechas)."""
    colores = colores or [AZUL] * len(rots)
    cajas = [caja(r, c, ancho=ancho, alto=alto, scale=escala) for r, c in zip(rots, colores)]
    g = VGroup(*cajas).arrange(RIGHT, buff=hueco).move_to([centro[0], centro[1], 0])
    fl = [flecha(a.get_right(), b.get_left(), INK, 3) for a, b in zip(cajas[:-1], cajas[1:])]
    return VGroup(g, *fl), cajas, fl


def tres_casillas(centro=(0.0, 0.0), activos=(1, 2, 3), textos=("blanquear", "parte causal", "deshacer"),
                  ancho: float = 3.3) -> VGroup:
    """Tres casillas numeradas 1, 2, 3 con el color de cada paso. `.casillas`."""
    cs = []
    for i, t in enumerate(textos, 1):
        c = caja(f"{i} · {t}", COLOR_PASO[i], ancho=ancho, alto=0.8, scale=0.5)
        cs.append(c)
    g = VGroup(*cs).arrange(RIGHT, buff=0.3).move_to([centro[0], centro[1], 0])
    g.casillas = cs
    return g


# ============================================================ capítulo 12, episodio 3: mirar el registro entero

def s_senal(w):
    """Densidad del sensor (señal y): 2,56 / |1 − 0,6 e^{−jΩ}|² (16 en 0, 1,88 en π/2, 1 en π)."""
    w = np.asarray(w, dtype=float)
    return 2.56 / (1.36 - 1.2 * np.cos(w))


def h_wiener(w):
    """Filtro de Wiener no causal del sensor: S_yy / (S_yy + 1) (0,94 · 0,65 · 0,5)."""
    s = s_senal(w)
    return s / (s + 1.0)


def g_prom(w):
    """Ganancia del promediador (½, ½): |cos(Ω/2)| (1 · 0,71 en π/2 · 0,16 en 0,9π · 0 en π)."""
    return np.abs(np.cos(np.asarray(w, dtype=float) / 2))


def h_inverso(w, tope: float = 40.0):
    """Ganancia del filtro inverso 1/|G| (recortada en `tope` para poder dibujarla)."""
    return np.minimum(1.0 / np.maximum(g_prom(w), 1e-6), tope)


def h_wiener_dec(w):
    """Ganancia de Wiener de la deconvolución con señal 1 y ruido 0,1: (1/|G|) · |G|² / (|G|² + 0,1)."""
    g = g_prom(w)
    return g / (g * g + 0.1)


def lienzo_omega(ancho: float = 8.0, alto: float = 2.6, v_max: float = 1.2, centro=(0.0, 0.0),
                 w0: float = 0.0, w1: float = float(np.pi)) -> Lienzo:
    """Lienzo para curvas de la frecuencia Ω (por defecto de 0 a π)."""
    return Lienzo(ancho=ancho, alto=alto, t_rango=(w0, w1), v_max=v_max, centro=centro)


def eje_omega(L: Lienzo, v1: float, completo: bool = False, color=INK, escala: float = 0.55) -> VGroup:
    """Eje horizontal de Ω con sus marcas (0, π/2, π; con `completo`, −π, 0, π) y eje vertical.
    `.h`, `.v`, `.rotulos`."""
    h = L.base(color, 2.0)
    x_v = 0.0 if completo else L.t0
    v = Line(L.p(x_v, 0.0), L.p(x_v, v1), color=color, stroke_width=2.0)
    pos = [(-np.pi, r"-\pi"), (0.0, "0"), (np.pi, r"\pi")] if completo else \
        [(0.0, "0"), (np.pi / 2, r"\pi/2"), (np.pi, r"\pi")]
    rot = VGroup(*[MathTex(t, color=INK).scale(escala).next_to(L.p(w, 0), DOWN, buff=0.14) for w, t in pos])
    g = VGroup(h, v, rot)
    g.h, g.v, g.rotulos = h, v, rot
    return g


def columna_ecuaciones(centro=(0.0, 0.0), escala: float = 0.7, paso: float = 0.78, ms=(-2, -1, 0, 1, 2)) -> VGroup:
    """Columna de ecuaciones «Σ h[j] C[m−j] = C[m]» para varios m, con puntos suspensivos arriba y abajo."""
    filas = VGroup(*[MathTex(rf"\sum_j h[j]\,C_{{xx}}[{m}-j]=C_{{yx}}[{m}]", color=TXT).scale(escala) for m in ms])
    arriba = MathTex(r"\vdots", color=INK).scale(escala)
    abajo = MathTex(r"\vdots", color=INK).scale(escala)
    g = VGroup(arriba, *filas, abajo).arrange(DOWN, buff=paso - 0.45)
    g.move_to([centro[0], centro[1], 0])
    return g


def columna_incognitas(centro=(0.0, 0.0), escala: float = 0.8, paso: float = 0.78, js=(-2, -1, 0, 1, 2)) -> VGroup:
    """Columna de coeficientes h[j] (las incógnitas), con puntos suspensivos arriba y abajo."""
    filas = VGroup(*[MathTex(f"h[{j}]", color=AMBAR).scale(escala) for j in js])
    arriba = MathTex(r"\vdots", color=INK).scale(escala)
    abajo = MathTex(r"\vdots", color=INK).scale(escala)
    g = VGroup(arriba, *filas, abajo).arrange(DOWN, buff=paso - 0.45)
    g.move_to([centro[0], centro[1], 0])
    return g


def registro_e3(n: int = 80, semilla: int = 11):
    """(y, v, x) del sensor: temperatura (varianza 4, factor 0,6), ruido blanco (varianza 1) y lo medido."""
    y = 2.0 * serie(semilla, n, 0.6)
    v = np.random.default_rng(semilla + 100).normal(0, 1.0, n)
    return y, v, y + v


def rebanadas_omega(L: Lienzo, n: int = 7, alto: float = 1.0, color=INK) -> VGroup:
    """`n` rebanadas verticales del eje de frecuencias (rectángulos contiguos)."""
    paso = L.ancho / n
    return VGroup(*[Rectangle(width=paso, height=alto, color=color, stroke_width=2).set_fill(color, 0.06)
                    .move_to([L.cx - L.ancho / 2 + paso * (i + 0.5), L.cy, 0]) for i in range(n)])


# ============================================================ capítulo 12, episodio 7: de Wiener a Kalman

class ParabolaJ(VGroup):
    """La parábola del error del E1: J(h) = 4 − 8h + 5h², con el vértice en h = 0,8 (J = 0,8).

    Atributos: `.eje` (el eje h, a la altura J = 0), `.curva`, `.vertice` (punto en el mínimo).
    `p(h)` da el punto de la parábola sobre la pantalla; `punto(h, color)` un punto ahí;
    `pendiente(h, largo, color)` la tangente en h."""

    H0, H1, JMAX = -0.2, 1.8, 6.0

    def __init__(self, centro=(0.0, 0.0), ancho: float = 5.0, alto: float = 3.0, color=ESTIMACION):
        super().__init__()
        self.cx, self.cy, self.ancho, self.alto = centro[0], centro[1], ancho, alto
        hs = np.linspace(self.H0, self.H1, 120)
        self.eje = Line(self.p(self.H0, 0), self.p(self.H1, 0), color=INK, stroke_width=2)
        self.curva = traza(*zip(*[self.p(h)[:2] for h in hs]), color=color, ancho=4.0)
        self.vertice = Dot(self.p(0.8), radius=0.09, color=VERDE)
        self.add(self.eje, self.curva, self.vertice)

    @staticmethod
    def J(h):
        return 4 - 8 * np.asarray(h) + 5 * np.asarray(h) ** 2

    def p(self, h, j=None) -> np.ndarray:
        j = self.J(h) if j is None else j
        x = self.cx - self.ancho / 2 + (h - self.H0) / (self.H1 - self.H0) * self.ancho
        y = self.cy - self.alto / 2 + float(j) / self.JMAX * self.alto
        return np.array([float(x), float(y), 0.0])

    def punto(self, h, color=AZUL, radio: float = 0.13) -> Dot:
        return Dot(self.p(h), radius=radio, color=color)

    def pendiente(self, h, largo: float = 1.6, color=ROJO) -> Line:
        d = -8 + 10 * h
        v = np.array([(self.ancho / (self.H1 - self.H0)), d * self.alto / self.JMAX, 0.0])
        v = v / np.linalg.norm(v) * largo / 2
        c = self.p(h)
        return Line(c - v, c + v, color=color, stroke_width=4)


def auriculares(color=TXT) -> VGroup:
    """Unos auriculares de diadema. `.arco`, `.copas`."""
    arco = Arc(radius=0.6, start_angle=0, angle=PI, color=color, stroke_width=6)
    c1 = RoundedRectangle(corner_radius=0.08, width=0.26, height=0.5, color=color, stroke_width=3).set_fill(color, 0.5)
    c2 = c1.copy()
    c1.move_to(arco.get_start() + DOWN * 0.1)
    c2.move_to(arco.get_end() + DOWN * 0.1)
    g = VGroup(arco, c1, c2)
    g.arco, g.copas = arco, VGroup(c1, c2)
    return g


def brujula(color=TXT) -> VGroup:
    """Brújula con la aguja ámbar hacia arriba. `.aro`, `.aguja`."""
    aro = Circle(radius=0.55, color=color, stroke_width=4).set_fill(FONDO, 1)
    aguja = Polygon([0, 0.42, 0], [0.12, 0, 0], [-0.12, 0, 0], color=ESTIMACION, stroke_width=2).set_fill(ESTIMACION, 0.9)
    g = VGroup(aro, aguja)
    g.aro, g.aguja = aro, aguja
    return g


COL_X = [-2.4, -0.6, 1.2, 3.0]      # columnas m = −1, 0, 1, 2 de la tabla de mediciones blancas


def tabla_blanca(ys=(2.4, 1.0, -0.4)) -> VGroup:
    """Tabla del ejemplo blanco (σ² = 2): filas m, C_yx y h; columnas m = −1…2. No agrega nada a la escena:
    cada pieza se anima por separado. `.ms`, `.cs`, `.hs` (listas de Text), `.rots` (rótulos de fila),
    `col(i)` (la columna i como grupo)."""
    ms = [Text(t, color=INK).scale(0.6).move_to([x, ys[0], 0]) for t, x in zip(["−1", "0", "1", "2"], COL_X)]
    cs = [Text(t, color=SENAL, weight=BOLD).scale(0.6).move_to([x, ys[1], 0])
          for t, x in zip(["1", "2", "1", "0,5"], COL_X)]
    hs = [Text(t, color=ESTIMACION, weight=BOLD).scale(0.6).move_to([x, ys[2], 0])
          for t, x in zip(["0,5", "1", "0,5", "0,25"], COL_X)]
    rots = [MathTex("m", color=INK).scale(0.8).move_to([-4.6, ys[0], 0]),
            MathTex("C_{yx}", color=SENAL).scale(0.8).move_to([-4.6, ys[1], 0]),
            MathTex("h", color=ESTIMACION).scale(0.8).move_to([-4.6, ys[2], 0])]
    g = VGroup(*ms, *cs, *hs, *rots)
    g.ms, g.cs, g.hs, g.rots = ms, cs, hs, rots
    g.col = lambda i: VGroup(ms[i], cs[i], hs[i])
    return g


def recuadro_mini(centro=(5.9, 3.3), lado: float = 0.55, buff: float = 0.12) -> VGroup:
    """Los tres pasos de la fórmula causal como tres casillas pequeñas numeradas (blanquear = cian,
    parte causal = ámbar, deshacer = verde). `.casillas` (lista), `.c1`, `.c2`, `.c3`."""
    colores = [CIAN, AMBAR, VERDE]
    cas = []
    for i, c in enumerate(colores):
        r = RoundedRectangle(corner_radius=0.08, width=lado, height=lado, color=c, fill_color=c,
                             fill_opacity=0.18, stroke_width=3)
        n = Text(str(i + 1), color=c, weight=BOLD).scale(0.4).move_to(r)
        cas.append(VGroup(r, n))
    g = VGroup(*cas).arrange(RIGHT, buff=buff).move_to([centro[0], centro[1], 0])
    g.casillas = cas
    g.c1, g.c2, g.c3 = cas
    return g


# ============================================================ capítulo 13, episodio 1: más datos no bastan

class RectaR(VGroup):
    """Recta de una medición `r`, con marcas en los valores que se pidan.

        R = RectaR(centro=(0, -1), ancho=8, x_rango=(-1.5, 1.5))
        R.p(0.5)                      # punto de la recta
        R.marca(1, "1")               # raya + rótulo debajo
    Atributos: `.base`, `.rot` (la letra r en la punta).
    """

    def __init__(self, centro=(0.0, 0.0), ancho: float = 8.0, x_rango=(-1.5, 1.5), rotulo: str = "r", color=INK):
        super().__init__()
        self.cx, self.cy, self.ancho = centro[0], centro[1], ancho
        self.x0, self.x1 = x_rango
        self.base = Arrow(self.p(self.x0), self.p(self.x1), buff=0, color=color, stroke_width=3,
                          tip_length=0.2, max_tip_length_to_length_ratio=0.1)
        self.rot = MathTex(rotulo, color=color).scale(0.7).next_to(self.p(self.x1), DR, buff=0.08)
        self.add(self.base, self.rot)

    def p(self, x: float) -> np.ndarray:
        return np.array([self.cx - self.ancho / 2 + (x - self.x0) / (self.x1 - self.x0) * self.ancho, self.cy, 0.0])

    def marca(self, x: float, texto: str, color=INK, escala: float = 0.5) -> VGroup:
        p = self.p(x)
        raya = Line(p + UP * 0.1, p + DOWN * 0.1, color=color, stroke_width=3)
        rot = MathTex(texto, color=color).scale(escala).next_to(raya, DOWN, buff=0.08)
        return VGroup(raya, rot)


def rect_dens(R: RectaR, a: float, b: float, h: float, esc: float, color=SENAL, opacidad: float = 0.3) -> Rectangle:
    """Densidad uniforme de altura `h` (en unidades de `esc` cm de pantalla) entre `a` y `b` sobre la recta."""
    ancho = abs(R.p(b)[0] - R.p(a)[0])
    r = Rectangle(width=ancho, height=max(h * esc, 0.001), color=color, fill_color=color,
                  fill_opacity=opacidad, stroke_width=3)
    r.move_to(R.p((a + b) / 2) + UP * h * esc / 2)
    return r


def tri_dens(R: RectaR, a: float, b: float, h: float, esc: float, color=SENAL, opacidad: float = 0.3) -> Polygon:
    """Densidad triangular de altura `h` entre `a` y `b` sobre la recta."""
    m = (a + b) / 2
    return Polygon(R.p(a), R.p(m) + UP * h * esc, R.p(b), color=color, fill_color=color,
                   fill_opacity=opacidad, stroke_width=3)


class Plano2(VGroup):
    """Plano de dos mediciones r₁, r₂ con el cuadrado grande (H₀) y el pequeño (H₁).

        P = Plano2(centro=(0, 0), u=1.3)       # `u` = largo en pantalla de una unidad
        P.p(0.3, -0.5)                         # coordenadas de pantalla
    Atributos: `.ejes`, `.rot1`, `.rot2`, `.grande` (lado 2, magenta), `.pequeno` (lado 1, azul).
    """

    def __init__(self, centro=(0.0, 0.0), u: float = 1.3, rango: float = 1.6):
        super().__init__()
        self.cx, self.cy, self.u = centro[0], centro[1], u
        ex = Arrow(self.p(-rango, 0), self.p(rango, 0), buff=0, color=INK, stroke_width=3,
                   tip_length=0.2, max_tip_length_to_length_ratio=0.1)
        ey = Arrow(self.p(0, -rango), self.p(0, rango), buff=0, color=INK, stroke_width=3,
                   tip_length=0.2, max_tip_length_to_length_ratio=0.1)
        self.ejes = VGroup(ex, ey)
        self.rot1 = MathTex("r_1", color=INK).scale(0.65).next_to(self.p(rango, 0), DR, buff=0.05)
        self.rot2 = MathTex("r_2", color=INK).scale(0.65).next_to(self.p(0, rango), UR, buff=0.05)
        self.grande = Square(side_length=2 * u, color=RUIDO, fill_color=RUIDO, fill_opacity=0.18,
                             stroke_width=3).move_to(self.p(0, 0))
        self.pequeno = Square(side_length=u, color=SENAL, fill_color=SENAL, fill_opacity=0.4,
                              stroke_width=3).move_to(self.p(0, 0))
        self.add(self.ejes, self.rot1, self.rot2, self.grande, self.pequeno)

    def p(self, x: float, y: float) -> np.ndarray:
        return np.array([self.cx + x * self.u, self.cy + y * self.u, 0.0])


def barras_senal(valores, centro=(0.0, 0.0), ancho: float = 0.55, unidad: float = 0.5, hueco: float = 0.2,
                 color=SENAL, opacidad: float = 0.55) -> VGroup:
    """Una señal de muestras como barras que suben desde una base (`.barras`, `.base`)."""
    barras = []
    n = len(valores)
    paso = ancho + hueco
    for i, v in enumerate(valores):
        x = centro[0] + (i - (n - 1) / 2) * paso
        b = Rectangle(width=ancho, height=max(abs(v) * unidad, 0.001), color=color, fill_color=color,
                      fill_opacity=opacidad, stroke_width=2.5)
        b.move_to([x, centro[1] + np.sign(v if v else 1) * abs(v) * unidad / 2, 0])
        barras.append(b)
    base = Line([centro[0] - n * paso / 2 - 0.1, centro[1], 0], [centro[0] + n * paso / 2 + 0.1, centro[1], 0],
                color=INK, stroke_width=2)
    g = VGroup(base, *barras)
    g.base, g.barras = base, barras
    return g


def casillas(n: int, rojas=(), centro=(0.0, 0.0), lado: float = 0.5, color=INK, color_rojo=ERROR,
             hueco: float = 0.1) -> VGroup:
    """Fila de `n` casillas; las de índice en `rojas` van rellenas de rojo (`.cas`)."""
    cas = []
    for i in range(n):
        c = color_rojo if i in rojas else color
        cas.append(Square(side_length=lado, color=c, fill_color=c, fill_opacity=0.6 if i in rojas else 0.12,
                          stroke_width=2.5))
    g = VGroup(*cas).arrange(RIGHT, buff=hueco).move_to([centro[0], centro[1], 0])
    g.cas = cas
    return g


def barra_v(x: float, base_y: float, alto: float, ancho: float = 0.9, color=ERROR, opacidad: float = 0.4) -> Rectangle:
    """Barra vertical que sube desde `base_y`."""
    r = Rectangle(width=ancho, height=max(alto, 0.001), color=color, fill_color=color,
                  fill_opacity=opacidad, stroke_width=3)
    return r.move_to([x, base_y + alto / 2, 0])


class TablaDecision(VGroup):
    """Tabla de 2 × 2: filas = realidad (H₀, H₁), columnas = decisión (H₀, H₁).

        T = TablaDecision(centro=(-1, -0.3), lado=1.8)
        T.c(i, j)       # centro de la casilla (fila i, columna j)
    Atributos: `.cel` (dict (i, j) → Rectangle), `.enc` (rótulos de encabezado), `.titulos`.
    """

    def __init__(self, centro=(0.0, 0.0), lado: float = 1.8):
        super().__init__()
        self.cx, self.cy, self.lado = centro[0], centro[1], lado
        self.cel = {}
        for i in range(2):
            for j in range(2):
                r = Rectangle(width=lado, height=lado, color=INK, stroke_width=2.5, fill_color=INK,
                              fill_opacity=0.08).move_to(self.c(i, j))
                self.cel[(i, j)] = r
        self.enc = VGroup(
            MathTex("H_0", color=RUIDO).scale(1.0).move_to(self.c(0, 0) + UP * (lado / 2 + 0.4)),
            MathTex("H_1", color=SENAL).scale(1.0).move_to(self.c(0, 1) + UP * (lado / 2 + 0.4)),
            MathTex("H_0", color=RUIDO).scale(1.0).move_to(self.c(0, 0) + LEFT * (lado / 2 + 0.45)),
            MathTex("H_1", color=SENAL).scale(1.0).move_to(self.c(1, 0) + LEFT * (lado / 2 + 0.45)),
        )
        self.titulos = VGroup(
            Text("decisión", color=INK).scale(0.6).move_to(self.c(0, 0) / 2 + self.c(0, 1) / 2 + UP * (lado / 2 + 0.95)),
            Text("realidad", color=INK).scale(0.6).rotate(PI / 2).move_to(
                self.c(0, 0) / 2 + self.c(1, 0) / 2 + LEFT * (lado / 2 + 1.0)),
        )
        self.add(*self.cel.values(), self.enc, self.titulos)

    def c(self, i: int, j: int) -> np.ndarray:
        return np.array([self.cx + (j - 0.5) * self.lado, self.cy + (0.5 - i) * self.lado, 0.0])


# ============================================================ capítulo 13, episodio 6: ¿cuándo llegó el eco?

PULSO13 = (2, 2, 1)                                    # el pulso del capítulo
FILTRO13 = (1, 2, 2)                                   # su filtro adaptado
BARKER13 = (1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1)  # secuencia de Barker de trece


def autocorr13(a, b=None) -> np.ndarray:
    """Correlación cruzada completa (largo 2n − 1) de `a` con `b` (por defecto, con ella misma)."""
    a = np.asarray(a, dtype=float)
    b = a if b is None else np.asarray(b, dtype=float)
    return np.correlate(a, b, mode="full")


def chirp13(n: int = 64, f0: float = 0.03, f1: float = 0.45) -> np.ndarray:
    """Sinusoide cuya frecuencia sube de `f0` a `f1` ciclos por muestra, en `n` muestras."""
    t = np.arange(n)
    return np.cos(2 * np.pi * (f0 * t + (f1 - f0) * t ** 2 / (2 * n)))


def radar13(color=TXT) -> VGroup:
    """Antena de radar: plato, mástil y base. `.plato`, `.ondas` (tres arcos hacia la derecha)."""
    plato = Arc(radius=0.7, start_angle=-PI / 2.4, angle=2 * PI / 2.4, color=color, stroke_width=5)
    plato.rotate(-PI / 16).shift(LEFT * 0.1)
    foco = Dot(plato.get_center() + RIGHT * 0.1, radius=0.06, color=color)
    mastil = Line([0, -0.1, 0], [0, -0.75, 0], color=color, stroke_width=5)
    base = RoundedRectangle(width=0.8, height=0.14, corner_radius=0.05, color=color,
                            stroke_width=3).set_fill(color, 0.3).move_to([0, -0.82, 0])
    ondas = VGroup(*[Arc(radius=0.35 * i, start_angle=-PI / 5, angle=2 * PI / 5, color=color, stroke_width=3,
                         stroke_opacity=0.7).shift(RIGHT * 0.45) for i in range(1, 4)])
    g = VGroup(mastil, base, plato, foco, ondas)
    g.plato, g.ondas = plato, ondas
    return g


def celdas13(n: int, ancho: float = 10.0, centro=(0.0, 0.0), alto: float = 0.6, color=INK,
             opacidad: float = 0.12) -> VGroup:
    """Tira de `n` celdas contiguas de ancho total `ancho` (la tira de posiciones de distancia)."""
    w = ancho / n
    g = VGroup(*[Rectangle(width=w, height=alto, stroke_width=1.2 if n > 40 else 2, color=color)
                 .set_fill(color, opacidad) for _ in range(n)])
    g.arrange(RIGHT, buff=0).move_to([centro[0], centro[1], 0])
    return g


def grilla13(n: int = 100, filas: int = 10, lado: float = 0.3, centro=(0.0, 0.0), color=INK) -> VGroup:
    """Grilla de `n` casillas (para «56 de cada 100»); se llena por filas, de izquierda a derecha."""
    g = VGroup(*[Square(lado, stroke_width=1.5, color=color).set_fill(color, 0.1) for _ in range(n)])
    g.arrange_in_grid(rows=filas, cols=n // filas, buff=0.04).move_to([centro[0], centro[1], 0])
    return g


def autocorr_tallos13(vals, centro=(0.0, 0.0), paso: float = 0.4, unidad: float = 0.15, color=AMBAR) -> Tallos:
    """Autocorrelación (o salida del filtro) como palitos."""
    return Tallos(vals, centro=centro, paso=paso, unidad=unidad, color=color)


def curva_barras13(L: Lienzo, vals, color=SENAL, ancho: float = 3.0) -> VMobject:
    """Línea poligonal que une las muestras `vals` (la autocorrelación vista como curva)."""
    n = len(vals)
    return L.curva(np.arange(n), np.asarray(vals, dtype=float), color, ancho)


def avion_lejano13(escala: float = 0.5, color=AZUL) -> VGroup:
    """El avión de los ecos (el ícono del curso, pequeño)."""
    return avion(color).scale(escala)


# ============================================================ capítulo 13, episodio 4: el filtro adaptado

S13 = [2, 2, 1]                  # el pulso del capítulo
H13 = [1, 2, 2]                  # el filtro adaptado: el pulso al revés
R13 = [3, 1, 2]                  # lo recibido (señal + ruido) del episodio 2
SAL13 = [3, 7, 10, 6, 4]         # r pasando por h
AUT13 = [2, 6, 9, 6, 2]          # s pasando por h: la autocorrelación (pico 9 = energía)


def valores_sobre13(t: Tallos, color=TXT, escala: float = 0.45, dy: float = 0.3) -> VGroup:
    """Los números sobre las cimas de un `Tallos` (debajo si son negativos): uno por palito."""
    g = VGroup()
    for i, v in enumerate(t.valores):
        txt = Text(str(v).replace("-", "−"), color=color).scale(escala)
        txt.move_to(t.pos(i) + (UP if v >= 0 else DOWN) * dy)
        g.add(txt)
    return g


class CasillasSalida13(VGroup):
    """Fila de casillas para la salida y[n]: `.cas`, `.ks`; `c(i)` da el centro de la casilla `i`;
    `poner(i, txt, color)` devuelve un texto centrado en ella."""

    def __init__(self, n: int = 5, centro=(0.0, 0.0), lado: float = 0.85, color=ESTIMACION):
        super().__init__()
        self.cx, self.cy, self.lado, self.n = centro[0], centro[1], lado, n
        self.cas, self.ks = [], VGroup()
        for i in range(n):
            r = Square(side_length=lado, color=color, stroke_width=2.5).set_fill(color, 0.08).move_to(self.c(i))
            self.cas.append(r)
            self.ks.add(Text(str(i), color=INK).scale(0.4).move_to(self.c(i) + DOWN * (lado / 2 + 0.25)))
        self.add(*self.cas, self.ks)

    def c(self, i: int) -> np.ndarray:
        return np.array([self.cx + (i - (self.n - 1) / 2) * (self.lado + 0.08), self.cy, 0.0])

    def poner(self, i: int, txt: str, color=TXT, escala: float = 0.7) -> Text:
        return Text(txt, color=color, weight=BOLD).scale(escala).move_to(self.c(i))


def alarma13(color=ROJO) -> VGroup:
    """Una campana de alarma de ~1 de alto. `.rayos` son las rayitas de los lados."""
    cupula = Arc(radius=0.4, start_angle=0, angle=PI, color=color, stroke_width=5).shift(UP * 0.0)
    cuerpo = Polygon([-0.4, 0, 0], [0.4, 0, 0], [0.55, -0.3, 0], [-0.55, -0.3, 0],
                     color=color, stroke_width=5).set_fill(color, 0.3)
    badajo = Dot([0, -0.42, 0], radius=0.08, color=color)
    rayos = VGroup(*[Line([s * 0.62, 0.32, 0], [s * 0.82, 0.46, 0], color=color, stroke_width=4)
                     for s in (-1, 1)],
                   *[Line([s * 0.7, 0.1, 0], [s * 0.95, 0.1, 0], color=color, stroke_width=4) for s in (-1, 1)])
    g = VGroup(cupula, cuerpo, badajo, rayos)
    g.rayos = rayos
    return g


def interrogante13(color=AMBAR, escala: float = 1.2) -> Text:
    return Text("?", color=color, weight=BOLD).scale(escala)


def cos13(t, amp: float, frec: float, fase_deg: float):
    """Una sinusoide para dibujar: amp·cos(2π·frec·t + fase)."""
    return amp * np.cos(2 * np.pi * frec * np.asarray(t) + np.deg2rad(fase_deg))


# ============================================================ capítulo 13, episodio 7: ¿cuál de ellas mandaron?

AZUL_C7 = "#8ab4ff"             # la «otra» señal (s₀): un azul más claro que SENAL


def modem7(color=INK) -> VGroup:
    """Módem plano con dos antenas y tres luces (~1,5 de ancho). `.luces`."""
    cuerpo = RoundedRectangle(corner_radius=0.1, width=1.5, height=0.6, color=color,
                              stroke_width=4).set_fill(color, 0.2)
    luces = VGroup(*[Dot([-0.45 + 0.3 * i, 0, 0], radius=0.06, color=c) for i, c in enumerate((VERDE, AMBAR, VERDE))])
    an1 = Line([0.5, 0.3, 0], [0.7, 0.95, 0], color=color, stroke_width=4)
    an2 = Line([-0.5, 0.3, 0], [-0.7, 0.95, 0], color=color, stroke_width=4)
    g = VGroup(an1, an2, cuerpo, luces)
    g.luces = luces
    return g


def campana7(cx: float, y0: float, s: float, alto: float, color=SENAL, k: float = 3.4, ancho: float = 4.0) -> VMobject:
    """Campana de Gauss dibujada: centro `cx`, base `y0`, desvío `s` (en unidades de pantalla), `alto` en el centro."""
    xs = np.linspace(cx - k * s, cx + k * s, 120)
    ys = y0 + alto * np.exp(-0.5 * ((xs - cx) / s) ** 2)
    return traza(xs, ys, color, ancho)


def cola7(cx: float, y0: float, s: float, alto: float, x_ini: float, x_fin: float,
          color=ERROR, opacidad: float = 0.45) -> VMobject:
    """Área bajo la campana entre dos posiciones de pantalla (una cola para sombrear)."""
    xs = np.linspace(x_ini, x_fin, 60)
    ys = y0 + alto * np.exp(-0.5 * ((xs - cx) / s) ** 2)
    pts = [np.array([x, y0, 0.0]) for x in (xs[0],)] + [np.array([x, y, 0.0]) for x, y in zip(xs, ys)] \
        + [np.array([xs[-1], y0, 0.0])]
    return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)


def planito7(centro=(0.0, 0.0), ancho: float = 4.6, alto: float = 3.4, color=INK) -> VGroup:
    """Dos ejes sin números (el plano donde viven las señales como puntos). `.o`, `.p(x, y)`."""
    c = np.array([centro[0], centro[1], 0.0])
    h = Line(c + LEFT * ancho / 2, c + RIGHT * ancho / 2, color=color, stroke_width=2)
    v = Line(c + DOWN * alto / 2, c + UP * alto / 2, color=color, stroke_width=2)
    g = VGroup(h, v)
    g.o = c
    g.p = lambda x, y: c + np.array([x, y, 0.0])
    return g


def pulso7(valores, centro=(0.0, 0.0), color=SENAL, paso: float = 0.5, unidad: float = 0.34) -> Tallos:
    """Un pulso corto como palitos (el mismo `Tallos`, con la escala de este episodio)."""
    return Tallos(valores, centro=centro, paso=paso, unidad=unidad, color=color)


# ============================================================ capítulo 13, episodio 2: el pulso, el ruido y el estadístico g

class Barras(VGroup):
    """Una señal de muestras como barras (el pulso s, el ruido w, lo recibido r).

        b = Barras((2, 2, 1), centro=(0, 0), paso=1.5, unidad=0.5, color=SENAL, indices=True, nums=True)
    Atributos: `.base`, `.barras` (lista de Rectangle), `.nums`, `.ks`. `x(i)` es la posición
    horizontal de la muestra `i`, `top(i)` la punta de su barra. Cada pieza se agrega al grupo:
    para animarlas por separado usar `b.base`, `b.barras[i]`, `b.nums[i]`.
    """

    def __init__(self, valores, centro=(0.0, 0.0), paso: float = 1.3, unidad: float = 0.5, color=SENAL,
                 ancho: float = 0.7, indices: bool = False, nums: bool = False, k0: int = 0):
        super().__init__()
        self.valores = list(valores)
        self.cx, self.cy, self.paso, self.unidad, self.color = centro[0], centro[1], paso, unidad, color
        n = len(self.valores)
        self.base = Line([self.x(-0.6), self.cy, 0], [self.x(n - 0.4), self.cy, 0], color=INK, stroke_width=1.8)
        self.barras, self.nums, self.ks = [], VGroup(), VGroup()
        for i, v in enumerate(self.valores):
            h = max(abs(v) * unidad, 0.001)
            r = Rectangle(width=ancho, height=h, stroke_width=2, color=color).set_fill(color, 0.55)
            r.move_to([self.x(i), self.cy + v * unidad / 2, 0])
            self.barras.append(r)
            if nums:
                t = Text(num(v), color=color).scale(0.45)
                t.move_to([self.x(i), self.cy + v * unidad + (0.28 if v >= 0 else -0.28), 0])
                self.nums.add(t)
            if indices:
                self.ks.add(Text(str(k0 + i), color=INK).scale(0.4).move_to([self.x(i), self.cy - 0.28, 0]))
        self.add(self.base, *self.barras, self.nums, self.ks)

    def x(self, i: float) -> float:
        n = len(self.valores)
        return self.cx + (i - (n - 1) / 2) * self.paso

    def top(self, i: int) -> np.ndarray:
        return np.array([self.x(i), self.cy + self.valores[i] * self.unidad, 0.0])


def campana_curva(L: Lienzo, mu: float = 0.0, sigma: float = 1.0, color=RUIDO, ancho: float = 3.5,
                  x0=None, x1=None, n: int = 120, pico: float = 1.0) -> VMobject:
    """Campana de Gauss (de altura `pico`) dibujada sobre un `Lienzo` (eje t = el valor)."""
    x0 = L.t0 if x0 is None else x0
    x1 = L.t1 if x1 is None else x1
    t = np.linspace(x0, x1, n)
    return L.curva(t, pico * np.exp(-0.5 * ((t - mu) / sigma) ** 2), color, ancho)


def gx(g: float) -> float:
    """Posición horizontal de la recta de `g` (una unidad de g = una unidad de pantalla; g = 5 en el centro)."""
    return g - 5.0 + 0.5


def recta_g(y: float = -0.8, g0: float = -1.0, g1: float = 11.0, color=INK) -> Line:
    return Line([gx(g0), y, 0], [gx(g1), y, 0], color=color, stroke_width=2.5)


def marca_g(g: float, y: float = -0.8, color=INK, texto=None, alto: float = 0.16, escala: float = 0.5) -> VGroup:
    """Una marca sobre la recta de g, con su número debajo."""
    v = Line([gx(g), y - alto, 0], [gx(g), y + alto, 0], color=color, stroke_width=4)
    t = Text(texto if texto is not None else num(g), color=color).scale(escala).next_to(v, DOWN, buff=0.12)
    return VGroup(v, t)


def umbral_g(gamma: float, y: float = -0.8, color=AMBAR, largo: float = 0.9) -> VGroup:
    """Cuña ámbar con una línea que marca el umbral γ sobre la recta de g."""
    v = Line([gx(gamma), y - 0.28, 0], [gx(gamma), y + largo, 0], color=color, stroke_width=4)
    p = Triangle(color=color, stroke_width=2).set_fill(color, 1).scale(0.13).rotate(PI).move_to([gx(gamma), y + 0.22, 0])
    return VGroup(v, p)


def nube_de_puntos(centro=(0.0, 0.0), radio: float = 1.2, n: int = 90, semilla: int = 5, color=RUIDO) -> VGroup:
    """Nube circular de puntos (el ruido gaussiano, que no distingue direcciones)."""
    rng = np.random.default_rng(semilla)
    ang = rng.uniform(0, 2 * np.pi, n)
    rad = radio * np.sqrt(rng.uniform(0, 1, n)) * 0.98
    return VGroup(*[Dot([centro[0] + r * np.cos(a), centro[1] + r * np.sin(a), 0], radius=0.045, color=color)
                    for a, r in zip(ang, rad)])


# ============================================================ capítulo 13, episodio 5: ruido con memoria

class PlanoV(VGroup):
    """Plano de dos muestras de ruido (v₀ horizontal, v₁ vertical) para las nubes correlacionadas.

        P = PlanoV(centro=(-3.5, 0), lado=2.3, esc=1.0)
        e = P.elipse(0.6)            # contorno de la nube con correlación 0,6
        d = P.puntos(0.6, n=30)      # puntos de ejemplo
    `esc` = unidades de pantalla por desvío. Atributos: `.ejes`, `.rot0`, `.rot1`; `p(a, b)` da el punto.
    """

    def __init__(self, centro=(0.0, 0.0), lado: float = 2.3, esc: float = 1.0, rot0: str = r"v_0",
                 rot1: str = r"v_1", color=INK):
        super().__init__()
        self.c = np.array([centro[0], centro[1], 0.0])
        self.lado, self.esc = lado, esc
        kw = dict(color=color, stroke_width=2.5, buff=0, max_tip_length_to_length_ratio=0.08)
        h = Arrow(self.c + LEFT * lado, self.c + RIGHT * lado, **kw)
        v = Arrow(self.c + DOWN * lado, self.c + UP * lado, **kw)
        self.ejes = VGroup(h, v)
        self.rot0 = MathTex(rot0, color=RUIDO).scale(0.7).next_to(h.get_end(), RIGHT, buff=0.2)
        self.rot1 = MathTex(rot1, color=RUIDO).scale(0.7).next_to(v.get_end(), UP, buff=0.2)
        self.add(self.ejes, self.rot0, self.rot1)

    def p(self, a: float, b: float) -> np.ndarray:
        return self.c + np.array([a * self.esc, b * self.esc, 0.0])

    def elipse(self, rho: float, color=RUIDO, k: float = 1.5, sx: float = 1.0, sy: float = 1.0) -> Ellipse:
        """Contorno a `k` desvíos de la nube con correlación `rho` (eje largo en la diagonal)."""
        if rho == 0:
            e = Ellipse(width=2 * k * sx * self.esc, height=2 * k * sy * self.esc, color=color, stroke_width=4)
        else:
            e = Ellipse(width=2 * k * np.sqrt(1 + rho) * self.esc, height=2 * k * np.sqrt(1 - rho) * self.esc,
                        color=color, stroke_width=4).rotate(PI / 4)
        return e.set_fill(color, 0.12).move_to(self.c)

    def puntos(self, rho: float, n: int = 30, semilla: int = 5, color=RUIDO, radio: float = 0.05) -> VGroup:
        rng = np.random.default_rng(semilla)
        z1, z2 = rng.normal(0, 1, n), rng.normal(0, 1, n)
        a = z1
        b = rho * z1 + np.sqrt(1 - rho * rho) * z2
        pts = [Dot(self.p(x, y), radius=radio, color=color) for x, y in zip(a, b)
               if abs(x) < 2.2 and abs(y) < 2.2]
        return VGroup(*pts)


def ruido_ar(n: int, a: float, semilla: int = 3) -> np.ndarray:
    """Ruido con memoria `a` (varianza 1); `a` puede ser negativa."""
    return serie(semilla, n, a)


def d_ruido(w, a: float = 0.6):
    """Densidad espectral del ruido con memoria `a`, normalizada a 1 en su máximo."""
    w = np.asarray(w, dtype=float)
    d = 1.0 / (1 + a * a - 2 * a * np.cos(w))
    return d * (1 + a * a - 2 * abs(a))


def s2_lento(w):
    """|S|² del pulso (1, 1), normalizado a 1: vive en las bajas frecuencias."""
    return (1 + np.cos(np.asarray(w, dtype=float))) / 2


def s2_rapido(w):
    """|S|² del pulso (1, −1), normalizado a 1: vive en las altas frecuencias."""
    return (1 - np.cos(np.asarray(w, dtype=float))) / 2


def lienzo_w(ancho: float = 9.0, alto: float = 2.8, base_y: float = -1.4, cx: float = 0.0) -> Lienzo:
    """Lienzo de frecuencias Ω de 0 a π; el cero está en `base_y` y el 1 `alto` más arriba."""
    return Lienzo(ancho=ancho, alto=2 * alto, t_rango=(0, np.pi), v_max=1.0, centro=(cx, base_y))


def eje_w(L: Lienzo) -> VGroup:
    """Eje de frecuencias con 0 y π. `.base`, `.rotulos`."""
    base = L.base(INK, 2.0)
    r0 = MathTex("0", color=INK).scale(0.55).next_to(L.p(0, 0), DOWN, buff=0.15)
    r1 = MathTex(r"\pi", color=INK).scale(0.55).next_to(L.p(np.pi, 0), DOWN, buff=0.15)
    g = VGroup(base, r0, r1)
    g.base, g.rotulos = base, VGroup(r0, r1)
    return g


def nube_lluvia(color=INK) -> VGroup:
    """Nube con gotas. `.gotas`."""
    cuerpo = VGroup(Circle(0.28), Circle(0.38).shift(RIGHT * 0.4 + UP * 0.1), Circle(0.28).shift(RIGHT * 0.8))
    cuerpo.set_stroke(color, 4).set_fill(color, 0.25)
    gotas = VGroup(*[Line([x, -0.45, 0], [x - 0.1, -0.75, 0], color=CIAN, stroke_width=4)
                     for x in (0.0, 0.3, 0.6, 0.9)])
    g = VGroup(cuerpo, gotas)
    g.gotas = gotas
    return g


def aviso_triangulo(color=AMBAR) -> VGroup:
    """Triángulo de advertencia con «!»."""
    t = Triangle(color=color, stroke_width=6).set_fill(color, 0.15).scale(0.5)
    ex = Text("!", color=color, weight=BOLD).scale(0.55).move_to(t.get_center() + DOWN * 0.04)
    return VGroup(t, ex)


def datos_celdas(n: int = 48, i0: int = 20, i1: int = 36, sig_lluvia: float = 2.0, semilla: int = 8) -> np.ndarray:
    """Envolvente (valor absoluto) del ruido de un radar: más fuerte entre las celdas i0 e i1 (lluvia)."""
    rng = np.random.default_rng(semilla)
    s = np.ones(n)
    s[i0:i1] = sig_lluvia
    return np.abs(rng.normal(0, 1, n)) * s


def umbral_local(x: np.ndarray, k: float = 2.6, vecinas: int = 7) -> np.ndarray:
    """Umbral que se adapta: `k` veces la raíz de la potencia media de las celdas vecinas (sin la central)."""
    n = len(x)
    u = np.zeros(n)
    for i in range(n):
        idx = [j for j in range(max(0, i - vecinas), min(n, i + vecinas + 1)) if j != i]
        u[i] = k * np.sqrt(np.mean(x[idx] ** 2))
    return u


# ============================================================ capítulo 13, episodio 3: ¿cuánto nos equivocamos?

def lienzo_g3(centro=(0.0, -1.2), ancho: float = 11.0, alto: float = 3.6, g0: float = -8.0, g1: float = 17.0) -> Lienzo:
    """Lienzo de las dos campanas de g (la medición): el eje horizontal es el valor de g."""
    return Lienzo(ancho=ancho, alto=alto, t_rango=(g0, g1), v_max=1.2, centro=centro)


def dens3(L: Lienzo, mu: float, sigma: float, color=RUIDO, ancho: float = 4.0, sigma0: float = 3.0,
          k: float = 3.4) -> VMobject:
    """Campana de media `mu` y desvío `sigma`, con la altura de una densidad (el desvío `sigma0` mide 1)."""
    t = np.linspace(max(L.t0, mu - k * sigma), min(L.t1, mu + k * sigma), 140)
    v = (sigma0 / sigma) * np.exp(-0.5 * ((t - mu) / sigma) ** 2)
    return L.curva(t, v, color, ancho)


def cola3(L: Lienzo, mu: float, sigma: float, desde: float, hasta: float, color=ERROR, opacidad: float = 0.5,
          sigma0: float = 3.0) -> VMobject:
    """Área bajo la campana (`mu`, `sigma`) entre dos valores de g: una cola para sombrear."""
    t = np.linspace(max(desde, L.t0), min(hasta, L.t1), 70)
    v = (sigma0 / sigma) * np.exp(-0.5 * ((t - mu) / sigma) ** 2)
    pts = [L.p(t[0], 0.0)] + [L.p(a, b) for a, b in zip(t, v)] + [L.p(t[-1], 0.0)]
    return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)


def umbral3(L: Lienzo, g: float, color=ESTIMACION, alto: float = 2.0, rotulo: str = r"\gamma") -> VGroup:
    """Marca vertical del umbral γ sobre las campanas, con su letra arriba (`.linea`, `.rot`)."""
    linea = Line(L.p(g, 0.0) + DOWN * 0.15, L.p(g, 0.0) + UP * alto, color=color, stroke_width=4)
    rot = MathTex(rotulo, color=color).scale(0.8).next_to(linea, UP, buff=0.08)
    grp = VGroup(linea, rot)
    grp.linea, grp.rot = linea, rot
    return grp


def eje_g3(L: Lienzo, marcas=(0, 9), color=INK, escala: float = 0.55) -> VGroup:
    """Base de las campanas con números debajo en los valores de `marcas` (`.base`, `.nums`)."""
    base = L.base(color=color, ancho=2.4)
    nums = VGroup(*[Text(num(m), color=color).scale(escala).move_to(L.p(m, 0.0) + DOWN * 0.35) for m in marcas])
    g = VGroup(base, nums)
    g.base, g.nums = base, nums
    return g


def hoja3(ancho: float = 3.6, alto: float = 3.0, color=INK, renglones: int = 5) -> VGroup:
    """Una hoja de papel con renglones cortos (`.renglones`)."""
    hoja = RoundedRectangle(corner_radius=0.1, width=ancho, height=alto, color=TXT, stroke_width=3).set_fill(TXT, 0.07)
    rng = np.random.default_rng(3)
    ren = VGroup()
    for i in range(renglones):
        y = alto / 2 - 0.45 - i * 0.5
        largo = ancho * (0.45 + 0.35 * rng.random())
        ren.add(Line([-ancho / 2 + 0.35, y, 0], [-ancho / 2 + 0.35 + largo, y, 0], color=color, stroke_width=4))
    g = VGroup(hoja, ren)
    g.hoja, g.renglones = hoja, ren
    return g


def rejilla3(rojos: int, n: int = 100, filas: int = 10, lado: float = 0.28, centro=(0.0, 0.0)) -> VGroup:
    """Cien puntos en rejilla; los primeros `rojos` (por filas) van en rojo (`.pts`)."""
    pts = [Dot(radius=lado * 0.3, color=ERROR if i < rojos else INK) for i in range(n)]
    g = VGroup(*pts).arrange_in_grid(rows=filas, cols=n // filas, buff=lado * 0.45).move_to([centro[0], centro[1], 0])
    g.pts = pts
    return g


def casilla_h3(k: int, texto: str, centro=(0.0, 0.0), ancho: float = 3.8, alto: float = 0.85) -> VGroup:
    """Casilla de una hipótesis: «H₀ · solo ruido» (magenta) o «H₁ · señal + ruido» (azul). `.caja`."""
    col = RUIDO if k == 0 else SENAL
    r = RoundedRectangle(corner_radius=0.12, width=ancho, height=alto, color=col, stroke_width=3).set_fill(col, 0.12)
    h = MathTex(f"H_{k}", color=col).scale(0.9)
    t = Text(texto, color=TXT).scale(0.5)
    VGroup(h, t).arrange(RIGHT, buff=0.3).move_to(r.get_center())
    g = VGroup(r, h, t).move_to([centro[0], centro[1], 0])
    g.caja = r
    return g


def subrayado(m: Mobject, color=AMBAR, ancho: float = 5.0) -> Underline:
    """Subrayado de una pieza de fórmula (una línea: no cuenta como encimado en los controles)."""
    return Underline(m, color=color, buff=0.08, stroke_width=ancho)


def tachado(m: Mobject, color=ROJO) -> Line:
    """Línea diagonal roja que tacha una pieza (para cancelar términos)."""
    return Line(m.get_corner(DL) + DL * 0.05, m.get_corner(UR) + UR * 0.05, color=color, stroke_width=6)


def avion_arriba(color=AZUL) -> VGroup:
    """Avión visto desde arriba, apuntando a la derecha (de ~1 unidad de largo)."""
    def ala(s):
        return Polygon([0.25, 0.1 * s, 0], [-0.2, 0.1 * s, 0], [-0.75, 0.85 * s, 0], [-0.95, 0.85 * s, 0],
                       stroke_width=0).set_fill(color, 1)

    def cola(s):
        return Polygon([-0.75, 0.08 * s, 0], [-1.0, 0.08 * s, 0], [-1.1, 0.4 * s, 0], [-1.25, 0.4 * s, 0],
                       stroke_width=0).set_fill(color, 1)
    cuerpo = RoundedRectangle(width=2.0, height=0.26, corner_radius=0.13, stroke_width=0).set_fill(color, 1)
    cuerpo.move_to([-0.1, 0, 0])
    g = VGroup(ala(1), ala(-1), cola(1), cola(-1), cuerpo)
    g.scale(1.0 / g.width)
    return g


# ============================================================ capítulo 07, episodio 1: repaso y modelo probabilístico

class Cursor7(VGroup):
    """Cursor vertical con un punto que sigue una curva (t, v) de un `Lienzo`.

        c = Cursor7(L, t, v); self.play(FadeIn(c)); self.play(c.barrer(0.2, 1.6), run_time=1.2)
    Atributos: `.linea`, `.punto`. `mover(t)` lo coloca; `barrer(t0, t1)` devuelve la animación.
    """

    def __init__(self, L: Lienzo, t, v, color=AMBAR, t_ini: float | None = None):
        super().__init__()
        self.L, self.t, self.v = L, np.asarray(t, dtype=float), np.asarray(v, dtype=float)
        self.linea = L.vertical(self.t[0], color, 2.5)
        self.punto = Dot(radius=0.1, color=color)
        self.add(self.linea, self.punto)
        self.mover(self.t[0] if t_ini is None else t_ini)

    def mover(self, tt: float):
        x = float(self.L.x(tt))
        y = float(self.L.y(np.interp(tt, self.t, self.v)))
        self.linea.set_x(x)
        self.punto.move_to([x, y, 0])
        return self

    def barrer(self, t0: float, t1: float, **kw):
        return UpdateFromAlphaFunc(self, lambda m, a: m.mover(t0 + (t1 - t0) * a), **kw)


class CajaSistema7(VGroup):
    """Caja de un sistema con rótulo de texto y flechas de entrada y salida.
    `.caja`, `.rot` (Text), `.ent`, `.sal`; `nuevo_rotulo(txt)` devuelve un Text en su sitio."""

    def __init__(self, rotulo: str = "sistema", centro=(0.0, 0.0), ancho: float = 3.0, alto: float = 1.5,
                 color=AZUL, largo: float = 1.3):
        super().__init__()
        cx, cy = centro
        self.centro = np.array([cx, cy, 0.0])
        self.caja = RoundedRectangle(corner_radius=0.12, width=ancho, height=alto, color=color,
                                     fill_color=color, fill_opacity=0.12, stroke_width=2.5).move_to(self.centro)
        self.rot = self.nuevo_rotulo(rotulo)
        kw = dict(color=INK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.25)
        self.ent = Arrow([cx - ancho / 2 - largo, cy, 0], [cx - ancho / 2, cy, 0], **kw)
        self.sal = Arrow([cx + ancho / 2, cy, 0], [cx + ancho / 2 + largo, cy, 0], **kw)
        self.add(self.ent, self.caja, self.rot, self.sal)

    def nuevo_rotulo(self, txt: str, color=TXT) -> Text:
        return Text(txt, color=color).scale(0.55).move_to(self.centro)


class EspacioDado(VGroup):
    """El espacio muestral del dado: seis caras en dos filas, dentro de un rectángulo.

    Disposición (para que los dos eventos del episodio sean figuras limpias):
        2 4 6      «sale par» = fila de arriba;  «más de 4» = columna de la derecha (5 y 6)
        1 3 5
    Atributos: `.rect`, `.caras` (dict n → dado). `p(n)`, `fracciones()` (dict de «1/6»),
    `marco_par(color)`, `marco_mas4(color)`.
    """
    ORDEN = [[2, 4, 6], [1, 3, 5]]

    def __init__(self, centro=(0.0, 0.0), paso_x: float = 1.55, paso_y: float = 1.75, lado: float = 0.8):
        super().__init__()
        self.cx, self.cy, self.px, self.py = centro[0], centro[1], paso_x, paso_y
        self.caras = {}
        for r, fila in enumerate(self.ORDEN):
            for c, n in enumerate(fila):
                d = dado_n(n).scale(lado)
                d.move_to([self.cx + (c - 1) * paso_x, self.cy + (0.5 - r) * paso_y, 0])
                self.caras[n] = d
        self.rect = RoundedRectangle(corner_radius=0.2, width=3 * paso_x + 0.5, height=3.35, color=INK,
                                     stroke_width=3).move_to([self.cx, self.cy - 0.175, 0])
        self.add(self.rect, *self.caras.values())

    def p(self, n: int) -> np.ndarray:
        return self.caras[n].get_center()

    def fracciones(self, txt: str = "1/6", color=INK, escala: float = 0.45) -> dict:
        return {n: Text(txt, color=color).scale(escala).move_to(self.p(n) + DOWN * 0.62) for n in self.caras}

    def _marco(self, x0, x1, y0, y1, color, relleno=0.1):
        m = RoundedRectangle(corner_radius=0.14, width=x1 - x0, height=y1 - y0, color=color, stroke_width=4,
                             fill_color=color, fill_opacity=relleno)
        return m.move_to([(x0 + x1) / 2, (y0 + y1) / 2, 0])

    def marco_par(self, color=AMBAR, relleno=0.1):
        """Rodea la fila de arriba (2, 4, 6) con sus fracciones."""
        y_alta = self.cy + self.py / 2
        return self._marco(self.cx - self.px - 0.62, self.cx + self.px + 0.62, y_alta - 0.92, y_alta + 0.55,
                           color, relleno)

    def marco_mas4(self, color=CIAN, relleno=0.1):
        """Rodea la columna de la derecha (6 y 5) con sus fracciones."""
        y_alta = self.cy + self.py / 2
        y_baja = self.cy - self.py / 2
        return self._marco(self.cx + self.px - 0.62, self.cx + self.px + 0.62, y_baja - 0.95, y_alta + 0.55,
                           color, relleno)


class Mapa7(VGroup):
    """El mapa del curso: siete estaciones (capítulos 7 a 13) sobre una línea.
    `.circ[i]`, `.nums[i]`, `.rot[i]` (nombre bajo cada estación), `.linea`. `luz(i, color)` da las
    animaciones que encienden la estación `i` (0 = capítulo 7)."""
    NOMBRES = ["Modelos", "Estimación", "Hipótesis", "Procesos", "Espectro", "Filtrado", "Detección"]

    def __init__(self, centro=(0.0, 0.0), paso: float = 1.9):
        super().__init__()
        cx, cy = centro
        xs = [cx + (i - 3) * paso for i in range(7)]
        self.linea = Line([xs[0], cy, 0], [xs[-1], cy, 0], color=INK, stroke_width=3)
        self.circ, self.nums, self.rot = [], [], []
        for i, x in enumerate(xs):
            c = Circle(radius=0.36, color=INK, stroke_width=3).set_fill(FONDO, 1).move_to([x, cy, 0])
            n = Text(str(7 + i), color=INK, weight=BOLD).scale(0.55).move_to(c)
            r = Text(self.NOMBRES[i], color=INK).scale(0.48).move_to([x, cy - 0.75, 0])
            self.circ.append(c)
            self.nums.append(n)
            self.rot.append(r)
        self.add(self.linea, *self.circ, *self.nums, *self.rot)

    def luz(self, i: int, color=AMBAR):
        return [self.circ[i].animate.set_stroke(color).set_fill(color, 0.3),
                self.nums[i].animate.set_color(color), self.rot[i].animate.set_color(color)]


def movil7(color=TXT) -> VGroup:
    """Teléfono móvil plano (~1,2 de alto). `.cuerpo`."""
    cuerpo = RoundedRectangle(corner_radius=0.12, width=0.65, height=1.2, color=color,
                              stroke_width=4).set_fill(FONDO, 1)
    pantalla = RoundedRectangle(corner_radius=0.05, width=0.5, height=0.8, color=color, stroke_width=0)
    pantalla.set_fill(AZUL, 0.15).move_to(cuerpo.get_center() + UP * 0.1)
    boton_ = Circle(radius=0.05, color=color, stroke_width=0).set_fill(color, 1).move_to(cuerpo.get_bottom() + UP * 0.12)
    g = VGroup(cuerpo, pantalla, boton_)
    g.cuerpo = cuerpo
    return g


def serie_monedas7(n: int = 10000, semilla: int = 4) -> np.ndarray:
    """Lanzamientos (1 = cara) de la escena del repaso: los diez primeros dan siete caras."""
    rng = np.random.default_rng(semilla)
    primeros = np.array([1, 1, 0, 1, 1, 0, 1, 0, 1, 1])
    return np.concatenate([primeros, rng.integers(0, 2, n - 10)])


def fraccion_caras7(puntos: int = 160) -> tuple[np.ndarray, np.ndarray]:
    """(log10 de la cantidad de lanzamientos, fracción de caras) desde 10 hasta 10.000."""
    x = serie_monedas7()
    acum = np.cumsum(x) / np.arange(1, len(x) + 1)
    ks = np.unique(np.round(np.logspace(1, 4, puntos)).astype(int))
    return np.log10(ks), acum[ks - 1]


def fila_monedas7(caras: int = 7, n: int = 10, centro=(0.0, 0.0), paso: float = 0.5, radio: float = 0.2) -> VGroup:
    """Fila de `n` monedas pequeñas; las primeras `caras` son ámbar (cara) y el resto, grises (cruz)."""
    ms = []
    for i in range(n):
        col = AMBAR if i < caras else INK
        ms.append(Circle(radius=radio, color=col, stroke_width=3).set_fill(col, 0.4))
    g = VGroup(*ms).arrange(RIGHT, buff=paso - 2 * radio).move_to([centro[0], centro[1], 0])
    g.monedas = ms
    return g


# ============================================================ capítulo 7, episodio 6: correlación y covarianza

CANAL6 = [[0.63, 0.07], [0.03, 0.27]]    # filas: enviado S = 0, 1; columnas: recibido R = 0, 1


class TablaCanal:
    """Tabla conjunta del canal que confunde bits (S enviado en filas, R recibido en columnas).
    Las piezas se crean sueltas para animarlas una a una:

        T = TablaCanal(centro=(0, 0), lado=1.5)
        self.play(FadeIn(T.armazon()))            # casillas y encabezados
        self.play(FadeIn(T.probs()))              # 0,63 · 0,07 · 0,03 · 0,27
        self.play(Create(T.marco(1, 1, AMBAR)))   # contorno de una casilla
        T.texto(1, 1, "1·1", AMBAR, arriba=True)  # texto extra dentro de la casilla
    """

    def __init__(self, centro=(0.0, 0.0), lado: float = 1.5, esc: float = 0.6, probs=None):
        self.centro = np.array([centro[0], centro[1], 0.0])
        self.lado, self.esc = lado, esc
        self.p = probs if probs is not None else CANAL6
        self.cel = [[Square(lado, color=INK, stroke_width=2.5, fill_color=INK, fill_opacity=0.08)
                     .move_to(self.c(i, j)) for j in range(2)] for i in range(2)]
        self.prob = [[Text(num(self.p[i][j], 3), color=TXT).scale(esc).move_to(self.c(i, j) + DOWN * lado * 0.14)
                      for j in range(2)] for i in range(2)]
        self.enc_f = [Text(f"S = {i}", color=SENAL, weight=BOLD).scale(esc * 0.85)
                      .next_to(self.c(i, 0) + LEFT * lado / 2, LEFT, buff=0.2) for i in range(2)]
        self.enc_c = [Text(f"R = {j}", color=MEDIDA, weight=BOLD).scale(esc * 0.85)
                      .next_to(self.c(0, j) + UP * lado / 2, UP, buff=0.15) for j in range(2)]

    def c(self, i: int, j: int) -> np.ndarray:
        return self.centro + np.array([(j - 0.5) * self.lado, (0.5 - i) * self.lado, 0.0])

    def armazon(self) -> VGroup:
        return VGroup(*[c for fila in self.cel for c in fila], *self.enc_f, *self.enc_c)

    def probs(self) -> VGroup:
        return VGroup(*[p for fila in self.prob for p in fila])

    def marco(self, i: int, j: int, color=AMBAR, ancho: float = 6) -> Square:
        return Square(self.lado, color=color, stroke_width=ancho, fill_opacity=0).move_to(self.c(i, j))

    def texto(self, i: int, j: int, txt: str, color=TXT, escala: float = 0.5) -> Text:
        """Texto auxiliar en la mitad de arriba de la casilla (la probabilidad queda abajo)."""
        return Text(txt, color=color).scale(escala).move_to(self.c(i, j) + UP * self.lado * 0.25)


def puntos_corr(rho: float, n: int = 40, semilla: int = 1):
    """n pares (a, b) normales estándar con correlación `rho` (semilla fija)."""
    rng = np.random.default_rng(semilla)
    a = rng.normal(0, 1, n)
    b = rho * a + np.sqrt(1 - rho ** 2) * rng.normal(0, 1, n)
    return a, b


def nube6(centro, sx: float, sy: float, a, b, color=SENAL, radio: float = 0.06) -> VGroup:
    """Puntos (a, b) escalados a pantalla alrededor de `centro`."""
    c = np.array([centro[0], centro[1], 0.0])
    return VGroup(*[Dot(c + np.array([sx * x, sy * y, 0.0]), radius=radio, color=color) for x, y in zip(a, b)])


# ============================================================ capítulo 07, episodio 5: dos variables a la vez

def canal7(centro=(0.0, 0.0), ancho: float = 7.0, escala: float = 1.0) -> VGroup:
    """El canal que confunde bits: flecha de entrada, caja «canal», flecha de salida.
    `.caja`, `.rot`, `.ent`, `.sal`, `p_ent()`, `p_sal()` (extremos de las flechas)."""
    c = np.array([centro[0], centro[1], 0.0])
    caja_ = RoundedRectangle(corner_radius=0.14, width=2.3 * escala, height=1.3 * escala, color=INK,
                             stroke_width=3).set_fill(INK, 0.12).move_to(c)
    rot = Text("canal", color=TXT).scale(0.55 * escala).move_to(c)
    mitad = ancho / 2
    ent = Arrow(c + LEFT * mitad, c + LEFT * 1.15 * escala, color=SENAL, buff=0, stroke_width=4,
                max_tip_length_to_length_ratio=0.2)
    sal = Arrow(c + RIGHT * 1.15 * escala, c + RIGHT * mitad, color=MEDIDA, buff=0, stroke_width=4,
                max_tip_length_to_length_ratio=0.2)
    g = VGroup(caja_, rot, ent, sal)
    g.caja, g.rot, g.ent, g.sal = caja_, rot, ent, sal
    g.p_ent = lambda: c + LEFT * mitad
    g.p_sal = lambda: c + RIGHT * mitad
    return g


class Tabla2x2(VGroup):
    """Tabla conjunta de lo enviado (filas S = 0, 1) y lo recibido (columnas R = 0, 1).
    `.cel[i][j]` (cuadrados), `.rot_f[i]`, `.rot_c[j]`; `c(i, j)` centro de la casilla;
    `p_fila(i)` y `p_col(j)` donde van las sumas marginales; `marco(i, j)`; `valor(i, j, tex)`."""

    def __init__(self, centro=(0.0, 0.0), lado: float = 1.5):
        super().__init__()
        self.centro = np.array([centro[0], centro[1], 0.0])
        self.lado = lado
        self.cel = [[Square(lado, color=INK, stroke_width=3).set_fill(INK, 0.08).move_to(self.c(i, j))
                     for j in range(2)] for i in range(2)]
        self.rot_f = [MathTex(f"S={i}", color=SENAL).scale(1.0).move_to(self.c(i, 0) + LEFT * (lado * 0.5 + 0.8))
                      for i in range(2)]
        self.rot_c = [MathTex(f"R={j}", color=MEDIDA).scale(1.0).move_to(self.c(0, j) + UP * (lado * 0.5 + 0.45))
                      for j in range(2)]
        self.add(*[c for fila in self.cel for c in fila], *self.rot_f, *self.rot_c)

    def c(self, i: int, j: int) -> np.ndarray:
        return self.centro + np.array([(j - 0.5) * self.lado, (0.5 - i) * self.lado, 0.0])

    def p_fila(self, i: int) -> np.ndarray:
        return self.c(i, 1) + RIGHT * (self.lado * 0.5 + 0.9)

    def p_col(self, j: int) -> np.ndarray:
        return self.c(1, j) + DOWN * (self.lado * 0.5 + 0.45)

    def marco(self, i: int, j: int, color=AMBAR, ancho: float = 6) -> Square:
        return Square(self.lado, color=color, stroke_width=ancho).set_fill(color, 0).move_to(self.c(i, j))

    def valor(self, i: int, j: int, tex: str, color=TXT, escala: float = 0.9) -> MathTex:
        return MathTex(tex, color=color).scale(escala).move_to(self.c(i, j))


def nube_xy7(n: int = 130, semilla: int = 11, ruido: float = 0.7):
    """Pares (x, y) de la nube: x una tensión N(0, 1) recortada a ±2,6 e y = x + ruido (semilla fija)."""
    rng = np.random.default_rng(semilla)
    x = np.clip(rng.normal(0, 1, n), -2.6, 2.6)
    y = x + ruido * rng.normal(0, 1, n)
    return x, y


class Colina(VGroup):
    """La densidad conjunta como colina en perspectiva oblicua (líneas ocultas, de atrás hacia adelante).
    Coordenadas (u, v) en [-r, r]; la densidad es normal estándar bivariada con correlación `rho`.
    `.base` (el plano), `.filas` (relleno + línea de cada fila), `P(u, v, h)` → pantalla,
    `h(u, v)`, `region(u0, u1, v0, v1, color)` (volumen encima de un rectángulo del plano),
    `corte_u(u)` (la rebanada a u fijo) y `curva_fila(v)`."""

    def __init__(self, centro=(0.0, 0.0), rho: float = 0.82, ancho: float = 5.4, prof: float = 2.6,
                 alto: float = 2.4, n: int = 17, r: float = 2.5, color=AZUL):
        super().__init__()
        self.c0 = np.array([centro[0], centro[1], 0.0])
        self.rho, self.ancho, self.prof, self.alto, self.r, self.n, self.color = rho, ancho, prof, alto, r, n, color
        self.base = Polygon(*[self.P(u, v) for u, v in ((-r, -r), (r, -r), (r, r), (-r, r))],
                            color=INK, stroke_width=2.5).set_fill(INK, 0.06)
        self.filas = []
        us = np.linspace(-r, r, 70)
        for v in np.linspace(r, -r, n):
            sup = np.array([self.P(u, v, self.h(u, v)) for u in us])
            suelo = np.array([self.P(u, v) for u in us])
            relleno = Polygon(*sup, *suelo[::-1], stroke_width=0, fill_color=FONDO, fill_opacity=1)
            linea = traza(sup[:, 0], sup[:, 1], color, 2.4, 0.95)
            self.filas.append((relleno, linea))
        self.add(self.base, *[m for par in self.filas for m in par])
        for m in self.get_family():
            m.permitir_encima = True   # los rótulos sobre la colina son a propósito

    def P(self, u: float, v: float, h: float = 0.0) -> np.ndarray:
        r = self.r
        return self.c0 + np.array([u / r * self.ancho / 2 + v / r * self.prof * 0.45,
                                   v / r * self.prof / 2 + h * self.alto - self.alto * 0.25, 0.0])

    def h(self, u, v):
        q = (u ** 2 - 2 * self.rho * u * v + v ** 2) / (2 * (1 - self.rho ** 2))
        return np.exp(-q)

    def curva_fila(self, v: float, color=AMBAR, ancho: float = 4.0) -> VMobject:
        us = np.linspace(-self.r, self.r, 70)
        pts = np.array([self.P(u, v, self.h(u, v)) for u in us])
        return traza(pts[:, 0], pts[:, 1], color, ancho)

    def corte_u(self, u: float, color=AMBAR, ancho: float = 4.0) -> VMobject:
        vs = np.linspace(-self.r, self.r, 70)
        pts = np.array([self.P(u, v, self.h(u, v)) for v in vs])
        return traza(pts[:, 0], pts[:, 1], color, ancho)

    def region(self, u0: float, u1: float, v0: float, v1: float, color=AMBAR, k: int = 6) -> VGroup:
        """Parche del plano y, encima, las láminas de colina que hay sobre él."""
        parche = Polygon(*[self.P(u, v) for u, v in ((u0, v0), (u1, v0), (u1, v1), (u0, v1))],
                         stroke_width=3, color=color).set_fill(color, 0.35)
        laminas = VGroup()
        us = np.linspace(u0, u1, 24)
        for v in np.linspace(v1, v0, k):
            sup = np.array([self.P(u, v, self.h(u, v)) for u in us])
            suelo = np.array([self.P(u, v) for u in us])
            laminas.add(Polygon(*sup, *suelo[::-1], stroke_width=1.5, color=color).set_fill(color, 0.3))
        g = VGroup(parche, laminas)
        for m in g.get_family():
            m.permitir_encima = True
        return g


class Alturas7(VGroup):
    """Las dos campanas de la altura: hombres (40 %, 175 cm, desvío 7) y mujeres (60 %, 162 cm, desvío 6).
    `.base`, `.h`, `.m` (curvas), `x(cm)` → abscisa en pantalla, `y(d)` → ordenada, `marca(cm)` línea vertical."""

    def __init__(self, centro=(0.0, 0.0), ancho: float = 8.0, alto: float = 2.6):
        super().__init__()
        self.cx, self.cy, self.ancho, self.alto = centro[0], centro[1], ancho, alto
        self.x0, self.x1 = 143.0, 195.0
        cm = np.linspace(self.x0, self.x1, 160)
        dh = 0.4 * gaussiana(cm, 175, 7)
        dm = 0.6 * gaussiana(cm, 162, 6)
        self.vmax = float(max(dh.max(), dm.max()))
        self.base = Line([float(self.x(self.x0)), self.cy - alto / 2, 0],
                         [float(self.x(self.x1)), self.cy - alto / 2, 0], color=INK, stroke_width=2)
        self.h = traza(self.x(cm), self.y(dh), AZUL, 4)
        self.m = traza(self.x(cm), self.y(dm), MAGENTA, 4)
        self.add(self.base, self.h, self.m)

    def x(self, cm):
        return self.cx - self.ancho / 2 + (np.asarray(cm, dtype=float) - self.x0) / (self.x1 - self.x0) * self.ancho

    def y(self, d):
        return self.cy - self.alto / 2 + np.asarray(d, dtype=float) / self.vmax * self.alto

    def marca(self, cm: float, color=AMBAR, ancho: float = 3.0, alto: float | None = None) -> Line:
        a = self.alto if alto is None else alto
        x = float(self.x(cm))
        return Line([x, self.cy - self.alto / 2, 0], [x, self.cy - self.alto / 2 + a, 0],
                    color=color, stroke_width=ancho)


class BarrasVar7(VGroup):
    """Barra de varianza partida en dos trozos: dentro (41,2, rojo) y entre (40,56, verde) los grupos.
    `.dentro`, `.entre` (rectángulos), `esc` (unidades de pantalla por unidad de varianza)."""

    def __init__(self, origen=(-3.0, 0.0), esc: float = 0.075, alto: float = 0.7,
                 dentro: float = 41.2, entre: float = 40.56):
        super().__init__()
        o = np.array([origen[0], origen[1], 0.0])
        self.esc, self.o = esc, o
        self.dentro = Rectangle(width=dentro * esc, height=alto, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
        self.dentro.move_to(o + RIGHT * dentro * esc / 2)
        self.entre = Rectangle(width=entre * esc, height=alto, color=VERDE, stroke_width=2.5).set_fill(VERDE, 0.4)
        self.entre.move_to(o + RIGHT * (dentro + entre / 2) * esc)
        self.add(self.dentro, self.entre)


# ============================================================ capítulo 07, episodio 2: condicional, test médico y Bayes

class EspacioDado07(VGroup):
    """El espacio muestral del dado: rectángulo con las seis caras en fila.
    `.marco`, `.caras` (lista de 6), `.lado`, `.paso`; `p(i)` es el centro de la cara i (1–6);
    `aros(idx, color, margen)` devuelve un grupo de recuadros que rodean cada cara de `idx`."""

    def __init__(self, centro=(0.0, 0.0), lado: float = 0.9, color=INK):
        super().__init__()
        self.lado = lado
        self.paso = lado * 1.3
        self.c = np.array([centro[0], centro[1], 0.0])
        x0 = centro[0] - 2.5 * self.paso
        self.caras = [dado_n(i + 1).scale(lado).move_to([x0 + i * self.paso, centro[1], 0]) for i in range(6)]
        self.marco = RoundedRectangle(corner_radius=0.2, width=6 * self.paso + 0.1, height=lado + 0.7,
                                      color=color, stroke_width=3).move_to(self.c)
        self.add(self.marco, *self.caras)

    def p(self, i: int):
        return self.caras[i - 1].get_center()

    def aros(self, idx, color=AMBAR, margen: float = 0.14) -> VGroup:
        return VGroup(*[RoundedRectangle(corner_radius=0.2, width=self.lado + 2 * margen,
                                         height=self.lado + 2 * margen, color=color,
                                         stroke_width=5).move_to(self.p(i)) for i in idx])


class GrillaMil07(VGroup):
    """Mil personas como cuadraditos, 60 por fila (la primera fila son exactamente 60).
    `.pts` (lista de 1000), `.fila0` (primeros 60). Los diez primeros son «enfermos»."""

    def __init__(self, centro=(0.0, 0.0), n: int = 1000, cols: int = 60, paso: float = 0.12, color=VERDE):
        super().__init__()
        filas = -(-n // cols)
        x0 = centro[0] - (cols - 1) * paso / 2
        y0 = centro[1] + (filas - 1) * paso / 2
        self.pts = []
        for k in range(n):
            f, c = divmod(k, cols)
            self.pts.append(Square(side_length=paso * 0.72, stroke_width=0)
                            .set_fill(color, 0.9).move_to([x0 + c * paso, y0 - f * paso, 0]))
        self.add(*self.pts)
        self.paso, self.cols = paso, cols
        self.fila0 = VGroup(*self.pts[:cols])

    def recuadro(self, i0: int, i1: int, color=AMBAR) -> Rectangle:
        g = VGroup(*self.pts[i0:i1])
        return SurroundingRectangle(g, color=color, buff=0.06, stroke_width=3)


class Arbol07(VGroup):
    """Árbol de dos niveles hacia la derecha. `.raiz`, `.n1[i]`, `.hojas[i][j]` (rótulos de nodo),
    `.l1[i]`, `.l2[i][j]` (ramas), `.e1[i]`, `.e2[i][j]` (probabilidades de cada rama).
    `rama(i, j=None, color)` devuelve las ramas a resaltar."""

    def __init__(self, raiz: str, nivel1, nivel2, p1, p2, centro=(0.0, 0.0), ancho: float = 8.0,
                 alto: float = 3.8, escala: float = 0.5):
        super().__init__()
        cx, cy = centro
        xr, x1, x2 = cx - ancho / 2, cx - ancho / 2 + ancho * 0.42, cx + ancho / 2

        def nodo(txt, color, x, y):
            t = Text(txt, color=TXT).scale(escala)
            r = RoundedRectangle(corner_radius=0.1, width=t.width + 0.35, height=0.55, color=color,
                                 stroke_width=2.5).set_fill(color, 0.14).move_to([x, y, 0])
            t.move_to(r)
            return VGroup(r, t)

        self.raiz = nodo(raiz, INK, xr, cy)
        ys1 = [cy + alto / 4, cy - alto / 4]
        self.n1, self.hojas, self.l1, self.l2, self.e1, self.e2 = [], [], [], [], [], []
        for i, ((t, c), y1) in enumerate(zip(nivel1, ys1)):
            n = nodo(t, c, x1, y1)
            self.n1.append(n)
            l = Line(self.raiz[0].get_right(), n[0].get_left(), color=INK, stroke_width=3)
            self.l1.append(l)
            e = MathTex(p1[i], color=TXT).scale(0.62).move_to(l.get_center() + (UP if i == 0 else DOWN) * 0.3
                                                              + (LEFT if i == 0 else LEFT) * 0.1)
            self.e1.append(e)
            hs, ls, es = [], [], []
            for j, (t2, c2) in enumerate(nivel2[i]):
                y2 = y1 + (0.5 if j == 0 else -0.5) * (alto / 4 * 0.92)
                h = nodo(t2, c2, x2, y2)
                hs.append(h)
                l2 = Line(n[0].get_right(), h[0].get_left(), color=INK, stroke_width=3)
                ls.append(l2)
                e2 = MathTex(p2[i][j], color=TXT).scale(0.62).move_to(l2.get_center() + (UP if j == 0 else DOWN) * 0.3)
                es.append(e2)
            self.hojas.append(hs)
            self.l2.append(ls)
            self.e2.append(es)
        self.add(self.raiz, *self.n1, *self.l1, *self.e1,
                 *[x for hs in self.hojas for x in hs], *[x for ls in self.l2 for x in ls],
                 *[x for es in self.e2 for x in es])

    def rama(self, i: int, j: int | None = None, color=AMBAR, ancho: float = 7):
        """Ramas que llevan hasta la hoja (i, j), o solo la primera si j es None, ya coloreadas (copias)."""
        ls = [self.l1[i].copy().set_stroke(color, ancho)]
        if j is not None:
            ls.append(self.l2[i][j].copy().set_stroke(color, ancho))
        return VGroup(*ls)


def tira_test07(escala: float = 1.0) -> VGroup:
    """La tira del test: placa con la palabra «test» y una ventanita. `.cuerpo`, `.ventana`."""
    cuerpo = RoundedRectangle(corner_radius=0.15, width=1.3, height=2.6, color=MEDIDA,
                              stroke_width=4).set_fill(FONDO, 1)
    t = Text("Test", color=TXT).scale(0.5).move_to(cuerpo.get_top() + DOWN * 0.45)
    ventana = RoundedRectangle(corner_radius=0.1, width=0.85, height=0.85, color=INK,
                               stroke_width=3).move_to(cuerpo.get_center() + DOWN * 0.45)
    g = VGroup(cuerpo, t, ventana).scale(escala)
    g.cuerpo, g.ventana = cuerpo, ventana
    return g


# ============================================================ capítulo 07, episodio 3: la forma del azar

def cdf_normal(x, mu: float = 0.0, sigma: float = 1.0):
    """Acumulada de la normal N(mu, sigma²) en x (escalar o arreglo)."""
    from math import erf, sqrt
    z = (np.asarray(x, dtype=float) - mu) / (sigma * sqrt(2))
    return 0.5 * (1 + np.vectorize(erf)(z))


class RectaNum(VGroup):
    """Recta numérica horizontal con marcas y números.

        r = RectaNum(0, 7, centro=(0, -2), ancho=7, marcas=[1, 2, 3])
        r.p(x) -> punto en pantalla;  `.base`, `.ticks[x]`, `.nums[x]`
    """

    def __init__(self, x0, x1, centro=(0.0, 0.0), ancho=8.0, marcas=(), color=INK, tam=0.42):
        super().__init__()
        self.x0, self.x1, self.cx, self.cy, self.ancho = x0, x1, centro[0], centro[1], ancho
        self.base = Line(self.p(x0), self.p(x1), color=color, stroke_width=2.5)
        self.ticks, self.nums = {}, {}
        self.add(self.base)
        for v in marcas:
            t = Line(self.p(v) + UP * 0.1, self.p(v) + DOWN * 0.1, color=color, stroke_width=2.5)
            n = Text(str(v).replace(".", ","), color=color).scale(tam).next_to(t, DOWN, buff=0.1)
            self.ticks[v], self.nums[v] = t, n
            self.add(t, n)

    def p(self, x) -> np.ndarray:
        return np.array([self.cx - self.ancho / 2 + (x - self.x0) / (self.x1 - self.x0) * self.ancho,
                         self.cy, 0.0])


class AcumDado(VGroup):
    """Acumulada del dado: ejes (x de 0 a 8, y de 0 a 1) y su escalera.

    `.ax`, `.p(x, y)`, `.peldanos` (7 tramos: F = k/6 en [k, k+1)), `.llenos`,
    `.huecos` (extremos de cada salto), `.nums_x`, `.nums_y`, `cursor(x)`.
    """

    def __init__(self, centro=(0.5, -0.5), ancho=9.0, alto=3.9):
        super().__init__()
        self.ax = Axes(x_range=[0, 8, 1], y_range=[0, 1.15, 1], x_length=ancho, y_length=alto * 1.15,
                       axis_config={"color": INK, "stroke_width": 2, "include_ticks": False,
                                    "tip_width": 0.16, "tip_height": 0.16}).move_to([*centro, 0])
        self.nums_x = VGroup(*[Text(str(k), color=INK).scale(0.55).next_to(self.p(k, 0), DOWN, buff=0.12)
                               for k in range(1, 7)])
        self.nums_y = VGroup(*[Text(t, color=INK).scale(0.5).next_to(self.p(0, v), LEFT, buff=0.12)
                               for t, v in (("1/6", 1 / 6), ("2/6", 2 / 6), ("3/6", 3 / 6),
                                            ("4/6", 4 / 6), ("5/6", 5 / 6), ("1", 1.0))])
        self.peldanos = VGroup(*[Line(self.p(k, k / 6), self.p(k + 1, k / 6), color=AMBAR, stroke_width=5)
                                 for k in range(7)])
        self.llenos = VGroup(*[Dot(self.p(k, k / 6), radius=0.07, color=AMBAR) for k in range(1, 7)])
        self.huecos = VGroup(*[Circle(radius=0.07, color=AMBAR, stroke_width=3).set_fill(FONDO, 1)
                               .move_to(self.p(k + 1, k / 6)) for k in range(6)])
        self.add(self.ax, self.nums_x, self.nums_y)

    def p(self, x, y) -> np.ndarray:
        return self.ax.c2p(x, y)

    def cursor(self, x, color=VERDE) -> Line:
        return Line(self.p(x, 0), self.p(x, 1.08), color=color, stroke_width=3)

    def F(self, x) -> float:
        return float(min(max(np.floor(x), 0), 6)) / 6


# ============================================================ capítulo 07, episodio 4: media, varianza y promedios

class Regla7(VGroup):
    """Recta de valores 1 a 6 (la del dado) con marcas y rótulos.

        R = Regla7(centro=(0, -1.0), ancho=9.6)
    `p(v)` da el punto de la recta en el valor `v`; `.base`, `.marcas`, `.rots`.
    """

    def __init__(self, centro=(0.0, -1.0), ancho: float = 9.6, v0: float = 0.4, v1: float = 6.6,
                 valores=(1, 2, 3, 4, 5, 6), color=INK, rotulos: bool = True):
        super().__init__()
        self.cx, self.cy, self.ancho, self.v0, self.v1 = centro[0], centro[1], ancho, v0, v1
        self.base = Line(self.p(v0), self.p(v1), color=color, stroke_width=3)
        self.marcas = VGroup(*[Line(self.p(v) + DOWN * 0.1, self.p(v) + UP * 0.1, color=color, stroke_width=3)
                               for v in valores])
        self.rots = VGroup()
        if rotulos:
            for v in valores:
                self.rots.add(Text(str(v), color=INK).scale(0.45).next_to(self.p(v), DOWN, buff=0.2))
        self.add(self.base, self.marcas, self.rots)

    def p(self, v: float) -> np.ndarray:
        return np.array([self.cx - self.ancho / 2 + (v - self.v0) / (self.v1 - self.v0) * self.ancho,
                         self.cy, 0.0])


def caras7(regla: Regla7, escala: float = 0.85, altura: float = 1.1, valores=(1, 2, 3, 4, 5, 6)) -> VGroup:
    """Las caras del dado sobre una `Regla7`, cada una encima de su valor. `.caras`."""
    caras = [dado_n(v).scale(escala).move_to(regla.p(v) + UP * altura) for v in valores]
    g = VGroup(*caras)
    g.caras = caras
    return g


def promedios_dado(n: int, semilla: int = 7) -> np.ndarray:
    """Promedio acumulado de `n` tiradas de dado (semilla fija)."""
    x = np.random.default_rng(semilla).integers(1, 7, n)
    return np.cumsum(x) / np.arange(1, n + 1)


def promedios_ruido(n: int, semilla: int = 3, sigma: float = 1.0) -> np.ndarray:
    """Promedio acumulado de `n` medidas de ruido de media 0 y desvío `sigma` (semilla fija)."""
    x = np.random.default_rng(semilla).normal(0.0, sigma, n)
    return np.cumsum(x) / np.arange(1, n + 1)


def fila_personas7(n: int = 10, centro=(0.0, 0.0), paso: float = 0.95, escala: float = 0.9) -> VGroup:
    """Fila de personas para el ejemplo de los sueldos. `.personas`."""
    from comun.iconos import persona
    ps = [persona(AZUL).scale(escala) for _ in range(n)]
    g = VGroup(*ps).arrange(RIGHT, buff=paso - 0.72 * escala).move_to([centro[0], centro[1], 0])
    g.personas = ps
    return g


# ============================================================ capítulo 07, episodio 7: variables que son flechas

COL_U7 = SENAL    # la primera flecha (u, X)
COL_V7 = MEDIDA   # la segunda flecha (v, Y)


def cuadricula7(origen, paso: float, nx: int, ny: int) -> VGroup:
    """Cuadrícula tenue de nx × ny celdas de lado `paso`; `origen` es el punto de pantalla del (0, 0)."""
    o = np.array([origen[0], origen[1], 0.0])
    g = VGroup()
    for i in range(nx + 1):
        g.add(Line(o + RIGHT * i * paso, o + RIGHT * i * paso + UP * ny * paso,
                   color=INK, stroke_width=1.2, stroke_opacity=0.28))
    for j in range(ny + 1):
        g.add(Line(o + UP * j * paso, o + UP * j * paso + RIGHT * nx * paso,
                   color=INK, stroke_width=1.2, stroke_opacity=0.28))
    return g


def vec7(origen, x: float, y: float, paso: float, color=COL_U7, ancho: float = 7) -> Arrow:
    """Flecha del origen al punto (x, y) de la cuadrícula."""
    o = np.array([origen[0], origen[1], 0.0])
    return Arrow(o, o + np.array([x * paso, y * paso, 0.0]), buff=0, color=color, stroke_width=ancho,
                 max_tip_length_to_length_ratio=0.2)


def punto7(origen, x: float, y: float, paso: float) -> np.ndarray:
    return np.array([origen[0] + x * paso, origen[1] + y * paso, 0.0])


def arco7(origen, g0: float, g1: float, radio: float = 0.8, color=AMBAR, ancho: float = 4) -> Arc:
    """Arco entre dos direcciones (en grados), centrado en `origen`."""
    return Arc(radius=radio, start_angle=np.deg2rad(g0), angle=np.deg2rad(g1 - g0),
               arc_center=np.array([origen[0], origen[1], 0.0]), color=color, stroke_width=ancho)


def nube7(centro, rho: float, n: int = 40, ancho: float = 2.6, semilla: int = 3, color=SENAL) -> VGroup:
    """Nube de puntos con correlación `rho` (misma semilla: los puntos se mueven al cambiar rho)."""
    rng = np.random.default_rng(semilla)
    a, b = rng.normal(0, 1, n), rng.normal(0, 1, n)
    xs, ys = a, rho * a + np.sqrt(max(0.0, 1 - rho ** 2)) * b
    k = ancho / 6.0
    return VGroup(*[Dot([centro[0] + x * k, centro[1] + y * k, 0], radius=0.06, color=color)
                    for x, y in zip(xs, ys)])


def casilla7(txt: str, centro, color=INK, ancho: float = 3.6, alto: float = 0.8, escala: float = 0.5) -> VGroup:
    """Casilla vacía con un número o texto; `.marco` y `.txt`."""
    r = RoundedRectangle(corner_radius=0.12, width=ancho, height=alto, color=color, stroke_width=2.5)
    t = Text(txt, color=TXT).scale(escala)
    r.move_to([centro[0], centro[1], 0])
    t.move_to(r)
    g = VGroup(r, t)
    g.marco, g.txt = r, t
    return g


def huecos_tres(llenos=()) -> tuple:
    """Fila de tres huecos (Bernoulli, uniforme, gaussiana) arriba del plano.
    `llenos`: nombres ya colocados (se ven fijos). Devuelve `(grupo, huecos, centros)`."""
    centros = [np.array([x, 3.25, 0.0]) for x in (-4.4, 0.0, 4.4)]
    huecos = VGroup(*[DashedVMobject(RoundedRectangle(corner_radius=0.15, width=3.5, height=0.95, color=INK,
                                                    stroke_width=2.5)).move_to(c) for c in centros])
    g = VGroup(huecos)
    nombres = ("Bernoulli", "uniforme", "gaussiana")
    for i, n in enumerate(nombres):
        if n in llenos:
            g.add(Text(n.capitalize(), color=AMBAR, weight=BOLD).scale(0.65).move_to(centros[i]))
    return g, huecos, centros


def campana7(cx: float, cy: float, sigma: float = 1.0, color=SENAL, ancho: float = 1.0,
             alto: float = 2.0, mu: float = 0.0, x_max: float = 4.0) -> VMobject:
    """Campana en coordenadas de pantalla: centro en `cx`, base en `cy`, altura `alto`.
    `sigma` y `x_max` están en unidades de x; cada unidad mide `ancho` en pantalla."""
    xs = np.linspace(-x_max, x_max, 160)
    ys = np.exp(-0.5 * ((xs - mu) / sigma) ** 2)
    return traza(cx + xs * ancho, cy + ys * alto, color, 4)


def cola7(cx: float, cy: float, sigma: float, desde: float, hasta: float, color=ERROR,
          ancho: float = 1.0, alto: float = 2.0, opacidad: float = 0.5) -> VMobject:
    """Área bajo `campana7` (de media 0) entre `desde` y `hasta` (en unidades de x)."""
    xs = np.linspace(desde, hasta, 40)
    ys = np.exp(-0.5 * (xs / sigma) ** 2)
    pts = [np.array([cx + x * ancho, cy + y * alto, 0.0]) for x, y in zip(xs, ys)]
    pts += [np.array([cx + hasta * ancho, cy, 0.0]), np.array([cx + desde * ancho, cy, 0.0]), pts[0]]
    m = VMobject(stroke_width=0)
    m.set_fill(color, opacidad)
    m.set_points_as_corners(pts)
    return m


def eje_v7(L: Lienzo, v0: float, v1: float, t: float | None = None, color=INK, ancho: float = 1.8) -> Line:
    """Eje vertical de un `Lienzo` (por defecto en el borde izquierdo, t = t0), de v0 a v1."""
    tt = L.t0 if t is None else t
    return Line(L.p(tt, v0), L.p(tt, v1), color=color, stroke_width=ancho)


# ============================================================ capítulo 08, episodio 1: la mejor apuesta

class Mesa8(VGroup):
    """Las seis caras del dado sobre su recta (sin números en la recta), con sitio debajo para los
    cuadrados de los errores y una marca de apuesta.

        M = Mesa8(y_regla=0.4)
        M.p(v)                 punto de la recta en el valor v
        M.marca(a)             triángulo ámbar bajo la recta con «Apuesta a» (`.tri`, `.rot`)
        M.cuadrado(k, txt)     texto bajo la cara k (a 1,05 por debajo de la recta)
    Atributos: `.regla`, `.caras` (grupo, `.caras.caras[i]` es la cara i + 1)."""

    def __init__(self, ancho: float = 10.4, y_regla: float = 0.4):
        self.regla = Regla7(centro=(0.0, y_regla), ancho=ancho, rotulos=False)
        self.caras = caras7(self.regla, escala=0.8, altura=1.0)
        super().__init__(self.regla, self.caras)

    def p(self, v) -> np.ndarray:
        return self.regla.p(v)

    def marca(self, a: float, color=AMBAR) -> VGroup:
        tri = Triangle(color=color, stroke_width=2).set_fill(color, 0.9).scale(0.16)
        tri.move_to(self.p(a) + DOWN * 0.22)
        rot = Text(f"Apuesta {num(a)}", color=color, weight=BOLD).scale(0.5).next_to(tri, DOWN, buff=0.12)
        g = VGroup(tri, rot)
        g.tri, g.rot = tri, rot
        return g

    def cuadrado(self, k: float, txt: str, color=TXT, escala: float = 0.8) -> Text:
        return Text(txt, color=color, weight=BOLD).scale(escala).move_to(self.p(k) + DOWN * 1.15)


class ParabolaApuestas8(VGroup):
    """Apuesta (horizontal) contra error cuadrático medio (vertical) del dado: ECM(a) = 35/12 + (3,5 − a)².

    `.eje_x`, `.eje_y`, `.curva`, `.vertice`; `ecm(a)` (estática), `p(a)` punto de la curva,
    `punto(a, color)` un punto sobre ella, `suelo(color)` la línea del suelo (2,92)."""

    A0, A1, EMAX = 0.4, 6.6, 10.0
    SUELO = 35 / 12

    def __init__(self, centro=(0.0, -0.3), ancho: float = 8.6, alto: float = 4.6, color=ESTIMACION):
        super().__init__()
        self.cx, self.cy, self.ancho, self.alto = centro[0], centro[1], ancho, alto
        self.eje_x = Line(self.xy(self.A0, 0), self.xy(self.A1, 0), color=INK, stroke_width=2.5)
        self.eje_y = Line(self.xy(self.A0, 0), self.xy(self.A0, self.EMAX), color=INK, stroke_width=2.5)
        a = np.linspace(1.0, 6.0, 120)
        self.curva = traza(*zip(*[self.p(v)[:2] for v in a]), color=color, ancho=4.0)
        self.vertice = Dot(self.p(3.5), radius=0.11, color=VERDE)
        self.add(self.eje_x, self.eje_y)

    @staticmethod
    def ecm(a):
        return 35 / 12 + (3.5 - np.asarray(a)) ** 2

    def xy(self, a, e) -> np.ndarray:
        x = self.cx - self.ancho / 2 + (a - self.A0) / (self.A1 - self.A0) * self.ancho
        y = self.cy - self.alto / 2 + e / self.EMAX * self.alto
        return np.array([float(x), float(y), 0.0])

    def p(self, a) -> np.ndarray:
        return self.xy(a, float(self.ecm(a)))

    def punto(self, a, color=AZUL, radio: float = 0.11) -> Dot:
        return Dot(self.p(a), radius=radio, color=color)

    def suelo(self, color=INK) -> Line:
        return DashedLine(self.xy(self.A0, self.SUELO), self.xy(self.A1, self.SUELO), color=color, stroke_width=3)


class BarrasLlamadas8(VGroup):
    """Barras de probabilidad de las llamadas de la centralita (0 · 1 · 2 · 10 con 0,4 · 0,3 · 0,2 · 0,1),
    sobre una recta numérica de 0 a 10.

    `.base`, `.barras` (dict valor → Rectangle), `.nums` (dict valor → Text), `p(v)` punto de la base,
    `marcador(v, color)` triángulo bajo los números, `pct(v)` etiqueta con el porcentaje sobre la barra."""

    PROBS = {0: 0.4, 1: 0.3, 2: 0.2, 10: 0.1}

    def __init__(self, centro=(0.0, -1.2), ancho: float = 10.0, alto: float = 2.6):
        super().__init__()
        self.cx, self.cy, self.ancho, self.alto = centro[0], centro[1], ancho, alto
        self.base = Line(self.p(-0.8), self.p(10.8), color=INK, stroke_width=2.5)
        self.barras, self.nums = {}, {}
        self.add(self.base)
        for v, pr in self.PROBS.items():
            h = pr / 0.4 * alto
            r = Rectangle(width=0.55, height=h, color=SENAL, fill_color=SENAL, fill_opacity=0.45, stroke_width=3)
            r.move_to(self.p(v) + UP * h / 2)
            self.barras[v] = r
        for v in range(0, 11):
            self.nums[v] = Text(str(v), color=INK).scale(0.45).move_to(self.p(v) + DOWN * 0.28)

    def p(self, v) -> np.ndarray:
        return np.array([self.cx - self.ancho / 2 + (float(v) + 0.8) / 11.6 * self.ancho, self.cy, 0.0])

    def marcador(self, v: float, color=ESTIMACION) -> Triangle:
        t = Triangle(color=color, stroke_width=2).set_fill(color, 0.95).scale(0.2)
        return t.move_to(self.p(v) + DOWN * 0.72)

    def pct(self, v, color=TXT) -> Text:
        txt = f"{int(round(self.PROBS[v] * 100))} %"
        return Text(txt, color=color, weight=BOLD).scale(0.5).next_to(self.barras[v], UP, buff=0.12)


def casilla8(x: float, y: float, forma: str, resp: str, color, ancho: float = 3.8, alto: float = 1.6) -> VGroup:
    """Casilla «forma de medir el error → respuesta» (Cuadrado → media, Tamaño → mediana, Acierto → moda).
    `.rect`, `.forma` (texto de arriba) y `.resp` (texto de abajo, con la flecha)."""
    r = RoundedRectangle(corner_radius=0.15, width=ancho, height=alto, color=color, stroke_width=3,
                         fill_color=color, fill_opacity=0.1).move_to([x, y, 0])
    f = Text(forma, color=TXT, weight=BOLD).scale(0.8).move_to([x, y + 0.35, 0])
    t = Text("→ " + resp, color=color, weight=BOLD).scale(0.8).move_to([x, y - 0.35, 0])
    g = VGroup(r, f, t)
    g.rect, g.forma, g.resp = r, f, t
    return g


# ============================================================ capítulo 08, episodio 2: la altura, el canal y la ortogonalidad

CANAL8 = [[r"0{,}63", r"0{,}07"], [r"0{,}03", r"0{,}27"]]


def puerta8(alto: float = 3.0) -> VGroup:
    """Una puerta: marco, hoja y pomo (`.marco`, `.pomo`)."""
    marco = Rectangle(width=alto * 0.5, height=alto, color=INK, stroke_width=4).set_fill(INK, 0.1)
    pomo = Dot(marco.get_right() + LEFT * 0.18 + DOWN * 0.1, radius=0.07, color=AMBAR)
    g = VGroup(marco, pomo)
    g.marco, g.pomo = marco, pomo
    return g


class PuntosErr8(VGroup):
    """Errores sueltos alrededor de una línea de cero: `.cero` (la línea), `.pts` (los puntos),
    `y(v)` → ordenada en pantalla del error `v`. `desplaz` los sube o baja (un patrón)."""

    def __init__(self, centro=(0.0, 0.0), ancho: float = 6.0, alto: float = 2.4, n: int = 36,
                 semilla: int = 4, desplaz: float = 0.0, color=ERROR):
        super().__init__()
        self.c = np.array([centro[0], centro[1], 0.0])
        self.alto = alto
        rng = np.random.default_rng(semilla)
        xs = np.linspace(-ancho / 2 + 0.2, ancho / 2 - 0.2, n)
        vs = np.clip(rng.normal(0, 0.45, n), -0.95, 0.95)
        self.vs = vs
        self.cero = DashedLine(self.c + LEFT * ancho / 2, self.c + RIGHT * ancho / 2, color=INK, stroke_width=2.5)
        self.pts = VGroup(*[Dot([self.c[0] + x, self.y(v + desplaz), 0], radius=0.07, color=color)
                            for x, v in zip(xs, vs)])
        self.add(self.cero, self.pts)

    def y(self, v: float) -> float:
        return float(self.c[1] + v * self.alto / 2)


class Nube8(VGroup):
    """Nube de puntos (x, y) con y = x + ruido, sobre ejes. `.ax`, `.etq`, `.pts` (lista de Dots),
    `.xs`, `.ys`; `p(x, y)` → pantalla; `rebanada(x, ancho, color)` → recuadro vertical en x;
    `en_rebanada(x, ancho)` → índices de los puntos dentro."""

    def __init__(self, centro=(0.0, 0.0), ancho: float = 6.0, alto: float = 4.0, n: int = 90,
                 semilla: int = 11, color=SENAL):
        super().__init__()
        self.ax, self.etq = ejes([-3, 3, 1], [-3.5, 3.5, 1], ancho=ancho, alto=alto, x_label="x", y_label="y")
        self.ax.move_to([centro[0], centro[1], 0])
        self.etq[0].next_to(self.ax.x_axis.get_end(), DR, buff=0.12)
        self.etq[1].next_to(self.ax.y_axis.get_end(), UR, buff=0.08)
        self.xs, self.ys = nube_xy7(n, semilla)
        self.pts = [Dot(self.p(a, b), radius=0.055, color=color) for a, b in zip(self.xs, self.ys)]
        self.add(self.ax, self.etq, *self.pts)

    def p(self, x: float, y: float) -> np.ndarray:
        return self.ax.c2p(x, y)

    def rebanada(self, x: float, ancho: float = 0.5, color=AMBAR) -> Rectangle:
        a, b = self.p(x - ancho / 2, -3.3), self.p(x + ancho / 2, 3.3)
        r = Rectangle(width=b[0] - a[0], height=b[1] - a[1], color=color, stroke_width=3).set_fill(color, 0.1)
        r.move_to((a + b) / 2)
        return r

    def en_rebanada(self, x: float, ancho: float = 0.5) -> list[int]:
        return [i for i, v in enumerate(self.xs) if abs(v - x) <= ancho / 2]


def parabola8(centro=(0.0, 0.0), ancho: float = 2.2, alto: float = 1.6, color=ERROR):
    """Parábola de error (U) con el mínimo abajo, en el centro. Devuelve `(curva, punto_minimo, p)`
    con `p(dx)` la posición en pantalla del punto de la U a `dx` (de −1 a 1) del mínimo."""
    c = np.array([centro[0], centro[1], 0.0])

    def p(dx):
        return c + np.array([dx * ancho / 2, -alto / 2 + dx ** 2 * alto, 0.0])

    xs = np.linspace(-1, 1, 60)
    pts = np.array([p(x) for x in xs])
    curva = traza(pts[:, 0], pts[:, 1], color, 4)
    return curva, Dot(p(0.0), radius=0.12, color=VERDE), p
