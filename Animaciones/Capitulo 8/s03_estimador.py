"""Escena 3 - Estimacion contra estimador.

Con x ya observado, E[Y|X=x] es un NUMERO. Sin observar todavia, X es
aleatoria y E[Y|X] es una VARIABLE ALEATORIA, con su propia densidad.
La analogia del libro: f(3) contra f(.).

    manim -pql s03_estimador.py Estimador
"""
from manim import *
import numpy as np
from comun import *

RHO = 0.8
SX = SY = 1.0
N = 240


def media_cond(x):
    return RHO * (SY / SX) * x


class Estimador(Scene):
    def construct(self):
        configurar()

        tit = titulo("Estimación o estimador: número o variable aleatoria")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ la analogia
        izq = VGroup(
            MathTex(r"f(3)", color=VERDE).scale(1.0),
            Text("un número", color=INK).scale(0.5),
            nota("ya sé dónde evaluar", scale=0.42),
        ).arrange(DOWN, buff=0.2)
        der = VGroup(
            MathTex(r"f(\,\cdot\,)", color=AMBAR).scale(1.0),
            Text("una función", color=INK).scale(0.5),
            nota("todavía no sé dónde", scale=0.42),
        ).arrange(DOWN, buff=0.2)
        vs = Text("≠", color=ROJO).scale(0.9)
        fila = VGroup(izq, vs, der).arrange(RIGHT, buff=1.3)
        fila.move_to(UP * 0.4)

        self.play(FadeIn(izq, shift=RIGHT * 0.2))
        self.play(FadeIn(vs, scale=1.3))
        self.play(FadeIn(der, shift=LEFT * 0.2))
        self.wait(1.6)

        puente = Text("Con la estimación pasa exactamente lo mismo",
                      color=TXT).scale(0.6)
        puente.next_to(fila, DOWN, buff=0.9)
        self.play(FadeIn(puente))
        self.wait(1.6)
        self.play(FadeOut(VGroup(fila, puente)))

        # ------------------------------------------------ los dos casos
        caso1 = VGroup(
            MathTex(r"E[Y\,|\,X=3]", color=VERDE).scale(0.9),
            Text("ESTIMACIÓN", color=VERDE, weight=BOLD).scale(0.5),
            nota("un número: ya medí, x valía 3", scale=0.42),
        ).arrange(DOWN, buff=0.22)
        caso2 = VGroup(
            MathTex(r"\hat{Y} = E[Y\,|\,X]", color=AMBAR).scale(0.9),
            Text("ESTIMADOR", color=AMBAR, weight=BOLD).scale(0.5),
            nota("una variable aleatoria: X todavía no se observó", scale=0.42),
        ).arrange(DOWN, buff=0.22)
        fila2 = VGroup(caso1, caso2).arrange(RIGHT, buff=1.5)
        fila2.move_to(UP * 0.75)

        self.play(FadeIn(caso1, shift=UP * 0.15))
        self.wait(1.2)
        self.play(FadeIn(caso2, shift=UP * 0.15))
        self.wait(1.8)
        self.play(fila2.animate.scale(0.72).to_edge(UP, buff=1.15))

        # ------------------------------------------------ la nube y la densidad
        ax, lab = ejes([-3.0, 3.0, 3.0], [-3.0, 3.0, 3.0], ancho=4.4, alto=3.4,
                       x_label="x", y_label="y")
        ax.shift(LEFT * 3.2 + DOWN * 1.15)
        lab[0].next_to(ax.x_axis.get_end(), DR, buff=0.1)
        lab[1].next_to(ax.y_axis.get_end(), UR, buff=0.08)

        xs, ys = muestras_gauss(N, RHO, semilla=9)
        puntos = nube(ax, xs, ys, color=AZUL, radio=0.03, opacidad=0.5)
        recta = ax.plot(media_cond, x_range=[-3.0, 3.0], color=VERDE,
                        stroke_width=4)

        self.play(Create(ax), FadeIn(lab))
        self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in puntos],
                              lag_ratio=0.003, run_time=1.4))
        self.play(Create(recta))
        self.wait(0.4)

        # ------------------------------------------------ un valor concreto
        xf = ValueTracker(1.6)
        corte = always_redraw(lambda: DashedLine(
            ax.c2p(xf.get_value(), -3.0), ax.c2p(xf.get_value(), media_cond(xf.get_value())),
            color=AMBAR, stroke_width=2.6, dash_length=0.08))
        pto = always_redraw(lambda: Dot(
            ax.c2p(xf.get_value(), media_cond(xf.get_value())),
            color=VERDE, radius=0.075))
        horiz = always_redraw(lambda: DashedLine(
            ax.c2p(xf.get_value(), media_cond(xf.get_value())),
            ax.c2p(-3.0, media_cond(xf.get_value())),
            color=VERDE, stroke_width=2.2, dash_length=0.08))
        self.play(Create(corte), FadeIn(pto), Create(horiz))
        self.wait(0.8)

        # ------------------------------------------------ la densidad del estimador
        ax2, lab2 = ejes([-3.0, 3.0, 3.0], [0, 0.85], ancho=4.6, alto=2.4,
                         x_label=r"\hat{y}")
        ax2.shift(RIGHT * 3.3 + DOWN * 1.35)
        lab2.next_to(ax2.x_axis.get_end(), DR, buff=0.1)
        # Yhat = rho*(sy/sx)*X, con X ~ N(0, sx) -> Yhat ~ N(0, rho*sy)
        sd_est = RHO * SY
        dens = ax2.plot(lambda v: gauss(v, 0, sd_est), x_range=[-3.0, 3.0],
                        color=AMBAR, stroke_width=4)
        dens_area = ax2.get_area(dens, x_range=(-3.0, 3.0), color=AMBAR,
                                 opacity=0.16, stroke_width=0)
        d_tit = MathTex(r"\text{densidad de}\ \hat{Y}", color=AMBAR).scale(0.55)
        d_tit.next_to(ax2, UP, buff=0.25)

        self.play(Create(ax2), FadeIn(lab2), FadeIn(d_tit))
        self.play(Create(dens), FadeIn(dens_area))

        marca = always_redraw(lambda: Dot(
            ax2.c2p(media_cond(xf.get_value()),
                    gauss(media_cond(xf.get_value()), 0, sd_est)),
            color=VERDE, radius=0.075))
        self.play(FadeIn(marca))
        self.wait(0.6)

        # ------------------------------------------------ mover x
        msg = nota("si X cambia, la estimación cambia: por eso $\\hat{Y}$ "
                   "es aleatoria", scale=0.44)
        msg.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(msg))
        for destino in (-1.9, 2.2, -0.7):
            self.play(xf.animate.set_value(destino), run_time=1.5,
                      rate_func=rate_functions.ease_in_out_sine)
            self.wait(0.25)
        self.wait(0.8)
        self.play(FadeOut(msg))

        # ------------------------------------------------ el resultado no trivial
        self.play(FadeOut(VGroup(ax, lab, puntos, recta, corte, pto, horiz,
                                 ax2, lab2, dens, dens_area, d_tit, marca,
                                 fila2)))
        clave = VGroup(
            Text("Y algo que no es obvio:", color=INK).scale(0.55),
            MathTex(r"E_{Y,X}\big[(Y-\hat{y}(X))^2\big] \;=\;"
                    r"E_X\Big[\,E_{Y|X}\big[(Y-\hat{y}(X))^2\,\big|\,X\big]\Big]",
                    color=TXT).scale(0.66),
            nota("el estimador que minimiza el error para CADA x por separado", scale=0.5),
            nota("también minimiza el error PROMEDIADO sobre todos los x", scale=0.5),
        ).arrange(DOWN, buff=0.3)
        clave.move_to(ORIGIN)
        self.play(FadeIn(clave[0]))
        self.play(Write(clave[1]))
        self.wait(0.8)
        self.play(FadeIn(clave[2]))
        self.play(FadeIn(clave[3]))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, clave)))
        self.wait(0.3)
