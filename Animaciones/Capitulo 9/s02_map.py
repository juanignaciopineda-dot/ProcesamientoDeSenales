"""Escena 2 - La regla MAP.

Para minimizar la probabilidad de error hay que decidir por la hipotesis
mas probable DESPUES de medir. Con Bayes eso se reduce a comparar las
densidades escaladas por sus probabilidades a priori.

    manim -pql s02_map.py ReglaMAP
"""
from manim import *
import numpy as np
from comun import *

A0, A1 = 0.0, 2.6
SIGMA = 0.85
R_MIN, R_MAX = -3.4, 6.0


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def cruce(p0):
    """Donde p0*f0 = p1*f1. Sale de igualar los exponentes."""
    p1 = 1 - p0
    return (A0 + A1) / 2 + SIGMA ** 2 * np.log(p0 / p1) / (A1 - A0)


class ReglaMAP(Scene):
    def construct(self):
        configurar()

        tit = titulo("La regla MAP: decidir por la más probable")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el razonamiento
        paso1 = MathTex(r"P(H_1\,|\,R=r)", r"\;\gtrless\;", r"P(H_0\,|\,R=r)",
                        color=TXT).scale(0.72)
        paso1[0].set_color(VERDE); paso1[2].set_color(AZUL)
        paso1.next_to(tit, DOWN, buff=0.45)
        n1 = nota("comparar las probabilidades a posteriori", scale=0.44)
        n1.next_to(paso1, DOWN, buff=0.16)
        self.play(Write(paso1), FadeIn(n1))
        self.wait(1.4)

        bayes = MathTex(r"P(H_i\,|\,R=r) = \frac{f(r\,|\,H_i)\,P(H_i)}{f_R(r)}",
                        color=INK).scale(0.62)
        bayes.next_to(n1, DOWN, buff=0.35)
        self.play(FadeIn(bayes))
        self.wait(1.2)

        tacha = Line(bayes.get_corner(DL) + RIGHT * 1.55 + UP * 0.02,
                     bayes.get_corner(DR) + LEFT * 0.15 + UP * 0.02,
                     color=ROJO, stroke_width=3)
        n_com = nota("el denominador es el mismo de los dos lados: se cancela",
                     scale=0.44)
        n_com.next_to(bayes, DOWN, buff=0.2)
        self.play(Create(tacha), FadeIn(n_com))
        self.wait(1.6)

        paso2 = MathTex(r"p_1\,f(r\,|\,H_1)", r"\;\gtrless\;", r"p_0\,f(r\,|\,H_0)",
                        color=TXT).scale(0.78)
        paso2[0].set_color(VERDE); paso2[2].set_color(AZUL)
        paso2.move_to(paso1)
        self.play(FadeOut(VGroup(bayes, tacha, n_com, n1)),
                  TransformMatchingShapes(paso1, paso2))
        n2 = nota("densidades escaladas por sus probabilidades a priori",
                  scale=0.44)
        n2.next_to(paso2, DOWN, buff=0.16)
        self.play(FadeIn(n2))
        self.wait(1.6)
        self.play(VGroup(paso2, n2).animate.scale(0.72).to_edge(UP, buff=1.15))

        # ------------------------------------------------ el dibujo
        p0 = ValueTracker(0.5)

        ax, lab = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 0.42], ancho=8.6,
                       alto=2.7, x_label="r")
        ax.shift(DOWN * 0.85)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        c0 = always_redraw(lambda: ax.plot(
            lambda r: p0.get_value() * g(r, A0), x_range=[R_MIN, R_MAX, 0.02],
            color=AZUL, stroke_width=4))
        c1 = always_redraw(lambda: ax.plot(
            lambda r: (1 - p0.get_value()) * g(r, A1),
            x_range=[R_MIN, R_MAX, 0.02], color=VERDE, stroke_width=4))
        a0 = always_redraw(lambda: ax.get_area(
            ax.plot(lambda r: p0.get_value() * g(r, A0),
                    x_range=[R_MIN, R_MAX, 0.02]),
            x_range=(R_MIN, R_MAX), color=AZUL, opacity=0.13, stroke_width=0))
        a1 = always_redraw(lambda: ax.get_area(
            ax.plot(lambda r: (1 - p0.get_value()) * g(r, A1),
                    x_range=[R_MIN, R_MAX, 0.02]),
            x_range=(R_MIN, R_MAX), color=VERDE, opacity=0.13, stroke_width=0))
        self.play(FadeIn(c0), FadeIn(a0), FadeIn(c1), FadeIn(a1))
        self.wait(0.5)

        # ------------------------------------------------ el umbral
        umbral = always_redraw(lambda: DashedLine(
            ax.c2p(cruce(p0.get_value()), 0), ax.c2p(cruce(p0.get_value()), 0.40),
            color=ROJO, stroke_width=3.5, dash_length=0.1))
        u_lbl = always_redraw(lambda: MathTex(r"\gamma", color=ROJO).scale(0.66)
                              .next_to(ax.c2p(cruce(p0.get_value()), 0), DOWN,
                                       buff=0.2))
        self.play(Create(umbral), FadeIn(u_lbl))

        d0 = always_redraw(lambda: texto("decido $H_0$", color=AZUL, scale=0.5)
                           .move_to(ax.c2p((R_MIN + cruce(p0.get_value())) / 2,
                                           0.335)))
        d1 = always_redraw(lambda: texto("decido $H_1$", color=VERDE, scale=0.5)
                           .move_to(ax.c2p((R_MAX + cruce(p0.get_value())) / 2,
                                           0.335)))
        self.play(FadeIn(d0), FadeIn(d1))
        self.wait(1.0)

        valor = always_redraw(lambda: VGroup(
            MathTex("p_0 =", color=AZUL).scale(0.58),
            DecimalNumber(p0.get_value(), num_decimal_places=2,
                          color=AZUL).scale(0.58),
            MathTex(r"\quad p_1 =", color=VERDE).scale(0.58),
            DecimalNumber(1 - p0.get_value(), num_decimal_places=2,
                          color=VERDE).scale(0.58),
        ).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.5))
        self.play(FadeIn(valor))
        self.wait(0.6)

        # ------------------------------------------------ mover los priors
        m1 = nota("si $H_0$ se vuelve más probable, el umbral se corre "
                  "hacia la derecha…", scale=0.46)
        m1.next_to(valor, UP, buff=0.22)
        self.play(FadeIn(m1))
        self.play(p0.animate.set_value(0.85), run_time=2.6,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(1.2)

        m2 = nota("…y al revés: hay que exigirle más evidencia a la hipótesis "
                  "poco probable", scale=0.46)
        m2.move_to(m1)
        self.play(FadeOut(m1), FadeIn(m2))
        self.play(p0.animate.set_value(0.18), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(1.4)
        self.play(p0.animate.set_value(0.5), run_time=1.6)
        self.play(FadeOut(m2))

        eq = nota("con $p_0=p_1$ el umbral queda justo en el medio", scale=0.46)
        eq.move_to(m1)
        self.play(FadeIn(eq))
        self.wait(1.6)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, c0, c1, a0, a1, umbral, u_lbl,
                                 d0, d1, valor, eq, paso2, n2)))
        cierre = VGroup(
            Text("Regla MAP", color=AMBAR, weight=BOLD).scale(0.75),
            Text("elegir la hipótesis con mayor probabilidad a posteriori",
                 color=TXT).scale(0.58),
            nota("es la que minimiza la probabilidad de error, y todo el "
                 "capítulo sale de acá", scale=0.5),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1]))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
