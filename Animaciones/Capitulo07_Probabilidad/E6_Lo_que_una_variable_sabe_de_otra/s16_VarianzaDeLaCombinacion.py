"""Escena 16 — La varianza de una combinación lineal, deducida paso a paso."""
from comun.escena import *


class VarianzaDeLaCombinacion(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        c = {0: AMBAR}
        L0 = formula(r"\sigma_Z^2", "=", "E", r"\big[(Z-\mu_Z)^2\big]", escala=1.2, colores=c).move_to([-3.6, 3.3, 0])
        L1 = formula(r"Z-\mu_Z", "=", r"\alpha(X-\mu_X)", "+", r"\beta(Y-\mu_Y)", escala=1.1,
                     colores={2: SENAL, 4: MEDIDA}).move_to([0, 2.0, 0])
        L2 = formula(r"(Z-\mu_Z)^2", "=", r"\Big[", r"\alpha(X-\mu_X)", "+", r"\beta(Y-\mu_Y)", r"\Big]^2",
                     escala=1.0, colores={3: SENAL, 5: MEDIDA}).move_to([0, 0.7, 0])
        L3 = formula("=", r"\alpha^2(X-\mu_X)^2", "+", r"\beta^2(Y-\mu_Y)^2", "+", r"2\alpha\beta(X-\mu_X)(Y-\mu_Y)",
                     escala=0.95, colores={1: SENAL, 3: MEDIDA, 5: AMBAR}).move_to([0, -0.6, 0])
        L4 = formula(r"\sigma_Z^2", "=", r"\alpha^2E[(X-\mu_X)^2]", "+", r"\beta^2E[(Y-\mu_Y)^2]", "+",
                     r"2\alpha\beta E[(X-\mu_X)(Y-\mu_Y)]", escala=0.85,
                     colores={0: AMBAR, 2: SENAL, 4: MEDIDA, 6: AMBAR}).move_to([0, -2.0, 0])
        abc = formula(r"(a+b)^2", "=", "a^2", "+", "2ab", "+", "b^2", escala=1.0, colores={0: INK}).move_to([4.0, 3.3, 0])
        for m in (L0, L1, L2, L3, L4, abc):
            oculta(m)
            self.add(m)
        self.todo = VGroup(L0, L1, L2, L3, L4, abc)
        with self.narrar("b1"):
            # «hay que deducirla»
            self.en("deducir")
            self.play(*revelar(*L0), run_time=self.dur(0.8))

            # «Restamos la media»
            self.en("restar2")
            self.play(*revelar(L1[0], L1[1]), run_time=self.dur(0.6))

            # «alfa por equis centrada»
            self.en("a_xc")
            self.play(*revelar(L1[2]), run_time=self.dur(0.7))

            # «más beta por i griega centrada»
            self.en("b_yc")
            self.play(*revelar(L1[3], L1[4]), run_time=self.dur(0.7))

            # «Lo elevamos al cuadrado»
            self.en("cuadrado")
            self.play(LaggedStart(*revelar(*L2), lag_ratio=0.12), run_time=self.dur(1.2))

            # «a más be al cuadrado»
            self.en("abc")
            self.play(LaggedStart(*revelar(*abc), lag_ratio=0.1), run_time=self.dur(1.1))

            # «el primero al cuadrado»
            self.en("prim")
            self.play(*revelar(L3[0], L3[1]), run_time=self.dur(0.7))

            # «el segundo al cuadrado»
            self.en("seg")
            self.play(*revelar(L3[2], L3[3]), run_time=self.dur(0.7))

            # «dos veces el producto»
            self.en("doble")
            self.play(*revelar(L3[4], L3[5]), run_time=self.dur(0.8))

            # «la esperanza de cada término»
            self.en("esp_t")
            self.play(LaggedStart(*revelar(*L4), lag_ratio=0.12), run_time=self.dur(1.3))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        R = formula(r"\sigma_Z^2", "=", r"\alpha^2\sigma_X^2", "+", r"\beta^2\sigma_Y^2", "+", r"2\alpha\beta\,\sigma_{XY}",
                    escala=1.3, colores={0: AMBAR, 2: SENAL, 4: MEDIDA, 6: AMBAR}).move_to([0, 1.6, 0])
        oculta(R)
        self.add(R)
        with self.narrar("b2"):
            # «Quedan tres términos»
            self.en("tres")
            self.play(FadeOut(self.todo), run_time=0.3)
            self.play(*revelar(R[0], R[1]), run_time=self.dur(0.5))

            # «Alfa al cuadrado por la varianza de equis»
            self.en("t1")
            self.play(*revelar(R[2]), run_time=self.dur(0.6))

            # «Beta al cuadrado por la varianza de i griega»
            self.en("t2")
            self.play(*revelar(R[3], R[4]), run_time=self.dur(0.7))

            # «un término cruzado»
            self.en("cruzado")
            self.play(*revelar(R[5], R[6]), run_time=self.dur(0.7))
            cr = SurroundingRectangle(VGroup(R[6]), color=AMBAR, buff=0.12, stroke_width=3)
            cr.permitir_encima = True
            self.play(Create(cr), run_time=self.dur(0.4))

            # «dos por alfa por beta»
            self.en("dosab")
            self.resaltar(cr, color=TXT, escala=1.1)

            # «por la covarianza»
            self.en("por_cov")
            self.resaltar(cr, color=ROJO, escala=1.1)

            # «no tienen covarianza»
            self.en("sin_cov")
            s0 = formula(r"\sigma_{XY}", "=", "0", escala=1.6, colores={0: AMBAR, 2: AMBAR}).move_to([0, -0.2, 0])
            self.pop(s0)

            # «desaparece»
            self.en("desaparece")
            self.play(FadeOut(cr), R[5].animate.set_opacity(0), R[6].animate.set_opacity(0), run_time=self.dur(0.6))

            # «las varianzas simplemente se suman»
            self.en("suman")
            marco = SurroundingRectangle(VGroup(R[0], R[4]), color=AMBAR, buff=0.2, stroke_width=3)
            marco.permitir_encima = True
            self.play(Create(marco), run_time=self.dur(0.6))

            # «la promesa que dejamos pendiente»
            self.en("promesa")
            prom = caja("Las varianzas se suman", AMBAR, ancho=6.6, alto=0.9, scale=0.7).move_to([0, -2.5, 0])
            self.play(FadeIn(prom, shift=UP * 0.2), run_time=self.dur(0.7))

            # «al hablar de promedios»
            self.en("pagada")
            ok = tilde(VERDE, 0.7).next_to(prom, RIGHT, buff=0.4)
            self.play(Create(ok), run_time=self.dur(0.5))
            self.sfx("exito")
