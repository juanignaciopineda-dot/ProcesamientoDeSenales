"""Escena 18 — Tercer paso: deshacer el blanqueo; la fórmula completa del filtro de Wiener causal."""
from comun.escena import *


class TercerPasoDeshacer(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        tc = tres_casillas(centro=(0, 3.3))
        tc.casillas[2].save_state()
        tc.casillas[2].fade(0.65)
        bq = BloqueLTI("F", centro=(-0.2, 1.3), ancho=1.6, alto=1.1, color=VERDE, largo=1.8, escala=0.9)
        leps = MathTex(r"\varepsilon", color=TXT).scale(1.0).move_to([-3.1, 1.3, 0])
        lyh = MathTex(r"\hat y", color=ESTIMACION).scale(1.0).move_to([2.9, 1.3, 0])
        lmul = formula(r"\times\,\frac{1}{F}", escala=0.9, colores={0: VERDE}).move_to([-0.2, 0.05, 0])
        fh = oculta(formula("H(z)", "=", r"\frac{1}{\sigma^2 F(z)}", r"\bigg[", r"\frac{S_{yx}(z)}{F(z^{-1})}",
                            r"\bigg]_{+}", escala=1.3,
                            colores={0: ESTIMACION, 2: COLOR_PASO[3], 3: COLOR_PASO[2], 4: COLOR_PASO[1],
                                     5: COLOR_PASO[2]}))
        fh.move_to([0, -1.3, 0])
        self.add(fh)
        der = Arrow([4.6, -2.7, 0], [-4.6, -2.7, 0], color=INK, stroke_width=3, buff=0)
        sel = sello("filtro de Wiener causal", AMBAR).scale(0.9).move_to([0, -3.5, 0])
        with self.narrar("b1"):
            # «Tercer paso»
            self.en("p3")
            self.play(FadeIn(tc), run_time=self.dur(0.4))
            self.play(Restore(tc.casillas[2]), run_time=self.dur(0.4))

            # «deshacer el blanqueo»
            self.en("deshacer")
            self.play(FadeIn(bq), FadeIn(leps), FadeIn(lyh), run_time=self.dur(0.8))

            # «multiplicando por uno entre F»
            self.en("mult")
            self.play(FadeIn(lmul, shift=UP * 0.1), run_time=self.dur(0.5))

            # «El filtro completo»
            self.en("completo")
            self.play(*revelar(fh[0], fh[1]), run_time=self.dur(0.5))

            # «uno entre sigma cuadrado por F de zeta»
            self.en("pizq")
            self.play(*revelar(fh[2]), run_time=self.dur(0.8))

            # «la parte causal de la cruzada»
            self.en("pc")
            self.play(*revelar(fh[3], fh[5]), run_time=self.dur(0.6))

            # «dividida entre F de zeta a la menos uno»
            self.en("div")
            self.play(*revelar(fh[4]), run_time=self.dur(0.8))

            # «de derecha a izquierda»
            self.en("der")
            self.play(GrowArrow(der), run_time=self.dur(0.9))

            # «blanquear, quedarse con lo causal y deshacer»
            self.en("tresp")
            for i, k in ((4, 0), (3, 1), (2, 2)):
                self.play(fh[i].animate(rate_func=there_and_back).scale(1.12), tc.casillas[k].animate(
                    rate_func=there_and_back).scale(1.06), run_time=self.dur(0.5))

            # «Justo lo que anunciamos»
            self.en("anunc")
            self.pop(sel, sonido="impacto")

        self.wait(1.0)
        self.limpiar()
