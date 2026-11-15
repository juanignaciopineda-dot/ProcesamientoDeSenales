"""Escena 01 — Gancho: infinitas ecuaciones, infinitas incógnitas, una sola división."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        ecs = columna_ecuaciones(centro=(-3.3, 0.0), escala=0.78, paso=0.9)
        inc = columna_incognitas(centro=(4.8, 0.0), escala=1.05, paso=0.9)
        frac = fraccion(MathTex("S_{yx}", color=TXT), MathTex("S_{xx}", color=TXT)).scale(1.7).move_to(ORIGIN)
        preg = Text("¿cómo?", color=AMBAR, weight=BOLD).scale(0.95).move_to([0, -2.4, 0])
        with self.narrar("b1"):
            self.en("ecs")                                   # «infinitas ecuaciones»
            self.play(LaggedStart(*[FadeIn(f, shift=RIGHT * 0.3) for f in ecs], lag_ratio=0.18),
                      run_time=self.dur(1.2))
            self.en("incog")                                 # «infinitas incógnitas»
            self.play(LaggedStart(*[FadeIn(f, shift=LEFT * 0.3) for f in inc], lag_ratio=0.18),
                      run_time=self.dur(1.2))
            self.en("division")                              # «una sola división»
            self.play(FadeOut(ecs, shift=RIGHT), FadeOut(inc, shift=LEFT), run_time=0.5)
            self.pop(frac)
            self.en("como")                                  # «Hoy vemos cómo»
            self.pop(preg)
        self.wait(1.0)
        self.limpiar()
