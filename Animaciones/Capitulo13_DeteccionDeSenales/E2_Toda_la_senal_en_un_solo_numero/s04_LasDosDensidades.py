"""Escena 04 — Las densidades de lo recibido bajo H0 y H1 (campana, producto, exponentes que se suman)."""
from comun.escena import *


class LasDosDensidades(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.h0()
        self.h1()
        self.comparar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def h0(self):
        L = Lienzo(ancho=3.6, alto=1.7, t_rango=(-3.5, 3.5), v_max=1.15, centro=(-4.6, 2.9))
        cam = VGroup(L.base(), campana_curva(L, 0, 1.0, RUIDO, 4))
        gen = formula("c", r"\exp\!\Big(", r"-\frac{x^2}{2\sigma^2}", r"\Big)", escala=1.45,
                      colores={0: INK, 2: RUIDO}).move_to([2.0, 2.9, 0])
        prod = formula("c", r"e^{-\frac{x_0^2}{2\sigma^2}}", r"\cdot", "c", r"e^{-\frac{x_1^2}{2\sigma^2}}",
                       r"\cdot", "c", r"e^{-\frac{x_2^2}{2\sigma^2}}", escala=1.5).move_to([0, 0.8, 0])
        res = formula(r"c^3", r"\exp\!\Big(", r"-\frac{x_0^2+x_1^2+x_2^2}{2\sigma^2}", r"\Big)", escala=1.5,
                      colores={2: AMBAR}).move_to([0, -1.3, 0])
        rc = [SurroundingRectangle(prod[i], color=AMBAR, buff=0.08) for i in (0, 3, 6)]
        re_ = [SurroundingRectangle(prod[i], color=AMBAR, buff=0.08) for i in (1, 4, 7)]
        rdos = SurroundingRectangle(gen[2], color=AMBAR, buff=0.08)
        self.h0_ = MathTex("H_0", color=RUIDO).scale(1.3).move_to([-6.7, 1.6, 0])
        self.dens = formula(r"f(\mathbf{r}\mid H_0)=", r"c^3\exp\!\Big(", r"-\frac{1}{2\sigma^2}\sum_n", r"r^2[n]",
                            r"\Big)", escala=1.0, colores={3: MEDIDA}).move_to([-0.55, 1.6, 0])
        w = Barras((0.6, -0.5, 0.4), centro=(5.7, 1.6), paso=0.7, unidad=0.5, color=RUIDO, ancho=0.45)
        marco = SurroundingRectangle(self.dens, color=RUIDO, buff=0.15)

        with self.narrar("b1"):
            # «la campana centrada en cero»
            self.en("campana")
            self.play(Create(cam), run_time=self.dur(0.8))

            # «una constante por e elevado a menos equis al cuadrado»
            self.en("forma")
            self.play(*[FadeIn(gen[i], shift=UP * 0.1) for i in range(4)], run_time=self.dur(1.6))

            # «entre dos sigma cuadrado»
            self.en("dossigma")
            self.play(Create(rdos), run_time=self.dur(0.4))

            # «Si multiplicamos tres»
            self.en("tres")
            self.play(FadeOut(rdos), *[FadeIn(prod[i], shift=DOWN * 0.1) for i in range(8)], run_time=self.dur(1.2))

            # «las constantes se multiplican»
            self.en("const")
            self.play(*[Create(r) for r in rc], run_time=self.dur(0.5))

            # «los exponentes»
            self.en("expo")
            self.play(*[FadeOut(r) for r in rc], *[Create(r) for r in re_], run_time=self.dur(0.5))

            # «se suman»
            self.en("suman")
            self.play(*[FadeIn(res[i], shift=UP * 0.1) for i in range(4)], run_time=self.dur(1.0))
            self.play(*[FadeOut(r) for r in re_], run_time=0.3)

            # «Bajo la hipótesis cero»
            self.en("h0")
            self.play(FadeOut(cam), FadeOut(gen), FadeOut(prod), FadeOut(res), run_time=self.dur(0.4))
            self.pop(self.h0_)

            # «solo recibimos ruido»
            self.en("solo")
            self.play(Create(w.base), *[GrowFromEdge(b, DOWN) for b in w.barras], run_time=self.dur(0.6))

            # «la densidad de lo recibido»
            self.en("dens")
            self.play(FadeIn(self.dens[0], shift=UP * 0.1), run_time=self.dur(0.5))

            # «la suma de los cuadrados de lo recibido»
            self.en("suma")
            self.play(*[FadeIn(self.dens[i], shift=UP * 0.1) for i in range(1, 5)], run_time=self.dur(1.2))

            # «entre dos sigma cuadrado»
            self.en("finh0")
            self.play(Create(marco), run_time=self.dur(0.5))
        self.wait(0.2)

    # ------------------------------------------------------------ b2
    def h1(self):
        h1 = MathTex("H_1", color=SENAL).scale(1.3).move_to([-6.7, -0.6, 0])
        A = formula(r"f(\mathbf{r}\mid H_1)=", r"c^3\exp\!\Big(", r"-\frac{1}{2\sigma^2}\sum_n\Big(", escala=1.0)
        medio = formula(r"r[n]", "-", r"s[n]", escala=1.0, colores={0: MEDIDA, 2: SENAL})
        C = MathTex(r"\Big)^2\Big)", color=TXT).scale(1.0)
        fila = VGroup(A, medio, C).arrange(RIGHT, buff=0.12).move_to([-0.55, -0.6, 0])
        M0 = MathTex(r"\cdot", color=TXT).scale(1.4).move_to(medio)
        s1 = Barras((2, 2, 1), centro=(5.7, -0.6), paso=0.7, unidad=0.28, color=SENAL, ancho=0.45)
        w1 = Barras((0.6, -0.5, 0.4), centro=(5.7, -0.6), paso=0.7, unidad=0.28, color=RUIDO, ancho=0.45)
        L = Lienzo(ancho=5.4, alto=1.5, t_rango=(-3.5, 5.5), v_max=1.15, centro=(-2.2, -3.0))
        b0 = campana_curva(L, 0, 1.0, RUIDO, 3.5)
        fantasma = campana_curva(L, 0, 1.0, RUIDO, 3.0).set_stroke(opacity=0.35)
        b2 = campana_curva(L, 2.0, 1.0, SENAL, 4)
        base_l = L.base()
        sn = MathTex(r"s[n]", color=SENAL).scale(0.9).move_to(L.p(2.0, 1.75))
        pto = DashedLine(L.p(2.0, 0), L.p(2.0, 1.05), color=SENAL, stroke_width=2.5)
        quitada = Brace(medio, DOWN, color=INK, buff=0.3)
        ruido = formula("w[n]", escala=1.0, colores={0: RUIDO}).next_to(quitada, DOWN, buff=0.15)

        with self.narrar("b2"):
            # «Bajo la hipótesis uno»
            self.en("h1")
            self.pop(h1)
            self.play(FadeIn(A[0]), run_time=self.dur(0.4))

            # «la señal más ruido»
            self.en("smasr")
            self.play(Create(s1.base), *[GrowFromEdge(b, DOWN) for b in s1.barras], run_time=self.dur(0.6))
            self.play(*[GrowFromEdge(b, DOWN) for b in w1.barras], run_time=self.dur(0.5))

            # «una campana igual»
            self.en("igual")
            self.play(Create(base_l), Create(b0), run_time=self.dur(0.8))

            # «centrada en ese de ene»
            self.en("centrada")
            self.add(fantasma)
            self.play(Transform(b0, b2), Create(pto), FadeIn(sn), run_time=self.dur(1.0))

            # «en lugar de en cero»
            self.en("encero")
            self.play(Flash(L.p(0, 0), color=RUIDO, flash_radius=0.4, line_length=0.1, run_time=0.5))

            # «la misma constante y el mismo exponente»
            self.en("misma")
            self.play(FadeIn(A[1], shift=UP * 0.1), FadeIn(A[2], shift=UP * 0.1), FadeIn(C), FadeIn(M0),
                      run_time=self.dur(1.2))

            # «una diferencia»
            self.en("dif")
            self.play(Indicate(M0, color=AMBAR, scale_factor=1.6), run_time=self.dur(0.7))

            # «lo recibido menos la señal»
            self.en("resta")
            self.play(ReplacementTransform(M0, medio), run_time=self.dur(0.8))

            # «lo que queda del ruido»
            self.en("queda")
            self.play(GrowFromCenter(quitada), FadeIn(ruido), run_time=self.dur(0.6))

            # «una vez quitada la señal»
            self.en("quitada")
            self.play(*[b.animate.fade(0.75) for b in s1.barras], run_time=self.dur(0.6))
        self.h1_ = h1
        self.dens1 = A
        self.C = C
        self.medio = medio
        self.wait(0.2)

    # ------------------------------------------------------------ b3
    def comparar(self):
        quedan = [self.dens, self.dens1, self.medio, self.C]
        resto = [m for m in self.mobjects if m is not self.camera.frame and m not in quedan]
        self.play(*[FadeOut(m) for m in resto], run_time=0.3)
        regla = Text("error mínimo", color=ESTIMACION).scale(0.7).move_to([0, 3.0, 0])
        mayor = MathTex(r"\gtrless", color=AMBAR).scale(1.8).move_to([0, 0.5, 0])
        p1 = MathTex("p_1", color=AMBAR).scale(1.2).move_to([-6.8, -0.6, 0])
        p0 = MathTex("p_0", color=AMBAR).scale(1.2).move_to([-6.8, 1.6, 0])
        r1 = Underline(self.dens[2], color=AMBAR, buff=0.1, stroke_width=5)
        r2 = Underline(self.dens1[2], color=AMBAR, buff=0.1, stroke_width=5)
        esc = VGroup(*[Rectangle(width=1.4 + 0.7 * i, height=0.4, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.15)
                       for i in range(4)]).arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to([0, -2.9, 0])

        with self.narrar("b3"):
            # «Esas son las dos densidades»
            self.en("dos")
            self.play(Indicate(self.dens, color=RUIDO, scale_factor=1.03), Indicate(VGroup(self.dens1, self.medio, self.C), color=SENAL, scale_factor=1.03),
                      run_time=self.dur(0.8))

            # «La regla que ya conocemos»
            self.en("regla")
            self.play(FadeIn(regla), run_time=self.dur(0.5))

            # «compararlas»
            self.en("compara")
            self.play(FadeIn(mayor), run_time=self.dur(0.5))

            # «su probabilidad a priori»
            self.en("prior")
            self.play(FadeIn(p1, shift=RIGHT * 0.2), FadeIn(p0, shift=RIGHT * 0.2), run_time=self.dur(0.7))

            # «Y aquí viene lo bonito»
            self.en("bonito")
            self.play(Indicate(self.dens, color=AMBAR, scale_factor=1.04), Indicate(VGroup(self.dens1, self.medio, self.C), color=AMBAR, scale_factor=1.04),
                      run_time=self.dur(0.9))

            # «exponentes con sumas»
            self.en("sumas")
            self.play(Create(r1), Create(r2), run_time=self.dur(0.6))

            # «casi todo lo que hay dentro»
            self.en("casi")
            self.play(Indicate(self.dens[3], color=AMBAR), Indicate(self.medio, color=AMBAR), run_time=self.dur(0.8))

            # «va a desaparecer»
            self.en("desaparecer")
            self.play(self.dens[3].animate.fade(0.7), self.medio.animate.fade(0.7), run_time=self.dur(0.8))

            # «paso a paso»
            self.en("paso")
            self.play(LaggedStart(*[FadeIn(e, shift=RIGHT * 0.2) for e in esc], lag_ratio=0.25), run_time=self.dur(1.0))
        self.wait(0.2)
