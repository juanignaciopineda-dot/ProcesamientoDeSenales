"""Escena 16 — 0,79 no es un bit: a veces no hay que estimar sino decidir (capítulo 9)."""
from comun.escena import *
from comun.figuras_c8e5 import *


def casilla_bit(t: str, centro) -> VGroup:
    r = RoundedRectangle(corner_radius=0.15, width=1.4, height=1.4, color=INK, stroke_width=4)
    r.set_fill(INK, 0.1).move_to([centro[0], centro[1], 0])
    g = VGroup(r, Text(t, color=TXT, weight=BOLD).scale(1.0).move_to(r))
    g.r = r
    return g


class DecidirEnVezDeEstimar(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        K = canal8(centro=(0.0, 2.0), ancho=8.0)
        uno = Text("1", color=SENAL, weight=BOLD).scale(0.9).move_to([-5.0, 2.0, 0])
        c79 = Text("0,79", color=AMBAR, weight=BOLD).scale(0.9).move_to([4.8, 2.0, 0])
        R = RectaNum(0, 1, centro=(0.0, -0.2), ancho=8.0, marcas=[0, 1])
        p = Dot(R.p(0.79), radius=0.14, color=AMBAR)
        pl = Text("0,79", color=AMBAR).scale(0.6).next_to(p, UP, buff=0.3)
        c0 = casilla_bit("0", (-4.8, 1.6))
        c1 = casilla_bit("1", (-2.2, 1.6))
        duda = Arrow([-3.5, -0.4, 0], [-4.6, 0.75, 0], buff=0, color=AMBAR, stroke_width=6,
                      max_tip_length_to_length_ratio=0.2)
        duda2 = Arrow([-3.5, -0.4, 0], [-2.4, 0.75, 0], buff=0, color=AMBAR, stroke_width=6,
                       max_tip_length_to_length_ratio=0.2)
        rad = radar13().scale(1.2).move_to([2.4, 1.2, 0])
        av = avion_arriba().scale(0.6).move_to([5.4, 2.6, 0])
        rui = ruido8(centro=(5.4, 2.4), ancho=1.8, amp=0.15, semilla=21, grosor=3)
        est = Text("Estimar", color=INK).scale(0.9).move_to([-3.4, -2.0, 0])
        tache = tachar(est)
        dec = Text("Decidir", color=AMBAR, weight=BOLD).scale(0.95).move_to([1.4, -2.0, 0])
        ok = tilde(VERDE, 0.5).move_to([3.6, -2.0, 0])
        no = cruz(ROJO, 0.5).move_to([4.6, -2.0, 0])
        c9 = Text("Capítulo 9", color=INK).scale(0.6).move_to([1.4, -2.9, 0])

        with self.narrar("b1"):
            # «desde el canal de bits»
            self.en("canal")
            self.play(FadeIn(K), run_time=self.dur(0.5))
            self.play(FadeIn(uno, shift=RIGHT * 0.3), run_time=0.3)

            # «cero coma setenta y nueve»
            self.en("c79")
            self.pop(c79)

            # «no es un bit»
            self.en("nobit")
            self.play(Create(R.base), *[Create(R.ticks[v]) for v in R.ticks], *[FadeIn(R.nums[v]) for v in R.nums],
                      run_time=self.dur(0.5))
            self.play(TransformFromCopy(c79, pl), FadeIn(p, scale=0.4), run_time=self.dur(0.6))

            # «sino elegir»
            self.en("elegir")
            self.corte()
            self.play(FadeIn(c0, scale=0.8), FadeIn(c1, scale=0.8), run_time=self.dur(0.4))

            # «¿Se envió un cero o un uno?»
            self.en("cero_uno")
            self.play(GrowArrow(duda), run_time=0.4)
            self.play(ReplacementTransform(duda, duda2), run_time=0.5)
            self.play(c1.r.animate.set_stroke(AMBAR, 5), run_time=0.3)

            # «¿Hay un avión»
            self.en("avion")
            self.play(FadeIn(rad), FadeIn(av, shift=LEFT * 0.3), run_time=self.dur(0.6))

            # «o solo ruido?»
            self.en("ruido")
            self.play(FadeOut(av), Create(rui), run_time=self.dur(0.6))

            # «Eso ya no es estimar»
            self.en("noest")
            self.play(FadeIn(est), run_time=0.3)
            self.play(Create(tache), run_time=self.dur(0.4))

            # «es decidir»
            self.en("decidir")
            self.pop(dec)

            # «acertar o fallar»
            self.en("acierto")
            self.play(Create(ok), run_time=0.4)
            self.play(Create(no), run_time=self.dur(0.4))

            # «el tema del capítulo siguiente»
            self.en("cap9")
            self.play(FadeIn(c9, shift=UP * 0.1), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
