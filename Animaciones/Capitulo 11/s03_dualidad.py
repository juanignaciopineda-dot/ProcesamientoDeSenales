"""Escena 3 - La dualidad tiempo/frecuencia de la PSD.

R_xx(tau) y S_xx(jw) son un par de transformadas: cuando la autocorrelacion
se angosta, el espectro se ensancha. Memoria corta <=> espectro ancho.

    manim -pql s03_dualidad.py Dualidad
"""
from manim import *
import numpy as np
from comun import *

TAU_MAX = 3.0
W_MAX = 9.0


class Dualidad(Scene):
    def construct(self):
        configurar()

        tit = titulo("La autocorrelación y el espectro son la misma información")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        alfa = ValueTracker(1.0)

        # ------------------------------------------------ panel izquierdo
        ax_r, lab_r = ejes([-TAU_MAX, TAU_MAX, TAU_MAX], [0, 1.25], ancho=5.0,
                           alto=2.6, x_label=r"\tau")
        ax_r.shift(LEFT * 3.35 + DOWN * 0.35)
        lab_r.next_to(ax_r.x_axis.get_end(), DR, buff=0.1)

        # paso fino en x_range: con el muestreo por defecto, una curva muy
        # picuda genera lobulos espurios al interpolar con bezier
        r_curva = always_redraw(lambda: ax_r.plot(
            lambda t: np.exp(-alfa.get_value() * abs(t)),
            x_range=[-TAU_MAX, TAU_MAX, 0.01], color=VERDE, stroke_width=4,
            use_smoothing=False))
        r_area = always_redraw(lambda: ax_r.get_area(
            ax_r.plot(lambda t: np.exp(-alfa.get_value() * abs(t)),
                      x_range=[-TAU_MAX, TAU_MAX, 0.01], use_smoothing=False),
            x_range=(-TAU_MAX, TAU_MAX), color=VERDE, opacity=0.14,
            stroke_width=0))
        r_lbl = MathTex(r"R_{xx}(\tau)=e^{-\alpha|\tau|}", color=VERDE).scale(0.58)
        r_lbl.next_to(ax_r, UP, buff=0.28).align_to(ax_r, LEFT)

        # ------------------------------------------------ panel derecho
        ax_s, lab_s = ejes([-W_MAX, W_MAX, W_MAX], [0, 3.1], ancho=5.0,
                           alto=2.6, x_label=r"\omega")
        ax_s.shift(RIGHT * 3.35 + DOWN * 0.35)
        lab_s.next_to(ax_s.x_axis.get_end(), DR, buff=0.1)

        s_curva = always_redraw(lambda: ax_s.plot(
            lambda w: 2 * alfa.get_value() / (alfa.get_value() ** 2 + w ** 2),
            x_range=[-W_MAX, W_MAX, 0.02], color=AZUL, stroke_width=4,
            use_smoothing=False))
        s_area = always_redraw(lambda: ax_s.get_area(
            ax_s.plot(lambda w: 2 * alfa.get_value() / (alfa.get_value() ** 2 + w ** 2),
                      x_range=[-W_MAX, W_MAX, 0.02], use_smoothing=False),
            x_range=(-W_MAX, W_MAX), color=AZUL, opacity=0.14, stroke_width=0))
        s_lbl = MathTex(r"S_{xx}(j\omega)=\frac{2\alpha}{\alpha^2+\omega^2}",
                        color=AZUL).scale(0.58)
        s_lbl.next_to(ax_s, UP, buff=0.22).align_to(ax_s, RIGHT)

        self.play(Create(ax_r), FadeIn(lab_r), Create(ax_s), FadeIn(lab_s))
        self.play(FadeIn(r_curva), FadeIn(r_area), FadeIn(r_lbl))
        self.play(FadeIn(s_curva), FadeIn(s_area), FadeIn(s_lbl))
        self.wait(0.5)

        # ------------------------------------------------ flecha de Fourier
        fl = Arrow(ax_r.get_right() + RIGHT * 0.05, ax_s.get_left() + LEFT * 0.05,
                   color=AMBAR, stroke_width=3, buff=0.15,
                   max_tip_length_to_length_ratio=0.14)
        fl_lbl = MathTex(r"\mathcal{F}", color=AMBAR).scale(0.62)
        fl_lbl.next_to(fl, UP, buff=0.08)
        self.play(GrowArrow(fl), FadeIn(fl_lbl))
        self.wait(0.6)

        # ------------------------------------------------ el valor de alfa
        valor = always_redraw(lambda: VGroup(
            MathTex(r"\alpha =", color=INK).scale(0.6),
            DecimalNumber(alfa.get_value(), num_decimal_places=1, color=AMBAR)
            .scale(0.6),
        ).arrange(RIGHT, buff=0.14).next_to(fl, DOWN, buff=0.45))
        self.play(FadeIn(valor))

        # ------------------------------------------------ barrido
        msg1 = nota("memoria larga: la señal se parece a sí misma mucho tiempo",
                    scale=0.44)
        msg1.to_edge(DOWN, buff=0.7)
        self.play(alfa.animate.set_value(0.45), run_time=2.2)
        self.play(FadeIn(msg1))
        self.wait(1.5)

        msg2 = nota("memoria corta: se descorrelaciona enseguida", scale=0.44)
        msg2.to_edge(DOWN, buff=0.7)
        self.play(FadeOut(msg1))
        self.play(alfa.animate.set_value(4.0), run_time=3.0,
                  rate_func=rate_functions.ease_in_out_sine)
        self.play(FadeIn(msg2))
        self.wait(1.5)
        self.play(FadeOut(msg2))

        self.play(alfa.animate.set_value(0.7), run_time=2.0)
        self.play(alfa.animate.set_value(3.0), run_time=2.0)
        self.wait(0.4)

        # ------------------------------------------------ conservacion
        cons = MathTex(r"R_{xx}(0)=\frac{1}{2\pi}\int_{-\infty}^{\infty}"
                       r"S_{xx}(j\omega)\,d\omega \;=\; \text{potencia total}",
                       color=TXT).scale(0.58)
        cons.to_edge(DOWN, buff=0.72)
        self.play(Write(cons))
        self.wait(0.6)
        nota_cons = nota("se ensancha o se angosta, pero el área total no cambia",
                         scale=0.42)
        nota_cons.next_to(cons, DOWN, buff=0.14)
        self.play(FadeIn(nota_cons))
        self.wait(1.8)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(cons, nota_cons, valor, fl, fl_lbl)))
        # la flecha bidireccional larga (U+27FA) no esta en la fuente de
        # Text() y sale como caja vacia: va por MathTex
        cierre = VGroup(
            Text("Angosta en tiempo", color=VERDE).scale(0.6),
            MathTex(r"\Longleftrightarrow", color=AMBAR).scale(0.72),
            Text("ancha en frecuencia", color=AZUL).scale(0.6),
        ).arrange(RIGHT, buff=0.3)
        cierre.to_edge(DOWN, buff=0.75)
        self.play(FadeIn(cierre, shift=UP * 0.15))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, ax_r, lab_r, r_curva, r_area, r_lbl,
                                 ax_s, lab_s, s_curva, s_area, s_lbl, cierre)))
        self.wait(0.3)
