"""Escena 1 - Que es un proceso aleatorio: el ensemble.

La idea central del capitulo: una VA mapea un resultado a un numero, un
proceso mapea un resultado a UNA SENAL ENTERA. Y hay dos formas de
mirarlo: congelar t (queda una VA) o congelar el resultado (queda una
senal deterministica).

    manim -pql s01_ensemble.py Ensemble
"""
from manim import *
import numpy as np
from comun import *

N = 400
T = np.linspace(0, 10, N)
K = 5                       # realizaciones a la vista


def realizacion(semilla, escala=1.0):
    rng = np.random.default_rng(semilla)
    y = np.zeros_like(T)
    for _ in range(6):
        f = rng.uniform(0.3, 2.2)
        y += rng.normal(0, 1) * np.sin(2 * np.pi * f * T / T[-1] * 2
                                       + rng.uniform(0, 2 * np.pi))
    return escala * y / np.std(y)


class Ensemble(Scene):
    def construct(self):
        configurar()

        tit = titulo("¿Qué es un proceso aleatorio?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ VA contra proceso
        comp = VGroup(
            VGroup(Text("variable aleatoria", color=AZUL).scale(0.6),
                   MathTex(r"\text{resultado}\;\longmapsto\;\text{un número}",
                           color=INK).scale(0.6)).arrange(DOWN, buff=0.2),
            VGroup(Text("proceso aleatorio", color=AMBAR).scale(0.6),
                   MathTex(r"\text{resultado}\;\longmapsto\;"
                           r"\text{una señal entera}", color=INK).scale(0.6)
                   ).arrange(DOWN, buff=0.2),
        ).arrange(RIGHT, buff=1.5)
        comp.move_to(ORIGIN).shift(UP * 0.3)
        self.play(FadeIn(comp[0], shift=RIGHT * 0.2))
        self.wait(0.7)
        self.play(FadeIn(comp[1], shift=LEFT * 0.2))
        self.wait(1.6)
        self.play(FadeOut(comp))

        # ------------------------------------------------ el ensemble
        ejes_g = VGroup()
        ondas = VGroup()
        colores = [AZUL, AMBAR, VERDE, MAGENTA, ROJO]
        alturas = np.linspace(2.05, -2.15, K)
        datos = []
        for i in range(K):
            ax, _ = ejes([0, 10, 10], [-2.6, 2.6], ancho=6.6, alto=0.92,
                         tip=False)
            ax.move_to(np.array([-0.9, alturas[i], 0]))
            y = realizacion(i + 1)
            datos.append(y)
            onda = linea_datos(ax, T, y, color=colores[i], ancho=2.0)
            # solo la linea de base: el eje vertical de cada fila no aporta
            # nada y deja un muñon suelto a la izquierda
            base = Line(ax.c2p(0, 0), ax.c2p(10, 0), color=INK,
                        stroke_width=1.0).set_opacity(0.45)
            ejes_g.add(VGroup(base))
            ondas.add(onda)
            ejes_g[i].ax = ax          # se guarda para poder usar c2p despues

        etiqueta_ens = subtitulo("el ensemble: todas las señales posibles",
                                 scale=0.5, color=INK)
        etiqueta_ens.next_to(tit, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)

        self.play(FadeIn(etiqueta_ens))
        for i in range(K):
            self.play(FadeIn(ejes_g[i]), Create(ondas[i]), run_time=0.42)
        self.wait(0.8)

        # ------------------------------------------------ lectura 1: congelar t
        t1 = 4.3
        corte = DashedLine(
            ejes_g[0].ax.c2p(t1, 2.6), ejes_g[K - 1].ax.c2p(t1, -2.6),
            color=TXT, stroke_width=2.5, dash_length=0.11)
        puntos = VGroup(*[
            Dot(ejes_g[i].ax.c2p(t1, np.interp(t1, T, datos[i])),
                color=colores[i], radius=0.065) for i in range(K)])

        lect1 = VGroup(
            Text("congelás el tiempo", color=TXT).scale(0.52),
            MathTex(r"X(t_1)\;\text{es una variable aleatoria}",
                    color=TXT).scale(0.55),
        ).arrange(DOWN, buff=0.16)
        lect1.to_edge(RIGHT, buff=0.55).shift(UP * 1.2)

        self.play(Create(corte), FadeIn(etiqueta_ens.copy().set_opacity(0)))
        self.play(LaggedStart(*[GrowFromCenter(p) for p in puntos], lag_ratio=0.12))
        self.play(FadeIn(lect1, shift=LEFT * 0.2))
        self.wait(1.0)

        # los valores del corte se juntan en una nube: es la VA
        destino = np.array([4.55, -0.35, 0])
        copias = VGroup(*[p.copy() for p in puntos])
        self.add(copias)
        self.play(*[c.animate.move_to(destino + UP * (0.30 * (i - (K - 1) / 2)))
                    for i, c in enumerate(copias)], run_time=1.2)
        llave = Brace(copias, RIGHT, color=INK)
        llave_lbl = MathTex(r"X(t_1)", color=TXT).scale(0.6)
        llave_lbl.next_to(llave, RIGHT, buff=0.12)
        self.play(FadeIn(llave), FadeIn(llave_lbl))
        self.wait(1.5)
        self.play(FadeOut(VGroup(copias, llave, llave_lbl, lect1)))

        # ------------------------------------------------ lectura 2: congelar el resultado
        lect2 = VGroup(
            Text("congelás el resultado", color=TXT).scale(0.52),
            MathTex(r"x(t)\;\text{es una señal determinística}",
                    color=TXT).scale(0.55),
        ).arrange(DOWN, buff=0.16)
        lect2.to_edge(RIGHT, buff=0.55).shift(UP * 1.2)

        self.play(FadeOut(corte), FadeOut(puntos), FadeIn(lect2, shift=LEFT * 0.2))
        elegida = 2
        otros = VGroup(*[VGroup(ejes_g[i], ondas[i])
                         for i in range(K) if i != elegida])
        self.play(otros.animate.set_stroke(opacity=0.18),
                  Indicate(ondas[elegida], scale_factor=1.03, color=VERDE),
                  run_time=1.2)
        self.wait(1.6)
        self.play(otros.animate.set_stroke(opacity=1.0), FadeOut(lect2))
        self.wait(0.4)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ejes_g, ondas, etiqueta_ens)))
        cierre = VGroup(
            Text("Un proceso aleatorio no es una señal:", color=TXT).scale(0.62),
            Text("es una familia entera de señales,", color=AMBAR).scale(0.62),
            Text("y el azar elige cuál te toca.", color=AMBAR).scale(0.62),
        ).arrange(DOWN, buff=0.2)
        cierre.move_to(ORIGIN).shift(UP * 0.3)
        eq = MathTex(r"X(t)\;=\;A\,\sin(\Phi t + \Theta)", color=AZUL).scale(0.8)
        eq.next_to(cierre, DOWN, buff=0.65)
        eq_n = nota("los osciladores del galpón: lo aleatorio es cuál te tocó",
                    scale=0.44)
        eq_n.next_to(eq, DOWN, buff=0.2)

        for l in cierre:
            self.play(FadeIn(l, shift=UP * 0.12), run_time=0.6)
        self.wait(0.5)
        self.play(Write(eq), FadeIn(eq_n))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre, eq, eq_n)))
        self.wait(0.3)
