"""Piezas del capítulo 9, episodio 4 («La curva de todos los umbrales»).

Módulo aparte (como `figuras_c9e1.py`) para no pisar `figuras.py` cuando
varias sesiones trabajan a la vez. Las escenas lo importan:

    from comun.escena import *
    from comun.figuras_c9e4 import *

Las dos campanas son las del capítulo (`Campanas9`: el cero en 0 V, el uno en
2 V, desvío 1). Con el umbral en u, la falsa alarma es Q(u) y la detección
Q(u − d), con d = 2 la separación en desvíos; la pendiente de la curva ROC en
ese punto es la razón de verosimilitud en u, e^(d·u − d²/2) (e^(2u − 2) con d = 2).
"""
from __future__ import annotations

from math import erfc, sqrt

from manim import *

from comun.estilo import *
from comun.figuras_c9e1 import C0, C1, P0, P1, CRUCE9, Campanas9, casilla9

ROC = ESTIMACION      # la curva ROC (y el punto que la recorre)
FA = ERROR            # falsa alarma: cola de la campana del cero
DET = VERDE           # detección: cola de la campana del uno


def Q(x: float) -> float:
    """La función cu: área de la cola derecha de la campana estándar a partir de x."""
    return 0.5 * erfc(x / sqrt(2))


def Qinv(p: float) -> float:
    """Inversa de la función cu: el x cuya cola derecha vale p."""
    from statistics import NormalDist
    p = min(max(p, 1e-9), 1 - 1e-9)
    return NormalDist().inv_cdf(1 - p)


def pd_de_fa9(fa: float, m: float = 2.0, s: float = 1.0) -> float:
    """Detección en función de la falsa alarma (campana del uno en m, desvío s)."""
    return Q((Qinv(fa) - m) / s)


PLANO_C = dict(origen=(-2.6, -2.6), lado=5.2)    # el plano solo, centrado


def lam9(u: float, d: float = 2.0) -> float:
    """Razón de verosimilitud f₁/f₀ en u, con las campanas en 0 y d (desvío 1)."""
    return float(np.exp(d * u - d * d / 2))


def roc9(u: float, d: float = 2.0) -> tuple[float, float]:
    """Punto (falsa alarma, detección) del umbral u."""
    return Q(u), Q(u - d)


def campanas_izq9() -> Campanas9:
    """Las campanas en el panel izquierdo (el plano de la ROC va a la derecha)."""
    return Campanas9(centro=(-3.75, -1.55), ancho=6.0, alto=5.6, r_rango=(-3.0, 5.0), v_max=0.45)


def eje_izq9(C: Campanas9, marcas=(0, 1, 2), escala: float = 0.45) -> VGroup:
    """Eje de las campanas con «r (V)» debajo, a la derecha (arriba lo pisarían las colas)."""
    g = C.eje(marcas, rotulo=False, escala=escala)
    g.rot = MathTex(r"r\ (\mathrm{V})", color=INK).scale(0.55).move_to(C.p(4.3) + DOWN * 0.34)
    g.add(g.rot)
    return g


