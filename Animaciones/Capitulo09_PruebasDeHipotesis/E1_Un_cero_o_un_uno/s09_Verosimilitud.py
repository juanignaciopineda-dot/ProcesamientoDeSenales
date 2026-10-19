"""Escena 09 — La altura de cada campana: verosimilitud y umbral a mitad de camino."""
from comun.escena import *
from comun.figuras_c9e1 import *

R = 1.3


class Verosimilitud(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        C = Campanas9()
        self.C = C
        self.eje = C.eje((0, 1, 2))
        self.c0, self.c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        self.l0 = Text("Si se envió 0", color=C0).scale(0.5).move_to(C.p(-1.7, 0.43))
        self.l1 = Text("Si se envió 1", color=C1).scale(0.5).move_to(C.p(3.7, 0.43))
        self.add(self.eje, self.c0, self.c1, self.l0, self.l1)
        self.alturas()
        self.compatible()
        self.mitad()
        self.wait(1.0)
        self.limpiar()

    def alturas(self):
        C = self.C
        with self.narrar("b1"):
            # «uno coma tres voltios»
            self.en("medida")
            regla = C.regla(R)
            rt = MathTex(r"r = 1{,}3", color=MEDIDA).scale(0.7).next_to(regla, UP, buff=0.1)
            self.regla, self.rt = regla, rt
            self.play(Create(regla), FadeIn(rt, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «¿Cero o uno?»
            self.en("pregunta")
            preg = Text("¿0 o 1?", color=ESTIMACION, weight=BOLD).scale(0.75).move_to([0, 3.3, 0])
            self.preg = preg
            self.pop(preg)

            # «contar casos como en la»
            self.en("tabla")
            T = TablaCanal(centro=(-5.3, 2.75), lado=0.55, esc=0.26)
            mini = VGroup(*[c for fila in T.cel for c in fila], T.probs())
            self.play(FadeIn(mini), run_time=self.dur(0.4))
            tacha = tachar(mini)
            self.play(Create(tacha), run_time=self.dur(0.3))
            self.mini = VGroup(mini, tacha)

            # «cualquier número»
            self.en("eje")
            d = Dot(C.p(-3), radius=0.1, color=MEDIDA)
            self.play(FadeIn(d), FadeOut(self.mini), run_time=self.dur(0.2))
            self.play(d.animate.move_to(C.p(5)), run_time=self.dur(1.6), rate_func=there_and_back)
            self.play(FadeOut(d), run_time=self.dur(0.2))

            # «altura de cada campana»
            self.en("alturas")
            p0, p1 = C.punto(0, R, 1, C0), C.punto(2, R, 1, C1)
            self.pts = VGroup(p0, p1)
            self.play(FadeIn(p0, scale=0.5), FadeIn(p1, scale=0.5), run_time=self.dur(0.4))

            # «su densidad»
            self.en("dens")
            dens = Text("Densidad = altura", color=TXT).scale(0.5).move_to([4.6, 2.3, 0])
            self.dens = dens
            self.play(FadeIn(dens), run_time=self.dur(0.4))

            # «cero coma diecisiete»
            self.en("a17")
            s0 = C.segmento(0, R, 1, C0).shift(LEFT * 0.07)
            t0 = Text("0,17", color=C0, weight=BOLD).scale(0.5).next_to(s0, LEFT, buff=0.15).shift(DOWN * 0.25)
            self.play(Create(s0), FadeIn(t0), run_time=self.dur(0.5))

            # «cero coma treinta y uno»
            self.en("a31")
            s1 = C.segmento(2, R, 1, C1).shift(RIGHT * 0.07)
            t1 = Text("0,31", color=C1, weight=BOLD).scale(0.5).next_to(s1, RIGHT, buff=0.15)
            self.play(Create(s1), FadeIn(t1), run_time=self.dur(0.5))
            self.segs = VGroup(s0, s1, t0, t1)

    def compatible(self):
        C = self.C
        with self.narrar("b2"):
            # «se llama verosimilitud»
            self.en("vero")
            vero = Text("Verosimilitud", color=ESTIMACION, weight=BOLD).scale(0.75).move_to(self.preg)
            self.play(FadeOut(self.preg), FadeOut(self.dens), run_time=self.dur(0.2))
            self.pop(vero)
            self.vero = vero

            # «lo compatible»
            self.en("fx")
            f0 = MathTex(r"f(r \mid H_0) = 0{,}17", color=C0).scale(0.75).move_to([-4.2, 2.3, 0])
            f1 = MathTex(r"f(r \mid H_1) = 0{,}31", color=C1).scale(0.75).move_to([4.2, 2.3, 0])
            self.play(FadeIn(f0, shift=DOWN * 0.2), FadeIn(f1, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «con cada hipótesis»
            self.en("cada")
            g0 = Line(f0.get_bottom() + DOWN * 0.1, C.p(-0.9, C.f(0, -0.9)), color=C0, stroke_width=2.5)
            g1 = Line(f1.get_bottom() + DOWN * 0.1, C.p(2.9, C.f(2, 2.9)), color=C1, stroke_width=2.5)
            self.play(Create(g0), Create(g1), run_time=self.dur(0.5))

            # «lejos del centro»
            self.en("lejos")
            y = C.p(0)[1] - 0.85
            a0 = DoubleArrow([C.p(0)[0], y, 0], [C.p(R)[0], y, 0], color=C0, buff=0, stroke_width=4,
                             tip_length=0.16, max_tip_length_to_length_ratio=0.3)
            d0 = Text("1,3", color=C0).scale(0.45).next_to(a0, DOWN, buff=0.12)
            self.play(GrowFromCenter(a0), FadeIn(d0), run_time=self.dur(0.5))

            # «cerca del centro de la otra»
            self.en("cerca")
            a1 = DoubleArrow([C.p(R)[0], y, 0], [C.p(2)[0], y, 0], color=C1, buff=0, stroke_width=4,
                             tip_length=0.16, max_tip_length_to_length_ratio=0.3)
            d1 = Text("0,7", color=C1).scale(0.45).next_to(a1, DOWN, buff=0.12)
            self.play(GrowFromCenter(a1), FadeIn(d1), run_time=self.dur(0.5))

            # «casi el doble»
            self.en("doble")
            dob = MathTex(r"\frac{0{,}31}{0{,}17} \approx 1{,}8", color=ESTIMACION).scale(0.8).move_to([0, 2.15, 0])
            self.pop(dob)
            self.extra = VGroup(f0, f1, g0, g1, a0, d0, a1, d1, dob)

    def mitad(self):
        C = self.C
        with self.narrar("b3"):
            # «igual de frecuentes»
            self.en("iguales")
            ig = MathTex(r"p_0 = p_1", color=TXT).scale(0.85).move_to([0, 2.3, 0])
            self.play(FadeOut(self.extra), FadeOut(self.segs), run_time=self.dur(0.3))
            self.play(FadeIn(ig), run_time=self.dur(0.4))

            # «gana la campana más alta»
            self.en("gana")
            d1 = Text("Decir 1", color=ESTIMACION, weight=BOLD).scale(0.55).move_to([2.3, 1.55, 0])
            self.play(self.pts[1].animate.scale(1.6), run_time=self.dur(0.3))
            self.pop(d1)

            # «se cruzan justo en uno»
            self.en("cruce")
            cr = Dot(C.p(1, C.f(0, 1)), radius=0.11, color=ESTIMACION)
            uno = MathTex("1", color=ESTIMACION).scale(0.7).next_to(cr, UP, buff=0.15).shift(LEFT * 0.25)
            self.play(FadeIn(cr, scale=0.5), FadeIn(uno), run_time=self.dur(0.4))

            # «a mitad de camino»
            self.en("mitad")
            b0 = Brace(Line(C.p(0), C.p(1)), DOWN, buff=0.5, color=INK)
            b1 = Brace(Line(C.p(1), C.p(2)), DOWN, buff=0.5, color=INK)
            self.play(GrowFromCenter(b0), GrowFromCenter(b1), run_time=self.dur(0.5))

            # «dirías uno»
            self.en("der")
            r1 = C.region(1, 5, C1)
            t1 = Text("Decir 1", color=C1, weight=BOLD).scale(0.5).move_to([C.p(3.3)[0], -3.55, 0])
            self.play(FadeIn(r1), FadeOut(d1), FadeIn(t1), run_time=self.dur(0.5))

            # «por debajo, cero»
            self.en("izq")
            r0 = C.region(-3, 1, C0)
            t0 = Text("Decir 0", color=C0, weight=BOLD).scale(0.5).move_to([C.p(-1.6)[0], -3.55, 0])
            self.play(FadeIn(r0), FadeIn(t0), run_time=self.dur(0.5))

            # «no son igual de frecuentes»
            self.en("noiguales")
            tacha = tachar(ig)
            self.play(Create(tacha), run_time=self.dur(0.4))

            # «hay más»
            self.en("mas")
            nuevo = MathTex(r"p_0 = 0{,}7", r"\quad", r"p_1 = 0{,}3", color=TXT).scale(0.85).move_to([0, 2.3, 0])
            nuevo[0].set_color(C0)
            nuevo[2].set_color(C1)
            self.play(FadeOut(ig), FadeOut(tacha), FadeIn(nuevo), run_time=self.dur(0.5))

            # «¿Cómo se mezcla eso»
            self.en("mezcla")
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(0.9).next_to(nuevo, RIGHT, buff=0.45)
            self.pop(q)
