"""Piezas del capítulo 9, episodio 5 («¿Cuánto cuesta equivocarse?»).

Módulo aparte (como `figuras_c9e4.py`) para no pisar `figuras.py` cuando
varias sesiones trabajan a la vez. Las escenas lo importan:

    from comun.escena import *
    from comun.figuras_c9e5 import *

Trae también lo del E4 (`PlanoRoc9`, `roc9`, `Q`, `tarjeta9`…) y del E1
(`Campanas9`, `C0`, `C1`, `CRUCE9`). Las campanas son ahora un análisis de
sangre: sano con centro 0, enfermo con centro 2, desvío 1; a priori 0,7 / 0,3;
costes: falsa alarma 1, fallo 5. Con eso η = 0,47 y el umbral baja a 0,62.
"""
from __future__ import annotations

from manim import *

from comun.estilo import *
from comun.figuras_c9e1 import C0, C1, P0, P1, CRUCE9, Campanas9, canal9, casilla9
from comun.figuras_c9e2 import Tabla22_9
from comun.figuras_c9e4 import (DET, FA, PLANO_C, Q, ROC, PlanoRoc9, lam9, roc9, rotulo_par9,
                                tarjeta9)

C_FA, C_M = 1.0, 5.0
ETA_R = P0 * C_FA / (P1 * C_M)                 # 0,467
U_MAP = CRUCE9                                 # 1,42
U_R = 1 + np.log(ETA_R) / 2                    # 0,619
MEDICION = 1.3


def post_enfermo9(r: float) -> float:
    """Probabilidad a posteriori de estar enfermo con el análisis r (0,44 en 1,3)."""
    f0 = np.exp(-r * r / 2)
    f1 = np.exp(-(r - 2) ** 2 / 2)
    return float(P1 * f1 / (P0 * f0 + P1 * f1))


def campanas_e5(centro=(0.0, -2.0), ancho: float = 10.0, alto: float = 5.2) -> Campanas9:
    """Las campanas del capítulo, un poco más bajas que en el E1 (deja sitio arriba)."""
    return Campanas9(centro=centro, ancho=ancho, alto=alto, r_rango=(-3.0, 5.0), v_max=0.45)


def tubo9(color=ERROR, alto: float = 1.6) -> VGroup:
    """Tubo de ensayo con sangre: `.vidrio`, `.liquido`."""
    w = 0.42
    vidrio = VGroup(
        Line([-w / 2, 0.75, 0], [-w / 2, -0.55, 0]),
        Line([w / 2, 0.75, 0], [w / 2, -0.55, 0]),
        Arc(radius=w / 2, start_angle=PI, angle=PI, arc_center=[0, -0.55, 0]),
        Line([-w / 2 - 0.08, 0.75, 0], [w / 2 + 0.08, 0.75, 0]),
    ).set_stroke(TXT, 4)
    liq_pts = [[-w / 2 + 0.05, 0.05, 0], [w / 2 - 0.05, 0.05, 0]]
    liquido = VGroup(
        Rectangle(width=w - 0.1, height=0.6, stroke_width=0).set_fill(color, 0.85).move_to([0, -0.25, 0]),
        Sector(radius=w / 2 - 0.05, start_angle=PI, angle=PI, arc_center=[0, -0.55, 0],
               stroke_width=0).set_fill(color, 0.85))
    g = VGroup(liquido, vidrio)
    g.vidrio, g.liquido = vidrio, liquido
    return g.scale(alto / 1.6)


def pastilla9(color=VERDE, escala: float = 1.0) -> VGroup:
    """Cápsula de dos colores."""
    a = RoundedRectangle(corner_radius=0.12, width=0.3, height=0.24, stroke_width=0).set_fill(color, 1)
    b = RoundedRectangle(corner_radius=0.12, width=0.3, height=0.24, stroke_width=0).set_fill(TXT, 1)
    a.shift(LEFT * 0.12)
    b.shift(RIGHT * 0.12)
    return VGroup(a, b).rotate(25 * DEGREES).scale(escala)


