"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = self.palabra("¿Cuál de ellas", AMBAR, 1.5).move_to([0, 1.0, 0])
        t2 = self.palabra("mandaron?", TXT, 1.5).move_to([0, -0.2, 0])
        sub = etiqueta("Capítulo 13 · Detección de señales", INK, 0.55).move_to([0, -1.5, 0])
        tres = VGroup(pulso7([1, 1, 0, 0], color=SENAL, paso=0.3, unidad=0.35),
                      pulso7([0, 0, 1, 1], color=AZUL_C7, paso=0.3, unidad=0.35),
                      pulso7([1, -1, 0, 0], color=CIAN, paso=0.3, unidad=0.35)).arrange(RIGHT, buff=0.8)
        tres.move_to([0, -2.7, 0])
        with self.narrar("b1"):
            # «¿Cuál de ellas»
            self.en("t1")
            self.pop(t1)
            self.play(FadeIn(tres), run_time=0.5)
            # «mandaron?»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(sub), run_time=self.dur(0.4))
        self.wait(1.0)
        self.limpiar()
