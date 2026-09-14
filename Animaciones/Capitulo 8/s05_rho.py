"""Escena 5 - El papel de rho: cuanto ayuda medir X.

LMMSE = sigma_Y^2 (1 - rho^2). Con rho = 0 medir X no sirve de nada y el
error queda en la varianza entera; con |rho| = 1 la relacion es exacta y
el error se va a cero.

    manim -pql s05_rho.py Correlacion
"""
from manim import *
import numpy as np
from comun import *

N = 230
SY = 1.0
_rng = np.random.default_rng(31)
Z1 = _rng.normal(0, 1, N)
Z2 = _rng.normal(0, 1, N)


def nube_rho(ax, rho, color=AZUL):
    """La misma semilla siempre: lo unico que cambia es rho."""
    ys = rho * Z1 + np.sqrt(max(0.0, 1 - rho ** 2)) * Z2
    return nube(ax, Z1, ys, color=color, radio=0.032, opacidad=0.55)


class Correlacion(Scene):
    def construct(self):
        configurar()

        tit = titulo("¿Cuánto sirve medir X? Todo depende de ρ")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        formula = MathTex(r"\text{LMMSE} \;=\; \sigma_Y^2\,\big(1-\rho^2\big)",
                          color=TXT).scale(0.82)
        formula.next_to(tit, DOWN, buff=0.4)
        self.play(Write(formula))
        self.wait(1.2)
        self.play(formula.animate.scale(0.78).to_edge(UP, buff=1.2))

        # ------------------------------------------------ la nube
        ax, lab = ejes([-3.2, 3.2, 3.2], [-3.2, 3.2, 3.2], ancho=5.0, alto=4.0,
                       x_label="x", y_label="y")
        ax.shift(LEFT * 3.1 + DOWN * 0.6)
        lab[0].next_to(ax.x_axis.get_end(), DR, buff=0.1)
        lab[1].next_to(ax.y_axis.get_end(), UR, buff=0.08)

        rho = ValueTracker(0.0)
        puntos = always_redraw(lambda: nube_rho(ax, rho.get_value()))
        recta = always_redraw(lambda: ax.plot(
            lambda x: rho.get_value() * x, x_range=[-3.2, 3.2],
            color=VERDE, stroke_width=4.5))

        self.play(Create(ax), FadeIn(lab))
        self.play(FadeIn(puntos), Create(recta))
        self.wait(0.5)

        # ------------------------------------------------ las barras
        H = 3.0
        marco_var = medidor(alto_max=H, ancho=0.55)
        marco_var.shift(RIGHT * 1.35 + DOWN * 0.6)
        lleno_var = relleno_medidor(marco_var, 1.0, color=AZUL)
        lbl_var = MathTex(r"\sigma_Y^2", color=AZUL).scale(0.6)
        lbl_var.next_to(marco_var, UP, buff=0.2)
        nota_var = nota("sin medir", scale=0.4).next_to(marco_var, DOWN, buff=0.2)

        marco_err = medidor(alto_max=H, ancho=0.55)
        marco_err.shift(RIGHT * 3.1 + DOWN * 0.6)
        lleno_err = always_redraw(lambda: relleno_medidor(
            marco_err, 1 - rho.get_value() ** 2, color=ROJO))
        lbl_err = MathTex(r"\text{LMMSE}", color=ROJO).scale(0.5)
        lbl_err.next_to(marco_err, UP, buff=0.2)
        nota_err = nota("midiendo X", scale=0.4).next_to(marco_err, DOWN, buff=0.2)

        self.play(FadeIn(VGroup(marco_var, lleno_var, lbl_var, nota_var,
                                marco_err, lleno_err, lbl_err, nota_err)))

        # la ganancia, en el hueco entre ambas
        ganancia = always_redraw(lambda: MathTex(
            r"-%.0f\%%" % (100 * rho.get_value() ** 2), color=VERDE).scale(0.62)
            .next_to(marco_err, RIGHT, buff=0.35))
        self.play(FadeIn(ganancia))

        # alineado a la izquierda del cuadro: centrado pisa la etiqueta del eje y
        valor_rho = always_redraw(lambda: VGroup(
            MathTex(r"\rho =", color=INK).scale(0.7),
            DecimalNumber(rho.get_value(), num_decimal_places=2,
                          color=AMBAR).scale(0.75),
        ).arrange(RIGHT, buff=0.15).next_to(ax, UP, buff=0.25)
            .align_to(ax, LEFT))
        self.play(FadeIn(valor_rho))
        self.wait(0.6)

        # ------------------------------------------------ rho = 0
        m0 = nota("ρ = 0: la nube es redonda, X no dice nada de Y", scale=0.46)
        m0.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m0))
        self.wait(1.6)
        self.play(FadeOut(m0))

        # ------------------------------------------------ subiendo rho
        self.play(rho.animate.set_value(0.6), run_time=2.4,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.4)
        m1 = nota("la nube se estira y el error empieza a caer", scale=0.46)
        m1.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m1))
        self.wait(1.2)
        self.play(FadeOut(m1))

        self.play(rho.animate.set_value(0.97), run_time=2.6,
                  rate_func=rate_functions.ease_in_out_sine)
        m2 = nota("ρ → 1: la relación es casi exacta, casi no queda error",
                  scale=0.46)
        m2.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m2))
        self.wait(1.8)
        self.play(FadeOut(m2))

        # ------------------------------------------------ negativo
        self.play(rho.animate.set_value(-0.85), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        m3 = nota("ρ negativo sirve exactamente igual: lo que importa es ρ²",
                  scale=0.46)
        m3.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m3))
        self.wait(1.8)
        self.play(FadeOut(m3))
        self.play(rho.animate.set_value(0.55), run_time=1.8)
        self.wait(0.5)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, puntos, recta, marco_var, lleno_var,
                                 lbl_var, nota_var, marco_err, lleno_err,
                                 lbl_err, nota_err, ganancia, valor_rho,
                                 formula)))
        filas = VGroup(
            VGroup(MathTex(r"\rho = 0", color=ROJO).scale(0.75),
                   Text("medir X no sirve de nada", color=INK).scale(0.52),
                   MathTex(r"\text{LMMSE}=\sigma_Y^2", color=ROJO).scale(0.65)
                   ).arrange(RIGHT, buff=0.5),
            VGroup(MathTex(r"|\rho| = 1", color=VERDE).scale(0.75),
                   Text("la relación es exacta", color=INK).scale(0.52),
                   MathTex(r"\text{LMMSE}=0", color=VERDE).scale(0.65)
                   ).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, buff=0.45)
        filas.move_to(ORIGIN)
        self.play(FadeIn(filas[0], shift=RIGHT * 0.15))
        self.play(FadeIn(filas[1], shift=RIGHT * 0.15))
        self.wait(0.6)
        cierre = nota("ρ² es la fracción de la varianza de Y que la medición "
                      "logra explicar", scale=0.52)
        cierre.next_to(filas, DOWN, buff=0.7)
        self.play(FadeIn(cierre))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, filas, cierre)))
        self.wait(0.3)
