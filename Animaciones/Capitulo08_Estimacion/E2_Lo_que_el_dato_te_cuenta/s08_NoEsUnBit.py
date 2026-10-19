"""Escena 08 — Cero coma setenta y nueve no es un bit: estimar no es decidir (anuncia el capítulo 9)."""
from comun.escena import *


class NoEsUnBit(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        y = 0.3
        x0, x1 = -4.5, 4.5
        recta = Line([x0, y, 0], [x1, y, 0], color=INK, stroke_width=4)
        b0 = caja("0", SENAL, ancho=1.4, alto=1.4, scale=1.0).move_to([x0, y, 0])
        b1 = caja("1", SENAL, ancho=1.4, alto=1.4, scale=1.0).move_to([x1, y, 0])
        px = x0 + (x1 - x0) * 0.79
        with self.narrar("b1"):
            # «algo raro»
            self.en("raro")
            self.play(Create(recta), run_time=self.dur(0.4))
            self.pop(b0, b1)

            # «cero coma setenta y nueve»
            self.en("n79")
            punto = Dot([px, y, 0], radius=0.2, color=AMBAR)
            t79 = MathTex(r"0{,}79", color=AMBAR).scale(1.6).next_to(punto, UP, buff=0.5)
            self.pop(punto)
            self.pop(t79)

            # «no es un bit»
            self.en("no_bit")
            x = cruz(ROJO, 1.3).move_to(punto)
            self.play(Create(x), run_time=self.dur(0.4))

            # «Ni cero ni uno»
            self.en("ni")
            self.resaltar(b0, b1, color=AMBAR)

            # «no se busca acertar»
            self.en("acertar")
            diana = VGroup(Circle(radius=0.8, color=INK, stroke_width=5), Circle(radius=0.5, color=INK, stroke_width=5),
                           Circle(radius=0.18, color=ERROR, stroke_width=5).set_fill(ERROR, 0.8)).move_to([-4.5, 2.9, 0])
            tach = tachar(diana)
            self.play(FadeIn(diana), run_time=self.dur(0.3))
            self.play(Create(tach), run_time=self.dur(0.4))

            # «quedarse cerca»
            self.en("cerca")
            fl = Arrow([px + 0.1, y - 1.2, 0], [x1 - 0.2, y - 1.2, 0], color=VERDE, buff=0, stroke_width=6)
            ce = Text("Cerca", color=VERDE, weight=BOLD).scale(0.8).next_to(fl, DOWN, buff=0.15)
            self.play(Create(fl), FadeIn(ce), run_time=self.dur(0.6))

            # «cae entre medias»
            self.en("medias")
            ll = BraceBetweenPoints([x0, y - 1.0, 0], [x1, y - 1.0, 0], DOWN, color=INK)
            tm = Text("Entre medias", color=INK).scale(0.7).next_to(ll, DOWN, buff=0.1)
            self.play(FadeOut(fl), FadeOut(ce), run_time=0.2)
            self.play(GrowFromCenter(ll), FadeIn(tm), run_time=self.dur(0.5))

            # «Si lo que necesitas»
            self.en("necesitas")
            self.play(FadeOut(ll), FadeOut(tm), FadeOut(x), FadeOut(punto), FadeOut(t79), FadeOut(diana),
                      FadeOut(tach), FadeOut(recta), run_time=self.dur(0.4))
            self.play(b0.animate.move_to([-2.4, y, 0]), b1.animate.move_to([2.4, y, 0]), run_time=self.dur(0.5))

            # «elegir entre cero y uno»
            self.en("elegir")
            o = Text("o", color=INK).scale(1.1).move_to([0, y, 0])
            fl2 = Arrow([0, y + 2.2, 0], [2.2, y + 0.9, 0], color=AMBAR, buff=0, stroke_width=7)
            self.play(FadeIn(o), Create(fl2), run_time=self.dur(0.6))

            # «ya es decidir»
            self.en("decidir")
            dec = Text("Decidir ≠ estimar", color=AMBAR, weight=BOLD).scale(1.0).move_to([0, -1.5, 0])
            self.pop(dec)

            # «el capítulo siguiente»
            self.en("cap9")
            c9 = etiqueta("Capítulo 9", INK, 0.8).move_to([0, -2.7, 0])
            self.play(FadeIn(c9, shift=UP * 0.2), run_time=self.dur(0.4))

            # «Guárdate esta pregunta»
            self.en("guarda")
            self.play(FadeOut(fl2), FadeOut(o), FadeOut(b0), FadeOut(b1), FadeOut(dec), run_time=self.dur(0.3))
            can = candado(AMBAR, abierto=False).scale(2.2).move_to([0, 1.3, 0])
            preg = Text("¿Cero o uno?", color=AMBAR, weight=BOLD).scale(1.0).move_to([0, -0.7, 0])
            self.pop(preg)
            self.pop(can)
        self.wait(1.0)
        self.limpiar()
