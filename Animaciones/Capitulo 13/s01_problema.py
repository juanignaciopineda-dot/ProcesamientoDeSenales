"""Escena 1 - El problema: ¿solo ruido, o hay señal adentro?

De la deteccion de una hipotesis a partir de UNA medicion (cap. 9) a
decidir a partir de una SEÑAL ENTERA medida en un intervalo. Mismo tipo
de pregunta, ahora en L dimensiones.

    manim -pql s01_problema.py Problema
"""
from manim import *
import numpy as np
from comun import *

L = 14
SIGMA = 0.55
rng = np.random.default_rng(3)


def pulso(n):
    return np.where((n >= 3) & (n <= 9), 1.6 * np.sin(np.pi * (n - 3) / 6), 0.0)


class Problema(Scene):
    def construct(self):
        configurar()

        tit = titulo("¿Solo ruido, o hay señal escondida adentro?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        ejemplos = subtitulo("radar (¿hay un avión?)   ·   sonar   ·   "
                             "receptor digital (¿mandaron un 1 o un 0?)",
                             scale=0.5)
        ejemplos.next_to(tit, DOWN, buff=0.35).set_x(0)
        self.play(FadeIn(ejemplos))
        self.wait(1.4)
        self.play(FadeOut(ejemplos))

        # ------------------------------------------------ del capitulo 9 a este
        antes = VGroup(
            texto("Cap. 9: una sola medición $r$", color=INK, scale=0.5),
            texto("Cap. 13: toda una señal $r[n]$, $n=0,\\dots,L-1$",
                  color=AZUL, scale=0.5),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        antes.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(antes[0]))
        self.play(FadeIn(antes[1], shift=RIGHT * 0.1))
        self.wait(1.2)
        self.play(FadeOut(antes))

        # ------------------------------------------------ las dos hipotesis
        n = np.arange(L)
        s = pulso(n)
        w0 = rng.normal(0, SIGMA, L)
        w1 = rng.normal(0, SIGMA, L)

        h0_tit = MathTex(r"H_0:\ R[n]=W[n]", color=AZUL).scale(0.62)
        h1_tit = MathTex(r"H_1:\ R[n]=s[n]+W[n]", color=VERDE).scale(0.62)

        ax0, _ = ejes([0, L - 1, L], [-1.6, 2.2, 3.8], ancho=5.4, alto=2.1, tip=False)
        ax1, _ = ejes([0, L - 1, L], [-1.6, 2.2, 3.8], ancho=5.4, alto=2.1, tip=False)

        col_izq = VGroup(h0_tit, ax0).arrange(DOWN, buff=0.25)
        col_der = VGroup(h1_tit, ax1).arrange(DOWN, buff=0.25)
        cols = VGroup(col_izq, col_der).arrange(RIGHT, buff=0.7)
        cols.next_to(tit, DOWN, buff=0.5).set_x(0)

        st0 = stem(ax0, n, w0, color=AZUL, ancho=2.6, radio=0.035)
        st1 = stem(ax1, n, s + w1, color=VERDE, ancho=2.6, radio=0.035)

        self.play(FadeIn(h0_tit), Create(ax0))
        self.play(Create(st0))
        self.play(FadeIn(h1_tit), Create(ax1))
        self.play(Create(st1))
        self.wait(0.6)

        pregunta = nota("mirando solo la señal recibida, ¿podés distinguirlas?",
                        scale=0.46)
        pregunta.next_to(cols, DOWN, buff=0.4)
        self.play(FadeIn(pregunta))
        self.wait(1.8)
        self.play(FadeOut(VGroup(cols, st0, st1, pregunta)))

        # ------------------------------------------------ MAP con el vector r
        map_tit = Text("La regla MAP, ahora con un vector",
                       color=TXT).scale(0.58)
        map_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(map_tit))

        regla = MathTex(
            r"P(H_1|\mathbf R=\mathbf r)\underset{H_0}{\overset{H_1}{\gtrless}}"
            r"P(H_0|\mathbf R=\mathbf r)", color=TXT).scale(0.68)
        regla.next_to(map_tit, DOWN, buff=0.4)
        self.play(Write(regla))
        self.wait(1.0)

        bayes = MathTex(
            r"p_1\ f_{\mathbf R|H}(\mathbf r|H_1)\underset{H_0}{\overset{H_1}{\gtrless}}"
            r"p_0\ f_{\mathbf R|H}(\mathbf r|H_0)", color=AZUL).scale(0.68)
        bayes.next_to(regla, DOWN, buff=0.35)
        self.play(Write(bayes))
        n_bayes = nota("igual que antes, solo que ahora $f_{\\mathbf R|H}$ es\n"
                       "una densidad conjunta de $L$ variables", scale=0.46)
        n_bayes.next_to(bayes, DOWN, buff=0.3)
        self.play(FadeIn(n_bayes))
        self.wait(1.8)
        self.play(FadeOut(VGroup(map_tit, regla, bayes, n_bayes)))

        # ------------------------------------------------ regiones en L dimensiones
        dim_tit = Text("Lo único que cambia: las regiones de decisión",
                       color=TXT).scale(0.56)
        dim_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(dim_tit))

        nube_ax = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                       x_length=4.6, y_length=4.6,
                       axis_config={"color": INK, "stroke_width": 2,
                                   "include_ticks": False})
        nube_ax.next_to(dim_tit, DOWN, buff=0.4)
        self.play(Create(nube_ax))

        mu1 = np.array([1.7, 1.3])
        rng2 = np.random.default_rng(7)
        pts0 = rng2.normal(0, 0.55, (26, 2))
        pts1 = rng2.normal(0, 0.55, (26, 2)) + mu1

        nube0 = VGroup(*[Dot(nube_ax.c2p(*p), color=AZUL, radius=0.045)
                         for p in pts0])
        nube1 = VGroup(*[Dot(nube_ax.c2p(*p), color=VERDE, radius=0.045)
                         for p in pts1])
        l0 = MathTex("H_0", color=AZUL).scale(0.55).next_to(
            nube_ax.c2p(*(-mu1 * 0.9)), DL, buff=0.05)
        l1 = MathTex("H_1", color=VERDE).scale(0.55).next_to(
            nube_ax.c2p(*(mu1 * 1.55)), UR, buff=0.05)

        self.play(FadeIn(nube0, lag_ratio=0.02), FadeIn(l0))
        self.play(FadeIn(nube1, lag_ratio=0.02), FadeIn(l1))

        mid = mu1 / 2
        perp = np.array([-mu1[1], mu1[0]])
        perp = perp / np.linalg.norm(perp) * 2.6
        frontera = DashedLine(nube_ax.c2p(*(mid - perp)),
                              nube_ax.c2p(*(mid + perp)),
                              color=ROJO, stroke_width=3)
        self.play(Create(frontera))
        n_dim = nota("$D_0$ y $D_1$ son regiones en un espacio de $L$ "
                     "dimensiones, no ya tramos de la recta", scale=0.44)
        n_dim.next_to(nube_ax, DOWN, buff=0.3)
        self.play(FadeIn(n_dim))
        self.wait(2.0)
        self.play(FadeOut(VGroup(dim_tit, nube_ax, nube0, nube1, l0, l1,
                                 frontera, n_dim)))

        # ------------------------------------------------ mas datos no ayudan solos
        act_tit = Text("Dos mediciones son mejores que una...", color=AMBAR).scale(0.58)
        act_tit.next_to(tit, DOWN, buff=0.45).set_x(0)
        self.play(FadeIn(act_tit))

        filas = VGroup(
            texto("1 medición óptima:  $P_e=1/4$", color=INK, scale=0.52),
            texto("2 mediciones óptimas:  $P_e=3/16$", color=VERDE, scale=0.52),
            texto("2 mediciones, PROMEDIADAS:  $P_e=1/4$", color=ROJO, scale=0.52),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        filas.next_to(act_tit, DOWN, buff=0.4)
        for f in filas:
            self.play(FadeIn(f, shift=RIGHT * 0.12), run_time=0.5)
        self.wait(1.0)

        moraleja = nota("...si las usás bien. Más datos no ayudan solos:\n"
                        "hay que procesarlos bien.", scale=0.5, color=AMBAR)
        moraleja.next_to(filas, DOWN, buff=0.45)
        self.play(FadeIn(moraleja))
        self.wait(2.4)
        self.play(FadeOut(VGroup(act_tit, filas, moraleja)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("Misma pregunta que en el capítulo 9,", color=INK).scale(0.56),
            Text("pero ahora se decide con una señal entera.",
                 color=AZUL).scale(0.6),
            nota("¿cómo se arma esa regla en la práctica? sigue.", scale=0.48),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.4)
        self.play(FadeIn(cierre[2]))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
