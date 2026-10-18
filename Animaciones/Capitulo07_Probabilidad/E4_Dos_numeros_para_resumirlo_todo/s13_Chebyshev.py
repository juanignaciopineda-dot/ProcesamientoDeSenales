"""Escena 13 — Chebyshev: Markov aplicado a (X − μ)²."""
from comun.escena import *


class Chebyshev(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.deduccion()
        self.valores()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def deduccion(self):
        cheb = self.palabra("Chebyshev", AMBAR, 1.1).move_to([-4.8, 3.3, 0])
        mark = caja("Markov", AZUL, ancho=2.4, alto=0.8, scale=0.6).move_to([4.6, 3.3, 0])
        flecha_ = flecha([3.6, 3.0, 0], [2.5, 2.6, 0], AMBAR, 3)
        y_def = MathTex("Y", "=", r"(X-\mu)^2", color=TXT).scale(1.4).move_to([0, 2.2, 0])
        y_pos = MathTex(r"Y\ge 0", color=VERDE).scale(1.2).move_to([4.6, 2.2, 0])
        y_media = MathTex("E[Y]", "=", r"\sigma^2", color=TXT).scale(1.4).move_to([0, 0.9, 0])
        y_media[2].set_color(AMBAR)
        dos = MathTex(r"P(Y\ge\alpha^2\sigma^2)", r"\le", r"\frac{\sigma^2}{\alpha^2\sigma^2}", color=TXT
                      ).scale(1.2).move_to([0, -0.6, 0])
        alej = MathTex(r"P(|X-\mu|\ge\alpha\sigma)", color=TXT).scale(1.4).move_to([-1.6, -2.3, 0])
        res = MathTex(r"\le", r"\frac{1}{\alpha^2}", color=AMBAR).scale(1.4).next_to(alej, RIGHT, buff=0.3)
        with self.narrar("b1"):
            # «Chebyshev tuvo una idea»
            self.en("chebyshev")
            self.pop(cheb)
            # «aplicar Markov»
            self.en("aplicar")
            self.play(FadeIn(mark), GrowArrow(flecha_), run_time=self.dur(0.8))
            # «la distancia a la media, elevada al cuadrado»
            self.en("y_def")
            self.play(FadeIn(y_def, shift=DOWN * 0.15), run_time=self.dur(1.5))
            # «nunca es negativa»
            self.en("y_pos")
            self.play(FadeIn(y_pos, shift=LEFT * 0.15), run_time=self.dur(0.7))
            # «su media es, por definición, la varianza»
            self.en("y_media")
            self.play(FadeIn(y_media, shift=DOWN * 0.15), run_time=self.dur(1.2))
            # «la cuenta sale en dos líneas»
            self.en("dos_lineas")
            self.play(FadeIn(dos, shift=DOWN * 0.15), run_time=self.dur(1.5))
            # «alejarse de la media más de alfa desviaciones estándar»
            self.en("alejarse")
            self.play(FadeIn(alej, shift=DOWN * 0.15), run_time=self.dur(1.6))
            # «uno dividido entre alfa al cuadrado»
            self.en("uno_alfa2")
            self.play(FadeIn(res, shift=LEFT * 0.15), run_time=self.dur(1.0))
            self.play(Create(SurroundingRectangle(VGroup(alej, res), color=AMBAR, buff=0.2)), run_time=0.5)

    # ---------------------------------------------------------------- b2
    def valores(self):
        f2 = MathTex(r"\alpha=2", r"\to", r"\le 25\,\%", color=TXT).scale(1.3).move_to([-4.6, 1.8, 0])
        f3 = MathTex(r"\alpha=3", r"\to", r"\le 11\,\%", color=TXT).scale(1.3).move_to([-4.6, 0.4, 0])
        f2[2].set_color(AMBAR)
        f3[2].set_color(AMBAR)
        cx, cy = 3.4, 0.0
        base = Line([cx - 3.6, cy, 0], [cx + 3.6, cy, 0], color=INK, stroke_width=2)
        bell = campana7(cx, cy, 1.0, SENAL, ancho=0.9, alto=2.2)
        colas2 = VGroup(cola7(cx, cy, 1.0, 2.0, 4.0, ERROR, 0.9, 2.2), cola7(cx, cy, 1.0, -4.0, -2.0, ERROR, 0.9, 2.2))
        colas3 = VGroup(cola7(cx, cy, 1.0, 3.0, 4.0, ERROR, 0.9, 2.2), cola7(cx, cy, 1.0, -4.0, -3.0, ERROR, 0.9, 2.2))
        flechas_s = VGroup(flecha([cx, cy - 0.35, 0], [cx + 1.8, cy - 0.35, 0], AMBAR, 3),
                           flecha([cx, cy - 0.35, 0], [cx - 1.8, cy - 0.35, 0], AMBAR, 3))
        dos_s = MathTex(r"2\sigma", color=AMBAR).scale(0.8).move_to([cx + 0.9, cy - 0.75, 0])
        dos_s2 = MathTex(r"2\sigma", color=AMBAR).scale(0.8).move_to([cx - 0.9, cy - 0.75, 0])
        # tres formas con las mismas bandas
        formas = VGroup()
        y0 = -3.3
        for k, c in enumerate((-4.2, 0.0, 4.2)):
            formas.add(Line([c - 1.5, y0, 0], [c + 1.5, y0, 0], color=INK, stroke_width=2))
        forma1 = campana7(-4.2, y0, 0.7, SENAL, ancho=0.5, alto=1.0, x_max=3)
        forma2 = Polygon([-1.1, y0, 0], [-1.1, y0 + 0.7, 0], [1.1, y0 + 0.7, 0], [1.1, y0, 0], color=SENAL,
                         stroke_width=4)
        forma3 = VGroup(campana7(3.5, y0, 0.25, SENAL, ancho=0.5, alto=1.0, x_max=3),
                        campana7(4.9, y0, 0.25, SENAL, ancho=0.5, alto=1.0, x_max=3))
        # (la segunda forma queda centrada en 0; la tercera, bimodal, en 4,2)
        bandas = VGroup(*[DashedLine([c + d, y0 - 0.1, 0], [c + d, y0 + 1.1, 0], color=AMBAR, stroke_width=2)
                          for c in (-4.2, 0.0, 4.2) for d in (-0.9, 0.9)])
        mu_s2 = MathTex(r"\mu", ",", r"\sigma^2", color=AMBAR).scale(1.8).move_to([0, -1.6, 0])
        with self.narrar("b2"):
            # «Con alfa igual a dos»
            self.en("a2")
            self.corte()
            self.play(FadeIn(f2[0:2], shift=DOWN * 0.15), run_time=self.dur(0.6))
            # «el veinticinco por ciento»
            self.en("p25")
            self.play(FadeIn(f2[2], shift=LEFT * 0.15), Create(base), Create(bell), FadeIn(colas2),
                      run_time=self.dur(1.0))
            # «a más de dos sigmas de su media»
            self.en("dos_sigmas")
            self.play(LaggedStart(*[GrowArrow(a) for a in flechas_s], lag_ratio=0.2), FadeIn(dos_s), FadeIn(dos_s2),
                      run_time=self.dur(1.0))
            # «Con alfa igual a tres»
            self.en("a3")
            self.play(FadeIn(f3[0:2], shift=DOWN * 0.15), run_time=self.dur(0.6))
            # «un once por ciento»
            self.en("p11")
            self.play(FadeIn(f3[2], shift=LEFT * 0.15), FadeOut(colas2), FadeIn(colas3), run_time=self.dur(0.9))
            # «cualquier distribución»
            self.en("cualquiera")
            self.play(FadeIn(formas), Create(forma1), Create(forma2), Create(forma3), FadeIn(bandas),
                      run_time=self.dur(1.5))
            # «Solo hacen falta»
            self.en("solo")
            self.play(FadeOut(formas), FadeOut(forma1), FadeOut(forma2), FadeOut(forma3), FadeOut(bandas),
                      run_time=0.4)
            self.pop(mu_s2)
