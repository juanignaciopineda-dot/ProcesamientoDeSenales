"""Escena 8 - Decisiones de riesgo minimo.

Generalizacion de MAP: no todos los errores cuestan lo mismo. Se asigna
un costo a cada combinacion y se minimiza el costo esperado. MAP resulta
el caso particular en que todos los errores cuestan igual.

    manim -pql s08_riesgo.py RiesgoMinimo
"""
from manim import *
import numpy as np
from comun import *

A0, A1 = 0.0, 2.6
SIGMA = 0.85
R_MIN, R_MAX = -3.2, 6.2
P0 = 0.5


def g(r, mu):
    return np.exp(-(r - mu) ** 2 / (2 * SIGMA ** 2)) / (SIGMA * np.sqrt(2 * np.pi))


def umbral_de(c10, c01):
    """gamma que corresponde a eta = p0*c10 / (p1*c01), con c00=c11=0."""
    eta = (P0 * c10) / ((1 - P0) * c01)
    return (A0 + A1) / 2 + SIGMA ** 2 * np.log(eta) / (A1 - A0)


class RiesgoMinimo(Scene):
    def construct(self):
        configurar()

        tit = titulo("Riesgo mínimo: cuando los errores no cuestan igual")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ la motivacion
        mot = VGroup(
            Text("Hasta acá tratamos los dos errores como equivalentes.",
                 color=INK).scale(0.55),
            Text("Pero casi nunca lo son:", color=TXT).scale(0.58),
        ).arrange(DOWN, buff=0.2)
        mot.next_to(tit, DOWN, buff=0.5)
        self.play(FadeIn(mot))
        self.wait(1.0)

        ejemplos = VGroup(
            VGroup(Text("no detectar un tumor", color=ROJO).scale(0.52),
                   Text("vs", color=INK).scale(0.45),
                   Text("mandar a hacer otro estudio", color=VERDE).scale(0.52),
                   ).arrange(RIGHT, buff=0.3),
            VGroup(Text("no ver un misil", color=ROJO).scale(0.52),
                   Text("vs", color=INK).scale(0.45),
                   Text("una falsa alarma", color=VERDE).scale(0.52),
                   ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.26)
        ejemplos.next_to(mot, DOWN, buff=0.45)
        self.play(FadeIn(ejemplos[0], shift=RIGHT * 0.15))
        self.play(FadeIn(ejemplos[1], shift=RIGHT * 0.15))
        self.wait(2.0)

        # ------------------------------------------------ los costos
        self.play(FadeOut(VGroup(mot, ejemplos)))

        costo = MathTex(r"c_{ij}", color=AMBAR).scale(0.9)
        c_txt = nota("costo de decidir $H_i$ cuando la verdadera es $H_j$",
                     scale=0.5)
        grupo_c = VGroup(costo, c_txt).arrange(DOWN, buff=0.25)
        grupo_c.next_to(tit, DOWN, buff=0.5)
        self.play(FadeIn(costo, scale=1.3), FadeIn(c_txt))
        self.wait(1.2)

        riesgo = MathTex(r"E[\text{costo de `}H_i\text{'}\,|\,R=r]"
                         r"\;=\;\sum_j c_{ij}\,P(H_j\,|\,R=r)", color=TXT).scale(0.66)
        riesgo.next_to(grupo_c, DOWN, buff=0.5)
        r_nota = nota("se elige la decisión de menor costo esperado", scale=0.48)
        r_nota.next_to(riesgo, DOWN, buff=0.2)
        self.play(Write(riesgo))
        self.play(FadeIn(r_nota))
        self.wait(2.0)

        # ------------------------------------------------ MAP como caso particular
        caso = VGroup(
            Text("Si todos los errores cuestan lo mismo", color=INK).scale(0.52),
            MathTex(r"c_{ii}=0,\qquad c_{ij}=1\ (i\neq j)", color=VERDE).scale(0.65),
            Text("el riesgo ES la probabilidad de error, y vuelve la regla MAP.",
                 color=VERDE).scale(0.52),
        ).arrange(DOWN, buff=0.24)
        caso.next_to(r_nota, DOWN, buff=0.5)
        self.play(FadeIn(caso[0]), FadeIn(caso[1]))
        self.wait(0.6)
        self.play(FadeIn(caso[2]))
        self.wait(2.2)

        # ------------------------------------------------ el umbral generalizado
        self.play(FadeOut(VGroup(grupo_c, riesgo, r_nota, caso)))

        eta_gen = MathTex(r"\eta \;=\; \frac{P(H_0)\,(c_{10}-c_{00})}"
                          r"{P(H_1)\,(c_{01}-c_{11})}", color=AMBAR).scale(0.85)
        eta_gen.next_to(tit, DOWN, buff=0.45)
        e_nota = nota("el mismo test de razón de verosimilitud, con el umbral "
                      "corrido por los costos", scale=0.48)
        e_nota.next_to(eta_gen, DOWN, buff=0.22)
        self.play(Write(eta_gen), FadeIn(e_nota))
        self.wait(1.6)
        self.play(VGroup(eta_gen, e_nota).animate.scale(0.7)
                  .to_edge(UP, buff=1.15))

        # ------------------------------------------------ el dibujo
        ax, lab = ejes([R_MIN, R_MAX, R_MAX - R_MIN], [0, 0.52], ancho=8.2,
                       alto=2.7, x_label="r")
        ax.shift(DOWN * 0.75)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax), FadeIn(lab))

        f0 = ax.plot(lambda r: g(r, A0), x_range=[R_MIN, R_MAX, 0.02],
                     color=AZUL, stroke_width=4)
        f1 = ax.plot(lambda r: g(r, A1), x_range=[R_MIN, R_MAX, 0.02],
                     color=VERDE, stroke_width=4)
        self.play(Create(f0), Create(f1))

        c_miss = ValueTracker(1.0)      # c01: decir H0 siendo H1 (miss)
        umbral = always_redraw(lambda: DashedLine(
            ax.c2p(umbral_de(1.0, c_miss.get_value()), 0),
            ax.c2p(umbral_de(1.0, c_miss.get_value()), 0.50),
            color=ROJO, stroke_width=3.5, dash_length=0.1))
        area_m = always_redraw(lambda: ax.get_area(
            f1, x_range=(R_MIN, umbral_de(1.0, c_miss.get_value())),
            color=AMBAR, opacity=0.6, stroke_width=0))
        area_fa = always_redraw(lambda: ax.get_area(
            f0, x_range=(umbral_de(1.0, c_miss.get_value()), R_MAX),
            color=ROJO, opacity=0.6, stroke_width=0))
        self.play(Create(umbral), FadeIn(area_m), FadeIn(area_fa))

        valor = always_redraw(lambda: VGroup(
            MathTex(r"c_{01}/c_{10} =", color=AMBAR).scale(0.6),
            DecimalNumber(c_miss.get_value(), num_decimal_places=1,
                          color=AMBAR).scale(0.6),
        ).arrange(RIGHT, buff=0.12).to_edge(DOWN, buff=0.9))
        self.play(FadeIn(valor))
        self.wait(0.8)

        m1 = nota("si un miss cuesta 10 veces más que una falsa alarma…",
                  scale=0.48)
        m1.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m1))
        self.play(c_miss.animate.set_value(10.0), run_time=2.8,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.6)
        m2 = nota("…el umbral baja: el detector se vuelve desconfiado y "
                  "prefiere sobrediagnosticar", scale=0.48)
        m2.move_to(m1)
        self.play(FadeOut(m1), FadeIn(m2))
        self.wait(2.0)

        m3 = nota("y al revés, si lo caro es la falsa alarma", scale=0.48)
        m3.move_to(m1)
        self.play(FadeOut(m2), FadeIn(m3))
        self.play(c_miss.animate.set_value(0.12), run_time=2.8,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(1.6)
        self.play(FadeOut(m3))
        self.play(c_miss.animate.set_value(1.0), run_time=1.5)

        # ------------------------------------------------ cierre
        self.play(FadeOut(VGroup(ax, lab, f0, f1, umbral, area_m, area_fa,
                                 valor, eta_gen, e_nota)))
        cierre = VGroup(
            Text("Todo el capítulo es un solo test:", color=INK).scale(0.55),
            MathTex(r"\Lambda(r)\;\underset{H_0}{\overset{H_1}{\gtrless}}\;\eta",
                    color=AMBAR).scale(0.95),
            VGroup(
                Text("MAP", color=AZUL).scale(0.52),
                Text("·", color=INK).scale(0.52),
                Text("Neyman–Pearson", color=VERDE).scale(0.52),
                Text("·", color=INK).scale(0.52),
                Text("riesgo mínimo", color=MAGENTA).scale(0.52),
            ).arrange(RIGHT, buff=0.28),
            nota("los tres eligen η distinto, y nada más", scale=0.5),
        ).arrange(DOWN, buff=0.32)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(Write(cierre[1]))
        self.wait(0.4)
        self.play(FadeIn(cierre[2], shift=UP * 0.12))
        self.play(FadeIn(cierre[3]))
        self.wait(2.6)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
