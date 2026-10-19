"""Escena 02 — Título del episodio."""
from comun.escena import *
from comun.figuras_c8e4 import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = self.palabra("La sombra", TXT, 1.6).move_to([0, 0.9, 0])
        t2 = self.palabra("de una flecha", AMBAR, 1.6).move_to([0, -0.5, 0])
        etq = etiqueta("Capítulo 8 · Estimación", INK, 0.55).move_to([0, -1.9, 0])

        with self.narrar("b1"):
            # «La sombra»
            self.en("t1")
            self.pop(t1)

            # «de una flecha.»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(etq), run_time=0.4)
        self.wait(0.6)
        self.limpiar()
