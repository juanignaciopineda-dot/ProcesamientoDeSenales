"""Escena 15 — La parábola de Cauchy-Schwarz, por cuarta vez: capítulos 7, 10, 11 y 13."""
from comun.escena import *

POS = [(-4.7, 2.5), (-4.7, -0.7), (4.7, 2.5), (4.7, -0.7)]
TEXTOS = ["capítulo 7", "capítulo 10", "capítulo 11", "capítulo 13"]


class LaCuartaParabola(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        cs = etiqueta("Cauchy-Schwarz", AMBAR, 0.7, BOLD).move_to([0, 3.4, 0])
        par = parabola_l(centro=(0, 0.6), ancho=4.6, alto=3.0, fondo=0.25, color=AMBAR)
        cards = [caja(TEXTOS[i], INK, ancho=3.8, alto=0.8, scale=0.55).move_to([POS[i][0], POS[i][1], 0]) for i in range(4)]
        rho = MathTex(r"|\rho|\le 1", color=SENAL).scale(1.2).move_to([-4.7, 1.45, 0])
        term = termometro(1.0).move_to([-4.7, -1.8, 0])
        cov = etiqueta("covarianza acotada", INK, 0.5).move_to([-4.7, 1.45 - 3.2, 0])
        coh = MathTex(r"\text{coherencia}\le 1", color=MEDIDA).scale(1.0).move_to([4.7, 1.45, 0])
        xe = MathTex(r"X\ge -E", color=AMBAR).scale(1.2).move_to([4.7, -1.5, 0])
        suma = MathTex(r"\sum(\cdots)^2\ \ge\ 0", color=VERDE).scale(1.1).move_to([0, -2.5, 0])
        with self.narrar("b1"):
            # «Un último vistazo»
            self.paso("vistazo", cs, t=0.6)
            # «La parábola de Cauchy-Schwarz»
            self.en("parabola")
            self.play(Create(par.eje), Create(par.curva), run_time=self.dur(1.0))
            # «cuatro veces»
            self.paso("cuatro", *cards, t=0.7)
            # «En el capítulo siete»
            self.en("cap7")
            self.resaltar(cards[0], color=AMBAR, run_time=0.5)
            # «rho no pasa de uno»
            self.paso("rho", rho, t=0.6)
            # «En el diez»
            self.en("cap10")
            self.resaltar(cards[1], color=AMBAR, run_time=0.5)
            # «la covarianza del sensor»
            self.paso("sensor", term, t=0.6)
            # «En el once»
            self.en("cap11")
            self.resaltar(cards[2], color=AMBAR, run_time=0.5)
            # «la coherencia»
            self.paso("coh", coh, t=0.6)
            # «Y aquí»
            self.en("aqui")
            self.resaltar(cards[3], color=AMBAR, run_time=0.5)
            # «el filtro adaptado»
            self.paso("adaptado", xe, t=0.6)
            # «una suma de cuadrados no puede ser negativa»
            self.en("suma")
            self.play(par.curva.animate.set_color(VERDE), FadeIn(suma), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
