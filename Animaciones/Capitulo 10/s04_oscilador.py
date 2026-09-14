"""Escena 4 - El oscilador con fase aleatoria.

El ejemplo del libro. Con fase fija el proceso NO es WSS: la media
oscila con el tiempo. Con fase uniforme en [-pi, pi] la media se
aplana en cero y la autocorrelacion pasa a depender solo de tau.
La fase aleatoria es lo que "borra" el origen de tiempos.

    manim -pql s04_oscilador.py Oscilador
"""
from manim import *
import numpy as np
from comun import *

N = 500
T = np.linspace(0, 8, N)
W0 = 2.6
K = 9
COLS = [AZUL, AMBAR, VERDE, MAGENTA, ROJO, "#5ec8d8", "#d8c65e", "#8f9bff",
        "#57d69a"]
_rng = np.random.default_rng(41)
AMPS = _rng.uniform(0.7, 1.6, K)


class Oscilador(Scene):
    def construct(self):
        configurar()

        tit = titulo("El oscilador: por qué la fase aleatoria importa")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        modelo = MathTex(r"X(t)=A\,\cos(\omega_0 t + \Theta)", color=TXT).scale(0.85)
        modelo.next_to(tit, DOWN, buff=0.4)
        self.play(Write(modelo))
        self.wait(0.9)
        self.play(modelo.animate.scale(0.72).to_edge(UP, buff=1.15))

        ax, lab = ejes([0, 8, 8], [-2.4, 2.4], ancho=8.8, alto=2.9, x_label="t")
        ax.shift(DOWN * 0.75)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        # ============================================ caso 1: fase fija
        cartel = VGroup(
            Text("fase FIJA", color=ROJO, weight=BOLD).scale(0.55),
            MathTex(r"\Theta=\theta_0", color=ROJO).scale(0.55),
        ).arrange(RIGHT, buff=0.25)
        cartel.next_to(ax, UP, buff=0.25).to_edge(LEFT, buff=0.9)

        fijas = [AMPS[i] * np.cos(W0 * T + 0.0) for i in range(K)]
        ondas = VGroup(*[linea_datos(ax, T, fijas[i], color=COLS[i], ancho=1.7)
                         for i in range(K)])
        self.play(FadeIn(cartel))
        self.play(LaggedStart(*[Create(o) for o in ondas], lag_ratio=0.09,
                              run_time=1.8))
        self.wait(0.5)

        media_fija = np.mean(fijas, axis=0)
        c_media = linea_datos(ax, T, media_fija, color=TXT, ancho=4.5)
        m_lbl = MathTex(r"\mu_X(t)", color=TXT).scale(0.62)
        m_lbl.next_to(ax, UP, buff=0.25).to_edge(RIGHT, buff=1.0)
        self.play(ondas.animate.set_stroke(opacity=0.28))
        self.play(Create(c_media, run_time=1.6), FadeIn(m_lbl))
        self.wait(0.5)

        mal = Text("la media oscila con el tiempo  →  NO es WSS",
                   color=ROJO).scale(0.55)
        mal.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(mal))
        self.wait(1.8)
        self.play(FadeOut(mal))

        # ============================================ caso 2: fase uniforme
        fases = _rng.uniform(-np.pi, np.pi, K)
        unif = [AMPS[i] * np.cos(W0 * T + fases[i]) for i in range(K)]
        ondas2 = VGroup(*[linea_datos(ax, T, unif[i], color=COLS[i], ancho=1.7)
                          for i in range(K)])
        ondas2.set_stroke(opacity=0.28)
        cartel2 = VGroup(
            Text("fase UNIFORME", color=VERDE, weight=BOLD).scale(0.55),
            MathTex(r"\Theta\sim U[-\pi,\pi]", color=VERDE).scale(0.55),
        ).arrange(RIGHT, buff=0.25)
        cartel2.move_to(cartel, aligned_edge=LEFT)

        media_unif = np.mean(unif, axis=0)
        c_media2 = linea_datos(ax, T, media_unif, color=TXT, ancho=4.5)

        self.play(Transform(ondas, ondas2), Transform(cartel, cartel2),
                  Transform(c_media, c_media2), run_time=2.0)
        self.wait(0.6)
        bien = Text("la media se aplana en cero, no importa el instante",
                    color=VERDE).scale(0.55)
        bien.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(bien))
        self.wait(1.6)
        self.play(FadeOut(bien))

        # ============================================ la cuenta
        self.play(FadeOut(VGroup(ax, lab, ondas, c_media, m_lbl, cartel)))

        pasos = VGroup(
            MathTex(r"\mu_X(t)=\mu_A\int_{-\pi}^{\pi}\frac{1}{2\pi}"
                    r"\cos(\omega_0 t+\theta)\,d\theta \;=\; 0",
                    color=TXT).scale(0.62),
            nota("un coseno integrado sobre un período entero da cero, "
                 "sin importar cuánto valga $t$", scale=0.44),
            MathTex(r"R_{XX}(t_1,t_2)=E[A^2]\,E\big[\cos(\omega_0 t_1+\Theta)"
                    r"\cos(\omega_0 t_2+\Theta)\big]", color=TXT).scale(0.58),
            nota(r"con $\cos\alpha\cos\beta=\tfrac12[\cos(\alpha-\beta)"
                 r"+\cos(\alpha+\beta)]$: el segundo término también se anula",
                 scale=0.44),
            MathTex(r"R_{XX}(t_1,t_2)=\frac{E[A^2]}{2}\,"
                    r"\cos\big(\omega_0(t_2-t_1)\big)", color=VERDE).scale(0.72),
        ).arrange(DOWN, buff=0.3)
        pasos.move_to(ORIGIN).shift(UP * 0.2)

        for m in pasos:
            self.play(FadeIn(m, shift=UP * 0.1), run_time=0.75)
            self.wait(0.35)
        self.wait(0.8)

        marco = SurroundingRectangle(pasos[-1], color=VERDE, buff=0.22,
                                     corner_radius=0.1, stroke_width=2.5)
        solo_tau = nota("depende solo de la diferencia  →  es WSS", scale=0.5)
        solo_tau.next_to(marco, DOWN, buff=0.3)
        self.play(Create(marco), FadeIn(solo_tau))
        self.wait(2.0)

        # ============================================ cierre
        self.play(FadeOut(VGroup(pasos, marco, solo_tau, modelo)))
        cierre = VGroup(
            Text("La fase aleatoria uniforme", color=TXT).scale(0.64),
            Text("borra el origen de tiempos.", color=VERDE).scale(0.64),
            nota("Y eso es exactamente lo que vuelve estacionario al proceso.",
                 scale=0.5),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.12))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.4)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
