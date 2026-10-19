"""Escena 08 — Una parábola con dos raíces: 3r² + 4r − 9,55 ≥ 0."""
from comun.escena import *
from comun.figuras_c9e3 import *

RA, RB = -2.571, 1.238          # raíces de 3r² + 4r − 9,55


class LaParabolaDecide(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.logaritmo()
        self.parabola()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def logaritmo(self):
        with self.narrar("b1"):
            # «el logaritmo de la razón»
            self.en("lnl")
            F = formula(r"\ln\Lambda(r)", "=", r"\ln\tfrac{1}{2}", r"-\frac{(r-2)^2}{8}", r"+\frac{r^2}{2}",
                        escala=0.95, colores={0: MEDIDA, 2: ESTIMACION}).move_to([-0.6, 2.85, 0])
            self.play(Write(F[0:2]), run_time=self.dur(0.6))

            # «las constantes no se cancelan»
            self.en("ctes")
            C = CampanasS9(centro=(-0.6, -2.9), ancho=9.0, alto=4.4, r_rango=(-4.0, 7.0), v_max=0.45)
            eje = C.eje((0, 2), rotulo=False, escala=0.4)
            c0, c1 = C.campana_s(0, 1, C0, 3.5), C.campana_s(2, 2, C1, 3.5)
            k0 = MathTex("C", color=C0).scale(0.75).move_to(C.p(-1.4, 0.36))
            k1 = MathTex(r"C/2", color=C1).scale(0.75).move_to(C.p(5.0, 0.16))
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.8))
            self.play(FadeIn(k0), FadeIn(k1), run_time=self.dur(0.3))

            # «la mitad de alta»
            self.en("mitad")
            alto0, alto1 = C.fs(0, 1, 0), C.fs(2, 2, 2)
            top = DashedLine(C.p(0, alto0), C.p(3.2, alto0), color=INK, stroke_width=2.5)
            med = DashedLine(C.p(2, alto1), C.p(3.2, alto1), color=INK, stroke_width=2.5)
            fl = DoubleArrow(C.p(3.2, alto1), C.p(3.2, 0), color=C1, buff=0, stroke_width=3.5, tip_length=0.15)
            fl2 = DoubleArrow(C.p(3.5, alto0), C.p(3.5, 0), color=C0, buff=0, stroke_width=3.5, tip_length=0.15)
            m = MathTex(r"\tfrac{1}{2}", color=ESTIMACION).scale(0.85).next_to(fl, LEFT, buff=0.12)
            self.play(Create(top), Create(med), GrowFromCenter(fl), GrowFromCenter(fl2), run_time=self.dur(0.7))
            self.pop(m)

            # «el logaritmo de un medio»
            self.en("lnmedio")
            self.play(FadeIn(F[2], shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «los erre al cuadrado tampoco»
            self.en("r2")
            self.play(FadeIn(F[3:5], shift=LEFT * 0.1), run_time=self.dur(0.6))

            # «uno va dividido entre dos»
            self.en("div2")
            self.play(Indicate(F[4], color=C0, scale_factor=1.2), run_time=self.dur(0.6))

            # «el otro entre ocho»
            self.en("div8")
            dif = MathTex(r"\tfrac{1}{2} - \tfrac{1}{8} \neq 0", color=ESTIMACION).scale(0.8).move_to([5.3, 1.75, 0])
            self.play(Indicate(F[3], color=C1, scale_factor=1.2), FadeIn(dif), run_time=self.dur(0.6))
        self.F, self.dif = F, dif
        self.campanas = VGroup(eje, c0, c1, k0, k1, top, med, fl, fl2, m)

    # ------------------------------------------------------------------ b2
    def parabola(self):
        F = self.F
        # lienzo de la parábola: r de −3,6 a 2,4 y valores de −11 a 14
        x0, ex, y0, ey = -1.0, 1.15, -3.7, 0.144

        def P(r, v=0.0):
            return np.array([x0 + (r + 0.6) * ex, y0 + (v + 11) * ey, 0.0])

        def g(r):
            return 3 * r ** 2 + 4 * r - 9.55

        with self.narrar("b2"):
            # «Multiplicando todo por ocho»
            self.en("x8")
            x8 = MathTex(r"\times 8", color=ESTIMACION).scale(0.9).next_to(F, RIGHT, buff=0.35)
            self.play(FadeOut(self.campanas), FadeOut(self.dif), FadeIn(x8, shift=LEFT * 0.1),
                      run_time=self.dur(0.5))

            # «se dice uno cuando»
            self.en("cuando")
            d1 = Text("Decir 1 si", color=C1, weight=BOLD).scale(0.55).move_to([-3.6, 1.6, 0])
            self.play(FadeIn(d1, shift=RIGHT * 0.1), run_time=self.dur(0.4))
            Q = formula("3r^2", "+4r", r"-9{,}55", r"\geq 0", escala=1.05).next_to(d1, RIGHT, buff=0.35)

            # «tres erre al cuadrado»
            self.en("t3r2")
            self.play(FadeIn(Q[0], shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «más cuatro erre»
            self.en("t4r")
            self.play(FadeIn(Q[1], shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «menos nueve coma cincuenta y cinco»
            self.en("t955")
            self.play(FadeIn(Q[2], shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «es positivo»
            self.en("pos")
            Q[3].set_color(VERDE)
            self.play(FadeIn(Q[3], shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «una parábola que abre hacia arriba»
            self.en("parab")
            base = Line(P(-3.6), P(2.45), color=INK, stroke_width=2.4)
            rr = np.linspace(-3.55, 2.21, 120)
            curva = traza([P(r)[0] for r in rr], [P(r, g(r))[1] for r in rr], ESTIMACION, 4.5)
            self.play(Create(base), run_time=self.dur(0.3))
            self.play(Create(curva), run_time=self.dur(1.0))

            # «positiva fuera de sus dos raíces»
            self.en("fuera")
            b_izq = Line(P(-3.6), P(RA), color=VERDE, stroke_width=10)
            b_der = Line(P(RB), P(2.45), color=VERDE, stroke_width=10)
            self.play(Create(b_izq), Create(b_der), run_time=self.dur(0.6))

            # «La fórmula de la ecuación de segundo grado»
            self.en("bhaskara")
            bh = MathTex(r"r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", color=TXT).scale(0.95).move_to([4.8, -0.9, 0])
            self.play(FadeIn(bh, shift=LEFT * 0.15), run_time=self.dur(0.6))

            # «menos dos coma cincuenta y siete»
            self.en("raiz1")
            dA = Dot(P(RA), radius=0.1, color=ESTIMACION)
            tA = MathTex(r"-2{,}57", color=ESTIMACION).scale(0.8).move_to(P(RA) + UP * 0.35 + RIGHT * 0.6)
            self.play(FadeIn(dA, scale=0.5), FadeIn(tA), run_time=self.dur(0.4))

            # «uno coma veinticuatro»
            self.en("raiz2")
            dB = Dot(P(RB), radius=0.1, color=ESTIMACION)
            tB = MathTex(r"1{,}24", color=ESTIMACION).scale(0.8).move_to(P(RB) + UP * 0.35 + LEFT * 0.5)
            self.play(FadeIn(dB, scale=0.5), FadeIn(tB), run_time=self.dur(0.4))