class PlanoRoc9(VGroup):
    """Plano de la curva ROC: falsa alarma en horizontal y detección en vertical, de 0 a 1.

    `.ejes` (los dos ejes y el marco tenue), `.rot_x`, `.rot_y`, `.nums`;
    `p(fa, pd)` da el punto de pantalla; `curva(d)` la ROC de separación d;
    `diagonal()`; `tangente(u, d, largo)` la recta tangente en el umbral u;
    `recta(pendiente, por, largo)` una recta que pasa por el punto `por` (fa, pd),
    recortada al cuadrado.
    """

    def __init__(self, origen=(1.25, -2.15), lado: float = 4.6, escala: float = 0.42, rotulos: bool = True):
        super().__init__()
        self.o = np.array([origen[0], origen[1], 0.0])
        self.lado = lado
        ex = Line(self.o, self.o + RIGHT * (lado + 0.25), color=INK, stroke_width=2.5)
        ey = Line(self.o, self.o + UP * (lado + 0.25), color=INK, stroke_width=2.5)
        marco = VGroup(Line(self.p(0, 1), self.p(1, 1)), Line(self.p(1, 0), self.p(1, 1)))
        marco.set_stroke(INK, 1.5, opacity=0.35)
        self.ejes = VGroup(ex, ey, marco)
        self.nums = VGroup(
            Text("0", color=INK).scale(escala).move_to(self.p(0, 0) + DL * 0.25),
            Text("1", color=INK).scale(escala).move_to(self.p(1, 0) + DOWN * 0.28),
            Text("1", color=INK).scale(escala).move_to(self.p(0, 1) + LEFT * 0.25))
        self.add(self.ejes, self.nums)
        self.rot_x = Text("Falsa alarma", color=FA).scale(escala * 1.1)
        self.rot_x.next_to(self.p(0.5, 0), DOWN, buff=0.22)
        self.rot_y = Text("Detección", color=DET).scale(escala * 1.1)
        self.rot_y.next_to(self.p(0, 1), UP, buff=0.18).align_to(self.p(0, 1), LEFT).shift(LEFT * 0.2)
        if rotulos:
            self.add(self.rot_x, self.rot_y)

    def p(self, fa: float, pd: float) -> np.ndarray:
        return self.o + RIGHT * fa * self.lado + UP * pd * self.lado

    def curva(self, d: float = 2.0, color=ROC, ancho: float = 5.0, u0: float = 6.0, u1: float = -4.0,
              n: int = 140) -> VMobject:
        """La ROC de dos campanas separadas d desvíos, del umbral u0 al u1 (de (0, 0) a (1, 1))."""
        us = np.linspace(u0, u1, n)
        pts = [self.p(*roc9(u, d)) for u in us]
        m = VMobject(stroke_color=color, stroke_width=ancho)
        m.set_points_as_corners(pts)
        return m

    def curva_bin(self, m: float, s: float = 1.0, color=ROC, ancho: float = 5.0, n: int = 220) -> VMobject:
        """ROC de dos campanas con distinto desvío: la del uno centrada en m con desvío s
        (con s ≠ 1 puede cruzarse con otra ROC)."""
        us = np.linspace(max(6.0, m + 5 * s), min(-4.0, m - 5 * s), n)
        pts = [self.p(Q(u), Q((u - m) / s)) for u in us]
        mob = VMobject(stroke_color=color, stroke_width=ancho)
        mob.set_points_as_corners(pts)
        return mob

    def entre(self, f_arriba, f_abajo, fa0: float, fa1: float, color, opacidad: float = 0.25,
              n: int = 60) -> Polygon:
        """Zona entre dos curvas pd = f(fa), para fa entre fa0 y fa1."""
        xs = np.linspace(fa0, fa1, n)
        pts = [self.p(x, f_arriba(x)) for x in xs] + [self.p(x, f_abajo(x)) for x in xs[::-1]]
        return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)

    def diagonal(self, color=INK, ancho: float = 3.0) -> Line:
        return DashedLine(self.p(0, 0), self.p(1, 1), color=color, stroke_width=ancho, dash_length=0.12)

    def recta(self, pendiente: float, por, largo: float | None = None, color=TXT, ancho: float = 3.5) -> Line:
        """Recta de pendiente dada por el punto `por` = (fa, pd), recortada al cuadrado [0, 1]²
        (o de largo `largo`, en unidades del plano, centrada en el punto)."""
        x0, y0 = por
        if largo is not None:
            dx = largo / 2 / np.sqrt(1 + pendiente ** 2)
            a, b = (x0 - dx, y0 - pendiente * dx), (x0 + dx, y0 + pendiente * dx)
        else:
            # cortes con los bordes del cuadrado
            cand = []
            for x in (0.0, 1.0):
                y = y0 + pendiente * (x - x0)
                if -1e-9 <= y <= 1 + 1e-9:
                    cand.append((x, y))
            for y in (0.0, 1.0):
                if pendiente != 0:
                    x = x0 + (y - y0) / pendiente
                    if -1e-9 <= x <= 1 + 1e-9:
                        cand.append((x, y))
            cand = sorted(set((round(a, 6), round(b, 6)) for a, b in cand))
            if len(cand) < 2:
                cand = [(x0 - 0.1, y0 - 0.1 * pendiente), (x0 + 0.1, y0 + 0.1 * pendiente)]
            a, b = cand[0], cand[-1]
        return Line(self.p(*a), self.p(*b), color=color, stroke_width=ancho)

    def tangente(self, u: float, d: float = 2.0, largo: float = 0.5, color=TXT, ancho: float = 3.5) -> Line:
        return self.recta(lam9(u, d), roc9(u, d), largo=largo, color=color, ancho=ancho)

    def punto(self, fa: float, pd: float, color=ROC, radio: float = 0.09) -> Dot:
        return Dot(self.p(fa, pd), radius=radio, color=color)


