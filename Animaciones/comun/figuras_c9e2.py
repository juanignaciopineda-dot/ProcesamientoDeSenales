"""Piezas del capítulo 9, episodio 2 («Dos maneras de equivocarse»).

Módulo aparte (como `figuras_c9e1.py`) para no pisar `figuras.py` cuando
varias sesiones trabajan a la vez. Las escenas lo importan:

    from comun.escena import *
    from comun.figuras_c9e2 import *

Reutiliza las campanas del E1 (`Campanas9`: centros 0 y 2 V, desvío 1) y suma
la tabla 2 × 2 de errores, el umbral, las cotas, las barras de error y la curva
del valor predictivo contra la prevalencia.
"""
from __future__ import annotations

from math import erfc, sqrt

from manim import *

from comun.estilo import *
from comun.figuras import traza
from comun.figuras_c9e1 import C0, C1, CRUCE9, P0, P1, Campanas9, canal9, casilla9, TablaReglas9, garabato9


def Q9(x: float) -> float:
    """Área de la cola de la campana estándar a la derecha de x."""
    return 0.5 * erfc(x / sqrt(2))


class Tabla22_9(VGroup):
    """Tabla 2 × 2 con rótulos de fila a la izquierda y de columna arriba.

        T = Tabla22_9(("Solo ruido", "Hay avión"), ("Nada", "Avión"), centro=(1.6, -0.9))
        T.c(i, j)                 # centro de la casilla (fila i, columna j)
    `.cel[(i, j)]`, `.rot_f`, `.rot_c`, `.titulos`; `nuevas_filas(textos)` y
    `nuevas_cols(textos)` dan rótulos de reemplazo en el mismo sitio;
    `marca(i, j)` da una tilde (diagonal) o una cruz arriba de la casilla;
    `texto(i, j, txt)` un texto dentro de la casilla.
    """

    def __init__(self, filas, cols, centro=(0.0, 0.0), ancho: float = 1.8, alto: float = 1.2,
                 colores_f=(C0, C1), titulo_f: str = "", titulo_c: str = "", escala: float = 0.45):
        super().__init__()
        self.cx, self.cy, self.w, self.h, self.escala = centro[0], centro[1], ancho, alto, escala
        self.colores_f = colores_f
        self.cel = {}
        for i in range(2):
            for j in range(2):
                self.cel[(i, j)] = Rectangle(width=ancho, height=alto, color=INK, stroke_width=2.5) \
                    .set_fill(INK, 0.06).move_to(self.c(i, j))
        self.rot_f = self.nuevas_filas(filas, colores_f)
        self.rot_c = self.nuevas_cols(cols)
        self.titulos = VGroup()
        if titulo_c:
            self.titulos.add(Text(titulo_c, color=INK).scale(escala * 0.9)
                             .move_to([self.cx, self.cy + alto + 0.85, 0]))
        if titulo_f:
            t = Text(titulo_f, color=INK).scale(escala * 0.9)
            t.move_to([self.x_f() - t.width / 2, self.cy + alto + 0.4, 0])
            self.titulos.add(t)
        self.add(*self.cel.values(), self.rot_f, self.rot_c, self.titulos)

    def c(self, i: int, j: int) -> np.ndarray:
        return np.array([self.cx + (j - 0.5) * self.w, self.cy + (0.5 - i) * self.h, 0.0])

    def x_f(self) -> float:
        """Borde derecho de los rótulos de fila."""
        return self.cx - self.w - 0.22

    def nuevas_filas(self, textos, colores=None) -> VGroup:
        colores = colores or self.colores_f
        g = VGroup()
        for i, (t, col) in enumerate(zip(textos, colores)):
            m = Text(t, color=col).scale(self.escala)
            m.move_to([self.x_f() - m.width / 2, self.c(i, 0)[1], 0])
            g.add(m)
        return g

    def nuevas_cols(self, textos, color=INK) -> VGroup:
        return VGroup(*[Text(t, color=color).scale(self.escala)
                        .move_to([self.c(0, j)[0], self.cy + self.h + 0.35, 0]) for j, t in enumerate(textos)])

    def marca(self, i: int, j: int, tam: float = 0.32) -> VMobject:
        from comun.iconos import cruz, tilde
        m = tilde(VERDE, tam) if i == j else cruz(ERROR, tam)
        return m.move_to(self.c(i, j) + UP * self.h * 0.28)

    def texto(self, i: int, j: int, txt: str, color=TXT, dy: float = -0.12, escala: float | None = None) -> Text:
        return Text(txt, color=color).scale(escala or self.escala * 0.85).move_to(self.c(i, j) + UP * dy)


def barra9(x0: float, x1: float, y: float, alto: float = 0.5, color=C0, opacidad: float = 0.45) -> Rectangle:
    """Barra horizontal de x0 a x1 (una fila de la tabla «estirada»)."""
    return Rectangle(width=x1 - x0, height=alto, color=color, stroke_width=3).set_fill(color, opacidad) \
        .move_to([(x0 + x1) / 2, y, 0])


def umbral9(C: Campanas9, r: float, alto: float = 3.5, color=ESTIMACION, rotulo: str | None = "Umbral") -> VGroup:
    """Marca vertical del umbral sobre las campanas (`.linea`, `.rot`)."""
    l = Line(C.p(r), C.p(r) + UP * alto, color=color, stroke_width=4)
    g = VGroup(l)
    g.linea, g.rot = l, None
    if rotulo:
        g.rot = Text(rotulo, color=color).scale(0.42).next_to(l, UP, buff=0.1)
        g.add(g.rot)
    return g


