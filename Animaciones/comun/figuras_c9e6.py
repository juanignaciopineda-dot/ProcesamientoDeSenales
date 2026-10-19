"""Piezas del capítulo 9, episodio 6 («Decidir con datos de verdad»).

Módulo aparte (como `figuras_c9e4.py`) para no pisar `figuras.py` cuando
varias sesiones trabajan a la vez. Las escenas lo importan:

    from comun.escena import *
    from comun.figuras_c9e6 import *

Trae todo lo del E4 (`PlanoRoc9`, `campanas_izq9`, `Q`, `roc9`…) y suma:
- `CASOS6`: los ocho casos del episodio (puntuación y signo), de mayor a menor;
- `ficha6` y `columna6`: las fichas «+» / «−» con su puntuación;
- `Escalera6`: la ROC empírica de una tira de signos sobre un `PlanoRoc9`;
- `escalera_n6`: la escalera de n casos simulados con las campanas de siempre;
- `caja_detector6`, `rejilla6` (mil pruebas), `Histograma6` (falsas alarmas
  en mil pruebas), `tarjeta6`, `aviso6` y la grabación de ruido `ruido6`.
"""
from __future__ import annotations

from math import exp, factorial

from manim import *

from comun.estilo import *
from comun.figuras import traza
from comun.figuras_c9e1 import C0, C1, Campanas9, casilla9
from comun.figuras_c9e4 import (DET, FA, PLANO_C, Q, Qinv, ROC, Barrido9, PlanoRoc9, campanas_izq9, eje_izq9,
                                lam9, pd_de_fa9, roc9, rotulo_par9, tarjeta9)

POS, NEG = C1, C0          # positivo (H₁) en azul, negativo (H₀) en magenta

# los ocho casos, de mayor a menor puntuación: + + − + − + − −
CASOS6 = [(0.95, 1), (0.85, 1), (0.75, 0), (0.65, 1), (0.55, 0), (0.40, 1), (0.30, 0), (0.15, 0)]
SIGNOS6 = [s for _, s in CASOS6]
# orden revuelto en que entran al principio (índices de CASOS6)
REVUELTO6 = [6, 0, 3, 7, 1, 4, 2, 5]

FA_RARA6 = Q(3.0)          # 0,00135


def ficha6(signo: int | None, punt: float | None = None, lado: float = 0.62, escala: float = 0.4) -> VGroup:
    """Ficha de un caso: casilla con «+» (azul) o «−» (magenta) y su puntuación a la derecha.
    `signo=None` da una ficha gris (caso sin etiqueta). `.marco`, `.signo`, `.num`."""
    col = INK if signo is None else (POS if signo else NEG)
    r = RoundedRectangle(corner_radius=0.1, width=lado, height=lado, color=col, stroke_width=3)
    r.set_fill(col, 0.2)
    s = Text("" if signo is None else ("+" if signo else "−"), color=TXT, weight=BOLD).scale(0.6 * lado / 0.62)
    s.move_to(r)
    g = VGroup(r, s)
    g.marco, g.signo = r, s
    g.num = None
    if punt is not None:
        n = Text(num(punt), color=TXT).scale(escala).next_to(r, RIGHT, buff=0.14)
        g.add(n)
        g.num = n
    return g


def columna6(casos=CASOS6, centro=(-5.0, 0.0), paso: float = 0.78, lado: float = 0.62,
             escala: float = 0.4) -> VGroup:
    """Columna de fichas, de arriba (mayor puntuación) a abajo. `.fichas[i]`, `y(i)` (altura de la ficha i)
    y `entre(i)` (la altura del hueco por debajo de la ficha i; `entre(-1)` es por encima de la primera)."""
    fichas = VGroup(*[ficha6(s, p, lado, escala) for p, s in casos])
    for i, f in enumerate(fichas):
        f.move_to([centro[0], centro[1] + (len(casos) - 1) / 2 * paso - i * paso, 0])
        f.shift(RIGHT * (f.get_center()[0] - f.marco.get_center()[0]))
    g = VGroup(*fichas)
    g.fichas = fichas
    y0 = centro[1] + (len(casos) - 1) / 2 * paso
    g.y = lambda i: y0 - i * paso
    g.entre = lambda i: y0 - i * paso - paso / 2
    return g


def tira6(signos=SIGNOS6, centro=(0.0, 0.0), lado: float = 0.5, buff: float = 0.12) -> VGroup:
    """Tira horizontal de signos «+ + − + − + − −» (sin puntuación). `.fichas`."""
    g = VGroup(*[ficha6(s, None, lado) for s in signos]).arrange(RIGHT, buff=buff)
    g.move_to([centro[0], centro[1], 0])
    g.fichas = g
    return g


