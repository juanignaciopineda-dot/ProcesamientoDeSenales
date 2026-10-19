"""Escena 02 — Título del episodio."""
from comun.escena import *
from comun.figuras_c9e1 import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = self.palabra("¿Un cero", TXT, 1.6).move_to([0, 0.9, 0])
        t2 = self.palabra("o un uno?", AMBAR, 1.6).move_to([0, -0.5, 0])
        etq = etiqueta("Capítulo 9 · Pruebas de hipótesis", INK, 0.55).move_to([0, -1.9, 0])

        with self.narrar("b1"):
            # «¿Un cero»
            self.en("t1")
            self.pop(t1)

            # «o un uno?»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(etq), run_time=0.4)
        self.wait(0.6)
        self.limpiar()
