"""Escena 07 — La pregunta de la acumulada, con el dado: P(X ≤ x) para varios x."""
from comun.escena import *


class LaPregunta(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.A = AcumDado(centro=(0.5, -0.6))
        self.caras = VGroup(*[dado_n(k).scale(0.5).move_to([-6.2 + 0.78 * (k - 1), 3.3, 0]) for k in range(1, 7)])
        self.cur = None
        self.res = None
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def iluminar(self, k):
        """Enciende en verde las caras 1..k y apaga el resto."""
        return [c.cara.animate.set_stroke(VERDE if i < k else TXT) for i, c in enumerate(self.caras)]

    def resultado(self, txt, color=AMBAR):
        nuevo = Text(txt, color=color, weight=BOLD).scale(0.65).move_to([3.6, 3.2, 0])
        return nuevo

    def bloque1(self):
        A = self.A
        with self.narrar("b1"):
            self.en("curva")                                  # «una curva»
            self.play(Create(A.ax), FadeIn(A.nums_x), FadeIn(A.nums_y), run_time=self.dur(1.0))
            self.en("cualquiera")                             # «cualquier variable aleatoria»
            trio = VGroup(dado().scale(0.45), moneda("1").scale(0.45), termometro(alto=0.8, nivel=0.5)
                          ).arrange(RIGHT, buff=0.4).move_to([-3.9, 3.2, 0])
            self.play(LaggedStart(*[FadeIn(m, scale=0.7) for m in trio], lag_ratio=0.2), run_time=self.dur(0.7))
            self.play(FadeOut(trio), run_time=self.dur(0.3))
            self.en("misma")                                  # «la misma pregunta»
            q = formula("P", "(", "X", r"\le", "x", ")", "=", "?", escala=1.0, colores={0: AMBAR, 7: AMBAR})
            q.move_to([3.2, 3.3, 0])
            self.play(Write(q), run_time=self.dur(1.2))
            self.q = q
            self.en("menor")                                  # «menor o igual»
            self.play(q[3].animate(rate_func=there_and_back).scale(1.8).set_color(VERDE), run_time=self.dur(0.7))
            self.en("dado_num")                               # «un número dado»
            self.cur = A.cursor(3.0)
            self.play(Create(self.cur), run_time=self.dur(0.4))
            self.en("con_dado")                               # «con el dado»
            self.play(FadeIn(self.caras, shift=DOWN * 0.15), run_time=self.dur(0.6))
            self.en("medio")                                  # «cero coma cinco»
            self.play(self.cur.animate.set_x(float(A.p(0.5, 0)[0])), run_time=self.dur(0.7))
            self.en("cero")                                   # «Ninguna: cero»
            self.pto = Dot(A.p(0.5, 0), radius=0.1, color=AMBAR)
            self.res = self.resultado("P(X ≤ 0,5) = 0")
            self.play(FadeOut(q), FadeIn(self.pto, scale=2), FadeIn(self.res), run_time=self.dur(0.6))

    def mover(self, x, y, txt, k=None, dur=0.7):
        A = self.A
        res = self.resultado(txt)
        pto = Dot(A.p(x, y), radius=0.1, color=AMBAR)
        anims = [self.cur.animate.set_x(float(A.p(x, 0)[0])), ReplacementTransform(self.res, res)]
        if k is not None:
            anims += self.iluminar(k)
        self.play(*anims, run_time=self.dur(dur))
        self.play(FadeIn(pto, scale=2), run_time=self.dur(0.3))
        self.res = res
        self.dots.append(pto)

    def bloque2(self):
        A = self.A
        self.dots = [self.pto]
        with self.narrar("b2"):
            self.en("uno")                                    # «uno o menos»
            self.play(self.cur.animate.set_x(float(A.p(1, 0)[0])), run_time=self.dur(0.5))
            self.en("un_sexto")                               # «un sexto»
            pto = Dot(A.p(1, 1 / 6), radius=0.1, color=AMBAR)
            res = self.resultado("P(X ≤ 1) = 1/6")
            self.play(ReplacementTransform(self.res, res), FadeIn(pto, scale=2), *self.iluminar(1),
                      run_time=self.dur(0.6))
            self.res = res
            self.dots.append(pto)
            self.en("dos_medio")                              # «Dos coma cinco o menos»
            self.play(self.cur.animate.set_x(float(A.p(2.5, 0)[0])), run_time=self.dur(0.5))
            self.en("dos_sextos")                             # «dos sextos»
            pto = Dot(A.p(2.5, 2 / 6), radius=0.1, color=AMBAR)
            res = self.resultado("P(X ≤ 2,5) = 2/6")
            self.play(ReplacementTransform(self.res, res), FadeIn(pto, scale=2), *self.iluminar(2),
                      run_time=self.dur(0.6))
            self.res = res
            self.dots.append(pto)
            self.en("seis")                                   # «Seis o menos»
            self.play(self.cur.animate.set_x(float(A.p(6, 0)[0])), run_time=self.dur(0.5))
            self.en("todas")                                  # «Todas las caras»
            pto = Dot(A.p(6, 1), radius=0.1, color=AMBAR)
            res = self.resultado("P(X ≤ 6) = 1")
            self.play(ReplacementTransform(self.res, res), FadeIn(pto, scale=2), *self.iluminar(6),
                      run_time=self.dur(0.6))
            self.res = res
            self.dots.append(pto)
            self.en("diez")                                   # «diez o menos»
            self.play(self.cur.animate.set_x(float(A.p(7.6, 0)[0])), run_time=self.dur(0.6))
            self.en("no_mas")                                 # «ya no hay más caras»
            pto = Dot(A.p(7.6, 1), radius=0.1, color=AMBAR)
            res = self.resultado("P(X ≤ 10) = 1")
            self.play(ReplacementTransform(self.res, res), FadeIn(pto, scale=2), run_time=self.dur(0.6))
            self.res = res
            self.dots.append(pto)
            self.en("dibujamos")                              # «Si dibujamos todas estas respuestas»
            self.play(FadeIn(A.llenos), run_time=self.dur(0.6))
            self.en("escalera")                               # «una escalera»
            self.play(FadeOut(self.cur), *[FadeOut(d) for d in self.dots], FadeOut(self.res),
                      *[c.cara.animate.set_stroke(TXT) for c in self.caras],
                      LaggedStart(*[Create(p) for p in A.peldanos], lag_ratio=0.15),
                      FadeIn(A.huecos), run_time=self.dur(1.6))
            self.en("peldanos")                               # «un sexto en cada cara»
            tags = VGroup(*[Text("+1/6", color=VERDE, weight=BOLD).scale(0.38)
                            .next_to(A.p(k, (k - 0.5) / 6), LEFT, buff=0.12) for k in range(1, 7)])
            self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in tags], lag_ratio=0.12),
                      run_time=self.dur(1.0))
