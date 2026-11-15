"""Escena 07 — El umbral γ sobre la recta de g: la mitad de la energía y cómo lo mueven los aviones raros."""
from comun.escena import *

Y = -0.8                      # altura de la recta de g


class ElUmbral(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.recta_y_energia()
        self.pregunta()
        self.sentido()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def recta_y_energia(self):
        G = formula(r"\gamma", "=", r"\sigma^2\ln\frac{p_0}{p_1}", "+", r"\frac{E}{2}", escala=1.5,
                    colores={0: AMBAR, 4: SENAL}).move_to([0, 3.0, 0])
        recta = recta_g(Y)
        lg = MathTex("g", color=AMBAR).scale(1.2).move_to([gx(11.0) + 0.0, Y + 0.45, 0])
        m0 = marca_g(0, Y, INK, escala=0.7)
        m9 = marca_g(9, Y, SENAL, escala=0.7)
        g0 = MathTex(r"g=0", color=INK).scale(1.1).move_to([gx(0), 0.1, 0])
        s = Barras((2, 2, 1), centro=(gx(9), 1.4), paso=0.75, unidad=0.4, color=SENAL, ancho=0.5)
        Ef = formula("E", "=", r"\sum s^2[n]", "=", r"4+4+1", "=", "9", escala=1.3,
                     colores={0: SENAL, 6: SENAL}).move_to([-2.2, 1.9, 0])
        iguales = MathTex(r"p_0=p_1\;\Rightarrow\;\ln 1=0", color=TXT).scale(1.2).move_to([-1.6, 0.6, 0])
        emedio = MathTex(r"\gamma=E/2", color=AMBAR).scale(1.3).move_to([-1.6, 0.6, 0])
        um = umbral_g(4.5, Y)
        m45 = marca_g(4.5, Y, AMBAR, escala=0.7)
        dos = [DoubleArrow([gx(0) + 0.1, Y - 0.95, 0], [gx(4.5) - 0.1, Y - 0.95, 0], buff=0, color=INK, stroke_width=3,
                           tip_length=0.18),
               DoubleArrow([gx(4.5) + 0.1, Y - 0.95, 0], [gx(9) - 0.1, Y - 0.95, 0], buff=0, color=INK, stroke_width=3,
                           tip_length=0.18)]
        self.um, self.m45 = um, m45

        with self.narrar("b1"):
            # «Miremos el umbral»
            self.en("umbral")
            self.play(*[FadeIn(G[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.2))

            # «una recta»
            self.en("recta")
            self.play(Create(recta), FadeIn(lg), run_time=self.dur(0.8))

            # «Si no recibiéramos nada»
            self.en("nada")
            self.play(FadeIn(m0), run_time=self.dur(0.5))

            # «ge valdría cero»
            self.en("g0")
            self.play(FadeIn(g0, shift=UP * 0.1), run_time=self.dur(0.5))

            # «la señal sin ruido»
            self.en("sinruido")
            self.play(Create(s.base), *[GrowFromEdge(b, DOWN) for b in s.barras], run_time=self.dur(0.7))

            # «la suma de los cuadrados de la señal»
            self.en("cuadrados")
            self.play(FadeIn(Ef[0]), FadeIn(Ef[1]), FadeIn(Ef[2], shift=UP * 0.1), run_time=self.dur(0.9))

            # «la energía»
            self.en("energia")
            self.play(Indicate(Ef[0], color=AMBAR, scale_factor=1.5), run_time=self.dur(0.5))

            # «cuatro más cuatro más uno»
            self.en("cuenta")
            self.play(FadeIn(Ef[3]), FadeIn(Ef[4], shift=UP * 0.1), run_time=self.dur(0.8))

            # «nueve»
            self.en("nueve")
            self.play(FadeIn(Ef[5]), FadeIn(Ef[6]), FadeIn(m9), run_time=self.dur(0.5))

            # «Con probabilidades iguales»
            self.en("iguales")
            self.play(FadeIn(iguales, shift=UP * 0.1), run_time=self.dur(0.8))

            # «el umbral es la energía entre dos»
            self.en("emedio")
            self.play(FadeOut(iguales), FadeIn(emedio), run_time=self.dur(0.6))

            # «cuatro coma cinco»
            self.en("cuatro")
            self.play(Create(um[0]), FadeIn(um[1]), FadeIn(m45), run_time=self.dur(0.6))

            # «a mitad de camino»
            self.en("mitad")
            self.play(*[Create(a) for a in dos], run_time=self.dur(0.6))
        self.Gf, self.recta, self.lg, self.m0, self.m9 = G, recta, lg, m0, m9
        self.limpiar_b1 = [s, Ef, g0, emedio, *dos]
        self.wait(0.2)

    # ------------------------------------------------------------ b2
    def pregunta(self):
        self.play(*[FadeOut(m) for m in self.limpiar_b1], run_time=0.3)
        pregunta = Text("¿sube o baja?", color=AMBAR, weight=BOLD).scale(1.0).move_to([-3.2, 1.9, 0])
        reloj = reloj_arena(TXT).scale(1.1).move_to([-6.0, 1.9, 0])
        p1 = MathTex(r"p_1=0{,}2", color=AMBAR).scale(1.4).move_to([2.8, 1.9, 0])
        izq = Arrow([-0.6, 0.55, 0], [-2.0, 0.55, 0], buff=0, color=INK, stroke_width=5)
        der = Arrow([0.6, 0.55, 0], [2.0, 0.55, 0], buff=0, color=INK, stroke_width=5)
        cuenta = formula(r"\gamma", "=", r"1\cdot", r"\ln\frac{0{,}8}{0{,}2}", "+", r"4{,}5", escala=1.3,
                         colores={0: AMBAR}).move_to([-3.4, 0.55, 0])
        ln4 = MathTex(r"\ln 4=1{,}386", color=AMBAR).scale(1.2).move_to([2.8, 0.55, 0])
        dest = DashedLine([gx(5.886), Y - 0.3, 0], [gx(5.886), Y + 0.9, 0], color=AMBAR, stroke_width=2.5)
        new = Text("5,886", color=AMBAR, weight=BOLD).scale(0.7).next_to(dest, DOWN, buff=0.1)
        new.move_to([gx(5.886), Y - 0.4, 0])

        with self.narrar("b2"):
            # «una pregunta»
            self.en("pregunta")
            self.pop(pregunta)

            # «piénsala un momento»
            self.en("piensa")
            self.play(FadeIn(reloj), run_time=self.dur(0.4))
            self.play(Rotate(reloj, angle=PI, run_time=3.2, rate_func=smooth))

            # «si pe uno baja a cero coma dos»
            self.en("p1")
            self.pop(p1)

            # «¿el umbral sube o baja?»
            self.en("sube")
            self.play(FadeOut(reloj), GrowArrow(izq), GrowArrow(der), run_time=self.dur(0.6))

            # «La cuenta»
            self.en("cuenta")
            self.play(FadeOut(izq), FadeOut(der), *[FadeIn(cuenta[i], shift=UP * 0.1) for i in range(6)],
                      run_time=self.dur(1.2))

            # «el logaritmo de cero coma ocho»
            self.en("ln08")
            u = subrayado(cuenta[3])
            self.play(Create(u), run_time=self.dur(0.4))

            # «es el logaritmo de cuatro»
            self.en("ln4b")
            self.play(FadeIn(ln4, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «uno coma tres ocho seis»
            self.en("ln4")
            self.play(Indicate(ln4, color=AMBAR, scale_factor=1.15), run_time=self.dur(0.6))

            # «El umbral sube a cinco coma ocho ocho seis»
            self.en("sube2")
            self.play(self.um.animate.shift(RIGHT * 1.386), FadeOut(self.m45), FadeIn(new), FadeOut(u),
                      run_time=self.dur(1.0))
        self.nuevo = new
        self.cuenta7 = VGroup(pregunta, p1, cuenta, ln4)
        self.wait(0.2)

    # ------------------------------------------------------------ b3
    def sentido(self):
        raros = VGroup(*[avion(AZUL).scale(0.35).move_to(p) for p in ([-4.5, 1.6, 0], [-2.0, 1.0, 0])])
        frec = VGroup(*[avion(AZUL).scale(0.35).move_to([-5.5 + 1.1 * i, 1.8 - 0.25 * (i % 2), 0]) for i in range(7)])
        mas = Text("más evidencia", color=AMBAR, weight=BOLD).scale(0.65).move_to([gx(8.7), 0.0, 0])
        mas_a = Arrow([gx(6.2), 0.0, 0], [gx(7.0), 0.0, 0], buff=0, color=AMBAR, stroke_width=5)
        neg = MathTex(r"\ln\frac{p_0}{p_1}<0", color=TXT).scale(1.3).move_to([2.6, 1.0, 0])
        menos = Text("menos evidencia", color=AMBAR, weight=BOLD).scale(0.65).move_to([gx(1.6), 0.0, 0])
        ln1 = MathTex(r"\ln 1=0", color=TXT).scale(1.3).move_to([2.6, 1.0, 0])
        ok = tilde(VERDE, 0.6).move_to([gx(5.886), 0.5, 0])

        with self.narrar("b3"):
            # «Tiene sentido»
            self.en("sentido")
            self.play(FadeOut(self.cuenta7), FadeIn(ok), run_time=self.dur(0.5))

            # «los aviones son raros»
            self.en("raros")
            self.play(FadeOut(ok), LaggedStart(*[FadeIn(a, shift=LEFT * 0.3) for a in raros], lag_ratio=0.4),
                      run_time=self.dur(0.9))

            # «más evidencia»
            self.en("evidencia")
            self.play(GrowArrow(mas_a), FadeIn(mas), run_time=self.dur(0.6))

            # «antes de creerle»
            self.en("creerle")
            self.play(Indicate(self.um[1], color=AMBAR, scale_factor=1.5), run_time=self.dur(0.6))

            # «muy frecuentes»
            self.en("frecuentes")
            self.play(FadeOut(raros), FadeOut(mas), FadeOut(mas_a),
                      LaggedStart(*[FadeIn(a, shift=DOWN * 0.2) for a in frec], lag_ratio=0.12), run_time=self.dur(1.0))

            # «el logaritmo sería negativo»
            self.en("neg")
            self.play(FadeIn(neg, shift=UP * 0.1), run_time=self.dur(0.7))

            # «el umbral bajaría»
            self.en("baja")
            self.play(self.um.animate.shift(LEFT * (5.886 - 3.114)), FadeOut(self.nuevo), run_time=self.dur(1.0))

            # «menos evidencia»
            self.en("menos")
            self.play(FadeIn(menos), run_time=self.dur(0.5))

            # «el logaritmo de uno es cero»
            self.en("ln1")
            self.play(FadeOut(neg), FadeOut(frec), FadeOut(menos), FadeIn(ln1, shift=UP * 0.1), run_time=self.dur(0.6))

            # «volvemos al punto medio»
            self.en("medio")
            self.play(self.um.animate.shift(RIGHT * (4.5 - 3.114)), run_time=self.dur(0.9))
        self.wait(0.2)
