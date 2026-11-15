"""Escena 04 — El sensor de siempre escrito como un sistema de estados."""
from comun.escena import *


class ElSensorEnEstados(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        est = self.palabra("estado", AMBAR, 0.8).move_to([-4.6, 3.3, 0])
        f1 = formula("q[n+1]", "=", "0{,}6", "\\,q[n]", "+", "w[n]", escala=1.0,
                     colores={0: AMBAR, 2: AMBAR, 3: AMBAR, 5: RUIDO}).move_to([-1.5, 2.3, 0])
        mon = moneda("", RUIDO).scale(0.5).move_to([2.4, 2.3, 0])
        v256 = MathTex("\\sigma_w^2=2{,}56", color=RUIDO).scale(0.85).move_to([4.7, 2.3, 0])
        f2 = formula("y[n]", "=", "q[n]", escala=1.0, colores={0: SENAL, 2: AMBAR}).move_to([-3.6, 0.9, 0])
        f3 = formula("x[n]", "=", "y[n]", "+", "v[n]", escala=1.0,
                     colores={0: MEDIDA, 2: SENAL, 4: RUIDO}).move_to([-3.3, -0.4, 0])
        v1 = MathTex("\\sigma_v^2=1", color=RUIDO).scale(0.85).move_to([0.9, -0.4, 0])
        term = termometro(1.3).move_to([-5.9, -2.4, 0])
        siempre = etiqueta("el sensor de siempre", INK, 0.45).move_to([-3.6, -2.4, 0])
        cuatro = MathTex("\\sigma_y^2=4", color=SENAL).scale(0.95).move_to([0.6, -2.4, 0])
        esp = etiqueta("espectros", AZUL, 0.5).move_to([2.7, -1.3, 0])
        sta = etiqueta("estados", AMBAR, 0.5).move_to([5.7, -1.3, 0])
        dbl = DoubleArrow([3.6, -1.3, 0], [4.8, -1.3, 0], color=INK, stroke_width=3, buff=0,
                          max_tip_length_to_length_ratio=0.25)
        with self.narrar("b1"):
            # «El sensor es el estado»
            self.en("estado")
            self.pop(est)
            # «q de ene más uno»
            self.en("qsig")
            self.play(FadeIn(f1[0]), FadeIn(f1[1]), run_time=self.dur(0.5))
            # «cero coma seis por q de ene»
            self.en("seis")
            self.play(FadeIn(f1[2]), FadeIn(f1[3]), run_time=self.dur(0.6))
            # «la moneda w»
            self.en("moneda")
            self.play(FadeIn(f1[4]), FadeIn(f1[5]), FadeIn(mon), run_time=self.dur(0.6))
            # «de varianza dos coma cinco seis»
            self.en("var256")
            self.play(FadeIn(v256), run_time=self.dur(0.6))
            # «La temperatura, i griega»
            self.en("temp")
            self.play(FadeIn(f2), run_time=self.dur(0.6))
            # «lo medido»
            self.en("medido")
            self.play(FadeIn(f3[0]), FadeIn(f3[1]), FadeIn(f3[2]), run_time=self.dur(0.6))
            # «el ruido, de varianza uno»
            self.en("ruido")
            self.play(FadeIn(f3[3]), FadeIn(f3[4]), FadeIn(v1), run_time=self.dur(0.6))
            # «el sensor de siempre»
            self.en("siempre")
            self.play(FadeIn(term), FadeIn(siempre), run_time=self.dur(0.6))
            # «la varianza de la temperatura sigue siendo cuatro»
            self.en("cuatro")
            self.pop(cuatro)
            # «Lo que cambia»
            self.en("cambia")
            self.resaltar(cuatro, run_time=0.6)
            # «la manera de describirlo»
            self.en("describir")
            self.play(FadeIn(esp), GrowArrow(dbl), FadeIn(sta), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
