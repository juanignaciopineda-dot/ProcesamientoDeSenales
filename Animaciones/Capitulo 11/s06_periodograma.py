"""Escena 6 - Einstein-Wiener-Khinchin y el promediado de periodogramas.

Un solo periodograma es puro ruido y su varianza NO baja aunque agrandes
la ventana. Promediando M ventanas, la varianza cae como 1/M y el
estimado converge a la PSD verdadera.

    manim -pql s06_periodograma.py Periodograma
"""
from manim import *
import numpy as np
from comun import *

T_VENT = 128            # largo de cada ventana
NF = T_VENT // 2        # bins utiles
X_MAX = 6.0             # ancho del cuadro en unidades de escena
PSD_REAL = 1.0          # proceso de Bernoulli +-1: PSD plana en 1

_rng = np.random.default_rng(2024)


def un_periodograma():
    x = _rng.choice([-1.0, 1.0], size=T_VENT)
    P = np.abs(np.fft.fft(x)) ** 2 / T_VENT
    return P[:NF]


FREQ = np.arange(NF) / NF * X_MAX


class Periodograma(Scene):
    def construct(self):
        configurar()

        tit = titulo("Estimar el espectro: promediar periodogramas")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el teorema
        ewk = MathTex(
            r"S_{xx}(j\omega)\;=\;\lim_{T\to\infty}\frac{1}{2T}\,"
            r"E\big[\,|X_T(j\omega)|^2\,\big]",
            color=TXT).scale(0.68)
        ewk.next_to(tit, DOWN, buff=0.35)
        ewk_nota = nota("teorema de Einstein–Wiener–Khinchin", scale=0.44)
        ewk_nota.next_to(ewk, DOWN, buff=0.14)
        self.play(Write(ewk), FadeIn(ewk_nota))
        self.wait(1.6)
        self.play(FadeOut(ewk_nota), ewk.animate.scale(0.72).to_edge(UP, buff=1.15))

        # ------------------------------------------------ los ejes
        ax, lab = ejes([0, X_MAX, X_MAX], [0, 4.4], ancho=8.6, alto=3.0,
                       x_label=r"\Omega")
        ax.shift(DOWN * 0.75)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        # la PSD verdadera, de referencia
        real = DashedLine(ax.c2p(0, PSD_REAL), ax.c2p(X_MAX, PSD_REAL),
                          color=VERDE, stroke_width=3, dash_length=0.12)
        real_lbl = MathTex(r"S_{xx}=1", color=VERDE).scale(0.55)
        real_lbl.next_to(ax.c2p(X_MAX, PSD_REAL), UR, buff=0.08).shift(LEFT * 0.7)
        self.play(Create(real), FadeIn(real_lbl))
        self.wait(0.4)

        # ------------------------------------------------ M = 1
        P1 = un_periodograma()
        cur = linea_datos(ax, FREQ, P1, color=ROJO, ancho=2.2)
        contador = VGroup(
            MathTex("M =", color=INK).scale(0.7),
            Integer(1, color=AMBAR).scale(0.75),
        ).arrange(RIGHT, buff=0.16)
        contador.to_corner(UR, buff=0.75).shift(DOWN * 0.6)

        self.play(Create(cur, run_time=1.2), FadeIn(contador))
        self.wait(0.5)
        mal = Text("un solo periodograma es puro ruido", color=ROJO).scale(0.52)
        mal.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(mal))
        self.wait(1.5)
        self.play(FadeOut(mal))

        # ------------------------------------------------ acumulando
        acum = P1.copy()
        M = 1
        # primero de a uno, para que se vea el mecanismo
        for _ in range(3):
            M += 1
            acum += un_periodograma()
            nueva = linea_datos(ax, FREQ, acum / M, color=ROJO, ancho=2.2)
            self.play(Transform(cur, nueva),
                      contador[1].animate.set_value(M), run_time=0.75)

        # despues en tandas, para llegar a M grande sin alargar el video
        for objetivo, color in [(8, ROJO), (16, AMBAR), (32, AMBAR),
                                (64, VERDE), (128, VERDE)]:
            while M < objetivo:
                acum += un_periodograma()
                M += 1
            nueva = linea_datos(ax, FREQ, acum / M, color=color, ancho=2.4)
            self.play(Transform(cur, nueva),
                      contador[1].animate.set_value(M), run_time=0.9)
            self.wait(0.25)

        self.wait(0.6)
        bien = Text("promediando, la estimación converge a la PSD real",
                    color=VERDE).scale(0.52)
        bien.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(bien))
        self.wait(1.8)
        self.play(FadeOut(bien))

        # ------------------------------------------------ la ley 1/M
        ley = MathTex(r"\text{varianza del estimador}\;\propto\;\frac{1}{M}",
                      color=AMBAR).scale(0.72)
        ley.to_edge(DOWN, buff=0.5)
        self.play(Write(ley))
        self.wait(1.8)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, cur, real, real_lbl, contador, ley, ewk)))
        cierre = VGroup(
            Text("Más ventanas  →  menos varianza", color=VERDE).scale(0.6),
            Text("Ventanas más largas  →  mejor resolución", color=AZUL).scale(0.6),
            nota("pero con un registro fijo no se pueden las dos cosas…",
                 scale=0.5),
        ).arrange(DOWN, buff=0.26)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1], shift=UP * 0.15))
        self.wait(0.4)
        self.play(FadeIn(cierre[2]))
        self.wait(2.0)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
