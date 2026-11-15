"""Escena 03 — Cómo se reparte g cuando solo hay ruido: media 0, varianza 9σ², desvío 3."""
from comun.escena import *


class ReparteDeGe(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.definicion()
        self.media_y_varianza()
        self.campana_h0()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def definicion(self):
        g = formula("g", "=", r"\sum", "r[n]", "s[n]", escala=1.2,
                    colores={0: ESTIMACION, 3: MEDIDA, 4: SENAL}).move_to([0, 3.1, 0])
        duda = Text("¿cómo se reparte g?", color=ESTIMACION).scale(0.62).move_to([-1.6, 1.8, 0])
        camp_q = DashedVMobject(campana_mini((1.6, 1.8), 1.3, 0.8, ESTIMACION, 3.5))
        c0 = casilla_h3(0, "solo ruido", centro=(-4.0, 1.8))
        rw = formula("r[n]", "=", "W[n]", escala=1.0, colores={0: MEDIDA, 2: RUIDO}).move_to([3.6, 1.8, 0])
        self.terms = formula("g", "=", "2", r"\cdot", "W_0", "+", "2", r"\cdot", "W_1", "+", "1", r"\cdot", "W_2",
                             escala=1.25, colores={0: ESTIMACION, 2: SENAL, 4: RUIDO, 6: SENAL, 8: RUIDO,
                                                   10: SENAL, 12: RUIDO}).move_to([0, 0.2, 0])
        T = self.terms
        self.bells = VGroup(*[campana_mini((T[i].get_center()[0], -1.7), 1.5, 0.95, RUIDO, 3.5) for i in (4, 8, 12)])
        self.perps = VGroup(*[MathTex(r"\perp", color=INK).scale(0.9).move_to(
            [(self.bells[i].get_center()[0] + self.bells[i + 1].get_center()[0]) / 2, -1.7, 0]) for i in (0, 1)])

        with self.narrar("b1"):
            # «de dónde viene ge»
            self.en("ge")
            self.play(Write(g), run_time=self.dur(1.0))

            # «la suma de recibido por señal»
            self.en("suma")
            self.play(g[2].animate(rate_func=there_and_back).scale(1.35).set_color(AMBAR), run_time=self.dur(0.6))

            # «Queremos saber cómo se reparte»
            self.en("reparte")
            self.play(FadeIn(duda), Create(camp_q), run_time=self.dur(0.7))

            # «hipótesis cero»
            self.en("h0")
            self.play(FadeOut(duda), FadeOut(camp_q), FadeIn(c0), run_time=self.dur(0.5))

            # «solo hay ruido»
            self.en("solo")
            self.play(FadeIn(rw, shift=UP * 0.1), run_time=self.dur(0.6))

            # «ge vale dos veces el ruido de la primera muestra»
            self.en("w0")
            self.play(*[FadeIn(T[i], shift=UP * 0.1) for i in range(0, 5)], run_time=self.dur(0.9))

            # «más dos veces el de la segunda»
            self.en("w1")
            self.play(*[FadeIn(T[i], shift=UP * 0.1) for i in range(5, 9)], run_time=self.dur(0.8))

            # «más una vez el de la tercera»
            self.en("w2")
            self.play(*[FadeIn(T[i], shift=UP * 0.1) for i in range(9, 13)], run_time=self.dur(0.8))

            # «Una combinación de campanas independientes»
            self.en("comb")
            self.play(LaggedStart(*[Create(b) for b in self.bells], lag_ratio=0.3), run_time=self.dur(1.0))
            self.play(FadeIn(self.perps), run_time=self.dur(0.4))
        self.wait(0.3)
        self.g_def, self.c0, self.rw = g, c0, rw

    # ------------------------------------------------------------ b2
    def media_y_varianza(self):
        T, bells = self.terms, self.bells
        cap7 = Text("Capítulo 7", color=INK).scale(0.5).move_to([5.8, 3.1, 0])
        grande = campana_mini((4.3, 0.3), 3.2, 1.7, RUIDO, 4.0)
        etq_g = Text("gaussiana", color=RUIDO).scale(0.5).next_to(grande, DOWN, buff=0.25)
        q_media = formula(r"\text{media}", "=", "?", escala=0.95, colores={2: AMBAR}).move_to([-3.3, 0.9, 0])
        q_var = formula(r"\text{varianza}", "=", "?", escala=0.95, colores={2: AMBAR}).move_to([-3.3, -0.1, 0])
        media = formula(r"\text{media}", "=", "0+0+0", "=", "0", escala=0.95,
                        colores={4: AMBAR}).move_to([-3.3, 0.9, 0])
        w0 = campana_mini((-5.4, -2.1), 1.2, 0.9, RUIDO, 3.5)
        w0t = MathTex("W_0", color=RUIDO).scale(0.65).next_to(w0, DOWN, buff=0.12)
        dosw = campana_mini((-2.6, -2.1), 2.4, 0.45, RUIDO, 3.5)
        doswt = MathTex(r"2\cdot W_0", color=RUIDO).scale(0.65).next_to(dosw, DOWN, buff=0.12)
        por4 = formula(r"\text{varianza}", r"\times 2^2", "=", r"\times 4", escala=0.8,
                       colores={1: SENAL, 3: ESTIMACION}).move_to([2.2, -2.1, 0])
        suman = Text("independientes: las varianzas se suman", color=TXT).scale(0.55).move_to([1.2, -1.6, 0])
        perp = MathTex(r"\perp", color=INK).scale(1.0).next_to(suman, LEFT, buff=0.3)
        cuenta = formula(r"4\sigma^2", "+", r"4\sigma^2", "+", r"1\sigma^2", escala=1.0).move_to([-1.0, -3.0, 0])
        nueve = formula("=", r"9\sigma^2", escala=1.0, colores={1: AMBAR}).next_to(cuenta, RIGHT, buff=0.2)
        res_var = formula(r"\text{varianza}", "=", r"9\sigma^2", escala=0.95,
                          colores={2: AMBAR}).move_to([-3.3, -0.1, 0])

        with self.narrar("b2"):
            # «Del capítulo siete»
            self.en("cap7")
            self.play(*[FadeOut(m) for m in (self.g_def, self.c0, self.rw, self.perps)], run_time=self.dur(0.4))
            self.play(T.animate.move_to([0, 2.7, 0]).scale(0.8), bells.animate.move_to([0, 1.2, 0]).scale(0.7),
                      FadeIn(cap7), run_time=self.dur(0.6))

            # «es otra gaussiana»
            self.en("gauss")
            self.play(ReplacementTransform(bells, grande), FadeIn(etq_g), run_time=self.dur(1.0))

            # «Solo falta su media y su varianza»
            self.en("faltan")
            self.play(FadeIn(q_media), FadeIn(q_var), run_time=self.dur(0.6))

            # «La media es cero»
            self.en("media")
            self.play(ReplacementTransform(q_media, media), run_time=self.dur(0.7))

            # «porque cada ruido tiene media cero»
            self.en("cadaruido")
            ceros = VGroup(*[MathTex("0", color=RUIDO).scale(0.75).next_to(T[i], UP, buff=0.18) for i in (4, 8, 12)])
            self.play(LaggedStart(*[FadeIn(z, shift=DOWN * 0.1) for z in ceros], lag_ratio=0.25), run_time=self.dur(0.8))

            # «La varianza»
            self.en("varianza")
            self.play(q_var.animate(rate_func=there_and_back).scale(1.2), run_time=self.dur(0.6))

            # «multiplicar una variable por dos»
            self.en("por2")
            self.play(Create(w0), FadeIn(w0t), run_time=self.dur(0.5))
            self.play(Create(dosw), FadeIn(doswt), run_time=self.dur(0.6))

            # «multiplica su varianza por cuatro»
            self.en("por4")
            self.play(FadeIn(por4, shift=UP * 0.1), run_time=self.dur(0.7))

            # «las varianzas de variables independientes se suman»
            self.en("suman")
            self.play(*[FadeOut(m) for m in (w0, w0t, dosw, doswt, por4)], run_time=self.dur(0.3))
            self.play(FadeIn(suman), FadeIn(perp), run_time=self.dur(0.5))

            # «Cuatro más cuatro más uno»
            self.en("cuenta")
            self.play(LaggedStart(*[FadeIn(cuenta[i], shift=UP * 0.1) for i in range(5)], lag_ratio=0.25),
                      run_time=self.dur(1.2))

            # «nueve, por sigma cuadrado»
            self.en("nueve")
            self.play(FadeIn(nueve), run_time=self.dur(0.5))
            self.play(ReplacementTransform(q_var, res_var), run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def campana_h0(self):
        L = Lienzo(ancho=5.6, alto=3.0, t_rango=(-9, 9), v_max=1.2, centro=(3.6, -0.6))
        base = eje_g3(L, marcas=(0,))
        cam = dens3(L, 0, 3, RUIDO)
        s1 = formula(r"\sigma^2", "=", "1", escala=1.0, colores={2: AMBAR}).move_to([-4.3, 2.8, 0])
        v9 = formula(r"\text{varianza}", "=", "9", escala=1.0, colores={2: AMBAR}).move_to([-4.3, 1.7, 0])
        d3 = formula(r"\text{desvío}", "=", r"\sqrt{9}", "=", "3", escala=1.0, colores={4: AMBAR}).move_to([-4.0, 0.6, 0])
        en9 = formula("E", "=", r"2^2+2^2+1^2", "=", "9", escala=1.0,
                      colores={0: ESTIMACION, 4: AMBAR}).move_to([-3.7, -0.7, 0])
        gen = formula(r"\text{varianza de }g", "=", r"\sigma^2", "E", escala=1.0,
                      colores={2: RUIDO, 3: ESTIMACION}).move_to([-3.3, -2.1, 0])
        c0 = casilla_h3(0, "solo ruido", centro=(3.6, 2.8))
        cero = DashedLine(L.p(0, 0), L.p(0, 1.05), color=INK, stroke_width=2.5)
        brace = Line(L.p(0, 0.5), L.p(3, 0.5), color=ESTIMACION, stroke_width=4)
        punta = VGroup(Line(L.p(0, 0.45), L.p(0, 0.55), color=ESTIMACION, stroke_width=4),
                       Line(L.p(3, 0.45), L.p(3, 0.55), color=ESTIMACION, stroke_width=4))
        des = MathTex(r"\sigma\sqrt{E}", color=ESTIMACION).scale(0.8).next_to(brace, UP, buff=0.08)

        with self.narrar("b3"):
            # «Con sigma cuadrado igual a uno»
            self.en("sigma1")
            self.corte()
            self.play(Write(s1), run_time=self.dur(0.6))

            # «la varianza es nueve»
            self.en("var9")
            self.play(FadeIn(v9, shift=UP * 0.1), run_time=self.dur(0.6))

            # «el desvío, tres»
            self.en("des3")
            self.play(FadeIn(d3, shift=UP * 0.1), run_time=self.dur(0.7))

            # «nueve es la energía»
            self.en("energia")
            self.play(FadeIn(en9, shift=UP * 0.1), run_time=self.dur(1.0))
            self.play(en9[4].animate(rate_func=there_and_back).scale(1.4), run_time=self.dur(0.5))

            # «sigma cuadrado por la energía»
            self.en("general")
            self.play(FadeIn(gen, shift=UP * 0.1), run_time=self.dur(1.0))

            # «bajo la hipótesis cero»
            self.en("bajoh0")
            self.play(FadeIn(c0), Create(base), Create(cam), run_time=self.dur(1.0))

            # «centrada en cero»
            self.en("cero")
            self.play(Create(cero), run_time=self.dur(0.4))

            # «con desvío sigma por la raíz de la energía»
            self.en("desvio")
            self.play(Create(brace), Create(punta), FadeIn(des), run_time=self.dur(0.8))
        self.wait(0.3)
