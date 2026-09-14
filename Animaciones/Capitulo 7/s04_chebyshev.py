"""Escena 4 - La desigualdad de Chebyshev.

Vale para CUALQUIER variable aleatoria con varianza finita, sin saber
nada de su forma. El precio de esa generalidad es que la cota es floja:
se compara contra la masa real de tres distribuciones distintas.

    manim -pql s04_chebyshev.py Chebyshev
"""
from manim import *
import numpy as np
from comun import *

X0, X1 = -5.0, 5.0
_rng = np.random.default_rng(7)


def dens_normal(x):
    return gauss(x, 0.0, 1.0)


def dens_uniforme(x):
    h = np.sqrt(3.0)                      # varianza 1  ->  semiancho sqrt(3)
    return 1 / (2 * h) if abs(x) <= h else 0.0


def dens_laplace(x):
    b = 1 / np.sqrt(2.0)                  # varianza 1
    return np.exp(-abs(x) / b) / (2 * b)


def cola_normal(a):
    """P(|X| >= a) para la normal estandar, por integracion numerica."""
    xs = np.linspace(a, 12, 4000)
    return 2 * np.trapezoid(dens_normal(xs), xs)


def cola_uniforme(a):
    h = np.sqrt(3.0)
    return 0.0 if a >= h else (h - a) / h


def cola_laplace(a):
    b = 1 / np.sqrt(2.0)
    return np.exp(-a / b)


CASOS = [("normal", dens_normal, cola_normal, AZUL),
         ("uniforme", dens_uniforme, cola_uniforme, VERDE),
         ("Laplace", dens_laplace, cola_laplace, MAGENTA)]


