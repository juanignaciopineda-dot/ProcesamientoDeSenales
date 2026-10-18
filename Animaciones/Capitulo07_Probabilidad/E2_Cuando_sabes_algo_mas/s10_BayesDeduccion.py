"""Escena 10 — Bayes deducción: la regla sale de escribir P(A y B) de dos maneras."""
from comun.escena import *


class BayesDeduccion(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.deduccion()
        self.regla()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def deduccion(self):
        estante = formula(r"P(A\cap B)", "=", "P(B)", r"\cdot", r"P(A\mid B)", escala=1.0).move_to([0, 3.2, 0])
        caja_e = SurroundingRectangle(estante, color=INK, buff=0.15, stroke_width=3)
        r1 = formula(r"P(A\cap B)", "=", r"P(A\mid B)", r"\cdot", "P(B)", escala=1.6,
                     colores={2: MEDIDA, 4: MEDIDA}).move_to([0, 1.5, 0])
        r2 = formula(r"P(A\cap B)", "=", r"P(B\mid A)", r"\cdot", "P(A)", escala=1.6,
                     colores={2: ESTIMACION, 4: ESTIMACION}).move_to([0, 0.1, 0])
        for r in (r1, r2):
            r.align_to([-4.2, 0, 0], LEFT)
        r2.shift(RIGHT * (r1[0].get_left()[0] - r2[0].get_left()[0]))
        igual_ = MathTex("=", color=AMBAR).scale(1.8).move_to([-5.0, 0.8, 0])
        llave = Brace(VGroup(r1[0], r2[0]), LEFT, color=AMBAR, buff=0.15)
        r3 = formula(r"P(A\mid B)\,P(B)", "=", r"P(B\mid A)\,P(A)", escala=1.6).move_to([0, -1.35, 0])
        r4 = formula(r"P(A\mid B)", "=", r"\dfrac{P(B\mid A)\,P(A)}{P(B)}", escala=1.5, colores={0: AMBAR}).move_to([0, -3.05, 0])
        self.r4_pos = r4.get_center()

        with self.narrar("b1"):
            # «sale de algo que ya tenemos»
            self.en("ya_tenemos")
            self.play(FadeIn(estante), Create(caja_e), run_time=self.dur(0.6))

            # «ocurran A y B»
            self.en("ayb")
            self.play(FadeIn(r1[0]), FadeIn(r2[0]), run_time=self.dur(0.5))

            # «de dos maneras»
            self.en("dos")
            self.play(FadeIn(r1[1]), FadeIn(r2[1]), run_time=self.dur(0.4))

            # «primero B y después A dado B»
            self.en("primera")
            self.play(*[FadeIn(r1[i]) for i in (2, 3, 4)], run_time=self.dur(0.7))

            # «primero A y después B dado A»
            self.en("segunda")
            self.play(*[FadeIn(r2[i]) for i in (2, 3, 4)], run_time=self.dur(0.7))

            # «Las dos dan lo mismo»
            self.en("lo_mismo")
            self.play(FadeIn(igual_), run_time=self.dur(0.4))

            # «el mismo suceso»
            self.en("mismo")
            self.play(Create(llave), run_time=self.dur(0.6))

            # «igualamos las dos expresiones»
            self.en("igualar")
            self.play(FadeIn(r3, shift=UP * 0.3), run_time=self.dur(0.7))

            # «despejamos la probabilidad de A dado B»
            self.en("despejar")
            self.play(FadeIn(r4, shift=UP * 0.3), run_time=self.dur(0.8))

    # ------------------------------------------------------------ b2
    def regla(self):
        izq = MathTex(r"P(A\mid B)", color=AMBAR).scale(1.3).move_to([-4.7, 0.9, 0])
        eq = MathTex("=", color=TXT).scale(1.5).move_to([-2.7, 0.9, 0])
        n_a = MathTex(r"P(B\mid A)", color=ESTIMACION).scale(1.3).move_to([-0.3, 1.55, 0])
        punto = MathTex(r"\cdot", color=TXT).scale(1.5).move_to([1.6, 1.55, 0])
        n_b = MathTex(r"P(A)", color=SENAL).scale(1.3).move_to([2.8, 1.55, 0])
        raya = Line([-2.1, 0.9, 0], [4.1, 0.9, 0], color=TXT, stroke_width=4)
        den = MathTex(r"P(B)", color=TXT).scale(1.3).move_to([1.0, 0.3, 0])
        bayes = Text("Bayes", color=AMBAR, weight=BOLD).scale(1.5).move_to([0, 3.2, 0])
        marco = SurroundingRectangle(VGroup(izq, eq, n_a, n_b, raya, den), color=AMBAR, buff=0.25, stroke_width=4)

        # leyenda: expresión, dos puntos y nombre, una fila por pieza
        filas = [(r"P(A)", SENAL, "A priori", "Lo que creías antes de mirar", n_b, -1.2),
                 (r"P(B\mid A)", ESTIMACION, "Verosimilitud", "Cuánto encaja lo visto con A", n_a, -2.2),
                 (r"P(A\mid B)", AMBAR, "A posteriori", "Lo que crees después de mirar", izq, -3.2)]
        expr, dos, nom, cap = [], [], [], []
        for tex, col, nombre, texto, _, y in filas:
            e = MathTex(tex, color=col).scale(1.2)
            e.move_to([-4.3, y, 0]).align_to([-3.4, 0, 0], RIGHT)
            d = MathTex(":", color=TXT).scale(1.2).move_to([-3.1, y, 0])
            n = Text(nombre, color=col, weight=BOLD).scale(0.85).move_to([-2.8, y, 0]).align_to([-2.8, 0, 0], LEFT)
            c = Text(texto, color=INK).scale(0.65).move_to([1.0, y, 0]).align_to([1.0, 0, 0], LEFT)
            expr.append(e), dos.append(d), nom.append(n), cap.append(c)

        with self.narrar("b2"):
            # «Queda así»
            self.en("queda")
            self.corte()
            self.play(FadeIn(izq), FadeIn(eq), run_time=self.dur(0.5))

            # «la probabilidad de B dado A, por la probabilidad de A»
            self.en("numerador")
            self.play(FadeIn(n_a), FadeIn(punto), FadeIn(n_b), run_time=self.dur(0.8))

            # «dividida entre la probabilidad de B»
            self.en("denominador")
            self.play(Create(raya), FadeIn(den), run_time=self.dur(0.6))

            # «la regla de Bayes»
            self.en("bayes")
            self.pop(bayes)
            self.play(Create(marco), run_time=self.dur(0.5))

            # «Cada pieza tiene nombre»
            self.en("nombres")
            self.play(LaggedStart(*[AnimationGroup(FadeIn(e, shift=RIGHT * 0.3), FadeIn(d))
                                    for e, d in zip(expr, dos)], lag_ratio=0.3), run_time=self.dur(1.0))

            # «La probabilidad de A sola»
            self.en("a_sola")
            self.resaltar(n_b, color=SENAL)

            # «a priori»
            self.en("priori")
            self.pop(nom[0])

            # «lo que creías antes de mirar»
            self.en("antes")
            self.play(FadeIn(cap[0], shift=RIGHT * 0.3), run_time=self.dur(0.5))

            # «la verosimilitud»
            self.en("verosimilitud")
            self.resaltar(n_a, color=ESTIMACION)
            self.pop(nom[1])

            # «lo compatible que es lo que viste»
            self.en("compatible")
            self.play(FadeIn(cap[1], shift=RIGHT * 0.3), run_time=self.dur(0.5))

            # «Y el resultado»
            self.en("resultado")
            self.resaltar(izq, color=AMBAR)

            # «a posteriori»
            self.en("posteriori")
            self.pop(nom[2])

            # «lo que crees después de mirar»
            self.en("despues")
            self.play(FadeIn(cap[2], shift=RIGHT * 0.3), run_time=self.dur(0.5))
