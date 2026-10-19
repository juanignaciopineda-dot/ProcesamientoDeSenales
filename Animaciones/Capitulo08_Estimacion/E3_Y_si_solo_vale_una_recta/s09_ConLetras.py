"""Escena 09 — La mejor recta con letras: h = σ_xy / σ_x² y ŷ = μ_y + ρ (σ_y / σ_x)(x − μ_x)."""
from comun.escena import *


class ConLetras(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.pendiente_cero()
        self.la_recta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pendiente_cero(self):
        J = formula("J(h)", "=", r"\sigma_y^2", "-", r"2h\,\sigma_{xy}", "+", r"h^2\sigma_x^2", escala=1.2,
                    colores={0: ERROR, 2: SENAL, 6: MEDIDA}).move_to([-1.2, 2.7, 0])
        Jp = formula("J'(h)", "=", r"-2\sigma_{xy}", "+", r"2h\,\sigma_x^2", "=", "0", escala=1.2,
                     colores={0: ERROR}).move_to([-1.2, 1.2, 0])
        h = formula("h", "=", r"\frac{\sigma_{xy}}{\sigma_x^2}", escala=1.6, colores={0: ESTIMACION}).move_to([-2.2, -0.7, 0])
        marco = SurroundingRectangle(h, color=AMBAR, buff=0.2)
        termo = termometro(1.1, ROJO, 0.6).move_to([3.3, -0.7, 0])
        cuatro = MathTex(r"\frac{4}{5}", color=TXT).scale(1.1).move_to([4.6, -0.7, 0])
        r08 = MathTex(r"=0{,}8", color=AMBAR).scale(1.1).move_to([6.0, -0.7, 0])
        datos = MathTex(r"\sigma_{xy}=4,\;\sigma_x^2=5", color=INK).scale(0.7).move_to([4.8, -1.8, 0])

        with self.narrar("b1"):
            # «El error, centrado»
            self.en("j0")
            self.play(FadeIn(J[0]), FadeIn(J[1]), run_time=self.dur(0.4))

            # «la varianza de i griega»
            self.en("sy")
            self.play(FadeIn(J[2], shift=UP * 0.1), run_time=self.dur(0.4))

            # «menos dos hache por la covarianza»
            self.en("cov")
            self.play(FadeIn(J[3]), FadeIn(J[4], shift=UP * 0.1), run_time=self.dur(0.6))

            # «más hache al cuadrado por la varianza de equis»
            self.en("sx")
            self.play(FadeIn(J[5]), FadeIn(J[6], shift=UP * 0.1), run_time=self.dur(0.7))

            # «Su pendiente es»
            self.en("pend")
            self.play(FadeIn(Jp[0]), FadeIn(Jp[1]), run_time=self.dur(0.4))

            # «menos dos veces la covarianza»
            self.en("p1")
            self.play(FadeIn(Jp[2], shift=UP * 0.1), run_time=self.dur(0.5))

            # «más dos hache por la varianza de equis»
            self.en("p2")
            self.play(FadeIn(Jp[3]), FadeIn(Jp[4], shift=UP * 0.1), run_time=self.dur(0.7))

            # «Igualada a cero»
            self.en("cero")
            self.play(FadeIn(Jp[5]), FadeIn(Jp[6]), run_time=self.dur(0.5))

            # «hache es la covarianza dividida entre la varianza de equis»
            self.en("h")
            self.play(*[FadeIn(h[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.9))
            self.play(Create(marco), run_time=self.dur(0.4))

            # «En el termómetro, cuatro entre cinco»
            self.en("term")
            self.play(FadeIn(termo), run_time=self.dur(0.4))
            self.pop(cuatro)
            self.play(FadeIn(datos), run_time=self.dur(0.4))

            # «cero coma ocho»
            self.en("r08")
            self.pop(r08)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def la_recta(self):
        f = formula(r"\hat{y}", "=", r"\mu_y", "+", r"\frac{\sigma_{xy}}{\sigma_x^2}", "(", "x", "-", r"\mu_x", ")",
                    escala=1.4, colores={0: ESTIMACION, 2: SENAL, 6: MEDIDA, 8: MEDIDA}).move_to([0, 2.2, 0])
        rho = formula(r"\sigma_{xy}", "=", r"\rho\,\sigma_x\sigma_y", escala=1.4).move_to([0, 0.4, 0])
        f2 = formula(r"\frac{\sigma_{xy}}{\sigma_x^2}", "=", r"\rho", r"\frac{\sigma_y}{\sigma_x}", escala=1.4,
                     colores={2: AMBAR}).move_to([0, -1.5, 0])
        r_sig = SurroundingRectangle(f2[3], color=AMBAR, buff=0.1)
        final = formula(r"\hat{y}", "=", r"\mu_y", "+", r"\rho", r"\frac{\sigma_y}{\sigma_x}", "(", "x", "-",
                        r"\mu_x", ")", escala=1.2,
                        colores={0: ESTIMACION, 2: SENAL, 7: MEDIDA, 9: MEDIDA}).move_to([0, -3.2, 0])

        with self.narrar("b2"):
            # «la media de i griega»
            self.en("mu")
            self.corte()
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.7))

            # «más la covarianza entre la varianza de equis»
            self.en("fac")
            self.play(FadeIn(f[3]), FadeIn(f[4], shift=UP * 0.1), run_time=self.dur(0.8))

            # «por lo que equis se aparta de su media»
            self.en("xmu")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(5, 10)], run_time=self.dur(1.0))

            # «la covarianza es rho por las dos desviaciones típicas»
            self.en("rho")
            self.play(*[FadeIn(rho[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(1.0))

            # «el factor también se escribe»
            self.en("fac2")
            self.play(*[FadeIn(f2[i], shift=UP * 0.1) for i in range(4)], run_time=self.dur(1.0))

            # «sigma de i griega, entre sigma de equis»
            self.en("sigs")
            self.play(Create(r_sig), run_time=self.dur(0.4))
            self.play(FadeIn(final, shift=UP * 0.1), run_time=self.dur(0.8))