def cota9(p_a, p_b, texto: str, color=INK, escala: float = 0.42) -> VGroup:
    """Doble flecha entre dos puntos con un texto debajo (`.flecha`, `.txt`)."""
    fl = DoubleArrow(p_a, p_b, buff=0, color=color, stroke_width=3, tip_length=0.15,
                     max_tip_length_to_length_ratio=0.35)
    t = Text(texto, color=color).scale(escala).next_to(fl, DOWN, buff=0.12)
    g = VGroup(fl, t)
    g.flecha, g.txt = fl, t
    return g


class Barras9:
    """Barras verticales de error, sin armar: la escena entra cada pieza cuando toca.
    `.base`, `.barras[i]`, `.vals[i]`, `.rots[i]`."""

    def __init__(self, valores, rotulos, colores, xs, base_y: float = -2.6, esc: float = 10.0,
                 ancho: float = 1.4, escala: float = 0.45, textos=None):
        self.barras, self.vals, self.rots = [], [], []
        for k, (v, r, c, x) in enumerate(zip(valores, rotulos, colores, xs)):
            h = max(v * esc, 0.04)
            b = Rectangle(width=ancho, height=h, color=c, stroke_width=3).set_fill(c, 0.5)
            b.move_to([x, base_y + h / 2, 0])
            self.barras.append(b)
            txt = textos[k] if textos else num(v, 3)
            self.vals.append(Text(txt, color=TXT).scale(escala).next_to(b, UP, buff=0.14))
            self.rots.append(Text(r, color=INK).scale(escala).move_to([x, base_y - 0.38, 0]))
        self.base = Line([min(xs) - ancho, base_y, 0], [max(xs) + ancho, base_y, 0], color=INK, stroke_width=2.4)


def vpp9(p, sens: float = 0.99, fp: float = 0.05):
    """Valor predictivo positivo del test médico con prevalencia p."""
    p = np.asarray(p, dtype=float)
    return sens * p / (sens * p + fp * (1 - p))


class CurvaVPP9:
    """Plano del valor predictivo positivo contra la prevalencia (eje horizontal logarítmico).
    `.ejes`, `.etq` (números y títulos), `pt(p)`, `curva()`, `punto(p)`."""

    PREV = (0.001, 0.01, 0.1, 0.5)
    TXT_PREV = ("0,1 %", "1 %", "10 %", "50 %")

    def __init__(self, x0: float = -4.6, x1: float = 4.4, y0: float = -2.6, y1: float = 2.2,
                 lp0: float = -3.3, lp1: float = float(np.log10(0.6)), etiquetas: bool = True, escala: float = 0.42):
        self.x0, self.x1, self.y0, self.y1, self.lp0, self.lp1 = x0, x1, y0, y1, lp0, lp1
        self.ejes = VGroup(Line([x0, y0, 0], [x1 + 0.2, y0, 0], color=INK, stroke_width=2.4),
                           Line([x0, y0, 0], [x0, y1 + 0.2, 0], color=INK, stroke_width=2.4))
        self.etq = VGroup()
        if etiquetas:
            for p, t in zip(self.PREV, self.TXT_PREV):
                self.etq.add(Text(t, color=INK).scale(escala).move_to([self.x(p), y0 - 0.32, 0]))
            for v, t in ((0, "0"), (0.5, "50 %"), (1, "100 %")):
                m = Text(t, color=INK).scale(escala)
                self.etq.add(m.move_to([x0 - 0.2 - m.width / 2, self.y(v), 0]))
            self.etq.add(Text("Prevalencia", color=INK).scale(escala).move_to([x1 - 0.7, y0 - 0.78, 0]))
            tv = Text("Valor predictivo", color=INK).scale(escala)
            self.etq.add(tv.move_to([x0 + tv.width / 2, y1 + 0.55, 0]))

    def x(self, p):
        return self.x0 + (np.log10(p) - self.lp0) / (self.lp1 - self.lp0) * (self.x1 - self.x0)

    def y(self, v):
        return self.y0 + np.asarray(v, dtype=float) * (self.y1 - self.y0)

    def pt(self, p) -> np.ndarray:
        return np.array([float(self.x(p)), float(self.y(vpp9(p))), 0.0])

    def curva(self, color=ESTIMACION, ancho: float = 4.0) -> VMobject:
        ps = np.logspace(self.lp0, self.lp1, 140)
        return traza(self.x(ps), self.y(vpp9(ps)), color, ancho)

    def punto(self, p, color=ESTIMACION, radio: float = 0.09) -> Dot:
        return Dot(self.pt(p), radius=radio, color=color)


def monton9(n: int, centro=(0.0, 0.0), radio: float = 2.0, color=C0, r_punto: float = 0.045,
            semilla: int = 4) -> VGroup:
    """Montón de `n` puntos en forma de media luna apoyada en `centro` (la base)."""
    rng = np.random.default_rng(semilla)
    pts = []
    while len(pts) < n:
        x, y = rng.uniform(-1, 1), rng.uniform(0, 1)
        if x * x + y * y <= 1:
            pts.append(Dot([centro[0] + x * radio, centro[1] + y * radio * 0.75 + r_punto, 0],
                           radius=r_punto, color=color))
    return VGroup(*pts)
