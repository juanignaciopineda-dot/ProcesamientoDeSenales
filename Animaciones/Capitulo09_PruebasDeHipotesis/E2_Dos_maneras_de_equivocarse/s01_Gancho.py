"""Escena 01 — Gancho: el mismo test da un 2 % o un 95 %, y no depende del test."""
from comun.escena import *
from comun.figuras_c9e2 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        tira = tira_test07(1.1).move_to([0, 0.1, 0])
        t99 = casilla9("Enfermo → Positivo 99 %", C1, ancho=4.8, alto=0.7, escala=0.42).move_to([-3.6, -2.9, 0])
        t5 = casilla9("Sano → Positivo 5 %", C0, ancho=4.8, alto=0.7, escala=0.42).move_to([3.6, -2.9, 0])
        cand = candado(INK).scale(0.45).move_to([0, -2.9, 0])
        mas = Text("+", color=ERROR, weight=BOLD).scale(1.2).move_to(tira.ventana)
        prob = MathTex(r"P(\text{Enfermo}\mid +)", "=", "?", color=TXT).scale(1.05).move_to([-0.4, 3.2, 0])
        prob[2].set_color(ESTIMACION)
        v2 = Text("2 %", color=ERROR, weight=BOLD).scale(1.1).next_to(prob[1], RIGHT, buff=0.3)
        v95 = Text("95 %", color=VERDE, weight=BOLD).scale(1.1).move_to([4.0, 0.6, 0])
        flecha_ = CurvedDoubleArrow([-3.6, 1.25, 0], [3.6, 1.25, 0], angle=-PI / 4, color=INK, stroke_width=3)
        duda = Text("?", color=ESTIMACION, weight=BOLD).scale(2.2).move_to([1.7, 0.4, 0])

        with self.narrar("b1"):
            # «Un mismo test»
            self.en("test")
            self.play(FadeIn(tira, shift=UP * 0.3), run_time=self.dur(0.6))

            # «sin tocarle nada»
            self.en("nada")
            self.play(FadeIn(t99), FadeIn(t5), FadeIn(cand, scale=0.5), run_time=self.dur(0.6))

            # «Si das positivo»
            self.en("positivo")
            self.play(tira.ventana.animate.set_stroke(ERROR, 5), run_time=self.dur(0.3))
            self.pop(mas)

            # «la probabilidad de estar enfermo»
            self.en("prob")
            self.play(Write(prob), run_time=self.dur(0.8))

            # «un dos por ciento»
            self.en("dos")
            self.play(FadeOut(prob[2]), run_time=0.2)
            self.pop(v2)

            # «un noventa y cinco»
            self.en("noventa")
            self.play(v2.animate.move_to([-4.0, 0.6, 0]), run_time=self.dur(0.4))
            self.pop(v95)
            self.play(Create(flecha_), run_time=self.dur(0.5))

            # «no depende del test»
            self.en("nodepende")
            tira.save_state()
            self.play(VGroup(tira, mas).animate.fade(0.65), run_time=self.dur(0.4))
            self.pop(duda)
        self.wait(1.0)
        self.limpiar()
