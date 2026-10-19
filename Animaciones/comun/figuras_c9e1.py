"""Piezas del capítulo 9, episodio 1 («¿Un cero o un uno?»).

Módulo aparte (como `figuras_c8e4.py`) para no pisar `figuras.py` cuando
varias sesiones trabajan a la vez. Las escenas lo importan:

    from comun.escena import *
    from comun.figuras_c9e1 import *

Las dos campanas del capítulo: el cero se envía como 0 V y el uno como 2 V,
con ruido gaussiano de desvío 1. Con a priori 0,7 / 0,3 el cruce queda en
1 + ln(7/3)/2 = 1,42.
"""
from __future__ import annotations

from manim import *

from comun.estilo import *
from comun.figuras import Lienzo, gaussiana, traza

C0 = RUIDO       # la campana del cero, H₀, «Se envió 0»
C1 = SENAL       # la campana del uno, H₁, «Se envió 1»
P0, P1 = 0.7, 0.3
CRUCE9 = 1 + np.log(P0 / P1) / 2          # 1,4236


class Campanas9:
    """Lienzo de la medición r (en voltios) con las campanas de cada hipótesis.

        C = Campanas9()
        c0 = C.campana(0, 1, C0)            # campana del cero, sin escalar
        c1 = C.campana(2, 0.3, C1)          # la del uno, escalada por p₁
        C.p(1.3, C.f(2, 1.3))               # punto de pantalla de la altura en 1,3
    """

    def __init__(self, centro=(0.0, -2.3), ancho: float = 11.0, alto: float = 7.2,
                 r_rango=(-3.0, 5.0), v_max: float = 0.45):
        self.L = Lienzo(ancho=ancho, alto=alto, t_rango=r_rango, v_max=v_max, centro=centro)
        self.r0, self.r1 = r_rango

    @staticmethod
    def f(mu: float, r, factor: float = 1.0):
        """Altura de la campana centrada en `mu` (desvío 1), multiplicada por `factor`."""
        return factor * gaussiana(np.asarray(r, dtype=float), mu, 1.0)

    def p(self, r, v=0.0) -> np.ndarray:
        return self.L.p(r, v)

    def campana(self, mu: float, factor: float = 1.0, color=C0, ancho: float = 4.0,
                desde: float | None = None, hasta: float | None = None) -> VMobject:
        a = self.r0 if desde is None else desde
        b = self.r1 if hasta is None else hasta
        t = np.linspace(a, b, 170)
        return self.L.curva(t, self.f(mu, t, factor), color, ancho)

    def area(self, mu: float, factor: float, desde: float, hasta: float, color=ERROR,
             opacidad: float = 0.45) -> Polygon:
        """Área bajo una campana (escalada) entre dos valores de r."""
        t = np.linspace(max(desde, self.r0), min(hasta, self.r1), 80)
        v = self.f(mu, t, factor)
        pts = [self.p(t[0])] + [self.p(a, b) for a, b in zip(t, v)] + [self.p(t[-1])]
        return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)

    def solape(self, color=INK, opacidad: float = 0.22) -> Polygon:
        """Zona común de las dos campanas sin escalar (debajo de la más baja)."""
        t = np.linspace(self.r0, self.r1, 160)
        v = np.minimum(self.f(0, t), self.f(2, t))
        pts = [self.p(t[0])] + [self.p(a, b) for a, b in zip(t, v)] + [self.p(t[-1])]
        return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(color, opacidad)

    def eje(self, marcas=(0, 1, 2), rotulo: bool = True, escala: float = 0.5) -> VGroup:
        """Base con números debajo y el rótulo «r (V)» a la derecha (`.base`, `.nums`, `.rot`)."""
        base = Line(self.p(self.r0), self.p(self.r1), color=INK, stroke_width=2.4)
        nums = VGroup(*[Text(num(m), color=INK).scale(escala).move_to(self.p(m) + DOWN * 0.32) for m in marcas])
        g = VGroup(base, nums)
        g.base, g.nums = base, nums
        g.rot = None
        if rotulo:
            g.rot = MathTex(r"r\ (\mathrm{V})", color=INK).scale(0.6).next_to(base.get_right(), UP, buff=0.32)
            g.rot.shift(LEFT * 0.35)
            g.add(g.rot)
        return g

    def regla(self, r: float, color=MEDIDA, alto: float = 3.3, ancho: float = 4) -> Line:
        """Línea vertical en la medición r (la «regla»)."""
        return Line(self.p(r) + DOWN * 0.12, self.p(r) + UP * alto, color=color, stroke_width=ancho)

    def punto(self, mu: float, r: float, factor: float = 1.0, color=C0, radio: float = 0.09) -> Dot:
        return Dot(self.p(r, self.f(mu, r, factor)), radius=radio, color=color)

    def segmento(self, mu: float, r: float, factor: float = 1.0, color=C0, ancho: float = 7) -> Line:
        """Segmento vertical desde el eje hasta la altura de la campana en r."""
        return Line(self.p(r), self.p(r, self.f(mu, r, factor)), color=color, stroke_width=ancho)

    def region(self, desde: float, hasta: float, color, grosor: float = 0.16, opacidad: float = 0.75) -> Rectangle:
        """Banda coloreada pegada al eje, entre dos valores de r (una región de decisión)."""
        a, b = max(desde, self.r0), min(hasta, self.r1)
        r = Rectangle(width=float(self.L.x(b) - self.L.x(a)), height=grosor, stroke_width=0)
        r.set_fill(color, opacidad).move_to(self.p((a + b) / 2) + UP * grosor / 2)
        return r


