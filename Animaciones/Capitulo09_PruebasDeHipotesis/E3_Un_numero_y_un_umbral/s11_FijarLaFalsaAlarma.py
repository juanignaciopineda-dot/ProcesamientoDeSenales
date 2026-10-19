"""Escena 11 — Un cinco por ciento de falsas alarmas: umbral 1,645 y detección 0,64."""
from comun.escena import *
from comun.figuras_c9e3 import *

U = 1.645


class FijarLaFalsaAlarma(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.C = Campanas9()
        self.umbral()
        self.deteccion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def umbral(self):
        C = self.C
        vt = ValueTracker(0.6)
        self.vt = vt
        with self.narrar("b1"):
            # «el ruido solo»
            self.en("ruido")
            eje = C.eje((0, 1, 2))
            c0 = C.campana(0, 1, C0)
            l0 = Text("Ruido solo", color=C0, weight=BOLD).scale(0.5).move_to(C.p(-1.9, 0.43))
            self.play(FadeIn(eje), Create(c0), FadeIn(l0), run_time=self.dur(0.8))

            # «el eco»
            self.en("eco")
            c1 = C.campana(2, 1, C1)
            l1 = Text("Eco", color=C1, weight=BOLD).scale(0.5).move_to(C.p(3.9, 0.43))
            self.play(Create(c1), FadeIn(l1), run_time=self.dur(0.7))

            # «Buscamos el umbral»
            self.en("buscar")
            marca = always_redraw(lambda: Line(C.p(vt.get_value()) + DOWN * 0.1, C.p(vt.get_value()) + UP * 3.5,
                                               color=ESTIMACION, stroke_width=4))
            self.play(Create(marca), run_time=self.dur(0.3))
            self.play(vt.animate.set_value(1.1), run_time=self.dur(0.6), rate_func=there_and_back)

            # «un cinco por ciento de cola»
            self.en("cola")
            area = always_redraw(lambda: C.area(0, 1, vt.get_value(), 5, ERROR, 0.55))
            tc = Text("Cola", color=ERROR, weight=BOLD).scale(0.42).move_to(C.p(3.2, 0.02))
            self.play(FadeIn(area), FadeIn(tc), run_time=self.dur(0.5))

            # «en la campana del ruido»
            self.en("delruido")
            self.play(Indicate(l0, color=C0), Indicate(c0, color=C0, scale_factor=1.0), run_time=self.dur(0.6))

            # «la función cu al revés»
            self.en("qinv")
            Q = formula("Q(x) =", r"0{,}05", r"\;\Rightarrow\;", "x =", r"\,?", escala=0.95,
                        colores={1: ERROR, 4: ESTIMACION}).move_to([0, 3.15, 0])
            self.play(Write(Q), run_time=self.dur(0.8))

            # «dada un área»
            self.en("area")
            fl = C.area(0, 1, vt.get_value(), 5, ERROR, 0.95)
            self.play(FadeIn(fl, rate_func=there_and_back), run_time=self.dur(0.5))
            self.remove(fl)

            # «qué punto la deja»
            self.en("punto")
            gruesa = Line(C.p(vt.get_value()) + DOWN * 0.1, C.p(vt.get_value()) + UP * 3.5, color=ESTIMACION,
                          stroke_width=10)
            self.play(FadeIn(gruesa, rate_func=there_and_back), run_time=self.dur(0.5))
            self.remove(gruesa)

            # «Para un cinco por ciento»
            self.en("para5")
            self.play(Indicate(Q[1], color=ERROR, scale_factor=1.3), run_time=self.dur(0.4))
            self.play(vt.animate.set_value(U), run_time=self.dur(1.3))

            # «uno coma seiscientos cuarenta y cinco»
            self.en("u1645")
            v = MathTex(r"1{,}645", color=ESTIMACION).scale(0.95).move_to(Q[4], aligned_edge=LEFT)
            tu = Text("1,645", color=ESTIMACION, weight=BOLD).scale(0.45).move_to([C.p(U)[0], -3.05, 0])
            t5 = Text("5 %", color=ERROR, weight=BOLD).scale(0.42).move_to(tc)
            self.play(ReplacementTransform(Q[4], v), FadeIn(tu), ReplacementTransform(tc, t5),
                      run_time=self.dur(0.5))
            self.sfx("tick")
        self.Q, self.v, self.c0, self.c1 = Q, v, c0, c1

    # ------------------------------------------------------------------ b2
    def deteccion(self):
        C = self.C
        with self.narrar("b2"):
            # «Ahora la detección»
            self.en("det")
            det = Text("Detección", color=VERDE, weight=BOLD).scale(0.55).move_to([4.3, 2.5, 0])
            self.play(FadeIn(det, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «el área de la campana del eco»
            self.en("areaeco")
            ae = C.area(2, 1, U, 5, VERDE, 0.4)
            self.play(FadeIn(ae), run_time=self.dur(0.6))

            # «a la derecha de ese umbral»
            self.en("derumb")
            gruesa = Line(C.p(U) + DOWN * 0.1, C.p(U) + UP * 3.5, color=ESTIMACION, stroke_width=10)
            self.play(FadeIn(gruesa, rate_func=there_and_back), run_time=self.dur(0.5))
            self.remove(gruesa)

            # «un poco a la izquierda de su centro»
            self.en("izq")
            y = C.p(0, 0.43)[1]
            fl = Arrow([C.p(U)[0], y, 0], [C.p(2)[0] + 0.05, y, 0], color=ESTIMACION, buff=0, stroke_width=4,
                       max_tip_length_to_length_ratio=0.45)
            self.play(GrowArrow(fl), run_time=self.dur(0.4))

            # «algo más de la mitad»
            self.en("mitad")
            mid = DashedLine(C.p(2), C.p(2, C.f(2, 2)), color=C1, stroke_width=3)
            tm = MathTex(r"> \tfrac{1}{2}", color=VERDE).scale(0.8).move_to(C.p(3.05, 0.2))
            self.play(Create(mid), FadeIn(tm), run_time=self.dur(0.5))

            # «cero coma sesenta y cuatro»
            self.en("v064")
            det2 = Text("Detección = 0,64", color=VERDE, weight=BOLD).scale(0.55).move_to(det)
            self.play(ReplacementTransform(det, det2), run_time=self.dur(0.4))
            self.sfx("exito")

            # «dos de cada tres aviones»
            self.en("aviones")
            avs = VGroup(*[avion_arriba(INK).scale(0.55) for _ in range(3)]).arrange(RIGHT, buff=0.35)
            avs.move_to([4.3, 1.75, 0])
            self.play(FadeIn(avs, shift=LEFT * 0.2), run_time=self.dur(0.4))
            self.play(avs[0].animate.set_fill(VERDE, 1), avs[1].animate.set_fill(VERDE, 1), run_time=self.dur(0.4))

            # «un cinco por ciento de falsas alarmas»
            self.en("fa")
            fa = Text("Falsa alarma = 5 %", color=ERROR, weight=BOLD).scale(0.55).move_to([-4.2, 2.5, 0])
            self.play(FadeIn(fa, shift=DOWN * 0.1), run_time=self.dur(0.4))
