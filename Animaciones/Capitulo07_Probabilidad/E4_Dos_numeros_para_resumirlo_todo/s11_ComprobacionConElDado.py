"""Escena 11 — Comprobación con el dado (σ² = 2,92) y la varianza de la uniforme."""
from comun.escena import *


class ComprobacionConElDado(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        d = dado_n(5).scale(0.8).move_to([-6.0, 3.2, 0])
        f0 = MathTex(r"\sigma^2", "=", "E[X^2]", r"-\mu^2", color=TXT).scale(1.3).move_to([-1.5, 3.2, 0])
        f1 = MathTex("E[X^2]", "=", "(1+4+9+16+25", "+36)", "/6", color=TXT).scale(1.2).move_to([-1.5, 1.8, 0])
        s91 = MathTex("=91", color=AMBAR).scale(0.8).next_to(f1[3], DOWN, buff=0.15)
        r1517 = MathTex("=", "15{,}17", color=TXT).scale(1.2).next_to(f1, RIGHT, buff=0.25)
        f2 = MathTex(r"\mu^2", "=", "3{,}5^2", color=TXT).scale(1.2).move_to([-3.8, 0.4, 0])
        r1225 = MathTex("=", "12{,}25", color=TXT).scale(1.2).next_to(f2, RIGHT, buff=0.25)
        f3 = MathTex("15{,}17", "-", "12{,}25", "=", "2{,}92", color=TXT).scale(1.4).move_to([-3.2, -0.9, 0])
        f3[4].set_color(VERDE)
        antes = MathTex("2{,}92", color=INK).scale(1.0).move_to([2.8, -0.9, 0])
        antes_t = Text("Antes", color=INK).scale(0.5).next_to(antes, UP, buff=0.1)
        igual = MathTex("=", color=VERDE).scale(1.2).move_to([1.6, -0.9, 0])
        # uniforme entre a y b
        base = Line([-6.0, -3.2, 0], [0.2, -3.2, 0], color=INK, stroke_width=2)
        rect = Rectangle(width=3.6, height=1.0, stroke_width=3, color=SENAL).set_fill(SENAL, 0.35
                        ).move_to([-2.9, -2.7, 0])
        a_t = MathTex("a", color=TXT).scale(0.9).move_to([-4.7, -3.6, 0])
        b_t = MathTex("b", color=TXT).scale(0.9).move_to([-1.1, -3.6, 0])
        ancho = DoubleArrow([-4.7, -1.9, 0], [-1.1, -1.9, 0], color=AMBAR, stroke_width=3, buff=0)
        ancho_t = MathTex("b-a", color=AMBAR).scale(0.9).move_to([-2.9, -1.55, 0])
        doce = MathTex(r"\sigma^2", "=", r"\frac{(b-a)^2}{12}", color=TXT).scale(1.3).move_to([3.4, -2.8, 0])
        doce[0].set_color(AMBAR)
        with self.narrar("b1"):
            # «Comprobémoslo con el dado»
            self.en("dado")
            self.play(FadeIn(d), FadeIn(f0, shift=DOWN * 0.15), run_time=self.dur(1.2))
            # «uno más cuatro más nueve»
            self.en("cuad")
            self.play(FadeIn(f1[0:3], shift=DOWN * 0.15), run_time=self.dur(1.6))
            # «treinta y seis»
            self.en("t36")
            self.play(FadeIn(f1[3], shift=DOWN * 0.15), FadeIn(s91), run_time=self.dur(0.6))
            # «entre seis»
            self.en("entre6")
            self.play(FadeIn(f1[4], shift=LEFT * 0.15), run_time=self.dur(0.5))
            # «quince coma diecisiete»
            self.en("q1517")
            self.play(FadeIn(r1517, shift=LEFT * 0.15), run_time=self.dur(0.6))
            # «tres coma cinco al cuadrado»
            self.en("mu2")
            self.play(FadeIn(f2, shift=DOWN * 0.15), run_time=self.dur(0.7))
            # «doce coma veinticinco»
            self.en("doce25")
            self.play(FadeIn(r1225, shift=LEFT * 0.15), run_time=self.dur(0.6))
            # «dos coma noventa y dos»
            self.en("r292")
            self.play(FadeIn(f3, shift=DOWN * 0.15), run_time=self.dur(1.2))
            self.sfx("exito")
            # «lo mismo que antes»
            self.en("igual")
            self.play(FadeIn(antes_t), FadeIn(antes), FadeIn(igual), run_time=self.dur(0.8))

            # «una uniforme entre a y b»
            self.en("unif")
            self.play(Create(base), FadeIn(rect), FadeIn(a_t), FadeIn(b_t), run_time=self.dur(1.0))
            # «el ancho al cuadrado»
            self.en("ancho")
            self.play(GrowFromCenter(ancho), FadeIn(ancho_t), run_time=self.dur(0.8))
            # «entre doce»
            self.en("doce")
            self.play(FadeIn(doce, shift=LEFT * 0.15), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
