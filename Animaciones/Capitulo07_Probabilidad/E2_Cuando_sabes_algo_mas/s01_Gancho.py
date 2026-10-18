"""Escena 01 — Gancho: un test que acierta el 99 % y un positivo que casi siempre es falso."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        tira = tira_test07(1.5).move_to([-4.3, 0.0, 0])
        t99 = Text("99 %", color=VERDE, weight=BOLD).scale(2.4).move_to([0.3, 1.9, 0])
        marco = Rectangle(width=3.6, height=0.35, color=VERDE, stroke_width=3).move_to([0.3, 0.7, 0])
        relleno = Rectangle(width=3.6 * 0.99, height=0.35, stroke_width=0).set_fill(VERDE, 0.8)
        relleno.align_to(marco, LEFT).match_y(marco)
        mas = Text("+", color=ERROR, weight=BOLD).scale(3.0).move_to(tira.ventana)
        pers = persona(VERDE).scale_to_fit_height(2.8).move_to([4.4, -0.2, 0])
        etq = Text("Sano", color=VERDE, weight=BOLD).scale(0.7).next_to(pers, DOWN, buff=0.25)
        mas2 = Text("+", color=ERROR, weight=BOLD).scale(2.2).next_to(pers, UR, buff=-0.2)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(2.8).move_to([1.9, -0.5, 0])

        with self.narrar("b1"):
            # «Un test médico»
            self.en("test")
            self.play(FadeIn(tira, shift=UP * 0.3), run_time=self.dur(0.6))

            # «noventa y nueve por ciento»
            self.en("99")
            self.pop(t99)
            self.play(FadeIn(marco), GrowFromEdge(relleno, LEFT), run_time=self.dur(0.7))

            # «Das positivo»
            self.en("positivo")
            self.pop(mas, sonido="error")

            # «lo más probable es que estés sano»
            self.en("sano")
            self.play(FadeIn(pers), FadeIn(etq), run_time=self.dur(0.5))
            self.pop(mas2)

            # «¿Cómo puede ser?»
            self.en("pregunta")
            self.pop(interr)
        self.wait(1.0)
        self.limpiar()
