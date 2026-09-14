"""Escena 6 - Distribucion conjunta y marginales.

La conjunta vive en R^2. Las marginales se obtienen proyectando: integrar
sobre la otra variable. Y el punto importante: las marginales NO
determinan la conjunta.

    manim -pql s06_conjunta.py Conjunta
"""
from manim import *
import numpy as np
from comun import *

L = 3.0


class Conjunta(Scene):
    def construct(self):
        configurar()

        tit = titulo("La conjunta y sus marginales")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        intro = Text("Con dos variables a la vez —una señal transmitida y la "
                     "recibida, por ejemplo—", color=INK).scale(0.5)
        intro.next_to(tit, DOWN, buff=0.35)
        self.play(FadeIn(intro))
        self.wait(1.4)
        self.play(FadeOut(intro))

        # ------------------------------------------------ el plano
        ax = Axes(x_range=[-L, L, 1], y_range=[-L, L, 1],
                  x_length=4.6, y_length=4.6,
                  axis_config={"color": INK, "stroke_width": 2,
                               "include_ticks": False, "include_tip": True,
                               "tip_width": 0.14, "tip_height": 0.14})
        ax.shift(LEFT * 1.7 + DOWN * 0.45)
        x_l = MathTex("x", color=INK).scale(0.6).next_to(ax.x_axis.get_end(),
                                                          DR, buff=0.1)
        y_l = MathTex("y", color=INK).scale(0.6).next_to(ax.y_axis.get_end(),
                                                          UR, buff=0.08)
        self.play(Create(ax), FadeIn(x_l), FadeIn(y_l))

        rho = ValueTracker(0.72)
        xs, ys = muestras_bivariadas(0.72, n=300, semilla=3)

        puntos = nube(ax, xs, ys, color=AZUL, radio=0.032, opacidad=0.6)
        elipses = always_redraw(lambda: VGroup(*[
            elipse_nivel(ax, rho.get_value(), k=k, color=AMBAR,
                         ancho=2.6 - 0.5 * i)
            for i, k in enumerate((1.0, 2.0))]))

        self.play(FadeIn(puntos, lag_ratio=0.004, run_time=1.6))
        conj_lbl = MathTex(r"f_{X,Y}(x,y)", color=AZUL).scale(0.62)
        conj_lbl.next_to(ax, UP, buff=0.2)
        self.play(FadeIn(elipses), FadeIn(conj_lbl))
        self.wait(0.8)

        r2 = nota("vive en el plano: la probabilidad de una región\n"
                  "es una integral doble sobre esa región", scale=0.45)
        r2.next_to(ax, DOWN, buff=0.35)
        self.play(FadeIn(r2))
        self.wait(1.8)

        # una region concreta
        region = Rectangle(width=1.5, height=1.2, color=VERDE, stroke_width=3,
                           fill_color=VERDE, fill_opacity=0.22)
        region.move_to(ax.c2p(0.7, 0.6))
        int_doble = MathTex(r"P\big((X,Y)\in R\big)=\iint_R f_{X,Y}(x,y)\,dx\,dy",
                            color=VERDE).scale(0.55)
        int_doble.move_to(r2)
        self.play(Create(region), FadeOut(r2), FadeIn(int_doble))
        self.wait(2.0)
        self.play(FadeOut(region), FadeOut(int_doble))

        # ------------------------------------------------ las marginales
        ax_mx = Axes(x_range=[-L, L, 1], y_range=[0, 0.55],
                     x_length=4.6, y_length=1.35,
                     axis_config={"color": INK, "stroke_width": 2,
                                  "include_ticks": False, "include_tip": False})
        ax_mx.next_to(ax, DOWN, buff=0.35)
        mx = ax_mx.plot(lambda x: gauss(x, 0, 1), x_range=[-L, L, 0.02],
                        color=VERDE, stroke_width=3.5, use_smoothing=False)
        amx = ax_mx.get_area(mx, x_range=(-L, L), color=VERDE, opacity=0.2,
                             stroke_width=0)
        mx_lbl = MathTex(r"f_X(x)=\int f_{X,Y}(x,y)\,dy",
                         color=VERDE).scale(0.5)
        mx_lbl.next_to(ax_mx, DOWN, buff=0.15)

        ax_my = Axes(x_range=[-L, L, 1], y_range=[0, 0.55],
                     x_length=4.6, y_length=1.35,
                     axis_config={"color": INK, "stroke_width": 2,
                                  "include_ticks": False, "include_tip": False})
        ax_my.rotate(PI / 2).next_to(ax, RIGHT, buff=0.35)
        my = ax_my.plot(lambda x: gauss(x, 0, 1), x_range=[-L, L, 0.02],
                        color=MAGENTA, stroke_width=3.5, use_smoothing=False)
        amy = ax_my.get_area(my, x_range=(-L, L), color=MAGENTA, opacity=0.2,
                             stroke_width=0)
        my_lbl = MathTex(r"f_Y(y)=\int f_{X,Y}(x,y)\,dx",
                         color=MAGENTA).scale(0.5)
        my_lbl.next_to(ax_my, RIGHT, buff=0.2)

        proy = Text("proyectar = integrar sobre la otra variable",
                    color=INK).scale(0.5)
        proy.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(proy))

        self.play(Create(ax_mx), Create(mx), FadeIn(amx), FadeIn(mx_lbl),
                  run_time=1.4)
        self.wait(0.5)
        self.play(Create(ax_my), Create(my), FadeIn(amy), FadeIn(my_lbl),
                  run_time=1.4)
        self.wait(1.6)
        self.play(FadeOut(proy))

        # ------------------------------------------------ el punto clave
        aviso = Text("Ojo: las marginales NO determinan la conjunta",
                     color=ROJO).scale(0.58)
        aviso.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(aviso, shift=UP * 0.15))
        self.wait(1.0)

        # se cambia rho: la nube gira, las marginales quedan iguales
        for destino, semilla in ((-0.72, 11), (0.0, 21), (0.72, 3)):
            nuevos_x, nuevos_y = muestras_bivariadas(destino, n=300,
                                                     semilla=semilla)
            nueva_nube = nube(ax, nuevos_x, nuevos_y, color=AZUL, radio=0.032,
                              opacidad=0.6)
            self.play(Transform(puntos, nueva_nube),
                      rho.animate.set_value(destino), run_time=1.5)
            self.wait(0.7)

        remate = nota("la nube cambió por completo y las dos marginales "
                      "siguen siendo las mismas", scale=0.47)
        remate.next_to(aviso, UP, buff=0.2)
        self.play(FadeIn(remate))
        self.wait(2.4)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, x_l, y_l, puntos, elipses, conj_lbl,
                                 ax_mx, mx, amx, mx_lbl, ax_my, my, amy,
                                 my_lbl, aviso, remate)))
        cierre = VGroup(
            Text("Las marginales son sombras de la conjunta.", color=TXT).scale(0.62),
            nota("Muchas conjuntas distintas proyectan la misma sombra.",
                 scale=0.5),
            Text("Lo que falta es la dependencia entre las dos:",
                 color=INK).scale(0.55),
            Text("de eso se ocupa la covarianza.", color=AMBAR).scale(0.6),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.12))
        self.play(FadeIn(cierre[1]))
        self.wait(0.6)
        self.play(FadeIn(cierre[2]), FadeIn(cierre[3], shift=UP * 0.12))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