class BarrasSE9(VGroup):
    """Dos barras verticales, «Sano» y «Enfermo», que crecen hasta su probabilidad.
    `.marcos` (contornos vacíos), `.rellenos`, `.rots`, `.vals`, `.base`; `crecer(p_sano)`
    devuelve las animaciones."""

    def __init__(self, centro=(2.6, -0.2), alto: float = 4.0, ancho: float = 1.2, hueco: float = 0.9,
                 escala: float = 0.55):
        super().__init__()
        cx, cy = centro
        self.y0 = cy - alto / 2
        self.alto = alto
        self.xs = [cx - (ancho + hueco) / 2, cx + (ancho + hueco) / 2]
        self.colores = (C0, C1)
        self.marcos, self.rellenos, self.rots, self.vals = VGroup(), [], VGroup(), [None, None]
        for x, col, t in zip(self.xs, self.colores, ("Sano", "Enfermo")):
            m = Rectangle(width=ancho, height=alto, color=col, stroke_width=2.5, stroke_opacity=0.5)
            m.move_to([x, cy, 0])
            self.marcos.add(m)
            r = Rectangle(width=ancho, height=0.02, stroke_width=0).set_fill(col, 0.7)
            r.move_to([x, self.y0 + 0.01, 0])
            self.rellenos.append(r)
            self.rots.add(Text(t, color=col).scale(escala).move_to([x, self.y0 - 0.38, 0]))
        self.ancho, self.escala = ancho, escala
        self.base = Line([self.xs[0] - ancho, self.y0, 0], [self.xs[1] + ancho, self.y0, 0], color=INK,
                         stroke_width=2.4)
        self.add(self.base, self.marcos, *self.rellenos, self.rots)

    def crecer(self, p_sano: float):
        anims = []
        for i, p in enumerate((p_sano, 1 - p_sano)):
            h = p * self.alto
            nuevo = Rectangle(width=self.ancho, height=h, stroke_width=0).set_fill(self.colores[i], 0.7)
            nuevo.move_to([self.xs[i], self.y0 + h / 2, 0])
            anims.append(Transform(self.rellenos[i], nuevo))
            v = Text(f"{round(p * 100)} %", color=TXT, weight=BOLD).scale(self.escala * 1.1)
            v.move_to([self.xs[i], self.y0 + h + 0.32, 0])
            self.vals[i] = v
        return anims

    def fijar(self, p_sano: float) -> None:
        """Deja las barras ya crecidas (sin animar); los valores quedan en `.vals`."""
        for a in self.crecer(p_sano):
            a.mobject.become(a.target_mobject)

    def tope(self, i: int) -> np.ndarray:
        return self.rellenos[i].get_top()


def umbral9_e5(C: Campanas9, r: float, alto: float = 2.9, color=ESTIMACION) -> Line:
    """Línea vertical del umbral sobre las campanas."""
    return Line(C.p(r) + DOWN * 0.1, C.p(r) + UP * alto, color=color, stroke_width=4)


def tabla_costes9(centro=(0.9, -0.6), ancho: float = 3.0, alto: float = 1.45, escala: float = 0.5) -> Tabla22_9:
    """Tabla de costes 2 × 2: filas «Sano»/«Enfermo» (la realidad) y columnas «Decir sano»/«Decir
    enfermo». Falsa alarma en (0, 1) y fallo en (1, 0)."""
    return Tabla22_9(("Sano", "Enfermo"), ("Decir sano", "Decir enfermo"), centro=centro, ancho=ancho,
                     alto=alto, titulo_f="Realidad", titulo_c="Decisión", escala=escala)


