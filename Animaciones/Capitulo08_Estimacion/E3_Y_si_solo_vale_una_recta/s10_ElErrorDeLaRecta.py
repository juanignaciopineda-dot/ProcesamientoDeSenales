"""Escena 10 — El error de la mejor recta: σ_y² (1 − ρ²), con el termómetro como comprobación."""
from comun.escena import *


class ElErrorDeLaRecta(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        # la columna del termómetro entra entera en su momento; las filas se construyen a la izquierda
        CX = -1.8
        r1 = formula("J", "=", r"\sigma_y^2", "-", r"2h\,\sigma_{xy}", "+", r"h^2\sigma_x^2", escala=1.1,
                     colores={0: ERROR, 2: SENAL}).move_to([CX, 3.0, 0])
        cap = MathTex(r"h=\sigma_{xy}/\sigma_x^2", color=INK).scale(0.7).move_to([CX, 2.2, 0])
        r2 = formula("J", "=", r"\sigma_y^2", "-", r"2\frac{\sigma_{xy}^2}{\sigma_x^2}", "+",
                     r"\frac{\sigma_{xy}^2}{\sigma_x^2}", escala=1.1, colores={0: ERROR, 2: SENAL}).move_to([CX, 1.0, 0])
        rect_u = SurroundingRectangle(VGroup(*[r2[i] for i in range(3, 7)]), color=AMBAR, buff=0.12)
        r3 = formula("J", "=", r"\sigma_y^2", "-", r"\frac{\sigma_{xy}^2}{\sigma_x^2}", escala=1.1,
                     colores={0: ERROR, 2: SENAL}).move_to([CX, -0.4, 0])
        rect_f = SurroundingRectangle(r3[2], color=AMBAR, buff=0.1)
        r4 = formula("J", "=", r"\sigma_y^2", "(", "1", "-", r"\rho^2", ")", escala=1.3,
                     colores={0: ERROR, 2: SENAL}).move_to([CX, -1.9, 0])
        caja_f = SurroundingRectangle(r4, color=ERROR, buff=0.2)
        t0 = Text("Termómetro", color=INK).scale(0.6).move_to([4.8, 2.7, 0])
        d_y = MathTex(r"\sigma_y^2=4", color=SENAL).scale(0.9).move_to([4.8, 1.8, 0])
        d_x = MathTex(r"\sigma_x^2=5", color=MEDIDA).scale(0.9).move_to([4.8, 1.1, 0])
        d_xy = MathTex(r"\sigma_{xy}=4", color=TXT).scale(0.9).move_to([4.8, 0.4, 0])
        rho2 = MathTex(r"\rho^2=\frac{4^2}{4\cdot5}=\frac{16}{20}=0{,}8", color=TXT).scale(0.85).move_to([4.8, -1.0, 0])
        cuenta = MathTex(r"4\,(1-0{,}8)=0{,}8", color=ERROR).scale(0.95).move_to([4.4, -2.3, 0])
        ok = tilde(VERDE, 0.6).move_to([6.6, -2.3, 0])

        with self.narrar("b1"):
            # «Falta el error»
            self.en("falta")
            self.play(*[FadeIn(r1[i], shift=UP * 0.1) for i in range(7)], run_time=self.dur(1.0))

            # «Metiendo ese hache»
            self.en("meter")
            self.play(FadeIn(cap), run_time=self.dur(0.4))
            self.play(*[FadeIn(r2[i], shift=UP * 0.1) for i in range(7)], run_time=self.dur(1.0))

            # «los dos últimos términos»
            self.en("ultimos")
            self.play(Create(rect_u), run_time=self.dur(0.6))

            # «menos la covarianza al cuadrado entre la varianza de equis»
            self.en("res")
            self.play(*[FadeIn(r3[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.0))

            # «entre la varianza de equis»
            self.en("entre")
            self.play(Indicate(r3[4], color=AMBAR), run_time=self.dur(0.8))

            # «Sacando factor común la varianza de i griega»
            self.en("factor")
            self.play(FadeOut(rect_u), Create(rect_f), run_time=self.dur(0.6))

            # «uno menos rho al cuadrado»
            self.en("final")
            self.play(FadeOut(rect_f), *[FadeIn(r4[i], shift=UP * 0.1) for i in range(8)], run_time=self.dur(1.0))
            self.play(Create(caja_f), run_time=self.dur(0.4))

            # «En el termómetro»
            self.en("term")
            self.play(FadeIn(t0), run_time=self.dur(0.3))
            self.play(LaggedStart(FadeIn(d_y), FadeIn(d_x), FadeIn(d_xy), lag_ratio=0.35), run_time=self.dur(1.2))

            # «dieciséis entre veinte»
            self.en("d16")
            self.play(FadeIn(rho2, shift=UP * 0.1), run_time=self.dur(1.0))

            # «cuatro por cero coma dos»
            self.en("cuenta")
            self.play(FadeIn(cuenta, shift=UP * 0.1), run_time=self.dur(0.9))

            # «Coincide»
            self.en("ok")
            self.pop(ok, sonido="exito")
        self.wait(1.0)
        self.limpiar()
