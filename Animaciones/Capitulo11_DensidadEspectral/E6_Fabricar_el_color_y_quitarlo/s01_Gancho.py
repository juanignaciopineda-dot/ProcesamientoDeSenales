"""Escena 01 — Gancho: dos filtros fabrican el mismo ruido; al deshacerlo, uno se apaga y el otro explota."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        b1 = BloqueLTI("H_1", centro=(-3.2, 2.1), ancho=1.8, alto=1.0, largo=1.4, color=CIAN, escala=0.8)
        b2 = BloqueLTI("H_2", centro=(-3.2, 0.1), ancho=1.8, alto=1.0, largo=1.4, color=AMBAR, escala=0.8)
        L1 = Lienzo(ancho=3.6, alto=1.2, t_rango=(0, 3), v_max=1.0, centro=(2.6, 2.1))
        L2 = Lienzo(ancho=3.6, alto=1.2, t_rango=(0, 3), v_max=1.0, centro=(2.6, 0.1))
        r1 = ruido_t(L1, semilla=7, amp=0.8)
        r2 = ruido_t(L2, semilla=7, amp=0.8)
        v1 = flecha([-0.9, 1.4, 0], [-5.5, 1.4, 0], ERROR, 3)
        v2 = flecha([-0.9, -0.6, 0], [-5.5, -0.6, 0], ERROR, 3)
        t_apaga = Tallos([1, -0.5, 0.25, -0.125], centro=(-3.5, -2.5), paso=0.7, unidad=0.9, color=VERDE)
        t_explota = Tallos([1, -2, 4, -8], centro=(3.5, -2.5), paso=0.7, unidad=0.17, color=ROJO)
        destello = Rectangle(width=3.4, height=2.6, color=ROJO, stroke_width=0).set_fill(ROJO, 0.35).move_to([3.5, -2.5, 0])
        with self.narrar("b1"):
            # «dos filtros distintos»
            self.en("dos")
            self.play(FadeIn(b1), FadeIn(b2), run_time=self.dur(0.7))

            # «exactamente el mismo ruido»
            self.en("mismo")
            self.play(Create(L1.base()), Create(r1), Create(L2.base()), Create(r2), run_time=self.dur(1.2),
                      rate_func=linear)

            # «intentas deshacerlo»
            self.en("deshacer")
            self.play(GrowArrow(v1), GrowArrow(v2), run_time=self.dur(0.7))

            # «se apaga»
            self.en("apaga")
            self.play(Create(t_apaga.base), *[FadeIn(t_apaga.palito(i)) for i in range(4)], run_time=self.dur(0.8))

            # «explota»
            self.en("explota")
            self.play(Create(t_explota.base), *[FadeIn(t_explota.palito(i)) for i in range(4)], run_time=self.dur(0.7))
            self.sfx("error")
            self.play(FadeIn(destello, rate_func=there_and_back), run_time=0.6)

            # «fabricamos ruido a medida»
            self.en("medida")
            self.corte()
            L = Lienzo(ancho=8.0, alto=3.0, t_rango=(-np.pi, np.pi), v_max=6.5, centro=(0, -0.3))
            base = L.base()
            c = curva_f(L, psd_eco, -np.pi, np.pi, RUIDO, 5)
            self.play(Create(base), Create(c), run_time=self.dur(1.0))
            self.play(c.animate.set_color(AMBAR), run_time=0.4)

            # «quitarlo»
            self.en("quitarlo")
            x = np.linspace(-np.pi, np.pi, 160)
            plana = L.curva(x, np.ones(160) * 1.0, AMBAR, 5)
            self.play(ReplacementTransform(c, plana), run_time=self.dur(1.0))
        self.wait(0.6)
        self.limpiar()
