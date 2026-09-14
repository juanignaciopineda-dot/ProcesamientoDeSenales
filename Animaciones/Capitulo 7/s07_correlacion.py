"""Escena 7 - Covarianza, correlacion y coeficiente de correlacion.

La covarianza mide si las dos variables se mueven juntas; el coeficiente
la normaliza para que viva entre -1 y 1. Cierra con la trampa clasica:
no correlacionadas NO significa independientes.

    manim -pql s07_correlacion.py Correlacion
"""
from manim import *
import numpy as np
from comun import *

L = 3.2
N = 320
_rng = np.random.default_rng(4)


class Correlacion(Scene):
    def construct(self):
        configurar()

        tit = titulo("Covarianza y coeficiente de correlación")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ definiciones
        defs = VGroup(
            MathTex(r"r_{X,Y}=E[XY]", color=AZUL).scale(0.72),
            MathTex(r"\sigma_{X,Y}=E[XY]-E[X]E[Y]", color=VERDE).scale(0.72),
            MathTex(r"\rho_{X,Y}=\frac{\sigma_{X,Y}}{\sigma_X\,\sigma_Y}",
                    color=AMBAR).scale(0.72),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        defs.to_edge(RIGHT, buff=0.85).shift(DOWN * 0.25)
        rot = VGroup(
            nota("correlación", scale=0.42).next_to(defs[0], LEFT, buff=0.35),
            nota("covarianza", scale=0.42).next_to(defs[1], LEFT, buff=0.35),
            nota("coef. de correlación", scale=0.42).next_to(defs[2], LEFT,
                                                             buff=0.35),
        )

        # ------------------------------------------------ el plano
        ax = Axes(x_range=[-L, L, 1], y_range=[-L, L, 1],
                  x_length=4.5, y_length=4.5,
                  axis_config={"color": INK, "stroke_width": 2,
                               "include_ticks": False, "include_tip": True,
                               "tip_width": 0.14, "tip_height": 0.14})
        ax.to_edge(LEFT, buff=1.1).shift(DOWN * 0.4)
        x_l = MathTex("X", color=INK).scale(0.6).next_to(ax.x_axis.get_end(),
                                                          DR, buff=0.1)
        y_l = MathTex("Y", color=INK).scale(0.6).next_to(ax.y_axis.get_end(),
                                                          UR, buff=0.08)
        self.play(Create(ax), FadeIn(x_l), FadeIn(y_l))

        for d, r in zip(defs, rot):
            self.play(FadeIn(d, shift=LEFT * 0.15), FadeIn(r), run_time=0.6)
        self.wait(0.8)

        # ------------------------------------------------ la nube que gira
        estado = {"rho": 0.0}
        xs, ys = muestras_bivariadas(0.0, n=N, semilla=1)
        puntos = nube(ax, xs, ys, color=AZUL, radio=0.033, opacidad=0.62)
        self.play(FadeIn(puntos, lag_ratio=0.004, run_time=1.4))

        # alineado a la izquierda del recuadro: centrado se pisa con la
        # etiqueta del eje Y
        lector = always_redraw(lambda: VGroup(
            MathTex(r"\rho =", color=AMBAR).scale(0.75),
            DecimalNumber(estado["rho"], num_decimal_places=2, color=AMBAR,
                          include_sign=True).scale(0.75),
        ).arrange(RIGHT, buff=0.14).next_to(ax, UP, buff=0.3)
          .align_to(ax, LEFT))
        self.play(FadeIn(lector))
        self.wait(0.6)

        def mover_a(destino, semilla, run_time=1.6, etiqueta=None):
            nx, ny = muestras_bivariadas(destino, n=N, semilla=semilla)
            nueva = nube(ax, nx, ny, color=AZUL, radio=0.033, opacidad=0.62)
            estado["rho"] = destino
            anim = [Transform(puntos, nueva)]
            self.play(*anim, run_time=run_time)
            if etiqueta:
                self.play(FadeIn(etiqueta))
                self.wait(1.3)
                self.play(FadeOut(etiqueta))
            else:
                self.wait(0.5)

        e_pos = Text("se mueven juntas", color=VERDE).scale(0.52)
        e_pos.next_to(ax, DOWN, buff=0.35)
        e_neg = Text("se mueven al revés", color=ROJO).scale(0.52)
        e_neg.next_to(ax, DOWN, buff=0.35)
        e_cero = Text("sin relación lineal", color=INK).scale(0.52)
        e_cero.next_to(ax, DOWN, buff=0.35)

        mover_a(0.85, 2, etiqueta=e_pos)
        mover_a(0.99, 5)
        mover_a(0.0, 1, etiqueta=e_cero)
        mover_a(-0.85, 8, etiqueta=e_neg)
        mover_a(-0.99, 9)
        mover_a(0.55, 12)

        cota = MathTex(r"-1\;\leq\;\rho_{X,Y}\;\leq\;1", color=AMBAR).scale(0.72)
        cota.next_to(ax, DOWN, buff=0.4)
        self.play(Write(cota))
        self.wait(1.6)
        self.play(FadeOut(cota))

        # ------------------------------------------------ la trampa
        self.play(FadeOut(VGroup(defs, rot)))
        # en dos lineas y acotado a la mitad derecha: en una sola linea se
        # sale del cuadro
        trampa = VGroup(
            Text("No correlacionadas", color=ROJO, weight=BOLD).scale(0.56),
            VGroup(MathTex(r"\neq", color=ROJO).scale(0.72),
                   Text("independientes", color=ROJO, weight=BOLD).scale(0.56),
                   ).arrange(RIGHT, buff=0.22),
        ).arrange(DOWN, buff=0.16)
        trampa.move_to(RIGHT * 3.3 + UP * 1.9)
        self.play(FadeIn(trampa, shift=LEFT * 0.15))
        self.wait(0.8)

        # una parabola: Y queda determinada por X y sin embargo rho = 0.
        # La muestra de X se simetriza a mano: la correlacion de X con
        # cualquier funcion PAR de X es cero solo si X es simetrica, y con
        # una muestra al azar el ruido de muestreo daba rho ~ 0.2, que
        # contradecia el cartel de "rho = 0".
        medio = _rng.uniform(0.15, 2.2, N // 2)
        px = np.concatenate([medio, -medio])
        py = 0.58 * (px ** 2) - 1.4 + _rng.normal(0, 0.15, len(px))
        par = nube(ax, px, py, color=MAGENTA, radio=0.033, opacidad=0.7)
        estado["rho"] = float(np.corrcoef(px, py)[0, 1])
        self.play(Transform(puntos, par), run_time=1.6)
        self.wait(0.6)

        expl = VGroup(
            Text("Y está completamente", color=TXT).scale(0.48),
            Text("determinada por X…", color=TXT).scale(0.48),
            Text("…y sin embargo ρ ≈ 0", color=MAGENTA).scale(0.52),
            nota("ρ solo ve la relación LINEAL,", scale=0.45),
            nota("y una parábola no tiene", scale=0.45),
            nota("componente lineal.", scale=0.45),
        ).arrange(DOWN, buff=0.2)
        expl.next_to(trampa, DOWN, buff=0.55)
        for l in expl:
            self.play(FadeIn(l, shift=UP * 0.1), run_time=0.7)
        self.wait(2.4)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, x_l, y_l, puntos, lector, trampa, expl)))
        # las flechas dobles (U+27F9) no existen en la fuente de Text() y
        # salen como cajas vacias: van por MathTex
        def implica(izq, der, flecha, color):
            return VGroup(Text(izq, color=color).scale(0.58),
                          MathTex(flecha, color=color).scale(0.72),
                          Text(der, color=color).scale(0.58)
                          ).arrange(RIGHT, buff=0.3)

        cierre = VGroup(
            implica("Independientes", "no correlacionadas",
                    r"\Longrightarrow", VERDE),
            implica("No correlacionadas", "independientes",
                    r"\not\Longrightarrow", ROJO),
            nota("La excepción importante: si son conjuntamente gaussianas,\n"
                 "no correlacionadas SÍ implica independientes.", scale=0.5),
        ).arrange(DOWN, buff=0.34)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.12))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.6)
        self.play(FadeIn(cierre[2]))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
