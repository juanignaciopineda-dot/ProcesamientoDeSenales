"""Escena 2 - La condicion de ortogonalidad.

Es la idea que unifica las tres versiones del filtro de Wiener: el error
del mejor estimador lineal tiene que ser ORTOGONAL a todos los datos.
De ahi salen las ecuaciones normales.

    manim -pql s02_ortogonalidad.py Ortogonalidad
"""
from manim import *
import numpy as np
from comun import *


class Ortogonalidad(Scene):
    def construct(self):
        configurar()

        tit = titulo("La condición de ortogonalidad")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        recordatorio = nota("del capítulo 7: las variables aleatorias se "
                            "comportan como vectores, con "
                            r"$\langle X,Y\rangle = E[XY]$", scale=0.5)
        recordatorio.next_to(tit, DOWN, buff=0.3)
        self.play(FadeIn(recordatorio))
        self.wait(1.6)
        self.play(FadeOut(recordatorio))

        # ============================================ el dibujo geometrico
        centro = LEFT * 3.3 + DOWN * 0.5

        # el "plano" de los datos disponibles, dibujado en perspectiva
        plano = Polygon(
            centro + np.array([-2.5, -0.85, 0]),
            centro + np.array([1.9, -1.55, 0]),
            centro + np.array([2.5, 0.55, 0]),
            centro + np.array([-1.9, 1.25, 0]),
            color=INK, stroke_width=2, fill_color=INK, fill_opacity=0.07)
        plano_lbl = nota("todo lo que puedo construir\ncon las mediciones",
                         scale=0.42)
        plano_lbl.next_to(plano, DOWN, buff=0.22)

        self.play(Create(plano), FadeIn(plano_lbl))
        self.wait(0.6)

        origen = centro + np.array([-1.0, -0.55, 0])
        punta_y = centro + np.array([0.55, 2.15, 0])
        punta_h = centro + np.array([1.15, 0.05, 0])

        v_y = Arrow(origen, punta_y, color=VERDE, buff=0, stroke_width=5,
                    max_tip_length_to_length_ratio=0.13)
        v_h = Arrow(origen, punta_h, color=AZUL, buff=0, stroke_width=5,
                    max_tip_length_to_length_ratio=0.15)
        v_e = Arrow(punta_h, punta_y, color=ROJO, buff=0, stroke_width=5,
                    max_tip_length_to_length_ratio=0.15)

        l_y = MathTex("Y", color=VERDE).scale(0.72).next_to(punta_y, UP, buff=0.12)
        l_h = MathTex(r"\hat{Y}", color=AZUL).scale(0.72).next_to(punta_h, DR, buff=0.1)
        l_e = MathTex(r"Y-\hat{Y}", color=ROJO).scale(0.62)
        l_e.next_to(VGroup(v_e).get_center(), RIGHT, buff=0.22)

        self.play(GrowArrow(v_y), FadeIn(l_y))
        n1 = nota("lo que quiero estimar: no vive en el plano", scale=0.42)
        n1.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(n1))
        self.wait(1.3)
        self.play(FadeOut(n1))

        self.play(GrowArrow(v_h), FadeIn(l_h))
        self.play(GrowArrow(v_e), FadeIn(l_e))
        self.wait(0.6)

        # el angulo recto
        d = 0.28
        u = (punta_h - origen) / np.linalg.norm(punta_h - origen)
        w = (punta_y - punta_h) / np.linalg.norm(punta_y - punta_h)
        esq = punta_h - u * d + w * d
        recto = VMobject(color=AMBAR, stroke_width=3).set_points_as_corners(
            [punta_h - u * d, esq, punta_h + w * d])
        self.play(Create(recto))

        n2 = nota("el mejor estimador es la PROYECCIÓN ORTOGONAL", scale=0.5)
        n2.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(n2))
        self.wait(1.8)
        self.play(FadeOut(n2))

        # ============================================ el argumento
        arg = VGroup(
            Text("¿Por qué ortogonal?", color=TXT).scale(0.58),
            nota("Si el error tuviera alguna componente dentro del plano,", scale=0.46),
            nota("podría restársela y achicar el error. Contradicción.", scale=0.46),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        arg.move_to(RIGHT * 3.2 + UP * 1.35)
        for m in arg:
            self.play(FadeIn(m, shift=RIGHT * 0.15), run_time=0.7)
        self.wait(1.4)

        # ============================================ la ecuacion
        cond = MathTex(r"E\big[\,(Y-\hat{Y})\;X_i\,\big] \;=\; 0",
                       color=AMBAR).scale(0.85)
        cond.move_to(RIGHT * 3.2 + DOWN * 0.35)
        cond_n = nota("para TODA medición disponible", scale=0.46)
        cond_n.next_to(cond, DOWN, buff=0.2)
        self.play(Write(cond))
        self.play(FadeIn(cond_n))
        self.wait(1.6)

        flecha_abajo = MathTex(r"\Downarrow", color=INK).scale(0.9)
        flecha_abajo.next_to(cond_n, DOWN, buff=0.22)
        normales = MathTex(r"C_{XX}\,\mathbf{a} = \mathbf{c}_{XY}",
                           color=AZUL).scale(0.85)
        normales.next_to(flecha_abajo, DOWN, buff=0.22)
        norm_n = nota("las ecuaciones normales", scale=0.46)
        norm_n.next_to(normales, DOWN, buff=0.16)
        self.play(FadeIn(flecha_abajo))
        self.play(Write(normales), FadeIn(norm_n))
        self.wait(2.2)

        # ============================================ cierre
        self.play(FadeOut(VGroup(plano, plano_lbl, v_y, v_h, v_e, l_y, l_h,
                                 l_e, recto, arg, cond, cond_n, flecha_abajo,
                                 normales, norm_n)))
        cierre = VGroup(
            Text("Esta única condición genera las tres versiones del filtro:",
                 color=TXT).scale(0.58),
            VGroup(
                Text("FIR", color=AZUL, weight=BOLD).scale(0.55),
                Text("ortogonal a las L muestras usadas", color=INK).scale(0.48),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("no causal", color=AMBAR, weight=BOLD).scale(0.55),
                Text("ortogonal a TODO el registro", color=INK).scale(0.48),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("causal", color=VERDE, weight=BOLD).scale(0.55),
                Text("ortogonal solo al pasado y al presente", color=INK).scale(0.48),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.wait(0.4)
        for m in cierre[1:]:
            self.play(FadeIn(m, shift=RIGHT * 0.15), run_time=0.65)
        self.wait(2.3)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
