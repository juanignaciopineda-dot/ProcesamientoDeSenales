"""Escena 13 — La falsa alarma es un presupuesto: cada nivel cuesta falsa alarma y rinde detección."""
from comun.escena import *
from comun.figuras_c9e3 import *


class ElPresupuesto(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.T = TablaNiveles9()
        self.tabla()
        self.presupuesto()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def tabla(self):
        T = self.T
        with self.narrar("b1"):
            # «un caso de juguete»
            self.en("juguete")
            det = detector9(escala=1.3).move_to([0, 0.3, 0])
            self.play(FadeIn(det, shift=UP * 0.2), run_time=self.dur(0.4))
            self.play(Rotate(det.aguja, -PI / 3, about_point=det.centro()), run_time=self.dur(0.6),
                      rate_func=there_and_back)

            # «un nivel, de uno a cinco»
            self.en("niveles")
            self.play(det.animate.scale(0.55).move_to([-5.5, -2.6, 0]), run_time=self.dur(0.5))
            self.play(LaggedStart(*[FadeIn(VGroup(c, e), shift=DOWN * 0.15) for c, e in zip(T.cas, T.encs)],
                                  lag_ratio=0.15), run_time=self.dur(0.8))

            # «Sin avión»
            self.en("sin")
            rs = T.rot(0, "Sin avión", C0)
            self.play(FadeIn(rs, shift=RIGHT * 0.15), run_time=self.dur(0.3))

            vs = T.fila(0, T.SIN, C0)
            for i, m in enumerate(("n1", "n2", "n3", "n4", "n5")):
                self.en(m)
                self.play(FadeIn(vs[i], scale=0.6), run_time=self.dur(0.3))

            # «Con avión, al revés»
            self.en("con")
            rc = T.rot(1, "Con avión", C1)
            vc = T.fila(1, T.CON, C1)
            self.play(FadeIn(rc, shift=RIGHT * 0.15), LaggedStart(*[FadeIn(v, scale=0.6) for v in vc], lag_ratio=0.15),
                      run_time=self.dur(0.8))

            # «en qué niveles se dice avión»
            self.en("elegir")
            cajitas = VGroup(*[Square(0.32, color=ESTIMACION, stroke_width=3).move_to([T.x(i), 3.3, 0]) for i in range(5)])
            self.play(LaggedStart(*[Create(c) for c in cajitas], lag_ratio=0.15), run_time=self.dur(0.6))

            # «un quince por ciento de falsas alarmas»
            self.en("limite")
            lim = Text("Falsa alarma ≤ 0,15", color=ERROR, weight=BOLD).scale(0.55).move_to([1.4, -1.35, 0])
            self.pop(lim)
        self.rs, self.rc, self.vs, self.vc, self.lim, self.cajitas = rs, rc, vs, vc, lim, cajitas

    # ------------------------------------------------------------------ b2
    def presupuesto(self):
        T = self.T
        with self.narrar("b2"):
            # «como un presupuesto»
            self.en("monedero")
            mon = monedero9("0,15").move_to([1.0, -2.55, 0])
            tp = Text("Presupuesto", color=ESTIMACION, weight=BOLD).scale(0.5).next_to(mon, RIGHT, buff=0.3)
            self.play(ReplacementTransform(self.lim, VGroup(mon, tp)), run_time=self.dur(0.6))

            # «Cada nivel que metes»
            self.en("metes")
            m = T.columna(2)
            self.play(Create(m), run_time=self.dur(0.4))
            self.play(FadeOut(m), run_time=self.dur(0.3))

            # «cuesta su probabilidad sin avión»
            self.en("cuesta")
            rcu = T.rot(0, "Cuesta", ERROR)
            self.play(ReplacementTransform(self.rs, rcu), self.vs.animate.set_color(ERROR), run_time=self.dur(0.5))

            # «eso es falsa alarma»
            self.en("fa")
            tfa = Text("Falsa alarma", color=INK).scale(0.36).next_to(rcu, DOWN, buff=0.08).align_to(rcu, RIGHT)
            self.play(FadeIn(tfa, shift=UP * 0.1), run_time=self.dur(0.4))

            # «Y rinde su probabilidad con avión»
            self.en("rinde")
            rri = T.rot(1, "Rinde", VERDE)
            self.play(ReplacementTransform(self.rc, rri), self.vc.animate.set_color(VERDE), run_time=self.dur(0.5))

            # «eso es detección»
            self.en("det")
            tde = Text("Detección", color=INK).scale(0.36).next_to(rri, DOWN, buff=0.08).align_to(rri, RIGHT)
            self.play(FadeIn(tde, shift=UP * 0.1), run_time=self.dur(0.4))

            # «El nivel cinco cuesta»
            self.en("c5")
            m5 = T.columna(4)
            self.play(Create(m5), Indicate(self.vs[4], color=ERROR, scale_factor=1.4), run_time=self.dur(0.6))

            # «rinde cero coma cuarenta»
            self.en("r5")
            self.play(Indicate(self.vc[4], color=VERDE, scale_factor=1.4), run_time=self.dur(0.6))

            # «El nivel tres cuesta»
            self.en("c3")
            m3 = T.columna(2)
            self.play(ReplacementTransform(m5, m3), Indicate(self.vs[2], color=ERROR, scale_factor=1.4),
                      run_time=self.dur(0.6))

            # «rinde cero coma quince»
            self.en("r3")
            self.play(Indicate(self.vc[2], color=VERDE, scale_factor=1.4), run_time=self.dur(0.6))
            self.play(FadeOut(m3), run_time=self.dur(0.3))