def canal9(centro=(0.0, 0.0), ancho: float = 7.0, escala: float = 1.0) -> VGroup:
    """El canal que confunde bits: flecha de entrada, caja «Canal», flecha de salida.
    `.caja`, `.rot`, `.ent`, `.sal`, `p_ent()`, `p_sal()`. (Como `canal7`, con el rótulo en mayúscula.)"""
    c = np.array([centro[0], centro[1], 0.0])
    caja_ = RoundedRectangle(corner_radius=0.14, width=2.3 * escala, height=1.3 * escala, color=INK,
                             stroke_width=3).set_fill(INK, 0.12).move_to(c)
    rot = Text("Canal", color=TXT).scale(0.55 * escala).move_to(c)
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


def bit9(valor: int, color=None, lado: float = 0.5) -> VGroup:
    """Un bit: casilla con «0» o «1» (magenta el cero, azul el uno, si no se da color)."""
    col = color if color is not None else (C1 if valor else C0)
    cas = RoundedRectangle(corner_radius=0.08, width=lado, height=lado, color=col, stroke_width=3)
    cas.set_fill(col, 0.18)
    t = Text(str(valor), color=TXT, weight=BOLD).scale(0.5 * lado / 0.5).move_to(cas)
    return VGroup(cas, t)


def casilla9(texto: str, color, ancho: float = 3.2, alto: float = 0.8, escala: float = 0.5) -> VGroup:
    """Casilla de texto con borde y fondo del color dado (hipótesis, reglas)."""
    t = Text(texto, color=TXT).scale(escala)
    r = RoundedRectangle(corner_radius=0.12, width=max(ancho, t.width + 0.4), height=alto, color=color,
                         stroke_width=3).set_fill(color, 0.14)
    t.move_to(r)
    g = VGroup(r, t)
    g.marco, g.txt = r, t
    return g


