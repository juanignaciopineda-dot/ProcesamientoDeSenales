"""Escena 16 — Los mismos dos ecos con Barker: dos picos de trece y un valle."""
from comun.escena import *


class DosAvionesConBarker(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        a = autocorr13(BARKER13)
        s = np.zeros(28)
        s[0:25] += a
        s[3:28] += a
        suma = Tallos([float(v) for v in s], centro=(0.0, -0.9), paso=0.38, unidad=0.17, color=AMBAR)
        b1 = Tallos(list(BARKER13), centro=(-3.6, 3.3), paso=0.3, unidad=0.2, color=SENAL)
        b2 = Tallos(list(BARKER13), centro=(-2.7, 2.5), paso=0.3, unidad=0.2, color=SENAL)
        a1 = avion(AZUL).scale(0.7).move_to([-6.2, 3.3, 0])
        a2 = avion(AZUL).scale(0.7).move_to([-6.2, 2.5, 0])
        tres = BraceBetweenPoints(suma.pos(12) + UP * 0.9, suma.pos(15) + UP * 0.9, direction=UP, color=AMBAR)
        tresl = Text("3 muestras", color=AMBAR).scale(0.5).next_to(tres, UP, buff=0.05)
        cero = Text("0", color=VERDE, weight=BOLD).scale(0.8).move_to([suma.x(15), -1.4, 0])
        h13a = Text("13", color=AMBAR, weight=BOLD).scale(0.6).move_to(suma.pos(12) + LEFT * 0.35)
        h13b = Text("13", color=AMBAR, weight=BOLD).scale(0.6).move_to(suma.pos(15) + RIGHT * 0.35)
        valle = Rectangle(width=2 * 0.38, height=3.6, color=VERDE, stroke_width=0).set_fill(VERDE, 0.15)
        valle.move_to([(suma.x(13) + suma.x(14)) / 2, -0.4, 0])
        valle_t = Text("valle", color=VERDE).scale(0.5).move_to([(suma.x(13) + suma.x(14)) / 2, 1.9, 0])
        av_d = avion(AZUL).scale(0.7).move_to([3.6, 2.9, 0])
        av_d2 = avion(AZUL).scale(0.7).move_to([4.8, 2.9, 0])
        ok = tilde(VERDE, 0.6).move_to([5.9, 2.9, 0])
        with self.narrar("b1"):
            # «Con Barker»
            self.en("barker")
            self.play(FadeIn(a1), FadeIn(a2), FadeIn(b1), FadeIn(b2), FadeIn(suma.base), run_time=self.dur(0.7))
            # «cada eco da su pico de trece»
            self.en("picos13")
            self.play(FadeIn(suma.palito(12)), FadeIn(suma.palito(15)), run_time=0.4)
            self.play(FadeIn(h13a), FadeIn(h13b), run_time=0.3)
            # «los lóbulos laterales son cero o uno»
            self.en("lobulos")
            self.play(LaggedStart(*[FadeIn(suma.palito(i)) for i in range(28) if i not in (12, 15)], lag_ratio=0.04),
                      run_time=self.dur(1.2))
            # «A tres muestras de distancia»
            self.en("tres")
            self.play(Create(tres), FadeIn(tresl), run_time=self.dur(0.7))
            # «el lóbulo del vecino vale cero»
            self.en("vecino0")
            self.pop(cero)
            # «los dos picos conservan la altura completa»
            self.en("asique")
            self.resaltar(suma.palito(12), suma.palito(15), color=AMBAR, run_time=0.5)
            self.en("altura")
            self.resaltar(h13a, h13b, color=AMBAR, run_time=0.5)
            # «con un valle claro en medio»
            self.en("valle")
            self.play(FadeIn(valle), FadeIn(valle_t), run_time=self.dur(0.6))
            # «Se ven dos aviones»
            self.en("dosaviones")
            self.play(FadeIn(av_d), FadeIn(av_d2), FadeIn(ok), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
