"""Piezas del capítulo 8, episodio 3 (la carpa, el termómetro y la mejor recta).

Van en un módulo aparte (y no en `figuras.py`) para no pisarse con las demás sesiones que editan ese archivo.
Las escenas del episodio lo importan con `from comun.figuras_cap08_e3 import *`.
"""
from manim import *
import numpy as np

from comun.estilo import *
from comun.figuras import traza


def puntos_carpa_e3(n: int = 60, semilla: int = 5):
    """n puntos uniformes dentro de la carpa (triángulo de base 0–2 y pico (1, 1)). Devuelve `(xs, ys)`."""
    rng = np.random.default_rng(semilla)
    xs, ys = [], []
    while len(xs) < n:
        x, y = rng.uniform(0, 2), rng.uniform(0, 1)
        if y <= min(x, 2 - x):
            xs.append(x)
            ys.append(y)
    return np.array(xs), np.array(ys)


class CarpaE3:
    """La carpa del capítulo 8: ejes (x de 0 a 2,4; y de 0 a 1,2) y el triángulo de base 0–2 y pico (1, 1).

    Atributos (sueltos, no es un grupo: cada escena los agrega o los anima por separado):
    `.ax` (los ejes), `.et` (las letras x e y), `.tri` (el triángulo), `.nums` (0, 1, 2 del eje x) y `.n_y1`.
    `p(x, y)` da el punto en pantalla; `techo(x)` la altura de la carpa en x; `rebanada(x)` el trozo de la
    vertical en x que cae dentro; `corte(x)` la línea cian discontinua; `centro(x)` un punto ámbar en el medio
    de la rebanada; `base()` la lista de piezas fijas."""

    def __init__(self, centro=(0.0, -0.3), ancho: float = 8.4, alto: float = 3.6):
        self.ax, self.et = ejes((0, 2.4, 1), (0, 1.2, 1), ancho=ancho, alto=alto, x_label="x", y_label="y")
        viejo = self.ax.get_center().copy()
        self.ax.move_to([centro[0], centro[1], 0])
        self.et.shift(self.ax.get_center() - viejo)
        self.et[0].set_color(MEDIDA)
        self.et[1].set_color(SENAL)
        self.tri = Polygon(self.p(0, 0), self.p(1, 1), self.p(2, 0), color=SENAL, stroke_width=4)
        self.tri.set_fill(SENAL, 0.14)
        self.nums = VGroup(*[Text(str(v), color=INK).scale(0.42).move_to(self.p(v, 0) + DOWN * 0.3)
                             for v in (0, 1, 2)])
        self.n_y1 = Text("1", color=INK).scale(0.42).move_to(self.p(0, 1) + LEFT * 0.3)

    def p(self, x, y) -> np.ndarray:
        return self.ax.c2p(x, y)

    @staticmethod
    def techo(x: float) -> float:
        return float(min(x, 2 - x)) if 0 <= x <= 2 else 0.0

    def rebanada(self, x: float, color=SENAL, ancho: float = 8) -> Line:
        return Line(self.p(x, 0), self.p(x, self.techo(x)), color=color, stroke_width=ancho)

    def corte(self, x: float, color=MEDIDA) -> DashedLine:
        return DashedLine(self.p(x, 0), self.p(x, 1.12), color=color, stroke_width=3)

    def centro(self, x: float, color=ESTIMACION, radio: float = 0.12) -> Dot:
        return Dot(self.p(x, self.techo(x) / 2), radius=radio, color=color)

    def base(self) -> list:
        return [self.ax, self.et, self.tri, self.nums, self.n_y1]


class NubeRhoE3(VGroup):
    """Nube de puntos estandarizados (a, b) con correlación `rho`, sobre una cruz de ejes. Los puntos se mueven
    de forma continua al cambiar `rho` (`colocar(rho)`, para un updater con un ValueTracker).

    `.ejes`, `.pts` (lista de Dots); `p(a, b)` → pantalla; `recta(rho)` la recta de b sobre a (b = rho·a);
    `recta_inv(rho)` la de a sobre b (a = rho·b), es decir la «recta al revés»."""

    def __init__(self, centro=(0.0, 0.0), sx: float = 1.4, sy: float = 1.4, n: int = 48, semilla: int = 7,
                 rho: float = 0.0, color=TXT, radio: float = 0.06):
        super().__init__()
        rng = np.random.default_rng(semilla)
        self.a = np.clip(rng.normal(0, 1, n), -2.3, 2.3)
        self.z = np.clip(rng.normal(0, 1, n), -2.3, 2.3)
        self.c = np.array([centro[0], centro[1], 0.0])
        self.sx, self.sy = sx, sy
        self.ejes = VGroup(Line(self.p(-2.7, 0), self.p(2.7, 0), color=INK, stroke_width=2),
                           Line(self.p(0, -2.7), self.p(0, 2.7), color=INK, stroke_width=2))
        self.pts = [Dot(radius=radio, color=color, fill_opacity=0.85) for _ in range(n)]
        self.colocar(rho)
        self.add(self.ejes, *self.pts)

    def p(self, a, b) -> np.ndarray:
        return self.c + np.array([self.sx * a, self.sy * b, 0.0])

    def b(self, rho: float) -> np.ndarray:
        return rho * self.a + np.sqrt(max(0.0, 1 - rho * rho)) * self.z

    def colocar(self, rho: float) -> None:
        for d, a, b in zip(self.pts, self.a, self.b(rho)):
            d.move_to(self.p(a, b))

    def recta(self, rho: float, color=ESTIMACION, ancho: float = 5) -> Line:
        return Line(self.p(-2.5, -2.5 * rho), self.p(2.5, 2.5 * rho), color=color, stroke_width=ancho)

    def recta_inv(self, rho: float, color="#f2d04b", ancho: float = 5) -> Line:
        return Line(self.p(-2.5 * rho, -2.5), self.p(2.5 * rho, 2.5), color=color, stroke_width=ancho)


def carpa_mini_e3(centro=(0.0, 0.0), ancho: float = 2.4, alto: float = 1.3) -> VGroup:
    """La carpa en pequeño con su mejor recta (horizontal, a 1/3). `.tri`, `.recta`."""
    cx, cy = centro
    x0, y0 = cx - ancho / 2, cy - alto / 2
    tri = Polygon([x0, y0, 0], [x0 + ancho / 2, y0 + alto, 0], [x0 + ancho, y0, 0], color=SENAL, stroke_width=3)
    tri.set_fill(SENAL, 0.14)
    y3 = y0 + alto / 3
    recta = Line([x0 - 0.15, y3, 0], [x0 + ancho + 0.15, y3, 0], color=ESTIMACION, stroke_width=4)
    g = VGroup(tri, recta)
    g.tri, g.recta = tri, recta
    return g
