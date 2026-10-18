"""Escena 04 — Fórmula condicional: la cuenta del dado se vuelve P(A | B)."""
from comun.escena import *


class FormulaCondicional(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.cuenta()
        self.formula_()
        self.condicion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def cuenta(self):
        e = EspacioDado07(centro=(0, 2.3), lado=0.8)
        conta = MathTex(r"\text{Contando: }\tfrac13", color=INK).scale(1.3).move_to([3.9, -2.3, 0])
        fila = VGroup(
            formula(r"P(6\cap \text{par})", "=", r"\tfrac16", escala=1.5, colores={2: AMBAR}),
            formula(r"P(\text{par})", "=", r"\tfrac12", escala=1.5, colores={2: VERDE}),
            formula(r"\dfrac{\tfrac16}{\tfrac12}", "=", r"\tfrac13", escala=1.5, colores={2: AMBAR}),
        )
        for f, y in zip(fila, (0.6, -0.9, -2.6)):
            f.move_to([0, y, 0]).align_to([-5.0, 0, 0], LEFT)
        repetir = CurvedArrow([-5.6, -2.4, 0], [-5.6, 0.4, 0], angle=-PI / 2, color=AMBAR)
        iconos = VGroup(dado_n(3).scale(0.5), moneda().scale(0.55), cruz_hospital().scale(0.6)) \
            .arrange(DOWN, buff=0.35).move_to([5.7, 0.2, 0])
        aros_par = e.aros([2, 4, 6], VERDE, 0.08)
        aro6 = e.aros([6], AMBAR, 0.16)

        with self.narrar("b1"):
            # «con probabilidades»
            self.en("probs")
            self.play(FadeIn(e), FadeIn(conta), run_time=self.dur(0.7))

            # «para poder repetirla»
            self.en("repetir")
            self.play(Create(repetir), run_time=self.dur(0.6))

            # «cualquier situación»
            self.en("cualquiera")
            self.play(LaggedStart(*[FadeIn(i, shift=LEFT * 0.3) for i in iconos], lag_ratio=0.25),
                      run_time=self.dur(0.8))

            # «salga un seis y además sea par»
            self.en("seis_par")
            self.play(Create(aros_par), Create(aro6), FadeIn(fila[0][0]), run_time=self.dur(0.6))

            # «es un sexto»
            self.en("sexto")
            self.play(FadeIn(fila[0][1]), FadeIn(fila[0][2]), run_time=self.dur(0.5))

            # «salga par es un medio»
            self.en("medio")
            self.play(FadeOut(aro6), FadeIn(fila[1]), run_time=self.dur(0.6))

            # «Si dividimos»
            self.en("divide")
            self.play(FadeIn(fila[2][0]), run_time=self.dur(0.7))

            # «sale un tercio»
            self.en("tercio")
            self.play(FadeIn(fila[2][1]), FadeIn(fila[2][2]), run_time=self.dur(0.5))
            self.sfx("exito")

            # «Lo mismo que al contar»
            self.en("igual")
            flecha_ = Arrow(fila[2].get_right() + RIGHT * 0.2, conta.get_left() + LEFT * 0.1, color=VERDE,
                            stroke_width=5, buff=0.05)
            self.play(Create(flecha_), FadeIn(tilde(VERDE, 0.5).next_to(conta, RIGHT, buff=0.25)),
                      run_time=self.dur(0.6))

    # ------------------------------------------------------------ b2
    def formula_(self):
        titulo_ = Text("Probabilidad condicional", color=AMBAR, weight=BOLD).scale(0.95).move_to([0, 3.3, 0])
        f = formula("P", "(", "A", r"\mid", "B", ")", escala=1.5).move_to([-2.9, 1.3, 0])
        dado_ = Text("Dado", color=AMBAR, weight=BOLD).scale(0.8).next_to(f[3], UP, buff=0.5)
        igual = MathTex("=", color=TXT).scale(1.8).move_to([-0.9, 1.3, 0])
        num = MathTex(r"P(A\cap B)", color=TXT).scale(1.6).move_to([1.9, 2.05, 0])
        raya = Line([0.4, 1.3, 0], [3.4, 1.3, 0], color=TXT, stroke_width=3)
        den = MathTex(r"P(B)", color=TXT).scale(1.6).move_to([1.9, 0.6, 0])
        cb = Circle(radius=1.45, color=MEDIDA, stroke_width=4).set_fill(MEDIDA, 0.12).move_to([-1.05, -1.9, 0])
        ca = Circle(radius=1.2, color=ESTIMACION, stroke_width=4).set_fill(ESTIMACION, 0.12).move_to([0.85, -1.9, 0])
        inter = Intersection(ca, cb, color=AMBAR, fill_opacity=0.6, stroke_width=0)
        lb = Text("B", color=MEDIDA, weight=BOLD).scale(0.95).move_to([-1.8, -1.9, 0])
        la = Text("A", color=ESTIMACION, weight=BOLD).scale(0.95).move_to([1.6, -1.9, 0])
        vale1 = Text("Vale 1", color=VERDE, weight=BOLD).scale(0.85).move_to([-4.4, -1.9, 0])

        with self.narrar("b2"):
            # «Eso es la probabilidad condicional»
            self.en("titulo")
            self.corte()
            self.pop(titulo_)

            # «P de A, barra vertical, B»
            self.en("escritura")
            self.play(LaggedStart(*[FadeIn(p) for p in f], lag_ratio=0.2), run_time=self.dur(1.2))

            # «dado B»
            self.en("dado")
            self.play(f[3].animate.set_color(AMBAR), FadeIn(dado_), run_time=self.dur(0.5))

            # «que ocurran A y B a la vez»
            self.en("num")
            self.play(FadeIn(igual), FadeIn(num), run_time=self.dur(0.6))

            # «entre la probabilidad de B»
            self.en("den")
            self.play(Create(raya), FadeIn(den), run_time=self.dur(0.6))

            # «El numerador»
            self.en("numerador")
            self.resaltar(num, color=AMBAR)

            # «dentro del mundo nuevo»
            self.en("dentro")
            self.play(FadeIn(cb), FadeIn(ca), FadeIn(lb), FadeIn(la), FadeIn(inter), run_time=self.dur(0.8))

            # «El denominador mide el mundo nuevo»
            self.en("denominador")
            self.resaltar(den, color=AMBAR)
            self.play(cb.animate.set_stroke(AMBAR, 7), run_time=self.dur(0.4))

            # «vuelva a valer uno entero»
            self.en("uno")
            self.play(cb.animate.set_fill(VERDE, 0.3), FadeIn(vale1), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b3
    def condicion(self):
        pb = MathTex(r"P(B)>0", color=TXT).scale(1.8).move_to([-3.0, 2.7, 0])
        div0 = MathTex(r"\frac10", color=TXT).scale(1.8).move_to([2.8, 2.7, 0])
        x0 = cruz(ERROR, 1.3).move_to(div0)
        f1 = formula("P(A\\mid B)", "=", r"\dfrac{P(A\cap B)}{P(B)}", escala=1.7).move_to([0, 0.5, 0])
        f2 = formula(r"P(A\cap B)", "=", "P(B)", r"\cdot", r"P(A\mid B)", escala=1.7).move_to([0, 0.5, 0])
        rect = SurroundingRectangle(f2, color=AMBAR, buff=0.2, stroke_width=4)
        regla = Text("Regla del producto", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -1.7, 0])
        uno = Text("1", color=AMBAR, weight=BOLD).scale(0.8)
        dos = Text("2", color=VERDE, weight=BOLD).scale(0.8)
        caja_ = RoundedRectangle(corner_radius=0.15, width=6.4, height=1.2, color=INK, stroke_width=3) \
            .move_to([0, -2.6, 0])
        herr = Text("Herramientas", color=INK).scale(0.55).move_to([0, -3.5, 0])

        with self.narrar("b3"):
            # «B tiene que ser posible»
            self.en("posible")
            self.corte()
            self.pop(pb)

            # «no se puede dividir entre cero»
            self.en("cero")
            self.play(FadeIn(div0), run_time=self.dur(0.4))
            self.play(Create(x0), run_time=self.dur(0.4))
            self.sfx("error")
            self.play(FadeIn(f1), run_time=self.dur(0.6))

            # «dándole la vuelta a la fórmula»
            self.en("vuelta")
            self.play(ReplacementTransform(f1, f2), run_time=self.dur(1.2))

            # «otra muy útil»
            self.en("util")
            self.play(Create(rect), run_time=self.dur(0.5))

            # «la probabilidad de B por la de A dado B»
            self.en("producto")
            self.pop(regla)

            # «Primero pasa B»
            self.en("primero")
            uno.next_to(f2[2], DOWN, buff=0.5)
            self.play(f2[2].animate.set_color(AMBAR), FadeIn(uno), run_time=self.dur(0.5))

            # «sabiendo eso, pasa A»
            self.en("despues")
            dos.next_to(f2[4], DOWN, buff=0.5)
            self.play(f2[4].animate.set_color(VERDE), FadeIn(dos), run_time=self.dur(0.5))

            # «La usaremos en un minuto»
            self.en("usaremos")
            f2.add(rect)
            self.play(FadeOut(regla), FadeOut(uno), FadeOut(dos), FadeOut(pb), FadeOut(div0), FadeOut(x0),
                      FadeIn(caja_), FadeIn(herr), f2.animate.scale(0.55).move_to(caja_),
                      run_time=self.dur(0.9))
