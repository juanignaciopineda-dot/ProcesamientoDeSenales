"""Escena 6 - La interpretacion vectorial: proyeccion ortogonal.

Pensando las variables centradas como vectores con producto interno
E[XY], buscar el a que minimiza ||Y - aX||^2 es literalmente proyectar
Y sobre la direccion de X. Y rho resulta ser el coseno del angulo.

    manim -pql s06_ortogonalidad.py Ortogonalidad
"""
from manim import *
import numpy as np
from comun import *

ORIG = LEFT * 2.6 + DOWN * 1.4
LX = 3.6            # largo del vector X (= sigma_X)
LY = 2.9            # largo del vector Y (= sigma_Y)
THETA = 0.72        # angulo entre ambos (rho = cos theta)


class Ortogonalidad(Scene):
    def construct(self):
        configurar()

        tit = titulo("El mismo problema, visto como geometría")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el diccionario
        dicc = VGroup(
            MathTex(r"\langle X,Y\rangle \;=\; E[XY]", color=TXT).scale(0.7),
            MathTex(r"\|\tilde{X}\|^2 = \sigma_X^2 \qquad "
                    r"\|\tilde{Y}\|^2 = \sigma_Y^2", color=INK).scale(0.62),
        ).arrange(DOWN, buff=0.24)
        dicc.next_to(tit, DOWN, buff=0.38)
        self.play(Write(dicc[0]))
        self.wait(0.6)
        self.play(FadeIn(dicc[1]))
        self.wait(1.4)
        self.play(dicc.animate.scale(0.8).to_corner(UR, buff=0.55))

        # ------------------------------------------------ los dos vectores
        origen = Dot(ORIG, color=INK, radius=0.05)
        vec_x = Arrow(ORIG, ORIG + RIGHT * LX, color=AZUL, buff=0,
                      stroke_width=6, max_tip_length_to_length_ratio=0.09)
        vec_y = Arrow(ORIG, ORIG + np.array([LY * np.cos(THETA),
                                             LY * np.sin(THETA), 0]),
                      color=VERDE, buff=0, stroke_width=6,
                      max_tip_length_to_length_ratio=0.11)
        lx = MathTex(r"\tilde{X}", color=AZUL).scale(0.72)
        lx.next_to(vec_x.get_end(), DR, buff=0.12)
        ly = MathTex(r"\tilde{Y}", color=VERDE).scale(0.72)
        ly.next_to(vec_y.get_end(), UR, buff=0.12)

        self.play(FadeIn(origen))
        self.play(GrowArrow(vec_x), FadeIn(lx))
        self.play(GrowArrow(vec_y), FadeIn(ly))
        self.wait(0.5)

        centradas = nota("los vectores son las variables centradas: "
                         "$\\tilde{X}=X-\\mu_X$", scale=0.44)
        centradas.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(centradas))
        self.wait(1.4)
        self.play(FadeOut(centradas))

        # ------------------------------------------------ el candidato movil
        a = ValueTracker(0.25)

        cand = always_redraw(lambda: Arrow(
            ORIG, ORIG + RIGHT * LX * a.get_value(), color=AMBAR, buff=0,
            stroke_width=5, max_tip_length_to_length_ratio=0.14))
        error = always_redraw(lambda: Line(
            ORIG + RIGHT * LX * a.get_value(),
            ORIG + np.array([LY * np.cos(THETA), LY * np.sin(THETA), 0]),
            color=ROJO, stroke_width=4))
        cand_lbl = always_redraw(lambda: MathTex(r"a\tilde{X}", color=AMBAR)
                                 .scale(0.6)
                                 .next_to(ORIG + RIGHT * LX * a.get_value(),
                                          DOWN, buff=0.2))
        err_lbl = always_redraw(lambda: MathTex(r"\tilde{Y}-a\tilde{X}",
                                                color=ROJO).scale(0.55)
                                .move_to(Line(
                                    ORIG + RIGHT * LX * a.get_value(),
                                    ORIG + np.array([LY * np.cos(THETA),
                                                     LY * np.sin(THETA), 0])
                                ).get_center() + RIGHT * 0.75 + UP * 0.12))

        self.play(GrowArrow(cand), Create(error), FadeIn(cand_lbl), FadeIn(err_lbl))
        self.wait(0.6)

        # medidor del largo del error
        a_opt = LY * np.cos(THETA) / LX
        largo_max = 2.9

        def largo_err(av):
            p = ORIG + RIGHT * LX * av
            q = ORIG + np.array([LY * np.cos(THETA), LY * np.sin(THETA), 0])
            return float(np.linalg.norm(q - p))

        marco = medidor(alto_max=2.6, ancho=0.45)
        marco.to_edge(RIGHT, buff=1.0).shift(DOWN * 1.0)
        relleno = always_redraw(lambda: relleno_medidor(
            marco, largo_err(a.get_value()) / largo_max, color=ROJO))
        m_lbl = MathTex(r"\|\tilde{Y}-a\tilde{X}\|", color=ROJO).scale(0.5)
        m_lbl.next_to(marco, UP, buff=0.2)
        self.play(FadeIn(marco), FadeIn(relleno), FadeIn(m_lbl))
        self.wait(0.5)

        # ------------------------------------------------ buscar el minimo
        self.play(a.animate.set_value(1.05), run_time=2.2,
                  rate_func=rate_functions.ease_in_out_sine)
        self.play(a.animate.set_value(a_opt), run_time=2.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.4)

        # el angulo recto
        pie_p = ORIG + RIGHT * LX * a_opt
        recto = RightAngle(
            Line(pie_p, ORIG),
            Line(pie_p, ORIG + np.array([LY * np.cos(THETA),
                                         LY * np.sin(THETA), 0])),
            length=0.32, color=AMBAR, stroke_width=3)
        self.play(Create(recto))
        self.play(Flash(pie_p, color=AMBAR, line_length=0.22, num_lines=14))
        self.wait(0.6)

        clave = Text("el error mínimo es perpendicular a la medición",
                     color=AMBAR).scale(0.56)
        clave.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(clave))
        self.wait(1.6)
        self.play(FadeOut(clave))

        # ------------------------------------------------ ortogonalidad
        orto = MathTex(r"E\big[(Y-\hat{Y}_\ell)\,X\big] \;=\; 0",
                       color=AMBAR).scale(0.72)
        orto.to_edge(DOWN, buff=0.75)
        orto_n = nota("condición de ortogonalidad: de acá salen las ecuaciones "
                      "normales", scale=0.44)
        orto_n.next_to(orto, DOWN, buff=0.2)
        self.play(Write(orto), FadeIn(orto_n))
        self.wait(2.0)
        self.play(FadeOut(VGroup(orto, orto_n)))

        # ------------------------------------------------ rho como coseno
        arco = Angle(vec_x, vec_y, radius=0.75, color=MAGENTA, stroke_width=3)
        th_lbl = MathTex(r"\theta", color=MAGENTA).scale(0.6)
        th_lbl.move_to(ORIG + np.array([1.05 * np.cos(THETA / 2),
                                        1.05 * np.sin(THETA / 2), 0]))
        self.play(Create(arco), FadeIn(th_lbl))
        self.wait(0.5)

        cos = MathTex(r"\rho_{Y\!,X} \;=\; \cos\theta", color=MAGENTA).scale(0.8)
        cos.to_edge(DOWN, buff=0.8)
        self.play(Write(cos))
        self.wait(1.6)

        pit = MathTex(r"\|\tilde{Y}-\hat{Y}_\ell\|^2 \;=\;"
                      r"\|\tilde{Y}\|^2\sin^2\theta \;=\;"
                      r"\sigma_Y^2\,(1-\rho^2)", color=VERDE).scale(0.66)
        pit.next_to(cos, DOWN, buff=0.24)
        self.play(Write(pit))
        self.wait(0.6)
        pit_n = nota("Pitágoras, y aparece la misma fórmula del LMMSE",
                     scale=0.44)
        pit_n.next_to(pit, DOWN, buff=0.16)
        self.play(FadeIn(pit_n))
        self.wait(2.4)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(origen, vec_x, vec_y, lx, ly, cand, error,
                                 cand_lbl, err_lbl, marco, relleno, m_lbl,
                                 recto, arco, th_lbl, cos, pit, pit_n, dicc)))
        cierre = VGroup(
            Text("Estimar linealmente", color=INK).scale(0.6),
            Text("=", color=AMBAR).scale(0.7),
            Text("proyectar ortogonalmente", color=VERDE).scale(0.6),
        ).arrange(DOWN, buff=0.24)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.12))
        self.play(FadeIn(cierre[1]))
        self.play(FadeIn(cierre[2], shift=UP * 0.12))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
