"""Escena 02 — Título del episodio."""
from comun.escena import *
from comun.figuras_c9e4 import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        P = PlanoRoc9(origen=(-2.2, -2.2), lado=4.4, rotulos=False)
        curva = P.curva(ancho=6).set_stroke(opacity=0.35)
        curva.permitir_encima = True
        t1 = self.palabra("La curva de", TXT, 1.3).move_to([0, 0.7, 0])
        t2 = self.palabra("todos los umbrales", AMBAR, 1.3).move_to([0, -0.5, 0])
        etq = etiqueta("Capítulo 9 · Pruebas de hipótesis", INK, 0.55).move_to([0, -1.75, 0])

        with self.narrar("b1"):
            # «La curva de todos los umbrales»
            self.en("titulo")
            self.play(Create(curva), run_time=1.2)
            self.pop(t1, t2)
            self.play(FadeIn(etq), run_time=0.4)
        self.wait(0.6)
        self.limpiar()
