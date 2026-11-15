"""Escena 07 — El observador con G = 0,443 es el predictor del E6; lo mismo vale en general."""
from comun.escena import *

PRED = ("H(z)", "=", "0{,}443\\,z^{-1}", "\\Big/", "(1-0{,}157\\,z^{-1})")


class ElObservadorEsElFiltro(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.numeros()
        self.wait(0.6)
        self.general()
        self.wait(1.0)
        self.limpiar()

    def numeros(self):
        g = formula("G", "=", "0{,}443", escala=0.8, colores={0: ESTIMACION}).move_to([0, 3.5, 0])
        rec = formula("\\hat q[n+1]", "=", "0{,}157", "\\,\\hat q[n]", "+", "0{,}443", "\\,x[n]", escala=0.95,
                      colores={0: ESTIMACION, 2: AMBAR, 5: AMBAR}).move_to([0, 2.4, 0])
        fl = Arrow([0, 1.75, 0], [0, 1.25, 0], color=INK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.3)
        H = formula(*PRED, escala=1.0, colores={2: AMBAR, 4: AMBAR}).move_to([0, 0.8, 0])
        ret = Underline(H[2], color=AMBAR, buff=0.12, stroke_width=4)
        etq = etiqueta("predictor del episodio anterior", INK, 0.45).move_to([0, -0.0, 0])
        H2 = formula(*PRED, escala=1.0, colores={2: AMBAR, 4: AMBAR}).move_to([0, -0.7, 0])
        cob = caja("observador", AMBAR, ancho=3.0, alto=0.8, scale=0.5).move_to([-2.6, -2.5, 0])
        cwi = caja("Wiener causal", AZUL, ancho=3.0, alto=0.8, scale=0.5).move_to([2.6, -2.5, 0])
        eq = MathTex("=", color=VERDE).scale(1.1).move_to([0, -2.5, 0])
        with self.narrar("b1"):
            # «Con esa ganancia»
            self.en("gan")
            self.play(FadeIn(g), run_time=self.dur(0.5))
            # «cero coma uno cinco siete por su valor anterior»
            self.en("p157")
            self.play(FadeIn(rec[0]), FadeIn(rec[1]), FadeIn(rec[2]), FadeIn(rec[3]), run_time=self.dur(0.9))
            # «cero coma cuatro cuatro tres por lo que llega»
            self.en("p443")
            self.play(FadeIn(rec[4]), FadeIn(rec[5]), FadeIn(rec[6]), run_time=self.dur(0.9))
            # «Su transferencia»
            self.en("transf")
            self.play(GrowArrow(fl), FadeIn(H[0]), FadeIn(H[1]), run_time=self.dur(0.6))
            # «cero coma cuatro cuatro tres, zeta a la menos uno»
            self.en("num")
            self.play(FadeIn(H[2]), run_time=self.dur(0.7))
            # «entre uno menos cero coma uno cinco siete»
            self.en("den")
            self.play(FadeIn(H[3]), FadeIn(H[4]), run_time=self.dur(0.8))
            # «a la menos uno»
            self.en("retardo")
            self.play(Create(ret), run_time=self.dur(0.5))
            # «los números del predictor»
            self.en("predictor")
            self.play(FadeIn(etq), FadeIn(H2, shift=UP * 0.3), run_time=self.dur(0.8))
            self.resaltar(H, H2, run_time=0.6)
            # «El observador y el filtro de Wiener»
            self.en("obswie")
            self.play(FadeIn(cob), FadeIn(cwi), run_time=self.dur(0.6))
            # «el mismo filtro»
            self.en("mismo")
            self.play(FadeIn(eq), run_time=0.3)
            self.resaltar(cob, cwi, color=VERDE, run_time=0.6)

    def general(self):
        self.corte()
        cas = etiqueta("¿casualidad?", INK, 0.7).move_to([-2.4, 3.3, 0])
        tac = tachar(cas)
        gen = etiqueta("en general", AMBAR, 0.55, BOLD).move_to([-5.2, 2.4, 0])
        pol_l = etiqueta("polinomio del observador:", INK, 0.5).move_to([-2.0, 2.4, 0])
        pol = MathTex("\\alpha(z)", color=ESTIMACION).scale(0.9).next_to(pol_l, RIGHT, buff=0.25)
        h1 = formula("H", "=", "\\frac{\\alpha(z)-a(z)}{\\alpha(z)}", escala=1.1, colores={0: ESTIMACION}
                     ).move_to([-1.6, 0.8, 0])
        h2 = formula("H", "=", "\\big[(z-0{,}157)-(z-0{,}6)\\big]", "\\Big/", "(z-0{,}157)", escala=0.85,
                     colores={0: ESTIMACION}).move_to([-1.6, -0.7, 0])
        h3 = formula("H", "=", "0{,}443", "\\Big/", "(z-0{,}157)", escala=1.0,
                     colores={0: ESTIMACION, 2: AMBAR}).move_to([-1.6, -2.1, 0])
        wc = caja("Wiener causal", AZUL, ancho=2.8, alto=0.8, scale=0.48).move_to([5.2, 2.2, 0])
        ob = caja("observador", AMBAR, ancho=2.8, alto=0.8, scale=0.48).move_to([5.2, 0.7, 0])
        ar = flecha([5.2, 1.75, 0], [5.2, 1.15, 0])
        esp = etiqueta("predictor", AMBAR, 0.55, BOLD).move_to([5.2, -0.6, 0])
        xn = MathTex("x[n]", color=MEDIDA).scale(0.9).move_to([5.2, -1.7, 0])
        tx = tachar(xn)
        with self.narrar("b2"):
            # «No es una casualidad»
            self.en("casual")
            self.play(FadeIn(cas), run_time=0.3)
            self.play(Create(tx if False else tac), run_time=0.4)
            # «En general»
            self.en("general")
            self.play(FadeIn(gen), run_time=self.dur(0.5))
            # «el polinomio del observador sea alfa de zeta»
            self.en("polialfa")
            self.play(FadeIn(pol_l), FadeIn(pol), run_time=self.dur(0.7))
            # «la transferencia es alfa menos a, entre alfa»
            self.en("hobs")
            self.play(FadeIn(h1), run_time=self.dur(1.0))
            # «Con nuestros números»
            self.en("nuestros")
            self.play(FadeIn(h2), run_time=self.dur(1.0))
            # «menos zeta más cero coma seis»
            self.en("restaz")
            self.resaltar(h2[2], color=AMBAR, run_time=0.6)
            # «cero coma cuatro cuatro tres»
            self.en("r443")
            self.play(FadeIn(h3), run_time=self.dur(0.7))
            # «El filtro de Wiener causal»
            self.en("wcausal")
            self.play(FadeIn(wc), run_time=self.dur(0.5))
            # «se implementa como un observador»
            self.en("impl")
            self.play(GrowArrow(ar), FadeIn(ob), run_time=self.dur(0.7))
            # «es el predictor»
            self.en("esp")
            self.pop(esp)
            # «no usa la muestra de ahora»
            self.en("nousa")
            self.play(FadeIn(xn), run_time=0.3)
            self.play(Create(tx), run_time=0.4)
