"""Escena 1 - De donde sale el problema: PAM binario en ruido.

Se transmite a0 o a1, el canal le suma ruido, y en el receptor hay que
decidir cual fue. Ese es el problema de prueba de hipotesis.

    manim -pql s01_pam.py PAMenRuido
"""
from manim import *
import numpy as np
from comun import *

A0, A1 = 0.0, 2.4
SIGMA = 0.85


def gauss(x, mu, s):
    return np.exp(-(x - mu) ** 2 / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))


class PAMenRuido(Scene):
    def construct(self):
        configurar()

        tit = titulo("El problema: decidir qué se transmitió")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ la cadena PAM
        tx = MathTex(r"a[n]", color=VERDE).scale(0.65)
        canal = bloque(r"\text{canal}", color=INK, ancho=1.9, alto=0.85, scale=0.5)
        suma = Circle(radius=0.24, color=INK, stroke_width=2.5)
        mas = MathTex("+", color=INK).scale(0.6).move_to(suma)
        nodo = VGroup(suma, mas)
        rx = MathTex(r"r = a + v", color=AMBAR).scale(0.65)

        cadena = VGroup(tx, canal, nodo, rx).arrange(RIGHT, buff=0.85)
        cadena.next_to(tit, DOWN, buff=0.55)
        fs = VGroup(*[flecha(a.get_right(), b.get_left())
                      for a, b in zip(cadena[:-1], cadena[1:])])
        ruido = MathTex(r"v", color=ROJO).scale(0.65)
        ruido.next_to(nodo, UP, buff=0.55)
        f_ruido = flecha(ruido.get_bottom(), nodo.get_top())
        r_nota = nota("ruido", scale=0.4).next_to(ruido, RIGHT, buff=0.18)

        self.play(FadeIn(tx))
        self.play(GrowArrow(fs[0]), FadeIn(canal))
        self.play(GrowArrow(fs[1]), FadeIn(nodo))
        self.play(FadeIn(ruido), FadeIn(r_nota), GrowArrow(f_ruido))
        self.play(GrowArrow(fs[2]), FadeIn(rx))
        self.wait(1.0)

        # ------------------------------------------------ las dos hipotesis
        h0 = MathTex(r"H_0:\; a = a_0 \;\Rightarrow\; r = a_0 + v",
                     color=AZUL).scale(0.62)
        h1 = MathTex(r"H_1:\; a = a_1 \;\Rightarrow\; r = a_1 + v",
                     color=VERDE).scale(0.62)
        hip = VGroup(h0, h1).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        hip.next_to(cadena, DOWN, buff=0.6)
        self.play(FadeIn(h0, shift=RIGHT * 0.15))
        self.play(FadeIn(h1, shift=RIGHT * 0.15))
        self.wait(1.4)

        preg = Text("Medimos r. ¿Cuál de las dos ocurrió?", color=TXT).scale(0.6)
        preg.next_to(hip, DOWN, buff=0.55)
        self.play(FadeIn(preg))
        self.wait(1.8)

        # ------------------------------------------------ pasar a densidades
        self.play(FadeOut(VGroup(cadena, fs, ruido, f_ruido, r_nota, preg)),
                  hip.animate.scale(0.8).to_corner(UR, buff=0.5))

        ax, lab = ejes([-3.2, 5.6, 8.8], [0, 0.55], ancho=8.4, alto=2.9,
                       x_label="r")
        ax.shift(DOWN * 0.75)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        f0 = ax.plot(lambda r: gauss(r, A0, SIGMA), x_range=[-3.2, 5.6, 0.02],
                     color=AZUL, stroke_width=4)
        f1 = ax.plot(lambda r: gauss(r, A1, SIGMA), x_range=[-3.2, 5.6, 0.02],
                     color=VERDE, stroke_width=4)
        l0 = MathTex(r"f(r\,|\,H_0)", color=AZUL).scale(0.6)
        l0.next_to(ax.c2p(A0, gauss(A0, A0, SIGMA)), UL, buff=0.05)
        l1 = MathTex(r"f(r\,|\,H_1)", color=VERDE).scale(0.6)
        l1.next_to(ax.c2p(A1, gauss(A1, A1, SIGMA)), UR, buff=0.05)

        self.play(Create(f0), FadeIn(l0))
        self.play(Create(f1), FadeIn(l1))
        self.wait(0.6)

        marcas = VGroup(marca_x(ax, A0, "a_0", color=AZUL),
                        marca_x(ax, A1, "a_1", color=VERDE))
        self.play(FadeIn(marcas))
        self.wait(0.8)

        # ------------------------------------------------ una medicion concreta
        r_obs = 1.05
        punto = Dot(ax.c2p(r_obs, 0), color=AMBAR, radius=0.09)
        linea = DashedLine(ax.c2p(r_obs, 0), ax.c2p(r_obs, 0.50),
                           color=AMBAR, stroke_width=2.5, dash_length=0.09)
        r_lbl = MathTex("r", color=AMBAR).scale(0.62)
        r_lbl.next_to(punto, DOWN, buff=0.18)
        self.play(FadeIn(punto, scale=1.5), Create(linea), FadeIn(r_lbl))
        self.wait(0.8)

        duda = Text("cae justo en el medio: ninguna de las dos queda descartada",
                    color=AMBAR).scale(0.5)
        duda.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(duda))
        self.wait(2.0)
        self.play(FadeOut(duda))

        # ------------------------------------------------ la zona ambigua
        solape = ax.get_area(f0, x_range=(0.6, 5.6), color=ROJO, opacity=0.0,
                             stroke_width=0)
        m0 = ax.plot(lambda r: min(gauss(r, A0, SIGMA), gauss(r, A1, SIGMA)),
                     x_range=[-3.2, 5.6, 0.02], stroke_width=0)
        zona = ax.get_area(m0, x_range=(-3.2, 5.6), color=ROJO, opacity=0.45,
                           stroke_width=0)
        self.play(FadeIn(zona))
        zona_lbl = nota("acá las dos hipótesis son plausibles: siempre "
                        "vamos a equivocarnos algunas veces", scale=0.46)
        zona_lbl.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(zona_lbl))
        self.wait(2.2)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, f0, f1, l0, l1, marcas, punto, linea,
                                 r_lbl, zona, zona_lbl, hip, solape)))
        cierre = VGroup(
            Text("No se puede acertar siempre.", color=TXT).scale(0.66),
            Text("La pregunta es cómo equivocarse lo menos posible.",
                 color=AMBAR).scale(0.66),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.15))
        self.play(FadeIn(cierre[1], shift=UP * 0.15))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
