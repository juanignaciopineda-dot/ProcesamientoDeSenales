"""Escena 07 — La parábola del capítulo 7: de la varianza de una mezcla a Cauchy-Schwarz."""
from comun.escena import *


class LaParabolaDelCapitulo7(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        F0 = oculta(formula(r"\sigma_{XY}^2", r"\le", r"\sigma_X^2\,\sigma_Y^2", escala=1.1,
                            colores={0: AMBAR}).move_to([0, 3.2, 0]))
        F1 = formula("X", "+", r"\lambda", "Y", escala=1.1, colores={0: SENAL, 3: MEDIDA}).move_to([-3.8, 1.8, 0])
        F2 = formula(r"\mathrm{Var}(X+\lambda Y)", r"\ge 0", escala=1.0, colores={1: VERDE}).move_to([-3.8, 0.6, 0])
        F3 = formula(r"\lambda^2\sigma_Y^2", "+", r"2\lambda\sigma_{XY}", "+", r"\sigma_X^2",
                     escala=0.85).move_to([-3.4, -0.7, 0])
        par = parabola_l(centro=(3.6, -0.5), ancho=4.2, alto=2.6, fondo=0.3, color=AMBAR)
        pmin = Dot(par.L.p(0, 0.3), radius=0.09, color=VERDE)
        disc = etiqueta("discriminante ≤ 0", AMBAR, 0.65).move_to([-3.4, -2.2, 0])
        with self.narrar("b1"):
            # «la covarianza al cuadrado»
            self.en("desig")
            self.corte()
            self.add(F0)
            self.play(*revelar(F0[0]), run_time=self.dur(0.6))

            # «nunca supera»
            self.en("nosupera")
            self.play(*revelar(F0[1]), run_time=self.dur(0.5))

            # «el producto de las varianzas»
            self.en("prodvar")
            self.play(*revelar(F0[2]), run_time=self.dur(0.7))

            # «mezclar las dos variables con un número lambda»
            self.en("mezcla")
            self.play(FadeIn(F1), run_time=self.dur(1.0))

            # «la varianza de la mezcla nunca es negativa»
            self.en("nonegativa")
            self.play(FadeIn(F2), run_time=self.dur(0.9))

            # «desarrollada es una parábola en lambda»
            self.en("parabola")
            self.play(FadeIn(F3), Create(par.eje), Create(par.curva), run_time=self.dur(1.3))

            # «Una parábola que»
            self.en("unaparab")
            self.resaltar(par.curva, color=AMBAR)

            # «nunca baja de cero»
            self.en("nobaja")
            self.play(par.curva.animate.set_color(VERDE), run_time=self.dur(0.6))

            # «el discriminante menor o igual que cero»
            self.en("discr")
            self.play(FadeIn(pmin), FadeIn(disc), run_time=self.dur(0.6))

            # «De ahí salía todo»
            self.en("todo")
            self.resaltar(F0, color=AMBAR)

        self.wait(1.0)
        self.limpiar()
