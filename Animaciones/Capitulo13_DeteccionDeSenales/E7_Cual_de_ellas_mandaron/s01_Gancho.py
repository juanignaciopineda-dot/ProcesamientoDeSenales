"""Escena 01 — Gancho: mismo pulso, misma energía, cincuenta veces menos errores."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        pulso = pulso7([2, 2, 1], centro=(-4.6, 0.6), paso=0.8, unidad=0.55)
        E = MathTex("E=9", color=AMBAR).scale(1.0).move_to([-4.6, -1.0, 0])
        y0 = -1.4
        b1 = Rectangle(width=1.0, height=2.6, color=ERROR, stroke_width=3).set_fill(ERROR, 0.5)
        b1.move_to([0.2, y0 + 1.3, 0])
        b2 = Rectangle(width=1.0, height=0.07, color=ERROR, stroke_width=3).set_fill(ERROR, 0.9)
        b2.move_to([2.2, y0 + 0.035, 0])
        v1 = MathTex("0{,}0668", color=TXT).scale(0.85).next_to(b1, UP, buff=0.15)
        v2 = MathTex("0{,}00135", color=TXT).scale(0.85).next_to(b2, UP, buff=0.15)
        suelo = Line([-0.6, y0, 0], [3.0, y0, 0], color=INK, stroke_width=2)
        d50 = Text("÷ 50", color=AMBAR, weight=BOLD).scale(0.9).move_to([1.5, 0.7, 0])
        grupo_err = VGroup(b1, b2, v1, v2, suelo, d50)
        mod = modem7(INK).scale(1.5).move_to([-0.6, 0.6, 0])
        sal = Arrow([0.5, 0.6, 0], [1.9, 0.6, 0], color=INK, buff=0, stroke_width=4)
        uno = pulso7([2, 2, 1], centro=(4.4, 1.5), color=SENAL, paso=0.6, unidad=0.4)
        menos = pulso7([-2, -2, -1], centro=(4.4, -0.6), color=AZUL_C7, paso=0.6, unidad=0.4)
        bit1 = Text("bit 1", color=INK).scale(0.45).next_to(uno, RIGHT, buff=0.5)
        bit0 = Text("bit 0", color=INK).scale(0.45).next_to(menos, RIGHT, buff=0.5)
        with self.narrar("b1"):
            # «Mismo pulso»
            self.paso("pulso", pulso, t=0.7)
            # «misma energía»
            self.paso("energia", E, t=0.5)
            # «cincuenta veces menos errores»
            self.en("cincuenta")
            self.play(FadeIn(suelo), FadeIn(b1), FadeIn(v1), run_time=0.5)
            self.play(FadeIn(b2), FadeIn(v2), run_time=0.4)
            self.pop(d50)
            # «Hoy vemos por qué»
            self.en("hoy")
            self.play(FadeOut(grupo_err), run_time=0.4)
            # «los módems envían»
            self.paso("modem", mod, GrowArrow(sal), t=0.6)
            # «cada bit y su contrario»
            self.en("contrario")
            self.play(FadeIn(uno), FadeIn(bit1), run_time=0.5)
            self.play(FadeIn(menos), FadeIn(bit0), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
