"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        cap = etiqueta("Capítulo 7 · Modelos probabilísticos", INK, 0.6).move_to([0, 2.0, 0])
        a = self.palabra("Dos números", TXT, 1.5).move_to([0, 0.5, 0])
        b = self.palabra("Para resumirlo todo", AMBAR, 1.4).move_to([0, -0.9, 0])
        with self.narrar("b1"):
            self.en("t1")
            self.play(FadeIn(cap), run_time=0.3)
            self.pop(a)
            self.en("t2")
            self.pop(b)
        self.wait(1.0)
        self.limpiar()
