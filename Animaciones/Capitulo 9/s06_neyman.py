"""Escena 6 - El criterio de Neyman-Pearson.

Cuando no se conocen las probabilidades a priori (que es lo habitual),
se fija una cota tolerable para PFA y se maximiza PD sujeto a eso.

    manim -pql s06_neyman.py NeymanPearson
"""
from manim import *
import numpy as np
from comun import *

A0, A1 = 0.0, 2.6
SIGMA = 0.85
R_MIN, R_MAX = -3.0, 6.0


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    from math import erfc, sqrt
    return 0.5 * erfc(x / sqrt(2))


def pfa(gam):
    return Q((gam - A0) / SIGMA)


def pd(gam):
    return Q((gam - A1) / SIGMA)


def gamma_para_pfa(objetivo):
    """Umbral que da exactamente ese PFA (busqueda binaria)."""
    lo, hi = R_MIN - 4, R_MAX + 4
    for _ in range(60):
        mid = (lo + hi) / 2
        if pfa(mid) > objetivo:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


class NeymanPearson(Scene):
    def construct(self):
        configurar()

        tit = titulo("Neyman–Pearson: cuando no conocés los a priori")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el problema
        prob = VGroup(
            texto("La regla MAP necesita $p_0$ y $p_1$.", color=TXT, scale=0.6),
            nota("¿Cuál es la probabilidad a priori de que haya un avión?",
                 scale=0.5),
            nota("¿Y de que este paciente tenga la enfermedad?", scale=0.5),
        ).arrange(DOWN, buff=0.24)
        prob.next_to(tit, DOWN, buff=0.55)
        self.play(FadeIn(prob[0]))
        self.wait(0.7)
        self.play(FadeIn(prob[1]))
        self.play(FadeIn(prob[2]))
        self.wait(1.6)

        salida = VGroup(
            Text("Muchas veces no se sabe. La salida:", color=TXT).scale(0.58),
            VGroup(
                Text("fijar una cota para", color=INK).scale(0.55),
                MathTex(r"P_{FA}\leq\alpha", color=ROJO).scale(0.72),
            ).arrange(RIGHT, buff=0.25),
            VGroup(
                Text("y maximizar", color=INK).scale(0.55),
                MathTex(r"P_D", color=VERDE).scale(0.72),
                Text("sujeto a eso", color=INK).scale(0.55),
            ).arrange(RIGHT, buff=0.25),
        ).arrange(DOWN, buff=0.28)
        salida.next_to(prob, DOWN, buff=0.55)
        self.play(FadeIn(salida[0]))
        self.play(FadeIn(salida[1], shift=RIGHT * 0.15))
        self.play(FadeIn(salida[2], shift=RIGHT * 0.15))
        self.wait(2.0)

        clave = nota("ninguna de las dos depende de $p_0$ ni de $p_1$: son "
                     "condicionales a cada hipótesis", scale=0.48)
        clave.next_to(salida, DOWN, buff=0.45)
        self.play(FadeIn(clave))
        self.wait(2.2)

        # ------------------------------------------------ al dibujo
        self.play(FadeOut(VGroup(prob, salida, clave)))

        ax, lab = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 0.52], ancho=8.4,
                       alto=2.9, x_label="r")
        ax.shift(DOWN * 0.55)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        f0 = ax.plot(lambda r: g(r, A0), x_range=[R_MIN, R_MAX, 0.02],
                     color=AZUL, stroke_width=4)
        f1 = ax.plot(lambda r: g(r, A1), x_range=[R_MIN, R_MAX, 0.02],
                     color=VERDE, stroke_width=4)
        l0 = MathTex(r"f(r|H_0)", color=AZUL).scale(0.55)
        l0.next_to(ax.c2p(A0, g(A0, A0)), UL, buff=0.02)
        l1 = MathTex(r"f(r|H_1)", color=VERDE).scale(0.55)
        l1.next_to(ax.c2p(A1, g(A1, A1)), UR, buff=0.02)
        self.play(Create(f0), Create(f1), FadeIn(l0), FadeIn(l1))

        alfa = ValueTracker(0.30)
        gam = lambda: gamma_para_pfa(alfa.get_value())

        umbral = always_redraw(lambda: DashedLine(
            ax.c2p(gam(), 0), ax.c2p(gam(), 0.50), color=ROJO,
            stroke_width=3.5, dash_length=0.1))
        area_fa = always_redraw(lambda: ax.get_area(
            f0, x_range=(gam(), R_MAX), color=ROJO, opacity=0.65, stroke_width=0))
        area_pd = always_redraw(lambda: ax.get_area(
            f1, x_range=(gam(), R_MAX), color=VERDE, opacity=0.35, stroke_width=0))
        self.play(Create(umbral), FadeIn(area_fa), FadeIn(area_pd))

        marcador = always_redraw(lambda: VGroup(
            VGroup(MathTex(r"P_{FA}=", color=ROJO).scale(0.6),
                   DecimalNumber(pfa(gam()), num_decimal_places=3,
                                 color=ROJO).scale(0.6)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex(r"P_{D}=", color=VERDE).scale(0.6),
                   DecimalNumber(pd(gam()), num_decimal_places=3,
                                 color=VERDE).scale(0.6)).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        .to_corner(UR, buff=0.6).shift(DOWN * 0.55))
        self.play(FadeIn(marcador))
        self.wait(0.8)

        # ------------------------------------------------ apretar la cota
        msg = nota("bajás la cota de falsa alarma…", scale=0.48)
        msg.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(msg))
        self.play(alfa.animate.set_value(0.02), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.6)
        msg2 = nota("…y la detección se te cae con ella. No hay forma de evitarlo.",
                    scale=0.48)
        msg2.move_to(msg)
        self.play(FadeOut(msg), FadeIn(msg2))
        self.wait(2.0)

        msg3 = nota("aflojás la cota y recuperás detección, a costa de más "
                    "falsas alarmas", scale=0.48)
        msg3.move_to(msg)
        self.play(FadeOut(msg2), FadeIn(msg3))
        self.play(alfa.animate.set_value(0.45), run_time=2.6,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(1.8)
        self.play(FadeOut(msg3))

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, f0, f1, l0, l1, umbral, area_fa,
                                 area_pd, marcador)))
        cierre = VGroup(
            Text("Sigue siendo un test de razón de verosimilitud.",
                 color=TXT).scale(0.6),
            MathTex(r"\Lambda(r)\;\underset{H_0}{\overset{H_1}{\gtrless}}\;\eta",
                    color=AMBAR).scale(0.85),
            Text("Lo único que cambia es cómo se elige η:", color=INK).scale(0.52),
            Text("el más chico que respete la cota de falsa alarma.",
                 color=AMBAR).scale(0.55),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(Write(cierre[1]))
        self.wait(0.4)
        self.play(FadeIn(cierre[2]), FadeIn(cierre[3]))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
