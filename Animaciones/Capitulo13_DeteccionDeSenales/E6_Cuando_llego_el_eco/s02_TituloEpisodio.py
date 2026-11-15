"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = self.palabra("¿Cuándo", TXT, 1.5).move_to([0, 0.6, 0])
        t2 = self.palabra("llegó el eco?", AMBAR, 1.5).move_to([0, -0.7, 0])
        et = etiqueta("Capítulo 13 · Detección de señales", INK, 0.5).move_to([0, -2.0, 0])
        with self.narrar("b1"):
            # «¿Cuándo»
            self.en("t1")
            self.pop(t1)
            # «llegó el eco?»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(et), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
