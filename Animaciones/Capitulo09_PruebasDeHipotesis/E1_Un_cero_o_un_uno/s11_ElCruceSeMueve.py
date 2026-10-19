"""Escena 11 — Regiones de decisión: la misma medición cambia de decisión y el cruce se va a 1,42."""
from comun.escena import *
from comun.figuras_c9e1 import *

R = 1.3


class ElCruceSeMueve(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        C = Campanas9()
        self.C = C
        eje = C.eje((0, 1, 2))
        c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
        k0 = MathTex(r"\times\, 0{,}7", color=C0).scale(0.8).move_to(C.p(0, 0.7 * 0.4) + UP * 0.5)
        k1 = MathTex(r"\times\, 0{,}3", color=C1).scale(0.8).move_to(C.p(2, 0.3 * 0.4) + UP * 0.5)
        self.k = VGroup(k0, k1)
        self.add(eje, c0, c1, k0, k1)
        self.cuenta()
        self.cruce()
        self.regla_map()
        self.wait(1.0)
        self.limpiar()

    def cuenta(self):
        C = self.C
        with self.narrar("b1"):
            # «en uno coma tres»
            self.en("medida")
            regla = C.regla(R, alto=3.0)
            rt = MathTex(r"r = 1{,}3", color=MEDIDA).scale(0.7).next_to(regla, UP, buff=0.1)
            self.regla = regla
            self.play(Create(regla), FadeIn(rt, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «Cero coma siete por»
            self.en("m0")
            d0 = C.punto(0, R, P0, C0)
            f0 = formula(r"0{,}7 \cdot 0{,}17", r"= 0{,}12", colores={0: C0, 1: C0}).scale(0.8).move_to([-4.0, 2.5, 0])
            self.play(FadeIn(d0, scale=0.5), FadeIn(f0[0]), run_time=self.dur(0.4))

            # «cero coma doce»
            self.en("c12")
            self.play(FadeIn(f0[1], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «Cero coma tres por»
            self.en("m1")
            d1 = C.punto(2, R, P1, C1)
            f1 = formula(r"0{,}3 \cdot 0{,}31", r"= 0{,}094", colores={0: C1, 1: C1}).scale(0.8).move_to([3.9, 2.5, 0])
            self.play(FadeIn(d1, scale=0.5), FadeIn(f1[0]), run_time=self.dur(0.4))

            # «cero coma cero»
            self.en("c094")
            self.play(FadeIn(f1[1], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «Gana el cero»
            self.en("gana0")
            dec = Text("Decir 0", color=ESTIMACION, weight=BOLD).scale(0.55).move_to([2.4, 1.0, 0])
            self.play(d0.animate.scale(1.7), run_time=self.dur(0.3))
            self.pop(dec)

            # «Con la misma medición»
            self.en("misma")
            self.resaltar(regla, color=MEDIDA, escala=1.0)

            # «nos»
            self.en("antes")
            antes = Text("Antes: 1", color=INK).scale(0.55)
            ahora = Text("Ahora: 0", color=ESTIMACION, weight=BOLD).scale(0.55)
            card = VGroup(antes, Text("·", color=INK).scale(0.55), ahora).arrange(RIGHT, buff=0.25)
            card.move_to([0, 3.4, 0])
            self.play(FadeIn(card, shift=DOWN * 0.2), run_time=self.dur(0.5))
            self.cuentas = VGroup(f0, f1, d0, d1, dec, rt)

    def cruce(self):
        C = self.C
        with self.narrar("b2"):
            # «El cruce de las curvas»
            self.en("cruce")
            p1 = Dot(C.p(1), radius=0.11, color=ESTIMACION).set_opacity(0.45)
            self.play(FadeOut(self.cuentas), FadeOut(self.regla), FadeIn(p1), run_time=self.dur(0.4))

            # «uno coma cuarenta y dos»
            self.en("mueve")
            p142 = Dot(C.p(1), radius=0.11, color=ESTIMACION)
            self.add(p142)
            self.play(p142.animate.move_to(C.p(CRUCE9)), run_time=self.dur(0.8))
            vl = DashedLine(C.p(CRUCE9), C.p(CRUCE9, C.f(0, CRUCE9, P0)), color=ESTIMACION, stroke_width=3)
            cr = Dot(C.p(CRUCE9, C.f(0, CRUCE9, P0)), radius=0.1, color=ESTIMACION)
            t142 = Text("1,42", color=ESTIMACION, weight=BOLD).scale(0.55).move_to(cr.get_center() + UP * 0.6 + LEFT * 0.2)
            self.play(Create(vl), FadeIn(cr), FadeIn(t142), run_time=self.dur(0.5))
            self.marca = VGroup(p1, p142, vl, cr, t142)

            # «más raros»
            self.en("raros")
            self.play(*[k.animate(rate_func=there_and_back).scale(1.3) for k in self.k], run_time=self.dur(0.6))

            # «más voltios»
            self.en("voltios")
            y = C.p(0)[1] - 0.95
            fl = Arrow([C.p(1)[0], y, 0], [C.p(CRUCE9)[0], y, 0], color=ESTIMACION, buff=0, stroke_width=5,
                       max_tip_length_to_length_ratio=0.45)
            self.play(GrowArrow(fl), run_time=self.dur(0.4))
            self.fl = fl

            # «antes de creernos un uno»
            self.en("creer")
            d1 = Text("Decir 1", color=C1, weight=BOLD).scale(0.55).move_to(C.p(1) + UP * 2.6)
            self.play(FadeIn(d1), run_time=self.dur(0.3))
            self.play(d1.animate.move_to(C.p(CRUCE9) + UP * 2.6 + RIGHT * 1.3), run_time=self.dur(0.9))

            # «dos regiones de decisión»
            self.en("regiones")
            u = Line(C.p(CRUCE9) + DOWN * 0.15, C.p(CRUCE9) + UP * 2.2, color=ESTIMACION, stroke_width=4)
            self.play(Create(u), FadeOut(d1), run_time=self.dur(0.5))
            self.u = u

            # «se dice uno»
            self.en("d1")
            r1 = C.region(CRUCE9, 5, C1)
            t1 = rot_tex9("D_1", "· Decir 1", C1, 0.48).move_to([C.p(3.4)[0], -3.55, 0])
            self.play(FadeIn(r1), FadeIn(t1), run_time=self.dur(0.4))

            # «a la izquierda, cero»
            self.en("d0")
            r0 = C.region(-3, CRUCE9, C0)
            t0 = rot_tex9("D_0", "· Decir 0", C0, 0.48).move_to([C.p(-1.4)[0], -3.55, 0])
            self.play(FadeIn(r0), FadeIn(t0), run_time=self.dur(0.4))

    def regla_map(self):
        with self.narrar("b3"):
            # «la regla del máximo a posteriori»
            self.en("titulo")
            todo = Group(*[m for m in self.mobjects if m is not self.camera.frame])
            self.play(todo.animate.scale(0.5).move_to([0, 2.0, 0]), run_time=self.dur(0.7))
            mp = Text("MAP", color=ESTIMACION, weight=BOLD).scale(0.8).move_to([0, -0.35, 0])
            self.pop(mp)

            # «para una medición continua»
            self.en("continua")
            cont = rot_tex9("r", "continua", MEDIDA, 0.5).next_to(mp, RIGHT, buff=0.5)
            self.play(FadeIn(cont), run_time=self.dur(0.4))

            R_ = formula(r"p_1", r"\cdot f(r \mid H_1)", r"\gtrless", r"p_0", r"\cdot f(r \mid H_0)",
                         colores={0: C1, 1: C1, 2: ESTIMACION, 3: C0, 4: C0}).scale(1.05).move_to([0, -1.55, 0])

            # «Pe uno»
            self.en("p1")
            self.play(FadeIn(R_[0]), run_time=self.dur(0.3))

            # «la densidad de erre bajo hache uno»
            self.en("f1")
            self.play(FadeIn(R_[1], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «comparada con»
            self.en("comp")
            self.play(FadeIn(R_[2], scale=0.6), run_time=self.dur(0.3))

            # «pe cero»
            self.en("p0")
            self.play(FadeIn(R_[3]), run_time=self.dur(0.3))

            # «bajo hache cero»
            self.en("f0")
            self.play(FadeIn(R_[4], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «Si gana la primera»
            self.en("gana1")
            g1 = VGroup(MathTex(">", color=ESTIMACION).scale(0.9),
                        Text("Decir 1", color=C1, weight=BOLD).scale(0.55)).arrange(RIGHT, buff=0.3)
            g1.move_to([-3.0, -3.0, 0])
            a1 = Arrow(R_[2].get_bottom(), g1.get_top(), color=INK, buff=0.15, stroke_width=3)
            self.play(GrowArrow(a1), FadeIn(g1), run_time=self.dur(0.5))

            # «Si gana la segunda»
            self.en("gana0")
            g0 = VGroup(MathTex("<", color=ESTIMACION).scale(0.9),
                        Text("Decir 0", color=C0, weight=BOLD).scale(0.55)).arrange(RIGHT, buff=0.3)
            g0.move_to([3.0, -3.0, 0])
            a0 = Arrow(R_[2].get_bottom(), g0.get_top(), color=INK, buff=0.15, stroke_width=3)
            self.play(GrowArrow(a0), FadeIn(g0), run_time=self.dur(0.5))
