"""Escena 05 — De una medición a una señal entera: la sorpresa del episodio."""
from comun.escena import *


class UnaSenalEntera(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        T = TablaDecision(centro=(0.8, -0.6), lado=2.2)
        etq9 = etiqueta("Capítulo 9 · Pruebas de hipótesis", AMBAR, 0.9, BOLD).move_to([0.8, 3.3, 0])
        R = RectaR(centro=(0, 0), ancho=9.0, x_rango=(-1.5, 1.5))
        punto = Dot(R.p(0.4), radius=0.2, color=MEDIDA)
        r_et = MathTex("r", color=MEDIDA).scale(1.2).next_to(punto, UP, buff=0.2)
        x_roja = cruz(ROJO, 1.6).move_to(punto.get_center())

        vals = [1.4, 2.3, 0.8, 1.9, 2.6, 1.1, 2.0, 0.9, 1.7, 2.4]
        barras = barras_senal(vals, centro=(0, -1.2), ancho=0.7, hueco=0.25, unidad=0.95, color=MEDIDA)
        primeras = VGroup(barras.base, *barras.barras[:3])
        resto = VGroup(*barras.barras[3:])
        signo = Text("!", color=AMBAR, weight=BOLD).scale(3.0).move_to([0, 2.6, 0])
        mas = Text("más datos", color=TXT, weight=BOLD).scale(1.1)
        mejor = Text("mejor decisión", color=INK, weight=BOLD).scale(1.1)
        par = VGroup(mas, mejor).arrange(RIGHT, buff=0.7).move_to([0, -2.9, 0])
        tach = tachar(mejor)
        regla = caja("regla de decisión", AMBAR, ancho=6.8, alto=1.4, scale=1.0).move_to([0, 2.9, 0])

        with self.narrar("b1"):
            # «el capítulo de pruebas de hipótesis»
            self.en("cap9")
            self.play(FadeIn(T.cel[(0, 0)]), FadeIn(T.cel[(0, 1)]), FadeIn(T.cel[(1, 0)]), FadeIn(T.cel[(1, 1)]),
                      FadeIn(T.enc), FadeIn(etq9), run_time=self.dur(0.8))

            # «una única medición»
            self.en("una")
            self.corte()
            self.play(FadeIn(R), FadeIn(punto), FadeIn(r_et), run_time=self.dur(0.5))

            # «un radar no oye un número»
            self.en("nonum")
            self.play(FadeIn(x_roja, scale=0.5), run_time=self.dur(0.4))

            # «una señal entera»
            self.en("entera")
            self.corte()
            self.play(FadeIn(primeras, lag_ratio=0.3), run_time=self.dur(0.8))

            # «muchas muestras seguidas»
            self.en("muchas")
            self.play(FadeIn(resto, lag_ratio=0.15), run_time=self.dur(1.0))

            # «una sorpresa»
            self.en("sorpresa")
            self.pop(signo)

            # «tener más datos no basta»
            self.en("nobasta")
            self.play(FadeIn(par), run_time=self.dur(0.5))
            self.play(Create(tach), run_time=self.dur(0.4))

            # «la regla de decisión»
            self.en("regla")
            self.play(FadeOut(signo), run_time=0.2)
            self.pop(regla)

            # «un ejemplo muy pequeño»
            self.en("pequeno")
            self.play(FadeOut(barras), FadeOut(par), FadeOut(tach), run_time=self.dur(0.4))
            h0 = VGroup(RoundedRectangle(corner_radius=0.12, width=2.0, height=1.3, color=RUIDO, stroke_width=3,
                                         fill_color=RUIDO, fill_opacity=0.12),
                        MathTex("H_0", color=RUIDO).scale(1.2))
            h1 = VGroup(RoundedRectangle(corner_radius=0.12, width=2.0, height=1.3, color=SENAL, stroke_width=3,
                                         fill_color=SENAL, fill_opacity=0.12),
                        MathTex("H_1", color=SENAL).scale(1.2))
            VGroup(h0, h1).arrange(RIGHT, buff=1.0).move_to([0, -1.6, 0])
            R2 = RectaR(centro=(0, 0.6), ancho=8.0, x_rango=(-1.5, 1.5))
            p2 = Dot(R2.p(0.4), radius=0.18, color=MEDIDA)
            self.play(FadeIn(R2), FadeIn(p2), FadeIn(h0), FadeIn(h1), run_time=self.dur(0.6))
        self.wait(0.5)
        self.limpiar()
