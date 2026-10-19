"""Piezas del capítulo 9, episodio 3 («Un número y un umbral»).

Módulo aparte (como `figuras_c9e1.py`) para no pisar `figuras.py` cuando
varias sesiones trabajan a la vez. Las escenas lo importan:

    from comun.escena import *
    from comun.figuras_c9e3 import *

Reutiliza las campanas del E1 (`Campanas9`: centros 0 y 2 V, desvío 1; el cero
en magenta `C0`, el uno en azul `C1`) y suma:
- `CampanasS9`: las mismas campanas con desvío a elección (escenas 07 a 09);
- `CurvaLambda9`: la gráfica de Λ(r) = e^(2r − 2) contra r, con su línea η;
- `TablaNiveles9`: las cinco casillas del detector de juguete (escenas 13 y 14);
- íconos `monedero9`, `mochila9`, `fibra9`, `cuaderno9`;
- `lrt9` y `caja_lrt9`: la caja «Λ(r) ≷ η».
"""
from __future__ import annotations

from manim import *

from comun.estilo import *
from comun.figuras import Lienzo, gaussiana, traza
from comun.figuras_c9e1 import (C0, C1, CRUCE9, P0, P1, Campanas9, balanza9, bit9, canal9, casilla9,
                                garabato9, rot_tex9)

ETA9 = P0 / P1                       # 2,33
LAMBDA = r"\Lambda(r)"


def lrt9(eta: str = r"\eta", escala: float = 1.0) -> MathTex:
    """«Λ(r) ≷ η» en tres piezas: `[0]` Λ(r) (cian), `[1]` ≷, `[2]` η (ámbar)."""
    return formula(LAMBDA, r"\gtrless", eta, escala=escala, colores={0: MEDIDA, 2: ESTIMACION})


def caja_lrt9(escala: float = 1.0, color=ESTIMACION) -> VGroup:
    """La caja del test de razón de verosimilitud: `.f` (la fórmula) y `.marco`."""
    f = lrt9(escala=escala)
    marco = RoundedRectangle(corner_radius=0.15, width=f.width + 0.7, height=f.height + 0.55,
                             color=color, stroke_width=4).set_fill(color, 0.08).move_to(f)
    g = VGroup(marco, f)
    g.f, g.marco = f, marco
    return g


class CampanasS9(Campanas9):
    """`Campanas9` con campanas de desvío cualquiera (centro `mu`, desvío `s`).

        C = CampanasS9(r_rango=(-5.5, 6), v_max=0.45)
        C.campana_s(0, 1, C0); C.campana_s(2, 2, C1)
    """

    @staticmethod
    def fs(mu: float, s: float, r, factor: float = 1.0):
        return factor * gaussiana(np.asarray(r, dtype=float), mu, s)

    def campana_s(self, mu: float, s: float, color, ancho: float = 4.0, factor: float = 1.0) -> VMobject:
        t = np.linspace(self.r0, self.r1, 220)
        return self.L.curva(t, self.fs(mu, s, t, factor), color, ancho)

    def area_s(self, mu: float, s: float, desde: float, hasta: float, color=ERROR,
               opacidad: float = 0.45) -> Polygon:
        t = np.linspace(max(desde, self.r0), min(hasta, self.r1), 90)
        v = self.fs(mu, s, t)
        pts = [self.p(t[0])] + [self.p(a, b) for a, b in zip(t, v)] + [self.p(t[-1])]
        return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)

    def punto_s(self, mu: float, s: float, r: float, color, radio: float = 0.09) -> Dot:
        return Dot(self.p(r, self.fs(mu, s, r)), radius=radio, color=color)


