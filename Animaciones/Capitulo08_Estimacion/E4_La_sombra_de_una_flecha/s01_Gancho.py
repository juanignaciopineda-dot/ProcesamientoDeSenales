"""Escena 01 — Gancho: la parábola y la derivada contra una sombra."""
from comun.escena import *
from comun.figuras_c8e4 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        P = ParabolaJ(centro=(0.0, -0.3), ancho=7.0, alto=4.4)
        formula_j = formula("J(h)", "=", "4-8h+5h^2", escala=1.1, colores={0: ERROR}).move_to([0, 3.2, 0])
        tr = ValueTracker(0.0)
        punto = always_redraw(lambda: P.punto(tr.get_value(), ESTIMACION, 0.12))
        tangente = always_redraw(lambda: P.pendiente(tr.get_value(), largo=2.6, color=ROJO))
        F, r = flechas8(origen=(-3.0, -2.2), k=1.9)

        with self.narrar("b1"):
            # «una parábola»
            self.en("parabola")
            self.play(Create(P.eje), Create(P.curva), FadeIn(formula_j), run_time=self.dur(1.0))

            # «y una derivada»
            self.en("derivada")
            self.play(FadeIn(punto), FadeIn(tangente), run_time=self.dur(0.3))
            self.play(tr.animate.set_value(0.8), run_time=self.dur(1.2))
            self.play(FadeIn(P.vertice), run_time=0.25)

            # «Hoy»
            self.en("hoy")
            punto.clear_updaters()
            tangente.clear_updaters()
            self.play(FadeOut(P), FadeOut(punto), FadeOut(tangente), FadeOut(formula_j), run_time=self.dur(0.3))

            # «basta una sombra»
            self.en("sombra")
            self.play(Create(F.presente), Create(F.futuro), FadeIn(r["x"]), FadeIn(r["y"]), run_time=self.dur(0.5))
            self.play(Create(F.sombra), Create(F.error), FadeIn(r["yh"]), FadeIn(r["e"]), Create(F.recto),
                      run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
