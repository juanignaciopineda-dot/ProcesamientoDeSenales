"""Escena 1 - El problema de estimacion de senales.

Tengo una senal que no veo y una medicion contaminada. Quiero el mejor
filtro LINEAL para recuperarla. Es el LMMSE del capitulo 8, pero ahora
sobre procesos enteros en vez de variables sueltas.

    manim -pql s01_problema.py ProblemaEstimacion
"""
from manim import *
import numpy as np
from comun import *

N = 90
RHO = 0.5
_rng = np.random.default_rng(12)

_w = _rng.choice([-1.0, 1.0], size=N + 1)
_a = np.sqrt((1 + np.sqrt(1 - 4 * RHO ** 2)) / 2)
_b = RHO / _a
Y = (_a * _w[1:] + _b * _w[:-1])
Y = 1.6 * Y / np.std(Y)
V = _rng.normal(0, 1.35, N)
X = Y + V


class ProblemaEstimacion(Scene):
    def construct(self):
        configurar()

        tit = titulo("El problema: recuperar una señal escondida en ruido")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ la senal verdadera
        def panel(y_shift, color, etiqueta):
            ax, _ = ejes([0, N, N], [-5.2, 5.2], ancho=8.0, alto=1.65, tip=False)
            ax.shift(y_shift)
            lab = MathTex(etiqueta, color=color).scale(0.6)
            lab.next_to(ax, LEFT, buff=0.28)
            return ax, lab

        ax_y, lab_y = panel(UP * 1.55, VERDE, r"y[n]")
        ax_x, lab_x = panel(DOWN * 0.35, ROJO, r"x[n]")
        ax_h, lab_h = panel(DOWN * 2.25, AZUL, r"\hat{y}[n]")

        oy = linea_datos(ax_y, np.arange(N), Y, color=VERDE, ancho=2.2)
        self.play(Create(ax_y), FadeIn(lab_y))
        self.play(Create(oy, run_time=1.5, rate_func=linear))
        n1 = nota("la señal que me interesa… pero que NO puedo medir", scale=0.44)
        n1.next_to(ax_y, UP, buff=0.18)
        self.play(FadeIn(n1))
        self.wait(1.3)

        # ------------------------------------------------ la medicion
        ox = linea_datos(ax_x, np.arange(N), X, color=ROJO, ancho=2.2)
        self.play(Create(ax_x), FadeIn(lab_x))
        self.play(Create(ox, run_time=1.5, rate_func=linear))
        modelo = MathTex(r"x[n]=y[n]+v[n]", color=ROJO).scale(0.6)
        modelo.next_to(ax_x, UP, buff=0.16)
        self.play(FadeIn(modelo))
        self.wait(1.4)

        # ------------------------------------------------ la pregunta
        preg = Text("¿Cuál es el mejor filtro lineal para recuperar y[n]?",
                    color=TXT).scale(0.6)
        preg.move_to(ax_h)
        self.play(FadeIn(preg, shift=UP * 0.15))
        self.wait(1.8)
        self.play(FadeOut(preg))

        # ------------------------------------------------ la estimacion
        # Wiener no causal aplicado en frecuencia, solo para mostrar el objetivo
        Nf = 512
        W = 2 * np.pi * np.fft.fftfreq(Nf)
        Dyy = (1.6 ** 2) * (1 + 2 * RHO * np.cos(W))
        Dvv = np.full_like(W, 1.35 ** 2)
        H = Dyy / (Dyy + Dvv)
        YH = np.real(np.fft.ifft(np.fft.fft(X, Nf) * H))[:N]

        oh = linea_datos(ax_h, np.arange(N), YH, color=AZUL, ancho=2.2)
        self.play(Create(ax_h), FadeIn(lab_h))
        self.play(Create(oh, run_time=1.5, rate_func=linear))
        self.wait(0.8)

        # comparacion superpuesta
        comp = linea_datos(ax_h, np.arange(N), Y, color=VERDE, ancho=1.6)
        comp.set_opacity(0.55)
        n2 = nota("en verde, la señal verdadera superpuesta", scale=0.42)
        n2.next_to(ax_h, DOWN, buff=0.18)
        self.play(Create(comp), FadeIn(n2))
        self.wait(1.8)
        self.play(FadeOut(VGroup(comp, n2, n1, modelo)))

        # ------------------------------------------------ el enlace con el cap 8
        self.play(FadeOut(VGroup(ax_y, lab_y, oy, ax_x, lab_x, ox,
                                 ax_h, lab_h, oh)))

        izq = VGroup(
            Text("Capítulo 8", color=INK, weight=BOLD).scale(0.58),
            MathTex(r"\hat{Y}=\mu_Y+\mathbf{a}^T(\mathbf{X}-\boldsymbol\mu_X)",
                    color=TXT).scale(0.62),
            nota("estimar una VARIABLE a partir de otras", scale=0.44),
        ).arrange(DOWN, buff=0.24)
        der = VGroup(
            Text("Capítulo 12", color=AZUL, weight=BOLD).scale(0.58),
            MathTex(r"\hat{y}[n]=\mu_y+\sum_j h[j]\,(x[n-j]-\mu_x)",
                    color=AZUL).scale(0.62),
            nota("estimar un PROCESO a partir de otro", scale=0.44),
        ).arrange(DOWN, buff=0.24)
        fl = MathTex(r"\longrightarrow", color=AMBAR).scale(1.1)
        fila = VGroup(izq, fl, der).arrange(RIGHT, buff=0.7)
        fila.move_to(ORIGIN).shift(UP * 0.35)

        self.play(FadeIn(izq, shift=RIGHT * 0.15))
        self.wait(0.6)
        self.play(FadeIn(fl))
        self.play(FadeIn(der, shift=LEFT * 0.15))
        self.wait(1.2)

        clave = Text("La suma es una convolución: el estimador ES un filtro LTI",
                     color=AMBAR).scale(0.58)
        clave.next_to(fila, DOWN, buff=0.75)
        self.play(FadeIn(clave, shift=UP * 0.15))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, fila, clave)))
        self.wait(0.3)