class CurvaLambda9:
    """Gráfica de Λ(r) = e^(2r − 2) contra r (escenas 06 y 15).

        G = CurvaLambda9(origen=(-5.6, -3.0), ancho=6.0, alto=5.2)
        G.ejes (VGroup: `.h`, `.v`, `.rot_h`, `.rot_v`), G.curva(), G.punto(1), G.linea(2.33)
    """

    def __init__(self, origen=(-5.6, -3.0), ancho: float = 6.0, alto: float = 5.2,
                 r_rango=(-0.6, 2.25), v_top: float = 9.0, escala: float = 1.0):
        self.r0, self.r1 = r_rango
        self.ox, self.oy = origen
        self.ancho, self.alto, self.v_top = ancho, alto, v_top
        self.escala = escala
        h = Arrow([self.ox, self.oy, 0], [self.ox + ancho + 0.3, self.oy, 0], color=INK, buff=0,
                  stroke_width=2.5, max_tip_length_to_length_ratio=0.04)
        v = Arrow([self.x(0), self.oy, 0], [self.x(0), self.oy + alto + 0.3, 0], color=INK, buff=0,
                  stroke_width=2.5, max_tip_length_to_length_ratio=0.04)
        rot_h = MathTex("r", color=INK).scale(0.65 * escala).next_to(h.get_end(), DOWN, buff=0.15)
        rot_v = MathTex(LAMBDA, color=MEDIDA).scale(0.65 * escala).next_to(v.get_end(), RIGHT, buff=0.15)
        nums = VGroup(*[Text(num(k), color=INK).scale(0.4 * escala).move_to(self.p(k) + DOWN * 0.3)
                        for k in (1, 2)])
        self.ejes = VGroup(h, v, rot_h, rot_v, nums)
        self.ejes.h, self.ejes.v, self.ejes.rot_h, self.ejes.rot_v, self.ejes.nums = h, v, rot_h, rot_v, nums

    @staticmethod
    def lam(r):
        return np.exp(2 * np.asarray(r, dtype=float) - 2)

    def x(self, r):
        return self.ox + (np.asarray(r, dtype=float) - self.r0) / (self.r1 - self.r0) * self.ancho

    def y(self, v):
        return self.oy + np.asarray(v, dtype=float) / self.v_top * self.alto

    def p(self, r, v=0.0) -> np.ndarray:
        return np.array([float(self.x(r)), float(self.y(v)), 0.0])

    def curva(self, desde: float | None = None, hasta: float | None = None, color=MEDIDA, ancho: float = 4.5):
        a = self.r0 if desde is None else desde
        b = self.r1 if hasta is None else hasta
        t = np.linspace(a, b, 120)
        return traza(self.x(t), self.y(self.lam(t)), color, ancho)

    def punto(self, r: float, color=MEDIDA, radio: float = 0.1) -> Dot:
        return Dot(self.p(r, float(self.lam(r))), radius=radio, color=color)

    def linea(self, eta: float, color=ESTIMACION) -> DashedLine:
        """Línea horizontal en Λ = η, a lo ancho del gráfico."""
        return DashedLine(self.p(self.r0, eta), self.p(self.r1, eta), color=color, stroke_width=3.5,
                          dash_length=0.14)

    def corte(self, eta: float) -> float:
        """El r donde Λ(r) = η: 1 + ln(η)/2."""
        return 1 + np.log(eta) / 2

    def bajada(self, eta: float, color=ESTIMACION) -> DashedLine:
        """Vertical desde el corte con η hasta el eje r."""
        r = self.corte(eta)
        return DashedLine(self.p(r, eta), self.p(r), color=color, stroke_width=3, dash_length=0.1)


