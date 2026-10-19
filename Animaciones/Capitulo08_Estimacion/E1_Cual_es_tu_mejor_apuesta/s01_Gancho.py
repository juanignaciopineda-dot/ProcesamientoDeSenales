"""Escena 01 — Gancho: la mejor apuesta del dado es 3,5, un número que el dado no saca."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        d = dado_n(5).scale(2.2).move_to([0, 0.2, 0])
        q = Text("?", color=ESTIMACION, weight=BOLD).scale(2.2).move_to([0, 2.7, 0])
        R = Regla7(centro=(0, -0.6), ancho=10.4)
        caras = caras7(R, escala=0.85, altura=1.2)
        t35 = Text("3,5", color=ESTIMACION, weight=BOLD).scale(1.5).move_to(R.p(3.5) + DOWN * 1.8)
        flecha35 = Arrow(t35.get_top() + UP * 0.05, R.p(3.5) + DOWN * 0.08, buff=0, color=ESTIMACION, stroke_width=5)
        x35 = cruz(ROJO, 1.6).move_to(t35)

        with self.narrar("b1"):
            # «tirar un dado»
            self.en("dado")
            self.play(FadeIn(d, scale=0.6), run_time=self.dur(0.5))

            # «adivinar qué número sale»
            self.en("adivinar")
            self.pop(q)

            # «La mejor apuesta»
            self.en("mejor")
            self.play(FadeOut(q), FadeOut(d), run_time=0.25)
            self.play(FadeIn(R), FadeIn(caras, lag_ratio=0.15), run_time=self.dur(0.8))

            # «tres coma cinco»
            self.en("tres5")
            self.play(GrowArrow(flecha35), run_time=self.dur(0.3))
            self.pop(t35)

            # «no saca nunca»
            self.en("nunca")
            self.sfx("error")
            self.play(FadeIn(x35, scale=1.6), run_time=self.dur(0.4))
        self.wait(1.0)
        self.limpiar()