class Chebyshev(Scene):
    def construct(self):
        configurar()

        tit = titulo("Chebyshev: una cota que vale para cualquier distribución")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        enun = MathTex(r"P\!\left(\frac{|X-\mu_X|}{\sigma_X}\geq\alpha\right)"
                       r"\;\leq\;\frac{1}{\alpha^2}", color=TXT).scale(0.85)
        enun.next_to(tit, DOWN, buff=0.4)
        self.play(Write(enun))
        self.wait(0.8)
        clave = nota("no hace falta saber nada de la forma de la densidad: "
                     "solo que tenga varianza finita", scale=0.47)
        clave.next_to(enun, DOWN, buff=0.22)
        self.play(FadeIn(clave))
        self.wait(2.0)
        self.play(FadeOut(clave), enun.animate.scale(0.68).to_edge(UP, buff=1.1))

        # ------------------------------------------------ el grafico
        ax, lab = ejes([X0, X1, X1], [0, 0.55], ancho=8.4, alto=2.7,
                       x_label="x")
        ax.shift(DOWN * 0.85)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        alfa = ValueTracker(1.5)
        idx = [0]                                     # caso activo

        def dens_actual(x):
            return CASOS[idx[0]][1](x)

        curva_d = always_redraw(lambda: ax.plot(
            dens_actual, x_range=[X0, X1, 0.01], color=CASOS[idx[0]][3],
            stroke_width=4, use_smoothing=False))
        centro = always_redraw(lambda: ax.get_area(
            ax.plot(dens_actual, x_range=[X0, X1, 0.01], use_smoothing=False),
            x_range=(-alfa.get_value(), alfa.get_value()),
            color=CASOS[idx[0]][3], opacity=0.16, stroke_width=0))
        cola_izq = always_redraw(lambda: ax.get_area(
            ax.plot(dens_actual, x_range=[X0, X1, 0.01], use_smoothing=False),
            x_range=(X0, -alfa.get_value()), color=ROJO, opacity=0.8,
            stroke_width=0))
        cola_der = always_redraw(lambda: ax.get_area(
            ax.plot(dens_actual, x_range=[X0, X1, 0.01], use_smoothing=False),
            x_range=(alfa.get_value(), X1), color=ROJO, opacity=0.8,
            stroke_width=0))
        lim = always_redraw(lambda: VGroup(*[
            DashedLine(ax.c2p(s * alfa.get_value(), 0),
                       ax.c2p(s * alfa.get_value(), 0.5), color=AMBAR,
                       stroke_width=2, dash_length=0.08) for s in (-1, 1)]))
        lim_lbl = always_redraw(lambda: VGroup(
            MathTex(r"-\alpha\sigma", color=AMBAR).scale(0.5)
            .next_to(ax.c2p(-alfa.get_value(), 0), DOWN, buff=0.16),
            MathTex(r"+\alpha\sigma", color=AMBAR).scale(0.5)
            .next_to(ax.c2p(alfa.get_value(), 0), DOWN, buff=0.16)))

        self.play(Create(curva_d), FadeIn(centro))
        self.play(Create(lim), FadeIn(lim_lbl))
        self.play(FadeIn(cola_izq), FadeIn(cola_der))
        colas_lbl = Text("esto es lo que acota Chebyshev", color=ROJO).scale(0.5)
        colas_lbl.next_to(ax, DOWN, buff=0.45)
        self.play(FadeIn(colas_lbl))
        self.wait(1.4)
        self.play(FadeOut(colas_lbl))

        # ------------------------------------------------ marcador cota vs real
        def marcador():
            a = alfa.get_value()
            cota = 1 / a ** 2
            real = CASOS[idx[0]][2](a)
            fila = VGroup(
                VGroup(MathTex(r"\alpha =", color=INK).scale(0.6),
                       DecimalNumber(a, num_decimal_places=2, color=AMBAR)
                       .scale(0.6)).arrange(RIGHT, buff=0.12),
                VGroup(Text("cota  1/α² =", color=INK).scale(0.5),
                       DecimalNumber(cota, num_decimal_places=3, color=AMBAR)
                       .scale(0.6)).arrange(RIGHT, buff=0.14),
                VGroup(Text("masa real =", color=INK).scale(0.5),
                       DecimalNumber(real, num_decimal_places=3, color=ROJO)
                       .scale(0.6)).arrange(RIGHT, buff=0.14),
            ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            return fila.to_corner(UR, buff=0.7).shift(DOWN * 0.35)

        panel = always_redraw(marcador)
        nombre = always_redraw(lambda: Text(CASOS[idx[0]][0],
                                            color=CASOS[idx[0]][3],
                                            weight=BOLD).scale(0.6)
                               .to_corner(UL, buff=0.7).shift(DOWN * 0.95))
        self.play(FadeIn(panel), FadeIn(nombre))
        self.wait(0.8)

        # ------------------------------------------------ barrer alfa
        self.play(alfa.animate.set_value(3.0), run_time=2.6,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.6)
        self.play(alfa.animate.set_value(1.15), run_time=2.2)
        self.wait(0.8)
        self.play(alfa.animate.set_value(2.0), run_time=1.4)
        self.wait(0.6)

        # ------------------------------------------------ cambiar de distribucion
        cambio = nota("la MISMA cota, con distribuciones muy distintas",
                      scale=0.47)
        cambio.next_to(ax, DOWN, buff=0.45)
        self.play(FadeIn(cambio))
        for nuevo in (1, 2, 0):
            idx[0] = nuevo
            self.wait(1.5)
        self.wait(0.4)
        self.play(FadeOut(cambio))

        floja = Text("la cota siempre se cumple, pero es holgada",
                     color=AMBAR).scale(0.54)
        floja.next_to(ax, DOWN, buff=0.45)
        self.play(FadeIn(floja))
        self.wait(2.0)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, curva_d, centro, cola_izq, cola_der,
                                 lim, lim_lbl, panel, nombre, floja, enun)))
        cierre = VGroup(
            Text("Ese es el trato:", color=INK).scale(0.55),
            Text("no necesitás conocer la distribución…", color=TXT).scale(0.6),
            Text("…pero a cambio la cota es floja.", color=AMBAR).scale(0.6),
            nota("Cuando sí conocés la densidad, siempre podés hacerlo mejor.",
                 scale=0.48),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.play(FadeIn(cierre[2], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[3]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
