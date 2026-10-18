"""Escena 06 — La esperanza es lineal: E[aX + b] y la esperanza de una suma."""
from comun.escena import *


class Linealidad(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        e = MathTex("E[X]", "=", r"\mu", color=TXT).scale(1.5).move_to([-3.5, 3.0, 0])
        e[0].set_color(AMBAR)
        e[2].set_color(AMBAR)
        lin = self.palabra("Lineal", AMBAR, 1.2).move_to([4.2, 3.0, 0])
        f1 = MathTex("E[", "aX", "]", "=", "a", "E[X]", color=TXT).scale(1.2).move_to([0, 1.5, 0])
        f2 = MathTex("E[X+b]", "=", "E[X]", "+b", color=TXT).scale(1.2).move_to([0, 0.3, 0])
        dado = dado_n(5).scale(0.6).move_to([-5.8, -1.0, 0])
        f3 = MathTex("E[2X+1]", color=TXT).scale(1.2).move_to([-3.2, -1.0, 0])
        f3b = MathTex("=", r"2\cdot 3{,}5+1", color=TXT).scale(1.2).next_to(f3, RIGHT, buff=0.3)
        f3c = MathTex("=", "8", color=TXT).scale(1.2).next_to(f3b, RIGHT, buff=0.3)
        f3c[1].set_color(VERDE)
        g1 = MathTex("E[X+Y]", color=TXT).scale(1.2).move_to([-3.2, -2.5, 0])
        g2 = MathTex("=", "E[X]+E[Y]", color=TXT).scale(1.2).next_to(g1, RIGHT, buff=0.3)
        sello_ = sello("Siempre", VERDE).scale(0.9).move_to([5.2, -2.5, 0])
        with self.narrar("b1"):
            # «Se escribe E de equis»
            self.en("escribe")
            self.play(FadeIn(e[0:2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            # «o mu»
            self.en("mu")
            self.play(FadeIn(e[2], shift=DOWN * 0.15), run_time=self.dur(0.5))
            # «es lineal»
            self.en("lineal")
            self.pop(lin)

            # «multiplicas la variable por un número»
            self.en("mult")
            self.play(FadeIn(f1, shift=DOWN * 0.15), run_time=self.dur(1.0))
            # «se multiplica por ese número»
            self.en("se_mult")
            self.play(Indicate(f1[4], color=AMBAR), Indicate(f1[1][0], color=AMBAR), run_time=self.dur(0.9))

            # «Si le sumas algo»
            self.en("sumas")
            self.play(FadeIn(f2, shift=DOWN * 0.15), run_time=self.dur(1.0))

            # «dos veces el dado más uno»
            self.en("dado21")
            self.play(FadeIn(dado), FadeIn(f3, shift=DOWN * 0.15), run_time=self.dur(0.8))
            # «dos por tres coma cinco más uno»
            self.en("cuenta")
            self.play(FadeIn(f3b, shift=LEFT * 0.15), run_time=self.dur(0.7))
            # «ocho»
            self.en("ocho")
            self.play(FadeIn(f3c, shift=LEFT * 0.15), run_time=self.dur(0.5))
            self.sfx("exito")

            # «la esperanza de una suma»
            self.en("esp_suma")
            self.play(FadeIn(g1, shift=DOWN * 0.15), run_time=self.dur(0.7))
            # «es la suma de las esperanzas»
            self.en("suma_esp")
            self.play(FadeIn(g2, shift=LEFT * 0.15), run_time=self.dur(0.8))
            # «siempre»
            self.en("siempre")
            self.pop(sello_, sonido="impacto")
        self.wait(1.0)
        self.limpiar()
