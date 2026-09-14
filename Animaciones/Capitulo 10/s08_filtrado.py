"""Escena 8 - Filtrado LTI de procesos WSS: el resultado central del capitulo.

Si entra un proceso WSS a un sistema LTI, sale otro proceso WSS, y los tres
resultados clave son deterministicos:

    mu_y = H(j0) mu_x
    R_yy(tau) = R_hh(tau) * R_xx(tau)
    S_yy(jw) = |H(jw)|^2 S_xx(jw)

La ultima es identica a como se transforma la densidad espectral de energia
de una senal deterministica: por eso a S_xx se la llama PSD (cap 11).

    manim -pql s08_filtrado.py Filtrado
"""
from manim import *
import numpy as np
from comun import *

T = np.linspace(0, 10, 900)
W_MAX = 8.0
A_H = 2.0            # |H(jw)|^2 = A_H^2 / (A_H^2 + w^2), pasabajos
A_X = 1.1            # S_xx(jw) = 2 A_X / (A_X^2 + w^2), entrada de banda ancha


def entrada(t):
    # senoides sobre una grilla de frecuencias UNIFORME (no al azar: las
    # frecuencias al azar se agrupan y baten), con fase aleatoria. Asi la
    # realizacion se ve estadisticamente pareja a lo largo de todo el tramo.
    rng = np.random.default_rng(7)
    y = np.zeros_like(t)
    ciclos = np.arange(2, 46)          # 2..45 ciclos completos en la ventana
    for c in ciclos:
        y += np.sin(2 * np.pi * c * t / t[-1] + rng.uniform(0, 2 * np.pi))
    return 1.05 * y / np.std(y)


def suaviza(y, k=60):
    """Pasabajos de media movil, solo para el dibujo de y(t)."""
    nucleo = np.ones(k) / k
    z = np.convolve(y, nucleo, mode="same")
    # el modo 'same' distorsiona los bordes: los recorto al valor interno
    z[:k] = z[k]
    z[-k:] = z[-k - 1]
    return z


X = entrada(T)
# la salida del pasabajos, a proposito con menos amplitud: se ve mas calma
Y = 0.92 * suaviza(X) / np.std(suaviza(X))


def S_xx(w):
    return 2 * A_X / (A_X ** 2 + w ** 2)


def H2(w):
    return A_H ** 2 / (A_H ** 2 + w ** 2)


def S_yy(w):
    return S_xx(w) * H2(w)


