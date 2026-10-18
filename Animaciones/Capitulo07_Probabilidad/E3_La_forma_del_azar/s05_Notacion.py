"""Escena 05 — Notación: X mayúscula es la variable, x minúscula es un valor."""
from comun.escena import *


class Notacion(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        recta = RectaNum(0.4, 6.6, centro=(0, -2.0), ancho=9.0, marcas=[1, 2, 3, 4, 5, 6], tam=0.5)
        X = MathTex("X", color=AMBAR).scale(3.0).move_to([-3.6, 1.7, 0])
        x = MathTex("x", color=AMBAR).scale(2.4).move_to([3.6, 1.7, 0])
        regla_t = etiqueta("La regla", INK, 0.65).next_to(X, DOWN, buff=0.35)
        conc_t = etiqueta("Un valor concreto", INK, 0.65).next_to(x, DOWN, buff=0.35)
        d_aire = dado().scale(1.0).move_to([-3.6, -0.7, 0])
        interr = Text("?", color=ERROR, weight=BOLD).scale(1.0).next_to(d_aire, RIGHT, buff=0.3)

        with self.narrar("b1"):
            self.en("notacion")                               # «notación»
            nota_t = etiqueta("Notación", INK, 0.6).to_corner(UL, buff=0.45)
            self.play(FadeIn(nota_t), run_time=self.dur(0.5))
            self.en("mayus")                                  # «La equis mayúscula»
            self.pop(X)
            self.en("la_regla")                               # «la regla»
            self.play(FadeIn(regla_t), run_time=self.dur(0.4))
            self.en("no_ocurrio")                             # «todavía no ha ocurrido»
            self.play(FadeIn(d_aire, shift=DOWN * 0.3), FadeIn(interr), run_time=self.dur(0.6))
            self.en("minus")                                  # «La equis minúscula»
            self.pop(x)
            self.play(FadeIn(recta), run_time=self.dur(0.5))
            self.en("concreto")                               # «un número concreto»
            self.play(FadeIn(conc_t), run_time=self.dur(0.4))
            self.en("posibles")                               # «uno de los valores posibles»
            puntos = VGroup(*[Dot(recta.p(k) + UP * 0.0, radius=0.1, color=INK) for k in range(1, 7)])
            self.play(LaggedStart(*[FadeIn(p, scale=2) for p in puntos], lag_ratio=0.12), run_time=self.dur(0.9))
            self.en("x_cuatro")                               # «equis mayúscula igual a cuatro»
            f = formula("X", "=", "4", escala=1.6, colores={0: AMBAR}).move_to([0, 0.35, 0])
            self.play(FadeOut(interr), Write(f), run_time=self.dur(1.1))
            self.en("salido")                                 # «el experimento ha salido»
            self.play(d_aire.animate.shift(RIGHT * 2.0 + DOWN * 0.4), run_time=self.dur(0.7))
            self.en("valio")                                  # «ha valido cuatro»
            cuatro = dado_n(4).scale(1.0).move_to(d_aire.get_center())
            self.play(FadeOut(d_aire), FadeIn(cuatro), puntos[3].animate.set_color(AMBAR).scale(1.8),
                      run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