class Barrido9:
    """Umbral móvil sobre las campanas, con sus dos colas y el punto que deja en la ROC.

        B = Barrido9(C, P, u=3.0)
        self.add(*B.todo())                 # umbral, colas y punto (always_redraw)
        self.play(B.u.animate.set_value(1.0))
        rastro = B.rastro()                 # la curva que va dejando (desde el primer valor)
    """

    def __init__(self, C: Campanas9, P: PlanoRoc9 | None, u: float = 3.0, d: float = 2.0, alto: float = 2.9,
                 colas: bool = True):
        self.C, self.P, self.d = C, P, d
        self.u = ValueTracker(u)
        self.u_inicio = u
        self.linea = always_redraw(lambda: Line(
            C.p(self._uc()) + DOWN * 0.1, C.p(self._uc()) + UP * alto, color=ROC, stroke_width=4))
        self.cola0 = always_redraw(lambda: C.area(0, 1, self._uc(), C.r1, FA, 0.5))
        self.cola1 = always_redraw(lambda: C.area(d, 1, self._uc(), C.r1, DET, 0.4))
        self.colas = VGroup(self.cola1, self.cola0) if colas else VGroup()
        self.pt = always_redraw(lambda: P.punto(*roc9(self.u.get_value(), d))) if P is not None else VGroup()

    def _uc(self) -> float:
        """El umbral recortado al lienzo (más allá, la línea queda en el borde)."""
        return float(np.clip(self.u.get_value(), self.C.r0, self.C.r1))

    def todo(self):
        return [self.colas, self.linea, self.pt]

    def rastro(self, color=ROC, ancho: float = 5.0) -> VMobject:
        """Curva ROC entre el valor inicial del umbral y el actual (se redibuja sola)."""
        P, d = self.P, self.d

        def f():
            u0, u1 = self.u_inicio, self.u.get_value()
            if abs(u1 - u0) < 0.02:
                return VMobject()
            return P.curva(d, color, ancho, u0=u0, u1=u1, n=max(8, int(abs(u1 - u0) * 18)))
        return always_redraw(f)

    def fresco(self):
        """Redibuja las piezas con el umbral actual. Llamarlo antes de un `FadeIn`: una pieza con
        `always_redraw` que todavía no está en escena conserva la forma de cuando se creó."""
        for m in (self.linea, self.cola0, self.cola1, self.pt):
            m.update()
        return self

    def quieto(self):
        """Congela las piezas animadas (saca los updaters) para poder moverlas o atenuarlas."""
        for m in (self.linea, self.cola0, self.cola1, self.pt):
            m.clear_updaters()


def rotulo_par9(fa: str, pd: str, escala: float = 0.42) -> VGroup:
    """«(0,16; 0,84)» con la falsa alarma en rojo y la detección en verde."""
    g = VGroup(Text("(", color=TXT), Text(fa, color=FA), Text(";", color=TXT), Text(pd, color=DET),
               Text(")", color=TXT)).scale(escala).arrange(RIGHT, buff=0.06)
    g[2].shift(DOWN * 0.03)
    return g


def triangulo9(P: PlanoRoc9, por, dx: float, pendiente: float, color_h=FA, color_v=DET,
               ancho: float = 4.0) -> VGroup:
    """Triángulo de pendiente en el plano: cateto horizontal `dx` desde `por` y vertical `pendiente · dx`.
    `.h`, `.v`."""
    x0, y0 = por
    a, b, c = P.p(x0, y0), P.p(x0 + dx, y0), P.p(x0 + dx, y0 + pendiente * dx)
    h = Line(a, b, color=color_h, stroke_width=ancho)
    v = Line(b, c, color=color_v, stroke_width=ancho)
    g = VGroup(h, v)
    g.h, g.v = h, v
    return g


def mochila9(centro=(0.0, 0.0), lado: float = 0.62, escala: float = 0.36) -> VGroup:
    """La mochila del episodio 3, en pequeño: cinco niveles con su «Rinde / Cuesta».
    `.cas[i]` (nivel i + 1), `.vals[i]`, `.rot`."""
    valores = ["0,125", "0,33", "1", "3", "8"]
    cas, vals = VGroup(), VGroup()
    for i, v in enumerate(valores):
        c = RoundedRectangle(corner_radius=0.06, width=lado, height=lado, color=INK, stroke_width=2.5)
        c.set_fill(INK, 0.1)
        cas.add(c)
    cas.arrange(RIGHT, buff=0.1).move_to([centro[0], centro[1], 0])
    for i, v in enumerate(valores):
        vals.add(Text(v, color=TXT).scale(escala).move_to(cas[i]))
    niv = VGroup(*[Text(str(i + 1), color=INK).scale(escala * 0.85).next_to(cas[i], UP, buff=0.08)
                   for i in range(5)])
    rot = Text("Rinde / Cuesta", color=ESTIMACION).scale(escala).next_to(cas, DOWN, buff=0.14)
    g = VGroup(cas, vals, niv, rot)
    g.cas, g.vals, g.niv, g.rot = cas, vals, niv, rot
    return g


def estrella9(color=VERDE, radio: float = 0.22) -> Star:
    return Star(n=5, outer_radius=radio, inner_radius=radio * 0.45, color=color, stroke_width=2).set_fill(color, 0.9)


def tarjeta9(texto: str, color=INK, ancho: float = 3.4, alto: float = 0.75, escala: float = 0.45) -> VGroup:
    """Tarjeta de texto (alias de `casilla9`)."""
    return casilla9(texto, color, ancho=ancho, alto=alto, escala=escala)
