"""Escena 16 — Primer paso: blanquear; la cruzada con una señal filtrada se multiplica por el conjugado de la respuesta."""
from comun.escena import *


class PrimerPasoBlanquear(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        tc = tres_casillas(centro=(0, 3.3))
        for c in tc.casillas:
            c.save_state()
            c.fade(0.65)
        bq = BloqueLTI(r"\frac{1}{F}", centro=(-1.0, 1.2), ancho=1.8, alto=1.1, color=CIAN, largo=1.8, escala=0.9)
        lx = MathTex("x", color=MEDIDA).scale(0.9).move_to([-6.0, 1.2, 0])
        leps = MathTex(r"\varepsilon", color=TXT).scale(1.0).move_to([2.2, 1.2, 0])
        interr = self.palabra("?", AMBAR, 1.0).move_to([0, -0.5, 0])
        ly = MathTex("y", color=SENAL).scale(1.0).move_to([-3.2, -0.5, 0])
        leps2 = MathTex(r"\varepsilon", color=TXT).scale(1.0).move_to([3.2, -0.5, 0])
        regla = caja("regla", INK, ancho=1.6, alto=0.6, scale=0.45).move_to([-6.0, -1.9, 0])
        fr = oculta(formula(r"S_{y\,\text{filtrada}}", r"\times", r"H^{*}", escala=1.0,
                            colores={0: SENAL, 2: AMBAR})).move_to([0, -1.9, 0])
        self.add(fr)
        fc = oculta(formula(r"\left(\frac{1}{F}\right)^{*}", "=", r"\frac{1}{F(z^{-1})}", escala=1.0,
                            colores={0: CIAN, 2: CIAN})).move_to([0, -3.1, 0])
        self.add(fc)
        with self.narrar("b1"):
            # «tres pasos»
            self.en("tres")
            self.play(FadeIn(tc), run_time=self.dur(0.7))

            # «Primer paso»
            self.en("p1")
            self.play(Restore(tc.casillas[0]), run_time=self.dur(0.5))

            # «blanquear lo medido con uno entre F»
            self.en("bl")
            self.play(FadeIn(lx), FadeIn(bq), FadeIn(leps), run_time=self.dur(1.0))

            # «Necesitamos saber»
            self.en("necesitamos")
            self.pop(interr, sonido=None)

            # «la señal que buscamos, i griega»
            self.en("y")
            self.play(FadeIn(ly, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «la señal blanqueada»
            self.en("bla")
            self.play(FadeIn(leps2, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «La regla»
            self.en("regla")
            self.play(FadeIn(regla), run_time=self.dur(0.4))

            # «la densidad cruzada con una señal filtrada»
            self.en("cruz")
            self.play(*revelar(fr[0]), run_time=self.dur(0.7))

            # «se multiplica por el conjugado»
            self.en("mult")
            self.play(*revelar(fr[1]), run_time=self.dur(0.4))

            # «de la respuesta del filtro»
            self.en("resp")
            self.play(*revelar(fr[2]), run_time=self.dur(0.5))

            # «el conjugado de uno entre F»
            self.en("conj")
            self.play(*revelar(fc[0]), run_time=self.dur(0.7))

            # «uno entre F de zeta a la menos uno»
            self.en("res")
            self.play(*revelar(fc[1], fc[2]), run_time=self.dur(0.8))
            self.sfx("exito", gain=-18)

        self.wait(1.0)
        self.limpiar()
