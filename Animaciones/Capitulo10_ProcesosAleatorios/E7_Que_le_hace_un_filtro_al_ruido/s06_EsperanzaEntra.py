"""Escena 06 — La media de la salida: la esperanza entra en la suma, μ_y = H(0) μ_x."""
from comun.escena import *


class EsperanzaEntra(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.planteo()
        self.deduccion()

    # ------------------------------------------------------------------ b1
    def planteo(self):
        bl = BloqueLTI(r"h", centro=(0, 2.3), ancho=1.8, alto=1.2, largo=2.0)
        Le = Lienzo(ancho=2.6, alto=1.5, t_rango=(0, 1), v_max=1.5, centro=(-4.6, 2.3))
        Ls = Lienzo(ancho=2.6, alto=1.5, t_rango=(0, 1), v_max=1.5, centro=(4.6, 2.3))
        t = np.linspace(0, 1, 120)
        ce = Le.curva(t, 0.55 * serie(11, 120, 0.9), SENAL, 3.5)
        cs = Ls.curva(t, 0.55 * serie(12, 120, 0.96), MEDIDA, 3.5)
        pe = pila_de_curvas(Le, 6, semilla=3, a=0.9, puntos=120, color=SENAL, opacidad=0.6, ancho=2.4, escala=0.5)
        ps = pila_de_curvas(Ls, 6, semilla=4, a=0.96, puntos=120, color=MEDIDA, opacidad=0.6, ancho=2.4, escala=0.5)
        f = formula(r"E[y[n]]", "=", r"E\big[", r"\sum_k", r"h[k]", r"x[n-k]", r"\big]", escala=1.35).move_to([0, 0.5, 0])
        lin = self.palabra("linealidad", AMBAR, 1.0).move_to([-4.6, -1.7, 0])
        r1 = formula(r"E[a+b]", "=", r"E[a]+E[b]", escala=1.15).move_to([2.0, -1.3, 0])
        r2 = formula(r"E[c\,a]", "=", r"c\,E[a]", escala=1.15).move_to([2.0, -2.6, 0])

        with self.narrar("b1"):
            # «una realización»
            self.en("realiz")
            self.play(FadeIn(bl), Create(ce), run_time=self.dur(0.8))

            # «otra señal aleatoria»
            self.en("sale")
            self.play(Create(cs), run_time=self.dur(0.8))

            # «un proceso nuevo»
            self.en("nuevo")
            self.play(ReplacementTransform(ce, pe), ReplacementTransform(cs, ps), run_time=self.dur(1.0))

            # «su media»
            self.en("media")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.5))

            # «La media de la salida»
            self.en("media_y")
            self.resaltar(f[0], color=AMBAR, escala=1.15)

            # «una suma de entradas pesadas»
            self.en("suma")
            self.play(FadeIn(f[2:]), run_time=self.dur(0.9))

            # «pesadas por hache»
            self.en("pesadas")
            self.play(f[4].animate(rate_func=there_and_back).scale(1.3).set_color(AMBAR), run_time=0.5)

            # «la esperanza es lineal»
            self.en("lineal")
            self.pop(lin)

            # «la esperanza de una suma»
            self.en("esp_suma")
            self.play(FadeIn(r1), run_time=self.dur(0.8))

            # «los números que multiplican»
            self.en("numeros")
            self.play(FadeIn(r2), run_time=self.dur(0.8))

            # «salen fuera»
            self.en("fuera")
            self.play(r2[2][0].animate(rate_func=there_and_back).scale(1.4).set_color(AMBAR), run_time=0.6)
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def deduccion(self):
        l1 = formula(r"E[y[n]]", "=", r"E\big[\sum_k h[k]\,x[n-k]\big]", escala=1.35).move_to([0, 3.15, 0])
        l2 = formula("=", r"\sum_k", r"h[k]", r"E[x[n-k]]", escala=1.35).move_to([0, 1.65, 0])
        l3 = formula("=", r"\sum_k", r"h[k]", r"\mu_x", escala=1.35).move_to([0, 0.15, 0])
        l4 = formula("=", r"\mu_x", r"\sum_k h[k]", escala=1.35).move_to([0, -1.35, 0])
        for l in (l2, l3, l4):
            l.align_to(l1[1], LEFT)
        sello_e = sello("estacionaria", VERDE).scale(0.8).move_to([5.0, 0.1, 0])
        marco = Underline(l4[2], color=AMBAR, buff=0.1, stroke_width=5)
        etq_gan = formula("H(0)", escala=1.0, colores={0: AMBAR}).move_to([4.2, -1.35, 0])
        etq_h = etiqueta("ganancia en continua", AMBAR, 0.6).next_to(etq_gan, DOWN, buff=0.25)
        res = formula(r"\mu_y", "=", "H(0)", r"\,\mu_x", escala=1.4, colores={2: AMBAR}).move_to([0, -3.3, 0])
        caja_res = SurroundingRectangle(res, color=AMBAR, buff=0.2, stroke_width=3)

        with self.narrar("b2"):
            # «entra en la suma»
            self.en("entra")
            self.corte()
            self.play(FadeIn(l1), run_time=0.3)
            self.play(FadeIn(l2), run_time=self.dur(0.7))

            # «se queda con cada entrada»
            self.en("se_queda")
            self.play(l2[3].animate(rate_func=there_and_back).scale(1.25).set_color(AMBAR), run_time=0.6)

            # «estacionaria»
            self.en("estac")
            self.pop(sello_e)

            # «la misma media»
            self.en("misma")
            self.play(FadeIn(l3), run_time=self.dur(0.7))

            # «sale fuera»
            self.en("sale_fuera")
            self.play(FadeIn(l4), run_time=self.dur(0.8))

            # «Dentro queda»
            self.en("dentro")
            self.play(Create(marco), run_time=self.dur(0.5))

            # «la suma de todos los hache»
            self.en("suma_h")
            self.resaltar(l4[2], color=AMBAR, escala=1.1)

            # «la ganancia en continua»
            self.en("gan")
            self.play(FadeIn(etq_gan), FadeIn(etq_h), run_time=self.dur(0.6))

            # «La media de la salida»
            self.en("media_sale")
            self.play(FadeIn(res[0]), FadeIn(res[1]), run_time=self.dur(0.5))

            # «hache en cero por la media»
            self.en("resultado")
            self.play(FadeIn(res[2:]), Create(caja_res), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
