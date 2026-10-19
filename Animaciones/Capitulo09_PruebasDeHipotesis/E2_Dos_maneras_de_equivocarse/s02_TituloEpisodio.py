"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = Text("Dos maneras", color=TXT, weight=BOLD).scale(1.35).move_to([0, 0.65, 0])
        t2 = Text("de equivocarse", color=ESTIMACION, weight=BOLD).scale(1.35).move_to([0, -0.65, 0])
        et = Text("Capítulo 9 · Pruebas de hipótesis", color=INK).scale(0.5).move_to([0, -2.0, 0])

        with self.narrar("b1"):
            # «Dos maneras»
            self.en("t1")
            self.pop(t1)

            # «de equivocarse»
            self.en("t2")
            self.pop(t2, sonido=None)
            self.play(FadeIn(et, shift=UP * 0.2), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
