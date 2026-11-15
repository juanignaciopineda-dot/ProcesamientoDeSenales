"""Escena 01 — Gancho: una muestra sin relación con el futuro y aun así con coeficiente."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        F = FilaMuestras([r"x[n-3]", r"x[n-2]", r"x[n-1]", r"x[n]", r"x[n+1]"],
                         centro=(0.0, 0.2), lado=2.12, color=MEDIDA, escala=1.17)
        viejas = VGroup(F.cas[0], F.rots[0], F.cas[1], F.rots[1])
        recientes = VGroup(*F.cas[2:], *F.rots[2:])
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.17).next_to(F.cas[4], RIGHT, buff=0.25)
        arco = CurvedArrow(F.cas[2].get_top() + UP * 0.05, F.cas[4].get_top() + UP * 0.05,
                           angle=-PI / 2.2, color=ERROR, stroke_width=4)
        sinrel = Text("correlación = 0", color=ERROR).scale(0.78).move_to([1.7, 2.45, 0])
        h1 = MathTex("h_1", "=", color=AMBAR).scale(1.30).next_to(F.cas[2], DOWN, buff=0.55)
        val = MathTex(r"-0{,}19", color=AMBAR).scale(1.30).next_to(h1, RIGHT, buff=0.15)
        dist = Text("≠ 0", color=VERDE, weight=BOLD).scale(1.04).next_to(val, RIGHT, buff=0.3)
        lup = lupa(TXT).scale(1.1).move_to(F.cas[2].get_center() + RIGHT * 0.6 + DOWN * 0.5)
        lup.permitir_encima = True
        for m in (interr, sinrel, dist):
            m.permitir_fuera = True

        with self.narrar("b1"):
            # «Hay una muestra»
            self.en("muestra")
            self.play(FadeIn(recientes), run_time=self.dur(0.6))
            self.play(F.cas[2].animate.set_stroke(AMBAR), run_time=0.3)

            # «ninguna relación con lo que quieres adivinar»
            self.en("sinrel")
            self.play(FadeIn(interr), Create(arco), run_time=self.dur(0.7))
            self.play(FadeIn(sinrel), run_time=0.3)

            # «las cuentas le dan un coeficiente»
            self.en("coef")
            self.play(FadeIn(h1), run_time=self.dur(0.4))

            # «distinto de cero»
            self.en("distinto")
            self.pop(val)
            self.play(FadeIn(dist), run_time=0.3)

            # «Hoy vemos por qué»
            self.en("hoy")
            self.play(FadeIn(lup), run_time=self.dur(0.5))

            # «cuánto pasado hace falta»
            self.en("pasado")
            self.play(FadeOut(lup), FadeIn(viejas), run_time=self.dur(0.7))
            self.play(viejas.animate.fade(0.5), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
