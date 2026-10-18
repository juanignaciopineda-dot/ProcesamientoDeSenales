"""Escena 03 — Qué es una variable aleatoria: una regla que le pone un número a cada resultado."""
from comun.escena import *


class VariableAleatoria(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        textos = ["Cara", "Cruz", "Sano", "Enfermo"]
        ys = [2.3, 1.0, -0.8, -2.1]
        chips = VGroup(*[caja(s, INK, ancho=2.5, alto=0.95, scale=0.75).move_to([-3.4, y, 0])
                         for s, y in zip(textos, ys)])
        interr = VGroup(*[Text("?", color=ERROR, weight=BOLD).scale(1.0).move_to([-1.6, y, 0]) for y in ys])
        mon = moneda().scale(1.3).move_to([-6.0, 1.65, 0])
        pac = persona(CIAN).scale(1.5).move_to([-6.0, -1.45, 0])
        recta = RectaNum(-0.5, 1.5, centro=(4.2, 1.6), ancho=4.8, marcas=[0, 1], tam=0.8)

        with self.narrar("b1"):
            self.en("numeros")                                # «no siempre son números»
            self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.2) for c in chips], lag_ratio=0.2),
                      FadeIn(interr), run_time=self.dur(1.4))
            self.en("moneda")                                 # «Una moneda da cara o cruz»
            self.play(FadeIn(mon, scale=0.7), chips[0].animate.set_stroke(AMBAR), chips[1].animate.set_stroke(AMBAR),
                      run_time=self.dur(0.6))
            self.en("paciente")                               # «Un paciente está sano o enfermo»
            self.play(FadeIn(pac, scale=0.7), chips[2].animate.set_stroke(CIAN), chips[3].animate.set_stroke(CIAN),
                      run_time=self.dur(0.6))
            self.en("cuentas")                                # «hacer cuentas»
            pq = formula("P", "(", "?", ")", escala=1.5, colores={0: AMBAR, 2: AMBAR}).move_to([4.2, 3.1, 0])
            self.play(Write(pq), run_time=self.dur(0.9))
            self.en("regla")                                  # «una regla que le ponga un número»
            self.play(FadeIn(recta), run_time=self.dur(0.6))
            self.en("cada_res")                               # «a cada resultado»
            cortas = VGroup(*[Arrow(c.get_right() + RIGHT * 0.05, c.get_right() + RIGHT * 1.0, color=INK,
                                    stroke_width=3, buff=0) for c in chips])
            nums = VGroup(*[Text("N", color=AMBAR, weight=BOLD).scale(0.8).next_to(a, RIGHT, buff=0.1) for a in cortas])
            self.play(FadeOut(interr), FadeOut(pq), *[Create(a) for a in cortas], FadeIn(nums), run_time=self.dur(0.8))
            self.en("va")                                     # «variable aleatoria»
            pal = self.palabra("Variable aleatoria", AMBAR, 1.1).move_to([3.4, 3.2, 0])
            self.pop(pal)
            self.en("cara_uno")                               # «cara vale uno y cruz vale cero»
            fa = Arrow(chips[0].get_right(), recta.p(1) + UP * 0.12, color=AMBAR, stroke_width=5, buff=0.08)
            fb = Arrow(chips[1].get_right(), recta.p(0) + UP * 0.12, color=AMBAR, stroke_width=5, buff=0.08)
            self.play(FadeOut(cortas), FadeOut(nums), Create(fa), Create(fb), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
