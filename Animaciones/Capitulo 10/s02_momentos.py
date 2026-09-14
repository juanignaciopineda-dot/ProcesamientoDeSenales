"""Escena 2 - Momentos de primer y segundo orden.

La media es un promedio VERTICAL sobre el ensemble, no a lo largo del
tiempo. Y la autocorrelacion mide cuanto se parecen dos cortes: se ve
como una nube de puntos que se inclina cuando t2 se acerca a t1.

    manim -pql s02_momentos.py Momentos
"""
from manim import *
import numpy as np
from comun import *

N = 400
T = np.linspace(0, 10, N)
K = 7
COLS = [AZUL, AMBAR, VERDE, MAGENTA, ROJO, "#5ec8d8", "#d8c65e"]
RHO_TIEMPO = 1.5        # escala de correlacion del proceso simulado


def realizacion(semilla):
    """Proceso de media no nula y suave, para que la media se vea."""
    rng = np.random.default_rng(100 + semilla)
    y = np.zeros_like(T)
    for _ in range(5):
        f = rng.uniform(0.25, 1.4)
        y += rng.normal(0, 1) * np.sin(2 * np.pi * f * T / T[-1] * 2
                                       + rng.uniform(0, 2 * np.pi))
    return 1.15 * y / np.std(y)


DATOS = [realizacion(i) for i in range(K)]
MEDIA = np.mean(DATOS, axis=0)


