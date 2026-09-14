"""Escena 3 - El filtro de Wiener FIR y las ecuaciones normales.

Con L muestras el problema es un sistema lineal L x L. Y aparece un
resultado contraintuitivo: en un proceso "bandeado" el predictor usa
muestras que estan INCORRELADAS con lo que se quiere predecir.

    manim -pql s03_fir.py WienerFIR
"""
from manim import *
import numpy as np
from comun import *


class WienerFIR(Scene):
    def construct(self):
        configurar()

        tit = titulo("Wiener FIR: un sistema lineal de L ecuaciones")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el estimador
        est = MathTex(r"\hat{y}[n]=\mu_y+\sum_{j=0}^{L-1} h[j]\,"
                      r"\big(x[n-j]-\mu_x\big)", color=TXT).scale(0.75)
        est.next_to(tit, DOWN, buff=0.4)
        self.play(Write(est))
        self.wait(0.8)

        clave = nota("como los procesos son conjuntamente WSS, los mismos "
                     "h[j] sirven para todo n", scale=0.46)
        clave.next_to(est, DOWN, buff=0.22)
        self.play(FadeIn(clave))
        self.wait(1.6)
        self.play(FadeOut(clave), est.animate.scale(0.8).to_edge(UP, buff=1.15))

        # ------------------------------------------------ las ecuaciones normales
        sistema = MathTex(
            r"\begin{bmatrix} C_{xx}[0] & C_{xx}[1] & \cdots & C_{xx}[L-1]\\"
            r"C_{xx}[1] & C_{xx}[0] & \cdots & C_{xx}[L-2]\\"
            r"\vdots & \vdots & \ddots & \vdots\\"
            r"C_{xx}[L\!-\!1] & C_{xx}[L\!-\!2] & \cdots & C_{xx}[0]"
            r"\end{bmatrix}"
            r"\begin{bmatrix} h[0]\\ h[1]\\ \vdots\\ h[L\!-\!1]\end{bmatrix}"
            r"=\begin{bmatrix} C_{xy}[0]\\ C_{xy}[-1]\\ \vdots\\ "
            r"C_{xy}[1\!-\!L]\end{bmatrix}",
            color=TXT).scale(0.58)
        sistema.move_to(UP * 0.35)
        self.play(Write(sistema, run_time=2.2))
        self.wait(0.8)

        yw = nota("para predicción se las conoce como ecuaciones de "
                  "Yule–Walker", scale=0.46)
        yw.next_to(sistema, DOWN, buff=0.4)
        self.play(FadeIn(yw))
        self.wait(1.6)
        self.play(FadeOut(VGroup(sistema, yw)))

        # ============================================ dos casos que sorprenden
        sub = Text("Dos procesos, dos comportamientos muy distintos",
                   color=TXT).scale(0.6)
        sub.next_to(est, DOWN, buff=0.45)
        self.play(FadeIn(sub))
        self.wait(0.8)

        # ---------- caso 1: exponencialmente correlacionado
        ms = np.arange(-5, 6)
        ax1, _ = ejes([-5, 5, 5], [0, 1.2], ancho=4.0, alto=1.5, tip=False)
        ax1.shift(LEFT * 3.4 + DOWN * 0.55)
        t1 = subtitulo("exponencialmente correlacionado", scale=0.44, color=VERDE)
        t1.next_to(ax1, UP, buff=0.2)
        cov1 = stem(ax1, ms, 0.6 ** np.abs(ms), color=VERDE, ancho=3)

        ax2, _ = ejes([-5, 5, 5], [0, 1.2], ancho=4.0, alto=1.5, tip=False)
        ax2.shift(RIGHT * 3.4 + DOWN * 0.55)
        t2 = subtitulo("bandeado (memoria de un paso)", scale=0.44, color=AMBAR)
        t2.next_to(ax2, UP, buff=0.2)
        cov2 = stem(ax2, ms, np.where(np.abs(ms) == 0, 1.0,
                                      np.where(np.abs(ms) == 1, 0.5, 0.0)),
                    color=AMBAR, ancho=3)

        self.play(Create(ax1), FadeIn(t1), FadeIn(cov1),
                  Create(ax2), FadeIn(t2), FadeIn(cov2))
        self.wait(1.0)

        # ---------- las soluciones
        sol1 = MathTex(r"h[0]=\alpha,\quad h[j]=0\ \ (j\geq 1)",
                       color=VERDE).scale(0.6)
        sol1.next_to(ax1, DOWN, buff=0.45)
        sol2 = MathTex(r"h[0],\,h[1],\,h[2] \;\neq\; 0", color=AMBAR).scale(0.6)
        sol2.next_to(ax2, DOWN, buff=0.45)

        self.play(FadeIn(sol1))
        n1 = nota("solo importa la última muestra:\nsaber x[n] ya lo dice todo",
                  scale=0.42)
        n1.next_to(sol1, DOWN, buff=0.25)
        self.play(FadeIn(n1))
        self.wait(1.6)

        self.play(FadeIn(sol2))
        n2 = nota("usa x[n−1] y x[n−2]…\naunque estén INCORRELADAS con x[n+1]",
                  scale=0.42)
        n2.next_to(sol2, DOWN, buff=0.25)
        self.play(FadeIn(n2))
        self.wait(2.2)

        # ============================================ la explicacion
        self.play(FadeOut(VGroup(ax1, t1, cov1, sol1, n1,
                                 ax2, t2, cov2, sol2, n2, sub, est)))

        expl = VGroup(
            Text("¿Cómo puede servir una medición incorrelada?",
                 color=AMBAR).scale(0.62),
            nota("No aporta información sobre el futuro por sí sola,", scale=0.5),
            nota("pero ayuda a limpiar lo que x[n] está diciendo.", scale=0.5),
            Text("No correlacionado  ≠  inútil", color=TXT).scale(0.62),
        ).arrange(DOWN, buff=0.32)
        expl.move_to(ORIGIN).shift(UP * 0.2)
        self.play(FadeIn(expl[0], shift=UP * 0.15))
        self.wait(0.5)
        self.play(FadeIn(expl[1]), FadeIn(expl[2]))
        self.wait(1.4)
        self.play(FadeIn(expl[3], scale=1.15))
        self.wait(0.6)
        cierre_n = nota("es el mismo fenómeno que en regresión múltiple: una "
                        "variable puede servir como control", scale=0.46)
        cierre_n.next_to(expl, DOWN, buff=0.55)
        self.play(FadeIn(cierre_n))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, expl, cierre_n)))
        self.wait(0.3)