def tabla_costes_mini9(centro=(5.0, 2.6)) -> VGroup:
    """La tabla de costes en pequeño, ya llena, para una esquina. `.uno`, `.cinco`."""
    T = Tabla22_9(("Sano", "Enfermo"), ("Sano", "Enfermo"), centro=centro, ancho=1.0, alto=0.62, escala=0.32)
    vals = {}
    for (i, j), v, col in (((0, 0), "0", INK), ((0, 1), "1", ESTIMACION), ((1, 0), "5", ERROR),
                           ((1, 1), "0", INK)):
        vals[(i, j)] = Text(v, color=col, weight=BOLD).scale(0.42).move_to(T.c(i, j))
    g = VGroup(T, *vals.values())
    g.T, g.uno, g.cinco = T, vals[(0, 1)], vals[(1, 0)]
    return g


def etiqueta_precio9(color=ESTIMACION, escala: float = 1.0) -> VGroup:
    """Etiqueta de precio vacía (pentágono con agujero)."""
    cuerpo = Polygon([-0.35, 0.22, 0], [0.25, 0.22, 0], [0.45, 0, 0], [0.25, -0.22, 0], [-0.35, -0.22, 0],
                     color=color, stroke_width=3).set_fill(color, 0.15)
    agujero = Circle(radius=0.05, color=color, stroke_width=2.5).move_to([0.22, 0, 0])
    t = Text("?", color=color, weight=BOLD).scale(0.38).move_to([-0.08, 0, 0])
    return VGroup(cuerpo, agujero, t).scale(escala)


def campanitas9(C: Campanas9, n: int, color=C1, ancho: float = 3.5, alto_rel: float = 0.8) -> VGroup:
    """`n` campanas con centros repartidos entre 0 y 2 V, cada vez más estrechas (todas de la misma
    altura en pantalla). Con n = 2 son las del capítulo."""
    mus = np.linspace(0, 2, n)
    s = 1.0 if n == 2 else max(0.035, 0.75 * 2 / (n - 1) / 2)
    g = VGroup()
    for mu in mus:
        t = np.linspace(max(C.r0, mu - 4 * s), min(C.r1, mu + 4 * s), 90)
        v = alto_rel * C.L.v_max * np.exp(-(t - mu) ** 2 / (2 * s * s))
        g.add(C.L.curva(t, v, color, ancho))
    return g


def dardo9(color=ESTIMACION, escala: float = 1.0) -> VGroup:
    """Dardo apuntando hacia abajo (la punta en el origen del grupo, `.punta`)."""
    cuerpo = Line([0, 0.15, 0], [0, 1.0, 0], color=TXT, stroke_width=5)
    punta = Polygon([0, 0, 0], [-0.07, 0.18, 0], [0.07, 0.18, 0], color=TXT, stroke_width=0).set_fill(TXT, 1)
    plumas = VGroup(Polygon([0, 0.8, 0], [-0.18, 1.05, 0], [0, 1.0, 0]),
                    Polygon([0, 0.8, 0], [0.18, 1.05, 0], [0, 1.0, 0])).set_stroke(width=0).set_fill(color, 1)
    g = VGroup(cuerpo, punta, plumas).scale(escala, about_point=ORIGIN)
    g.punta = punta
    return g


def bloque9(texto: str, color=INK, ancho: float = 3.2, alto: float = 1.0, escala: float = 0.48) -> VGroup:
    """Caja redondeada con un texto (piezas de la «maquinaria»). `.marco`, `.txt`."""
    return casilla9(texto, color, ancho=ancho, alto=alto, escala=escala)


def lista_casos9(signos: str = "+ + − + − + − −", centro=(0.0, 0.0), lado: float = 0.62) -> VGroup:
    """Fila de casos sueltos, cada uno con su «+» (enfermo, azul) o «−» (sano, magenta)."""
    g = VGroup()
    for s in signos.split():
        col = C1 if s == "+" else C0
        c = RoundedRectangle(corner_radius=0.08, width=lado, height=lado, color=col, stroke_width=3)
        c.set_fill(col, 0.15)
        g.add(VGroup(c, Text(s, color=TXT, weight=BOLD).scale(0.55).move_to(c)))
    return g.arrange(RIGHT, buff=0.16).move_to([centro[0], centro[1], 0])


