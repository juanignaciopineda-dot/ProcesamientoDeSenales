"""Escena 15 — Dos ecos cercanos con el pulso rectangular: una meseta de 23."""
from comun.escena import *


def _tri(x, c=0.0):
    return np.clip(13 - np.abs(x - c), 0, None)


class DosAvionesConElRectangular(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        a1 = avion(AZUL).scale(0.7).move_to([-6.2, 3.3, 0])
        a2 = avion(AZUL).scale(0.7).move_to([-6.2, 2.5, 0])
        p1 = Rectangle(width=3.9, height=0.4, color=SENAL, stroke_width=3).set_fill(SENAL, 0.4).move_to([-3.6, 3.3, 0])
        p2 = Rectangle(width=3.9, height=0.4, color=SENAL, stroke_width=3).set_fill(SENAL, 0.4).move_to([-2.7, 2.5, 0])
        sep = DoubleArrow([-5.55, 2.9, 0], [-4.65, 2.9, 0], color=AMBAR, buff=0, stroke_width=3,
                          max_tip_length_to_length_ratio=0.3)
        sept = Text("3 muestras", color=AMBAR).scale(0.45).move_to([-4.9, 2.95 + 0.0, 0]).shift(RIGHT * 2.8 + UP * 0.0)
        sin_r = Text("sin ruido", color=MEDIDA).scale(0.5).move_to([5.0, 3.3, 0])
        rl = Text("rectangular", color=TXT).scale(0.5).move_to([1.4, 3.3, 0])
        L = Lienzo(ancho=11.0, alto=3.2, t_rango=(-14, 17), v_max=26, centro=(0.0, -0.9))
        base = L.base()
        c1 = curva_f(L, lambda x: _tri(x, 0.0), -14, 14, AMBAR, 3.5, n=120)
        c2 = curva_f(L, lambda x: _tri(x, 3.0), -11, 17, CIAN, 3.5, n=120)
        suma = curva_f(L, lambda x: _tri(x, 0.0) + _tri(x, 3.0), -14, 17, VERDE, 5.0, n=240)
        l1013 = Text("13 + 10", color=TXT).scale(0.5).move_to(L.p(-6.0, 27))
        l1112 = Text("12 + 11", color=TXT).scale(0.5).move_to(L.p(9.0, 27))
        v23 = VGroup(*[Text("23", color=VERDE, weight=BOLD).scale(0.45).move_to(L.p(x, 26.5)) for x in (-0.6, 1.5, 3.6)])
        mes = Line(L.p(0, 23), L.p(3, 23), color=VERDE, stroke_width=9)
        mest = Text("meseta", color=VERDE, weight=BOLD).scale(0.6).move_to(L.p(1.5, 32))
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.4).move_to(L.p(-11.0, 31))
        uno = Text("¿uno o dos?", color=AMBAR, weight=BOLD).scale(0.8).move_to([4.8, 1.5, 0])
        av_u = avion(AZUL).scale(0.6).move_to([4.2, 0.4, 0])
        av_d = avion(AZUL).scale(0.6).move_to([5.4, 0.4, 0])
        with self.narrar("b1"):
            # «dos aviones»
            self.en("dos")
            self.play(FadeIn(a1), FadeIn(a2), run_time=self.dur(0.6))
            # «ecos llegan separados tres muestras»
            self.en("separados")
            self.play(FadeIn(p1), FadeIn(p2), run_time=0.4)
            self.play(GrowArrow(sep), FadeIn(sept), run_time=self.dur(0.5))
            # «Sin ruido»
            self.en("sinruido")
            self.play(FadeIn(sin_r), run_time=0.4)
            # «Con el pulso rectangular»
            self.en("rect")
            self.play(FadeIn(rl), FadeIn(base), run_time=self.dur(0.5))
            # «cada eco da su triángulo»
            self.en("triangulos")
            self.play(Create(c1), Create(c2), run_time=self.dur(1.3))
            # «los dos se suman»
            self.en("suman")
            self.play(Create(suma), c1.animate.set_stroke(opacity=0.35), c2.animate.set_stroke(opacity=0.35),
                      run_time=self.dur(1.0))
            # «trece más diez»
            self.en("13mas10")
            self.pop(l1013)
            # «doce más once»
            self.en("12mas11")
            self.pop(l1112)
            # «veintitrés, veintitrés, veintitrés»
            self.en("v23")
            self.play(LaggedStart(*[FadeIn(m) for m in v23], lag_ratio=0.35), run_time=self.dur(1.1))
            # «La salida es una meseta»
            self.en("meseta")
            self.play(Create(mes), FadeIn(mest), run_time=self.dur(0.7))
            # «No hay forma de saber»
            self.en("noforma")
            self.pop(q)
            # «si hay uno o dos aviones»
            self.en("unoodos")
            self.play(FadeIn(uno), FadeIn(av_u), FadeIn(av_d), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
