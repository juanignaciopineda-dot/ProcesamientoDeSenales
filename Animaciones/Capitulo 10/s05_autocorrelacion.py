"""Escena 5 - La autocorrelacion como solapamiento deslizante.

R_xx(tau) mide cuanto se parece la senal a una copia corrida tau. Se
anima el corrimiento y se va trazando R_xx(tau) punto a punto. De ahi
salen solas las dos propiedades: simetria par y maximo en el origen.

    manim -pql s05_autocorrelacion.py Autocorrelacion
"""
from manim import *
import numpy as np
from comun import *

ALFA = 0.9
TAU_MAX = 4.0
T = np.linspace(-6, 6, 700)


def senal(t, corr=1.1):
    """Realizacion suave, con escala de correlacion controlada."""
    rng = np.random.default_rng(9)
    y = np.zeros_like(t)
    for _ in range(9):
        f = rng.uniform(0.15, 0.75)
        y += rng.normal(0, 1) * np.sin(2 * np.pi * f * t / corr
                                       + rng.uniform(0, 2 * np.pi))
    return 1.15 * y / np.std(y)


X = senal(T)


def R_teo(tau):
    """Autocorrelacion modelo, exponencial: baja al alejarse del origen."""
    return np.exp(-ALFA * abs(tau))


class Autocorrelacion(Scene):
    def construct(self):
        configurar()

        tit = titulo("La autocorrelación: la señal contra sí misma corrida")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ arriba: las dos copias
        ax, _ = ejes([-6, 6, 6], [-2.6, 2.6], ancho=8.6, alto=2.2, tip=False)
        ax.shift(UP * 1.15)
        base = Line(ax.c2p(-6, 0), ax.c2p(6, 0), color=INK, stroke_width=1.2)

        original = linea_datos(ax, T, X, color=AZUL, ancho=2.6)
        o_lbl = MathTex("x(t)", color=AZUL).scale(0.6)
        o_lbl.next_to(ax, LEFT, buff=0.1).shift(UP * 0.55)

        tau = ValueTracker(0.0)

        def _copia():
            # la copia corrida hay que recortarla al rango de los ejes, o
            # se dibuja fuera del cuadro y se derrama por la pantalla
            xs = T + tau.get_value()
            m = (xs >= -6) & (xs <= 6)
            if m.sum() < 2:
                return VMobject()
            return linea_datos(ax, xs[m], X[m], color=AMBAR, ancho=2.6)

        copia = always_redraw(_copia)
        c_lbl = always_redraw(lambda: MathTex(r"x(t+\tau)", color=AMBAR)
                              .scale(0.6).next_to(ax, LEFT, buff=0.1)
                              .shift(DOWN * 0.25))

        self.play(FadeIn(base), Create(original), FadeIn(o_lbl))
        self.play(FadeIn(copia), FadeIn(c_lbl))
        self.wait(0.6)

        val = always_redraw(lambda: VGroup(
            MathTex(r"\tau =", color=INK).scale(0.6),
            DecimalNumber(tau.get_value(), num_decimal_places=2, color=AMBAR,
                          include_sign=True).scale(0.6),
        ).arrange(RIGHT, buff=0.12).next_to(ax, UP, buff=0.15)
            .to_edge(RIGHT, buff=1.0))
        self.play(FadeIn(val))

        # ------------------------------------------------ abajo: R(tau)
        ax_r, lab_r = ejes([-TAU_MAX, TAU_MAX, TAU_MAX], [-0.25, 1.25],
                           ancho=7.2, alto=2.0, x_label=r"\tau")
        ax_r.shift(DOWN * 1.9)
        lab_r.next_to(ax_r.x_axis.get_end(), DR, buff=0.1)
        r_lbl = MathTex(r"R_{xx}(\tau)", color=VERDE).scale(0.62)
        r_lbl.next_to(ax_r, UP, buff=0.12).to_edge(LEFT, buff=1.4)

        self.play(Create(ax_r), FadeIn(lab_r), FadeIn(r_lbl))

        traza = always_redraw(lambda: ax_r.plot(
            R_teo, x_range=[min(0.0, tau.get_value()),
                            max(0.0, tau.get_value()), 0.01],
            color=VERDE, stroke_width=4, use_smoothing=False))
        punto = always_redraw(lambda: Dot(
            ax_r.c2p(tau.get_value(), R_teo(tau.get_value())),
            color=VERDE, radius=0.07))
        self.add(traza, punto)

        # ------------------------------------------------ el barrido
        pico = MathTex(r"R_{xx}(0)", color=VERDE).scale(0.52)
        pico.next_to(ax_r.c2p(0, 1.0), UR, buff=0.1)
        obs0 = nota("en τ=0 la señal calza consigo misma: el máximo", scale=0.46)
        obs0.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(pico), FadeIn(obs0))
        self.wait(1.3)
        self.play(FadeOut(obs0))

        self.play(tau.animate.set_value(TAU_MAX), run_time=3.6,
                  rate_func=rate_functions.ease_in_out_sine)
        obs1 = nota("al correrla, deja de parecerse: R baja", scale=0.46)
        obs1.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(obs1))
        self.wait(1.2)
        self.play(FadeOut(obs1))

        self.play(tau.animate.set_value(-TAU_MAX), run_time=4.2,
                  rate_func=rate_functions.ease_in_out_sine)
        obs2 = nota("y hacia el otro lado pasa exactamente lo mismo", scale=0.46)
        obs2.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(obs2))
        self.wait(1.4)
        self.play(FadeOut(obs2))
        self.play(tau.animate.set_value(0.0), run_time=1.4)

        # ------------------------------------------------ las dos propiedades
        self.play(FadeOut(VGroup(ax, base, original, copia, o_lbl, c_lbl, val,
                                 pico)))
        self.play(VGroup(ax_r, lab_r, r_lbl, traza, punto).animate.shift(UP * 1.5))

        props = VGroup(
            VGroup(MathTex(r"R_{xx}(\tau)=R_{xx}(-\tau)", color=AMBAR).scale(0.7),
                   nota("simetría par: correr para adelante o para atrás "
                        "es lo mismo", scale=0.44)).arrange(DOWN, buff=0.14),
            VGroup(MathTex(r"|C_{xx}(\tau)|\;\leq\;C_{xx}(0)", color=VERDE).scale(0.7),
                   nota("nada está más correlacionado con la señal "
                        "que la señal misma", scale=0.44)).arrange(DOWN, buff=0.14),
        ).arrange(DOWN, buff=0.45)
        props.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(props[0], shift=UP * 0.12))
        self.wait(1.2)
        self.play(FadeIn(props[1], shift=UP * 0.12))
        self.wait(0.6)
        origen = nota("la segunda sale directo del capítulo 7: el coeficiente "
                      "de correlación vive entre −1 y 1", scale=0.42)
        origen.next_to(props, DOWN, buff=0.22)
        self.play(FadeIn(origen))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, ax_r, lab_r, r_lbl, traza, punto, props,
                                 origen)))
        self.wait(0.3)
