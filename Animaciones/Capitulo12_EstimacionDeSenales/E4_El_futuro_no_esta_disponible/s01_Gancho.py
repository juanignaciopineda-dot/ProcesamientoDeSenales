"""Escena 01 — Gancho: el mejor filtro, cortado, deja de ser el mejor."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        h = Tallos(H_NO_CAUSAL, centro=(0, -0.9), paso=1.0, unidad=3.0, color=AMBAR, k0=-2, indices=True)
        cor = corona().scale(1.3).move_to([0, 1.8, 0])
        tj = tijeras().scale(0.9).move_to([-3.8, 0.9, 0])
        tj.permitir_encima = True
        rel = reloj().scale(1.2).move_to([-5.7, 2.5, 0])
        fut = etiqueta("futuro", ERROR, 0.55).move_to([-5.7, 1.6, 0])
        x = cruz(ROJO, 1.3).move_to(cor)
        lp = lupa(TXT).scale(1.5).move_to([4.0, 0.8, 0])
        lp.permitir_encima = True
        arr = self.palabra("blanquear primero", AMBAR, 0.8).move_to([0, -3.3, 0])
        with self.narrar("b1"):
            # «el mejor filtro posible»
            self.en("mejor")
            self.play(FadeIn(h), run_time=self.dur(0.8))
            self.play(FadeIn(cor, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «Le cortas la parte»
            self.en("cortas")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))

            # «mira al futuro»
            self.en("futuro")
            self.play(FadeIn(rel), FadeIn(fut), tj.animate.move_to([-0.5, 0.4, 0]), run_time=self.dur(0.7))
            self.sfx("tick")
            self.play(FadeOut(h.palito(0), h.palito(1), shift=DOWN * 0.4), run_time=self.dur(0.5))

            # «deja de ser el mejor»
            self.en("deja")
            self.play(Create(x), run_time=0.3)
            self.sfx("error")

            # «Hoy vemos por qué»
            self.en("porque")
            self.play(FadeIn(lp, scale=0.6), run_time=self.dur(0.4))
            self.play(lp.animate.move_to([1.2, 0.5, 0]), run_time=self.dur(1.0))

            # «cómo se arregla»
            self.en("arregla")
            self.pop(arr)

        self.wait(1.0)
        self.limpiar()
