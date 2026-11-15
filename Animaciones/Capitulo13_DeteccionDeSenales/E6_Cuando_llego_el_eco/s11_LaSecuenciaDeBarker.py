"""Escena 11 — La secuencia de Barker de trece y su autocorrelación."""
from comun.escena import *


def _rojos(t: Tallos, negativos) -> None:
    for i in negativos:
        t.tallos[i].set_color(ROJO)
        t.puntos[i].set_color(ROJO)


class LaSecuenciaDeBarker(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        neg = [i for i, v in enumerate(BARKER13) if v < 0]
        ins = Text("Barker", color=AMBAR, weight=BOLD).scale(1.4).move_to([0, 0.3, 0])
        tit = Text("Barker-13", color=AMBAR, weight=BOLD).scale(0.7).move_to([-5.2, 3.5, 0])
        bk = Tallos(list(BARKER13), centro=(0.0, 2.4), paso=0.45, unidad=0.55, color=SENAL)
        _rojos(bk, neg)
        copia = Tallos(list(BARKER13), centro=(0.45, 0.8), paso=0.45, unidad=0.55, color=SENAL)
        _rojos(copia, neg)
        copia.set_opacity(0.85)
        solape = Rectangle(width=12 * 0.45, height=3.0, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.12)
        solape.move_to([0.225, 1.6, 0])
        prods = [BARKER13[i] * BARKER13[i + 1] for i in range(12)]
        fila = VGroup(*[Text("+1" if p > 0 else "−1", color=INK).scale(0.4).move_to([bk.x(i + 1) + 0.0, -0.25, 0])
                        for i, p in enumerate(prods)])
        vals = [int(round(v)) for v in autocorr13(BARKER13)]
        ac = Tallos(vals, centro=(0.0, -2.6), paso=0.42, unidad=0.12, color=AMBAR)
        t13 = Text("13", color=AMBAR, weight=BOLD).scale(0.6).move_to(ac.pos(12) + UP * 0.4)
        c1 = Text("0 · 1", color=INK).scale(0.5).move_to([2.8, -1.8, 0])
        d12 = Text("12 productos", color=TXT).scale(0.5).move_to([4.8, 1.1, 0])
        s0 = formula("6", "-", "6", "=", "0", escala=0.9, colores={0: VERDE, 2: ROJO, 4: AMBAR}).move_to([4.8, -0.8, 0])
        anillo = Circle(radius=0.2, color=AMBAR, stroke_width=4).move_to(ac.pos(13))
        with self.narrar("b1"):
            # «Una solución clásica»
            self.en("clasica")
            self.pop(ins)
            # «la secuencia de Barker de trece»
            self.en("barker")
            self.play(FadeOut(ins), FadeIn(tit), FadeIn(bk.base), run_time=self.dur(0.5))
            # «más, más, más, más, más»
            self.en("cinco")
            self.play(LaggedStart(*[FadeIn(bk.palito(i)) for i in range(5)], lag_ratio=0.2), run_time=self.dur(0.9))
            # «menos, menos»
            self.en("menos2")
            self.play(*[FadeIn(bk.palito(i)) for i in (5, 6)], run_time=self.dur(0.5))
            # «más, más»
            self.en("mas2")
            self.play(*[FadeIn(bk.palito(i)) for i in (7, 8)], run_time=self.dur(0.5))
            # «menos, más, menos, más»
            self.en("resto")
            self.play(LaggedStart(*[FadeIn(bk.palito(i)) for i in (9, 10, 11, 12)], lag_ratio=0.25), run_time=self.dur(0.9))
            # «Su autocorrelación vale trece»
            self.en("trece")
            self.play(FadeIn(ac.base), FadeIn(ac.palito(12)), run_time=0.4)
            self.pop(t13)
            # «cualquier otro desplazamiento»
            self.en("otro")
            self.play(LaggedStart(*[FadeIn(ac.palito(i)) for i in range(25) if i != 12], lag_ratio=0.03),
                      run_time=self.dur(1.0))
            # «cero o uno»
            self.en("cerouno")
            self.play(FadeIn(c1), run_time=self.dur(0.4))
            # «Por ejemplo, con un desplazamiento»
            self.en("ejemplo")
            self.play(FadeOut(c1), FadeIn(copia), FadeIn(solape), Create(anillo), run_time=self.dur(0.9))
            # «doce productos»
            self.en("doce")
            self.play(FadeIn(fila), FadeIn(d12), run_time=self.dur(0.8))
            # «seis valen uno»
            self.en("seis1")
            self.play(*[fila[i].animate.set_color(VERDE) for i, p in enumerate(prods) if p > 0], run_time=self.dur(0.6))
            # «seis valen menos uno»
            self.en("seis2")
            self.play(*[fila[i].animate.set_color(ROJO) for i, p in enumerate(prods) if p < 0], run_time=self.dur(0.6))
            # «Suma cero»
            self.en("suma0")
            self.play(FadeIn(s0), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
