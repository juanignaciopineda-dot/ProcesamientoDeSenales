"""Escena 06 — El error del pulso (2, 2, 1): P_FA = P_M = Q(1,5) = 0,0668, y las fórmulas generales."""
from comun.escena import *


class ElErrorDelPulso(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.cuentas()
        self.en_general()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def cuentas(self):
        L = Lienzo(ancho=7.4, alto=3.2, t_rango=(-8, 17), v_max=1.2, centro=(-2.6, -1.3))
        base = eje_g3(L, marcas=(0, 9))
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        umb = umbral3(L, 4.5, alto=2.2)
        cola_d = cola3(L, 0, 3, 4.5, 17)
        cola_i = cola3(L, 9, 3, -8, 4.5)
        g45 = MathTex(r"\gamma=4{,}5", color=ESTIMACION).scale(0.9).move_to([4.7, 3.2, 0])
        cent = Text("media 0 · desvío 3", color=RUIDO).scale(0.5).move_to([-5.0, 1.7, 0])
        estand = Text("estandarizamos", color=AMBAR, weight=BOLD).scale(0.6).move_to([4.7, 2.3, 0])
        r1 = formula("(", "4{,}5", "-", "0", ")", "/", "3", "=", "1{,}5", escala=1.1,
                     colores={7: TXT, 8: AMBAR}).move_to([4.7, 1.3, 0])
        qfa = formula("P_{FA}", "=", "Q(1{,}5)", escala=1.1, colores={0: ERROR, 2: ESTIMACION}).move_to([4.7, 0.2, 0])
        val = formula("=", "0{,}0668", escala=1.1, colores={1: ERROR}).move_to([4.7, -0.7, 0])
        r2 = formula("(", "9", "-", "4{,}5", ")", "/", "3", "=", "1{,}5", escala=1.1,
                     colores={8: AMBAR}).move_to([4.7, -2.1, 0])
        ok = tilde(VERDE, 0.5).next_to(r2, RIGHT, buff=0.1)
        ok.move_to([6.75, -2.1, 0])

        with self.narrar("b1"):
            # «Ahora la falsa alarma»
            self.en("fa")
            self.play(FadeIn(base), Create(cam0), Create(cam1), run_time=self.dur(0.7))
            self.play(FadeIn(cola_d), run_time=self.dur(0.4))

            # «El umbral es cuatro coma cinco»
            self.en("umbral")
            self.play(Create(umb), FadeIn(g45), run_time=self.dur(0.7))

            # «centrada en cero con desvío tres»
            self.en("cent")
            self.play(FadeIn(cent), cam0.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.8))

            # «Estandarizamos»
            self.en("estand")
            self.pop(estand)

            # «cuatro coma cinco menos cero»
            self.en("resta")
            self.play(*[FadeIn(r1[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(0.8))

            # «entre tres»
            self.en("entre")
            self.play(*[FadeIn(r1[i], shift=UP * 0.1) for i in (5, 6)], run_time=self.dur(0.5))

            # «es uno coma cinco»
            self.en("uno5")
            self.play(*[FadeIn(r1[i], shift=UP * 0.1) for i in (7, 8)], run_time=self.dur(0.5))

            # «Falsa alarma igual a cu de uno coma cinco»
            self.en("qfa")
            self.play(FadeIn(qfa, shift=UP * 0.1), run_time=self.dur(0.9))

            # «cero coma cero seis seis ocho»
            self.en("val")
            self.play(FadeIn(val, shift=UP * 0.1), run_time=self.dur(0.7))

            # «Con el fallo hacemos lo mismo»
            self.en("fallo")
            self.play(FadeOut(cola_d), FadeIn(cola_i), cam1.animate(rate_func=there_and_back).set_stroke(width=9),
                      run_time=self.dur(0.9))

            # «nueve menos cuatro coma cinco»
            self.en("nueve")
            self.play(*[FadeIn(r2[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(0.9))

            # «otra vez uno coma cinco»
            self.en("otra")
            self.play(*[FadeIn(r2[i], shift=UP * 0.1) for i in (5, 6, 7, 8)], run_time=self.dur(0.7))
            self.play(FadeIn(ok, scale=0.5), run_time=self.dur(0.3))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def en_general(self):
        L = lienzo_g3(centro=(0.0, -1.2))
        base = eje_g3(L, marcas=())
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        umb = umbral3(L, 4.5, alto=2.0)
        cola_d = cola3(L, 0, 3, 4.5, 17)
        cola_i = cola3(L, 9, 3, -8, 4.5)
        iguales = formula("P_{FA}", "=", "P_M", escala=1.1, colores={0: ERROR, 2: ERROR}).move_to([0, -3.3, 0])
        priors = formula("p_0", "=", "p_1", "=", r"\tfrac12", escala=0.85,
                         colores={0: RUIDO, 2: SENAL, 4: AMBAR}).move_to([-5.2, 3.4, 0])
        pe = formula("P_e", "=", r"\tfrac12", r"\cdot", "0{,}0668", "+", r"\tfrac12", r"\cdot", "0{,}0668", "=", r"6{,}7\,\%",
                     escala=0.85, colores={0: ESTIMACION, 10: AMBAR}).move_to([2.0, 3.4, 0])
        rejilla = rejilla3(7, centro=(0, -0.4), lado=0.3)
        siete = Text("unas 7 de cada 100", color=TXT).scale(0.55).move_to([0, -3.3, 0])
        fgen = formula("P_{FA}", "=", "Q", "(", r"\frac{\gamma}{\sigma\sqrt{E}}", ")", escala=1.0,
                       colores={0: ERROR}).move_to([-3.2, 3.2, 0])
        mgen = formula("P_M", "=", "Q", "(", r"\frac{E-\gamma}{\sigma\sqrt{E}}", ")", escala=1.0,
                       colores={0: ERROR}).move_to([3.0, 3.2, 0])
        e_rot = MathTex("E", color=SENAL).scale(0.65).move_to(L.p(9, 0) + DOWN * 0.35)
        c_rot = MathTex("0", color=RUIDO).scale(0.65).move_to(L.p(0, 0) + DOWN * 0.35)
        d_i = DoubleArrow(L.p(0, 0) + DOWN * 0.9, L.p(4.5, 0) + DOWN * 0.9, buff=0, color=INK, stroke_width=3, tip_length=0.15)
        d_d = DoubleArrow(L.p(4.5, 0) + DOWN * 0.9, L.p(9, 0) + DOWN * 0.9, buff=0, color=INK, stroke_width=3, tip_length=0.15)
        ds = VGroup(MathTex(r"\gamma/\sigma\sqrt{E}", color=INK).scale(0.6).next_to(d_i, DOWN, buff=0.08),
                    MathTex(r"(E-\gamma)/\sigma\sqrt{E}", color=INK).scale(0.6).next_to(d_d, DOWN, buff=0.08))
        sim = Text("1.000.000 de pruebas", color=TXT).scale(0.6).move_to([-3.6, -3.4, 0])
        res = formula(r"0{,}0667", escala=1.1, colores={0: VERDE}).move_to([3.4, -3.4, 0])

        with self.narrar("b2"):
            # «Por la simetría de la campana»
            self.en("simetria")
            self.corte()
            self.play(FadeIn(base), Create(cam0), Create(cam1), FadeIn(umb), FadeIn(cola_d), FadeIn(cola_i),
                      run_time=self.dur(0.8))

            # «las dos colas son iguales»
            self.en("iguales")
            self.pop(iguales)

            # «Con probabilidades iguales»
            self.en("priors")
            self.play(FadeIn(priors, shift=UP * 0.1), run_time=self.dur(0.7))

            # «un seis coma siete por ciento»
            self.en("pe")
            self.play(Write(pe), run_time=self.dur(1.6))

            # «unas siete de cada cien veces»
            self.en("siete")
            self.play(*[FadeOut(m) for m in (base, cam0, cam1, umb, cola_d, cola_i, iguales)], run_time=self.dur(0.3))
            self.play(FadeIn(rejilla), FadeIn(siete), run_time=self.dur(0.6))

            # «En general»
            self.en("general")
            self.corte()
            self.add(base, cam0, cam1, umb, cola_d, cola_i)
            self.play(FadeIn(e_rot), FadeIn(c_rot), run_time=self.dur(0.4))

            # «la falsa alarma es cu de gamma entre sigma raíz de e»
            self.en("fgen")
            self.play(LaggedStart(*[FadeIn(fgen[i], shift=UP * 0.1) for i in range(5)], lag_ratio=0.25),
                      run_time=self.dur(1.5))

            # «y el fallo, cu de e menos gamma, entre lo mismo»
            self.en("mgen")
            self.play(LaggedStart(*[FadeIn(mgen[i], shift=UP * 0.1) for i in range(5)], lag_ratio=0.25),
                      run_time=self.dur(1.5))

            # «cuentan los desvíos del umbral a cada centro»
            self.en("desv")
            self.play(Create(d_i), Create(d_d), FadeIn(ds), run_time=self.dur(0.9))

            # «Un millón de simulaciones»
            self.en("sim")
            self.play(FadeIn(sim, shift=UP * 0.1), run_time=self.dur(0.6))

            # «da cero coma cero seis seis siete»
            self.en("res")
            self.pop(res)
        self.wait(0.3)