class Momentos(Scene):
    def construct(self):
        configurar()

        tit = titulo("Los momentos: promedios sobre el ensemble")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el ensemble, superpuesto
        ax, lab = ejes([0, 10, 10], [-3.0, 3.0], ancho=7.6, alto=3.2,
                       x_label="t")
        ax.shift(LEFT * 1.6 + DOWN * 0.5)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)

        ondas = VGroup(*[linea_datos(ax, T, DATOS[i], color=COLS[i], ancho=1.6)
                         for i in range(K)])
        self.play(Create(ax), FadeIn(lab))
        self.play(LaggedStart(*[Create(o) for o in ondas], lag_ratio=0.13,
                              run_time=2.2))
        self.wait(0.5)

        # ------------------------------------------------ la media: promedio vertical
        t1 = 3.4
        corte = DashedLine(ax.c2p(t1, -3.0), ax.c2p(t1, 3.0), color=TXT,
                           stroke_width=2.4, dash_length=0.1)
        pts = VGroup(*[Dot(ax.c2p(t1, np.interp(t1, T, DATOS[i])),
                           color=COLS[i], radius=0.055) for i in range(K)])
        flecha_v = Arrow(ax.c2p(t1, 2.7), ax.c2p(t1, -2.7), color=TXT,
                         stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.06)
        aviso = VGroup(
            Text("se promedia hacia abajo,", color=TXT).scale(0.5),
            Text("no a lo largo del tiempo", color=AMBAR).scale(0.5),
        ).arrange(DOWN, buff=0.12)
        aviso.to_edge(RIGHT, buff=0.5).shift(UP * 1.3)

        self.play(Create(corte), FadeIn(pts))
        self.play(GrowArrow(flecha_v), FadeIn(aviso, shift=LEFT * 0.2))
        punto_medio = Dot(ax.c2p(t1, np.interp(t1, T, MEDIA)), color=TXT,
                          radius=0.085)
        self.play(*[p.animate.move_to(punto_medio.get_center()) for p in pts],
                  run_time=1.1)
        self.add(punto_medio)
        self.remove(pts)
        self.wait(0.8)
        self.play(FadeOut(flecha_v), FadeOut(aviso))

        # la media completa, barriendo t
        curva_media = linea_datos(ax, T, MEDIA, color=TXT, ancho=4.0)
        media_lbl = MathTex(r"\mu_X(t)=E[X(t)]", color=TXT).scale(0.62)
        media_lbl.to_edge(RIGHT, buff=0.5).shift(UP * 1.3)
        self.play(ondas.animate.set_stroke(opacity=0.30))
        self.play(Create(curva_media, run_time=2.0), FadeIn(media_lbl))
        self.wait(0.5)
        media_n = nota("es una función del tiempo, no un número", scale=0.44)
        media_n.next_to(media_lbl, DOWN, buff=0.2)
        self.play(FadeIn(media_n))
        self.wait(1.6)

        # ------------------------------------------------ segundo momento
        self.play(FadeOut(VGroup(media_lbl, media_n, corte, punto_medio,
                                 curva_media)),
                  ondas.animate.set_stroke(opacity=1.0))

        seg = MathTex(r"R_{XX}(t_1,t_2)=E[X(t_1)\,X(t_2)]", color=AMBAR).scale(0.62)
        seg.to_edge(RIGHT, buff=0.45).shift(UP * 1.6)
        seg_n = nota("¿cuánto se parecen\ndos cortes distintos?", scale=0.44)
        seg_n.next_to(seg, DOWN, buff=0.22)
        self.play(FadeIn(seg), FadeIn(seg_n))
        self.wait(0.6)

        # dos cortes y la nube de dispersion
        t2v = ValueTracker(8.2)
        c1 = DashedLine(ax.c2p(t1, -3.0), ax.c2p(t1, 3.0), color=AZUL,
                        stroke_width=2.4, dash_length=0.1)
        c2 = always_redraw(lambda: DashedLine(
            ax.c2p(t2v.get_value(), -3.0), ax.c2p(t2v.get_value(), 3.0),
            color=AMBAR, stroke_width=2.4, dash_length=0.1))
        l1 = MathTex("t_1", color=AZUL).scale(0.55).next_to(ax.c2p(t1, -3.0),
                                                            DOWN, buff=0.12)
        l2 = always_redraw(lambda: MathTex("t_2", color=AMBAR).scale(0.55)
                           .next_to(ax.c2p(t2v.get_value(), -3.0), DOWN, buff=0.12))
        self.play(Create(c1), Create(c2), FadeIn(l1), FadeIn(l2))

        # panel de dispersion X(t1) vs X(t2)
        ax_d, _ = ejes([-3, 3, 3], [-3, 3, 3], ancho=2.5, alto=2.5, tip=False)
        ax_d.to_edge(RIGHT, buff=0.75).shift(DOWN * 1.35)
        d_x = MathTex("X(t_1)", color=AZUL).scale(0.45)
        d_x.next_to(ax_d, DOWN, buff=0.12)
        d_y = MathTex("X(t_2)", color=AMBAR).scale(0.45)
        d_y.next_to(ax_d, LEFT, buff=0.1).rotate(PI / 2)

        nube = always_redraw(lambda: VGroup(*[
            Dot(ax_d.c2p(np.interp(t1, T, DATOS[i]),
                         np.interp(t2v.get_value(), T, DATOS[i])),
                color=COLS[i], radius=0.052) for i in range(K)]))

        self.play(Create(ax_d), FadeIn(d_x), FadeIn(d_y))
        self.play(FadeIn(nube))
        self.wait(0.8)

        lejos = nota("lejos: la nube no tiene forma\n→ poca correlación",
                     scale=0.42)
        lejos.next_to(ax_d, DOWN, buff=0.42)
        self.play(FadeIn(lejos))
        self.wait(1.4)
        self.play(FadeOut(lejos))

        self.play(t2v.animate.set_value(t1 + 0.35), run_time=3.2,
                  rate_func=rate_functions.ease_in_out_sine)
        cerca = nota("cerca: los puntos se alinean\n→ mucha correlación",
                     scale=0.42)
        cerca.next_to(ax_d, DOWN, buff=0.42)
        self.play(FadeIn(cerca))
        self.wait(1.8)
        self.play(FadeOut(cerca))

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, ondas, c1, c2, l1, l2, ax_d, d_x,
                                 d_y, nube, seg, seg_n)))
        cierre = VGroup(
            MathTex(r"\mu_X(t)=E[X(t)]", color=TXT).scale(0.72),
            MathTex(r"R_{XX}(t_1,t_2)=E[X(t_1)X(t_2)]", color=AMBAR).scale(0.72),
            MathTex(r"C_{XX}(t_1,t_2)=R_{XX}(t_1,t_2)-\mu_X(t_1)\mu_X(t_2)",
                    color=VERDE).scale(0.72),
        ).arrange(DOWN, buff=0.32)
        cierre.move_to(ORIGIN).shift(UP * 0.35)
        razon = VGroup(
            nota("¿Por qué alcanza con estos dos?", scale=0.5),
            nota("porque un proceso gaussiano queda determinado por ellos,",
                 scale=0.46),
            nota("y porque es todo lo que un sistema LTI necesita.", scale=0.46),
        ).arrange(DOWN, buff=0.12)
        razon.next_to(cierre, DOWN, buff=0.55)

        for m in cierre:
            self.play(FadeIn(m, shift=UP * 0.1), run_time=0.55)
        self.wait(0.5)
        self.play(FadeIn(razon))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre, razon)))
        self.wait(0.3)
