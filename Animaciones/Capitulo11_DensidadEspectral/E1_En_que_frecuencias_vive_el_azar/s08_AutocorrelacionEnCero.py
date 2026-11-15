"""Escena 08 — La potencia esperada es la autocorrelación en cero."""
from comun.escena import *


class AutocorrelacionEnCero(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        L1 = Lienzo(ancho=9.0, alto=1.3, t_rango=(0, 6), v_max=1.4, centro=(-0.8, 1.0))
        L2 = Lienzo(ancho=9.0, alto=1.3, t_rango=(0, 6), v_max=1.4, centro=(-0.8, -0.6))
        senal = onda_tel(L1, color=SENAL, ancho=3.5)
        tau = 0.8
        copia = onda_tel(L2, tiempos=[t + tau for t in CAMBIOS], color=AMBAR, ancho=3.5)
        desplaza = float(L2.x(tau) - L2.x(0))
        F = formula("E", "[", "x^2(t)", "]", "=", "?", escala=1.1).move_to([-3.0, 3.3, 0])
        R = MathTex("R_{xx}(\\tau)", "=", "E[", "x(t)", "\\,x(t-\\tau)", "]", color=TXT).scale(1.0).move_to([0, -2.4, 0])
        Rfin = MathTex("R_{xx}(0)", "=", "E[x^2(t)]", color=TXT).scale(1.1).move_to([0, -3.5, 0])
        Rfin[0].set_color(AMBAR)
        with self.narrar("b1"):
            # «ya tiene nombre»
            self.en("nombre")
            self.play(FadeIn(F), run_time=self.dur(0.6))

            # «la autocorrelación»
            self.en("auto")
            pal = self.palabra("autocorrelación", AMBAR, 0.8).move_to([3.6, 3.3, 0])
            self.pop(pal)
            self.play(FadeIn(R[0]), run_time=0.4)

            # «una copia desplazada un tiempo tau»
            self.en("copia")
            self.play(Create(L1.base()), Create(senal), run_time=self.dur(0.6), rate_func=linear)
            self.play(Create(L2.base()), Create(copia), run_time=self.dur(0.9), rate_func=linear)

            # «las multiplicas y promedias»
            self.en("mult")
            self.play(FadeIn(R[1:3]), run_time=self.dur(0.5))
            self.play(FadeIn(R[3]), FadeIn(R[4]), run_time=self.dur(0.6))
            self.play(FadeIn(R[5]), run_time=0.3)

            # «cuánto se parece la señal a sí misma»
            self.en("parece")
            q = self.palabra("¿se parece?", AMBAR, 0.6).move_to([5.5, 0.2, 0])
            self.pop(q)

            # «tau segundos después»
            self.en("despues")
            dt = DoubleArrow([float(L2.x(0.7)), -1.55, 0], [float(L2.x(0.7 + tau)), -1.55, 0], color=AMBAR,
                             stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.25)
            tt = formula(r"\tau", escala=0.8, color=AMBAR).move_to([float(L2.x(0.7 + tau / 2)), -1.95, 0])
            self.play(Create(dt), FadeIn(tt), run_time=self.dur(0.6))

            # «Con tau igual a cero»
            self.en("tau0")
            self.play(FadeOut(dt), FadeOut(tt), copia.animate.shift(LEFT * desplaza), run_time=self.dur(1.0))

            # «la copia coincide con la señal»
            self.en("coincide")
            self.resaltar(senal, copia, color=AMBAR)

            # «la esperanza de equis al cuadrado»
            self.en("igual")
            self.play(FadeIn(Rfin[0:2]), run_time=0.3)
            self.play(FadeIn(Rfin[2]), run_time=self.dur(0.6))

        self.wait(1.0)
        self.limpiar()
