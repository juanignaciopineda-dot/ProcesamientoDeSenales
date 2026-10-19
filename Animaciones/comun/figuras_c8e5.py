"""Piezas del capítulo 8, episodio 5 («¿Dos termómetros mejor que uno?»).

Van en un módulo aparte (como `figuras_c8e4.py`) porque varias sesiones editan `figuras.py` a la vez.
Las escenas del E5 lo importan con `from comun.figuras_c8e5 import *`.
"""
from __future__ import annotations

import numpy as np
from manim import *

from comun.estilo import *
from comun.figuras import termometro, traza


# ------------------------------------------------------------ termómetros

class Termo8(VGroup):
    """Termómetro con su letra encima («A», «B», «B₁»…). `.t` (el de `termometro()`: `.tubo`, `.liquido`,
    `.bulbo`), `.letra`. `nivel(f)` devuelve la animación que lleva el líquido a la fracción `f` del tubo;
    `debajo(m, buff)` coloca `m` bajo el bulbo."""

    def __init__(self, letra: str = "A", centro=(0.0, 0.0), alto: float = 2.2, nivel: float = 0.45,
                 color_letra=MEDIDA, escala_letra: float = 0.8):
        super().__init__()
        self.alto = alto
        self.t = termometro(alto=alto, color=ROJO, nivel=nivel)
        self.t.move_to([centro[0], centro[1], 0])
        self.letra = MathTex(letra, color=color_letra).scale(escala_letra).next_to(self.t, UP, buff=0.18)
        self.add(self.t, self.letra)

    def nivel(self, f: float):
        liq = self.t.liquido
        return liq.animate.stretch_to_fit_height(self.alto * f, about_edge=DOWN)

    def debajo(self, m: Mobject, buff: float = 0.25) -> Mobject:
        return m.next_to(self.t.bulbo, DOWN, buff=buff)


def ruido8(centro=(0.0, 0.0), ancho: float = 1.6, amp: float = 0.15, semilla: int = 4, n: int = 26,
           color=RUIDO, grosor: float = 3.0) -> VMobject:
    """Una traza corta de ruido (zigzag aleatorio con semilla fija) centrada en `centro`."""
    rng = np.random.default_rng(semilla)
    xs = np.linspace(-ancho / 2, ancho / 2, n) + centro[0]
    ys = np.clip(rng.normal(0, 1, n), -2.2, 2.2) * amp + centro[1]
    return traza(xs, ys, color, grosor)


# ------------------------------------------------------------ matrices y columnas

class Matriz8(VGroup):
    """Matriz (o columna) de fórmulas entre corchetes. `filas` es una lista de listas de cadenas LaTeX.

    `.c[i][j]` (MathTex), `.corchetes`, `p(i, j)` (centro de la casilla), `fila(i, color)` (marco de una
    fila) y `celda(i, j, color)` (marco de una casilla). `vacia=True` deja las casillas sin agregar al grupo
    (para hacerlas aparecer de a una con `add` en la escena)."""

    def __init__(self, filas, centro=(0.0, 0.0), dx: float = 1.1, dy: float = 0.85, escala: float = 1.0,
                 color=TXT, vacia: bool = False):
        super().__init__()
        self.nf, self.nc = len(filas), len(filas[0])
        self.cx, self.cy, self.dx, self.dy = centro[0], centro[1], dx, dy
        self.c = [[None] * self.nc for _ in range(self.nf)]
        for i in range(self.nf):
            for j in range(self.nc):
                t = MathTex(filas[i][j], color=color).scale(escala).move_to(self.p(i, j))
                self.c[i][j] = t
                if not vacia:
                    self.add(t)
        w = self.nc * dx / 2 + 0.05
        h = self.nf * dy / 2 + 0.05
        o = np.array([self.cx, self.cy, 0.0])
        izq = VMobject(stroke_color=INK, stroke_width=4).set_fill(opacity=0)
        izq.set_points_as_corners([o + [-w + 0.18, h, 0], o + [-w, h, 0], o + [-w, -h, 0], o + [-w + 0.18, -h, 0]])
        der = VMobject(stroke_color=INK, stroke_width=4).set_fill(opacity=0)
        der.set_points_as_corners([o + [w - 0.18, h, 0], o + [w, h, 0], o + [w, -h, 0], o + [w - 0.18, -h, 0]])
        self.corchetes = VGroup(izq, der)
        self.add(self.corchetes)

    def p(self, i: int, j: int) -> np.ndarray:
        return np.array([self.cx + (j - (self.nc - 1) / 2) * self.dx,
                         self.cy - (i - (self.nf - 1) / 2) * self.dy, 0.0])

    def fila(self, i: int, color=AMBAR) -> Rectangle:
        return Rectangle(width=self.nc * self.dx - 0.05, height=self.dy * 0.9, color=color,
                         stroke_width=4).move_to([self.cx, self.p(i, 0)[1], 0])

    def celda(self, i: int, j: int, color=AMBAR, relleno: float = 0.0) -> Rectangle:
        return Rectangle(width=self.dx * 0.9, height=self.dy * 0.88, color=color,
                         stroke_width=3).set_fill(color, relleno).move_to(self.p(i, j))

    def todas(self) -> VGroup:
        return VGroup(*[self.c[i][j] for i in range(self.nf) for j in range(self.nc)])


