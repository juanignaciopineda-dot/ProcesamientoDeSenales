"""Escena 04 — La esperanza del dado calculada a mano: valor por probabilidad."""
from comun.escena import *


class CuentaDeLaEsperanza(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        d = dado_n(5).scale(0.9).move_to([-6.0, 3.0, 0])
        R = Regla7(centro=(0, 2.3), ancho=9.0, rotulos=False)
        caras = caras7(R, escala=0.7, altura=0.9)
        probs = VGroup(*[MathTex(r"\tfrac16", color=ESTIMACION).scale(0.8).move_to(R.p(v) + DOWN * 0.55)
                         for v in range(1, 7)])
        mas = VGroup(*[Text("+", color=TXT, weight=BOLD).scale(0.6).move_to((R.p(v) + R.p(v + 1)) / 2 + DOWN * 0.55)
                       for v in range(1, 6)])
        F = MathTex(r"1\cdot\tfrac16", "+", r"2\cdot\tfrac16", r"+\cdots+", r"6\cdot\tfrac16",
                    color=TXT).scale(1.1).move_to([0, 0.3, 0])
        suma_enteros = MathTex(r"\frac{1+2+3+4+5+6}{6}", color=TXT).scale(1.1).move_to([0, -1.0, 0])
        res = MathTex(r"\frac{21}{6}", "=", r"3{,}5", color=TXT).scale(1.1).move_to([0, -2.2, 0])
        res[2].set_color(VERDE)
        G = MathTex("E[X]", "=", r"\sum", "x", r"\cdot", "P(X=x)", color=TXT).scale(1.1).move_to([0, -3.3, 0])
        G[0].set_color(AMBAR)
        with self.narrar("b1"):
            # «sin tirar el dado»
            self.en("sin_tirar")
            self.play(FadeIn(d), run_time=0.3)
            self.play(Create(tachar(d)), run_time=self.dur(0.5))

            # «Cada valor»
            self.en("valor")
            self.play(FadeIn(R), FadeIn(caras), run_time=self.dur(0.7))

            # «por su probabilidad»
            self.en("prob")
            self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in probs], lag_ratio=0.1), run_time=self.dur(0.9))

            # «y se suma todo»
            self.en("suma")
            self.play(FadeIn(mas), run_time=self.dur(0.5))

            # «Uno por un sexto»
            self.en("t1")
            self.play(FadeIn(F[0], shift=DOWN * 0.15), run_time=self.dur(0.6))
            # «más dos por un sexto»
            self.en("t2")
            self.play(FadeIn(F[1:3], shift=DOWN * 0.15), run_time=self.dur(0.6))
            # «hasta seis por un sexto»
            self.en("t6")
            self.play(FadeIn(F[3:], shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «Uno más dos más tres»
            self.en("enteros")
            self.play(FadeIn(suma_enteros, shift=DOWN * 0.15), run_time=self.dur(1.2))

            # «son veintiuno»
            self.en("veintiuno")
            self.play(FadeIn(res[0], shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «da tres coma cinco»
            self.en("resultado")
            self.play(FadeIn(res[1:], shift=DOWN * 0.15), run_time=self.dur(0.6))
            self.sfx("exito")

            # «En general»
            self.en("general")
            self.play(FadeIn(G[0:2], shift=DOWN * 0.15), run_time=self.dur(0.6))
            # «la suma de cada valor»
            self.en("sumatoria")
            self.play(FadeIn(G[2:4], shift=DOWN * 0.15), run_time=self.dur(0.6))
            # «por su probabilidad»
            self.en("prob2")
            self.play(FadeIn(G[4:], shift=DOWN * 0.15), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