def camino6(signos=SIGNOS6) -> list[tuple[float, float]]:
    """Vértices de la escalera: cada «+» sube 1/nº de positivos, cada «−» avanza 1/nº de negativos."""
    npos, nneg = sum(signos), len(signos) - sum(signos)
    x = y = 0.0
    pts = [(0.0, 0.0)]
    for s in signos:
        if s:
            y += 1 / npos
        else:
            x += 1 / nneg
        pts.append((x, y))
    return pts


class Escalera6:
    """La ROC empírica de una tira de signos sobre un plano `P`.

        E = Escalera6(P)
        E.tramo(i)          # el tramo i (0..7) como Line ámbar
        E.todo()            # la escalera entera como VMobject
        E.columnas()        # los rectángulos bajo cada tramo horizontal (las columnas del área)
        E.area()            # el área bajo la escalera
    """

    def __init__(self, P: PlanoRoc9, signos=SIGNOS6, color=ROC, ancho: float = 6.0):
        self.P, self.signos, self.color, self.ancho = P, list(signos), color, ancho
        self.pts = camino6(signos)

    def tramo(self, i: int) -> Line:
        a, b = self.pts[i], self.pts[i + 1]
        return Line(self.P.p(*a), self.P.p(*b), color=self.color, stroke_width=self.ancho)

    def todo(self, color=None, ancho=None) -> VMobject:
        m = VMobject(stroke_color=color or self.color, stroke_width=ancho or self.ancho)
        m.set_points_as_corners([self.P.p(*q) for q in self.pts])
        return m

    def columnas(self, color=ROC, opacidad: float = 0.35) -> VGroup:
        """Una columna por cada «−»: de ancho 1/nº de negativos y alto la detección a esa altura."""
        cols = VGroup()
        for i, s in enumerate(self.signos):
            if s:
                continue
            (x0, y), (x1, _) = self.pts[i], self.pts[i + 1]
            r = Polygon(self.P.p(x0, 0), self.P.p(x1, 0), self.P.p(x1, y), self.P.p(x0, y),
                        stroke_color=color, stroke_width=1.5, stroke_opacity=0.8).set_fill(color, opacidad)
            cols.add(r)
        return cols

    def area(self, color=ROC, opacidad: float = 0.3) -> Polygon:
        pts = [self.P.p(*q) for q in self.pts] + [self.P.p(1, 0)]
        return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)


def escalera_n6(P: PlanoRoc9, n: int, semilla: int = 3, d: float = 2.0, color=ROC, ancho: float = 4.0) -> VMobject:
    """Escalera de n casos simulados (n/2 de cada campana, desvío 1, centros 0 y d)."""
    rng = np.random.default_rng(semilla)
    m = n // 2
    p = np.concatenate([rng.normal(d, 1, m), rng.normal(0, 1, m)])
    s = np.concatenate([np.ones(m, int), np.zeros(m, int)])
    orden = np.argsort(-p)
    pts = camino6(list(s[orden]))
    if len(pts) > 600:                       # basta con las esquinas cada tanto para dibujar
        idx = np.unique(np.linspace(0, len(pts) - 1, 600).astype(int))
        pts = [pts[i] for i in idx]
    mob = VMobject(stroke_color=color, stroke_width=ancho)
    mob.set_points_as_corners([P.p(*q) for q in pts])
    return mob


def area_curva6(P: PlanoRoc9, f=None, color=ROC, opacidad: float = 0.28, n: int = 120) -> Polygon:
    """Área bajo una curva pd = f(fa) en el plano (por defecto, la ROC de las dos campanas)."""
    f = f or (lambda x: pd_de_fa9(x))
    xs = np.concatenate([np.geomspace(1e-5, 0.05, 40), np.linspace(0.05, 1, n)])
    pts = [P.p(0, 0)] + [P.p(x, min(1.0, f(x))) for x in xs] + [P.p(1, 0)]
    return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)


def caja_detector6(ancho: float = 2.4, alto: float = 1.2, escala: float = 0.5, color=INK) -> VGroup:
    """Caja «Detector» con una luz a la derecha. `.caja`, `.rot`, `.luz`."""
    c = RoundedRectangle(corner_radius=0.16, width=ancho, height=alto, color=color, stroke_width=3.5)
    c.set_fill(color, 0.12)
    rot = Text("Detector", color=TXT).scale(escala).move_to(c).shift(LEFT * 0.25)
    luz = Circle(radius=0.14, color=INK, stroke_width=2.5).set_fill(INK, 0.3)
    luz.move_to(c.get_right() + LEFT * 0.35)
    g = VGroup(c, rot, luz)
    g.caja, g.rot, g.luz = c, rot, luz
    return g


