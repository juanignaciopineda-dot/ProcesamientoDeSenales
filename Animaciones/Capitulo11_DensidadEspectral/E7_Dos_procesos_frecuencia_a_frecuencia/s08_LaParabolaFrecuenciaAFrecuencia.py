"""Escena 08 — La misma parábola, ahora con la densidad de una mezcla de procesos, en cada frecuencia."""
from comun.escena import *


class LaParabolaFrecuenciaAFrecuencia(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        F1 = oculta(formula("z", "=", "x", "+", r"\alpha", "y", escala=1.2,
                            colores={2: SENAL, 5: MEDIDA}).move_to([-3.6, 3.1, 0]))
        l_ret = etiqueta("(retrasada)", MEDIDA, 0.5).move_to([-0.2, 3.1, 0])
        rel = reloj(INK).scale(0.6).move_to([1.4, 3.1, 0])
        F2 = oculta(formula(r"D_{zz}", "=", r"D_{yy}\,\alpha^2", "+", r"2\,\mathrm{Re}(D_{yx})\,\alpha", "+",
                            r"D_{xx}", escala=0.85, colores={0: AMBAR}).move_to([-2.9, 0.4, 0]))
        eje = Line([1.7, 2.0, 0], [6.6, 2.0, 0], color=INK, stroke_width=2.5)
        l_w = MathTex(r"\omega", color=INK).scale(0.6).move_to([6.85, 2.25, 0])
        marca = Dot([2.5, 2.0, 0], radius=0.1, color=AMBAR)
        par = parabola_l(centro=(4.1, -1.5), ancho=4.0, alto=2.4, fondo=0.25)
        with self.narrar("b1"):
            # «Mezclamos equis»
            self.en("mezcla")
            self.corte()
            self.add(F1, F2)
            self.play(*revelar(F1[0], F1[1], F1[2]), run_time=self.dur(0.7))

            # «multiplicada por un número alfa»
            self.en("alfa")
            self.play(*revelar(F1[3], F1[4]), run_time=self.dur(0.7))

            # «y a veces retrasada»
            self.en("retraso")
            self.play(*revelar(F1[5]), FadeIn(l_ret), FadeIn(rel), run_time=self.dur(0.7))

            # «La densidad espectral de la mezcla»
            self.en("dzz")
            self.play(*revelar(F2[0], F2[1]), run_time=self.dur(0.7))

            # «en una frecuencia cualquiera»
            self.en("freq")
            self.play(Create(eje), FadeIn(l_w), FadeIn(marca), run_time=self.dur(0.6))
            self.play(marca.animate.move_to([4.6, 2.0, 0]), run_time=self.dur(0.9))

            # «una parábola en alfa»
            self.en("parab")
            self.play(Create(par.eje), Create(par.curva), run_time=self.dur(1.0))

            # «la densidad de i griega por alfa al cuadrado»
            self.en("t1")
            self.play(*revelar(F2[2]), run_time=self.dur(0.6))

            # «más un término con la cruzada por alfa»
            self.en("t2")
            self.play(*revelar(F2[3], F2[4]), run_time=self.dur(0.8))

            # «más la densidad de equis»
            self.en("t3")
            self.play(*revelar(F2[5], F2[6]), run_time=self.dur(0.7))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        F3 = formula(r"D_{zz}", r"\ge 0", escala=1.0, colores={0: AMBAR, 1: VERDE}).move_to([-3.0, 3.2, 0])
        par = parabola_l(centro=(-3.0, 0.3), ancho=4.0, alto=2.6, fondo=0.3, color=AMBAR)
        par7 = parabola_l(centro=(-3.0, 0.3), ancho=4.0, alto=2.6, fondo=0.3, color=INK)
        t7 = etiqueta("capítulo 7", INK, 0.5).move_to([-3.0, -1.0, 0])
        # tres frecuencias, tres parábolas
        pequenas = VGroup(*[parabola_l(centro=(x, 0.5), ancho=1.7, alto=1.4, fondo=f, color=AMBAR)
                            for x, f in [(1.6, 0.2), (3.9, 0.4), (6.1, 0.15)]])
        eje = Line([0.7, -0.5, 0], [6.9, -0.5, 0], color=INK, stroke_width=2.5)
        l_w = MathTex(r"\omega", color=INK).scale(0.6).move_to([6.9, -0.85, 0])
        disc = etiqueta("discriminante ≤ 0", AMBAR, 0.6).move_to([-3.0, -1.9, 0])
        F4 = oculta(formula(r"|D_{yx}(j\omega)|^2", r"\le", r"D_{xx}(j\omega)", r"D_{yy}(j\omega)", escala=0.9,
                            colores={0: AMBAR}).move_to([0.2, -3.2, 0]))
        l_ret = formula(r"\text{retardo }\tau", escala=0.7, colores={0: CIAN}).move_to([-3.0, -2.55, 0])
        o = np.array([6.0, -2.0, 0.0])
        pl = plano_c((o[0], o[1]), radio=0.8)
        fz = flecha_c(o, 0.8, 130, AMBAR, ancho=5)
        nota_ap = caja("apunte en profundidad", INK, ancho=3.4, alto=0.5, scale=0.4).move_to([4.8, 3.3, 0])
        with self.narrar("b2"):
            # «nunca es negativa»
            self.en("nonegativa")
            self.corte()
            self.add(F4)
            self.play(FadeIn(F3), Create(par.eje), Create(par.curva), run_time=self.dur(0.9))

            # «la misma parábola»
            self.en("misma")
            self.play(Create(par7.curva), FadeIn(t7), run_time=self.dur(0.8))
            self.play(FadeOut(par7.curva), run_time=0.3)

            # «en cada frecuencia por separado»
            self.en("cadafreq")
            self.play(Create(eje), FadeIn(l_w), run_time=self.dur(0.4))
            self.play(LaggedStart(*[Create(p.curva) for p in pequenas], lag_ratio=0.3), run_time=self.dur(1.2))

            # «Su discriminante»
            self.en("discr")
            self.play(FadeIn(disc), run_time=self.dur(0.5))

            # «el módulo de la densidad cruzada al cuadrado»
            self.en("mod2")
            self.play(*revelar(F4[0]), run_time=self.dur(0.8))

            # «no supera el producto de las dos densidades»
            self.en("prod")
            self.play(*revelar(F4[1], F4[2], F4[3]), run_time=self.dur(1.0))

            # «El retardo»
            self.en("retardo")
            self.play(FadeIn(l_ret), run_time=self.dur(0.5))

            # «sirve para girar la flecha»
            self.en("gira")
            self.play(Create(pl), GrowArrow(fz), run_time=self.dur(0.5))
            self.play(Rotate(fz, -np.deg2rad(130), about_point=o), run_time=self.dur(1.2))

            # «el detalle está en el apunte en profundidad»
            self.en("apunte")
            self.play(FadeIn(nota_ap), run_time=self.dur(0.5))
