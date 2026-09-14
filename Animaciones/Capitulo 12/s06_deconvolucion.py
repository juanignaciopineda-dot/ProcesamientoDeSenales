"""Escena 6 - Deconvolucion: por que no alcanza con invertir.

La senal pasa por un sensor que la borronea y ademas se le suma ruido.
El filtro inverso 1/G amplifica brutalmente el ruido justo donde |G| es
chico. Wiener resuelve eso solo.

    manim -pql s06_deconvolucion.py Deconvolucion
"""
from manim import *
import numpy as np
from comun import *

A_G = 0.75          # G(z) = 1/(1 - a z^-1): sensor pasabajos (borronea)
SIG_V = 0.5         # intensidad del ruido de medicion
ESC = 3.2           # tope del cuadro
K = 1.6             # escala comun a las tres curvas


def modG2(w):
    """|G(e^{jW})|^2."""
    return 1.0 / (1 - 2 * A_G * np.cos(w) + A_G ** 2)


def modG(w):
    return np.sqrt(modG2(w))


G0 = modG(0.0)


def ganancia_sensor(w):
    """|G| normalizado a 1 en continua: se ve que corta las altas."""
    return modG(w) / G0 * 2.2


def inverso(w):
    """|1/G|: chico en continua, explota en alta frecuencia."""
    return min(ESC, K / modG(w))


def wiener(w):
    """|H_Wiener| = |1/G| * Drr/(Drr+Dvv), con Dyy plano.

    Sigue al inverso mientras hay señal, y se da vuelta cuando el ruido
    empieza a dominar: esa es toda la diferencia.
    """
    Drr = modG2(w)
    return min(ESC, K / modG(w) * Drr / (Drr + SIG_V))


