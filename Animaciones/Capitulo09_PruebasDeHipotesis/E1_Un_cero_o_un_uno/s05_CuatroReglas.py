"""Escena 05 — Las cuatro reglas posibles del canal y cuánto falla cada una."""
from comun.escena import *
from comun.figuras_c9e1 import *


class CuatroReglas(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.armar()
        self.llenar()
        self.wait(1.0)
        self.limpiar()

    def armar(self):
        with self.narrar("b1"):
            # «se puede comprobar»
            self.en("titulo")
            tit = Text("Cuatro reglas", color=TXT, weight=BOLD).scale(0.75).move_to([-0.6, 3.35, 0])
            self.play(FadeIn(tit, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «solo hay cuatro reglas»
            self.en("cuatro")
            cuatro = Text("4", color=ESTIMACION, weight=BOLD).scale(1.2).next_to(tit, RIGHT, buff=0.4)
            self.pop(cuatro)

            # «Lo recibido»
            self.en("rec")
            rt = Text("Recibido", color=MEDIDA).scale(0.55).move_to([-4.2, 2.1, 0])
            r0 = bit9(0, color=MEDIDA, lado=0.6).move_to([-4.2, 1.1, 0])
            r1 = bit9(1, color=MEDIDA, lado=0.6).move_to([-4.2, -0.1, 0])
            self.play(FadeIn(rt), FadeIn(r0), FadeIn(r1), run_time=self.dur(0.5))

            # «hay que decir cero o uno»
            self.en("decir")
            dt = Text("Decir", color=ESTIMACION).scale(0.55).move_to([-1.2, 2.1, 0])
            q0 = VGroup(Square(0.6, color=ESTIMACION, stroke_width=3),
                        Text("?", color=ESTIMACION).scale(0.5)).move_to([-1.2, 1.1, 0])
            q1 = q0.copy().move_to([-1.2, -0.1, 0])
            f0 = Arrow(r0.get_right(), q0.get_left(), color=INK, buff=0.15, stroke_width=3)
            f1 = Arrow(r1.get_right(), q1.get_left(), color=INK, buff=0.15, stroke_width=3)
            self.play(FadeIn(dt), GrowArrow(f0), GrowArrow(f1), FadeIn(q0), FadeIn(q1), run_time=self.dur(0.6))

            # «Dos»
            self.en("dosxdos")
            cuenta = MathTex(r"2 \times 2 = 4", color=ESTIMACION).scale(1.1).move_to([2.6, 0.5, 0])
            self.pop(cuenta)

            # «cuatro reglas.»
            self.en("tabla")
            self.play(FadeOut(VGroup(rt, r0, r1, dt, q0, q1, f0, f1, cuenta)), run_time=self.dur(0.3))
            T = TablaReglas9(centro=(0.0, -0.7))
            self.T = T
            self.play(FadeIn(T.titulos), Create(T.lineas), run_time=self.dur(0.6))

            # «cuánto falla cada una»
            self.en("error")
            self.play(LaggedStart(*[FadeIn(h) for h in T.huecos], lag_ratio=0.25), run_time=self.dur(0.6))

    def llenar(self):
        T = self.T
        x_marca = -5.4
        with self.narrar("b2"):
            # «Primera: creer lo recibido»
            self.en("r1")
            self.play(FadeIn(T.nombres[0], shift=RIGHT * 0.2), FadeIn(T.detalles[0]), run_time=self.dur(0.5))

            # «el canal cambia el bit»
            self.en("cambia")
            b = bit9(0, lado=0.42).move_to([x_marca, T.ys[0], 0])
            b2 = bit9(1, color=ERROR, lado=0.42).move_to(b)
            self.play(FadeIn(b), run_time=self.dur(0.3))
            self.play(ReplacementTransform(b, b2), run_time=self.dur(0.4))

            # «un diez por ciento»
            self.en("e1")
            self.play(ReplacementTransform(T.huecos[0], T.errores[0]), run_time=self.dur(0.4))

            # «decir siempre cero»
            self.en("r2")
            self.play(FadeIn(T.nombres[1], shift=RIGHT * 0.2), FadeIn(T.detalles[1]), run_time=self.dur(0.5))

            # «Falla cuando se envió un uno»
            self.en("falla2")
            u = bit9(1, lado=0.42).move_to([x_marca, T.ys[1], 0])
            self.play(FadeIn(u), run_time=self.dur(0.3))
            self.play(Create(tachar(u)), run_time=self.dur(0.3))

            # «un treinta por ciento»
            self.en("e2")
            self.play(ReplacementTransform(T.huecos[1], T.errores[1]), run_time=self.dur(0.4))

            # «decir siempre uno»
            self.en("r3")
            self.play(FadeIn(T.nombres[2], shift=RIGHT * 0.2), FadeIn(T.detalles[2]), run_time=self.dur(0.5))

            # «Falla el setenta»
            self.en("e3")
            self.play(ReplacementTransform(T.huecos[2], T.errores[2]), run_time=self.dur(0.4))

            # «llevar la contraria»
            self.en("r4")
            self.play(FadeIn(T.nombres[3], shift=RIGHT * 0.2), FadeIn(T.detalles[3]), run_time=self.dur(0.5))

            # «Falla el noventa»
            self.en("e4")
            self.play(ReplacementTransform(T.huecos[3], T.errores[3]), run_time=self.dur(0.4))

            # «Gana la primera»
            self.en("gana")
            m = T.marco(0, VERDE)
            self.play(Create(m), T.errores[0].animate.set_color(VERDE), run_time=self.dur(0.5))
            self.sfx("exito", gain=-18)

            # «máximo a posteriori»
            self.en("map")
            mp = Text("MAP", color=VERDE, weight=BOLD).scale(0.6).next_to(m, RIGHT, buff=0.25)
            self.pop(mp)
