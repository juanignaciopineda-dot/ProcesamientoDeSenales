"""Piezas del capítulo 8, episodio 4 («La sombra de una flecha»).

Van en un módulo aparte (y no al final de `figuras.py`) porque varias sesiones editan `figuras.py` a la vez
y una sobrescribe a la otra. Las escenas del E4 lo importan con `from comun.figuras_c8e4 import *`.
"""
from __future__ import annotations

import numpy as np
from manim import *

from comun.estilo import *
from comun.figuras import Flechas

K8 = 2.6                                   # unidades de pantalla por unidad de desviación típica
ANG8 = float(np.degrees(np.arccos(2 / np.sqrt(5))))   # ≈ 26,57°: el ángulo entre la temperatura y la lectura
ORIGEN8 = (-6.3, -2.5)


def flechas8(origen=ORIGEN8, k: float = K8):
    """El termómetro como flechas: la lectura X (cian, largo √5) y la temperatura Y (azul, largo 2), a ≈ 27°.
    Devuelve `(F, rotulos)`: `F` es un `Flechas` (`.presente` = X, `.futuro` = Y, `.sombra`, `.error`, `.recto`)
    y `rotulos` un dict de MathTex con las claves `x`, `y`, `yh` (ŷ) y `e`."""
    F = Flechas(origen=origen, largo=np.sqrt(5) * k, angulo=ANG8, largo_objetivo=2 * k,
                color_dato=MEDIDA, color_objetivo=SENAL)
    rx = MathTex("X", color=MEDIDA).scale(0.9).next_to(F.fin_presente, RIGHT, buff=0.15)
    ry = MathTex("Y", color=SENAL).scale(0.9).next_to(F.fin_futuro, UP, buff=0.12)
    ryh = MathTex(r"\hat{y}", color=ESTIMACION).scale(0.9).move_to((F.fin_sombra + F.o) / 2 + DOWN * 0.4)
    re = MathTex("e", color=ERROR).scale(0.9).next_to((F.fin_sombra + F.fin_futuro) / 2, RIGHT, buff=0.15)
    return F, {"x": rx, "y": ry, "yh": ryh, "e": re}


def en_recta8(F, h: float) -> np.ndarray:
    """El punto h · X sobre la recta de la lectura."""
    return F.o + h * (F.fin_presente - F.o)


class AnguloVivo8(VGroup):
    """El dibujo de flechas con el ángulo como parámetro (`tr`, un ValueTracker en grados): la lectura X queda
    quieta y la temperatura Y gira (largo fijo 2k). Atributos: `.x_flecha`, `.y_flecha`, `.sombra`, `.error`,
    `.recto`, `.arco` (todo con `always_redraw`), `.rx`, `.ry`, `.rth` (rótulos con updaters) y `.todo`
    (el grupo que se agrega a la escena). `.apagar()` quita los updaters antes de sacar el grupo."""

    def __init__(self, tr: ValueTracker, origen=ORIGEN8, k: float = K8):
        super().__init__()
        self.tr, self.o, self.k = tr, np.array([origen[0], origen[1], 0.0]), k
        o = self.o
        self.fin_x = o + np.array([np.sqrt(5) * k, 0.0, 0.0])
        self.x_flecha = Arrow(o, self.fin_x, buff=0, color=MEDIDA, stroke_width=6, max_tip_length_to_length_ratio=0.12)

        def punta():
            a = np.deg2rad(tr.get_value())
            return o + 2 * k * np.array([np.cos(a), np.sin(a), 0.0])

        def pie():
            return o + np.array([punta()[0] - o[0], 0.0, 0.0])

        self._punta, self._pie = punta, pie
        self.y_flecha = always_redraw(lambda: Arrow(o, punta(), buff=0, color=SENAL, stroke_width=6,
                                                    max_tip_length_to_length_ratio=0.12))
        self.sombra = always_redraw(lambda: Line(o, pie() + RIGHT * 0.001, color=ESTIMACION, stroke_width=11))
        self.error = always_redraw(lambda: Line(pie(), punta(), color=ERROR, stroke_width=5))

        def recto():
            p, q = pie(), punta()
            largo = q[1] - p[1]
            if largo < 0.3 or q[0] - o[0] < 0.01:
                return VMobject()
            s = min(0.22, largo * 0.45)
            m = VMobject(stroke_color=ERROR, stroke_width=3).set_fill(opacity=0)
            m.set_points_as_corners([p + [-s, 0, 0], p + [-s, s, 0], p + [0, s, 0]])
            return m

        self.recto = always_redraw(recto)
        self.arco = always_redraw(lambda: Arc(radius=1.0, start_angle=0, angle=np.deg2rad(max(tr.get_value(), 0.5)),
                                              arc_center=o, color=AMBAR, stroke_width=4))
        self.rx = MathTex("X", color=MEDIDA).scale(0.9).next_to(self.fin_x, RIGHT, buff=0.15)
        self.ry = MathTex("Y", color=SENAL).scale(0.9)
        self.ry.add_updater(lambda m: m.move_to(punta() + np.array([0.05, 0.4, 0.0])))
        self.rth = MathTex(r"\theta", color=AMBAR).scale(0.8)
        self.rth.add_updater(lambda m: m.move_to(o + 1.5 * np.array(
            [np.cos(np.deg2rad(max(tr.get_value(), 3) / 2)), np.sin(np.deg2rad(max(tr.get_value(), 3) / 2)), 0.0])))
        self.ry.update(0)
        self.rth.update(0)
        self.todo = VGroup(self.x_flecha, self.y_flecha, self.sombra, self.error, self.recto, self.arco,
                           self.rx, self.ry, self.rth)

    def apagar(self) -> None:
        for m in (self.ry, self.rth):
            m.clear_updaters()
