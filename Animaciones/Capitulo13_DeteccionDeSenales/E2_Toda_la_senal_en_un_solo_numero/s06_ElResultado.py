"""Escena 06 — El resultado: g = Σ r s contra un umbral γ, y dos comprobaciones numéricas."""
from comun.escena import *


class ElResultado(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.resultado()
        self.comprobacion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resultado(self):
        R = formula(r"\ln p_1", r"+\tfrac{1}{2\sigma^2}\sum\big(", r"2rs", r"-s^2", r"\big)", r"\gtrless", r"\ln p_0",
                    escala=1.4, colores={0: AMBAR, 2: AMBAR, 5: AMBAR, 6: AMBAR}).move_to([0, 2.8, 0])
        por = MathTex(r"\times\,\sigma^2", color=RUIDO).scale(1.5).move_to([5.6, 1.2, 0])
        F = formula("g", "=", r"\sum r[n]\,s[n]", r"\gtrless", r"\gamma", "=", r"\sigma^2\ln\frac{p_0}{p_1}", "+",
                    r"\frac{E}{2}", escala=1.45,
                    colores={0: AMBAR, 4: AMBAR, 2: MEDIDA}).move_to([0, -0.9, 0])
        self.F = F
        us = []

        with self.narrar("b1"):
            # «Queda»
            self.en("queda")
            self.play(*[FadeIn(R[i], shift=UP * 0.1) for i in range(7)], run_time=self.dur(1.0))

            # «logaritmo de pe uno»
            self.en("lnp1")
            u = subrayado(R[0])
            us.append(u)
            self.play(Create(u), run_time=self.dur(0.4))

            # «dos veces recibido por señal»
            self.en("dosrs")
            u = subrayado(R[2], MEDIDA)
            us.append(u)
            self.play(Create(u), run_time=self.dur(0.4))

            # «señal al cuadrado»
            self.en("s2")
            u = subrayado(R[3], SENAL)
            us.append(u)
            self.play(Create(u), run_time=self.dur(0.4))

            # «mayor que logaritmo de pe cero»
            self.en("lnp0")
            u = subrayado(R[6])
            us.append(u)
            self.play(Create(u), run_time=self.dur(0.4))

            # «Multiplicamos por sigma cuadrado»
            self.en("mult")
            self.play(FadeIn(por, shift=LEFT * 0.3), run_time=self.dur(0.6))

            # «y ordenamos»
            self.en("ordena")
            self.play(*[FadeOut(u) for u in us], run_time=0.2)
            self.play(Indicate(R, color=AMBAR, scale_factor=1.04), run_time=self.dur(0.8))

            # «lo único que depende de lo recibido»
            self.en("depende")
            self.play(FadeOut(por), run_time=0.2)
            u = subrayado(R[2], MEDIDA, 6)
            self.play(Create(u), run_time=self.dur(0.5))

            # «la suma de recibido por señal»
            self.en("sumars")
            self.play(FadeIn(F[2], shift=DOWN * 0.2), run_time=self.dur(0.8))

            # «ge»
            self.en("ge")
            self.play(FadeIn(F[0]), FadeIn(F[1]), run_time=self.dur(0.4))
            self.play(Indicate(F[0], color=AMBAR, scale_factor=1.5), run_time=self.dur(0.5))

            # «un umbral, gamma»
            self.en("gamma")
            self.play(FadeOut(u), FadeIn(F[3]), FadeIn(F[4]), FadeIn(F[5]), run_time=self.dur(0.8))

            # «sigma cuadrado por el logaritmo de pe cero entre pe uno»
            self.en("lnpp")
            self.play(FadeIn(F[6], shift=DOWN * 0.2), run_time=self.dur(1.0))

            # «más la energía entre dos»
            self.en("energia")
            self.play(FadeIn(F[7]), FadeIn(F[8], shift=DOWN * 0.2), run_time=self.dur(0.7))
            self.play(Create(SurroundingRectangle(F, color=ESTIMACION, buff=0.2)), run_time=self.dur(0.5))
        self.wait(0.2)

    # ------------------------------------------------------------ b2
    def comprobacion(self):
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
        F = formula("g", "=", r"\sum r[n]\,s[n]", r"\gtrless", r"\gamma", escala=1.2,
                    colores={0: AMBAR, 2: MEDIDA, 4: AMBAR}).move_to([0, 3.3, 0])
        s = Barras((2, 2, 1), centro=(-3.6, 0.9), paso=1.2, unidad=0.5, color=SENAL, ancho=0.8, nums=True)
        r = Barras((3, 1, 2), centro=(-3.6, -1.7), paso=1.2, unidad=0.5, color=MEDIDA, ancho=0.8, nums=True)
        sl = MathTex("s", color=SENAL).scale(1.3).move_to([-6.4, 1.1, 0])
        rl = MathTex("r", color=MEDIDA).scale(1.3).move_to([-6.4, -1.5, 0])
        cuenta = formula("g", "=", r"3\cdot 2", "+", r"1\cdot 2", "+", r"2\cdot 1", escala=1.3,
                         colores={0: AMBAR}).move_to([1.5, 1.3, 0])
        diez = MathTex("=10", color=AMBAR).scale(1.5).next_to(cuenta, RIGHT, buff=0.15)
        umbral = MathTex(r"\gamma=4{,}5", color=AMBAR).scale(1.3).move_to([2.6, -0.2, 0])
        hay = MathTex(r"10>4{,}5", color=TXT).scale(1.3).move_to([2.0, -1.6, 0])
        ok = tilde(VERDE, 0.6).next_to(hay, RIGHT, buff=0.4)
        hay_t = Text("hay señal", color=SENAL, weight=BOLD).scale(0.7).next_to(hay, DOWN, buff=0.3)
        r2 = Barras((0.5, -1, 1), centro=(-3.6, -1.7), paso=1.2, unidad=0.5, color=MEDIDA, ancho=0.8, nums=True)
        cuenta2 = formula("g", "=", "1", "-", "2", "+", "1", escala=1.3, colores={0: AMBAR}).move_to([1.5, 1.3, 0])
        cero = MathTex("=0", color=AMBAR).scale(1.5).next_to(cuenta2, RIGHT, buff=0.15)
        menor = MathTex(r"0<4{,}5", color=TXT).scale(1.3).move_to([2.0, -1.6, 0])
        solo_t = Text("solo ruido", color=RUIDO, weight=BOLD).scale(0.7).next_to(menor, DOWN, buff=0.3)
        parece = Text("cuánto se parece r a s", color=ESTIMACION).scale(0.7).move_to([2.2, -3.5, 0])
        self.add(F)

        with self.narrar("b2"):
            # «Compruébalo con números»
            self.en("comprueba")
            self.play(Create(s.base), *[GrowFromEdge(b, DOWN) for b in s.barras], FadeIn(s.nums), FadeIn(sl),
                      run_time=self.dur(0.8))

            # «tres, uno y dos»
            self.en("r1")
            self.play(Create(r.base), *[GrowFromEdge(b, DOWN) for b in r.barras], FadeIn(r.nums), FadeIn(rl),
                      run_time=self.dur(0.8))

            # «tres por dos, más uno por dos, más dos por uno»
            self.en("cuenta")
            self.play(*[FadeIn(cuenta[i], shift=UP * 0.1) for i in range(7)], run_time=self.dur(1.6))

            # «diez»
            self.en("diez")
            self.pop(diez)

            # «el umbral es cuatro coma cinco»
            self.en("umbral")
            self.play(FadeIn(umbral, shift=UP * 0.1), run_time=self.dur(0.6))

            # «hay señal»
            self.en("hay")
            self.play(FadeIn(hay), FadeIn(ok), run_time=self.dur(0.5))
            self.play(FadeIn(hay_t), run_time=self.dur(0.4))

            # «cero coma cinco, menos uno y uno»
            self.en("r2")
            self.play(FadeOut(hay), FadeOut(ok), FadeOut(hay_t), FadeOut(cuenta), FadeOut(diez), run_time=0.3)
            self.play(ReplacementTransform(VGroup(r.base, *r.barras, r.nums), VGroup(r2.base, *r2.barras, r2.nums)),
                      run_time=self.dur(0.8))

            # «ge vale cero»
            self.en("cero")
            self.play(*[FadeIn(cuenta2[i], shift=UP * 0.1) for i in range(7)], run_time=self.dur(1.0))
            self.pop(cero)

            # «solo ruido»
            self.en("solo")
            self.play(FadeIn(menor), run_time=self.dur(0.4))
            self.play(FadeIn(solo_t), run_time=self.dur(0.4))

            # «cuánto se parece lo recibido a la señal buscada»
            self.en("parece")
            self.play(FadeIn(parece, shift=DOWN * 0.1), run_time=self.dur(0.7))
        self.wait(0.2)
