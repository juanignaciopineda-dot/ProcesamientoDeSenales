"""Escena 06 — Variables discretas y continuas."""
from comun.escena import *


class DiscretasContinuas(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        # arriba: discretas; abajo: continuas
        r1 = RectaNum(0, 7, centro=(2.2, 1.9), ancho=7.0, marcas=[], color=INK)
        r2 = RectaNum(0, 7, centro=(2.2, -1.2), ancho=7.0, marcas=[], color=INK)
        pts = VGroup(*[Dot(r1.p(k), radius=0.17, color=AMBAR) for k in range(1, 7)])
        bits = VGroup(*[Dot(r1.p(k), radius=0.17, color=AMBAR) for k in (2, 5)])
        tramo = Line(r2.p(1), r2.p(6), color=AZUL, stroke_width=16)
        d = dado().scale(1.4).move_to([-4.9, 1.9, 0])
        bits_t = VGroup(*[Text(b, color=TXT, weight=BOLD).scale(1.0) for b in "10110"]).arrange(RIGHT, buff=0.15)
        bits_t.move_to([-4.9, 1.9, 0])
        L = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=1.5, centro=(-4.9, -1.2))
        t = np.linspace(0, 1, 80)
        cable = VGroup(L.base(), L.curva(t, 0.6 * np.sin(5 * np.pi * t), MEDIDA, 3.5))
        term = termometro(alto=2.0, nivel=0.55).move_to([-4.9, -1.2, 0])

        with self.narrar("b1"):
            self.en("contar")                                 # «se pueden contar uno a uno»
            self.play(FadeIn(r1), LaggedStart(*[FadeIn(p, scale=2) for p in pts], lag_ratio=0.2),
                      run_time=self.dur(1.2))
            self.en("caras")                                  # «las caras de un dado»
            self.play(FadeIn(d, scale=0.7), run_time=self.dur(0.5))
            self.en("bits")                                   # «los bits de un mensaje»
            self.play(FadeOut(d), FadeOut(pts[0]), FadeOut(pts[2]), FadeOut(pts[3]), FadeOut(pts[5]),
                      FadeIn(bits_t), run_time=self.dur(0.7))
            self.en("discretas")                              # «Se llaman discretas»
            pal1 = self.palabra("Discretas", AMBAR, 0.9).move_to([2.2, 3.3, 0])
            self.pop(pal1)
            self.en("otras")                                  # «Otras pueden tomar»
            self.play(r1.animate.fade(0.5), run_time=self.dur(0.5))
            self.en("intervalo")                              # «cualquier valor dentro de un intervalo»
            self.play(FadeIn(r2), Create(tramo), run_time=self.dur(1.2))
            self.en("tension")                                # «la tensión en un cable»
            self.play(FadeIn(cable, scale=0.8), run_time=self.dur(0.5))
            self.en("temperatura")                            # «la temperatura»
            self.play(FadeOut(cable), FadeIn(term, scale=0.8), run_time=self.dur(0.5))
            self.en("continuas")                              # «Se llaman continuas»
            pal2 = self.palabra("Continuas", AZUL, 0.9).move_to([2.2, -2.5, 0])
            self.pop(pal2)
            self.en("aparecen")                               # «En señales aparecen las dos»
            self.play(pal1.animate.scale(1.15), pal2.animate.scale(1.15), run_time=self.dur(0.5))
            self.en("necesitamos")                            # «necesitamos una forma»
            q = Text("?", color=AMBAR, weight=BOLD).scale(1.8).move_to([2.2, 0.35, 0])
            self.pop(q)
            self.en("herramienta")                            # «la misma herramienta»
            self.play(q.animate.scale(1.3).set_color(VERDE), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
