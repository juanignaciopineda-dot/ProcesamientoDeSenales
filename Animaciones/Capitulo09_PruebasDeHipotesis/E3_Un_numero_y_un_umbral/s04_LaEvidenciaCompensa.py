"""Escena 04 — La evidencia contra la ventaja de partida: el test con la medición 1,3."""
from comun.escena import *
from comun.figuras_c9e3 import *

R = 1.3


class LaEvidenciaCompensa(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.comprobar()
        self.balanza()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def comprobar(self):
        C = Campanas9()
        with self.narrar("b1"):
            # «uno coma tres voltios»
            self.en("medida")
            eje = C.eje((0, 1, 2))
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            regla = C.regla(R, alto=3.3)
            rt = MathTex(r"r = 1{,}3", color=MEDIDA).scale(0.65).next_to(regla, DOWN, buff=0.45)
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.8))
            self.play(Create(regla), FadeIn(rt), run_time=self.dur(0.4))

            # «cero coma treinta y uno»
            self.en("a031")
            s1 = C.segmento(2, R, 1, C1).shift(RIGHT * 0.06)
            t1 = Text("0,31", color=C1, weight=BOLD).scale(0.5).next_to(s1, RIGHT, buff=0.12).shift(UP * 0.35)
            self.play(Create(s1), FadeIn(t1), run_time=self.dur(0.5))

            # «cero coma diecisiete»
            self.en("a017")
            s0 = C.segmento(0, R, 1, C0).shift(LEFT * 0.06)
            t0 = Text("0,17", color=C0, weight=BOLD).scale(0.5).next_to(s0, LEFT, buff=0.12).shift(DOWN * 0.3)
            self.play(Create(s0), FadeIn(t0), run_time=self.dur(0.5))

            # «uno coma ochenta y dos»
            self.en("r182")
            lam = formula(r"\Lambda(1{,}3)", "=", r"\frac{0{,}31}{0{,}17}", "=", r"1{,}82", escala=0.85,
                          colores={0: MEDIDA, 4: MEDIDA}).move_to([0, 3.15, 0])
            self.play(Write(lam), run_time=self.dur(0.9))

            # «igual de frecuentes»
            self.en("iguales")
            XI, XD = -4.3, 4.3
            ig = MathTex(r"p_0 = p_1 = 0{,}5", color=TXT).scale(0.75).move_to([XI, 2.45, 0])
            self.play(FadeIn(ig, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «eta vale uno»
            self.en("eta1")
            e1 = MathTex(r"\eta = 1", color=ESTIMACION).scale(0.8).move_to([XI, 1.8, 0])
            self.play(FadeIn(e1, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «se dice uno»
            self.en("decir1")
            cmp1 = MathTex(r"1{,}82 > 1", color=VERDE).scale(0.75)
            d1 = Text("→ Decir 1", color=VERDE, weight=BOLD).scale(0.48)
            g1 = VGroup(cmp1, d1).arrange(RIGHT, buff=0.2).move_to([XI, 1.15, 0])
            self.pop(g1)

            # «Con setenta y treinta»
            self.en("p73")
            p73 = MathTex(r"p_0 = 0{,}7", r"\quad", r"p_1 = 0{,}3", color=TXT).scale(0.75).move_to([XD, 2.45, 0])
            p73[0].set_color(C0)
            p73[2].set_color(C1)
            self.play(FadeIn(p73, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «eta vale dos coma treinta y tres»
            self.en("eta233")
            e2 = MathTex(r"\eta = \frac{0{,}7}{0{,}3} = 2{,}33", color=ESTIMACION).scale(0.7).move_to([XD, 1.75, 0])
            self.play(FadeIn(e2, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «no llega»
            self.en("nollega")
            cmp2 = MathTex(r"1{,}82 < 2{,}33", color=ERROR).scale(0.75).move_to([XD - 0.6, 1.13, 0])
            self.pop(cmp2, sonido="error")

            # «y se dice cero»
            self.en("decir0")
            d0 = Text("→ Decir 0", color=ESTIMACION, weight=BOLD).scale(0.48).next_to(cmp2, RIGHT, buff=0.2)
            self.pop(d0)

            # «las curvas escaladas»
            self.en("escaladas")
            c0b, c1b = C.campana(0, 1.4, C0), C.campana(2, 0.6, C1)
            cruce = Dot(C.p(CRUCE9, C.f(0, CRUCE9, 1.4)), radius=0.1, color=ESTIMACION)
            tc = MathTex(r"1{,}42", color=ESTIMACION).scale(0.6).move_to(C.p(CRUCE9) + DOWN * 0.75 + RIGHT * 0.75)
            r0 = C.region(-3, CRUCE9, C0)
            r1 = C.region(CRUCE9, 5, C1)
            self.play(FadeOut(VGroup(s0, s1, t0, t1, ig, e1, g1, p73, e2, cmp2, d0)), Transform(c0, c0b), Transform(c1, c1b),
                      run_time=self.dur(0.8))
            self.play(FadeIn(cruce, scale=0.5), FadeIn(tc), FadeIn(r0), FadeIn(r1), run_time=self.dur(0.5))

    # ------------------------------------------------------------------ b2
    def balanza(self):
        with self.narrar("b2"):
            # «se lee muy bien»
            self.en("lee")
            self.limpiar(run_time=0.3)
            B = Balanza(centro=(0, 0.6), semi=2.6)
            self.play(FadeIn(B), run_time=self.dur(0.5))

            # «dos coma tres veces más frecuentes»
            self.en("frec")
            pesa_d = MathTex(r"\eta = 2{,}33", color=ESTIMACION).scale(0.85)
            pesa_d.next_to(B.der[1], DOWN, buff=0.15)
            self.play(FadeIn(pesa_d, shift=DOWN * 0.3), run_time=self.dur(0.4))
            B.der.add(pesa_d)
            self.play(*B.inclinar("der"), run_time=self.dur(0.6))

            # «para decir uno»
            self.en("paradecir")
            d1 = Text("Decir 1", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([0, 3.15, 0])
            self.pop(d1)

            # «al menos dos coma tres veces más compatible»
            self.en("compat")
            pesa_i = MathTex(r"\Lambda(r) \geq 2{,}33", color=MEDIDA).scale(0.85)
            pesa_i.next_to(B.izq[1], DOWN, buff=0.15)
            self.play(FadeIn(pesa_i, shift=DOWN * 0.3), run_time=self.dur(0.4))
            B.izq.add(pesa_i)

            # «con el uno»
            self.en("conuno")
            self.play(*B.inclinar("izq"), run_time=self.dur(0.8))

            # «La evidencia»
            self.en("evidencia")
            ev = Text("Evidencia", color=MEDIDA, weight=BOLD).scale(0.5).next_to(pesa_i, DOWN, buff=0.2)
            self.play(FadeIn(ev, shift=UP * 0.15), run_time=self.dur(0.4))
            B.izq.add(ev)

            # «la ventaja de partida»
            self.en("ventaja")
            ve = Text("Ventaja de partida", color=ESTIMACION, weight=BOLD).scale(0.5)
            ve.next_to(pesa_d, DOWN, buff=0.2)
            self.play(FadeIn(ve, shift=UP * 0.15), run_time=self.dur(0.4))
            B.der.add(ve)
            self.play(*B.inclinar("izq", 0.08), run_time=self.dur(0.35))
            self.play(*B.inclinar("der", 0.08), run_time=self.dur(0.35))

            # «el test de razón de verosimilitud»
            self.en("lrt")
            caja_ = caja_lrt9(escala=1.2).move_to([0, -2.3, 0])
            rot = Text("Test de razón de verosimilitud (LRT)", color=TXT, weight=BOLD).scale(0.5)
            rot.next_to(caja_, UP, buff=0.3)
            self.play(VGroup(B, d1).animate.scale(0.8).move_to([0, 1.55, 0]), run_time=self.dur(0.6))
            self.play(Write(caja_.f), FadeIn(rot), run_time=self.dur(0.7))

            # «en todo lo que queda de capítulo»
            self.en("resto")
            self.play(Create(caja_.marco), run_time=self.dur(0.6))
            self.sfx("exito")