class Deconvolucion(Scene):
    def construct(self):
        configurar()

        tit = titulo("Deconvolución: por qué no alcanza con invertir")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el planteo
        y = MathTex("y[n]", color=VERDE).scale(0.6)
        g = bloque("G(z)", color=AMBAR, ancho=1.5, alto=0.75, scale=0.5)
        suma = Circle(radius=0.22, color=INK, stroke_width=2.5)
        mas = MathTex("+", color=INK).scale(0.6).move_to(suma)
        nodo = VGroup(suma, mas)
        h = bloque("H(z)", color=AZUL, ancho=1.5, alto=0.75, scale=0.5)
        yh = MathTex(r"\hat{y}[n]", color=AZUL).scale(0.6)

        cadena = VGroup(y, g, nodo, h, yh).arrange(RIGHT, buff=0.75)
        # con buff chico, la etiqueta v[n] (que va arriba del sumador) le
        # pega al titulo: se baja toda la cadena
        cadena.next_to(tit, DOWN, buff=0.95)
        fs = VGroup(*[flecha(a.get_right(), b.get_left())
                      for a, b in zip(cadena[:-1], cadena[1:])])
        v = MathTex("v[n]", color=ROJO).scale(0.55)
        v.next_to(nodo, UP, buff=0.55)
        fv = flecha(v.get_bottom(), nodo.get_top(), color=ROJO)
        r_lbl = MathTex("r[n]", color=AMBAR).scale(0.5)
        r_lbl.next_to(fs[1], UP, buff=0.08)
        x_lbl = MathTex("x[n]", color=ROJO).scale(0.5)
        x_lbl.next_to(fs[2], UP, buff=0.08)

        self.play(FadeIn(y), GrowArrow(fs[0]), FadeIn(g))
        self.play(GrowArrow(fs[1]), FadeIn(r_lbl), FadeIn(nodo))
        self.play(FadeIn(v), GrowArrow(fv))
        self.play(GrowArrow(fs[2]), FadeIn(x_lbl), FadeIn(h))
        self.play(GrowArrow(fs[3]), FadeIn(yh))
        self.wait(0.6)

        sensor = nota("el sensor borronea la señal", scale=0.42)
        sensor.next_to(g, DOWN, buff=0.2)
        self.play(FadeIn(sensor))
        self.wait(1.4)
        self.play(FadeOut(sensor))

        # ------------------------------------------------ la tentacion
        idea = MathTex(r"H(z)=\frac{1}{G(z)}\ ?", color=VERDE).scale(0.8)
        idea.next_to(cadena, DOWN, buff=0.55)
        self.play(FadeIn(idea, scale=1.1))
        self.wait(1.3)
        self.play(idea.animate.scale(0.72).to_edge(LEFT, buff=0.9)
                  .shift(DOWN * 0.15))

        # ------------------------------------------------ los espectros
        ax, lab = ejes([-PI, PI, PI], [0, ESC + 0.4], ancho=6.6, alto=3.0,
                       x_label=r"\Omega")
        ax.shift(DOWN * 1.35 + RIGHT * 1.4)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        c_g = ax.plot(ganancia_sensor, x_range=[-PI, PI, 0.01], color=AMBAR,
                      stroke_width=3.5, use_smoothing=False)
        l_g = MathTex(r"|G|", color=AMBAR).scale(0.6)
        l_g.next_to(ax.c2p(0, ganancia_sensor(0)), UR, buff=0.08)
        self.play(Create(c_g), FadeIn(l_g))
        n_g = nota("el sensor deja pasar poco en alta frecuencia", scale=0.42)
        n_g.next_to(ax, DOWN, buff=0.25)
        self.play(FadeIn(n_g))
        self.wait(1.5)
        self.play(FadeOut(n_g))

        c_inv = ax.plot(inverso, x_range=[-PI, PI, 0.005], color=ROJO,
                        stroke_width=4, use_smoothing=False)
        l_inv = MathTex(r"|1/G|", color=ROJO).scale(0.6)
        l_inv.next_to(ax.c2p(PI, inverso(PI)), UL, buff=0.06)
        self.play(Create(c_inv, run_time=1.6), FadeIn(l_inv))
        self.wait(0.5)

        alerta = Text("el inverso amplifica justo donde solo queda ruido",
                      color=ROJO).scale(0.52)
        alerta.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(alerta))
        self.play(Flash(ax.c2p(PI * 0.93, ESC * 0.85), color=ROJO,
                        line_length=0.3, num_lines=16))
        self.wait(1.8)
        self.play(FadeOut(alerta))

        # ------------------------------------------------ Wiener
        c_w = ax.plot(wiener, x_range=[-PI, PI, 0.005], color=AZUL,
                      stroke_width=4.5, use_smoothing=False)
        l_w = MathTex(r"|H_{\text{Wiener}}|", color=AZUL).scale(0.6)
        l_w.next_to(ax.c2p(-PI * 0.72, wiener(-PI * 0.72)), UL, buff=0.06)
        self.play(Create(c_w, run_time=1.6), FadeIn(l_w))
        self.wait(0.6)

        bien = Text("Wiener invierte donde puede y se frena donde no",
                    color=AZUL).scale(0.52)
        bien.to_edge(DOWN, buff=0.42)
        self.play(FadeIn(bien))
        self.wait(2.0)
        self.play(FadeOut(bien))

        # ------------------------------------------------ la lectura
        lectura = MathTex(r"H = \underbrace{\frac{1}{G}}_{\text{invertir}}\cdot"
                          r"\underbrace{\frac{D_{rr}}{D_{rr}+D_{vv}}}"
                          r"_{\text{limpiar el ruido}}", color=TXT).scale(0.68)
        lectura.next_to(idea, DOWN, buff=0.75).to_edge(LEFT, buff=0.65)
        self.play(Write(lectura))
        self.wait(0.8)
        n_l = nota("primero limpia,\ndespués invierte", scale=0.44)
        n_l.next_to(lectura, DOWN, buff=0.28)
        self.play(FadeIn(n_l))
        self.wait(2.2)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(cadena, fs, v, fv, r_lbl, x_lbl, idea,
                                 ax, lab, c_g, l_g, c_inv, l_inv, c_w, l_w,
                                 lectura, n_l)))
        cierre = VGroup(
            Text("Con poco ruido, Wiener tiende al filtro inverso.",
                 color=INK).scale(0.58),
            Text("Con mucho ruido, se abstiene.", color=AZUL).scale(0.62),
            nota("el que decide cuánto invertir en cada banda es el SNR",
                 scale=0.5),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
