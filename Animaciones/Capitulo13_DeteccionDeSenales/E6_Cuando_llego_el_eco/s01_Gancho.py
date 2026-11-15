"""Escena 01 — Gancho: dos pulsos con la misma energía; con uno, dos aviones parecen uno."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        rect = Tallos([1] * 13, centro=(-3.6, 1.4), paso=0.4, unidad=1.0, color=SENAL)
        bark = Tallos(list(BARKER13), centro=(3.6, 1.4), paso=0.4, unidad=1.0, color=SENAL)
        e1 = MathTex("E=13", color=AMBAR).scale(1.2).move_to([-3.6, 0.1, 0])
        e2 = MathTex("E=13", color=AMBAR).scale(1.2).move_to([3.6, 0.1, 0])
        av1 = avion(AZUL).scale(1.5).move_to([-3.6, -1.5, 0])
        av2 = avion(AZUL).scale(1.5).move_to([3.6, -1.5, 0])
        ok1 = tilde(VERDE, 0.5).move_to([-2.1, -1.5, 0])
        ok2 = tilde(VERDE, 0.5).move_to([5.2, -1.5, 0])
        av3 = avion(AZUL).scale(1.5).move_to([-2.9, -1.5, 0])
        interr = Text("¿uno solo?", color=ROJO, weight=BOLD).scale(0.8).move_to([-3.6, -3.0, 0])
        with self.narrar("b1"):
            # «Dos pulsos»
            self.en("dos")
            self.play(FadeIn(rect), FadeIn(bark), run_time=self.dur(0.8))
            # «la misma energía»
            self.en("energia")
            self.pop(e1, e2)
            # «detectan un avión igual de bien»
            self.en("igual")
            self.play(FadeIn(av1), FadeIn(av2), run_time=0.4)
            self.play(FadeIn(ok1), FadeIn(ok2), run_time=self.dur(0.4))
            # «Pero con uno de ellos»
            self.en("pero")
            self.play(VGroup(bark, e2, av2, ok2).animate.fade(0.7), run_time=0.4)
            self.resaltar(rect, color=AMBAR, run_time=0.5)
            # «dos aviones cercanos»
            self.en("cercanos")
            self.play(FadeOut(ok1), av1.animate.move_to([-4.4, -1.5, 0]), FadeIn(av3), run_time=self.dur(0.7))
            # «parecen uno solo»
            self.en("uno")
            self.play(av1.animate.move_to([-3.6, -1.5, 0]), av3.animate.move_to([-3.6, -1.5, 0]),
                      FadeIn(interr), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