def sistema8(valores, pesos=(r"h_A", r"h_B"), lado=(r"4", r"4"), centro=(0.0, 0.0), escala: float = 0.9):
    """La cuenta «matriz · pesos = columna» de dos termómetros. `valores` = 2 × 2 cadenas.
    Devuelve `(M, H, igual, C, todo)`."""
    M = Matriz8(valores, centro=(centro[0] - 2.0, centro[1]), dx=0.95, dy=0.8, escala=escala)
    H = Matriz8([[pesos[0]], [pesos[1]]], centro=(centro[0] - 0.15, centro[1]), dx=1.0, dy=0.8, escala=escala,
                color=ESTIMACION)
    igual = MathTex("=", color=TXT).scale(escala).move_to([centro[0] + 0.85, centro[1], 0])
    C = Matriz8([[lado[0]], [lado[1]]], centro=(centro[0] + 1.75, centro[1]), dx=0.85, dy=0.8, escala=escala,
                color=SENAL)
    return M, H, igual, C, VGroup(M, H, igual, C)


# ------------------------------------------------------------ el plano de las dos lecturas

class PlanoDos8(VGroup):
    """Dos lecturas (cian) que abren un plano visto en perspectiva, la temperatura (azul) que sale del plano,
    su sombra (ámbar) sobre el plano y el error (rojo), vertical, en ángulo recto con las dos lecturas.

    Atributos: `.plano`, `.xa`, `.xb`, `.y`, `.sombra`, `.error`, `.recto_a`, `.recto_b` y `.rot` (dict de
    MathTex: `xa`, `xb`, `y`, `yh`, `e`). `.o` es el origen y `.pie` el pie de la sombra."""

    def __init__(self, centro=(0.0, 0.0), k: float = 1.0):
        super().__init__()
        o = np.array([centro[0], centro[1], 0.0]) + np.array([-1.6, -0.8, 0.0]) * k
        self.o = o

        def P(x, y):
            return o + np.array([x, y, 0.0]) * k

        esq = [P(-0.9, -0.75), P(3.4, -0.75), P(4.2, 1.2), P(-0.1, 1.2)]
        self.plano = Polygon(*esq, color=INK, stroke_width=2).set_fill(INK, 0.1)
        fa, fb = P(2.9, -0.45), P(1.5, 0.95)
        self.pie = o + 0.55 * (fa - o) + 0.6 * (fb - o)
        punta = self.pie + np.array([0.0, 2.0 * k, 0.0])
        kw = dict(buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.13)
        self.xa = Arrow(o, fa, color=MEDIDA, **kw)
        self.xb = Arrow(o, fb, color=MEDIDA, **kw)
        self.y = Arrow(o, punta, color=SENAL, **kw)
        self.sombra = Line(o, self.pie, color=ESTIMACION, stroke_width=9)
        self.error = Line(self.pie, punta, color=ERROR, stroke_width=5)
        s = 0.24 * k

        def recto(d):
            u = d / np.linalg.norm(d) * s
            m = VMobject(stroke_color=ERROR, stroke_width=3).set_fill(opacity=0)
            m.set_points_as_corners([self.pie + u, self.pie + u + UP * s, self.pie + UP * s])
            return m

        self.recto_a = recto(fa - o)
        self.recto_b = recto(fb - o)
        e = 0.85 * k
        self.rot = {
            "xa": MathTex("x_A", color=MEDIDA).scale(0.8 * e).next_to(fa, UP, buff=0.3).shift(LEFT * 0.45 * k),
            "xb": MathTex("x_B", color=MEDIDA).scale(0.8 * e).next_to(fb, RIGHT, buff=0.2 * k),
            "y": MathTex("y", color=SENAL).scale(0.85 * e).next_to(punta, UP, buff=0.1),
            "yh": MathTex(r"\hat{y}", color=ESTIMACION).scale(0.85 * e).move_to(self.pie + np.array([0.62, -0.08, 0.0]) * k),
            "e": MathTex("e", color=ERROR).scale(0.85 * e).next_to((self.pie + punta) / 2, RIGHT, buff=0.12),
        }
        self.add(self.plano, self.xa, self.xb, self.sombra, self.y, self.error, self.recto_a, self.recto_b,
                 *self.rot.values())


