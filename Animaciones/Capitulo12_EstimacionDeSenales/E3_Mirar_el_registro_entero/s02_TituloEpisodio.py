"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        cap = etiqueta("Capítulo 12 · Estimación de señales", INK, 0.6).move_to([0, 1.6, 0])
        a = self.palabra("Mirar", TXT, 1.6).move_to([0, 0.3, 0])
        b = self.palabra("el registro entero", AMBAR, 1.6).move_to([0, -1.2, 0])
        with self.narrar("b1"):
            self.en("t1")
            self.add(cap)
            self.pop(a)
            self.en("t2")
            self.pop(b)
        self.wait(1.0)
        self.limpiar()
