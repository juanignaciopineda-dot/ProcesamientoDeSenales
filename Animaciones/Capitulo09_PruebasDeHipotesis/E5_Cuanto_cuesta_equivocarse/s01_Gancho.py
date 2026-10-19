"""Escena 01 — Gancho: el análisis da 1,3; lo más probable es «sano» (56 %) y aun así conviene «enfermo»."""
from comun.escena import *
from comun.figuras_c9e5 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        p_sano = 1 - post_enfermo9(MEDICION)          # 0,56
        with self.narrar("b1"):
            # «Un análisis de sangre»
            self.en("tubo")
            tb = tubo9(alto=2.6).move_to([-3.6, 0.2, 0])
            self.play(FadeIn(tb, shift=UP * 0.4), run_time=self.dur(0.5))

            # «uno coma tres»
            self.en("valor")
            v = Text("1,3", color=MEDIDA, weight=BOLD).scale(1.5).next_to(tb, RIGHT, buff=0.45).shift(UP * 0.4)
            self.pop(v)

            # «Lo más probable»
            self.en("barras")
            B = BarrasSE9(centro=(2.9, -0.3), alto=4.0)
            self.play(FadeIn(B), run_time=self.dur(0.5))

            # «cincuenta y seis por ciento»
            self.en("sano56")
            self.play(*B.crecer(p_sano), run_time=self.dur(0.8))
            self.play(FadeIn(B.vals[0]), FadeIn(B.vals[1]), run_time=self.dur(0.3))

            # «la decisión correcta»
            self.en("decision")
            s = sello("Enfermo", ESTIMACION).scale(1.3).move_to([2.9, 3.0, 0])
            self.play(FadeIn(s, shift=DOWN * 0.3), run_time=self.dur(0.4))

            # «tratarte como enfermo»
            self.en("enfermo")
            self.sfx("impacto", gain=-16)
            self.play(s.animate.scale(0.85).move_to([B.xs[1], 2.45, 0]),
                      run_time=self.dur(0.35), rate_func=rate_functions.ease_in_quad)

            # «¿Cómo puede ser?»
            self.en("pregunta")
            q = Text("?", color=AMBAR, weight=BOLD).scale(2.2).move_to([-0.2, 2.6, 0])
            self.pop(q)
        self.wait(0.6)
        self.limpiar()
