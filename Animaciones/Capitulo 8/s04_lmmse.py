"""Escena 4 - LMMSE: obligar al estimador a ser una recta.

E[Y|X] suele ser imposible de calcular porque no se conoce la densidad
condicional. El compromiso: restringir el estimador a la forma aX+b y
elegir a y b que minimicen el error cuadratico medio.

    manim -pql s04_lmmse.py LMMSE
"""
from manim import *
import numpy as np
from comun import *

RHO = 0.72
SX = SY = 1.0
N = 220
XS, YS = muestras_gauss(N, RHO, sd=(SX, SY), semilla=17)

A_OPT = RHO * SY / SX          # pendiente optima
B_OPT = 0.0                    # ambas medias son cero


def mse(a, b):
    return float(np.mean((YS - (a * XS + b)) ** 2))


MSE_MAX = mse(-1.6, 1.7)


class LMMSE(Scene):
    def construct(self):
        configurar()

        tit = titulo("Cuando no se puede calcular E[Y|X]: pedirle una recta")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        motivo = VGroup(
            nota("la densidad condicional casi nunca se conoce…", scale=0.5),
            MathTex(r"\hat{y}_\ell(X) \;=\; aX+b", color=AMBAR).scale(0.85),
            nota("…así que se restringe la forma y se optimiza $a$ y $b$",
                 scale=0.5),
        ).arrange(DOWN, buff=0.24)
        motivo.next_to(tit, DOWN, buff=0.4)
        self.play(FadeIn(motivo[0]))
        self.play(Write(motivo[1]))
        self.play(FadeIn(motivo[2]))
        self.wait(1.6)
        self.play(FadeOut(motivo))

        # ------------------------------------------------ la nube
        ax, lab = ejes([-3.2, 3.2, 3.2], [-3.2, 3.2, 3.2], ancho=5.6, alto=4.2,
                       x_label="x", y_label="y")
        ax.shift(LEFT * 2.6 + DOWN * 0.45)
        lab[0].next_to(ax.x_axis.get_end(), DR, buff=0.1)
        lab[1].next_to(ax.y_axis.get_end(), UR, buff=0.08)

        puntos = nube(ax, XS, YS, color=AZUL, radio=0.032, opacidad=0.55)
        self.play(Create(ax), FadeIn(lab))
        self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in puntos],
                              lag_ratio=0.003, run_time=1.5))
        self.wait(0.4)

        # ------------------------------------------------ la recta movil
        av, bv = ValueTracker(-1.1), ValueTracker(1.5)

        recta = always_redraw(lambda: ax.plot(
            lambda x: av.get_value() * x + bv.get_value(),
            x_range=[-3.2, 3.2], color=AMBAR, stroke_width=4.5))

        # residuos: solo unos pocos, para no tapar la nube
        idx = np.arange(0, N, 9)
        residuos = always_redraw(lambda: VGroup(*[
            Line(ax.c2p(XS[i], YS[i]),
                 ax.c2p(XS[i], av.get_value() * XS[i] + bv.get_value()),
                 color=ROJO, stroke_width=2, stroke_opacity=0.75)
            for i in idx]))

        self.play(Create(recta))
        self.play(FadeIn(residuos))
        self.wait(0.5)

        res_lbl = nota("cada segmento rojo es un error", scale=0.44)
        res_lbl.next_to(ax, DOWN, buff=0.25)
        self.play(FadeIn(res_lbl))
        self.wait(1.2)
        self.play(FadeOut(res_lbl))

        # ------------------------------------------------ el medidor
        marco = medidor(alto_max=3.0)
        marco.to_edge(RIGHT, buff=1.5).shift(DOWN * 0.35)
        relleno = always_redraw(lambda: relleno_medidor(
            marco, mse(av.get_value(), bv.get_value()) / MSE_MAX, color=ROJO))
        med_lbl = MathTex(r"E\big[(Y-\hat{y}_\ell)^2\big]", color=ROJO).scale(0.5)
        med_lbl.next_to(marco, UP, buff=0.22)
        valor = always_redraw(lambda: DecimalNumber(
            mse(av.get_value(), bv.get_value()), num_decimal_places=3,
            color=ROJO).scale(0.55).next_to(marco, DOWN, buff=0.2))

        params = always_redraw(lambda: VGroup(
            VGroup(MathTex("a =", color=INK).scale(0.55),
                   DecimalNumber(av.get_value(), num_decimal_places=2,
                                 color=AMBAR).scale(0.58)).arrange(RIGHT, buff=0.12),
            VGroup(MathTex("b =", color=INK).scale(0.55),
                   DecimalNumber(bv.get_value(), num_decimal_places=2,
                                 color=AMBAR).scale(0.58)).arrange(RIGHT, buff=0.12),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            .next_to(marco, LEFT, buff=0.75))

        self.play(FadeIn(marco), FadeIn(relleno), FadeIn(med_lbl), FadeIn(valor),
                  FadeIn(params))
        self.wait(0.8)

        # ------------------------------------------------ la busqueda
        self.play(bv.animate.set_value(-1.4), run_time=1.8,
                  rate_func=rate_functions.ease_in_out_sine)
        self.play(av.animate.set_value(1.9), run_time=2.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.3)
        self.play(av.animate.set_value(A_OPT), bv.animate.set_value(B_OPT),
                  run_time=2.4, rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)

        destello = Flash(ax.c2p(0, 0), color=VERDE, line_length=0.35,
                         num_lines=18, flash_radius=0.5)
        self.play(destello)
        self.wait(0.4)

        # ------------------------------------------------ la solucion
        sol = MathTex(r"\hat{Y}_\ell \;=\; \mu_Y \;+\; \rho_{Y\!,X}\,"
                      r"\frac{\sigma_Y}{\sigma_X}\,(X-\mu_X)",
                      color=VERDE).scale(0.68)
        sol.to_edge(DOWN, buff=0.78)
        self.play(Write(sol))
        self.wait(1.6)

        err = MathTex(r"\text{LMMSE} \;=\; \sigma_Y^2\,(1-\rho^2_{Y\!,X})",
                      color=AMBAR).scale(0.68)
        err.next_to(sol, DOWN, buff=0.26)
        self.play(Write(err))
        self.wait(2.2)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, puntos, recta, residuos, marco,
                                 relleno, med_lbl, valor, params, sol, err)))
        cierre = VGroup(
            Text("Todo el estimador queda determinado por", color=INK).scale(0.55),
            MathTex(r"\mu_X,\ \mu_Y,\ \sigma_X,\ \sigma_Y,\ \rho_{Y\!,X}",
                    color=VERDE).scale(0.85),
            nota("los momentos de primer y segundo orden, nada más.\n"
                 "No hace falta conocer la densidad conjunta.", scale=0.5),
        ).arrange(DOWN, buff=0.32)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(Write(cierre[1]))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
