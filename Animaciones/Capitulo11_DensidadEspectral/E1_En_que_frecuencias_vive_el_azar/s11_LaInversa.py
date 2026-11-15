"""Escena 11 — La inversa: el área bajo la densidad dividida entre 2π es la potencia."""
from comun.escena import *


class LaInversa(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        f = MathTex("R_{xx}(\\tau)", "=", "\\frac{1}{2\\pi}", "\\int", "S_{xx}(j\\omega)", "e^{j\\omega\\tau}",
                    "\\,d\\omega", color=TXT).scale(1.0).move_to([0, 2.5, 0])
        f[0].set_color(AZUL)
        f[4].set_color(AMBAR)
        f2 = MathTex("R_{xx}(0)", "=", "\\frac{1}{2\\pi}", "\\int", "S_{xx}(j\\omega)", "e^{0}",
                     "\\,d\\omega", color=TXT).scale(1.0).move_to([0, 0.7, 0])
        f2[0].set_color(AZUL)
        f2[4].set_color(AMBAR)
        f3 = MathTex("R_{xx}(0)", "=", "\\frac{1}{2\\pi}", "\\int", "S_{xx}(j\\omega)", "\\,d\\omega",
                     color=TXT).scale(1.0).move_to([0, -1.2, 0])
        f3[0].set_color(AZUL)
        f3[4].set_color(AMBAR)
        with self.narrar("b1"):
            # «tiene inversa»
            self.en("inversa")
            self.play(FadeIn(f[0:2]), run_time=self.dur(0.6))

            # «uno sobre dos pi»
            self.en("dospi")
            self.play(FadeIn(f[2]), run_time=self.dur(0.5))

            # «la integral de la densidad»
            self.en("integral")
            self.play(FadeIn(f[3:5]), run_time=self.dur(0.6))

            # «e elevado a jota omega tau»
            self.en("exp")
            self.play(FadeIn(f[5:]), run_time=self.dur(0.8))

            # «Pongamos tau igual a cero»
            self.en("tau0")
            self.play(TransformFromCopy(f, f2), run_time=self.dur(1.0))

            # «La exponencial de cero»
            self.en("expcero")
            r1 = SurroundingRectangle(f2[5], color=AMBAR, buff=0.08, stroke_width=3)
            r1.permitir_encima = True
            self.play(Create(r1), run_time=0.4)

            # «vale uno, y desaparece»
            self.en("desap")
            self.play(FadeOut(r1), FadeOut(f2[5]), run_time=self.dur(0.4))
            self.play(ReplacementTransform(f2, f3), run_time=self.dur(0.8))

            # «la potencia, la autocorrelación en cero»
            self.en("pot")
            lp = etiqueta("potencia", AZUL, 0.5).move_to([-3.3, -2.3, 0])
            self.resaltar(f3[0], color=AZUL)
            self.play(FadeIn(lp), run_time=0.3)

            # «el área bajo la densidad espectral»
            self.en("area")
            r2 = SurroundingRectangle(VGroup(f3[3], f3[4], f3[5]), color=AMBAR, buff=0.1, stroke_width=3)
            r2.permitir_encima = True
            la = etiqueta("área bajo la densidad", AMBAR, 0.5).move_to([2.3, -2.3, 0])
            self.play(Create(r2), FadeIn(la), run_time=self.dur(0.6))

            # «dividida entre dos pi»
            self.en("div")
            self.resaltar(f3[2], color=AMBAR)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=7.0, alto=3.0, color=AMBAR, x_label=r"\omega") \
            .move_to([-1.9, -0.9, 0])
        F = MathTex("S_{xx}(j\\omega)", "=", "\\frac{4}{4+\\omega^{2}}", color=TXT).scale(1.1).move_to([0, 3.2, 0])
        F[0].set_color(AMBAR)
        with self.narrar("b2"):
            # «Comprobémoslo con la telegráfica»
            self.en("comprueba")
            self.corte()
            self.play(Create(c.ejes), FadeIn(c.etiquetas), Create(c.grafica), run_time=self.dur(1.2))

            # «Su densidad espectral»
            self.en("su")
            self.play(FadeIn(F[0:2]), run_time=self.dur(0.5))

            # «cuatro dividido entre cuatro más omega al cuadrado»
            self.en("formula")
            self.play(FadeIn(F[2]), run_time=self.dur(1.0))

            # «haremos la cuenta en dos episodios»
            self.en("promesa")
            cd = candado(AMBAR).scale(0.7).move_to([5.2, 1.9, 0])
            ce = etiqueta("la cuenta: episodio 3", INK, 0.5).move_to([5.2, 1.2, 0])
            self.play(FadeIn(cd), FadeIn(ce), run_time=self.dur(0.6))

            # «El área bajo esa curva vale dos pi»
            self.en("area")
            self.play(FadeIn(c.area(-6, 6, AMBAR, 0.35)), run_time=self.dur(0.7))
            ar = MathTex("\\text{area}=2\\pi", color=AMBAR).scale(0.8).move_to([5.2, 0.1, 0])
            self.pop(ar)

            # «Dividida entre dos pi, da uno»
            self.en("uno")
            un = MathTex("\\frac{2\\pi}{2\\pi}", "=", "1", color=TXT).scale(0.9).move_to([5.2, -1.2, 0])
            self.play(FadeIn(un), run_time=self.dur(0.7))

            # «la potencia que contamos a mano»
            self.en("mano")
            self.resaltar(un[2], color=AMBAR)

            # «El área total es la potencia total»
            self.en("total")
            tot = self.palabra("área total = potencia total", AMBAR, 0.75).move_to([0, -3.5, 0])
            self.pop(tot)