class Filtrado(Scene):
    def construct(self):
        configurar()

        tit = titulo("Filtrado LTI de procesos WSS: el resultado del capítulo")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ============================================ 1. el planteo, en el tiempo
        ax, lab = ejes([0, 10, 10], [-2.6, 2.6], ancho=9.2, alto=2.5,
                       x_label="t")
        ax.shift(UP * 1.35)
        lab.next_to(ax.x_axis.get_end(), DR, buff=0.1)

        onda_x = linea_datos(ax, T, X, color=AZUL, ancho=1.9)
        x_lbl = MathTex("x(t)", color=AZUL).scale(0.6)
        x_lbl.next_to(ax, LEFT, buff=0.1).shift(UP * 0.35)

        self.play(Create(ax), FadeIn(lab))
        self.play(Create(onda_x, run_time=1.6), FadeIn(x_lbl))

        entra = Text("proceso WSS: media constante, autocorrelación que "
                     "solo depende de τ", color=INK, slant=ITALIC).scale(0.44)
        entra.next_to(ax, DOWN, buff=0.3)
        self.play(FadeIn(entra))
        self.wait(1.2)
        self.play(FadeOut(entra))

        # el bloque LTI
        h = bloque("h(t)", color=AMBAR, ancho=1.7, alto=0.9, scale=0.6)
        h.next_to(ax, DOWN, buff=0.45)
        fl_in = flecha(h.get_left() + LEFT * 1.6, h.get_left(), color=AZUL)
        fl_out = flecha(h.get_right(), h.get_right() + RIGHT * 1.6, color=VERDE)
        sis_lbl = Text("sistema LTI", color=AMBAR, slant=ITALIC).scale(0.42)
        sis_lbl.next_to(h, UP, buff=0.12)
        self.play(GrowArrow(fl_in), FadeIn(h), FadeIn(sis_lbl),
                  GrowArrow(fl_out))
        self.wait(0.4)

        onda_y = linea_datos(ax, T, Y, color=VERDE, ancho=3.4)
        y_lbl = MathTex("y(t)", color=VERDE).scale(0.6)
        y_lbl.next_to(ax, LEFT, buff=0.1).shift(DOWN * 0.4)
        self.play(onda_x.animate.set_stroke(opacity=0.35))
        self.play(Create(onda_y, run_time=1.6), FadeIn(y_lbl))

        clave1 = Text("la salida también es WSS  —  y x(t), y(t) son "
                      "conjuntamente WSS", color=TXT).scale(0.5)
        clave1.next_to(h, DOWN, buff=0.4)
        self.play(FadeIn(clave1))
        self.wait(1.8)

        # ============================================ 2. los tres resultados
        self.play(FadeOut(VGroup(ax, lab, onda_x, onda_y, x_lbl, y_lbl,
                                 fl_in, fl_out, h, sis_lbl, clave1)))

        r1 = MathTex(r"\mu_y = H(j0)\,\mu_x", color=VERDE).scale(0.8)
        n1 = nota("la media atraviesa el sistema como una señal constante: "
                  "la escala la ganancia en continua", scale=0.44)
        r2 = MathTex(r"R_{yy}(\tau) = R_{hh}(\tau) * R_{xx}(\tau)",
                     color=VERDE).scale(0.8)
        n2 = nota("R_hh es la autocorrelación determinística de h — la de "
                  "señales del capítulo 1, sin nada de azar", scale=0.44)
        bloque1 = VGroup(r1, n1).arrange(DOWN, buff=0.18)
        bloque2 = VGroup(r2, n2).arrange(DOWN, buff=0.18)
        cuerpo = VGroup(bloque1, bloque2).arrange(DOWN, buff=0.55)
        cuerpo.move_to(ORIGIN).shift(UP * 0.2)

        self.play(FadeIn(bloque1, shift=UP * 0.1))
        self.wait(1.6)
        self.play(FadeIn(bloque2, shift=UP * 0.1))
        self.wait(1.4)

        det = nota("lo notable: la relación entre las correlaciones es "
                   "una convolución determinística, sin azar", scale=0.46)
        det.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(det))
        self.wait(2.0)
        self.play(FadeOut(VGroup(cuerpo, det)))

        # ============================================ 3. y en frecuencia
        r3 = MathTex(r"S_{yy}(j\omega) = |H(j\omega)|^2\, S_{xx}(j\omega)",
                     color=VERDE).scale(0.9)
        r3.next_to(tit, DOWN, buff=0.5)
        self.play(Write(r3))
        self.wait(0.3)
        conv = nota("las convoluciones se vuelven productos: acá vive la "
                    "comodidad de trabajar en frecuencia", scale=0.44)
        conv.next_to(r3, DOWN, buff=0.2)
        self.play(FadeIn(conv))
        self.wait(1.5)
        self.play(FadeOut(conv), r3.animate.scale(0.7).to_edge(UP, buff=1.15))

        ax_w, lab_w = ejes([-W_MAX, W_MAX, W_MAX], [0, 2.6], ancho=9.4,
                           alto=3.3, x_label=r"\omega")
        ax_w.shift(DOWN * 0.7)
        lab_w.next_to(ax_w.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_w), FadeIn(lab_w))

        c_sxx = ax_w.plot(S_xx, x_range=[-W_MAX, W_MAX, 0.02], color=AZUL,
                          stroke_width=3.5)
        c_h2 = ax_w.plot(lambda w: 2.2 * H2(w), x_range=[-W_MAX, W_MAX, 0.02],
                         color=AMBAR, stroke_width=3.0)
        c_h2.set_stroke(opacity=0.9)
        c_syy = ax_w.plot(S_yy, x_range=[-W_MAX, W_MAX, 0.02], color=VERDE,
                          stroke_width=4.5)
        area_syy = ax_w.get_area(ax_w.plot(S_yy, x_range=[-W_MAX, W_MAX, 0.02]),
                                 x_range=(-W_MAX, W_MAX), color=VERDE,
                                 opacity=0.16, stroke_width=0)

        l_sxx = MathTex(r"S_{xx}(j\omega)", color=AZUL).scale(0.5)
        l_sxx.next_to(ax_w.c2p(-W_MAX, S_xx(-W_MAX)), UR, buff=0.05).shift(
            RIGHT * 0.6 + UP * 0.7)
        l_h2 = MathTex(r"|H(j\omega)|^2", color=AMBAR).scale(0.5)
        l_h2.next_to(ax_w.c2p(3.0, 2.2 * H2(3.0)), UR, buff=0.1)
        l_syy = MathTex(r"S_{yy}(j\omega)", color=VERDE).scale(0.5)
        l_syy.next_to(ax_w.c2p(0, S_yy(0)), UP, buff=0.15).shift(RIGHT * 1.7)

        self.play(Create(c_sxx), FadeIn(l_sxx))
        self.wait(0.5)
        self.play(Create(c_h2), FadeIn(l_h2))
        self.wait(0.5)

        # barrido: el producto punto a punto
        w_t = ValueTracker(-W_MAX + 0.3)
        scrub = always_redraw(lambda: DashedLine(
            ax_w.c2p(w_t.get_value(), 0),
            ax_w.c2p(w_t.get_value(), 2.5), color=INK, stroke_width=2,
            dash_length=0.08))
        d_x = always_redraw(lambda: Dot(
            ax_w.c2p(w_t.get_value(), S_xx(w_t.get_value())), color=AZUL,
            radius=0.06))
        d_h = always_redraw(lambda: Dot(
            ax_w.c2p(w_t.get_value(), 2.2 * H2(w_t.get_value())), color=AMBAR,
            radius=0.06))
        d_y = always_redraw(lambda: Dot(
            ax_w.c2p(w_t.get_value(), S_yy(w_t.get_value())), color=VERDE,
            radius=0.07))
        op = always_redraw(lambda: MathTex(
            r"S_{xx}\;\times\;|H|^2\;=\;S_{yy}", color=INK).scale(0.5)
            .next_to(ax_w, UP, buff=0.1).to_edge(RIGHT, buff=0.7))

        self.add(scrub, d_x, d_h, d_y, op)
        self.play(Create(c_syy), FadeIn(area_syy), FadeIn(l_syy))
        self.play(w_t.animate.set_value(W_MAX - 0.3), run_time=3.6,
                  rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.4)
        self.play(w_t.animate.set_value(0.0), run_time=1.4)
        self.remove(scrub, d_x, d_h, d_y, op)

        forma = nota("el pasabajos recorta las frecuencias altas: la salida "
                     "queda con menos potencia y más lenta", scale=0.44)
        forma.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(forma))
        self.wait(2.0)
        self.play(FadeOut(forma))

        # ============================================ 4. el puente al cap 11
        self.play(FadeOut(VGroup(ax_w, lab_w, c_sxx, c_h2, c_syy, area_syy,
                                 l_sxx, l_h2, l_syy, r3)))

        eco = MathTex(r"S_{yy} = |H|^2\, S_{xx}", color=VERDE).scale(0.85)
        comp = VGroup(
            Text("Es idéntico a cómo se transforma la densidad espectral",
                 color=TXT).scale(0.54),
            Text("de energía de una señal determinística al filtrarla.",
                 color=TXT).scale(0.54),
        ).arrange(DOWN, buff=0.16)
        cierre = VGroup(
            Text("Esa analogía no es casual:", color=INK,
                 slant=ITALIC).scale(0.5),
            Text("por eso a S_xx(jω) se la llama densidad espectral de "
                 "potencia — la PSD.", color=AMBAR).scale(0.5),
            Text("Es el tema del capítulo 11.", color=INK,
                 slant=ITALIC).scale(0.5),
        ).arrange(DOWN, buff=0.16)
        todo = VGroup(eco, comp, cierre).arrange(DOWN, buff=0.5)
        todo.move_to(ORIGIN)

        self.play(FadeIn(eco, shift=UP * 0.1))
        self.wait(0.5)
        self.play(FadeIn(comp))
        self.wait(1.6)
        self.play(FadeIn(cierre))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, todo)))
        self.wait(0.3)
