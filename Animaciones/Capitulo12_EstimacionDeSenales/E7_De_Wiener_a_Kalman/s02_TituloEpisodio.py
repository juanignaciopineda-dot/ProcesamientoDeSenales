"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = self.palabra("De Wiener", TXT, 1.5).move_to([0, 0.6, 0])
        t2 = self.palabra("a Kalman", AMBAR, 1.5).move_to([0, -0.7, 0])
        et = etiqueta("Capítulo 12 · Estimación de señales", INK, 0.5).move_to([0, -2.0, 0])
        with self.narrar("b1"):
            # «De Wiener»
            self.en("t1")
            self.pop(t1)
            # «a Kalman»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(et), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
