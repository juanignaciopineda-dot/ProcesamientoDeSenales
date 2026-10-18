"""Escena 04 — Sobre un mismo experimento hay muchas variables: el dado y dos reglas."""
from comun.escena import *


class VariasReglas(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        d = dado().scale(1.8).move_to([-4.6, 0.0, 0])
        # regla 1: el número que sale (arriba a la derecha)
        r1 = RectaNum(0.5, 6.5, centro=(1.9, 2.5), ancho=6.0, marcas=[1, 2, 3, 4, 5, 6], tam=0.55)
        # regla 2: par o impar (abajo a la derecha)
        r2 = RectaNum(-0.5, 1.5, centro=(1.9, -2.0), ancho=4.0, marcas=[0, 1], tam=0.7)
        x1 = formula("X", escala=1.8, colores={0: AMBAR}).next_to(r1, RIGHT, buff=0.5).shift(UP * 0.1)
        x2 = formula("Y", escala=1.8, colores={0: VERDE}).next_to(r2, RIGHT, buff=0.5).shift(UP * 0.1)

        with self.narrar("b1"):
            self.en("muchas")                                 # «muchas variables»
            self.play(FadeIn(d, scale=0.8), run_time=self.dur(0.5))
            self.play(FadeIn(x1), FadeIn(x2), run_time=self.dur(0.4))
            self.en("numero")                                 # «el número que sale»
            self.play(FadeIn(r1), run_time=self.dur(0.5))
            flechas = VGroup(*[Arrow(d.get_right() + UP * 0.3, r1.p(k) + UP * 0.1, color=AMBAR, stroke_width=2.5,
                                     buff=0.1, max_tip_length_to_length_ratio=0.1) for k in range(1, 7)])
            self.play(LaggedStart(*[Create(f) for f in flechas], lag_ratio=0.12), run_time=self.dur(1.2))
            self.en("par")                                    # «valga uno si sale par»
            self.play(FadeOut(flechas), FadeIn(r2), run_time=self.dur(0.5))
            fpar = Arrow(d.get_right() + DOWN * 0.3, r2.p(1) + UP * 0.1, color=VERDE, stroke_width=4, buff=0.1)
            lab_par = etiqueta("2, 4, 6", VERDE, 0.65, BOLD).next_to(r2.p(1) + UP * 0.1, UP, buff=0.55)
            self.play(Create(fpar), FadeIn(lab_par), run_time=self.dur(0.7))
            self.en("impar")                                  # «cero si sale impar»
            fimp = Arrow(d.get_right() + DOWN * 0.6, r2.p(0) + UP * 0.1, color=INK, stroke_width=4, buff=0.1)
            lab_imp = etiqueta("1, 3, 5", INK, 0.65, BOLD).next_to(r2.p(0) + UP * 0.1, UP, buff=0.55)
            self.play(Create(fimp), FadeIn(lab_imp), run_time=self.dur(0.7))
            self.en("mismo")                                  # «El experimento es el mismo»
            self.play(d.animate(rate_func=there_and_back).scale(1.2), run_time=self.dur(0.7))
            self.en("pregunta")                               # «lo que cambia es la pregunta»
            self.play(x1.animate(rate_func=there_and_back).scale(1.3), x2.animate(rate_func=there_and_back).scale(1.3),
                      run_time=self.dur(0.9))
            self.en("por_eso")                                # «Por eso»
            self.play(d.animate.fade(0.55), run_time=self.dur(0.4))
            self.en("no_dado")                                # «no es el dado»
            tacha = cruz(ROJO, 1.4).move_to(d.get_center())
            self.play(Create(tacha), run_time=self.dur(0.5))
            self.en("leerlo")                                 # «una forma de leerlo»
            lu = lupa().scale(1.6).move_to(d.get_center() + RIGHT * 0.2 + UP * 0.1)
            self.play(FadeOut(tacha), FadeIn(lu, scale=0.7), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
