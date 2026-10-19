"""Escena 05 — La cuenta con las campanas: la razón de verosimilitud es e^(2r − 2)."""
from comun.escena import *
from comun.figuras_c9e3 import *


def exponente(base: Mobject, *partes, escala: float = 0.72, color=TXT) -> MathTex:
    """Exponente partido en piezas, ubicado como superíndice de `base` (sin llaves entre piezas)."""
    e = MathTex(*partes, color=color).scale(escala)
    e.next_to(base, UR, buff=0.04).shift(DOWN * 0.12)
    return e


class LaCuentaConCampanas(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.formula_campana()
        self.cociente()
        self.desarrollo()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def formula_campana(self):
        C = Campanas9(centro=(0, -2.7), ancho=11.0, alto=5.4)
        with self.narrar("b1"):
            # «para nuestras campanas»
            self.en("campanas")
            eje = C.eje((0, 1, 2))
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.9))

            # «tiene fórmula»
            self.en("formula")
            F = formula("f(r)", "=", "C", r"\cdot", "e", escala=1.15).move_to([-1.3, 2.75, 0])
            self.play(Write(F[0:2]), run_time=self.dur(0.5))

            # «una constante»
            self.en("cte")
            self.play(FadeIn(F[2:4], shift=LEFT * 0.15), run_time=self.dur(0.4))

            # «por e elevado a»
            self.en("e")
            hueco = DashedVMobject(Rectangle(width=2.6, height=0.55, color=INK, stroke_width=2), num_dashes=24)
            hueco.next_to(F[4], UR, buff=0.04).shift(DOWN * 0.12)
            self.play(FadeIn(F[4]), Create(hueco), run_time=self.dur(0.5))

            # «la distancia al centro al cuadrado»
            self.en("dist")
            ex = exponente(F[4], r"-(r - \mathrm{Centro})^2", r"/\,", r"2\sigma^2")
            y = C.p(0, 0.3)[1]
            d = DoubleArrow(C.p(-1.6, 0.3), C.p(0, 0.3), color=ESTIMACION, buff=0, stroke_width=4,
                            tip_length=0.18, max_tip_length_to_length_ratio=0.3)
            td = Text("Distancia al centro", color=ESTIMACION).scale(0.42).next_to(d, DOWN, buff=0.15)
            self.play(FadeOut(hueco), FadeIn(ex[0]), GrowFromCenter(d), FadeIn(td), run_time=self.dur(0.6))

            # «dos sigma cuadrado»
            self.en("sigma")
            self.play(FadeIn(ex[1:3], shift=LEFT * 0.15), run_time=self.dur(0.5))

            # «sigma vale uno»
            self.en("s1")
            s1 = MathTex(r"\sigma = 1", color=ESTIMACION).scale(0.9).move_to([4.6, 2.75, 0])
            self.pop(s1)

            # «el exponente»
            self.en("expo")
            self.play(Indicate(ex, color=ESTIMACION, scale_factor=1.15), run_time=self.dur(0.6))

            # «entre dos»
            self.en("entre2")
            dos = MathTex("2", color=TXT).scale(0.72).move_to(ex[2], aligned_edge=LEFT)
            self.play(ReplacementTransform(ex[2], dos), run_time=self.dur(0.5))
        self.campanas = VGroup(eje, c0, c1, d, td)
        self.F, self.ex, self.s1 = VGroup(F, ex[0], ex[1], dos), ex, s1

    # ------------------------------------------------------------------ b2
    def cociente(self):
        with self.narrar("b2"):
            # «Dividimos la campana del uno»
            self.en("div")
            lam = formula(LAMBDA, "=", escala=1.1, colores={0: MEDIDA}).move_to([-3.3, 0.95, 0])
            num_ = MathTex("C", r"\cdot", r"e^{-(r-2)^2/2}", color=C1).scale(1.0).move_to([-0.2, 1.5, 0])
            raya = Line([-1.9, 0.95, 0], [1.5, 0.95, 0], color=TXT, stroke_width=3)
            self.play(FadeOut(self.campanas), run_time=self.dur(0.3))
            self.play(Write(lam), Write(num_), Create(raya), run_time=self.dur(0.8))

            # «entre la del cero»
            self.en("del0")
            den = MathTex("C", r"\cdot", r"e^{-r^2/2}", color=C0).scale(1.0).move_to([-0.2, 0.4, 0])
            self.play(FadeIn(den, shift=UP * 0.15), run_time=self.dur(0.5))

            # «se cancelan»
            self.en("cancel")
            t1, t2 = tachar(num_[0]), tachar(den[0])
            self.play(Create(t1), Create(t2), run_time=self.dur(0.4))

            # «dividir potencias del mismo número»
            self.en("potencias")
            self.play(Indicate(num_[2], color=ESTIMACION, scale_factor=1.12),
                      Indicate(den[2], color=ESTIMACION, scale_factor=1.12), run_time=self.dur(0.6))

            # «restar los exponentes»
            self.en("restar")
            reg = MathTex(r"\frac{e^a}{e^b} = e^{a-b}", color=ESTIMACION).scale(0.85).move_to([4.6, 0.95, 0])
            marco = SurroundingRectangle(reg, color=ESTIMACION, buff=0.15, stroke_width=2)
            self.play(FadeIn(reg), Create(marco), run_time=self.dur(0.5))

            # «Queda e elevado a»
            self.en("queda")
            L3 = formula(LAMBDA, "=", "e", escala=1.1, colores={0: MEDIDA}).move_to([-3.3, -0.75, 0])
            self.play(Write(L3), run_time=self.dur(0.5))

            # «menos erre menos dos al cuadrado entre dos»
            self.en("t1")
            ex3 = exponente(L3[2], r"-(r-2)^2/2", r"+\,r^2/2", escala=0.8)
            ex3[0].set_color(C1)
            ex3[1].set_color(C0)
            self.play(FadeIn(ex3[0], shift=UP * 0.1), run_time=self.dur(0.5))

            # «más erre al cuadrado entre dos»
            self.en("t2")
            self.play(FadeIn(ex3[1], shift=UP * 0.1), run_time=self.dur(0.5))
        self.cuenta = VGroup(lam, num_, raya, den, t1, t2, reg, marco)
        self.L3, self.ex3 = L3, ex3

    # ------------------------------------------------------------------ b3
    def desarrollo(self):
        ex3 = self.ex3
        with self.narrar("b3"):
            # «Desarrollamos el cuadrado»
            self.en("desarrollo")
            L4 = formula("(r-2)^2", "=", "r^2", "-4r", "+4", escala=1.0).move_to([-1.2, -1.95, 0])
            L4.align_to(self.L3, LEFT).shift(RIGHT * 0.5)
            self.play(Write(L4[0:2]), run_time=self.dur(0.5))

            # «Erre menos dos, al cuadrado»
            self.en("rm2")
            self.play(Indicate(ex3[0], color=ESTIMACION, scale_factor=1.2), run_time=self.dur(0.6))

            # «es erre al cuadrado»
            self.en("r2")
            self.play(FadeIn(L4[2], shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «menos cuatro erre»
            self.en("m4r")
            self.play(FadeIn(L4[3], shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «más cuatro»
            self.en("mas4")
            self.play(FadeIn(L4[4], shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «se cancelan»
            self.en("tacha")
            ex4 = MathTex(r"-(", "r^2", r"-4r+4)/2", r"+\,", "r^2", "/2", color=TXT).scale(0.8)
            ex4.next_to(self.L3[2], UR, buff=0.04).shift(DOWN * 0.12)
            ex4[0:3].set_color(C1)
            ex4[3:6].set_color(C0)
            self.play(ReplacementTransform(ex3[0], ex4[0:3]), ReplacementTransform(ex3[1], ex4[3:6]),
                      run_time=self.dur(0.5))
            ta, tb = tachar(ex4[1]), tachar(ex4[4])
            self.play(Create(ta), Create(tb), run_time=self.dur(0.4))

            # «cuatro erre menos cuatro, entre dos»
            self.en("frac")
            L5 = formula("=", r"\frac{4r-4}{2}", "=", "2r-2", escala=1.0).next_to(L4, DOWN, buff=0.35)
            L5.align_to(L4, LEFT)
            self.play(FadeIn(L5[0:2], shift=UP * 0.1), run_time=self.dur(0.5))

            # «dos erre menos dos»
            self.en("res")
            L5[3].set_color(ESTIMACION)
            self.play(FadeIn(L5[2:4], shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «es e elevado a dos erre menos dos»
            self.en("marco")
            final = formula(LAMBDA, "=", r"e^{2r-2}", escala=1.5, colores={0: MEDIDA, 2: ESTIMACION})
            final.move_to([0, -0.4, 0])
            caja_ = SurroundingRectangle(final, color=ESTIMACION, buff=0.3, stroke_width=4)
            self.play(FadeOut(VGroup(self.cuenta, self.L3, ex4, ta, tb, L4, L5)), run_time=self.dur(0.3))
            self.play(Write(final), run_time=self.dur(0.6))
            self.play(Create(caja_), run_time=self.dur(0.4))
            self.sfx("exito")
