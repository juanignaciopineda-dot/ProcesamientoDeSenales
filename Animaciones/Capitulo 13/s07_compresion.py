"""Escena 7 - Compresion de pulso: el retardo se lee del maximo.

Si la entrada es s[n-D], la salida del adaptado es R_ss[k-D]: su maximo
delata el retardo. Pero solo si el pico es nitido. Un pulso rectangular
tiene un pico ancho: con ruido, el maximo se corre y dos ecos cercanos se
confunden. Barker-13 (o un chirp) tiene autocorrelacion casi nula fuera
del origen: mismo largo, pico nitido.

    manim -pql s07_compresion.py CompresionPulso
"""
from manim import *
import numpy as np
from comun import *


class CompresionPulso(Scene):
    def construct(self):
        configurar()

        tit = titulo("Compresión de pulso: leer el retardo del máximo")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        formula = MathTex(r"g[k]=R_{ss}[k-D]", color=TXT).scale(0.7)
        formula.next_to(tit, DOWN, buff=0.4).set_x(0)
        n_form = nota("si la entrada es $s[n-D]$, la salida del adaptado "
                      "se corre en $D$: su máximo delata el retardo",
                      scale=0.46)
        n_form.next_to(formula, DOWN, buff=0.25)
        self.play(Write(formula), FadeIn(n_form))
        self.wait(1.8)
        self.play(FadeOut(VGroup(formula, n_form)))

        # ------------------------------------------------ el problema del radar
        prob = VGroup(
            Text("En radar no sabemos ni cuándo llega el eco,",
                 color=INK).scale(0.5),
            Text("ni con qué atenuación.", color=INK).scale(0.5),
        ).arrange(DOWN, buff=0.15)
        prob.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(prob))
        self.wait(1.4)
        self.play(FadeOut(prob))

        # ------------------------------------------------ pulso rectangular: pico ancho
        rect_tit = subtitulo("pulso rectangular largo: pico ANCHO", scale=0.52,
                             color=AMBAR)
        rect_tit.next_to(tit, DOWN, buff=0.35).set_x(0)
        self.play(FadeIn(rect_tit))

        L = 13
        rect = np.ones(L)
        lags, Rrect = autocorr(rect)

        ax_r, lab_r = ejes([lags[0], lags[-1], len(lags)], [-1, L + 1, L + 2],
                           ancho=7.6, alto=2.2, x_label="k")
        ax_r.next_to(rect_tit, DOWN, buff=0.35)
        lab_r.next_to(ax_r.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_r), FadeIn(lab_r))
        curva_r = ax_r.plot(
            lambda k: np.interp(k, lags, Rrect), x_range=[lags[0], lags[-1], 0.1],
            color=AMBAR, stroke_width=3.5)
        self.play(Create(curva_r))
        n_ancho = nota("con ruido, el máximo se corre y dos ecos cercanos "
                       "se confunden en uno solo", scale=0.44)
        n_ancho.next_to(ax_r, DOWN, buff=0.25)
        self.play(FadeIn(n_ancho))
        self.wait(1.8)
        self.play(FadeOut(VGroup(rect_tit, ax_r, lab_r, curva_r, n_ancho)))

        # ------------------------------------------------ barker-13
        bark_tit = subtitulo("secuencia Barker-13: mismo largo, pico NÍTIDO",
                             scale=0.52, color=VERDE)
        bark_tit.next_to(tit, DOWN, buff=0.35).set_x(0)
        self.play(FadeIn(bark_tit))

        n13 = np.arange(13)
        ax_b1, _ = ejes([0, 12, 13], [-1.6, 1.6, 3.2], ancho=7.0, alto=1.4, tip=False)
        ax_b1.next_to(bark_tit, DOWN, buff=0.3)
        st_b1 = stem(ax_b1, n13, BARKER13, color=VERDE, ancho=2.6, radio=0.04)
        self.play(Create(ax_b1), Create(st_b1))
        self.wait(0.8)

        lags_b, Rbark = autocorr(BARKER13)
        ax_b2, lab_b2 = ejes([lags_b[0], lags_b[-1], len(lags_b)],
                             [-2, 14, 16], ancho=7.6, alto=2.2,
                             x_label="k")
        ax_b2.next_to(ax_b1, DOWN, buff=0.4)
        lab_b2.next_to(ax_b2.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_b2), FadeIn(lab_b2))
        curva_b = ax_b2.plot(
            lambda k: np.interp(k, lags_b, Rbark), x_range=[lags_b[0], lags_b[-1], 0.1],
            color=VERDE, stroke_width=3.5)
        self.play(Create(curva_b))
        pico_lbl = MathTex(r"13A^2", color=VERDE).scale(0.5)
        pico_lbl.next_to(ax_b2.c2p(0, 13), UP, buff=0.1)
        self.play(FadeIn(pico_lbl))
        n_bark = nota("$13A^2$ en el origen, a lo sumo $A^2$ en cualquier "
                      "otro lag", scale=0.44)
        n_bark.next_to(ax_b2, DOWN, buff=0.25)
        self.play(FadeIn(n_bark))
        self.wait(2.0)
        self.play(FadeOut(VGroup(bark_tit, ax_b1, st_b1, ax_b2, lab_b2, curva_b,
                                 pico_lbl, n_bark)))

        # ------------------------------------------------ dos ecos: se resuelven
        ecos_tit = subtitulo("dos ecos cercanos: rectangular los funde, "
                             "Barker los separa", scale=0.48)
        ecos_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(ecos_tit))

        D1, D2 = -3, 3
        def salida_dos_ecos(lags_, R_, D1, D2):
            k = np.linspace(lags_[0] - 3, lags_[-1] + 3, 400)
            g = (np.interp(k - D1, lags_, R_, left=0, right=0)
                 + 0.85 * np.interp(k - D2, lags_, R_, left=0, right=0))
            return k, g

        kr, gr = salida_dos_ecos(lags, Rrect, D1, D2)
        kb, gb = salida_dos_ecos(lags_b, Rbark, D1, D2)

        ax_e1, lab_e1 = ejes([kr[0], kr[-1], (kr[-1] - kr[0])], [-2, 22, 24],
                             ancho=7.6, alto=2.0, x_label="k")
        ax_e1.next_to(ecos_tit, DOWN, buff=0.3)
        lab_e1.next_to(ax_e1.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_e1), FadeIn(lab_e1))
        curva_e1 = ax_e1.plot(lambda k: np.interp(k, kr, gr),
                              x_range=[kr[0], kr[-1], 0.1], color=AMBAR,
                              stroke_width=3.5)
        l_e1 = MathTex(r"\text{rectangular: UN pico}", color=AMBAR).scale(0.46)
        l_e1.next_to(ax_e1, UP, buff=0.05)
        self.play(Create(curva_e1), FadeIn(l_e1))
        self.wait(1.2)

        ax_e2, lab_e2 = ejes([kb[0], kb[-1], (kb[-1] - kb[0])], [-2, 15, 17],
                             ancho=7.6, alto=2.0, x_label="k")
        ax_e2.next_to(ax_e1, DOWN, buff=0.35)
        lab_e2.next_to(ax_e2.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_e2), FadeIn(lab_e2))
        curva_e2 = ax_e2.plot(lambda k: np.interp(k, kb, gb),
                              x_range=[kb[0], kb[-1], 0.1], color=VERDE,
                              stroke_width=3.5)
        l_e2 = MathTex(r"\text{Barker-13: DOS picos}", color=VERDE).scale(0.46)
        l_e2.next_to(ax_e2, UP, buff=0.05)
        self.play(Create(curva_e2), FadeIn(l_e2))
        self.wait(2.0)
        self.play(FadeOut(VGroup(ecos_tit, ax_e1, lab_e1, curva_e1, l_e1,
                                 ax_e2, lab_e2, curva_e2, l_e2)))

        # ------------------------------------------------ chirp
        chirp_tit = subtitulo("otra forma: el chirp (frecuencia barriendo "
                              "linealmente)", scale=0.5)
        chirp_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(chirp_tit))

        L2 = 60
        c = chirp(L2)
        nC = np.arange(L2)
        ax_c, _ = ejes([0, L2 - 1, L2], [-1.4, 1.4, 2.8], ancho=7.6, alto=1.6,
                       tip=False)
        ax_c.next_to(chirp_tit, DOWN, buff=0.3)
        curva_c = linea_datos(ax_c, nC, c, color=MAGENTA, ancho=2.6)
        self.play(Create(ax_c), Create(curva_c))
        n_chirp = nota("distintos tramos tienen frecuencias distintas:\n"
                       "no se parecen entre sí → autocorrelación cae rápido",
                       scale=0.44)
        n_chirp.next_to(ax_c, DOWN, buff=0.3)
        self.play(FadeIn(n_chirp))
        self.wait(2.2)
        self.play(FadeOut(VGroup(chirp_tit, ax_c, curva_c, n_chirp)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("Energía = largo × amplitud, y la amplitud está limitada.",
                 color=INK).scale(0.5),
            Text("Diseñar bien la FORMA compra resolución gratis.",
                 color=VERDE).scale(0.58),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
