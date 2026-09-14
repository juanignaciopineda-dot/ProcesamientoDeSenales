"""Escena 7 - Estimacion lineal: prediccion y filtrado FIR.

El capitulo 8 se aplica tal cual a los procesos. El predictor LMMSE pesa
la medicion con el coeficiente de correlacion entre el presente y el
futuro: si estan muy correlacionados le hace caso, si no se queda con la
media. Y el filtrado FIR de senal + ruido lleva a las ecuaciones normales.

    manim -pql s07_prediccion.py Prediccion
"""
from manim import *
import numpy as np
from comun import *

ALFA = 0.62          # C_xx[m] = C0 * alfa^|m|
N = 46
NS = np.arange(N)
_rng = np.random.default_rng(77)


def proceso():
    x = np.zeros(N)
    for n in range(1, N):
        x[n] = ALFA * x[n - 1] + _rng.normal(0, 1)
    return 1.5 * x / np.std(x)


X = proceso()
N0 = 26              # instante desde el que se predice


class Prediccion(Scene):
    def construct(self):
        configurar()

        tit = titulo("Predicción lineal: el capítulo 8, aplicado a procesos")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        ax, lab = ejes([0, N, N], [-3.2, 3.2], ancho=9.0, alto=3.0, x_label="n")
        ax.shift(DOWN * 0.5)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)

        pasado = stem(ax, NS[:N0 + 1], X[:N0 + 1], color=AZUL, ancho=2.4,
                      radio=0.038)
        futuro = stem(ax, NS[N0 + 1:], X[N0 + 1:], color=INK, ancho=1.6,
                      radio=0.03)
        futuro.set_stroke(opacity=0.35)

        self.play(Create(ax), FadeIn(lab))
        self.play(FadeIn(pasado))
        self.wait(0.4)

        marca = VGroup(
            Dot(ax.c2p(N0, X[N0]), color=AMBAR, radius=0.075),
            MathTex("x[n_0]", color=AMBAR).scale(0.55)
            .next_to(ax.c2p(N0, X[N0]), UP, buff=0.18),
        )
        self.play(FadeIn(marca))
        preg = Text("conozco esto… ¿cuánto vale m pasos más adelante?",
                    color=TXT).scale(0.55)
        preg.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(preg), FadeIn(futuro))
        self.wait(1.6)
        self.play(FadeOut(preg))

        # ------------------------------------------------ el estimador
        forma = MathTex(r"\hat x[n_0+m] = a\,x[n_0] + b", color=TXT).scale(0.68)
        forma.next_to(tit, DOWN, buff=0.35).shift(RIGHT * 0.5)
        self.play(Write(forma))
        self.wait(0.6)
        es_lo_mismo = nota("es exactamente el problema LMMSE del capítulo 8: "
                           "el futuro hace de Y, el presente de X", scale=0.44)
        es_lo_mismo.next_to(forma, DOWN, buff=0.16)
        self.play(FadeIn(es_lo_mismo))
        self.wait(1.8)
        self.play(FadeOut(es_lo_mismo))

        # ------------------------------------------------ la solucion
        sol = MathTex(r"\hat x[n_0+m] \;=\; \mu_x \;+\; "
                      r"\underbrace{\frac{C_{xx}[m]}{C_{xx}[0]}}_{\text{peso}}"
                      r"\,\big(x[n_0]-\mu_x\big)", color=VERDE).scale(0.62)
        # el subllave hace la formula mas alta: la bajo para que no toque el titulo
        sol.next_to(tit, DOWN, buff=0.5).shift(RIGHT * 0.3)
        self.play(FadeOut(forma), FadeIn(sol))
        self.wait(1.0)

        # la prediccion, para m creciente
        m_t = ValueTracker(1.0)

        def _pred():
            m = m_t.get_value()
            peso = ALFA ** m
            val = peso * X[N0]
            n = N0 + m
            return VGroup(
                DashedLine(ax.c2p(n, 0), ax.c2p(n, val), color=VERDE,
                           stroke_width=3, dash_length=0.07),
                Dot(ax.c2p(n, val), color=VERDE, radius=0.075),
            )

        pred = always_redraw(_pred)
        info = always_redraw(lambda: VGroup(
            MathTex("m =", color=INK).scale(0.55),
            Integer(int(m_t.get_value()), color=AMBAR).scale(0.6),
            MathTex(r"\;\;\text{peso} =", color=INK).scale(0.55),
            DecimalNumber(ALFA ** m_t.get_value(), num_decimal_places=2,
                          color=VERDE).scale(0.6),
        ).arrange(RIGHT, buff=0.12).next_to(ax, UP, buff=0.2)
            .to_edge(RIGHT, buff=0.8))

        self.play(FadeIn(pred), FadeIn(info))
        self.wait(0.8)
        cerca = nota("cerca: la medición manda", scale=0.46)
        cerca.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cerca))
        self.wait(1.2)
        self.play(FadeOut(cerca))

        self.play(m_t.animate.set_value(17.0), run_time=3.6,
                  rate_func=rate_functions.ease_in_out_sine)
        linea_mu = DashedLine(ax.c2p(0, 0), ax.c2p(N, 0), color=AMBAR,
                              stroke_width=2, dash_length=0.09)
        mu_lbl = MathTex(r"\mu_x", color=AMBAR).scale(0.55)
        # arriba de la linea, no a la derecha: ahi choca con la etiqueta "n"
        mu_lbl.next_to(ax.c2p(N, 0), UP, buff=0.12).shift(RIGHT * 0.2)
        lejos = nota("lejos: el peso se apaga y la predicción cae a la media",
                     scale=0.46)
        lejos.to_edge(DOWN, buff=0.45)
        self.play(Create(linea_mu), FadeIn(mu_lbl), FadeIn(lejos))
        self.wait(2.0)
        self.play(FadeOut(lejos))

        clave = nota("el peso ES el coeficiente de correlación entre el "
                     "presente y el futuro", scale=0.48)
        clave.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(clave))
        self.wait(2.0)

        # ------------------------------------------------ filtrado FIR
        self.play(FadeOut(VGroup(ax, lab, pasado, futuro, marca, pred, info,
                                 linea_mu, mu_lbl, clave, sol)))

        sub = Text("El otro caso: filtrar señal + ruido", color=TXT).scale(0.62)
        sub.next_to(tit, DOWN, buff=0.5)
        self.play(FadeIn(sub))

        s = MathTex("s[n]", color=VERDE).scale(0.6)
        suma = Circle(radius=0.24, color=INK, stroke_width=2.5)
        mas = MathTex("+", color=INK).scale(0.6).move_to(suma)
        nodo = VGroup(suma, mas)
        d = MathTex("d[n]", color=ROJO).scale(0.6)
        h = bloque("h[n]", color=AZUL, ancho=1.5, alto=0.8, scale=0.55)
        out = MathTex(r"\hat s[n]", color=AMBAR).scale(0.6)

        cadena = VGroup(s, nodo, h, out).arrange(RIGHT, buff=0.95)
        cadena.next_to(sub, DOWN, buff=0.7)
        d.next_to(nodo, UP, buff=0.55)
        fl = VGroup(flecha(s.get_right(), nodo.get_left()),
                    flecha(d.get_bottom(), nodo.get_top()),
                    flecha(nodo.get_right(), h.get_left()),
                    flecha(h.get_right(), out.get_left()))
        r_lbl = MathTex("r[n]", color=INK).scale(0.5)
        r_lbl.next_to(fl[2], UP, buff=0.1)

        self.play(FadeIn(s), FadeIn(nodo), FadeIn(d), *[GrowArrow(a) for a in fl[:2]])
        self.play(GrowArrow(fl[2]), FadeIn(r_lbl), FadeIn(h))
        self.play(GrowArrow(fl[3]), FadeIn(out))
        self.wait(0.8)

        fir = MathTex(r"\hat s[n]=\sum_{k=0}^{L-1}h[k]\,r[n-k]",
                      color=TXT).scale(0.66)
        fir.next_to(cadena, DOWN, buff=0.6)
        self.play(Write(fir))
        self.wait(0.8)

        orto = nota("condición de ortogonalidad: el error tiene que ser "
                    "ortogonal a todos los datos", scale=0.46)
        orto.next_to(fir, DOWN, buff=0.3)
        self.play(FadeIn(orto))
        self.wait(1.4)

        normales = MathTex(r"\sum_{k=0}^{L-1}h[k]\,R_{rr}[m-k]=R_{sr}[m],"
                           r"\qquad m=0,\dots,L-1", color=VERDE).scale(0.66)
        normales.move_to(fir)
        marco = SurroundingRectangle(normales, color=VERDE, buff=0.2,
                                     corner_radius=0.1, stroke_width=2.5)
        etiq = Text("las ecuaciones normales", color=VERDE).scale(0.5)
        etiq.next_to(marco, DOWN, buff=0.25)
        self.play(FadeOut(fir), FadeOut(orto), FadeIn(normales))
        self.play(Create(marco), FadeIn(etiq))
        self.wait(1.2)
        germen = nota("este es el germen del filtro de Wiener, que se "
                      "desarrolla en el capítulo 12", scale=0.46)
        germen.next_to(etiq, DOWN, buff=0.28)
        self.play(FadeIn(germen))
        self.wait(2.2)

        self.play(FadeOut(VGroup(tit, sub, cadena, d, fl, r_lbl, normales,
                                 marco, etiq, germen)))
        self.wait(0.3)