class ParBarras9(VGroup):
    """Dos barras verticales con su valor encima y su rótulo debajo (probabilidades a posteriori).
    `.barras`, `.valores`, `.rots`, `.base`, `.titulo`; `marco(i, color)` rodea una barra."""

    def __init__(self, valores, colores, rotulos, titulo: str = "", centro=(0.0, 0.0),
                 alto: float = 2.6, ancho: float = 0.8, hueco: float = 0.55, escala: float = 0.48):
        super().__init__()
        cx, cy = centro
        y0 = cy - alto / 2
        self.barras, self.valores, self.rots = VGroup(), VGroup(), VGroup()
        for i, (v, col, rot) in enumerate(zip(valores, colores, rotulos)):
            x = cx + (i - 0.5) * (ancho + hueco)
            h = max(0.04, v * alto)
            b = Rectangle(width=ancho, height=h, color=col, stroke_width=3).set_fill(col, 0.45)
            b.move_to([x, y0 + h / 2, 0])
            self.barras.add(b)
            self.valores.add(Text(num(v, 3), color=TXT).scale(escala).next_to(b, UP, buff=0.12))
            self.rots.add(MathTex(rot, color=col).scale(0.62).move_to([x, y0 - 0.32, 0]))
        self.base = Line([cx - ancho - hueco, y0, 0], [cx + ancho + hueco, y0, 0], color=INK, stroke_width=2.4)
        self.titulo = Text(titulo, color=MEDIDA).scale(0.5).move_to([cx, y0 - 0.85, 0]) if titulo else VGroup()
        self.add(self.base, self.barras, self.valores, self.rots, self.titulo)

    def marco(self, i: int, color=ESTIMACION) -> SurroundingRectangle:
        return SurroundingRectangle(VGroup(self.barras[i], self.valores[i]), color=color, buff=0.1,
                                    stroke_width=5)


class TablaReglas9(VGroup):
    """Tabla de las cuatro reglas del canal: renglones con nombre y error, armados uno a uno.
    `.titulos`, `.nombres[i]`, `.errores[i]`, `.huecos[i]`; `fila(i)` es el renglón entero."""

    NOMBRES = ["Creer lo recibido", "Siempre 0", "Siempre 1", "Llevar la contraria"]
    DETALLE = ["0 → 0 · 1 → 1", "0 → 0 · 1 → 0", "0 → 1 · 1 → 1", "0 → 1 · 1 → 0"]
    ERRORES = [0.10, 0.30, 0.70, 0.90]

    def __init__(self, centro=(0.0, -0.4), ancho: float = 9.4, paso: float = 0.95, escala: float = 0.52):
        super().__init__()
        cx, cy = centro
        self.x_nom = cx - ancho / 2 + 0.2
        self.x_det = cx + 0.9
        self.x_err = cx + ancho / 2 - 0.7
        self.ys = [cy + paso * (1.5 - i) for i in range(4)]
        self.titulos = VGroup(
            Text("Regla", color=INK).scale(escala * 0.9).move_to([self.x_nom, cy + paso * 2.5, 0], aligned_edge=LEFT),
            Text("Decir", color=INK).scale(escala * 0.9).move_to([self.x_det, cy + paso * 2.5, 0]),
            Text("Error", color=ERROR).scale(escala * 0.9).move_to([self.x_err, cy + paso * 2.5, 0]))
        self.nombres, self.detalles, self.errores, self.huecos = [], [], [], []
        for i in range(4):
            y = self.ys[i]
            self.nombres.append(Text(self.NOMBRES[i], color=TXT).scale(escala).move_to([self.x_nom, y, 0],
                                                                                      aligned_edge=LEFT))
            self.detalles.append(Text(self.DETALLE[i], color=INK).scale(escala * 0.85).move_to([self.x_det, y, 0]))
            self.errores.append(Text(num(self.ERRORES[i]), color=ERROR).scale(escala).move_to([self.x_err, y, 0]))
            self.huecos.append(Text("?", color=INK).scale(escala).move_to([self.x_err, y, 0]))
        self.lineas = VGroup(*[Line([cx - ancho / 2, y - paso / 2, 0], [cx + ancho / 2, y - paso / 2, 0],
                                    color=INK, stroke_width=1.5, stroke_opacity=0.5) for y in self.ys])
        self.add(self.titulos, self.lineas)
        self.ancho, self.paso, self.cx = ancho, paso, cx

    def fila(self, i: int) -> VGroup:
        return VGroup(self.nombres[i], self.detalles[i], self.errores[i])

    def marco(self, i: int, color=VERDE) -> Rectangle:
        r = Rectangle(width=self.ancho + 0.2, height=self.paso * 0.92, color=color, stroke_width=5)
        return r.move_to([self.cx, self.ys[i], 0])


