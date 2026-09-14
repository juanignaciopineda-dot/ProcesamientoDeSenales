"""Escena 1 - Estimar sin observaciones: el MMSE es la media.

Si lo unico que se sabe de Y es su densidad, la estimacion que minimiza
E[(Y - y)^2] es la media, y el error que queda es la varianza.

    manim -pql s01_mmse.py MMSE
"""
from manim import *
import numpy as np
from comun import *

MU, SD = 1.4, 1.15
X_MIN, X_MAX = -3.2, 6.2


def f_Y(y):
    return gauss(y, MU, SD)


def mse(yhat):
    """E[(Y - yhat)^2] = sigma^2 + (mu - yhat)^2."""
    return SD ** 2 + (MU - yhat) ** 2


MSE_MAX = mse(X_MIN)


class MMSE(Scene):
    def construct(self):
        configurar()

        tit = titulo("Estimar una variable aleatoria, sin medir nada")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ojo con el espacio final: sin el, \quad se pega a la E de la
        # linea siguiente al concatenar los literales y LaTeX ve \quadE
        preg = MathTex(r"\text{elegir}\ \hat{y}\ \text{que minimice}\quad "
                       r"E\big[(Y-\hat{y})^2\big]", color=TXT).scale(0.72)
        preg.next_to(tit, DOWN, buff=0.38)
        self.play(Write(preg))
        self.wait(1.2)
        self.play(preg.animate.scale(0.78).to_edge(UP, buff=1.15))

        # ------------------------------------------------ la densidad
        ax, lab = ejes([X_MIN, X_MAX, X_MAX - X_MIN], [0, 0.42], ancho=8.0,
                       alto=2.7, x_label="y")
        ax.shift(DOWN * 0.55).shift(LEFT * 0.55)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)

        dens = curva(ax, f_Y, [X_MIN, X_MAX], color=AZUL, ancho=4)
        dens_area = ax.get_area(dens, x_range=(X_MIN, X_MAX), color=AZUL,
                                opacity=0.14, stroke_width=0)
        dens_lbl = MathTex(r"f_Y(y)", color=AZUL).scale(0.68)
        dens_lbl.next_to(ax.c2p(MU - 2.4, f_Y(MU - 1.5)), UL, buff=0.05)

        self.play(Create(ax), FadeIn(lab))
        self.play(Create(dens, run_time=1.3), FadeIn(dens_area), FadeIn(dens_lbl))
        self.wait(0.5)

        # ------------------------------------------------ el candidato movil
        yh = ValueTracker(X_MIN + 0.9)

        linea = always_redraw(lambda: DashedLine(
            ax.c2p(yh.get_value(), 0), ax.c2p(yh.get_value(), 0.40),
            color=AMBAR, stroke_width=3, dash_length=0.1))
        marca = always_redraw(lambda: MathTex(r"\hat{y}", color=AMBAR)
                              .scale(0.65)
                              .next_to(ax.c2p(yh.get_value(), 0), DOWN, buff=0.16))
        self.play(Create(linea), FadeIn(marca))

        # ------------------------------------------------ el medidor de error
        marco = medidor(alto_max=2.7)
        marco.to_edge(RIGHT, buff=0.9).shift(DOWN * 0.55)
        relleno = always_redraw(lambda: relleno_medidor(
            marco, mse(yh.get_value()) / MSE_MAX, color=ROJO))
        med_lbl = MathTex(r"E\big[(Y-\hat{y})^2\big]", color=ROJO).scale(0.5)
        med_lbl.next_to(marco, UP, buff=0.22)
        valor = always_redraw(lambda: DecimalNumber(
            mse(yh.get_value()), num_decimal_places=2, color=ROJO)
            .scale(0.55).next_to(marco, DOWN, buff=0.2))

        self.play(FadeIn(marco), FadeIn(relleno), FadeIn(med_lbl), FadeIn(valor))
        self.wait(0.8)

        # ------------------------------------------------ barrido
        self.play(yh.animate.set_value(X_MAX - 0.9), run_time=3.4,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.3)
        self.play(yh.animate.set_value(MU), run_time=2.6,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.6)

        # ------------------------------------------------ el minimo
        destello = Flash(ax.c2p(MU, 0), color=VERDE, line_length=0.3,
                         num_lines=16, flash_radius=0.4)
        mu_lbl = MathTex(r"\mu_Y", color=VERDE).scale(0.7)
        mu_lbl.next_to(ax.c2p(MU, 0), DOWN, buff=0.16)
        self.play(destello, FadeOut(marca), FadeIn(mu_lbl))
        self.wait(0.5)

        res = MathTex(r"\hat{y}_{\text{MMSE}} \;=\; E[Y] \;=\; \mu_Y",
                      color=VERDE).scale(0.78)
        res.to_edge(DOWN, buff=0.85)
        self.play(Write(res))
        self.wait(1.2)

        res2 = MathTex(r"\text{MMSE} \;=\; \sigma_Y^2", color=AMBAR).scale(0.78)
        res2.next_to(res, DOWN, buff=0.28)
        self.play(Write(res2))
        self.wait(0.6)
        obs = nota("el mejor que podés hacer sin medir nada: apuntar a la media, "
                   "y comerte la varianza entera", scale=0.44)
        obs.next_to(res2, DOWN, buff=0.22)
        self.play(FadeIn(obs))
        self.wait(2.2)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, dens, dens_area, dens_lbl, linea,
                                 mu_lbl, marco, relleno, med_lbl, valor,
                                 res, res2, obs, preg)))
        cierre = VGroup(
            Text("¿Y si además puedo medir algo?", color=TXT).scale(0.72),
            nota("ahí entra la densidad condicional, y el error baja", scale=0.5),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1]))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
