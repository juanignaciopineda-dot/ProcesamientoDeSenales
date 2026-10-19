"""Escena 11 — El error en el plano: los puntos de igual error forman rectas de pendiente p₀/p₁."""
from comun.escena import *
from comun.figuras_c9e4 import *

PLANO_11 = dict(origen=(-1.6, -3.2), lado=4.6)
X0, Y0 = 0.3, 0.4           # el punto de prueba
XD = 5.0                    # columna de rótulos a la derecha


class RectasDeIgualError(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.P = PlanoRoc9(**PLANO_11)
        self.formula()
        self.rectas()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def formula(self):
        P = self.P
        with self.narrar("b1"):
            # «¿Qué punto de la curva»
            self.en("pregunta")
            cur = P.curva()
            ut = ValueTracker(2.4)
            pt = always_redraw(lambda: P.punto(*roc9(ut.get_value()), color=TXT))
            q = always_redraw(lambda: Text("?", color=ROC, weight=BOLD).scale(0.55)
                              .next_to(P.p(*roc9(ut.get_value())), DR, buff=0.12))
            self.play(FadeIn(P), Create(cur), run_time=self.dur(0.6))
            self.play(FadeIn(pt), FadeIn(q), run_time=0.25)
            self.play(ut.animate.set_value(0.2), run_time=self.dur(1.4))
            self.play(ut.animate.set_value(1.6), run_time=self.dur(1.0))
            self.cur = cur

            # «Recuerda la fórmula»
            self.en("formula")
            f = MathTex("P_e", "=", "p_0", r"\cdot", "P_{FA}", "+", "p_1", r"\cdot", "P_M", color=TXT).scale(0.95)
            f[4].set_color(FA)
            f[8].set_color(ERROR)
            f.move_to([0, 2.75, 0])
            self.play(FadeIn(f[0:2], shift=DOWN * 0.15), run_time=self.dur(0.35))
            self.f = f

            # «pe cero por la falsa alarma»
            self.en("t1")
            self.play(FadeIn(f[2:5], shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «más pe uno por el fallo»
            self.en("t2")
            self.play(FadeIn(f[5:9], shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «uno menos la detección»
            self.en("t3")
            nueva = MathTex("P_e", "=", "p_0", r"\cdot", "P_{FA}", "+", "p_1", r"\cdot", "(1 - P_D)",
                            color=TXT).scale(0.95)
            nueva[4].set_color(FA)
            nueva[8].set_color(DET)
            nueva.move_to([0, 2.75, 0])
            self.play(TransformMatchingTex(f, nueva), run_time=self.dur(0.6))
            self.f = nueva
            pt.clear_updaters()
            q.clear_updaters()
            self.prueba = VGroup(pt, q)

    # ------------------------------------------------------------ b2
    def rectas(self):
        P = self.P
        f = self.f
        with self.narrar("b2"):
            # «Con setenta y treinta»
            self.en("pes")
            n = MathTex("P_e", "=", "0{,}7", r"\cdot", "P_{FA}", "+", "0{,}3", r"\cdot", "(1 - P_D)",
                        color=TXT).scale(0.95)
            n[2].set_color(C0)
            n[6].set_color(C1)
            n[4].set_color(FA)
            n[8].set_color(DET)
            n.move_to(f)
            self.play(TransformMatchingTex(f, n), FadeOut(self.prueba), self.cur.animate.set_stroke(opacity=0.35),
                      run_time=self.dur(0.6))
            self.f = n

            # «hacia la derecha»
            self.en("derecha")
            dot = P.punto(X0, Y0, color=TXT, radio=0.1)
            fr = Arrow(P.p(X0, Y0), P.p(X0 + 0.22, Y0), color=FA, buff=0.1, stroke_width=5,
                       max_tip_length_to_length_ratio=0.25)
            self.play(FadeIn(dot, scale=0.4), GrowArrow(fr), run_time=self.dur(0.45))

            # «cero coma siete por cada unidad»
            self.en("mas07")
            t07 = Text("+0,7 de error por unidad", color=FA).scale(0.42).move_to([XD, 0.4, 0])
            self.play(FadeIn(t07, shift=LEFT * 0.2), run_time=self.dur(0.45))

            # «de falsa alarma»
            self.en("ufa")
            self.play(dot.animate(rate_func=there_and_back).move_to(P.p(X0 + 0.15, Y0)), run_time=self.dur(0.8))

            # «hacia arriba»
            self.en("arriba")
            fu = Arrow(P.p(X0, Y0), P.p(X0, Y0 + 0.22), color=DET, buff=0.1, stroke_width=5,
                       max_tip_length_to_length_ratio=0.25)
            self.play(GrowArrow(fu), run_time=self.dur(0.4))

            # «coma tres por cada unidad»
            self.en("menos03")
            t03 = Text("−0,3 por unidad", color=DET).scale(0.42).move_to([XD, -0.3, 0], aligned_edge=LEFT)
            t03.align_to(t07, LEFT)
            self.play(FadeIn(t03), run_time=self.dur(0.4))

            # «Para quedarte»
            self.en("quedar")
            self.play(FadeOut(VGroup(fr, fu)), run_time=self.dur(0.35))

            # «el mismo error»
            self.en("mismo")
            tri = triangulo9(P, (X0, Y0), 0.15, P0 / P1, ancho=5)
            th = Text("1 a la derecha", color=FA).scale(0.4).next_to(tri.h, DOWN, buff=0.12)
            self.play(Create(tri.h), FadeIn(th), run_time=self.dur(0.45))

            # «dos coma treinta y tres»
            self.en("sube233")
            tv = Text("2,33 hacia arriba", color=DET).scale(0.4).next_to(tri.v, RIGHT, buff=0.12)
            self.play(Create(tri.v), FadeIn(tv), run_time=self.dur(0.6))

            # «forman rectas»
            self.en("recta")
            r = P.recta(P0 / P1, (X0, Y0), color=TXT, ancho=4)
            self.play(Create(r), run_time=self.dur(0.6))

            # «pe cero entre pe uno»
            self.en("pend")
            p1 = Text("Pendiente", color=TXT, weight=BOLD).scale(0.48)
            p2 = MathTex(r"= p_0 / p_1 = 2{,}33", color=TXT).scale(0.85)
            pg = VGroup(p1, p2).arrange(DOWN, buff=0.15).move_to([XD + 0.4, -1.8, 0])
            self.pop(pg)
