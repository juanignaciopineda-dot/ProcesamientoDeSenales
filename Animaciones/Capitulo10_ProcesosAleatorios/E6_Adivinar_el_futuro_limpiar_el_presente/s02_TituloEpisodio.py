"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        cap = etiqueta("Capítulo 10 · Procesos aleatorios", INK, 0.6).move_to([0, 1.6, 0])
        a = self.palabra("Adivinar el futuro", TXT, 1.6).move_to([0, 0.3, 0])
        b = self.palabra("limpiar el presente", AMBAR, 1.6).move_to([0, -1.2, 0])
        with self.narrar("b1"):
            self.en("t1")
            self.play(FadeIn(cap), run_time=0.3)
            self.pop(a)
            self.en("t2")
            self.pop(b)
        self.wait(1.0)
        self.limpiar()
