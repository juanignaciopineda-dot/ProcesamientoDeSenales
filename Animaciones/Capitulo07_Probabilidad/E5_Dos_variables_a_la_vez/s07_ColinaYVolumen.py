"""Escena 07 — La probabilidad de una región es el volumen de colina que hay encima; el volumen total vale uno."""
from comun.escena import *


class ColinaYVolumen(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        c = Curva(lambda x: gaussiana(x, 0, 1), x_rango=(-3, 3), y_max=0.5, ancho=7.0, alto=3.4,
                  x_label="x", y_label="f_X(x)").move_to([0, -0.3, 0])
        area = c.area(-1, 1, AMBAR)
        colina = Colina(centro=(-0.6, -0.9), rho=0.82, ancho=6.6, prof=3.2, alto=3.0, n=19)
        region = colina.region(0.2, 1.4, -0.2, 1.2, AMBAR, k=7)
        integral = formula(r"P\big((X,Y)\in R\big)", "=", r"\iint_R", r"f_{XY}(x,y)", r"\,dx\,dy",
                           escala=1.0, colores={0: AMBAR}).move_to([0, 3.3, 0])
        entera = colina.region(-colina.r, colina.r, -colina.r, colina.r, VERDE, k=19)
        uno = MathTex(r"=\,1", color=VERDE).scale(1.8).move_to([5.0, 0.4, 0])
        with self.narrar("b1"):
            # «un área bajo una curva»
            self.en("area")
            self.play(Create(c.ejes), FadeIn(c.etiquetas), run_time=self.dur(0.5))
            self.play(Create(c.grafica), run_time=self.dur(0.8))
            self.play(FadeIn(area), run_time=self.dur(0.5))

            # «un volumen bajo la colina»
            self.en("volumen")
            self.play(FadeOut(VGroup(c, area)), run_time=0.3)
            self.play(FadeIn(colina.base), run_time=0.3)
            self.play(LaggedStart(*[AnimationGroup(FadeIn(r[0]), FadeIn(r[1])) for r in colina.filas],
                                  lag_ratio=0.05), run_time=self.dur(1.5))

            # «la probabilidad de que la pareja caiga»
            self.en("cae")
            gota = Dot(colina.P(0.8, 0.5) + UP * 2.4, radius=0.13, color=AMBAR)
            self.add(gota)
            self.play(gota.animate.move_to(colina.P(0.8, 0.5)), run_time=self.dur(0.9), rate_func=rate_functions.ease_in_quad)
            self.play(FadeOut(gota), run_time=0.2)

            # «una región del plano»
            self.en("region")
            self.play(FadeIn(region[0]), run_time=self.dur(0.5))
            r_ = self.palabra("R", AMBAR, 1.1).move_to(colina.P(0.8, 0.5) + DOWN * 0.45 + LEFT * 0.7)
            r_.permitir_encima = True
            self.pop(r_)

            # «el volumen de colina»
            self.en("bloque")
            self.play(FadeIn(region[1]), run_time=self.dur(0.8))

            # «una integral doble»
            self.en("integral")
            self.play(FadeIn(integral[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            self.play(FadeIn(integral[2:], shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «sumar a lo largo de los dos ejes»
            self.en("ejes")
            a_x = Arrow(colina.P(0.2, -0.2) + DOWN * 0.3, colina.P(1.4, -0.2) + DOWN * 0.3, color=AMBAR, buff=0,
                        stroke_width=5, max_tip_length_to_length_ratio=0.2)
            a_y = Arrow(colina.P(1.4, -0.2) + RIGHT * 0.25 + DOWN * 0.15, colina.P(1.4, 1.2) + RIGHT * 0.25 + DOWN * 0.15,
                        color=AMBAR, buff=0, stroke_width=5, max_tip_length_to_length_ratio=0.2)
            dx = MathTex("dx", color=AMBAR).scale(0.9).next_to(a_x, DOWN, buff=0.1)
            dy = MathTex("dy", color=AMBAR).scale(0.9).next_to(a_y, RIGHT, buff=0.1)
            dx.permitir_encima = dy.permitir_encima = True
            self.play(GrowArrow(a_x), FadeIn(dx), run_time=self.dur(0.5))
            self.play(GrowArrow(a_y), FadeIn(dy), run_time=self.dur(0.5))

            # «el volumen total»
            self.en("total")
            self.play(FadeOut(VGroup(region, a_x, a_y, dx, dy, r_)), run_time=0.25)
            self.play(FadeIn(entera), run_time=self.dur(0.8))

            # «vuelve a valer uno»
            self.en("uno")
            self.pop(uno)
        self.wait(1.0)
        self.limpiar()
