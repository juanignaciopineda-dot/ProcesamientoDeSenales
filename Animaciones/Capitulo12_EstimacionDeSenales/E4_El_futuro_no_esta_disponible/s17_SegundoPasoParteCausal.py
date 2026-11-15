"""Escena 17 — Segundo paso: con la señal blanca, resolver sin restricción y cortar la parte de m < 0 (el corchete ₊)."""
from comun.escena import *


class SegundoPasoParteCausal(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        tc = tres_casillas(centro=(0, 3.3))
        tc.casillas[1].save_state()
        tc.casillas[2].save_state()
        tc.casillas[1].fade(0.65)
        tc.casillas[2].fade(0.65)
        f = oculta(formula(r"S_{y\varepsilon}", "=", "S_{yx}", "/", "F(z^{-1})", escala=1.2,
                           colores={0: SENAL, 2: SENAL})).move_to([-1.2, 1.8, 0])
        self.add(f)
        leps = MathTex(r"\varepsilon", color=TXT).scale(1.0).move_to([-6.2, 0.3, 0])
        tira = tira_blanca((1, -1, -1, 1, -1, 1), lado=0.5).move_to([-3.6, 0.3, 0])
        sec = Tallos([0.15, 0.35, 1.0, 0.5, 0.25, 0.12], centro=(3.4, 0.0), paso=0.75, unidad=1.3,
                     color=ESTIMACION, k0=-2, indices=True)
        tj = tijeras().scale(0.9).move_to([sec.x(1.5), 1.9, 0])
        tj.permitir_encima = True
        fc = formula(r"\bigg[", r"\frac{S_{yx}}{F(z^{-1})}", r"\bigg]_{+}", escala=1.2,
                     colores={0: AMBAR, 2: AMBAR}).move_to([-1.5, -1.9, 0])
        lpc = etiqueta("parte causal", AMBAR, 0.55).move_to([-1.5, -3.1, 0])
        marco = Rectangle(width=3.4, height=2.7, color=VERDE, stroke_width=4).set_fill(VERDE, 0.05)
        marco.move_to([(sec.x(2) + sec.x(5)) / 2, 0.6, 0])
        fm = formula(r"m\geq 0", escala=1.0, colores={0: AMBAR}).move_to([marco.get_center()[0], -1.3, 0])
        with self.narrar("b1"):
            # «La cruzada entre i griega y la innovación»
            self.en("cr1")
            self.play(FadeIn(tc), *revelar(f[0]), run_time=self.dur(0.7))

            # «la cruzada entre i griega y equis»
            self.en("cr2")
            self.play(*revelar(f[1], f[2]), run_time=self.dur(0.6))

            # «dividida entre F de zeta a la menos uno»
            self.en("div")
            self.play(*revelar(f[3], f[4]), run_time=self.dur(0.7))

            # «Segundo paso»
            self.en("p2")
            self.play(Restore(tc.casillas[1]), run_time=self.dur(0.5))

            # «con la señal blanca»
            self.en("blanca")
            self.play(FadeIn(leps), FadeIn(tira), run_time=self.dur(0.6))

            # «calcular la solución sin restricción»
            self.en("sinres")
            self.play(FadeIn(sec), run_time=self.dur(0.9))

            # «cortar la parte de eme negativo»
            self.en("corta")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))
            self.play(sec.palito(0).animate.fade(0.8), sec.palito(1).animate.fade(0.8), FadeOut(tj),
                      run_time=self.dur(0.6))

            # «un corchete más»
            self.en("corch")
            self.play(FadeIn(fc, shift=UP * 0.15), run_time=self.dur(0.8))

            # «la parte causal»
            self.en("pcausal")
            self.play(FadeIn(lpc), run_time=self.dur(0.4))

            # «las posiciones cero y positivas»
            self.en("pos")
            self.play(Create(marco), FadeIn(fm), run_time=self.dur(0.6))
            self.sfx("exito", gain=-18)

        self.wait(1.0)
        self.limpiar()
