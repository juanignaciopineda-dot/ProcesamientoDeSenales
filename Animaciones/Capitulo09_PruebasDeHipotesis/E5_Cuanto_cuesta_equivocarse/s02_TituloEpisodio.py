"""Escena 02 — Título del episodio."""
from comun.escena import *
from comun.figuras_c9e5 import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        b = Balanza(centro=(0.0, 0.6), semi=3.0).set_opacity(0.3)
        b.permitir_encima = True
        t1 = self.palabra("¿Cuánto cuesta", TXT, 1.3).move_to([0, 0.7, 0])
        t2 = self.palabra("equivocarse?", AMBAR, 1.3).move_to([0, -0.5, 0])
        etq = etiqueta("Capítulo 9 · Pruebas de hipótesis", INK, 0.55).move_to([0, -1.75, 0])

        with self.narrar("b1"):
            # «¿Cuánto cuesta equivocarse?»
            self.en("titulo")
            self.play(FadeIn(b), run_time=0.5)
            self.pop(t1, t2)
            self.play(FadeIn(etq), *b.inclinar("der", ang=0.18), run_time=0.6)
        self.wait(0.6)
        self.limpiar()
