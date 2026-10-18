"""Escena 13 — Las dos propiedades de la densidad, y que la densidad no es una probabilidad."""
from comun.escena import *


class PropiedadesDeLaDensidad(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        top = Curva(lambda x: float(cdf_normal(x)), x_rango=(-4, 4), y_max=1.0, ancho=8.0, alto=2.5,
                    x_label="x", y_label="F_X(x)").move_to([-1.0, 1.3, 0])
        bot = Curva(lambda x: float(gaussiana(x)), x_rango=(-4, 4), y_max=0.5, ancho=8.0, alto=2.1,
                    color=AMBAR, x_label="x", y_label="f_X(x)").move_to([-1.0, -2.2, 0])
        self.add(top, bot)

        with self.narrar("b1"):
            self.en("traducen")                               # «se traducen solas»
            fl = Arrow([4.5, 0.9, 0], [4.5, -1.3, 0], color=INK, stroke_width=4, buff=0)
            lab = etiqueta("Pendiente", INK, 0.5).next_to(fl, RIGHT, buff=0.15)
            self.play(Create(fl), FadeIn(lab), run_time=self.dur(0.8))
            self.en("nunca_baja")                             # «nunca baja»
            sube = Arrow(top.ejes.c2p(-2.2, 0.08), top.ejes.c2p(2.2, 0.95), color=VERDE, stroke_width=5, buff=0)
            self.play(Create(sube), run_time=self.dur(0.9))
            self.en("no_neg")                                 # «nunca es negativa»
            tans = VGroup(*[Line(top.ejes.c2p(x - 0.7, float(cdf_normal(x)) - 0.7 * float(gaussiana(x))),
                                 top.ejes.c2p(x + 0.7, float(cdf_normal(x)) + 0.7 * float(gaussiana(x))),
                                 color=AMBAR, stroke_width=5) for x in (-2.0, -0.6, 0.0, 1.0, 2.2)])
            self.play(FadeOut(sube), LaggedStart(*[Create(t) for t in tans], lag_ratio=0.15), run_time=self.dur(1.2))
            self.en("encima")                                 # «por encima del eje»
            lin = Line(bot.ejes.c2p(-4, 0), bot.ejes.c2p(4, 0), color=VERDE, stroke_width=5)
            self.play(FadeOut(tans), Create(lin), run_time=self.dur(0.7))
            self.en("cero_uno")                               # «de cero a uno»
            z = formula("0", colores={0: CIAN}).next_to(top.ejes.c2p(-4, 0), DOWN, buff=0.2)
            u = formula("1", colores={0: VERDE}).next_to(top.ejes.c2p(4, 1), UP, buff=0.12)
            self.play(FadeOut(lin), FadeIn(z), FadeIn(u), run_time=self.dur(0.6))
            self.en("total")                                  # «el área total bajo la densidad»
            area = bot.area(-4, 4, AMBAR, 0.4)
            self.play(FadeIn(area), run_time=self.dur(0.8))
            self.en("uno")                                    # «exactamente uno»
            u2 = Text("Área = 1", color=AMBAR, weight=BOLD).scale(0.65).move_to([5.6, -2.3, 0])
            self.pop(u2)
            self.en("ojo")                                    # «Ojo con un detalle»
            tri = Triangle(color=AMBAR, stroke_width=5).scale(0.4).move_to([5.6, 3.0, 0])
            adm = Text("!", color=AMBAR, weight=BOLD).scale(0.6).move_to(tri.get_center() + DOWN * 0.04)
            self.play(FadeOut(fl), FadeOut(lab), FadeOut(z), FadeOut(u), FadeIn(tri), FadeIn(adm), run_time=self.dur(0.5))
            self.en("no_prob")                                # «la densidad no es una probabilidad»
            nop = formula("f_X(x)", r"\neq", "P", escala=1.0, colores={0: AMBAR, 1: ERROR, 2: ERROR}).move_to([5.3, 1.4, 0])
            self.play(Write(nop), run_time=self.dur(0.9))
            self.en("una_prob")                               # «Una probabilidad es»
            pr = Text("Probabilidad =", color=TXT, weight=BOLD).scale(0.5).move_to([5.3, -0.4, 0])
            self.play(FadeIn(pr), run_time=self.dur(0.4))
            self.en("siempre_area")                           # «siempre un área»
            ar = Rectangle(width=0.9, height=0.5, stroke_width=0, stroke_opacity=0, fill_color=AMBAR,
                           fill_opacity=0.5).next_to(pr, DOWN, buff=0.2)
            self.play(FadeIn(ar), area.animate.set_fill(AMBAR, 0.15), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
