"""Escena 6 - Ergodicidad: promedio temporal contra promedio de ensemble.

En el laboratorio tenes UNA grabacion, no el ensemble. La pregunta es si
promediar a lo largo del tiempo esa unica realizacion da lo mismo que
promediar hacia abajo sobre todas. A veces si (ergodico) y a veces no
(el contraejemplo de las baterias).

    manim -pql s06_ergodicidad.py Ergodicidad
"""
from manim import *
import numpy as np
from comun import *

N = 600
T = np.linspace(0, 12, N)
K = 5
COLS = [AZUL, AMBAR, VERDE, MAGENTA, ROJO]


def realizacion(semilla):
    rng = np.random.default_rng(500 + semilla)
    y = np.zeros_like(T)
    for _ in range(8):
        f = rng.uniform(0.4, 2.6)
        y += rng.normal(0, 1) * np.sin(2 * np.pi * f * T / T[-1] * 2
                                       + rng.uniform(0, 2 * np.pi))
    return 0.9 * y / np.std(y)


ERG = [realizacion(i) for i in range(K)]
BAT = [np.full_like(T, v) for v in (1.55, 0.75, -0.15, -0.95, -1.7)]


class Ergodicidad(Scene):
    def construct(self):
        configurar()

        tit = titulo("Ergodicidad: ¿alcanza con una sola grabación?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        planteo = VGroup(
            Text("En el laboratorio tenés UNA realización.", color=TXT).scale(0.58),
            Text("¿Podés estimar la estadística del ensemble con ella?",
                 color=AMBAR).scale(0.58),
        ).arrange(DOWN, buff=0.2)
        planteo.move_to(ORIGIN).shift(UP * 0.3)
        self.play(FadeIn(planteo[0], shift=UP * 0.12))
        self.wait(0.6)
        self.play(FadeIn(planteo[1], shift=UP * 0.12))
        self.wait(1.6)
        self.play(FadeOut(planteo))

        # ------------------------------------------------ el ensemble
        filas = VGroup()
        ondas = VGroup()
        alturas = np.linspace(1.75, -1.55, K)
        for i in range(K):
            ax, _ = ejes([0, 12, 12], [-2.4, 2.4], ancho=6.4, alto=0.78,
                         tip=False)
            ax.move_to(np.array([-1.4, alturas[i], 0]))
            b = Line(ax.c2p(0, 0), ax.c2p(12, 0), color=INK,
                     stroke_width=0.9).set_stroke(opacity=0.4)
            filas.add(b)
            filas[i].ax = ax
            ondas.add(linea_datos(ax, T, ERG[i], color=COLS[i], ancho=1.8))

        self.play(FadeIn(filas), LaggedStart(*[Create(o) for o in ondas],
                                             lag_ratio=0.12, run_time=1.6))
        self.wait(0.4)

        # ------------------------------------------------ los dos promedios
        tc = 5.2
        fl_v = Arrow(filas[0].ax.c2p(tc, 2.4), filas[K - 1].ax.c2p(tc, -2.4),
                     color=AMBAR, stroke_width=4, buff=0,
                     max_tip_length_to_length_ratio=0.07)
        lbl_v = VGroup(
            Text("promedio de ensemble", color=AMBAR).scale(0.46),
            MathTex(r"E[x(t)]", color=AMBAR).scale(0.55),
        ).arrange(DOWN, buff=0.1)
        lbl_v.next_to(fl_v, UP, buff=0.15)

        # fila 0 (azul) a proposito: si se usa la fila verde, la flecha
        # verde se confunde con la propia realizacion
        fila_el = 0
        fl_h = Arrow(filas[fila_el].ax.c2p(0.2, 0), filas[fila_el].ax.c2p(11.8, 0),
                     color=VERDE, stroke_width=4, buff=0,
                     max_tip_length_to_length_ratio=0.05)
        lbl_h = VGroup(
            Text("promedio temporal", color=VERDE).scale(0.46),
            MathTex(r"\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}x(t)\,dt",
                    color=VERDE).scale(0.5),
        ).arrange(DOWN, buff=0.1)
        lbl_h.next_to(filas[fila_el].ax, RIGHT, buff=0.35).shift(DOWN * 0.15)

        self.play(GrowArrow(fl_v), FadeIn(lbl_v))
        self.wait(1.0)
        self.play(GrowArrow(fl_h), FadeIn(lbl_h))
        self.wait(1.2)

        preg = MathTex(r"\text{¿dan lo mismo?}", color=TXT).scale(0.7)
        preg.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(preg))
        self.wait(1.4)

        si = VGroup(
            Text("Si dan lo mismo, el proceso es", color=TXT).scale(0.55),
            Text("ERGÓDICO", color=VERDE, weight=BOLD).scale(0.7),
        ).arrange(RIGHT, buff=0.25)
        si.to_edge(DOWN, buff=0.42)
        self.play(FadeOut(preg), FadeIn(si))
        self.wait(1.8)

        # ------------------------------------------------ el contraejemplo
        self.play(FadeOut(VGroup(fl_v, lbl_v, fl_h, lbl_h, si)))

        contra = Text("El contraejemplo: un cajón de baterías",
                      color=ROJO).scale(0.58)
        contra.to_edge(DOWN, buff=0.5)
        ondas_b = VGroup(*[linea_datos(filas[i].ax, T, BAT[i], color=COLS[i],
                                       ancho=2.6) for i in range(K)])
        self.play(Transform(ondas, ondas_b), FadeIn(contra), run_time=1.6)
        self.wait(1.0)

        expl = VGroup(
            nota("cada realización es una constante: el voltaje de esa batería",
                 scale=0.46),
            nota("promediar en el tiempo te devuelve ESA batería,", scale=0.46),
            nota("no el promedio del cajón", scale=0.46),
        ).arrange(DOWN, buff=0.12)
        expl.to_edge(DOWN, buff=0.42)
        self.play(FadeOut(contra), FadeIn(expl))
        self.wait(2.2)
        self.play(FadeOut(expl))

        veredicto_b = VGroup(
            Text("SSS", color=VERDE, weight=BOLD).scale(0.6),
            Text("pero NO ergódico", color=ROJO, weight=BOLD).scale(0.6),
        ).arrange(RIGHT, buff=0.3)
        veredicto_b.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(veredicto_b))
        self.wait(1.8)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(filas, ondas, veredicto_b)))
        cierre = VGroup(
            Text("Estacionariedad y ergodicidad son cosas distintas:",
                 color=TXT).scale(0.58),
            Text("la primera dice que la estadística no cambia con el tiempo,",
                 color=INK).scale(0.52),
            Text("la segunda que una sola realización representa a todas.",
                 color=INK).scale(0.52),
        ).arrange(DOWN, buff=0.22)
        crit = VGroup(
            nota("Criterio útil: un proceso WSS cuya autocovarianza tiende a "
                 "cero", scale=0.48),
            nota("cuando el lag crece es ergódico en media.", scale=0.48),
        ).arrange(DOWN, buff=0.1)
        todo = VGroup(cierre, crit).arrange(DOWN, buff=0.6)
        todo.move_to(ORIGIN)

        self.play(FadeIn(cierre[0], shift=UP * 0.12))
        self.play(FadeIn(cierre[1]), FadeIn(cierre[2]))
        self.wait(0.8)
        self.play(FadeIn(crit))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, todo)))
        self.wait(0.3)
