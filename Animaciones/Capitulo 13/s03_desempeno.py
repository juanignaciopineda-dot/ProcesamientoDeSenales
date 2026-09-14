"""Escena 3 - Caracterizar el desempeno: dos gaussianas separadas por E.

Bajo H0, g es gaussiana de media 0. Bajo H1, la misma gaussiana corrida
en E. El desempeno (P_FA, P_M, P_e) depende solo de E/sigma^2: la forma
de s[n] no importa, solo su energia.

    manim -pql s03_desempeno.py Desempeno
"""
from manim import *
import numpy as np
from comun import *

SIGMA = 1.0
R_MIN, R_MAX = -3.0, 7.0


def sigma_g(E):
    return SIGMA * np.sqrt(E)


class Desempeno(Scene):
    def construct(self):
        configurar()

        tit = titulo("El desempeño: dos gaussianas separadas por E")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        intro = VGroup(
            MathTex(r"H_0:\ G\sim\mathcal N(0,\ \sigma^2 E)", color=AZUL).scale(0.62),
            MathTex(r"H_1:\ G\sim\mathcal N(E,\ \sigma^2 E)", color=VERDE).scale(0.62),
        ).arrange(RIGHT, buff=0.9)
        intro.next_to(tit, DOWN, buff=0.4).set_x(0)
        n_intro = nota("mismo desvío $\\sigma\\sqrt E$ en las dos: "
                       "solo se corre la media", scale=0.46)
        n_intro.next_to(intro, DOWN, buff=0.25)
        self.play(FadeIn(intro), FadeIn(n_intro))
        self.wait(1.8)
        self.play(FadeOut(VGroup(intro, n_intro)))

        # ------------------------------------------------ el grafico
        E_val = ValueTracker(3.0)

        ax, lab = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 0.55], ancho=8.4,
                       alto=2.8, x_label="g")
        ax.shift(DOWN * 0.55 + LEFT * 0.35)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        f0 = always_redraw(lambda: ax.plot(
            lambda g: gauss(g, 0, sigma_g(E_val.get_value())),
            x_range=[R_MIN, R_MAX, 0.02], color=AZUL, stroke_width=4))
        f1 = always_redraw(lambda: ax.plot(
            lambda g: gauss(g, E_val.get_value(), sigma_g(E_val.get_value())),
            x_range=[R_MIN, R_MAX, 0.02], color=VERDE, stroke_width=4))
        l0 = MathTex(r"f(g|H_0)", color=AZUL).scale(0.55)
        l0.next_to(ax.c2p(0, gauss(0, 0, sigma_g(3.0))), UL, buff=0.05)
        l1 = always_redraw(lambda: MathTex(r"f(g|H_1)", color=VERDE).scale(0.55)
                           .next_to(ax.c2p(E_val.get_value(),
                                           gauss(0, 0, sigma_g(E_val.get_value()))),
                                    UR, buff=0.05))
        self.play(Create(f0), Create(f1), FadeIn(l0), FadeIn(l1))

        gamma = always_redraw(lambda: DashedLine(
            ax.c2p(E_val.get_value() / 2, 0), ax.c2p(E_val.get_value() / 2, 0.5),
            color=ROJO, stroke_width=3.2))
        g_lbl = always_redraw(lambda: MathTex(r"\gamma=E/2", color=ROJO).scale(0.5)
                              .next_to(ax.c2p(E_val.get_value() / 2, 0),
                                       DOWN, buff=0.18))
        self.play(Create(gamma), FadeIn(g_lbl))

        area_fa = always_redraw(lambda: ax.get_area(
            f0, x_range=(E_val.get_value() / 2, R_MAX), color=ROJO,
            opacity=0.55, stroke_width=0))
        area_m = always_redraw(lambda: ax.get_area(
            f1, x_range=(R_MIN, E_val.get_value() / 2), color=AMBAR,
            opacity=0.55, stroke_width=0))
        self.play(FadeIn(area_fa), FadeIn(area_m))
        self.wait(0.5)

        marcador = always_redraw(lambda: VGroup(
            VGroup(MathTex(r"E/\sigma^2=", color=TXT).scale(0.55),
                   DecimalNumber(E_val.get_value(), num_decimal_places=2,
                                 color=TXT).scale(0.55)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex(r"P_e=", color=AMBAR).scale(0.55),
                   DecimalNumber(Q(np.sqrt(E_val.get_value()) / 2),
                                 num_decimal_places=3, color=AMBAR).scale(0.55)
                   ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        .to_corner(UR, buff=0.55).shift(DOWN * 1.1))
        self.play(FadeIn(marcador))
        self.wait(0.8)

        formula = MathTex(r"P_e=Q\!\left(\frac{\sqrt E}{2\sigma}\right)",
                          color=TXT).scale(0.68)
        formula.to_edge(DOWN, buff=0.42)
        self.play(Write(formula))
        self.wait(1.0)

        m1 = nota("poca energía: las campanas se superponen mucho", scale=0.46)
        m1.next_to(formula, UP, buff=0.22)
        self.play(E_val.animate.set_value(0.8), run_time=2.0)
        self.play(FadeIn(m1))
        self.wait(1.4)
        self.play(FadeOut(m1))

        m2 = nota("mucha energía: casi no se superponen, $P_e\\to 0$",
                  scale=0.46)
        m2.move_to(m1)
        self.play(E_val.animate.set_value(9.0), run_time=2.6,
                  rate_func=rate_functions.ease_in_out_sine)
        self.play(FadeIn(m2))
        self.wait(1.6)
        self.play(FadeOut(m2))
        self.play(E_val.animate.set_value(3.0), run_time=1.6)

        n_res = nota("decae MÁS RÁPIDO que exponencialmente con el SNR:\n"
                     "duplicar la energía mejora muchísimo", scale=0.46)
        n_res.next_to(formula, UP, buff=0.22)
        self.play(FadeIn(n_res))
        self.wait(2.0)
        self.play(FadeOut(VGroup(ax, lab, f0, f1, l0, l1, gamma, g_lbl,
                                 area_fa, area_m, marcador, formula, n_res)))

        # ------------------------------------------------ la forma no importa
        forma_tit = Text("La forma de s[n] no importa, solo su energía",
                         color=TXT).scale(0.58)
        forma_tit.next_to(tit, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(forma_tit))

        n = np.arange(10)
        s_a = np.where((n >= 2) & (n <= 6), 1.5, 0.0)
        s_b = 1.2 * np.sin(2 * np.pi * (n - 1) / 9) * ((n >= 1) & (n <= 8))
        Ea, Eb = np.sum(s_a ** 2), np.sum(s_b ** 2)
        escala = np.sqrt(Ea / max(Eb, 1e-9))
        s_b = s_b * escala  # igualar energias

        ax_a, _ = ejes([0, 9, 10], [-2, 2, 4], ancho=4.6, alto=1.8, tip=False)
        ax_b, _ = ejes([0, 9, 10], [-2, 2, 4], ancho=4.6, alto=1.8, tip=False)
        cols = VGroup(ax_a, ax_b).arrange(RIGHT, buff=0.9)
        cols.next_to(forma_tit, DOWN, buff=0.5)
        st_a = stem(ax_a, n, s_a, color=AMBAR, ancho=2.6, radio=0.035)
        st_b = stem(ax_b, n, s_b, color=MAGENTA, ancho=2.6, radio=0.035)
        la = MathTex(r"s_a[n]", color=AMBAR).scale(0.5).next_to(ax_a, UP, buff=0.1)
        lb = MathTex(r"s_b[n]", color=MAGENTA).scale(0.5).next_to(ax_b, UP, buff=0.1)
        self.play(Create(ax_a), FadeIn(la), Create(st_a))
        self.play(Create(ax_b), FadeIn(lb), Create(st_b))

        misma_E = MathTex(r"\sum_n s_a^2[n]=\sum_n s_b^2[n]=E", color=TXT).scale(0.55)
        misma_E.next_to(cols, DOWN, buff=0.35)
        self.play(Write(misma_E))
        self.wait(1.0)

        conclu = nota("distintas formas, misma energía → EXACTAMENTE la "
                      "misma $P_{FA}$, $P_M$, $P_e$", scale=0.46)
        conclu.next_to(misma_E, DOWN, buff=0.3)
        self.play(FadeIn(conclu))
        self.wait(2.2)
        self.play(FadeOut(VGroup(forma_tit, cols, la, lb, st_a, st_b, misma_E,
                                 conclu)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("Todo depende de un solo número:", color=INK).scale(0.56),
            Text("la relación señal-ruido E/σ².", color=AZUL).scale(0.62),
            nota("la forma de la señal es irrelevante para el desempeño",
                 scale=0.48),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.4)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