class TablaNiveles9(VGroup):
    """El detector de juguete: cinco casillas «Nivel 1» … «Nivel 5» y filas de números.

        T = TablaNiveles9()
        T.cas[i]                 casilla del nivel i+1 (con su encabezado en `.encs[i]`)
        T.fila(k, valores, color) -> VGroup de textos en la fila k (0, 1, 2)
        T.rot(k, texto, color)    rótulo a la izquierda de la fila k
        T.columna(i)              rectángulo que rodea la columna i
    """

    SIN = [0.40, 0.30, 0.15, 0.10, 0.05]
    CON = [0.05, 0.10, 0.15, 0.30, 0.40]
    COCIENTE = ["0,125", "0,33", "1", "3", "8"]

    def __init__(self, x0: float = -1.7, paso: float = 1.55, y_enc: float = 2.45, dy: float = 0.85,
                 escala: float = 0.5):
        super().__init__()
        self.x0, self.paso, self.y_enc, self.dy, self.escala = x0, paso, y_enc, dy, escala
        self.cas, self.encs = VGroup(), VGroup()
        for i in range(5):
            c = RoundedRectangle(corner_radius=0.1, width=paso - 0.2, height=3 * dy + 0.75, color=INK,
                                 stroke_width=2.5).set_fill(INK, 0.06)
            c.move_to([self.x(i), y_enc - (3 * dy + 0.75) / 2 + 0.38, 0])
            e = Text(f"Nivel {i + 1}", color=TXT, weight=BOLD).scale(escala * 0.9).move_to([self.x(i), y_enc, 0])
            self.cas.add(c)
            self.encs.add(e)
        self.add(self.cas, self.encs)

    def x(self, i: int) -> float:
        return self.x0 + i * self.paso

    def y(self, k: int) -> float:
        return self.y_enc - (k + 1) * self.dy

    def p(self, i: int, k: int) -> np.ndarray:
        return np.array([self.x(i), self.y(k), 0.0])

    def fila(self, k: int, valores, color) -> VGroup:
        return VGroup(*[Text(v if isinstance(v, str) else f"{v:.2f}".replace(".", ","), color=color).scale(self.escala)
                        .move_to(self.p(i, k)) for i, v in enumerate(valores)])

    def rot(self, k: int, texto: str, color) -> Text:
        t = Text(texto, color=color, weight=BOLD).scale(self.escala)
        return t.move_to([self.x(0) - self.paso / 2 - 0.25, self.y(k), 0], aligned_edge=RIGHT)

    def columna(self, i: int, color=ESTIMACION) -> RoundedRectangle:
        c = self.cas[i]
        return RoundedRectangle(corner_radius=0.12, width=c.width + 0.12, height=c.height + 0.12,
                                color=color, stroke_width=5).move_to(c)


# ------------------------------------------------------------------ íconos

def monedero9(texto: str = "", color=AMBAR, escala: float = 1.0) -> VGroup:
    """Monedero: cuerpo redondeado con cierre y, opcionalmente, un texto adentro (`.cuerpo`, `.txt`)."""
    cuerpo = RoundedRectangle(corner_radius=0.3, width=2.3, height=1.4, color=color,
                              stroke_width=4).set_fill(color, 0.15)
    cierre = VGroup(Circle(radius=0.12, color=color, stroke_width=4).move_to(cuerpo.get_top() + LEFT * 0.2 + UP * 0.08),
                    Circle(radius=0.12, color=color, stroke_width=4).move_to(cuerpo.get_top() + RIGHT * 0.2 + UP * 0.08))
    txt = Text(texto, color=TXT, weight=BOLD).scale(0.5).move_to(cuerpo) if texto else VGroup()
    g = VGroup(cuerpo, cierre, txt).scale(escala)
    g.cuerpo, g.txt = cuerpo, txt
    return g


def mochila9(color=INK, escala: float = 1.0) -> VGroup:
    """Mochila de frente: cuerpo, solapa, bolsillo y asa (`.cuerpo`)."""
    cuerpo = RoundedRectangle(corner_radius=0.35, width=2.0, height=2.3, color=color,
                              stroke_width=4).set_fill(color, 0.1)
    solapa = ArcBetweenPoints(cuerpo.get_corner(UL) + DOWN * 0.45 + RIGHT * 0.05,
                              cuerpo.get_corner(UR) + DOWN * 0.45 + LEFT * 0.05, angle=PI / 3,
                              color=color, stroke_width=4)
    bolsillo = RoundedRectangle(corner_radius=0.15, width=1.2, height=0.6, color=color,
                                stroke_width=3).move_to(cuerpo.get_bottom() + UP * 0.5)
    asa = Arc(radius=0.3, start_angle=0, angle=PI, color=color, stroke_width=4).move_to(cuerpo.get_top() + UP * 0.15)
    g = VGroup(asa, cuerpo, solapa, bolsillo).scale(escala)
    g.cuerpo = cuerpo
    return g


