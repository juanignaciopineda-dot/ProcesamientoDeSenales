"""Escena 05 — Luz blanca por un vidrio de color: el modelador con la moneda y el filtro de ρ = 0,4."""
from comun.escena import *


class LuzBlancaPorUnVidrio(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        mon = moneda("", AMBAR).scale(0.9).move_to([-6.0, 2.4, 0])
        tira = tira_pm1([1, -1, 1, 1, -1], lado=0.55).move_to([-3.6, 2.4, 0])
        E1 = Lienzo(ancho=3.0, alto=1.3, t_rango=(-3, 3), v_max=1.5, centro=(-4.4, -0.4))
        base1 = E1.base()
        plano = E1.curva([-3, 3], [1, 1], AMBAR, 5)
        t_plano = etiqueta("plano, altura 1", INK, 0.5).move_to([-4.4, -1.6, 0])
        blq = BloqueLTI("H", centro=(0.4, 0.5), ancho=1.9, alto=1.2, largo=1.0, color=CIAN)
        F = formula("D_{xx}", "=", "|H|^2", r"\cdot", "1", escala=1.3, colores={0: AMBAR}).move_to([0.4, -1.6, 0])
        E2 = Lienzo(ancho=3.0, alto=1.5, t_rango=(-3, 3), v_max=1.5, centro=(5.0, -0.4))
        base2 = E2.base()
        forma = curva_f(E2, lambda w: 0.25 + 1.0 * np.exp(-(np.asarray(w) / 1.2) ** 2), -3, 3, AMBAR, 5)
        t_sal = etiqueta("densidad de salida", INK, 0.5).move_to([5.0, -1.6, 0])
        F2 = formula("|H|", "=", r"\sqrt{D_{xx}}", escala=1.3, colores={0: AMBAR}).move_to([0.4, -3.0, 0])
        luz = luz_blanca(MAGENTA, largo=1.6).scale(0.9).move_to([4.6, 2.4, 0])
        with self.narrar("b1"):
            # «el ruido blanco, la moneda»
            self.en("moneda")
            self.play(FadeIn(mon), FadeIn(tira), run_time=self.dur(0.8))

            # «espectro plano de altura uno»
            self.en("plano")
            self.play(Create(base1), Create(plano), run_time=self.dur(0.8))
            self.play(FadeIn(t_plano), run_time=0.3)

            # «Lo pasamos por un filtro»
            self.en("filtro")
            self.play(FadeIn(blq), run_time=self.dur(0.6))

            # «la ganancia al cuadrado por la de la entrada»
            self.en("formula")
            self.play(FadeIn(F[0]), FadeIn(F[1]), FadeIn(F[2]), run_time=self.dur(1.0))
            self.play(FadeIn(F[3]), run_time=0.3)

            # «que es uno»
            self.en("uno")
            self.play(FadeIn(F[4]), run_time=0.3)
            self.resaltar(F[4], color=AMBAR)

            # «una densidad concreta»
            self.en("concreta")
            self.play(Create(base2), Create(forma), FadeIn(t_sal), run_time=self.dur(1.0))

            # «ganancia al cuadrado sea esa densidad»
            self.en("despeja")
            self.play(FadeOut(F), FadeIn(F2), run_time=self.dur(0.8))

            # «luz blanca por un vidrio de color»
            self.en("vidrio")
            self.play(Create(luz.entrada), run_time=0.4)
            self.play(FadeIn(luz.vidrio), run_time=0.2)
            self.play(Create(luz.salida), run_time=0.5)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        blq = BloqueLTI("H", centro=(-3.5, 2.6), ancho=2.0, alto=1.2, largo=1.5, color=CIAN)
        rho = MathTex(r"\rho=0{,}4", color=AMBAR).scale(1.0).move_to([4.8, 2.6, 0])
        filtro = formula("y[n]", "=", r"\frac{2\,w[n]+w[n-1]}{\sqrt5}", escala=1.0).move_to([-3.2, 0.7, 0])
        gan = formula(r"\frac{|2+e^{-j\Omega}|^2}{5}", escala=0.95).move_to([-3.5, -0.8, 0])
        cuenta = formula("=", r"\frac{4+1+4\cos\Omega}{5}", escala=0.95).move_to([-3.3, -2.0, 0])
        igual = MathTex("=", color=AMBAR).scale(1.5).move_to([-0.8, -2.0, 0])
        res = formula("1", "+", num_tex(0.8), r"\cos\Omega", escala=1.1, colores={0: AMBAR}).move_to([0.9, -2.0, 0])
        E = Lienzo(ancho=4.0, alto=2.0, t_rango=(-np.pi, np.pi), v_max=2.0, centro=(4.4, -1.0))
        ej = ejes_L(E, 0, 2.0)
        c = curva_f(E, espectro_3b(0.4), -np.pi, np.pi, AMBAR, 5)
        ok = tilde(VERDE, 0.6).move_to([6.5, 0.6, 0])
        with self.narrar("b2"):
            # «Ya lo hemos hecho sin decirlo»
            self.en("hecho")
            self.corte()
            self.play(FadeIn(blq), run_time=self.dur(0.7))

            # «rho igual a cero coma cuatro»
            self.en("rho")
            self.pop(rho)

            # «dos veces la moneda más la anterior entre raíz de cinco»
            self.en("filtro")
            self.play(FadeIn(filtro), run_time=self.dur(1.2))

            # «una ganancia al cuadrado»
            self.en("gan")
            self.play(FadeIn(gan), run_time=self.dur(1.2))

            # «cuatro más uno más cuatro por el coseno de omega, entre cinco»
            self.en("cuenta")
            self.play(FadeIn(cuenta), run_time=self.dur(1.2))

            # «por el coseno de omega»
            self.en("coseno")
            self.resaltar(cuenta, color=AMBAR)

            # «Es decir»
            self.en("esdecir")
            self.pop(igual)

            # «uno más cero coma ocho por el coseno de omega»
            self.en("resultado")
            self.play(FadeIn(res), run_time=self.dur(1.2))

            # «El espectro de aquel proceso»
            self.en("espectro")
            self.play(Create(ej), Create(c), run_time=self.dur(1.0))
            self.pop(ok)
