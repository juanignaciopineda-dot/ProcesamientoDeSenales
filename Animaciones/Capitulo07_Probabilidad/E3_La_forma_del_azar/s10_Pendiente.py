"""Escena 10 — De la acumulada a la densidad: la densidad es la pendiente de la acumulada."""
from comun.escena import *


class Pendiente(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.top = Curva(lambda x: float(cdf_normal(x)), x_rango=(-4, 4), y_max=1.0, ancho=8.0, alto=2.7,
                         x_label="x", y_label="F_X(x)").move_to([-0.8, 1.1, 0])
        self.bot = Curva(lambda x: float(gaussiana(x)), x_rango=(-4, 4), y_max=0.5, ancho=8.0, alto=2.1,
                         color=AMBAR, x_label="x", y_label="f_X(x)").move_to([-0.8, -2.2, 0])
        self.x0 = ValueTracker(-3.0)
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def tangente(self):
        top, x0 = self.top, self.x0

        def f():
            x = x0.get_value()
            y = float(cdf_normal(x))
            m = float(gaussiana(x))
            return Line(top.ejes.c2p(x - 1.0, y - m), top.ejes.c2p(x + 1.0, y + m), color=VERDE, stroke_width=5)
        return always_redraw(f)

    def bloque1(self):
        top = self.top
        with self.narrar("b1"):
            self.en("acumulada")                              # «la acumulada de una variable continua»
            self.play(Create(top.ejes), Create(top.grafica), run_time=self.dur(1.5))
            self.en("deprisa")                                # «sube deprisa»
            self.seg = top.ejes.plot(lambda x: float(cdf_normal(x)), x_range=[-1, 1, 0.02], color=AMBAR,
                                     stroke_width=9)
            self.play(Create(self.seg), run_time=self.dur(0.6))
            self.en("quieta")                                 # «apenas se mueve»
            self.cola = VGroup(*[top.ejes.plot(lambda x: float(cdf_normal(x)), x_range=r, color=CIAN,
                                               stroke_width=9) for r in ([-4, -2.5, 0.02], [2.5, 4, 0.02])])
            self.play(Create(self.cola), run_time=self.dur(0.7))
            self.en("mucha")                                  # «mucha probabilidad en poco espacio»
            br = Brace(Line(top.ejes.c2p(-1, 0), top.ejes.c2p(1, 0)), DOWN, color=AMBAR, buff=0.12)
            alto = DoubleArrow(top.ejes.c2p(-1.4, float(cdf_normal(-1))), top.ejes.c2p(-1.4, float(cdf_normal(1))),
                               color=AMBAR, buff=0, stroke_width=4, tip_length=0.15)
            self.play(Create(br), Create(alto), run_time=self.dur(0.8))
            self.en("mas_salen")                              # «los valores que más salen»
            t = Text("Los que más salen", color=AMBAR, weight=BOLD).scale(0.5).move_to([5.3, 1.1, 0])
            self.play(FadeIn(t, shift=LEFT * 0.2), FadeOut(br), FadeOut(alto), run_time=self.dur(0.6))
            self.en("rapido")                                 # «Lo rápido que sube una curva»
            self.x0.set_value(-2.0)
            self.tg = self.tangente()
            self.play(FadeOut(self.seg), FadeOut(self.cola), FadeIn(self.tg), FadeOut(t), run_time=self.dur(0.6))
            self.en("pendiente")                              # «su pendiente»
            self.play(self.x0.animate.set_value(2.0), run_time=self.dur(2.0), rate_func=linear)
            self.en("derivada")                               # «derivada»
            pal = Text("Derivada = pendiente", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.6, 3.45, 0])
            self.pop(pal)
            self.pal = pal

    def bloque2(self):
        top, bot = self.top, self.bot
        with self.narrar("b2"):
            self.en("en_cada")                                # «la pendiente de la acumulada en cada punto»
            self.x0.set_value(-4.0)
            self.play(FadeOut(self.pal), FadeIn(bot.ejes), run_time=0.4)
            punto = always_redraw(lambda: Dot(bot.ejes.c2p(self.x0.get_value(), float(gaussiana(self.x0.get_value()))),
                                              radius=0.1, color=AMBAR))
            self.add(punto)
            self.play(self.x0.animate.set_value(4.0), Create(bot.grafica, rate_func=linear),
                      run_time=self.dur(2.4), rate_func=linear)
            self.en("nueva")                                  # «una curva nueva»
            punto.clear_updaters()
            self.tg.clear_updaters()
            self.play(FadeOut(punto), FadeOut(self.tg), bot.grafica.animate.set_stroke(width=7), run_time=self.dur(0.5))
            self.en("densidad")                               # «función de densidad de probabilidad»
            pal = Text("Densidad de probabilidad", color=AMBAR, weight=BOLD).scale(0.5).move_to([4.7, -0.6, 0])
            self.pop(pal)
            self.en("f_minus")                                # «efe minúscula sub equis de equis»
            ff = formula("f_X(x)", escala=1.3, colores={0: AMBAR}).move_to([5.3, -2.0, 0])
            self.play(Write(ff), run_time=self.dur(0.7))
            self.en("alta")                                   # «Es alta»
            pico = Circle(radius=0.35, color=VERDE, stroke_width=4).move_to(bot.ejes.c2p(0, float(gaussiana(0))))
            self.play(Create(pico), run_time=self.dur(0.5))
            self.en("despacio")                               # «sube despacio»
            col = VGroup(*[Circle(radius=0.3, color=CIAN, stroke_width=4).move_to(bot.ejes.c2p(x, float(gaussiana(x))))
                           for x in (-2.7, 2.7)])
            self.play(Create(col), FadeOut(pico), run_time=self.dur(0.6))
            self.en("vistazo")                                # «de un vistazo»
            o = ojo().scale(0.8).move_to([5.3, 0.3, 0])
            self.play(FadeOut(col), FadeIn(o, scale=0.7), run_time=self.dur(0.5))
            self.en("concentran")                             # «dónde se concentran los valores»
            banda = Rectangle(width=top.ejes.c2p(1, 0)[0] - top.ejes.c2p(-1, 0)[0], height=6.0,
                              stroke_width=0, stroke_opacity=0, fill_color=AMBAR, fill_opacity=0.15)
            banda.move_to([top.ejes.c2p(0, 0)[0], -0.5, 0])
            self.play(FadeIn(banda), run_time=self.dur(0.7))
