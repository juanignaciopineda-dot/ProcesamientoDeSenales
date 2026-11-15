"""Escena 07 — El error entre dos señales: las dos campanas de g y la cuenta de Q(2,12)."""
from comun.escena import *

ESC = 0.36          # pantalla por unidad de g
Y0 = -1.5           # base de las campanas
S = 4.24 * ESC      # desvío en pantalla
ALTO = 2.2


class CuantoNosEquivocamos(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        pregunta = MathTex("P_e=?", color=ERROR).scale(1.2).move_to([-5.6, 3.3, 0])
        iguales = MathTex(r"p_0=p_1,\ E_0=E_1", color=AMBAR).scale(0.8).move_to([5.3, 3.3, 0])
        eje = Line([-6.6, Y0, 0], [6.6, Y0, 0], color=INK, stroke_width=2)
        g_rot = MathTex("g", color=INK).scale(0.8).move_to([6.7, Y0 + 0.3, 0])
        umbral = DashedLine([0, Y0 - 0.3, 0], [0, Y0 + 3.0, 0], color=AMBAR, stroke_width=3)
        t_umbral = etiqueta("umbral = 0", AMBAR, 0.5).move_to([0, Y0 - 0.65, 0])
        c1 = campana7(9 * ESC, Y0, S, ALTO, SENAL, k=2.4)
        c0 = campana7(-9 * ESC, Y0, S, ALTO, RUIDO, k=2.4)
        media = MathTex(r"E[g\mid H_1]", color=SENAL).scale(0.85).move_to([9 * ESC, Y0 + ALTO + 0.4, 0])
        prod = MathTex(r"s_1\cdot(s_1-s_0)=(2,2,1)\cdot(0,3,3)=9", color=TXT).scale(0.95).move_to([-0.5, 3.3, 0])
        m9 = VGroup(Dot([9 * ESC, Y0, 0], radius=0.09, color=SENAL),
                    MathTex("+9", color=SENAL).scale(0.8).move_to([9 * ESC, Y0 - 0.4, 0]))
        m0 = VGroup(Dot([-9 * ESC, Y0, 0], radius=0.09, color=RUIDO),
                    MathTex("-9", color=RUIDO).scale(0.8).move_to([-9 * ESC, Y0 - 0.4, 0]))
        desvio = MathTex(r"\sigma_g=4{,}24", color=MEDIDA).scale(0.9).move_to([0, 1.6, 0])
        res = formula(r"\frac{9}{4{,}24}", "=2{,}12", r"\ \Rightarrow\ ", "Q(2{,}12)", "=0{,}017", escala=1.2,
                      colores={0: MEDIDA, 3: ERROR, 4: ERROR}).move_to([0, -3.2, 0])
        cola1 = cola7(9 * ESC, Y0, S, ALTO, 9 * ESC - 2.4 * S, 0.0, ERROR, 0.5)
        cola0 = cola7(-9 * ESC, Y0, S, ALTO, 0.0, -9 * ESC + 2.4 * S, ERROR, 0.5)
        with self.narrar("b1"):
            # «¿Cuánto nos equivocamos?»
            self.paso("pregunta", pregunta, FadeIn(eje), FadeIn(g_rot), t=0.5)
            # «Con probabilidades y energías iguales»
            self.paso("iguales", iguales, t=0.5)
            # «el umbral es cero»
            self.paso("umbral", Create(umbral), FadeIn(t_umbral), t=0.5)
            # «Bajo la hipótesis uno»
            self.en("h1")
            self.play(Create(c1), run_time=self.dur(0.9))
            # «ge tiene media»
            self.paso("media", media, t=0.4)
            # «la señal uno por la diferencia»
            self.paso("producto", prod, t=0.8)
            # «nueve»
            self.en("nueve")
            self.pop(m9)
            # «Bajo la cero»
            self.en("h0")
            self.play(Create(c0), run_time=self.dur(0.9))
            # «menos nueve»
            self.en("menosnueve")
            self.pop(m0)
            # «desvío cuatro coma dos cuatro»
            self.paso("desvio", desvio, t=0.5)
            # «Nueve entre cuatro coma dos cuatro»
            self.paso("division", res[0], t=0.6)
            # «dos coma doce»
            self.paso("dos12", res[1], res[2], t=0.5)
            # «cu de dos coma doce»
            self.en("q")
            self.play(FadeIn(res[3]), FadeIn(cola1), FadeIn(cola0), run_time=self.dur(0.7))
            # «cero coma cero uno siete»
            self.en("valor")
            self.pop(res[4])