def rejilla6(n: int = 1000, columnas: int = 40, centro=(0.0, 0.0), ancho: float = 6.0,
             color=INK, radio: float = 0.035) -> VGroup:
    """Rejilla de n puntos (mil pruebas): filas de `columnas` puntos."""
    filas = int(np.ceil(n / columnas))
    paso = ancho / (columnas - 1)
    pts = VGroup()
    for k in range(n):
        i, j = divmod(k, columnas)
        pts.add(Dot([centro[0] - ancho / 2 + j * paso, centro[1] + (filas - 1) / 2 * paso - i * paso, 0],
                    radius=radio, color=color))
    return pts


def poisson6(k: int, lam: float) -> float:
    return exp(-lam) * lam ** k / factorial(k)


class Histograma6(VGroup):
    """Histograma de cuántas falsas alarmas salen en mil pruebas (Poisson de media 1,35):
    barras 0, 1, 2, 3 y 4+. `.base`, `.barras[i]`, `.nums[i]` (debajo), `.vals[i]` (porcentaje encima)."""

    def __init__(self, centro=(3.6, -1.0), ancho: float = 5.0, alto: float = 3.6, lam: float = 1000 * FA_RARA6,
                 escala: float = 0.42):
        super().__init__()
        ps = [poisson6(k, lam) for k in range(4)]
        ps.append(1 - sum(ps))
        self.ps = ps
        c = np.array([centro[0], centro[1], 0.0])
        paso = ancho / 5
        self.base = Line(c + LEFT * ancho / 2 + DOWN * alto / 2, c + RIGHT * ancho / 2 + DOWN * alto / 2,
                         color=INK, stroke_width=2.5)
        self.barras, self.nums, self.vals = VGroup(), VGroup(), VGroup()
        tope = max(ps)
        for i, p in enumerate(ps):
            x = c[0] - ancho / 2 + paso * (i + 0.5)
            h = alto * 0.85 * p / tope
            b = Rectangle(width=paso * 0.7, height=h, stroke_color=ERROR, stroke_width=2).set_fill(ERROR, 0.45)
            b.move_to([x, c[1] - alto / 2 + h / 2, 0])
            self.barras.add(b)
            self.nums.add(Text("4+" if i == 4 else str(i), color=INK).scale(escala).move_to([x, c[1] - alto / 2 - 0.3, 0]))
            self.vals.add(Text(f"{round(100 * p)} %", color=TXT).scale(escala).next_to(b, UP, buff=0.1))
        self.add(self.base, self.barras, self.nums, self.vals)


def tarjeta6(texto: str, color=INK, ancho: float = 3.6, alto: float = 0.8, escala: float = 0.46) -> VGroup:
    """Tarjeta de texto (casilla del capítulo). `.marco`, `.txt`."""
    return casilla9(texto, color, ancho=ancho, alto=alto, escala=escala)


def aviso6(color=ESTIMACION, lado: float = 0.7) -> VGroup:
    """Triángulo de aviso con «!»."""
    t = Triangle(color=color, stroke_width=4).scale(lado / 2).set_fill(color, 0.15)
    e = Text("!", color=color, weight=BOLD).scale(0.55 * lado / 0.7).move_to(t.get_center() + DOWN * lado * 0.08)
    return VGroup(t, e)


def ruido6(centro=(0.0, 0.0), ancho: float = 8.0, alto: float = 0.9, n: int = 160, semilla: int = 1,
           color=RUIDO, ancho_trazo: float = 2.5, opacidad: float = 1.0) -> VMobject:
    """Una grabación de ruido (con un poco de memoria, para que se vea continua)."""
    rng = np.random.default_rng(semilla)
    v = np.zeros(n)
    e = rng.normal(0, 1, n)
    for k in range(1, n):
        v[k] = 0.6 * v[k - 1] + e[k]
    v = v / np.max(np.abs(v)) * alto / 2
    x = np.linspace(centro[0] - ancho / 2, centro[0] + ancho / 2, n)
    return traza(x, centro[1] + v, color, ancho_trazo, opacidad)


def fila_barras6(n: int = 24, centro=(0.0, 0.0), ancho: float = 9.0, alto: float = 1.2, semilla: int = 4,
                 color=MEDIDA) -> VGroup:
    """Señal entera muestra a muestra: barras cian de altura positiva con un poco de ruido. `.barras`, `.base`."""
    rng = np.random.default_rng(semilla)
    paso = ancho / n
    base = Line([centro[0] - ancho / 2, centro[1], 0], [centro[0] + ancho / 2, centro[1], 0], color=INK, stroke_width=2)
    barras = VGroup()
    for k in range(n):
        h = alto * (0.55 + 0.35 * rng.normal())
        h = float(np.clip(h, 0.15, alto))
        b = Rectangle(width=paso * 0.55, height=h, stroke_width=0).set_fill(color, 0.85)
        b.move_to([centro[0] - ancho / 2 + paso * (k + 0.5), centro[1] + h / 2, 0])
        barras.add(b)
    g = VGroup(base, barras)
    g.base, g.barras = base, barras
    return g
