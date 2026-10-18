"""Escena 10 — Deducción de σ² = E[X²] − μ², paso a paso."""
from comun.escena import *


class FormulaPractica(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        r1 = MathTex(r"\sigma^2", "=", "E[", r"(X-\mu)^2", "]", color=TXT).scale(1.3).move_to([-1.8, 3.0, 0])
        r2 = MathTex("=", "E[", "X^2", r"-2\mu X", r"+\mu^2", "]", color=TXT).scale(1.3).move_to([-1.8, 1.6, 0])
        r3 = MathTex("=", "E[X^2]", r"-2\mu", "E[X]", r"+\mu^2", color=TXT).scale(1.3).move_to([-1.8, 0.2, 0])
        r4 = MathTex("=", "E[X^2]", r"-2\mu^2", r"+\mu^2", color=TXT).scale(1.3).move_to([-1.8, -1.2, 0])
        r5 = MathTex("=", "E[X^2]", r"-\mu^2", color=TXT).scale(1.3).move_to([-1.8, -2.7, 0])
        r5[2].set_color(AMBAR)
        for r in (r2, r3, r4, r5):
            r.shift(RIGHT * (r1[1].get_left()[0] - r[0].get_left()[0]))
        regla_2 = Text("Desarrollar el cuadrado", color=INK).scale(0.5).move_to([5.0, 1.6, 0])
        regla_3 = Text("Linealidad", color=INK).scale(0.5).move_to([5.0, 0.2, 0])
        ex_mu = MathTex("E[X]", "=", r"\mu", color=AMBAR).scale(0.9).move_to([5.0, -0.5, 0])
        juntar = MathTex(r"-2\mu^2+\mu^2=-\mu^2", color=AMBAR).scale(0.8).move_to([4.6, -1.2, 0])
        lente = lupa().scale(0.9).move_to(r1.get_right() + RIGHT * 0.2 + UP * 0.1)
        with self.narrar("b1"):
            # «una forma más cómoda»
            self.en("comoda")
            self.play(FadeIn(r1, shift=DOWN * 0.15), run_time=self.dur(1.2))
            # «de dónde sale»
            self.en("donde_sale")
            self.play(FadeIn(lente), run_time=0.3)
            self.play(lente.animate.shift(LEFT * 3.0), run_time=self.dur(1.0))
            self.play(FadeOut(lente), run_time=0.3)

            # «desarrollamos el cuadrado»
            self.en("desarrollo")
            self.play(FadeIn(r2, shift=DOWN * 0.15), FadeIn(regla_2), run_time=self.dur(1.0))
            # «equis al cuadrado»
            self.en("x2")
            self.play(Indicate(r2[2], color=AMBAR), run_time=self.dur(0.8))
            # «menos dos mu equis»
            self.en("dos_mu")
            self.play(Indicate(r2[3], color=AMBAR), run_time=self.dur(0.8))
            # «más mu al cuadrado»
            self.en("mu2")
            self.play(Indicate(r2[4], color=AMBAR), run_time=self.dur(0.8))

            # «la linealidad»
            self.en("linealidad")
            self.play(FadeIn(r3, shift=DOWN * 0.15), FadeIn(regla_3), run_time=self.dur(1.0))
            # «la esperanza de equis es mu»
            self.en("ex_mu")
            self.play(Indicate(r3[3], color=AMBAR), FadeIn(ex_mu, shift=LEFT * 0.15), run_time=self.dur(1.0))

            # «menos dos mu al cuadrado»
            self.en("menos2mu2")
            self.play(FadeIn(r4, shift=DOWN * 0.15), run_time=self.dur(0.8))
            # «al juntar todo»
            self.en("juntar")
            self.play(FadeIn(juntar, shift=LEFT * 0.15), run_time=self.dur(0.8))
            # «la varianza es la esperanza de equis al cuadrado»
            self.en("result")
            self.play(FadeIn(r5[0:2], shift=DOWN * 0.15), run_time=self.dur(0.7))
            # «menos mu al cuadrado»
            self.en("menos_mu2")
            self.play(FadeIn(r5[2], shift=LEFT * 0.15), run_time=self.dur(0.6))
            self.sfx("exito")
            self.play(Create(SurroundingRectangle(r5, color=AMBAR, buff=0.2)), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
