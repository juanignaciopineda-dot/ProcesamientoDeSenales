"""Escena 8 - Varias mediciones: las ecuaciones normales.

Con L mediciones X_1..X_L el estimador afin es una combinacion lineal.
La condicion de ortogonalidad (error perpendicular a CADA medicion) da
un sistema L x L: las ecuaciones normales, C_XX a = c_XY.

    manim -pql s08_multiples.py Multiples
"""
from manim import *
import numpy as np
from comun import *


class Multiples(Scene):
    def construct(self):
        configurar()

        tit = titulo("Varias mediciones a la vez")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el estimador
        est = MathTex(r"\hat{Y}_\ell \;=\; a_0 \;+\; \sum_{j=1}^{L}"
                      r"a_j\,\big(X_j - \mu_{X_j}\big)", color=TXT).scale(0.8)
        est.next_to(tit, DOWN, buff=0.45)
        est_n = nota("una combinación lineal (más constante) de todo lo que medí",
                     scale=0.46)
        est_n.next_to(est, DOWN, buff=0.2)
        self.play(Write(est))
        self.play(FadeIn(est_n))
        self.wait(1.6)
        self.play(FadeOut(est_n), est.animate.scale(0.78).to_edge(UP, buff=1.2))

        # ------------------------------------------------ la idea vectorial
        idea = VGroup(
            Text("El error tiene que ser perpendicular a", color=INK).scale(0.55),
            Text("CADA una de las mediciones", color=AMBAR, weight=BOLD).scale(0.58),
        ).arrange(RIGHT, buff=0.22)
        idea.next_to(est, DOWN, buff=0.5)
        self.play(FadeIn(idea))
        self.wait(1.0)

        cond = MathTex(r"E\big[(Y-\hat{Y}_\ell)\,X_i\big] \;=\; 0"
                       r"\qquad i=1,\dots,L", color=VERDE).scale(0.72)
        cond.next_to(idea, DOWN, buff=0.4)
        self.play(Write(cond))
        self.wait(1.2)
        cond_n = nota("una ecuación por cada medición  →  L ecuaciones, L incógnitas",
                      scale=0.44)
        cond_n.next_to(cond, DOWN, buff=0.2)
        self.play(FadeIn(cond_n))
        self.wait(2.0)
        self.play(FadeOut(VGroup(idea, cond, cond_n)))

        # ------------------------------------------------ las ecuaciones normales
        sistema = MathTex(
            r"\begin{bmatrix}"
            r"\sigma_{X_1X_1} & \cdots & \sigma_{X_1X_L}\\"
            r"\vdots & \ddots & \vdots\\"
            r"\sigma_{X_LX_1} & \cdots & \sigma_{X_LX_L}"
            r"\end{bmatrix}"
            r"\begin{bmatrix} a_1\\ \vdots\\ a_L\end{bmatrix}"
            r"\;=\;"
            r"\begin{bmatrix}\sigma_{X_1Y}\\ \vdots\\ \sigma_{X_LY}\end{bmatrix}",
            color=TXT).scale(0.68)
        sistema.move_to(ORIGIN).shift(UP * 0.35)
        self.play(Write(sistema, run_time=2.0))
        self.wait(0.8)

        etq = VGroup(
            Text("matriz de covarianzas", color=AZUL).scale(0.42),
            Text("de las mediciones entre sí", color=AZUL).scale(0.42),
        ).arrange(DOWN, buff=0.05)
        etq.next_to(sistema, DOWN, buff=0.55).shift(LEFT * 2.6)
        etq2 = VGroup(
            Text("covarianzas de cada", color=VERDE).scale(0.42),
            Text("medición con Y", color=VERDE).scale(0.42),
        ).arrange(DOWN, buff=0.05)
        etq2.next_to(sistema, DOWN, buff=0.55).shift(RIGHT * 3.0)
        self.play(FadeIn(etq), FadeIn(etq2))
        self.wait(1.6)
        self.play(FadeOut(VGroup(etq, etq2)))

        # ------------------------------------------------ forma compacta
        compacta = MathTex(r"C_{XX}\,\mathbf{a} \;=\; \mathbf{c}_{XY}",
                           color=AMBAR).scale(0.95)
        compacta.next_to(sistema, DOWN, buff=0.55)
        self.play(TransformFromCopy(sistema, compacta))
        self.wait(0.6)
        sol = MathTex(r"\mathbf{a} \;=\; C_{XX}^{-1}\,\mathbf{c}_{XY}",
                      color=VERDE).scale(0.85)
        sol.next_to(compacta, DOWN, buff=0.3)
        self.play(Write(sol))
        self.wait(2.0)

        # ------------------------------------------------ el detalle fino
        self.play(FadeOut(VGroup(sistema, compacta, sol)))
        cab = VGroup(
            Text("Lo que hace la matriz", color=INK).scale(0.5),
            MathTex(r"C_{XX}", color=AZUL).scale(0.6),
        ).arrange(RIGHT, buff=0.18)
        detalle = VGroup(
            cab,
            nota("si dos mediciones están muy correlacionadas entre sí "
                 "(redundantes),", scale=0.5),
            nota("el sistema lo detecta y reparte el peso para no contar "
                 "dos veces la misma información", scale=0.5),
        ).arrange(DOWN, buff=0.28)
        detalle.move_to(UP * 0.3)
        for linea in detalle:
            self.play(FadeIn(linea, shift=UP * 0.1))
            self.wait(0.4)
        self.wait(1.6)

        conexion = nota("es el mismo sistema que después resolvés —bajo otro "
                        "nombre— en filtrado de Wiener,\narrays de antenas o "
                        "ecualización de canales", scale=0.46)
        conexion.next_to(detalle, DOWN, buff=0.6)
        self.play(FadeIn(conexion))
        self.wait(2.4)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(detalle, conexion, est)))
        cierre = VGroup(
            Text("Todo el capítulo, en una idea:", color=INK).scale(0.55),
            Text("el mejor estimador lineal es una proyección,", color=TXT).scale(0.6),
            Text("y proyectar es resolver un sistema de covarianzas.",
                 color=VERDE).scale(0.6),
        ).arrange(DOWN, buff=0.26)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.1))
        self.play(FadeIn(cierre[2], shift=UP * 0.1))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
