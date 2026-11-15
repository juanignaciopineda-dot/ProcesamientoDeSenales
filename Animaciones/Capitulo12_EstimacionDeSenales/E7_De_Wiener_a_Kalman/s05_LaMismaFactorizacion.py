"""Escena 05 — El numerador en espacio de estados es el mismo de la factorización del E5."""
from comun.escena import *


class LaMismaFactorizacion(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        cx = -2.4
        t0 = etiqueta("numerador de la densidad de lo medido", INK, 0.5).move_to([cx, 3.3, 0])
        f1 = formula("r", "=", "\\frac{\\sigma_w^2}{\\sigma_v^2}", "=", "2{,}56", escala=0.9,
                     colores={0: AMBAR}).move_to([cx, 2.4, 0])
        f2 = formula("2{,}56", "+", "a(z)\\,a(z^{-1})", escala=0.9, colores={2: AMBAR}).move_to([cx, 1.2, 0])
        f3 = formula("a(z)", "=", "z-0{,}6", escala=0.9, colores={0: AMBAR}).move_to([cx, 0.1, 0])
        f4 = formula("a(z)\\,a(z^{-1})", "=", "1{,}36-0{,}6\\,(z+z^{-1})", escala=0.85).move_to([cx, -0.9, 0])
        f5 = formula("3{,}92", "-", "0{,}6", "\\,(z+z^{-1})", escala=1.0, colores={0: AMBAR}).move_to([cx, -2.2, 0])
        suma = MathTex("2{,}56+1{,}36=3{,}92", color=INK).scale(0.6).move_to([cx, -1.55, 0])
        aq = etiqueta("episodio 5", INK, 0.42).move_to([4.3, -1.6, 0])
        f6 = formula("3{,}92", "-", "0{,}6", "\\,(z+z^{-1})", escala=0.85).move_to([4.3, -2.3, 0])
        eq = MathTex("=", color=VERDE).scale(1.0).move_to([1.35, -2.25, 0])
        al = formula("\\alpha(z)", "=", "z-0{,}157", escala=1.0, colores={0: ESTIMACION}).move_to([4.3, 2.4, 0])
        recta = Line([2.7, 0.9, 0], [6.0, 0.9, 0], color=INK, stroke_width=2)
        cero = Dot([2.7 + 3.3 * 0.157 / 0.6, 0.9, 0], radius=0.1, color=ESTIMACION)
        l157 = MathTex("0{,}157", color=ESTIMACION).scale(0.6).move_to([2.7 + 3.3 * 0.157 / 0.6, 0.45, 0])
        with self.narrar("b1"):
            # «En este lenguaje»
            self.en("lenguaje")
            self.play(FadeIn(t0), run_time=self.dur(0.5))
            # «es erre»
            self.en("erre")
            self.play(FadeIn(f1[0]), FadeIn(f1[1]), run_time=self.dur(0.4))
            # «el cociente entre la potencia de la moneda y la del ruido»
            self.en("cociente")
            self.play(FadeIn(f1[2]), run_time=self.dur(0.8))
            # «dos coma cinco seis»
            self.en("v256")
            self.play(FadeIn(f1[3]), FadeIn(f1[4]), run_time=self.dur(0.5))
            # «a de zeta por a de zeta a la menos uno»
            self.en("aa")
            self.play(FadeIn(f2), run_time=self.dur(0.8))
            # «zeta menos cero coma seis»
            self.en("az")
            self.play(FadeIn(f3), run_time=self.dur(0.5))
            self.play(FadeIn(f4), run_time=self.dur(0.8))
            # «tres coma nueve dos»
            self.en("resultado")
            self.play(FadeIn(suma), FadeIn(f5[0]), run_time=self.dur(0.6))
            # «menos cero coma seis por zeta»
            self.en("menoszeta")
            self.play(FadeIn(f5[1]), FadeIn(f5[2]), FadeIn(f5[3]), run_time=self.dur(0.6))
            # «el numerador del episodio quinto»
            self.en("igual")
            self.play(FadeIn(aq), FadeIn(f6), run_time=self.dur(0.6))
            self.play(FadeIn(eq), run_time=0.3)
            self.resaltar(f5, f6, color=VERDE, run_time=0.6)
            # «Y alfa de zeta»
            self.en("alfa")
            self.play(FadeIn(al), run_time=self.dur(0.6))
            # «zeta menos cero coma uno cinco siete»
            self.en("z157")
            self.play(Create(recta), FadeIn(cero), FadeIn(l157), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
