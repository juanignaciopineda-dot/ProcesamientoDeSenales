"""Escena 03 — Adivinar un número: estimar es apostar un valor antes de que el dado caiga."""
from comun.escena import *


class AdivinarUnNumero(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        cE = caja("Estimar", ESTIMACION, ancho=4.0, alto=1.4, scale=1.0).move_to([-3.2, 0.4, 0])
        cD = caja("Detectar", AZUL, ancho=4.0, alto=1.4, scale=1.0).move_to([3.2, 0.4, 0])
        etq = etiqueta("Estimar", ESTIMACION, 0.8, BOLD).move_to([0, 3.4, 0])
        cap7 = etiqueta("Capítulo 7 · Modelos probabilísticos", INK, 0.65).move_to([0, 3.0, 0])
        d = dado_n(1).scale(1.9).move_to([0, -0.2, 0])
        q = Text("?", color=ESTIMACION, weight=BOLD).scale(1.8).move_to([0, 1.8, 0])
        burb = burbuja_pensamiento(Text("?", color=ESTIMACION, weight=BOLD).scale(0.8)).scale(2.2).move_to([-4.6, 0.3, 0])
        diana = VGroup(*[Circle(radius=r, color=INK, stroke_width=3) for r in (0.95, 0.62, 0.3)],
                       Dot(radius=0.12, color=ESTIMACION)).move_to([4.6, 0.1, 0])
        pregunta = Text("¿Qué número dices?", color=ESTIMACION, weight=BOLD).scale(1.2).move_to([0, -2.9, 0])

        with self.narrar("b1"):
            # «primer capítulo»
            self.en("primero")
            self.play(FadeIn(cap7, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «estimar y detectar»
            self.en("dos")
            self.play(FadeIn(cE, shift=RIGHT * 0.3), FadeIn(cD, shift=LEFT * 0.3), run_time=self.dur(0.6))

            # «Empezamos por estimar»
            self.en("estimar")
            self.play(FadeOut(cD), cE.animate.move_to([0, 0.4, 0]).scale(1.3), run_time=self.dur(0.6))

            # «el caso más sencillo posible»
            self.en("sencillo")
            self.corte()
            self.play(FadeIn(etq), run_time=self.dur(0.4))

            # «Voy a tirar un dado»
            self.en("tirar")
            self.play(FadeIn(d, scale=0.6), run_time=self.dur(0.3))
            for n in (4, 2, 6):
                nuevo = dado_n(n).scale(1.9).move_to(d)
                self.sfx("tick", gain=-18)
                self.play(ReplacementTransform(d, nuevo), run_time=0.2)
                d = nuevo

            # «Antes de que lo tire»
            self.en("antes")
            self.pop(q)

            # «tienes que decirme un número»
            self.en("numero")
            self.play(FadeIn(burb, shift=RIGHT * 0.3), run_time=self.dur(0.5))

            # «te equivoques lo menos posible»
            self.en("menos")
            self.play(FadeIn(diana, scale=0.6), run_time=self.dur(0.5))

            # «¿Qué número dices?»
            self.en("pregunta")
            self.pop(pregunta)
        self.wait(1.0)
        self.limpiar()
