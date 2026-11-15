"""Escena 08 — Mediciones blancas con números: σ² = 2, C_yx = (1, 2, 1, 0,5) y h = (0,5; 1; 0,5; 0,25)."""
from comun.escena import *


class ConNumerosInventados(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        t = tabla_blanca()
        s2 = formula(r"\sigma^2=2", escala=1.1, colores={0: AMBAR}).move_to([0, 3.4, 0])
        div = Arrow([5.2, 0.7, 0], [5.2, -0.1, 0], color=INK, stroke_width=3, buff=0)
        ldiv = MathTex(r"\div 2", color=INK).scale(0.8).move_to([6.1, 0.3, 0])
        barras = Tallos([0.5, 1, 0.5, 0.25], centro=(0.3, -3.3), paso=1.8, unidad=0.9, color=ESTIMACION)
        noc = etiqueta("no causal", INK, 0.55).move_to([-4.7, -3.3, 0])
        marco = Rectangle(width=1.2, height=7.0, color=ROJO, stroke_width=4).set_fill(ROJO, 0.06)
        marco.move_to([COL_X[0], -0.4, 0])
        with self.narrar("b1"):
            # «Con números inventados»
            self.en("inv")
            self.play(*[FadeIn(r) for r in t.rots], *[FadeIn(m) for m in t.ms], run_time=self.dur(0.7))

            # «Sigma cuadrado vale dos»
            self.en("s2")
            self.pop(s2)

            # «uno en menos uno»
            self.en("c1")
            self.play(FadeIn(t.cs[0], shift=DOWN * 0.15), run_time=self.dur(0.3))

            # «dos en cero»
            self.en("c2")
            self.play(FadeIn(t.cs[1], shift=DOWN * 0.15), run_time=self.dur(0.3))

            # «uno en uno»
            self.en("c3")
            self.play(FadeIn(t.cs[2], shift=DOWN * 0.15), run_time=self.dur(0.3))

            # «cero coma cinco en dos»
            self.en("c4")
            self.play(FadeIn(t.cs[3], shift=DOWN * 0.15), run_time=self.dur(0.3))

            # «Dividimos entre dos»
            self.en("div")
            self.play(GrowArrow(div), FadeIn(ldiv), run_time=self.dur(0.5))

            # «cero coma cinco, uno, cero coma cinco»
            self.en("h")
            self.play(LaggedStart(*[FadeIn(t.hs[i], shift=DOWN * 0.15) for i in range(3)], lag_ratio=0.3),
                      FadeIn(barras.base), run_time=self.dur(1.2))
            self.play(*[GrowFromEdge(barras.tallos[i], DOWN) for i in range(3)],
                      *[FadeIn(barras.puntos[i]) for i in range(3)], run_time=self.dur(0.6))

            # «y cero coma dos cinco»
            self.en("h4")
            self.play(FadeIn(t.hs[3], shift=DOWN * 0.15), GrowFromEdge(barras.tallos[3], DOWN),
                      FadeIn(barras.puntos[3]), run_time=self.dur(0.5))

            # «filtro no causal»
            self.en("noc")
            self.play(FadeIn(noc), run_time=self.dur(0.4))

            # «una muestra del futuro»
            self.en("fut")
            self.play(Create(marco), run_time=self.dur(0.6))
            self.sfx("tick")

        self.wait(1.0)
        self.limpiar()
