"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = self.palabra("¿Cuál es", TXT, 1.6).move_to([0, 0.9, 0])
        t2 = self.palabra("el mejor filtro?", AMBAR, 1.6).move_to([0, -0.5, 0])
        etq = etiqueta("Capítulo 12 · Estimación de señales", INK, 0.55).move_to([0, -1.9, 0])

        with self.narrar("b1"):
            # «¿Cuál es»
            self.en("t1")
            self.pop(t1)

            # «el mejor filtro?»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(etq), run_time=0.4)
        self.wait(0.6)
        self.limpiar()
