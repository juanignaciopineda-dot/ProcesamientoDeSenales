"""Escena 03 — Qué hace un filtro: respuesta al impulso y convolución (dar la vuelta, deslizar, multiplicar, sumar)."""
from comun.escena import *


class ElFiltro(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        f = formula("g", "=", r"\sum", "r[n]", "s[n]", escala=1.2, colores={3: MEDIDA, 4: SENAL}).move_to([-1.0, 3.0, 0])
        q = interrogante13().move_to([2.4, 3.0, 0])
        bl = BloqueLTI("h", centro=(0, 0.7), ancho=2.2, alto=1.4, color=ESTIMACION, largo=2.4)
        h = Tallos(H13, centro=(0, -1.7), paso=0.7, unidad=0.35, color=ESTIMACION)
        hv = Tallos([2, 2, 1], centro=(0, -1.7), paso=0.7, unidad=0.35, color=ESTIMACION)
        lab_h = etiqueta("respuesta al impulso", INK, 0.5).move_to([0, -2.9, 0])
        delta = Tallos([1, 0, 0], centro=(-4.9, 0.7), paso=0.5, unidad=0.5, color=AMBAR)
        sale = Tallos(H13, centro=(4.9, 0.7), paso=0.5, unidad=0.3, color=ESTIMACION)
        r = Tallos(R13, centro=(-4.9, 0.7), paso=0.5, unidad=0.25, color=MEDIDA)
        suma = etiqueta("multiplicar y sumar", TXT, 0.6).move_to([3.7, -1.5, 0])
        with self.narrar("b1"):
            # «ge, la suma de recibido por señal»
            self.en("ge")
            self.play(Write(f), run_time=self.dur(1.4))

            # «cómo se calcula en la práctica»
            self.en("practica")
            self.pop(q)

            # «ahí entra un filtro»
            self.en("filtro")
            self.play(FadeOut(q), FadeIn(bl), run_time=self.dur(0.6))

            # «Recuerda cómo actúa un filtro»
            self.en("recuerda")
            self.resaltar(bl.caja, color=AMBAR, escala=1.08)

            # «una respuesta al impulso»
            self.en("respuesta")
            self.play(FadeIn(h), FadeIn(lab_h), run_time=self.dur(0.6))

            # «un único uno»
            self.en("ununo")
            self.play(FadeIn(delta), run_time=self.dur(0.4))
            self.play(FadeIn(sale, shift=RIGHT * 0.3), run_time=self.dur(0.5))

            # «Y para cualquier entrada»
            self.en("entrada")
            self.play(Transform(delta, r), FadeOut(sale), run_time=self.dur(0.6))

            # «dando la vuelta a esa respuesta»
            self.en("vuelta")
            self.sfx("whoosh")
            self.play(Transform(h, hv), run_time=self.dur(0.7))

            # «deslizándola sobre la entrada»
            self.en("desliza")
            self.play(h.animate.move_to([-4.9, -1.0, 0]).scale(0.8), FadeOut(lab_h), run_time=self.dur(0.7))
            self.play(h.animate.shift(RIGHT * 0.5), run_time=self.dur(0.7))
            self.play(h.animate.shift(RIGHT * 0.5), run_time=self.dur(0.7))

            # «multiplicando y sumando»
            self.en("suma")
            self.pop(suma)
        self.wait(1.0)
        self.limpiar()
