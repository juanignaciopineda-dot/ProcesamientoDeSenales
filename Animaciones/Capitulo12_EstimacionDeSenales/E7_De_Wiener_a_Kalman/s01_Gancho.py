"""Escena 01 — Gancho: Wiener y Kalman parecen distintos, y son el mismo."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        cw = caja("Wiener", AZUL, ancho=2.6, alto=1.1).move_to([-3.6, 1.8, 0])
        Lw = Lienzo(ancho=2.2, alto=0.8, t_rango=(0, 1), v_max=1.0, centro=(-3.6, 0.5))
        espw = curva_f(Lw, lambda u: 0.15 + 0.8 * np.exp(-((u - 0.3) / 0.2) ** 2), 0, 1, AZUL, 3.5)
        ck = caja("Kalman", AMBAR, ancho=2.6, alto=1.1).move_to([3.6, 1.8, 0])
        coh = cohete().scale(0.7).move_to([3.6, 0.5, 0])
        ne = MathTex(r"\neq", color=INK).scale(1.1).move_to([0, 1.8, 0])
        eq = MathTex("=", color=VERDE).scale(1.1).move_to([0, 1.8, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.2).move_to([0, 0.6, 0])
        term = termometro(1.4).move_to([0, -1.9, 0])
        a1 = flecha([-0.5, -1.7, 0], [-2.4, -0.7, 0])
        a2 = flecha([0.5, -1.7, 0], [2.4, -0.7, 0])
        n1 = MathTex("0{,}443", color=AMBAR).scale(0.8).move_to([-2.4, -1.9, 0])
        n2 = MathTex("0{,}443", color=AMBAR).scale(0.8).move_to([2.4, -1.9, 0])
        bw = Lw.base()
        gw = VGroup(cw, bw, espw)
        gk = VGroup(ck, coh)
        with self.narrar("b1"):
            # «El filtro de Wiener»
            self.en("wiener")
            self.play(FadeIn(cw), Create(bw), Create(espw), run_time=self.dur(0.9))
            # «el de Kalman»
            self.en("kalman")
            self.play(FadeIn(ck), FadeIn(coh), run_time=self.dur(0.7))
            # «dos inventos distintos»
            self.en("distintos")
            self.play(FadeIn(ne), run_time=0.3)
            self.pop(q)
            # «Con un sensor»
            self.en("sensor")
            self.play(FadeIn(term, shift=UP * 0.3), run_time=self.dur(0.6))
            # «una sola cuenta»
            self.en("cuenta")
            self.play(GrowArrow(a1), GrowArrow(a2), FadeIn(n1), FadeIn(n2), run_time=self.dur(0.8))
            # «son el mismo»
            self.en("mismo")
            self.play(FadeOut(q), Transform(ne, eq), FadeOut(a1), FadeOut(a2), FadeOut(n1), FadeOut(n2),
                      gw.animate.shift(RIGHT * 1.9), gk.animate.shift(LEFT * 1.9), run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