def fibra9(largo: float = 6.0, color=CIAN) -> VGroup:
    """Cable de fibra óptica: un tubo con un núcleo de luz (`.tubo`, `.nucleo`)."""
    tubo = RoundedRectangle(corner_radius=0.22, width=largo, height=0.44, color=INK,
                            stroke_width=3).set_fill(INK, 0.12)
    nucleo = Line(tubo.get_left() + RIGHT * 0.2, tubo.get_right() + LEFT * 0.2, color=color, stroke_width=5)
    g = VGroup(tubo, nucleo)
    g.tubo, g.nucleo = tubo, nucleo
    return g


def pulso_ruidoso9(centro=(0.0, 0.0), ancho: float = 2.6, alto: float = 1.0, ruido: float = 0.05,
                   semilla: int = 3, color=C1) -> VMobject:
    """Un pulso rectangular (de 0 a `alto`) con ruido encima."""
    rng = np.random.default_rng(semilla)
    x = np.linspace(-ancho / 2, ancho / 2, 90)
    base = np.where(np.abs(x) < ancho * 0.32, alto, 0.0)
    y = base + rng.normal(0, ruido, x.size)
    return traza(x + centro[0], y + centro[1] - alto / 2, color, 3.0)


def cuaderno9(texto: str = "En profundidad", color=INK) -> VGroup:
    """Cuaderno con espiral y un rótulo en la tapa."""
    tapa = RoundedRectangle(corner_radius=0.1, width=2.0, height=2.5, color=color, stroke_width=4).set_fill(color, 0.1)
    espiral = VGroup(*[Circle(radius=0.07, color=color, stroke_width=3).move_to(tapa.get_left() + UP * (0.9 - 0.3 * i))
                       for i in range(7)])
    t = VGroup(*[Text(p, color=TXT).scale(0.36) for p in texto.split(" ", 1)]).arrange(DOWN, buff=0.1)
    t.move_to(tapa).shift(RIGHT * 0.12)
    return VGroup(tapa, espiral, t)


def region_rara9(C: Campanas9, trozos, color=ESTIMACION, grosor: float = 0.16) -> VGroup:
    """Varios trozos sueltos de región de decisión sobre el eje de `C` (lista de (desde, hasta))."""
    return VGroup(*[C.region(a, b, color, grosor) for a, b in trozos])


def detector9(color=INK, escala: float = 1.0) -> VGroup:
    """Detector de juguete: caja con un cuadrante y una aguja (`.caja`, `.aguja`, `.centro`)."""
    caja_ = RoundedRectangle(corner_radius=0.2, width=2.4, height=1.7, color=color, stroke_width=4).set_fill(color, 0.1)
    c = caja_.get_center() + DOWN * 0.45
    arco = Arc(radius=0.85, start_angle=PI / 6, angle=2 * PI / 3, color=TXT, stroke_width=3, arc_center=c)
    rayas = VGroup(*[Line(c + 0.72 * np.array([np.cos(a), np.sin(a), 0]), c + 0.85 * np.array([np.cos(a), np.sin(a), 0]),
                          color=TXT, stroke_width=3) for a in np.linspace(PI / 6, 5 * PI / 6, 5)])
    aguja = Line(c, c + 0.75 * np.array([np.cos(2 * PI / 3), np.sin(2 * PI / 3), 0]), color=ESTIMACION, stroke_width=5)
    g = VGroup(caja_, arco, rayas, aguja).scale(escala)
    g.caja, g.aguja = caja_, aguja
    g.centro = lambda: aguja.get_start()
    return g


def ficha9(texto: str, color=VERDE, lado: float = 0.5) -> VGroup:
    """Ficha cuadrada con un número (el nivel que entra en la mochila)."""
    r = RoundedRectangle(corner_radius=0.08, width=lado, height=lado, color=color, stroke_width=3).set_fill(color, 0.25)
    t = Text(texto, color=TXT, weight=BOLD).scale(0.42 * lado / 0.5).move_to(r)
    return VGroup(r, t)
