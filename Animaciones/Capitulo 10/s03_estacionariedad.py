"""Escena 3 - Estacionariedad: SSS y WSS.

Un proceso es estacionario cuando su estadistica no depende de EN QUE
MOMENTO lo mires. Se compara un proceso que claramente no lo es (media
que deriva, varianza que crece) contra uno que si, deslizando una
ventana y mirando lo que pasa adentro.

    manim -pql s03_estacionariedad.py Estacionariedad
"""
from manim import *
import numpy as np
from comun import *

N = 600
T = np.linspace(0, 12, N)
K = 4
COLS = [AZUL, AMBAR, VERDE, MAGENTA]


def base(semilla):
    rng = np.random.default_rng(300 + semilla)
    y = np.zeros_like(T)
    for _ in range(7):
        f = rng.uniform(0.5, 3.0)
        y += rng.normal(0, 1) * np.sin(2 * np.pi * f * T / T[-1] * 2
                                       + rng.uniform(0, 2 * np.pi))
    return y / np.std(y)


ESTAC = [0.85 * base(i) for i in range(K)]
# no estacionario: la media deriva y la amplitud crece con el tiempo
NO_EST = [0.30 * (1 + 0.42 * T) * base(i) + (-1.4 + 0.26 * T) for i in range(K)]


class Estacionariedad(Scene):
    def construct(self):
        configurar()

        tit = titulo("Estacionariedad: ¿importa cuándo mires?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        ax, lab = ejes([0, 12, 12], [-4.1, 4.1], ancho=9.0, alto=4.1,
                       x_label="t")
        ax.shift(DOWN * 0.55)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        # ============================================ caso NO estacionario
        etiqueta = Text("NO estacionario", color=ROJO, weight=BOLD).scale(0.6)
        etiqueta.next_to(tit, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)
        ondas = VGroup(*[linea_datos(ax, T, NO_EST[i], color=COLS[i], ancho=1.6)
                         for i in range(K)])
        self.play(FadeIn(etiqueta))
        self.play(LaggedStart(*[Create(o) for o in ondas], lag_ratio=0.15,
                              run_time=1.8))
        self.wait(0.5)

        # ventana deslizante que mide media y dispersion adentro
        cen = ValueTracker(1.6)
        ANCHO = 2.6

        def ventana(datos):
            return always_redraw(lambda: Rectangle(
                width=ax.c2p(ANCHO, 0)[0] - ax.c2p(0, 0)[0],
                height=ax.c2p(0, 4.1)[1] - ax.c2p(0, -4.1)[1],
                color=TXT, stroke_width=2.5, fill_color=TXT, fill_opacity=0.07
            ).move_to(ax.c2p(cen.get_value(), 0)))

        def lectura(datos):
            def _f():
                a, b = cen.get_value() - ANCHO / 2, cen.get_value() + ANCHO / 2
                m = (T >= a) & (T <= b)
                vals = np.concatenate([d[m] for d in datos])
                g = VGroup(
                    VGroup(MathTex(r"\hat\mu =", color=INK).scale(0.55),
                           DecimalNumber(float(np.mean(vals)), num_decimal_places=2,
                                         color=AMBAR).scale(0.55)
                           ).arrange(RIGHT, buff=0.12),
                    VGroup(MathTex(r"\hat\sigma =", color=INK).scale(0.55),
                           DecimalNumber(float(np.std(vals)), num_decimal_places=2,
                                         color=VERDE).scale(0.55)
                           ).arrange(RIGHT, buff=0.12),
                ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
                return g.to_edge(RIGHT, buff=0.6).shift(UP * 1.75)
            return always_redraw(_f)

        v = ventana(NO_EST)
        r = lectura(NO_EST)
        self.play(FadeIn(v), FadeIn(r))
        self.wait(0.5)
        self.play(cen.animate.set_value(10.4), run_time=4.2,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.5)
        obs = Text("la estadística cambia según dónde mires", color=ROJO).scale(0.52)
        obs.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(obs))
        self.wait(1.6)
        self.play(FadeOut(obs))

        # ============================================ caso estacionario
        ondas2 = VGroup(*[linea_datos(ax, T, ESTAC[i], color=COLS[i], ancho=1.6)
                          for i in range(K)])
        etiqueta2 = Text("estacionario", color=VERDE, weight=BOLD).scale(0.6)
        etiqueta2.move_to(etiqueta, aligned_edge=LEFT)
        self.play(Transform(ondas, ondas2), Transform(etiqueta, etiqueta2),
                  run_time=1.4)
        self.remove(r)
        r2 = lectura(ESTAC)
        self.add(r2)
        self.play(cen.animate.set_value(1.6), run_time=0.9)
        self.wait(0.4)
        self.play(cen.animate.set_value(10.4), run_time=4.2,
                  rate_func=rate_functions.ease_in_out_sine)
        obs2 = Text("mire donde mire, lo mismo", color=VERDE).scale(0.52)
        obs2.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(obs2))
        self.wait(1.8)

        # ============================================ SSS contra WSS
        self.play(FadeOut(VGroup(ax, lab, ondas, v, r2, etiqueta, obs2)))

        col_i = VGroup(
            Text("SSS", color=VERDE, weight=BOLD).scale(0.78),
            Text("sentido estricto", color=INK).scale(0.46),
            MathTex(r"f_{X(t_1),\dots}(\cdot)=f_{X(t_1+\alpha),\dots}(\cdot)",
                    color=TXT).scale(0.52),
            nota("TODAS las densidades\nson invariantes", scale=0.42),
        ).arrange(DOWN, buff=0.22)
        col_d = VGroup(
            Text("WSS", color=AZUL, weight=BOLD).scale(0.78),
            Text("sentido amplio", color=INK).scale(0.46),
            MathTex(r"\mu_X(t)=\mu_X", color=TXT).scale(0.58),
            MathTex(r"R_{XX}(t_1,t_2)=R_{XX}(\tau)", color=TXT).scale(0.58),
            nota("solo pide eso: los\nmomentos, nada más", scale=0.42),
        ).arrange(DOWN, buff=0.2)
        fila = VGroup(col_i, col_d).arrange(RIGHT, buff=1.9)
        fila.move_to(ORIGIN).shift(UP * 0.35)

        self.play(FadeIn(col_i, shift=RIGHT * 0.2))
        self.wait(0.4)
        self.play(FadeIn(col_d, shift=LEFT * 0.2))
        self.wait(1.2)

        rel = VGroup(
            MathTex(r"\text{SSS}\;\Longrightarrow\;\text{WSS}", color=AMBAR).scale(0.7),
            MathTex(r"\text{WSS}\;\not\Longrightarrow\;\text{SSS}",
                    color=ROJO).scale(0.7),
        ).arrange(RIGHT, buff=1.1)
        rel.next_to(fila, DOWN, buff=0.7)
        gauss = nota("…salvo para procesos gaussianos, donde son equivalentes",
                     scale=0.46)
        gauss.next_to(rel, DOWN, buff=0.25)

        self.play(FadeIn(rel[0]))
        self.play(FadeIn(rel[1]))
        self.wait(0.6)
        self.play(FadeIn(gauss))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, fila, rel, gauss)))
        self.wait(0.3)
