"""Escena 7 - La curva ROC.

Barriendo el umbral, el par (PFA, PD) recorre una curva. Esa curva es el
retrato completo del detector, y no depende de donde uno decida operar.

    manim -pql s07_roc.py CurvaROC
"""
from manim import *
import numpy as np
from comun import *

SIGMA = 1.0
R_MIN, R_MAX = -3.6, 6.6


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def Q(x):
    from math import erfc, sqrt
    return 0.5 * erfc(x / sqrt(2))


class CurvaROC(Scene):
    def construct(self):
        configurar()

        tit = titulo("La curva ROC: el retrato del detector")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        d = 2.6                                   # separacion entre medias
        gam = ValueTracker(R_MAX)

        # ------------------------------------------------ panel densidades
        ax_d, lab_d = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 0.52], ancho=5.0,
                           alto=2.4, x_label="r")
        ax_d.shift(LEFT * 3.5 + DOWN * 0.55)
        lab_d.next_to(ax_d.x_axis.get_end(), DR, buff=0.08)

        f0 = ax_d.plot(lambda r: g(r, 0), x_range=[R_MIN, R_MAX, 0.02],
                       color=AZUL, stroke_width=3.5)
        f1 = ax_d.plot(lambda r: g(r, d), x_range=[R_MIN, R_MAX, 0.02],
                       color=VERDE, stroke_width=3.5)
        self.play(Create(ax_d), FadeIn(lab_d), Create(f0), Create(f1))

        umbral = always_redraw(lambda: DashedLine(
            ax_d.c2p(gam.get_value(), 0), ax_d.c2p(gam.get_value(), 0.50),
            color=ROJO, stroke_width=3, dash_length=0.09))
        a_fa = always_redraw(lambda: ax_d.get_area(
            f0, x_range=(min(gam.get_value(), R_MAX - 1e-3), R_MAX),
            color=ROJO, opacity=0.65, stroke_width=0))
        a_pd = always_redraw(lambda: ax_d.get_area(
            f1, x_range=(min(gam.get_value(), R_MAX - 1e-3), R_MAX),
            color=VERDE, opacity=0.32, stroke_width=0))
        self.play(Create(umbral), FadeIn(a_fa), FadeIn(a_pd))

        # ------------------------------------------------ panel ROC
        ax_r = Axes(x_range=[0, 1, 0.5], y_range=[0, 1, 0.5],
                    x_length=3.9, y_length=3.4,
                    axis_config={"color": INK, "stroke_width": 2,
                                 "include_ticks": True, "include_tip": False,
                                 "font_size": 22})
        ax_r.add_coordinates([0, 0.5, 1], [0, 0.5, 1])
        ax_r.shift(RIGHT * 3.6 + DOWN * 0.5)
        lx = MathTex("P_{FA}", color=ROJO).scale(0.55).next_to(ax_r, DOWN, buff=0.22)
        ly = MathTex("P_{D}", color=VERDE).scale(0.55).next_to(ax_r, LEFT, buff=0.18)
        diag = DashedLine(ax_r.c2p(0, 0), ax_r.c2p(1, 1), color=INK,
                          stroke_width=1.8, dash_length=0.08)
        d_lbl = nota("azar", scale=0.38).next_to(ax_r.c2p(0.62, 0.55), DR, buff=0.02)

        self.play(Create(ax_r), FadeIn(lx), FadeIn(ly))
        self.play(Create(diag), FadeIn(d_lbl))
        self.wait(0.5)

        # el punto que recorre la ROC
        punto = always_redraw(lambda: Dot(
            ax_r.c2p(Q(gam.get_value() / SIGMA), Q((gam.get_value() - d) / SIGMA)),
            color=AMBAR, radius=0.075))
        self.play(FadeIn(punto, scale=1.6))

        expl = nota("cada umbral es un punto de la curva", scale=0.46)
        expl.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(expl))
        self.wait(1.2)

        # ------------------------------------------------ trazar la ROC
        traza = TracedPath(punto.get_center, stroke_color=AMBAR,
                           stroke_width=4)
        self.add(traza)
        self.play(gam.animate.set_value(R_MIN), run_time=5.5,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.6)
        self.play(FadeOut(expl))

        extremos = VGroup(
            nota("$\\eta\\to\\infty$: nunca declaro $H_1$   →   (0,0)", scale=0.44),
            nota("$\\eta\\to 0$: siempre declaro $H_1$   →   (1,1)", scale=0.44),
        ).arrange(DOWN, buff=0.14)
        extremos.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(extremos))
        self.wait(2.2)
        self.play(FadeOut(extremos))

        # ------------------------------------------------ comparar detectores
        self.play(FadeOut(VGroup(ax_d, lab_d, f0, f1, umbral, a_fa, a_pd,
                                 punto, traza)))
        self.play(VGroup(ax_r, lx, ly, diag, d_lbl).animate
                  .scale(1.28).move_to(ORIGIN).shift(DOWN * 0.35))

        comp = Text("Comparar detectores", color=TXT).scale(0.58)
        comp.next_to(tit, DOWN, buff=0.35)
        self.play(FadeIn(comp))

        curvas = VGroup()
        etiquetas = VGroup()
        for sep, col, txt in [(0.9, ROJO, "SNR bajo"),
                              (2.0, AMBAR, "SNR medio"),
                              (3.4, VERDE, "SNR alto")]:
            gs = np.linspace(-6, 8, 400)
            pts = [ax_r.c2p(Q(x), Q(x - sep)) for x in gs]
            c = VMobject(color=col, stroke_width=4).set_points_as_corners(pts)
            curvas.add(c)
            e = Text(txt, color=col).scale(0.44)
            etiquetas.add(e)

        for c, e, pos in zip(curvas, etiquetas,
                             [(0.62, 0.30), (0.52, 0.62), (0.30, 0.88)]):
            e.move_to(ax_r.c2p(*pos))
            self.play(Create(c, run_time=1.1), FadeIn(e))
        self.wait(1.2)

        flecha_mejor = Arrow(ax_r.c2p(0.55, 0.45), ax_r.c2p(0.12, 0.93),
                             color=TXT, stroke_width=3, buff=0.1,
                             max_tip_length_to_length_ratio=0.13)
        mejor = Text("mejor", color=TXT).scale(0.46)
        mejor.next_to(flecha_mejor.get_end(), RIGHT, buff=0.15)
        self.play(GrowArrow(flecha_mejor), FadeIn(mejor))
        self.wait(2.0)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax_r, lx, ly, diag, d_lbl, curvas, etiquetas,
                                 flecha_mejor, mejor, comp)))
        cierre = VGroup(
            Text("La ROC no depende del umbral que elijas.", color=TXT).scale(0.6),
            Text("Es la calidad del detector; el umbral solo dice "
                 "dónde te parás sobre ella.", color=AMBAR).scale(0.55),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1], shift=UP * 0.15))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