def fila_bits9(n_unos: int = 1, n: int = 20, centro=(0.0, 0.0), lado: float = 0.42, hueco: float = 0.1) -> VGroup:
    """Fila de `n` bits con `n_unos` unos (los primeros a la derecha del centro)."""
    bits = VGroup()
    pos_unos = {n // 2 + k for k in range(n_unos)}
    for i in range(n):
        bits.add(bit9(1 if i in pos_unos else 0, lado=lado))
    bits.arrange(RIGHT, buff=hueco).move_to([centro[0], centro[1], 0])
    return bits


def pulsos9(bits, centro=(0.0, 0.0), ancho_bit: float = 0.9, alto: float = 1.0, color=C1) -> VMobject:
    """Tren de pulsos PAM: nivel 0 para el cero y `alto` para el uno."""
    x0 = centro[0] - len(bits) * ancho_bit / 2
    y0 = centro[1]
    pts = []
    for i, b in enumerate(bits):
        y = y0 + (alto if b else 0.0)
        pts += [[x0 + i * ancho_bit, y, 0], [x0 + (i + 1) * ancho_bit, y, 0]]
    m = VMobject(stroke_color=color, stroke_width=4)
    m.set_points_as_corners(np.array(pts, dtype=float))
    return m


def garabato9(centro=(0.0, 0.0), ancho: float = 1.6, alto: float = 0.5, semilla: int = 5, color=RUIDO) -> VMobject:
    """Garabato de ruido (para el cable)."""
    rng = np.random.default_rng(semilla)
    x = np.linspace(-ancho / 2, ancho / 2, 40)
    y = rng.normal(0, alto / 3, 40)
    return traza(x + centro[0], y + centro[1], color, 3.0)


def balanza9(centro=(0.0, 0.0), semi: float = 2.0, izq: str = "Lo que sabías", der: str = "Lo que ves"):
    """La `Balanza` de `figuras.py` con un rótulo en cada platillo (`.rot_izq`, `.rot_der`)."""
    from comun.figuras import Balanza
    b = Balanza(centro=centro, semi=semi)
    b.rot_izq = Text(izq, color=ESTIMACION).scale(0.42).next_to(b.izq[1], DOWN, buff=0.18)
    b.rot_der = Text(der, color=MEDIDA).scale(0.42).next_to(b.der[1], DOWN, buff=0.18)
    b.izq.add(b.rot_izq)
    b.der.add(b.rot_der)
    return b


def rot_tex9(tex: str, texto: str, color, escala: float = 0.5) -> VGroup:
    """Rótulo mixto: un símbolo en LaTeX (H_0, D_1, p_0…) seguido de texto («· Se envió 0»)."""
    m = MathTex(tex, color=color).scale(escala * 1.35)
    t = Text(texto, color=TXT).scale(escala)
    g = VGroup(m, t).arrange(RIGHT, buff=0.14)
    t.align_to(m, DOWN).shift(DOWN * 0.02)
    return g


def casilla_h9(tex: str, texto: str, color, ancho: float = 3.6, alto: float = 0.85, escala: float = 0.5) -> VGroup:
    """Casilla de hipótesis: «H₀ · Se envió 0» con borde y fondo del color dado (`.marco`, `.txt`)."""
    t = rot_tex9(tex, texto, color, escala)
    r = RoundedRectangle(corner_radius=0.12, width=max(ancho, t.width + 0.5), height=alto, color=color,
                         stroke_width=3).set_fill(color, 0.14)
    t.move_to(r)
    g = VGroup(r, t)
    g.marco, g.txt = r, t
    return g
