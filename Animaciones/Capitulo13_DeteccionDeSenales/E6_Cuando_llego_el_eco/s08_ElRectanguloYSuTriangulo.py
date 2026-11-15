"""Escena 08 — El pulso rectangular de trece: su autocorrelación es un triángulo ancho."""
from comun.escena import *


class ElRectanguloYSuTriangulo(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        cx, y0 = -2.6, 2.3
        rect = Rectangle(width=13 * 0.4, height=0.8, color=SENAL, stroke_width=4).set_fill(SENAL, 0.35)
        rect.move_to([cx, y0 + 0.4, 0])
        bars = Tallos([1] * 13, centro=(cx, y0), paso=0.4, unidad=0.8, color=SENAL)
        unos = VGroup(*[Text("1", color=TXT).scale(0.35).move_to([bars.x(i), y0 + 1.1, 0]) for i in range(13)])
        copia = Tallos([1] * 13, centro=(cx + 0.4, 0.9), paso=0.4, unidad=0.8, color=SENAL)
        copia.set_opacity(0.8)
        solape = Rectangle(width=12 * 0.4, height=2.4, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.16)
        solape.move_to([cx + 0.2, 1.7, 0])
        vals = [i + 1 for i in range(13)] + [12 - i for i in range(12)]
        ac = Tallos(vals, centro=(0.0, -2.0), paso=0.42, unidad=0.15, color=AMBAR)
        base_ac = ac.base
        t12 = Text("12", color=AMBAR, weight=BOLD).scale(0.55).move_to(ac.pos(13) + UP * 0.7 + RIGHT * 0.12)
        t11 = Text("11", color=AMBAR, weight=BOLD).scale(0.55).move_to(ac.pos(14) + UP * 1.05 + RIGHT * 0.1)
        t13 = Text("13", color=AMBAR, weight=BOLD).scale(0.55).move_to(ac.pos(12) + UP * 0.7 + LEFT * 0.12)
        env = VMobject(stroke_color=AMBAR, stroke_width=3).set_fill(opacity=0)
        env.set_points_as_corners([ac.pos(i) for i in range(25)])
        casi = MathTex(r"\approx", color=INK).scale(0.9).move_to([1.5, 0.15, 0])
        L = Lienzo(ancho=1.4, alto=0.8, t_rango=(0, 1), v_max=1.0, centro=(0.0, 0.0))
        rui = ruido_t(Lienzo(ancho=1.6, alto=0.8, t_rango=(0, 1), v_max=1.0, centro=(0.0, 1.65)), semilla=3, amp=0.5, color=RUIDO)
        cual = Text("¿cuál?", color=ROJO, weight=BOLD).scale(0.6).move_to([2.6, 0.9, 0])
        with self.narrar("b1"):
            # «un pulso rectangular»
            self.en("rect")
            self.play(FadeIn(rect), run_time=self.dur(0.6))
            # «de trece muestras»
            self.en("trece")
            self.play(FadeOut(rect), FadeIn(bars), run_time=self.dur(0.7))
            # «trece unos»
            self.en("unos")
            self.play(LaggedStart(*[FadeIn(u) for u in unos], lag_ratio=0.08), run_time=self.dur(0.8))
            # «Su autocorrelación sale sola»
            self.en("sale")
            self.play(FadeIn(base_ac), run_time=self.dur(0.4))
            # «al desplazarlo una muestra»
            self.en("una")
            self.play(FadeIn(copia), FadeIn(solape), run_time=self.dur(0.6))
            # «coinciden doce»
            self.en("doce")
            self.play(FadeIn(ac.palito(13)), FadeIn(ac.palito(11)), run_time=0.3)
            self.pop(t12)
            # «dos, once»
            self.en("once")
            self.play(copia.animate.shift(RIGHT * 0.4), solape.animate.stretch_to_fit_width(11 * 0.4).shift(RIGHT * 0.2),
                      run_time=0.4)
            self.play(FadeIn(ac.palito(14)), FadeIn(ac.palito(10)), run_time=0.3)
            self.pop(t11)
            # «y así»
            self.en("asi")
            resto = [i for i in range(25) if i not in (10, 11, 12, 13, 14)]
            self.play(FadeOut(copia), FadeOut(solape), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(ac.palito(i)) for i in resto], lag_ratio=0.05), run_time=self.dur(1.0))
            # «Un triángulo ancho»
            self.en("triangulo")
            self.play(Create(env), run_time=self.dur(0.8))
            # «El pico vale trece»
            self.en("pico13")
            self.play(FadeIn(ac.palito(12)), run_time=0.3)
            self.pop(t13)
            # «el vecino vale doce»
            self.en("vecino")
            self.resaltar(t12, color=ROJO, run_time=0.5)
            # «casi igual»
            self.en("casiigual")
            self.pop(casi)
            # «Con un poco de ruido»
            self.en("conruido")
            self.play(Create(rui), run_time=self.dur(0.8))
            # «no hay manera de saber cuál es el bueno»
            self.en("cual")
            self.pop(cual)
        self.wait(1.0)
        self.limpiar()
