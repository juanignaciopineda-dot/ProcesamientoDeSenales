"""Escena 14 — Por qué nos quedamos con el cuadrado; acertar o fallar es decidir (capítulo 9)."""
from comun.escena import *


class TresRespuestas(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        cas = [casilla8(-4.6, 0.0, "Cuadrado", "Media", ESTIMACION), casilla8(0.0, 0.0, "Tamaño", "Mediana", VERDE),
               casilla8(4.6, 0.0, "Acierto", "Moda", CIAN)]
        self.add(*cas)
        decidir = Text("Decidir", color=CIAN, weight=BOLD).scale(0.9).move_to([4.6, 1.5, 0])
        cap9 = Text("Capítulo 9", color=INK, weight=BOLD).scale(0.7).move_to([4.6, -1.5, 0])
        n1 = Text("1", color=INK, weight=BOLD).scale(0.9).move_to([-1.2, 1.3, 0])
        n2 = Text("2", color=INK, weight=BOLD).scale(0.9).move_to([-1.2, 0.0, 0])
        n3 = Text("3", color=INK, weight=BOLD).scale(0.9).move_to([-1.2, -1.3, 0])
        m1 = Text("Castiga lo grande", color=TXT, weight=BOLD).scale(0.85).next_to(n1, RIGHT, buff=0.4)
        m2 = Text("Cuentas limpias", color=TXT, weight=BOLD).scale(0.85).next_to(n2, RIGHT, buff=0.4)
        m3 = Text("Geometría", color=TXT, weight=BOLD).scale(0.85).next_to(n3, RIGHT, buff=0.4)
        tri = VGroup(Polygon([0, 0, 0], [1.0, 0, 0], [1.0, 0.7, 0], color=SENAL, stroke_width=4),
                     Square(side_length=0.18, color=INK, stroke_width=2.5).move_to([0.91, 0.09, 0])
                     ).next_to(m3, RIGHT, buff=0.5)
        ojo_g = ojo(TXT).scale(1.6).move_to([-1.5, 0.2, 0])
        q = Text("?", color=ESTIMACION, weight=BOLD).scale(2.4).move_to([2.0, 0.2, 0])

        with self.narrar("b1"):
            # «La última, acertar o fallar»
            self.en("ultima")
            self.resaltar(cas[2].rect, color=CIAN, escala=1.08, run_time=0.6)

            # «para decidir»
            self.en("decidir")
            self.pop(decidir)

            # «el capítulo siguiente»
            self.en("siguiente")
            self.play(FadeIn(cap9, shift=UP * 0.15), run_time=self.dur(0.5))

            # «nos quedamos con el cuadrado»
            self.en("cuadrado")
            cas[0].rect.set_stroke(VERDE)
            self.play(FadeOut(cas[1]), FadeOut(cas[2]), FadeOut(decidir), FadeOut(cap9), run_time=self.dur(0.5))
            self.play(cas[0].animate.scale(1.15), run_time=self.dur(0.4))

            # «tres motivos»
            self.en("motivos")
            self.play(cas[0].animate.scale(0.8).move_to([-4.8, 0.0, 0]), run_time=self.dur(0.5))
            self.play(LaggedStart(FadeIn(n1), FadeIn(n2), FadeIn(n3), lag_ratio=0.2), run_time=self.dur(0.5))

            # «castiga los errores grandes»
            self.en("castiga")
            self.play(FadeIn(m1, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «las cuentas salen limpias»
            self.en("limpias")
            self.play(FadeIn(m2, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «convierte la estimación en geometría»
            self.en("geometria")
            self.play(FadeIn(m3, shift=RIGHT * 0.2), FadeIn(tri, scale=0.6), run_time=self.dur(0.7))

            # «Pero antes»
            self.en("antes")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)

            # «puedes mirar algo»
            self.en("mirar")
            self.play(FadeIn(ojo_g, scale=0.6), run_time=self.dur(0.5))
            self.pop(q)
        self.wait(1.0)
        self.limpiar()
