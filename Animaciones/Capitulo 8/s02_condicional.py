"""Escena 2 - Estimar con una observacion: la media condicional.

Al medir X = x, la densidad que importa deja de ser f_Y(y) y pasa a ser
f_{Y|X}(y|x). El estimador MMSE es su media, y el error que queda es la
varianza condicional, que es menor.

    manim -pql s02_condicional.py Condicional
"""
from manim import *
import numpy as np
from comun import *

RHO = 0.78
N = 260
X0, Y0 = 0.0, 0.0
SX, SY = 1.0, 1.0


def media_cond(x):
    return Y0 + RHO * (SY / SX) * (x - X0)


SD_COND = SY * np.sqrt(1 - RHO ** 2)


class Condicional(Scene):
    def construct(self):
        configurar()

        tit = titulo("Medir X cambia lo que sé de Y")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ la nube conjunta
        ax, lab = ejes([-3.2, 3.2, 3.2], [-3.2, 3.2, 3.2], ancho=5.6, alto=4.4,
                       x_label="x", y_label="y")
        ax.shift(LEFT * 3.0 + DOWN * 0.45)
        lab[0].next_to(ax.x_axis.get_end(), DR, buff=0.1)
        lab[1].next_to(ax.y_axis.get_end(), UR, buff=0.08)

        xs, ys = muestras_gauss(N, RHO, semilla=4)
        puntos = nube(ax, xs, ys, color=AZUL, radio=0.032, opacidad=0.6)
        # subtitulo() usa Text, que no interpreta LaTeX: la formula va aparte.
        # posicion fija arriba a la izquierda, lejos de la punta del eje y
        conj = VGroup(
            Text("muestras de", color=AZUL).scale(0.44),
            MathTex(r"f_{X,Y}(x,y)", color=AZUL).scale(0.52),
        ).arrange(RIGHT, buff=0.16)
        conj.to_corner(UL, buff=0.5).shift(DOWN * 1.15 + RIGHT * 0.2)

        self.play(Create(ax), FadeIn(lab), FadeIn(conj))
        self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in puntos],
                              lag_ratio=0.004, run_time=1.8))
        self.wait(0.6)

        # ------------------------------------------------ el corte en X = x
        xv = ValueTracker(-1.7)

        corte = always_redraw(lambda: Line(
            ax.c2p(xv.get_value(), -3.2), ax.c2p(xv.get_value(), 3.2),
            color=AMBAR, stroke_width=3.5))
        x_lbl = always_redraw(lambda: MathTex("X=x", color=AMBAR).scale(0.55)
                              .next_to(ax.c2p(xv.get_value(), -3.2), DOWN,
                                       buff=0.16))
        self.play(Create(corte), FadeIn(x_lbl))
        self.wait(0.5)

        obs = nota("solo importan las muestras que caen sobre esa línea",
                   scale=0.44)
        obs.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(obs))
        self.wait(1.4)
        self.play(FadeOut(obs))

        # ------------------------------------------------ la densidad condicional
        ax2, lab2 = ejes([-3.2, 3.2, 3.2], [0, 1.15], ancho=4.6, alto=2.6,
                         x_label="y")
        ax2.shift(RIGHT * 3.4 + DOWN * 0.75)
        lab2.next_to(ax2.x_axis.get_end(), DR, buff=0.1)
        cond_tit = MathTex(r"f_{Y|X}(y\,|\,x)", color=AMBAR).scale(0.62)
        cond_tit.next_to(ax2, UP, buff=0.28)

        cond = always_redraw(lambda: ax2.plot(
            lambda y: gauss(y, media_cond(xv.get_value()), SD_COND),
            x_range=[-3.2, 3.2, 0.02], color=AMBAR, stroke_width=4,
            use_smoothing=False))
        cond_area = always_redraw(lambda: ax2.get_area(
            ax2.plot(lambda y: gauss(y, media_cond(xv.get_value()), SD_COND),
                     x_range=[-3.2, 3.2, 0.02], use_smoothing=False),
            x_range=(-3.2, 3.2), color=AMBAR, opacity=0.18, stroke_width=0))
        cond_mu = always_redraw(lambda: DashedLine(
            ax2.c2p(media_cond(xv.get_value()), 0),
            ax2.c2p(media_cond(xv.get_value()), 1.05),
            color=VERDE, stroke_width=3, dash_length=0.09))

        # la marginal, de referencia
        marg = ax2.plot(lambda y: gauss(y, Y0, SY), x_range=[-3.2, 3.2],
                        color=AZUL, stroke_width=2.5)
        marg_lbl = MathTex(r"f_Y(y)", color=AZUL).scale(0.5)
        marg_lbl.next_to(ax2.c2p(-2.6, gauss(-1.3, Y0, SY)), UL, buff=0.02)

        self.play(Create(ax2), FadeIn(lab2), FadeIn(cond_tit))
        self.play(Create(marg), FadeIn(marg_lbl))
        self.wait(0.4)
        self.play(FadeIn(cond), FadeIn(cond_area), Create(cond_mu))
        self.wait(0.8)

        angosta = nota("más angosta que la marginal: medir X redujo la "
                       "incertidumbre", scale=0.44)
        angosta.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(angosta))
        self.wait(1.6)
        self.play(FadeOut(angosta))

        # ------------------------------------------------ la recta de regresion
        rastro = TracedPath(lambda: ax.c2p(xv.get_value(),
                                           media_cond(xv.get_value())),
                            stroke_color=VERDE, stroke_width=5)
        self.add(rastro)
        punto = always_redraw(lambda: Dot(
            ax.c2p(xv.get_value(), media_cond(xv.get_value())),
            color=VERDE, radius=0.08))
        self.play(FadeIn(punto))

        self.play(xv.animate.set_value(2.0), run_time=4.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.4)
        self.play(xv.animate.set_value(-0.6), run_time=2.2,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)

        # bien abajo, para no pisar la etiqueta "X = x" del corte
        reg = MathTex(r"\text{el rastro verde es}\quad E[Y\,|\,X=x]",
                      color=VERDE).scale(0.55)
        reg.to_edge(DOWN, buff=0.35).shift(LEFT * 3.0)
        self.play(Write(reg))
        self.wait(1.4)

        # ------------------------------------------------ el resultado
        res = VGroup(
            MathTex(r"\hat{y} \;=\; E[Y\,|\,X=x]", color=VERDE).scale(0.62),
            MathTex(r"\text{MMSE} \;=\; \sigma^2_{Y|X=x}", color=AMBAR).scale(0.62),
        ).arrange(DOWN, buff=0.24)
        res.next_to(ax2, DOWN, buff=0.45)
        self.play(Write(res[0]))
        self.wait(0.4)
        self.play(Write(res[1]))
        self.wait(1.8)

        # ------------------------------------------------ cierre
        self.remove(rastro)
        self.play(FadeOut(VGroup(ax, lab, puntos, conj, corte, x_lbl, punto,
                                 ax2, lab2, cond_tit, cond, cond_area, cond_mu,
                                 marg, marg_lbl, reg, res)))
        cierre = VGroup(
            Text("Sin medir:", color=INK).scale(0.58),
            MathTex(r"\hat{y}=\mu_Y \qquad \text{MMSE}=\sigma_Y^2",
                    color=AZUL).scale(0.72),
            Text("Midiendo X = x:", color=INK).scale(0.58),
            MathTex(r"\hat{y}=E[Y|X=x] \qquad \text{MMSE}=\sigma^2_{Y|X=x}",
                    color=VERDE).scale(0.72),
        ).arrange(DOWN, buff=0.26)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]), FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]), FadeIn(cierre[3], shift=UP * 0.12))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
