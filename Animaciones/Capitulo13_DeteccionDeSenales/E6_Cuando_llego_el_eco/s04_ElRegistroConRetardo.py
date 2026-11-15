"""Escena 04 — Un eco a mano, sin ruido: la salida es la autocorrelación desplazada."""
from comun.escena import *


class ElRegistroConRetardo(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        X = -1.2
        reg = Tallos([0, 0, 0, 2, 2, 1, 0, 0], centro=(X, 2.0), paso=0.8, unidad=0.4, indices=True)
        pul = Tallos([2, 2, 1], centro=(-5.8, 2.0), paso=0.5, unidad=0.4)
        pul_g = VGroup(*pul.tallos, *pul.puntos)
        dest = VGroup(*[reg.tallos[i] for i in (3, 4, 5)], *[reg.puntos[i] for i in (3, 4, 5)])
        sin_r = Text("sin ruido", color=MEDIDA).scale(0.55).move_to([5.3, 2.3, 0])
        fl = DoubleArrow([reg.x(0), 3.25, 0], [reg.x(3), 3.25, 0], color=AMBAR, buff=0, stroke_width=4,
                         max_tip_length_to_length_ratio=0.12)
        dl = MathTex("D=3", color=AMBAR).scale(0.8).move_to([reg.x(1.5), 3.65, 0])
        fil = caja("filtro adaptado", AMBAR, ancho=3.4, alto=0.75, scale=0.5).move_to([X, 0.75, 0])
        h = Tallos([1, 2, 2], centro=(2.7, 0.55), paso=0.5, unidad=0.3, color=AMBAR)
        hl = MathTex("h", color=AMBAR).scale(0.8).move_to([2.7, 1.6, 0])
        fh = flecha([1.6, 0.75, 0], [0.6, 0.75, 0], AMBAR)
        sal = Tallos([0, 0, 0, 2, 6, 9, 6, 2, 0, 0], centro=(X, -1.5), paso=0.8, unidad=0.17, color=ESTIMACION,
                     indices=True)
        ac = Tallos([2, 6, 9, 6, 2], centro=(5.6, -1.5), paso=0.45, unidad=0.17, color=AMBAR)
        ac_l = Text("autocorrelación", color=INK).scale(0.42).move_to([5.6, -2.5, 0])
        flc = Arrow([4.5, -0.9, 0], [3.0, -0.9, 0], color=INK, buff=0, stroke_width=3)
        des = Text("desplazada 3", color=AMBAR).scale(0.45).move_to([3.7, -0.45, 0])
        with self.narrar("b1"):
            # «Veámoslo con números»
            self.en("numeros")
            self.play(FadeIn(reg.base), FadeIn(reg.ks), run_time=self.dur(0.6))
            # «sin ruido»
            self.en("sinruido")
            self.play(FadeIn(sin_r), run_time=0.4)
            # «Nuestro pulso, dos, dos, uno»
            self.en("pulso")
            self.play(FadeIn(pul_g), run_time=self.dur(0.6))
            # «llega con un retardo de tres muestras»
            self.en("retardo3")
            self.play(Transform(pul_g, dest), GrowArrow(fl), FadeIn(dl), run_time=self.dur(0.9))
            # «el registro es cero, cero, cero»
            self.en("ceros")
            self.play(*[FadeIn(reg.palito(i)) for i in (0, 1, 2)], run_time=self.dur(0.5))
            # «dos, dos, uno, cero, cero»
            self.en("resto")
            self.play(*[FadeIn(reg.palito(i)) for i in (6, 7)], run_time=self.dur(0.5))
            # «Lo pasamos por el filtro adaptado»
            self.en("filtro")
            self.play(FadeIn(fil), run_time=self.dur(0.5))
            # «uno, dos, dos»
            self.en("h")
            self.play(FadeIn(h), FadeIn(hl), GrowArrow(fh), run_time=self.dur(0.6))
            # «La salida es cero, cero, cero»
            self.en("salida0")
            self.play(FadeIn(sal.base), FadeIn(sal.ks), *[FadeIn(sal.palito(i)) for i in (0, 1, 2)],
                      run_time=self.dur(0.6))
            # «dos, seis, nueve»
            self.en("sube")
            self.play(LaggedStart(*[FadeIn(sal.palito(i)) for i in (3, 4, 5)], lag_ratio=0.5), run_time=self.dur(1.1))
            # «seis, dos, cero, cero»
            self.en("baja")
            self.play(LaggedStart(*[FadeIn(sal.palito(i)) for i in (6, 7, 8, 9)], lag_ratio=0.4), run_time=self.dur(1.1))
            # «la misma autocorrelación de antes»
            self.en("autocorr")
            self.play(FadeIn(ac), FadeIn(ac_l), run_time=self.dur(0.7))
            # «solo que desplazada»
            self.en("desplazada")
            self.play(GrowArrow(flc), FadeIn(des), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
