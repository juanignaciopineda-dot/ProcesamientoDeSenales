"""Escena 3 - Falsa alarma, miss y deteccion.

Los cuatro resultados posibles, los dos que son error, y como se combinan
en la probabilidad de error total Pe = p0*PFA + p1*PM.

    manim -pql s03_errores.py Errores
"""
from manim import *
import numpy as np
from comun import *

A0, A1 = 0.0, 2.6
SIGMA = 0.85
R_MIN, R_MAX = -3.4, 6.0
P0 = 0.5


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    from math import erfc, sqrt
    return 0.5 * erfc(x / sqrt(2))


def pfa(gam):
    return Q((gam - A0) / SIGMA)


def pm(gam):
    return 1 - Q((gam - A1) / SIGMA)


class Errores(Scene):
    def construct(self):
        configurar()

        tit = titulo("Falsa alarma, miss y detección")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ los cuatro casos
        filas = [
            ("$H_0$ verdadera", "decido $H_0$", "acierto", VERDE),
            ("$H_0$ verdadera", "decido $H_1$", "FALSA ALARMA", ROJO),
            ("$H_1$ verdadera", "decido $H_0$", "MISS", ROJO),
            ("$H_1$ verdadera", "decido $H_1$", "DETECCIÓN", VERDE),
        ]
        tabla = VGroup()
        for a, b, c, col in filas:
            tabla.add(VGroup(
                Text(a, color=INK).scale(0.46),
                MathTex(r"\rightarrow", color=INK).scale(0.5),
                Text(b, color=INK).scale(0.46),
                MathTex(r"\Rightarrow", color=INK).scale(0.5),
                Text(c, color=col, weight=BOLD).scale(0.48),
            ).arrange(RIGHT, buff=0.22))
        tabla.arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        tabla.next_to(tit, DOWN, buff=0.5)

        for f in tabla:
            self.play(FadeIn(f, shift=RIGHT * 0.15), run_time=0.45)
        self.wait(1.4)

        defs = VGroup(
            MathTex(r"P_{FA}=P(\text{`}H_1\text{'}\,|\,H_0)", color=ROJO).scale(0.6),
            MathTex(r"P_{M}=P(\text{`}H_0\text{'}\,|\,H_1)", color=AMBAR).scale(0.6),
            MathTex(r"P_{D}=P(\text{`}H_1\text{'}\,|\,H_1)=1-P_M",
                    color=VERDE).scale(0.6),
        ).arrange(DOWN, buff=0.2)
        defs.next_to(tabla, DOWN, buff=0.5)
        self.play(FadeIn(defs, shift=UP * 0.15))
        self.wait(2.0)

        # ------------------------------------------------ al dibujo
        self.play(FadeOut(tabla), defs.animate.scale(0.78).to_corner(UR, buff=0.45))

        ax, lab = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 0.52], ancho=8.2,
                       alto=2.8, x_label="r")
        ax.shift(DOWN * 0.6).shift(LEFT * 0.5)
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

        gam = ValueTracker((A0 + A1) / 2)
        umbral = always_redraw(lambda: DashedLine(
            ax.c2p(gam.get_value(), 0), ax.c2p(gam.get_value(), 0.50),
            color=ROJO, stroke_width=3.5, dash_length=0.1))
        u_lbl = always_redraw(lambda: MathTex(r"\gamma", color=ROJO).scale(0.62)
                              .next_to(ax.c2p(gam.get_value(), 0), DOWN, buff=0.18))
        self.play(Create(umbral), FadeIn(u_lbl))
        self.wait(0.5)

        # ------------------------------------------------ las dos areas
        area_fa = always_redraw(lambda: ax.get_area(
            f0, x_range=(gam.get_value(), R_MAX), color=ROJO, opacity=0.6,
            stroke_width=0))
        area_m = always_redraw(lambda: ax.get_area(
            f1, x_range=(R_MIN, gam.get_value()), color=AMBAR, opacity=0.6,
            stroke_width=0))

        self.play(FadeIn(area_fa))
        et_fa = nota("$P_{FA}$: la cola de $H_0$ que cae del lado de $H_1$",
                     scale=0.46)
        et_fa.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(et_fa))
        self.wait(1.5)

        self.play(FadeIn(area_m))
        et_m = nota("$P_{M}$: la cola de $H_1$ que cae del lado de $H_0$",
                    scale=0.46)
        et_m.move_to(et_fa)
        self.play(FadeOut(et_fa), FadeIn(et_m))
        self.wait(1.5)
        self.play(FadeOut(et_m))

        # ------------------------------------------------ numeros en vivo
        marcador = always_redraw(lambda: VGroup(
            VGroup(MathTex("P_{FA}=", color=ROJO).scale(0.55),
                   DecimalNumber(pfa(gam.get_value()), num_decimal_places=3,
                                 color=ROJO).scale(0.55)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex("P_{M}=", color=AMBAR).scale(0.55),
                   DecimalNumber(pm(gam.get_value()), num_decimal_places=3,
                                 color=AMBAR).scale(0.55)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex("P_{e}=", color=TXT).scale(0.55),
                   DecimalNumber(P0 * pfa(gam.get_value())
                                 + (1 - P0) * pm(gam.get_value()),
                                 num_decimal_places=3, color=TXT).scale(0.55)
                   ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        .to_edge(LEFT, buff=0.55).shift(DOWN * 1.9))
        self.play(FadeIn(marcador))
        self.wait(0.8)

        formula = MathTex(r"P_e = p_0 P_{FA} + p_1 P_M", color=TXT).scale(0.72)
        formula.to_edge(DOWN, buff=0.45)
        self.play(Write(formula))
        self.wait(1.2)

        # ------------------------------------------------ el compromiso
        comp = nota("bajar una cola sube la otra: es un compromiso, no una "
                    "cuestión de afinar mejor", scale=0.46)
        comp.next_to(formula, UP, buff=0.22)
        self.play(FadeIn(comp))
        self.play(gam.animate.set_value(A1 + 1.1), run_time=2.4,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.8)
        self.play(gam.animate.set_value(A0 - 1.0), run_time=2.8,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.8)
        self.play(gam.animate.set_value((A0 + A1) / 2), run_time=1.8)
        self.wait(0.5)
        opt = nota("con $p_0=p_1$, el mínimo de $P_e$ está justo en el cruce",
                   scale=0.46)
        opt.move_to(comp)
        self.play(FadeOut(comp), FadeIn(opt))
        self.wait(2.0)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, f0, f1, l0, l1, umbral, u_lbl,
                                 area_fa, area_m, marcador, formula, opt, defs)))
        cierre = VGroup(
            Text("Los dos errores no son simétricos.", color=TXT).scale(0.64),
            Text("Qué te importa más define dónde ponés el umbral.",
                 color=AMBAR).scale(0.64),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1], shift=UP * 0.15))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
