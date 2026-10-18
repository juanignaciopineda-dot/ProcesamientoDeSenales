"""Escena 09 — La vuelta: P(+ | enfermo) no es P(enfermo | +)."""
from comun.escena import *


class LaVuelta(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        t99 = Text("99 %", color=VERDE, weight=BOLD).scale(2.2).move_to([0, 3.0, 0])
        f1 = formula(r"P(+\mid \text{enfermo})", "=", r"99\,\%", escala=1.9, colores={2: VERDE}).move_to([0, 1.6, 0])
        lup = lupa().scale_to_fit_height(1.1).move_to([-6.2, -0.9, 0])
        f2 = formula(r"P(\text{enfermo}\mid +)", r"\approx", r"17\,\%", escala=1.9, colores={2: ERROR}).move_to([0, -0.9, 0])
        distinto = MathTex(r"\neq", color=AMBAR).scale(1.6).move_to([0, 0.35, 0])
        g = GrillaMil07(centro=(0, -2.9))
        for p in g.pts[:10]:
            p.set_fill(ROJO, 1)
        tilde_g = tilde(VERDE, 0.6).move_to([4.6, -2.9, 0])
        interr = Text("?", color=ERROR, weight=BOLD).scale(2.0).move_to([4.6, -2.9, 0])
        necesitamos = MathTex(r"P(A\mid B)=\,?", color=AMBAR).scale(1.8).move_to([0, -2.9, 0])
        caja_n = SurroundingRectangle(necesitamos, color=AMBAR, buff=0.25, stroke_width=4)
        giro1 = CurvedArrow([-5.4, 1.4, 0], [-5.4, -0.7, 0], angle=PI / 1.3, color=AMBAR)
        giro2 = CurvedArrow([5.4, -0.7, 0], [5.4, 1.4, 0], angle=PI / 1.3, color=AMBAR)

        with self.narrar("b1"):
            # «El noventa y nueve por ciento»
            self.en("99")
            self.pop(t99)

            # «dar positivo dado que estás enfermo»
            self.en("pos_dado_enf")
            self.play(FadeOut(t99), LaggedStart(*[FadeIn(p) for p in f1], lag_ratio=0.3), run_time=self.dur(1.0))

            # «Lo que tú querías saber»
            self.en("querias")
            self.play(FadeIn(lup, shift=RIGHT * 0.4), run_time=self.dur(0.5))

            # «estar enfermo dado que has dado positivo»
            self.en("enf_dado_pos")
            self.play(LaggedStart(*[FadeIn(p) for p in f2], lag_ratio=0.3), run_time=self.dur(1.0))

            # «Son preguntas distintas»
            self.en("distintas")
            self.play(FadeOut(lup), run_time=0.2)
            self.pop(distinto)

            # «respuestas muy distintas»
            self.en("resp")
            self.resaltar(f1[2], f2[2], color=AMBAR, escala=1.25)

            # «Contar personas funciona»
            self.en("contar")
            self.play(FadeIn(g), FadeIn(tilde_g), run_time=self.dur(0.7))

            # «no siempre tendremos mil personas»
            self.en("no_siempre")
            self.play(FadeOut(tilde_g), FadeIn(interr), run_time=self.dur(0.4))

            # «Necesitamos una fórmula»
            self.en("necesitamos")
            self.play(FadeOut(g), FadeOut(interr), FadeIn(necesitamos), Create(caja_n), run_time=self.dur(0.7))

            # «le dé la vuelta a la pregunta»
            self.en("vuelta")
            self.play(Create(giro1), Create(giro2), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
