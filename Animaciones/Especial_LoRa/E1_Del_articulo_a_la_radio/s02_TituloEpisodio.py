"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        t1 = self.palabra("LoRa", AMBAR, 2.0).move_to([0, 0.8, 0])
        t2 = self.palabra("Del artículo a la radio", TXT, 1.1).move_to([0, -0.6, 0])
        et = etiqueta("Especial · Trabajo práctico", INK, 0.5).move_to([0, -1.9, 0])
        with self.narrar("b1"):
            # «LoRa»
            self.en("t1")
            self.pop(t1)
            # «del artículo a la radio»
            self.en("t2")
            self.pop(t2)
            self.play(FadeIn(et), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
