"""Escena 01 — Gancho: un segundo termómetro, peor que el primero, puede no servir o dejar el error en cero."""
from comun.escena import *
from comun.figuras_c8e5 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        A = Termo8("A", centro=(-4.9, 0.7), alto=3.4, escala_letra=1.1)
        B = Termo8("B", centro=(-1.3, 0.7), alto=3.4, escala_letra=1.1)
        ra = A.debajo(ruido8(ancho=2.2, amp=0.09, semilla=2, grosor=4), 0.35)
        rb = B.debajo(ruido8(ancho=2.2, amp=0.34, semilla=5, grosor=4), 0.35)
        base_y = -2.2
        barra = Rectangle(width=1.6, height=3.2, color=ERROR, stroke_width=0).set_fill(ERROR, 0.85)
        barra.move_to([3.9, base_y + 1.6, 0])
        suelo = Line([2.5, base_y, 0], [5.3, base_y, 0], color=INK, stroke_width=2)
        rot = Text("Error", color=INK).scale(0.65).move_to([3.9, base_y - 0.45, 0])
        val = Text("0,8", color=TXT).scale(0.85).next_to(barra, UP, buff=0.15)
        cero = Text("0", color=VERDE, weight=BOLD).scale(1.4).move_to([3.9, base_y + 0.7, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to([-3.1, 0.9, 0])

        with self.narrar("b1"):
            # «Pones un segundo termómetro»
            self.en("segundo")
            self.play(FadeIn(A), run_time=0.4)
            self.play(FadeIn(B, shift=LEFT * 0.4), run_time=self.dur(0.5))

            # «peor que el primero»
            self.en("peor")
            self.play(Create(ra), Create(rb), run_time=self.dur(0.6))
            self.play(Wiggle(B, scale_value=1.05, rotation_angle=0.05 * TAU), run_time=self.dur(0.8))

            # «no servir de nada»
            self.en("nada")
            self.play(Create(suelo), GrowFromEdge(barra, DOWN), FadeIn(rot), run_time=self.dur(0.6))
            self.play(FadeIn(val, shift=DOWN * 0.1), run_time=0.3)

            # «dejar el error en cero»
            self.en("cero")
            self.play(barra.animate.stretch_to_fit_height(0.03, about_edge=DOWN), FadeOut(val), run_time=self.dur(0.8))
            self.pop(cero, sonido="exito")

            # «¿De qué depende?»
            self.en("depende")
            self.pop(q)
        self.wait(1.0)
        self.limpiar()
