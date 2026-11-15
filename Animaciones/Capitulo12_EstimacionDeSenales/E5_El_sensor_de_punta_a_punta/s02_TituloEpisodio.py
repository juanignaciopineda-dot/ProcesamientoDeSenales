"""Escena 02 — Título del episodio."""
from comun.escena import *


class TituloEpisodio(EscenaCurso):
    ESCENA = "02"

    def construct(self):
        cap = etiqueta("Capítulo 12 · Estimación de señales", INK, 0.6).move_to([0, 2.0, 0])
        a = self.palabra("El sensor,", TXT, 1.4).move_to([0, 0.5, 0])
        b = self.palabra("de punta a punta", AMBAR, 1.4).move_to([0, -0.9, 0])
        term = termometro(alto=1.5).move_to([-5.9, 0.4, 0])
        L = Lienzo(ancho=1.8, alto=0.7, t_rango=(0, 1), v_max=1.0, centro=(-5.9, -1.55))
        cable = ruido_t(L, semilla=11, amp=0.35, color=RUIDO)
        with self.narrar("b1"):
            self.en("t1")
            self.play(FadeIn(cap), FadeIn(term), Create(cable), run_time=0.5)
            self.pop(a)
            self.en("t2")
            self.pop(b)
        self.wait(1.0)
        self.limpiar()
