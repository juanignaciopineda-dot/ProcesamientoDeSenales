"""Escena 06 — Correlación de variables continuas: la integral doble."""
from comun.escena import *


class CorrelacionContinua(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        ax, et = ejes((-3, 3, 1), (-3, 3, 1), ancho=6.0, alto=4.6, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-3.6, 0.7, 0])
        c = ax.c2p(0, 0)
        anchos = [(2.9, 1.2, 0.10), (2.1, 0.88, 0.14), (1.3, 0.55, 0.20)]
        elipses = VGroup(*[Ellipse(width=w * 1.6, height=h * 1.6, color=SENAL, fill_color=SENAL, fill_opacity=o,
                                   stroke_width=1.5).rotate(0.6).move_to(c) for w, h, o in anchos])
        barrido = Rectangle(width=5.8, height=4.5, color=AMBAR, fill_opacity=0.12, stroke_width=2).move_to(c)
        with self.narrar("b1"):
            # «variables continuas»
            self.en("continuas")
            self.play(Create(g), run_time=self.dur(0.5))
            self.play(FadeIn(elipses, scale=0.6), run_time=self.dur(0.8))

            # «se multiplica equis por i griega»
            self.en("xy")
            f = formula("r_{XY}", "=", r"\iint", "x\\,y", "f_{XY}(x,y)", r"\,dx\,dy", escala=1.3,
                        colores={0: AMBAR, 3: SENAL, 4: MEDIDA}).move_to([0.2, -3.2, 0])
            oculta(f)
            self.add(f)
            self.play(*revelar(f[0], f[1], f[3]), run_time=self.dur(0.8))

            # «se pesa con la densidad conjunta»
            self.en("peso")
            self.play(*revelar(f[4]), run_time=self.dur(0.7))

            # «se suma sobre todo el plano»
            self.en("plano")
            self.play(FadeIn(barrido), run_time=self.dur(0.4))
            self.play(barrido.animate.set_fill(AMBAR, 0.3), run_time=self.dur(0.5))

            # «con una integral doble»
            self.en("integral")
            self.play(*revelar(f[2], f[5]), run_time=self.dur(0.8))

            # «esa diferencia»
            self.en("dif2")
            d = formula("E[XY]", "-", "E[X]\\,E[Y]", escala=1.3, colores={0: AMBAR, 2: INK}).move_to([3.9, 1.9, 0])
            self.play(FadeIn(d, shift=UP * 0.2), run_time=self.dur(0.6))

            # «la correlación»
            self.en("la_corr")
            self.resaltar(d[0], color=AMBAR, escala=1.1)

            # «el producto de las medias»
            self.en("las_medias")
            self.resaltar(d[2], color=TXT, escala=1.1)

            # «nombre propio»
            self.en("nombre")
            q = Text("¿Cómo se llama?", color=AMBAR).scale(0.9).move_to([3.8, 0.7, 0])
            self.pop(q)
        self.wait(1.0)
        self.limpiar()
