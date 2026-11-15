"""Escena 01 — Gancho: dale la vuelta a una señal, úsala como filtro y tienes el mejor detector."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        s = Tallos(S13, centro=(-3.5, -0.4), paso=0.8, unidad=0.55, color=SENAL)
        h = Tallos(H13, centro=(-3.5, -0.4), paso=0.8, unidad=0.55, color=ESTIMACION)
        bl = BloqueLTI("h", centro=(1.0, 0.0), ancho=2.0, alto=1.4, color=ESTIMACION, largo=1.6)
        cor = corona().scale(1.2).move_to([1.0, 2.6, 0])
        al = alarma13().scale(1.2).move_to([5.3, 0.0, 0])
        lp = lupa(TXT).scale(1.6).move_to([4.6, -2.2, 0])
        lp.permitir_encima = True
        with self.narrar("b1"):
            # «Dale la vuelta a una señal»
            self.en("vuelta")
            self.play(FadeIn(s), run_time=self.dur(0.4))
            self.sfx("whoosh")
            self.play(Transform(s, h), run_time=self.dur(0.8))

            # «úsala como filtro»
            self.en("filtro")
            self.play(FadeIn(bl), s.animate.scale(0.5).move_to([1.0, 1.35, 0]), run_time=self.dur(0.8))

            # «el mejor detector»
            self.en("mejor")
            self.play(FadeIn(cor, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «que se puede construir»
            self.en("construir")
            self.play(FadeIn(al, scale=0.7), run_time=self.dur(0.4))
            self.sfx("alarma", gain=-18)
            self.resaltar(al, color=ROJO, escala=1.25)

            # «Hoy vemos por qué»
            self.en("porque")
            self.play(FadeIn(lp, scale=0.6), run_time=self.dur(0.4))
            self.play(lp.animate.move_to([1.6, -0.4, 0]), run_time=self.dur(1.0))
        self.wait(1.0)
        self.limpiar()
