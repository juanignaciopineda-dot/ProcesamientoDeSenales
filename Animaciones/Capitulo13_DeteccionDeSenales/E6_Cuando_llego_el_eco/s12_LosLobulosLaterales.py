"""Escena 12 — Barker contra rectangular en decibelios; errores raros pero grandes."""
from comun.escena import *


def _barra(ancho: float, y: float, color) -> Rectangle:
    return Rectangle(width=ancho, height=0.45, color=color, stroke_width=2).set_fill(color, 0.55).move_to([-1.8 + ancho / 2, y, 0])


class LosLobulosLaterales(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        vb = [int(round(v)) for v in autocorr13(BARKER13)]
        vr = [i + 1 for i in range(13)] + [12 - i for i in range(12)]
        ab = Tallos(vb, centro=(-3.6, 0.9), paso=0.27, unidad=0.12, color=AMBAR)
        ar = Tallos(vr, centro=(3.6, 0.9), paso=0.27, unidad=0.12, color=AMBAR)
        nb = Text("Barker", color=TXT).scale(0.5).move_to([-3.6, 3.5, 0])
        nr = Text("rectangular", color=TXT).scale(0.5).move_to([3.6, 3.5, 0])
        lob = Circle(radius=0.15, color=ROJO, stroke_width=4).move_to(ab.pos(14))
        p13 = Text("13", color=AMBAR, weight=BOLD).scale(0.5).move_to(ab.pos(12) + UP * 0.35)
        db22 = formula(r"20\log\frac{1}{13}", r"\approx", r"-22\,\text{dB}", escala=0.8, colores={2: VERDE}).move_to([-3.6, -0.6, 0])
        dbr = formula(r"20\log\frac{12}{13}", r"\approx", r"-0{,}7\,\text{dB}", escala=0.8, colores={2: ROJO}).move_to([3.6, -0.6, 0])
        b12 = _barra(0.12 * 8, -1.7, VERDE)
        b56 = _barra(0.56 * 8, -2.5, ROJO)
        l12 = Text("Barker 12 %", color=TXT).scale(0.5).move_to([-4.5, -1.7, 0])
        l56 = Text("rectangular 56 %", color=TXT).scale(0.5).move_to([-4.0, -2.5, 0])
        pero = Text("pero…", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, 3.5, 0])
        L = Lienzo(ancho=6.5, alto=1.4, t_rango=(0, 1), v_max=1.0, centro=(-3.6, 0.9))
        rui = ruido_t(L, semilla=11, amp=0.8, color=RUIDO)
        sal = Arrow(ab.pos(12) + RIGHT * 0.3 + UP * 0.9, ab.pos(22) + UP * 0.9, color=ROJO, buff=0, stroke_width=5)
        gr = Text("error grande", color=ROJO, weight=BOLD).scale(0.5).move_to([-1.3, 2.9, 0])
        hb = Tallos([0.1, 0, 0.1, 0, 0.1, 0, 1.9, 0, 0.1, 0, 0.1, 0, 0.1], centro=(-3.5, -2.6), paso=0.3, unidad=0.7, color=VERDE)
        hr = Tallos([0, 0, 0.1, 0.25, 0.5, 0.8, 1.0, 0.8, 0.5, 0.25, 0.1, 0, 0], centro=(3.5, -2.6), paso=0.3, unidad=0.7, color=ROJO)
        with self.narrar("b1"):
            # «El lóbulo lateral más alto es uno»
            self.en("lobulo")
            self.play(FadeIn(nb), FadeIn(ab), FadeIn(nr), FadeIn(ar), run_time=self.dur(0.7))
            self.play(Create(lob), run_time=0.3)
            # «contra un pico de trece»
            self.en("pico")
            self.pop(p13)
            # «unos veintidós decibelios por debajo»
            self.en("db22")
            self.play(FadeIn(db22), run_time=self.dur(0.9))
            # «El rectangular, menos de uno»
            self.en("rect")
            self.play(FadeIn(dbr), run_time=self.dur(0.9))
            # «Con las mismas simulaciones»
            self.en("mismas")
            self.play(FadeOut(db22), FadeOut(dbr), run_time=0.3)
            # «Barker falla el retardo exacto»
            self.en("barkerfalla")
            self.play(FadeIn(l12), run_time=self.dur(0.5))
            # «doce veces de cada cien»
            self.en("doce")
            self.play(FadeIn(b12), FadeIn(l56), FadeIn(b56), run_time=self.dur(0.9))
            # «Aunque hay un matiz»
            self.en("matiz")
            self.pop(pero)
            # «cuando el ruido le gana»
            self.en("gana")
            self.play(FadeOut(b12), FadeOut(b56), FadeOut(l12), FadeOut(l56), Create(rui), run_time=self.dur(0.8))
            # «salta a un lóbulo lateral lejano»
            self.en("salta")
            self.play(GrowArrow(sal), run_time=self.dur(0.7))
            # «el error es grande»
            self.en("grande")
            self.pop(gr)
            # «Errores raros pero grandes»
            self.en("raros")
            self.play(FadeOut(rui), FadeIn(hb), run_time=self.dur(0.8))
            # «contra errores frecuentes pero pequeños»
            self.en("frecuentes")
            self.play(FadeIn(hr), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
