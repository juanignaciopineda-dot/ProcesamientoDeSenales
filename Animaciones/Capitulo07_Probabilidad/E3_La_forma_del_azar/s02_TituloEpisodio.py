"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        with self.narrar("b1"):
            self.en("t1")                                     # «La forma»
            a = self.palabra("La forma", TXT, 1.9).move_to([0, 0.5, 0])
            self.pop(a)
            self.en("t2")                                     # «del azar»
            b = self.palabra("Del azar", AMBAR, 1.9).next_to(a, DOWN, buff=0.3)
            c = etiqueta("Capítulo 7 · Modelos probabilísticos", INK, 0.6).next_to(b, DOWN, buff=0.55)
            self.pop(b)
            self.play(FadeIn(c), run_time=self.dur(0.5))
        self.wait(0.6)
        self.limpiar()
