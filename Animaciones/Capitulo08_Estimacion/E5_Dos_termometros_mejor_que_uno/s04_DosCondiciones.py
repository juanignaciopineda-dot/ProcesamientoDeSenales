"""Escena 04 — Dos condiciones: cada covarianza con su porqué y el sistema resuelto por sustitución."""
from comun.escena import *
from comun.figuras_c8e5 import *


class DosCondiciones(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.con_a()
        self.con_b()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def con_a(self):
        X0 = -6.2
        con_a = Text("Con A", color=MEDIDA, weight=BOLD).scale(0.6).move_to([X0 + 0.6, 3.25, 0])
        e1 = formula("4", "-", "h_A", r"\cdot", "5", "-", "h_B", r"\cdot", "4", "=", "0", escala=1.35,
                     colores={2: ESTIMACION, 6: ESTIMACION})
        e1.move_to([X0, 2.1, 0], aligned_edge=LEFT)
        n0 = MathTex(r"\mathrm{cov}(y,x_A)", color=INK).scale(0.75).next_to(e1[0], DOWN, buff=0.55)
        n0.align_to(e1[0], LEFT).shift(LEFT * 0.2)
        n4 = MathTex(r"\mathrm{var}(x_A)=4+1", color=INK).scale(0.75).next_to(e1[4], DOWN, buff=1.05)
        n8 = MathTex(r"\mathrm{cov}(x_A,x_B)", color=INK).scale(0.75).next_to(e1[8], DOWN, buff=0.55)
        q = MathTex("?", color=AMBAR).scale(1.35).move_to(e1[8])
        # el diagrama de la derecha: la misma temperatura llega a los dos termómetros
        ty = MathTex("y", color=SENAL).scale(1.3).move_to([4.0, 0.9, 0])
        A = Termo8("A", centro=(2.7, -1.4), alto=1.8, escala_letra=0.8)
        B = Termo8("B", centro=(5.3, -1.4), alto=1.8, escala_letra=0.8)
        fa = Arrow(ty.get_bottom() + DOWN * 0.1, A.letra.get_top() + UP * 0.1, buff=0, color=SENAL, stroke_width=4,
                   max_tip_length_to_length_ratio=0.15)
        fb = Arrow(ty.get_bottom() + DOWN * 0.1, B.letra.get_top() + UP * 0.1, buff=0, color=SENAL, stroke_width=4,
                   max_tip_length_to_length_ratio=0.15)
        ra = A.debajo(ruido8(ancho=1.3, amp=0.06, semilla=2), 0.25)
        rb = B.debajo(ruido8(ancho=1.3, amp=0.2, semilla=9), 0.25)
        self.dib = VGroup(ty, A, B, fa, fb, ra, rb)

        with self.narrar("b1"):
            # «Primera condición, con A»
            self.en("con_a")
            self.pop(con_a)

            # «La covarianza de la temperatura con A»
            self.en("cov")
            self.play(FadeIn(n0, shift=UP * 0.1), run_time=self.dur(0.5))

            # «es cuatro»
            self.en("c4")
            self.play(FadeIn(e1[0], shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «Menos el peso de A»
            self.en("mha")
            self.play(FadeIn(e1[1]), FadeIn(e1[2], shift=UP * 0.1), FadeIn(e1[3]), run_time=self.dur(0.5))

            # «la varianza de A, que es cinco»
            self.en("v5")
            self.play(FadeIn(e1[4], shift=DOWN * 0.15), FadeIn(n4, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Menos el peso de B»
            self.en("mhb")
            self.play(FadeIn(e1[5]), FadeIn(e1[6], shift=UP * 0.1), FadeIn(e1[7]), run_time=self.dur(0.5))

            # «la covarianza entre A y B»
            self.en("cab")
            self.play(FadeIn(n8, shift=UP * 0.1), run_time=self.dur(0.5))

            # «¿Cuánto vale esa?»
            self.en("cuanto")
            self.pop(q)

            # «ven la misma temperatura»
            self.en("misma")
            self.play(FadeIn(ty), FadeIn(A), FadeIn(B), run_time=self.dur(0.4))
            self.play(GrowArrow(fa), GrowArrow(fb), run_time=self.dur(0.6))

            # «sus ruidos no se relacionan»
            self.en("ruidos")
            self.play(Create(ra), Create(rb), run_time=self.dur(0.8))

            # «comparten solo la varianza de la temperatura»
            self.en("comparten")
            self.resaltar(fa, fb, ty, color=AMBAR, escala=1.08, run_time=0.7)

            # «que es cuatro»
            self.en("c4b")
            self.play(ReplacementTransform(q, e1[8]), run_time=self.dur(0.5))

            # «igualado a cero»
            self.en("cero")
            self.play(FadeIn(e1[9]), FadeIn(e1[10], shift=LEFT * 0.1), run_time=self.dur(0.5))
        self.e1, self.notas, self.con_a_t = e1, VGroup(n0, n4, n8), con_a

    # ------------------------------------------------------------ b2
    def con_b(self):
        X0 = -5.0
        e1c = formula("4", "-", "5", "h_A", "-", "4", "h_B", "=", "0", escala=1.15,
                      colores={3: ESTIMACION, 6: ESTIMACION}).move_to([X0, 2.9, 0], aligned_edge=LEFT)
        lbl_a = Text("Con A", color=MEDIDA, weight=BOLD).scale(0.5).next_to(e1c, LEFT, buff=0.35)
        e2 = formula("4", "-", "4", "h_A", "-", "8", "h_B", "=", "0", escala=1.15,
                     colores={3: ESTIMACION, 6: ESTIMACION}).move_to([X0, 1.9, 0], aligned_edge=LEFT)
        lbl_b = Text("Con B", color=MEDIDA, weight=BOLD).scale(0.5).next_to(e2, LEFT, buff=0.35)
        lbl_b.align_to(lbl_a, LEFT)
        n44 = MathTex(r"\mathrm{var}(x_B)=4+4", color=INK).scale(0.75).move_to([3.4, 1.9, 0])
        llave = Brace(VGroup(e1c, e2), RIGHT, color=INK).shift(RIGHT * 0.2)
        des = formula("h_A", "=", "1-2h_B", escala=1.15, colores={0: ESTIMACION}).move_to([-2.0, 0.6, 0])
        flecha_d = Arrow(e2.get_bottom() + LEFT * 0.4, des.get_top() + UP * 0.05, buff=0.08, color=INK, stroke_width=3,
                         max_tip_length_to_length_ratio=0.25)
        sus = formula("4-5", r"(1-2h_B)", "-4h_B", "=", "0", escala=1.15, colores={1: ESTIMACION})
        sus.move_to([-2.0, -0.6, 0])
        m1 = formula("-1+6h_B", escala=1.15).move_to([-2.4, -1.75, 0])
        ig0 = MathTex("=0", color=TXT).scale(1.15).next_to(m1, RIGHT, buff=0.15)
        hb = formula("h_B", "=", r"\frac{1}{6}", escala=1.15, colores={0: ESTIMACION, 2: ESTIMACION})
        hb.move_to([-3.6, -3.05, 0])
        ha = formula("h_A", "=", r"\frac{2}{3}", escala=1.15, colores={0: ESTIMACION, 2: ESTIMACION})
        ha.move_to([-0.4, -3.05, 0])

        with self.narrar("b2"):
            # «Segunda condición, con B»
            self.en("con_b")
            self.play(FadeOut(self.notas), FadeOut(self.dib), FadeOut(self.con_a_t),
                      ReplacementTransform(self.e1, e1c), run_time=self.dur(0.7))
            self.play(FadeIn(lbl_a), FadeIn(lbl_b), run_time=self.dur(0.3))

            # «Cuatro, menos»
            self.en("b4")
            self.play(FadeIn(e2[0], shift=DOWN * 0.1), FadeIn(e2[1]), run_time=self.dur(0.4))

            # «cuatro por el peso de A»
            self.en("b4ha")
            self.play(FadeIn(e2[2]), FadeIn(e2[3], shift=UP * 0.1), run_time=self.dur(0.4))

            # «menos ocho por el peso de B»
            self.en("b8hb")
            self.play(FadeIn(e2[4]), FadeIn(e2[5]), FadeIn(e2[6], shift=UP * 0.1), run_time=self.dur(0.5))

            # «cuatro más cuatro»
            self.en("b44")
            self.play(FadeIn(n44, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Igual a cero»
            self.en("bcero")
            self.play(FadeIn(e2[7]), FadeIn(e2[8], shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «Dos ecuaciones, dos incógnitas»
            self.en("sis")
            self.play(FadeOut(n44), GrowFromCenter(llave), run_time=self.dur(0.5))
            self.resaltar(e1c[3], e1c[6], e2[3], e2[6], color=AMBAR, escala=1.2, run_time=0.6)

            # «De la segunda»
            self.en("despeje")
            marco = SurroundingRectangle(e2, color=AMBAR, buff=0.1)
            self.play(Create(marco), run_time=self.dur(0.5))

            # «el peso de A es uno menos dos veces el de B»
            self.en("despeja2")
            self.play(GrowArrow(flecha_d), FadeIn(des, shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «Lo metemos en la primera»
            self.en("mete")
            self.play(FadeOut(marco), FadeIn(sus[0]), FadeIn(sus[2:]), TransformFromCopy(des[2], sus[1]),
                      run_time=self.dur(0.9))

            # «menos uno más seis veces el peso de B»
            self.en("m1")
            self.play(FadeIn(m1, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «igual a cero»
            self.en("igual0")
            self.play(FadeIn(ig0, shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «El peso de B es un sexto»
            self.en("hb")
            self.pop(hb)

            # «y el de A, dos tercios»
            self.en("ha")
            self.pop(ha)
