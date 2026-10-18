"""Escena 12 — Markov: con los sueldos, una media pequeña limita cuántos pueden cobrar mucho."""
from comun.escena import *


class Markov(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.sueldos()
        self.desigualdad()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def sueldos(self):
        fila = fila_personas7(10, centro=(0, 0.6), paso=1.15, escala=1.3)
        media = Text("Media: 1.000 €", color=AMBAR, weight=BOLD).scale(0.8).move_to([-3.6, 3.0, 0])
        neg = Text("Sueldo ≥ 0", color=TXT).scale(0.8).move_to([3.6, 3.0, 0])
        frac = Text("¿Qué fracción?", color=INK).scale(0.8).move_to([-3.8, -1.8, 0])
        diezmil = Text("≥ 10.000 €", color=ERROR, weight=BOLD).scale(0.8).move_to([3.6, -1.8, 0])
        billetes = VGroup(*[Text("10.000 €", color=ERROR).scale(0.45).next_to(fila.personas[i], UP, buff=0.15)
                            for i in (0, 1)])
        dos = Text("Media ≥ 2.000 €", color=ERROR, weight=BOLD).scale(0.8).move_to([0, -3.1, 0])
        diez = Text("≤ 10 %", color=VERDE, weight=BOLD).scale(1.0).move_to([0, -3.1, 0])
        with self.narrar("b1"):
            # «pregunta de sueldos»
            self.en("sueldos")
            self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in fila.personas], lag_ratio=0.08),
                      run_time=self.dur(1.2))
            # «el sueldo medio es de mil euros»
            self.en("media")
            self.pop(media)
            # «nadie cobra un sueldo negativo»
            self.en("negativo")
            self.play(FadeIn(neg, shift=DOWN * 0.15), run_time=self.dur(0.7))
            # «¿Qué fracción de la plantilla»
            self.en("fraccion")
            self.play(FadeIn(frac), run_time=self.dur(0.6))
            # «diez mil euros o más»
            self.en("diezmil")
            self.pop(diezmil)
            # «si el veinte por ciento»
            self.en("veinte")
            self.play(*[fila.personas[i].animate.set_color(ERROR) for i in (0, 1)], run_time=self.dur(0.7))
            # «cobrara diez mil»
            self.en("cobrara")
            self.play(FadeIn(billetes, shift=DOWN * 0.15), run_time=self.dur(0.7))
            # «la media fuera de dos mil»
            self.en("dosmil")
            self.play(FadeIn(dos, shift=UP * 0.15), run_time=self.dur(0.8))
            tach = tachar(dos)
            self.play(Create(tach), run_time=0.4)
            self.sfx("error")
            # «Como mucho»
            self.en("mucho")
            self.play(fila.personas[1].animate.set_color(AZUL), FadeOut(billetes[1]), run_time=self.dur(0.6))
            # «un diez por ciento»
            self.en("diez")
            self.play(FadeOut(dos), FadeOut(tach), run_time=0.2)
            self.pop(diez)

    # ---------------------------------------------------------------- b2
    def desigualdad(self):
        F = MathTex(r"P(Y\ge a)", r"\le", r"\frac{E[Y]}{a}", color=TXT).scale(1.6).move_to([0, 0.6, 0])
        F[2].set_color(AMBAR)
        pal = self.palabra("Markov", AMBAR, 1.1).move_to([-4.8, 3.3, 0])
        pos = MathTex(r"Y\ge 0", color=VERDE).scale(1.3).move_to([4.2, 3.3, 0])
        recta = Line([-3.0, -1.6, 0], [4.0, -1.6, 0], color=INK, stroke_width=3)
        cero = Text("0", color=INK).scale(0.5).move_to([-3.0, -2.0, 0])
        vedado = Rectangle(width=1.5, height=0.5, stroke_width=0).set_fill(ERROR, 0.3).move_to([-3.75, -1.45, 0])
        barra = Rectangle(width=4.0, height=0.45, stroke_width=0).set_fill(AMBAR, 0.6).move_to([0.0, -3.0, 0])
        barra.align_to([-2.0, 0, 0], LEFT)
        pbarra = Text("Probabilidad", color=INK).scale(0.5).next_to(barra, LEFT, buff=0.3)
        with self.narrar("b2"):
            # «la desigualdad de Markov»
            self.en("markov")
            self.corte()
            self.pop(pal)
            # «nunca es negativa»
            self.en("nunca_neg")
            self.play(FadeIn(pos, shift=DOWN * 0.15), run_time=self.dur(0.7))
            # «la probabilidad de que supere un valor a»
            self.en("supere")
            self.play(FadeIn(F[0], shift=DOWN * 0.15), run_time=self.dur(1.0))
            # «como mucho»
            self.en("como_mucho")
            self.play(FadeIn(F[1], shift=DOWN * 0.15), run_time=self.dur(0.5))
            # «su media dividida entre a»
            self.en("cociente")
            self.play(FadeIn(F[2], shift=DOWN * 0.15), run_time=self.dur(0.8))
            # «no puede ser negativa»
            self.en("no_puede")
            self.play(Create(recta), FadeIn(cero), FadeIn(vedado), run_time=self.dur(0.9))
            # «una media pequeña»
            self.en("pequena")
            self.play(F[2].animate.scale(0.7), run_time=self.dur(0.7))
            # «valores grandes muy a menudo»
            self.en("a_menudo")
            self.play(FadeIn(pbarra), FadeIn(barra), run_time=0.4)
            self.play(barra.animate.stretch_to_fit_width(0.8, about_edge=LEFT), run_time=self.dur(0.9))
