"""Escena 5 - El test de razon de verosimilitud.

Reacomodando la regla MAP toda la decision se reduce a comparar un solo
numero, la razon de verosimilitud, contra un umbral. Y eso es lo que
sobrevive cuando se cambia de criterio.

    manim -pql s05_verosimilitud.py RazonVerosimilitud
"""
from manim import *
import numpy as np
from comun import *

A0, A1 = 0.0, 2.6
SIGMA = 0.85
R_MIN, R_MAX = -2.4, 5.4


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def lam(r):
    """Razon de verosimilitud: para gaussianas de igual sigma es exponencial."""
    return np.exp((A1 - A0) * (r - (A0 + A1) / 2) / SIGMA ** 2)


def r_de_eta(eta):
    """El umbral en r que corresponde a un umbral eta en Lambda."""
    return (A0 + A1) / 2 + SIGMA ** 2 * np.log(eta) / (A1 - A0)


class RazonVerosimilitud(Scene):
    def construct(self):
        configurar()

        tit = titulo("El test de razón de verosimilitud")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el despeje
        p1 = MathTex(r"p_1\,f(r|H_1)", r"\;\gtrless\;", r"p_0\,f(r|H_0)",
                     color=TXT).scale(0.75)
        p1[0].set_color(VERDE); p1[2].set_color(AZUL)
        p1.next_to(tit, DOWN, buff=0.5)
        self.play(Write(p1))
        self.wait(1.0)

        p2 = MathTex(r"\underbrace{\frac{f(r|H_1)}{f(r|H_0)}}_{\Lambda(r)}",
                     r"\;\gtrless\;",
                     r"\underbrace{\frac{p_0}{p_1}}_{\eta}", color=TXT).scale(0.85)
        p2[0].set_color(AMBAR); p2[2].set_color(ROJO)
        p2.move_to(p1)
        self.play(TransformMatchingShapes(p1, p2), run_time=1.4)
        self.wait(1.0)

        n = nota("todo lo que depende de la medición queda de un lado; "
                 "todo lo que se conoce de antemano, del otro", scale=0.46)
        n.next_to(p2, DOWN, buff=0.32)
        self.play(FadeIn(n))
        self.wait(2.0)
        self.play(FadeOut(n), p2.animate.scale(0.65).to_edge(UP, buff=1.1))

        # ------------------------------------------------ los dos paneles
        ax_d, lab_d = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 0.52], ancho=4.9,
                           alto=2.4, x_label="r")
        ax_d.shift(LEFT * 3.4 + DOWN * 0.75)
        lab_d.next_to(ax_d.x_axis.get_end(), DR, buff=0.08)
        t_d = subtitulo("las dos densidades", scale=0.46)
        t_d.next_to(ax_d, UP, buff=0.22)

        ax_l, lab_l = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 12], ancho=4.9,
                           alto=2.4, x_label="r")
        ax_l.shift(RIGHT * 3.4 + DOWN * 0.75)
        lab_l.next_to(ax_l.x_axis.get_end(), DR, buff=0.08)
        t_l = MathTex(r"\Lambda(r)", color=AMBAR).scale(0.62)
        t_l.next_to(ax_l, UP, buff=0.22)

        self.play(Create(ax_d), FadeIn(lab_d), FadeIn(t_d),
                  Create(ax_l), FadeIn(lab_l), FadeIn(t_l))

        f0 = ax_d.plot(lambda r: g(r, A0), x_range=[R_MIN, R_MAX, 0.02],
                       color=AZUL, stroke_width=3.5)
        f1 = ax_d.plot(lambda r: g(r, A1), x_range=[R_MIN, R_MAX, 0.02],
                       color=VERDE, stroke_width=3.5)
        curva_l = ax_l.plot(lam, x_range=[R_MIN, R_MAX, 0.02], color=AMBAR,
                            stroke_width=4)
        self.play(Create(f0), Create(f1))
        self.play(Create(curva_l, run_time=1.5))
        self.wait(0.6)

        crece = nota("$\\Lambda$ crece con $r$: cuanto más grande, más a favor "
                     "de $H_1$", scale=0.44)
        crece.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(crece))
        self.wait(1.6)
        self.play(FadeOut(crece))

        # ------------------------------------------------ el umbral eta
        eta = ValueTracker(1.0)

        linea_eta = always_redraw(lambda: DashedLine(
            ax_l.c2p(R_MIN, min(11.8, eta.get_value())),
            ax_l.c2p(R_MAX, min(11.8, eta.get_value())),
            color=ROJO, stroke_width=3, dash_length=0.09))
        eta_lbl = always_redraw(lambda: MathTex(r"\eta", color=ROJO).scale(0.6)
                                .next_to(ax_l.c2p(R_MIN, min(11.8, eta.get_value())),
                                         LEFT, buff=0.12))
        umbral_d = always_redraw(lambda: DashedLine(
            ax_d.c2p(r_de_eta(eta.get_value()), 0),
            ax_d.c2p(r_de_eta(eta.get_value()), 0.50),
            color=ROJO, stroke_width=3, dash_length=0.09))
        umbral_l = always_redraw(lambda: DashedLine(
            ax_l.c2p(r_de_eta(eta.get_value()), 0),
            ax_l.c2p(r_de_eta(eta.get_value()), min(11.8, eta.get_value())),
            color=ROJO, stroke_width=2, dash_length=0.07))
        punto = always_redraw(lambda: Dot(
            ax_l.c2p(r_de_eta(eta.get_value()), min(11.8, eta.get_value())),
            color=ROJO, radius=0.07))

        self.play(Create(linea_eta), FadeIn(eta_lbl))
        self.play(Create(umbral_l), FadeIn(punto), Create(umbral_d))
        self.wait(0.6)

        equiv = nota("fijar un umbral sobre $\\Lambda$ equivale a fijar un "
                     "umbral sobre $r$", scale=0.46)
        equiv.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(equiv))
        self.wait(1.8)
        self.play(FadeOut(equiv))

        valor = always_redraw(lambda: VGroup(
            MathTex(r"\eta =", color=ROJO).scale(0.55),
            DecimalNumber(eta.get_value(), num_decimal_places=2,
                          color=ROJO).scale(0.55),
        ).arrange(RIGHT, buff=0.12).to_edge(DOWN, buff=0.95))
        self.play(FadeIn(valor))

        self.play(eta.animate.set_value(6.0), run_time=2.4,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.6)
        self.play(eta.animate.set_value(0.22), run_time=2.6,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.6)
        self.play(eta.animate.set_value(1.0), run_time=1.5)

        # ------------------------------------------------ lo importante
        clave = VGroup(
            Text("Cambiar de criterio NO cambia la forma del test.",
                 color=TXT).scale(0.52),
            Text("Solo cambia dónde se pone η.", color=AMBAR).scale(0.52),
        ).arrange(DOWN, buff=0.16)
        clave.to_edge(DOWN, buff=0.4)
        self.play(FadeOut(valor), FadeIn(clave))
        self.wait(2.2)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax_d, lab_d, t_d, f0, f1, ax_l, lab_l, t_l,
                                 curva_l, linea_eta, eta_lbl, umbral_d,
                                 umbral_l, punto, clave, p2)))
        cierre = VGroup(
            MathTex(r"\Lambda(r)=\frac{f(r|H_1)}{f(r|H_0)}"
                    r"\;\underset{H_0}{\overset{H_1}{\gtrless}}\;\eta",
                    color=AMBAR).scale(0.95),
            nota("MAP, Neyman–Pearson y riesgo mínimo son todos este test. "
                 "Solo difieren en η.", scale=0.52),
        ).arrange(DOWN, buff=0.5)
        cierre.move_to(ORIGIN)
        self.play(Write(cierre[0]))
        self.wait(0.6)
        self.play(FadeIn(cierre[1]))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
