"""Escena 05 — Muestras y monedas son la misma información (si F es de fase mínima)."""
from comun.escena import *


class LaMismaInformacion(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        bF = BloqueLTI(r"F", centro=(-3.2, 2.5), ancho=1.3, alto=0.9, largo=1.2, color=AZUL, escala=0.9)
        b1F = BloqueLTI(r"1/F", centro=(3.2, 2.5), ancho=1.3, alto=0.9, largo=1.2, color=AMBAR, escala=0.9)
        l_w1 = MathTex(r"w[n]", color=SENAL).scale(0.7).next_to(bF.p_ent(), LEFT, buff=0.12)
        l_x = MathTex(r"x[n]", color=MEDIDA).scale(0.7).move_to([0, 2.5, 0])
        l_w2 = MathTex(r"w[n]", color=SENAL).scale(0.7).next_to(b1F.p_sal(), RIGHT, buff=0.12)

        pz = plano_c(centro=(-4.2, -0.8), radio=1.2)
        cero = Circle(radius=0.11, color=AMBAR, stroke_width=4).move_to([-4.2 + 0.5, -0.8, 0])
        l_fm = etiqueta("fase mínima", AMBAR, 0.6).move_to([-4.2, -2.6, 0])
        l_causal = etiqueta("causal", VERDE, 0.6).move_to([3.2, 3.45, 0])

        s_x = caja_tex(r"x[k],\ k\le n", MEDIDA, ancho=2.8, alto=1.0, escala=0.75).move_to([0.6, 0.2, 0])
        s_w = caja_tex(r"w[k],\ k\le n", SENAL, ancho=2.8, alto=1.0, escala=0.75).move_to([5.0, 0.2, 0])
        igual = MathTex(r"=", color=VERDE).scale(1.8).move_to([2.8, 0.2, 0])
        distinto = MathTex(r"\neq", color=ERROR).scale(1.8).move_to([2.8, 0.2, 0])
        l_fut = etiqueta("mira al futuro", ERROR, 0.55).move_to([3.2, 1.45, 0])
        a_fut = Arrow([3.2, 0.95, 0], [3.2, 1.2, 0], color=ERROR, buff=0, stroke_width=4,
                      max_tip_length_to_length_ratio=0.5)

        with self.narrar("b1"):
            # «un hecho general»
            self.en("general")
            self.play(FadeIn(bF), FadeIn(b1F), FadeIn(l_w1), FadeIn(l_x), FadeIn(l_w2), run_time=self.dur(0.9))

            # «fase mínima»
            self.en("fm")
            self.play(FadeIn(pz), Create(cero), FadeIn(l_fm), run_time=self.dur(0.7))

            # «su inverso es causal»
            self.en("inverso")
            self.pop(l_causal)

            # «las muestras hasta ahora»
            self.en("muestras")
            self.play(FadeIn(s_x, shift=UP * 0.2), run_time=self.dur(0.6))

            # «las monedas hasta ahora»
            self.en("monedas")
            self.play(FadeIn(s_w, shift=UP * 0.2), run_time=self.dur(0.6))

            # «la misma información»
            self.en("igual")
            self.pop(igual)

            # «no fuese de fase mínima»
            self.en("nofm")
            self.play(cero.animate.shift(RIGHT * 1.45).set_color(ERROR), run_time=self.dur(0.8))

            # «miraría al futuro»
            self.en("futuro")
            self.play(FadeIn(l_fut), GrowArrow(a_fut), run_time=self.dur(0.5))

            # «se rompería»
            self.en("rompe")
            self.sfx("error", gain=-18)
            self.play(ReplacementTransform(igual, distinto), run_time=self.dur(0.5))

        self.wait(1.0)
        self.limpiar()