# ------------------------------------------------------------ tarjetas de la encuesta

def tarjeta8(rotulo: str, centro=(0.0, 0.0), ancho: float = 2.4, alto: float = 3.0, color=INK) -> VGroup:
    """Tarjeta boca abajo con un rótulo LaTeX («B_1»…). `.marco`, `.rot`."""
    marco = RoundedRectangle(corner_radius=0.18, width=ancho, height=alto, color=color,
                             stroke_width=3).set_fill(color, 0.15).move_to([centro[0], centro[1], 0])
    rot = MathTex(rotulo, color=TXT).scale(1.1).move_to(marco)
    g = VGroup(marco, rot)
    g.marco, g.rot = marco, rot
    return g


def canal8(centro=(0.0, 0.0), ancho: float = 7.0) -> VGroup:
    """El canal que confunde bits del capítulo 7 (entrada, caja «Canal», salida). `.caja`, `.rot`, `.ent`,
    `.sal`."""
    c = np.array([centro[0], centro[1], 0.0])
    caja_ = RoundedRectangle(corner_radius=0.14, width=2.3, height=1.3, color=INK,
                             stroke_width=3).set_fill(INK, 0.12).move_to(c)
    rot = Text("Canal", color=TXT).scale(0.6).move_to(c)
    mitad = ancho / 2
    ent = Arrow(c + LEFT * mitad, c + LEFT * 1.15, color=SENAL, buff=0, stroke_width=4,
                max_tip_length_to_length_ratio=0.2)
    sal = Arrow(c + RIGHT * 1.15, c + RIGHT * mitad, color=MEDIDA, buff=0, stroke_width=4,
                max_tip_length_to_length_ratio=0.2)
    g = VGroup(caja_, rot, ent, sal)
    g.caja, g.rot, g.ent, g.sal = caja_, rot, ent, sal
    return g


def barras8(valores, rotulos, centro=(0.0, 0.0), ancho: float = 5.0, alto: float = 3.0, v_max: float = 4.0,
            colores=None, textos=None):
    """Barras verticales con rótulo debajo y valor encima. Devuelve un dict con `base`, `barras`, `rots`,
    `vals` (listas) para animarlas de a una."""
    n = len(valores)
    paso = ancho / n
    base_y = centro[1] - alto / 2
    d = {"base": Line([centro[0] - ancho / 2, base_y, 0], [centro[0] + ancho / 2, base_y, 0], color=INK,
                      stroke_width=2), "barras": [], "rots": [], "vals": []}
    for i, v in enumerate(valores):
        x = centro[0] - ancho / 2 + (i + 0.5) * paso
        h = max(0.04, v / v_max * alto)
        col = colores[i] if colores else ERROR
        b = Rectangle(width=paso * 0.55, height=h, color=col, stroke_width=0).set_fill(col, 0.85)
        b.move_to([x, base_y + h / 2, 0])
        r = Text(rotulos[i], color=INK).scale(0.45).move_to([x, base_y - 0.32, 0])
        vt = Text(textos[i] if textos else num(v), color=TXT).scale(0.5).next_to(b, UP, buff=0.12)
        d["barras"].append(b), d["rots"].append(r), d["vals"].append(vt)
    return d
