"""Escena 03 — Factorizar lo medido: S_xx como una sola fracción y el numerador como κ(1 − ρz⁻¹)(1 − ρz)."""
from comun.escena import *


class FactorizarLoMedido(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        term = termometro(alto=1.1).move_to([-6.4, 3.0, 0])
        A0 = formula("S_{xx}", "=", escala=1.2, colores={0: MEDIDA}).move_to([-4.6, 3.2, 0])
        A1 = oculta(formula("S_{yy}", "+", "1", escala=1.2, colores={0: SENAL, 2: RUIDO}))
        A1.next_to(A0, RIGHT, buff=0.2)
        interro = MathTex("?", color=AMBAR).scale(1.2).next_to(A0, RIGHT, buff=0.25)
        num_a = MathTex(r"2{,}56", color=SENAL).scale(1.15)
        den_a = formula(r"|1-0{,}6\,", r"e^{-j\Omega}", r"|^2", escala=1.15)
        fr_a = fraccion(num_a, den_a)
        mas1 = formula("+", "1", escala=1.15, colores={0: RUIDO, 1: RUIDO})
        fila = VGroup(fr_a, mas1).arrange(RIGHT, buff=0.35).move_to([-1.6, 1.3, 0])
        llave = Brace(den_a, DOWN, color=AMBAR, buff=0.12)
        dev = formula(r"1+0{,}36-0{,}6\,", r"(e^{j\Omega}+e^{-j\Omega})", escala=1.05).move_to([-1.6, -0.35, 0])
        d2 = oculta(formula(r"1{,}36", r"-0{,}6\,", r"(z+z^{-1})", escala=1.15).move_to([-1.6, -0.35, 0]))
        d2_nota = etiqueta("con z = e^{jΩ}", INK, 0.5).move_to([3.6, -0.35, 0])
        # la suma en una sola fracción
        num_b = formula(r"3{,}92", r"-0{,}6\,", r"(z+z^{-1})", escala=1.1)
        den_b = formula(r"1{,}36", r"-0{,}6\,", r"(z+z^{-1})", escala=1.1)
        fr_b = fraccion(num_b, den_b)
        fr_b.move_to([-0.8, -2.6, 0])
        oculta(num_b)
        self.fr_b, self.num_b = fr_b, num_b
        with self.narrar("b1"):
            # «Factoricemos, a mano»
            self.en("factor")
            self.add(A1)
            self.play(FadeIn(term), FadeIn(A0), FadeIn(interro), run_time=self.dur(0.6))

            # «la densidad de lo medido»
            self.en("medido")
            self.play(FadeOut(interro), run_time=0.15)
            self.play(*revelar(A1), run_time=self.dur(0.6))

            # «dos coma cinco seis»
            self.en("numer")
            self.play(FadeIn(num_a, shift=UP * 0.2), Create(fr_a.barra), run_time=self.dur(0.5))

            # «entre el módulo al cuadrado de uno menos cero coma seis»
            self.en("modulo")
            self.play(FadeIn(den_a), run_time=self.dur(0.8))

            # «e elevado a menos jota omega»
            self.en("exp")
            self.play(den_a[1].animate.set_color(AMBAR), run_time=self.dur(0.4))

            # «más el uno del ruido»
            self.en("ruido")
            self.play(FadeIn(mas1, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Ese denominador vale»
            self.en("deno")
            self.play(GrowFromCenter(llave), run_time=0.3)
            self.play(FadeIn(dev), run_time=self.dur(0.9))

            # «uno coma tres seis»
            self.en("desarrollo")
            self.add(d2)
            self.play(FadeOut(dev), FadeOut(llave), *revelar(d2[0]), run_time=self.dur(0.5))

            # «cero coma seis por zeta más zeta a la menos uno»
            self.en("zeta")
            self.play(*revelar(d2[1], d2[2]), FadeIn(d2_nota), run_time=self.dur(0.6))

            # «Al sumar las fracciones»
            self.en("suma")
            self.add(num_b)
            self.play(Create(fr_b.barra), TransformFromCopy(d2, fr_b.den), FadeOut(d2_nota),
                      fr_a.animate.set_opacity(0.4), mas1.animate.set_opacity(0.4), run_time=self.dur(1.0))

            # «el numerador queda tres coma nueve dos»
            self.en("tres92")
            self.play(*revelar(num_b[0]), run_time=self.dur(0.6))
            self.sfx("pop")

            # «por esa misma suma»
            self.en("misma")
            self.play(*revelar(num_b[1], num_b[2]), run_time=self.dur(0.7))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        N = self.num_b
        fr_b = self.fr_b
        fr_b.remove(N)
        self.add(N)
        N.generate_target()
        N.target.move_to([-0.6, 3.0, 0]).scale(1.1)
        k = oculta(formula("=", r"\kappa", r"(1-\rho\,z^{-1})", r"(1-\rho\,z)", escala=1.2,
                           colores={1: AMBAR}).move_to([0.2, 1.5, 0]))
        ex = oculta(formula("=", r"\kappa(1+\rho^2)", r"-\kappa\rho\,(z+z^{-1})", escala=1.2).move_to([0.2, 0.0, 0]))
        eq1 = oculta(formula(r"\kappa\rho", "=", r"0{,}6", escala=1.2, colores={0: VERDE, 2: VERDE}).move_to([-3.0, -1.9, 0]))
        eq2 = oculta(formula(r"\kappa(1+\rho^2)", "=", r"3{,}92", escala=1.2, colores={0: CIAN, 2: CIAN}).move_to([3.0, -1.9, 0]))
        self.add(k, ex, eq1, eq2)
        with self.narrar("b2"):
            # «Queremos escribir ese numerador»
            self.en("queremos")
            self.play(*[FadeOut(m) for m in self.mobjects
                        if m is not self.camera.frame and all(m is not x for x in (N, k, ex, eq1, eq2))],
                      run_time=0.3)
            self.play(MoveToTarget(N), run_time=self.dur(0.6))
            self.play(N.animate.set_color(AMBAR), run_time=0.3)

            # «una constante, kappa»
            self.en("kappa")
            self.play(*revelar(k[0], k[1]), run_time=self.dur(0.5))

            # «por uno menos ro zeta a la menos uno»
            self.en("ro1")
            self.play(*revelar(k[2]), run_time=self.dur(0.6))

            # «por uno menos ro zeta.»
            self.en("ro2")
            self.play(*revelar(k[3]), run_time=self.dur(0.6))

            # «Al multiplicar»
            self.en("multiplica")
            self.resaltar(k[2], k[3], run_time=0.6)

            # «aparece kappa por uno más ro al cuadrado»
            self.en("masro2")
            self.play(*revelar(ex[0], ex[1]), run_time=self.dur(0.7))

            # «menos kappa ro por la suma»
            self.en("menoskro")
            self.play(*revelar(ex[2]), run_time=self.dur(0.7))

            # «Igualamos»
            self.en("igualamos")
            self.play(N[0].animate.set_color(CIAN), N[1].animate.set_color(VERDE), N[2].animate.set_color(VERDE),
                      ex[1].animate.set_color(CIAN), ex[2].animate.set_color(VERDE), run_time=self.dur(0.8))

            # «kappa por ro vale cero coma seis»
            self.en("kro")
            self.play(*revelar(eq1), run_time=self.dur(0.7))

            # «tres coma nueve dos»
            self.en("k392")
            self.play(*revelar(eq2), run_time=self.dur(0.7))
