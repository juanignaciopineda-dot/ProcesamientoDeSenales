"""Escena 02 — Título del episodio."""
from comun.escena import *
from comun.figuras_c9e6 import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        P = PlanoRoc9(origen=(-2.2, -2.2), lado=4.4, rotulos=False)
        esc = Escalera6(P).todo(ancho=6).set_stroke(opacity=0.3)
        esc.permitir_encima = True
        t1 = self.palabra("Decidir", TXT, 1.4).move_to([0, 0.75, 0])
        t2 = self.palabra("con datos de verdad", AMBAR, 1.2).move_to([0, -0.45, 0])
        etq = etiqueta("Capítulo 9 · Pruebas de hipótesis", INK, 0.55).move_to([0, -1.7, 0])

        self.add(esc)
        with self.narrar("b1"):
            # «Decidir»
            self.en("t1")
            self.pop(t1, run_time=0.35)
            # «con datos de verdad»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(etq), run_time=0.35)
        self.wait(0.6)
        self.limpiar()