def frac9(num: str, den: str, color=TXT, escala: float = 0.85, color_den=None) -> VGroup:
    """Fracción armada a mano (numerador y denominador como `MathTex` sueltos, para entrarlos por
    separado). `.num`, `.barra`, `.den`."""
    n = MathTex(num, color=color).scale(escala)
    d = MathTex(den, color=color_den or color).scale(escala)
    w = max(n.width, d.width) + 0.15
    barra = Line(LEFT * w / 2, RIGHT * w / 2, color=TXT, stroke_width=3)
    n.next_to(barra, UP, buff=0.12)
    d.next_to(barra, DOWN, buff=0.12)
    g = VGroup(n, barra, d)
    g.num, g.barra, g.den = n, barra, d
    return g


class TablaDosReglas9(VGroup):
    """Tabla para medir las dos reglas con las dos varas: renglones «Máximo a posteriori» y «Riesgo
    mínimo»; columnas «Falsa alarma», «Fallo», «Error», «Coste». Se arma vacía (rótulos de fila y
    líneas); las cabeceras y las celdas se piden con `cabecera(j)` y `celda(i, j, txt, color)`.
    `.filas`, `.lineas`; `c(i, j)` da el centro de una celda; `marco(i, j, color)`."""

    COLS = ("Falsa alarma", "Fallo", "Error", "Coste")
    COL_COLOR = (ERROR, ERROR, ERROR, ESTIMACION)

    def __init__(self, y0: float = -1.35, paso: float = 0.72, x_rot: float = -4.6,
                 xs=(-1.5, 0.7, 2.75, 4.8), escala: float = 0.46):
        super().__init__()
        self.y0, self.paso, self.xs, self.escala = y0, paso, xs, escala
        self.filas = VGroup(
            Text("Máximo a posteriori", color=TXT).scale(escala).move_to([x_rot, self.y(0), 0]),
            Text("Riesgo mínimo", color=TXT).scale(escala).move_to([x_rot, self.y(1), 0]))
        x_a, x_b = x_rot - 1.75, xs[-1] + 1.0
        self.lineas = VGroup(*[Line([x_a, y, 0], [x_b, y, 0], color=INK, stroke_width=1.5, stroke_opacity=0.5)
                               for y in (self.y0 - paso / 2, self.y(0) - paso / 2, self.y(1) - paso / 2)])
        self.add(self.filas, self.lineas)

    def y(self, i: int) -> float:
        """Altura del renglón i (−1 = cabecera)."""
        return self.y0 - self.paso * (i + 1)

    def c(self, i: int, j: int) -> np.ndarray:
        return np.array([self.xs[j], self.y(i), 0.0])

    def cabecera(self, j: int) -> Text:
        return Text(self.COLS[j], color=self.COL_COLOR[j]).scale(self.escala * 0.95).move_to([self.xs[j], self.y0, 0])

    def celda(self, i: int, j: int, txt: str, color=TXT) -> Text:
        return Text(txt, color=color).scale(self.escala * 1.1).move_to(self.c(i, j))

    def marco(self, i: int, j: int, color=VERDE) -> Rectangle:
        return Rectangle(width=1.5, height=self.paso * 0.82, color=color, stroke_width=4).move_to(self.c(i, j))

    def todas(self, valores=(("0,077", "0,28", "0,139", "0,48"), ("0,27", "0,084", "0,21", "0,31"))) -> VGroup:
        """Cabeceras y celdas ya llenas (para retomar la tabla en otra escena). `.cel[i][j]`."""
        g = VGroup(*[self.cabecera(j) for j in range(4)])
        self.cel = [[self.celda(i, j, valores[i][j]) for j in range(4)] for i in range(2)]
        for fila in self.cel:
            g.add(*fila)
        return g


def casita9(ancho: float = 1.0, color=INK) -> VGroup:
    """La `casa` de `iconos.py` en pequeño (su alero es fijo: se dibuja grande y se escala)."""
    from comun.iconos import casa
    return casa(ancho=2.0, alto=1.45, color=color).scale_to_fit_width(ancho)
