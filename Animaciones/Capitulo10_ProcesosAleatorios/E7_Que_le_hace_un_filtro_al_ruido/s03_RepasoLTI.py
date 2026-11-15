"""Escena 03 — Repaso: un sistema LTI queda descrito por su respuesta al impulso (el promediador)."""
from comun.escena import *


class RepasoLTI(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        bl = BloqueLTI(r"\text{LTI}", centro=(0.0, 1.4), ancho=2.6, alto=1.4, largo=2.0)
        eje_t = Arrow([-4.0, -0.25, 0], [4.0, -0.25, 0], color=INK, stroke_width=2, buff=0, max_tip_length_to_length_ratio=0.05)
        lt = MathTex("t", color=INK).scale(0.6).move_to([4.15, -0.55, 0])
        golpe = Tallos([1.0], centro=(-2.55, 1.4), paso=0.6, unidad=0.7, color=AMBAR)
        lab_d = MathTex(r"\delta", color=AMBAR).scale(0.7).next_to(golpe, UP, buff=0.12)
        h_mini = Tallos([0.3, 0.6, 0.9, 0.55, 0.3, 0.1], centro=(2.55, 1.4), paso=0.22, unidad=0.7, color=ESTIMACION)
        h_mini.base.set_opacity(1)
        lab_h = MathTex(r"h", color=ESTIMACION).scale(0.8).next_to(h_mini, UP, buff=0.15)

        prom = caja("promediador", AZUL, ancho=3.4, alto=0.75, scale=0.5).move_to([0, 1.4, 0])
        muestras = tira_pm1([1, -1, 1, 1, -1, 1], lado=0.5).move_to([0, -1.2, 0])
        par = SurroundingRectangle(VGroup(muestras.celdas[2], muestras.celdas[3]), color=AMBAR, buff=0.06)
        g_h = Tallos([0.5, 0.5], centro=(0, -2.3), paso=0.9, unidad=1.8, color=ESTIMACION, k0=0, indices=True, extra=1.5)
        f0 = MathTex(r"h[0]=\tfrac12", color=TXT).scale(0.8).move_to([-2.3, -2.6, 0])
        f1 = MathTex(r"h[1]=\tfrac12", color=TXT).scale(0.8).move_to([2.3, -2.6, 0])
        d_t = Tallos([1.0, 1.0, 0.0, 0.0], centro=(0, -2.3), paso=0.9, unidad=1.8, color=ESTIMACION, extra=1)

        with self.narrar("b1"):
            # «sistema lineal e invariante»
            self.en("lti")
            self.play(FadeIn(bl), run_time=self.dur(0.6))

            # «en el tiempo»
            self.en("tiempo")
            self.play(Create(eje_t), FadeIn(lt), run_time=self.dur(0.5))

            # «Queda descrito entero»
            self.en("entero")
            self.resaltar(bl.caja, color=AMBAR, escala=1.08)

            # «respuesta al impulso»
            self.en("resp")
            self.play(FadeIn(golpe), FadeIn(lab_d), run_time=self.dur(0.4))
            self.play(FadeIn(h_mini, shift=RIGHT * 0.3), run_time=self.dur(0.6))

            # «hache»
            self.en("hache")
            self.pop(lab_h)

            # «un golpe instantáneo»
            self.en("golpe")
            self.resaltar(golpe, color=AMBAR, escala=1.4)

            # «Tomemos uno sencillo»
            self.en("sencillo")
            self.play(FadeOut(golpe), FadeOut(lab_d), FadeOut(h_mini), FadeOut(lab_h), FadeOut(bl.rot), run_time=0.3)

            # «en tiempo discreto»
            self.en("discreto")
            self.play(Create(Line([-2.4, -1.85, 0], [2.4, -1.85, 0], color=INK, stroke_width=1.8)), run_time=self.dur(0.4))

            # «el que promedia»
            self.en("promedia")
            self.play(FadeIn(prom), run_time=self.dur(0.4))

            # «las dos últimas muestras»
            self.en("dos")
            self.play(FadeIn(muestras), run_time=self.dur(0.5))
            self.play(Create(par), run_time=self.dur(0.4))

            # «Su respuesta al impulso»
            self.en("su_resp")
            self.play(FadeOut(muestras), FadeOut(par), FadeOut(eje_t), FadeOut(lt), run_time=0.3)
            self.play(FadeIn(d_t), run_time=self.dur(0.4))

            # «un medio en cero»
            self.en("h0")
            self.play(ReplacementTransform(d_t, g_h), run_time=self.dur(0.6))
            self.play(FadeIn(f0), run_time=0.3)

            # «un medio en uno»
            self.en("h1")
            self.play(FadeIn(f1), run_time=0.3)

            # «y nada más»
            self.en("nada")
            vacio = Text("nada más", color=INK).scale(0.5).move_to([4.3, -1.6, 0])
            self.play(FadeIn(vacio), run_time=0.3)
        self.wait(1.0)
        self.limpiar()
