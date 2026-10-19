"""Escena 07 — ¿Cero o uno en −4 V? Con la campana del uno más ancha, gana el uno."""
from comun.escena import *
from comun.figuras_c9e3 import *

R = -4.0


class MasCercaNoBasta(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.C = CampanasS9(centro=(0, -2.6), ancho=12.0, alto=5.6, r_rango=(-5.5, 6.0), v_max=0.45)
        self.plantear()
        self.respuesta()
        self.wait(1.0)
        self.zoom_reset(run_time=0.5)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def plantear(self):
        C = self.C
        with self.narrar("b1"):
            # «Un cambio pequeño»
            self.en("cambio")
            eje = C.eje((-4, -2, 0, 2, 4))
            self.play(FadeIn(eje), run_time=self.dur(0.4))

            # «con más ruido»
            self.en("ruido")
            p0 = pulso_ruidoso9(centro=(-2.6, 2.5), alto=0.0, ruido=0.03, semilla=2, color=C0)
            p1 = pulso_ruidoso9(centro=(2.6, 2.5), alto=1.0, ruido=0.16, semilla=4, color=C1)
            r0 = Text("Cero", color=C0, weight=BOLD).scale(0.45).move_to([-2.6, 1.55, 0])
            r1 = Text("Uno", color=C1, weight=BOLD).scale(0.45).move_to([2.6, 1.55, 0])
            pulsos = VGroup(p0, p1, r0, r1)
            self.play(Create(p0), Create(p1), FadeIn(r0), FadeIn(r1), run_time=self.dur(0.8))

            # «la fibra óptica»
            self.en("fibra")
            fib = fibra9(largo=8.0).move_to([0, 2.3, 0])
            tf = Text("Fibra óptica", color=TXT, weight=BOLD).scale(0.45).move_to([0, 3.25, 0])
            self.play(FadeOut(pulsos), FadeIn(fib), FadeIn(tf), run_time=self.dur(0.6))

            # «la luz encendida»
            self.en("encendida")
            g1 = garabato9(centro=(-2.0, 2.3), ancho=3.0, alto=0.9, semilla=7, color=C1)
            te = Text("Encendida", color=C1, weight=BOLD).scale(0.45).move_to([-2.0, 1.35, 0])
            self.play(Create(g1), FadeIn(te), run_time=self.dur(0.6))
            self.play(g1.animate(rate_func=there_and_back).shift(UP * 0.12), run_time=self.dur(0.4))

            # «más ruidosa que la apagada»
            self.en("apagada")
            g0 = garabato9(centro=(2.0, 2.3), ancho=3.0, alto=0.15, semilla=8, color=C0)
            ta = Text("Apagada", color=C0, weight=BOLD).scale(0.45).move_to([2.0, 1.35, 0])
            self.play(Create(g0), FadeIn(ta), run_time=self.dur(0.6))

            # «La campana del cero»
            self.en("campana0")
            c0 = C.campana_s(0, 1, C0)
            self.play(FadeOut(VGroup(fib, tf, g1, te, g0, ta)), run_time=self.dur(0.3))
            self.play(Create(c0), run_time=self.dur(0.8))

            # «centro cero y desvío uno»
            self.en("c0")
            l0 = Text("Cero · Desvío 1", color=C0, weight=BOLD).scale(0.45).move_to([C.p(0)[0] - 0.4, 0.3, 0])
            self.play(FadeIn(l0, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «centro dos y desvío dos»
            self.en("c1")
            c1 = C.campana_s(2, 2, C1)
            l1 = Text("Uno · Desvío 2", color=C1, weight=BOLD).scale(0.45).move_to([C.p(4.3)[0], -0.85, 0])
            self.play(Create(c1), FadeIn(l1), run_time=self.dur(0.8))

            # «igual de frecuentes»
            self.en("iguales")
            ig = MathTex(r"p_0 = p_1 = 0{,}5", color=TXT).scale(0.7).move_to([5.4, 3.4, 0])
            self.play(FadeIn(ig), run_time=self.dur(0.4))

            # «menos cuatro voltios»
            self.en("m4")
            regla = Line(C.p(R) + DOWN * 0.12, C.p(R) + UP * 1.3, color=MEDIDA, stroke_width=4)
            tr = MathTex(r"r = -4", color=MEDIDA).scale(0.65).move_to([C.p(R)[0] + 0.15, -1.0, 0])
            self.play(Create(regla), FadeIn(tr), run_time=self.dur(0.5))

            # «¿Cero o uno?»
            self.en("pregunta")
            preg = Text("¿Cero o uno?", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([0, 2.85, 0])
            op0 = casilla9("Cero, está más cerca", C0, ancho=3.6).move_to([-2.4, 1.6, 0])
            op1 = casilla9("Uno", C1, ancho=3.6).move_to([2.4, 1.6, 0])
            self.pop(preg)
            self.play(FadeIn(op0, shift=UP * 0.15), FadeIn(op1, shift=UP * 0.15), run_time=self.dur(0.5))

            # «Piénsalo un momento»
            self.en("pausa")
            reloj = reloj_arena().scale(0.7).move_to([5.6, 1.6, 0])
            self.play(FadeIn(reloj), run_time=self.dur(0.3))
            self.play(Rotate(reloj, PI), run_time=self.dur(1.0))
        self.c0, self.c1, self.op0, self.op1 = c0, c1, op0, op1
        self.arriba = VGroup(preg, op0, op1, reloj, ig, l0, l1, tr)

    # ------------------------------------------------------------------ b2
    def respuesta(self):
        C = self.C
        with self.narrar("b2"):
            # «más cerca de cero que de dos»
            self.en("cerca")
            a0 = DoubleArrow(C.p(R) + DOWN * 0.75, C.p(0) + DOWN * 0.75, color=C0, buff=0, stroke_width=4,
                             tip_length=0.16, max_tip_length_to_length_ratio=0.2)
            a1 = DoubleArrow(C.p(R) + DOWN * 1.15, C.p(2) + DOWN * 1.15, color=C1, buff=0, stroke_width=4,
                             tip_length=0.16, max_tip_length_to_length_ratio=0.2)
            n0 = Text("4", color=C0, weight=BOLD).scale(0.42).next_to(a0, RIGHT, buff=0.15)
            n1 = Text("6", color=C1, weight=BOLD).scale(0.42).next_to(a1, RIGHT, buff=0.15)
            self.play(GrowFromCenter(a0), FadeIn(n0), run_time=self.dur(0.5))
            self.play(GrowFromCenter(a1), FadeIn(n1), run_time=self.dur(0.5))

            # «la respuesta es uno»
            self.en("uno")
            t = tachar(self.op0)
            m = SurroundingRectangle(self.op1, color=VERDE, buff=0.08, stroke_width=5)
            self.play(Create(t), Create(m), run_time=self.dur(0.5))
            self.sfx("exito")

            # «A cuatro desvíos»
            self.en("cuatro")
            self.play(FadeOut(VGroup(a0, a1, n0, n1)), run_time=self.dur(0.2))
            self.zoom(C.p(-3.4) + UP * 0.9, 6.0, run_time=self.dur(0.8))
            ticks0 = VGroup(*[Line(C.p(-k) + UP * 0.02, C.p(-k) + UP * 0.32, color=C0, stroke_width=4)
                              for k in (1, 2, 3, 4)])
            self.play(LaggedStart(*[Create(k) for k in ticks0], lag_ratio=0.3), run_time=self.dur(0.8))

            # «prácticamente ha desaparecido»
            self.en("desap")
            d0 = C.punto_s(0, 1, R, C0, radio=0.07)
            self.play(FadeIn(d0, scale=0.4), Indicate(self.c0, color=C0, scale_factor=1.0), run_time=self.dur(0.6))

            # «una diezmilésima»
            self.en("v0001")
            v0 = Text("0,0001", color=C0, weight=BOLD).scale(0.32).move_to(C.p(R) + UP * 0.75 + LEFT * 0.75)
            self.play(FadeIn(v0, shift=UP * 0.1), run_time=self.dur(0.4))

            # «a solo tres de sus desvíos»
            self.en("tres")
            ticks1 = VGroup(*[Line(C.p(2 - 2 * k) + DOWN * 0.02, C.p(2 - 2 * k) + DOWN * 0.3, color=C1,
                                   stroke_width=4) for k in (1, 2, 3)])
            self.play(LaggedStart(*[Create(k) for k in ticks1], lag_ratio=0.3), run_time=self.dur(0.7))

            # «diecisiete veces más»
            self.en("x17")
            d1 = C.punto_s(2, 2, R, C1, radio=0.07)
            v1 = Text("0,002", color=C1, weight=BOLD).scale(0.32).move_to(C.p(R) + UP * 0.75 + RIGHT * 0.75)
            x17 = Text("17 veces más", color=ESTIMACION, weight=BOLD).scale(0.4).move_to(C.p(R) + UP * 1.45 + RIGHT * 1.8)
            self.play(FadeIn(d1, scale=0.4), FadeIn(v1), run_time=self.dur(0.4))
            self.pop(x17)
