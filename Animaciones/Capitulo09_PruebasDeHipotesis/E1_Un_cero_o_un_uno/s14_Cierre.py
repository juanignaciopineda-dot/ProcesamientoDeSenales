"""Escena 14 — Cierre: resumen y anuncio de «Dos maneras de equivocarse»."""
from comun.escena import *
from comun.figuras_c9e1 import *


class Cierre(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        C = Campanas9(centro=(0.0, -2.6), alto=8.0, v_max=0.3)
        with self.narrar("b1"):
            # «Decidir es quedarse»
            self.en("decidir")
            eje = C.eje((0, 1, 2))
            c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
            r0, r1 = C.region(-3, CRUCE9, C0), C.region(CRUCE9, 5, C1)
            t0 = rot_tex9("D_0", "· Decir 0", C0, 0.48).move_to([C.p(-1.4)[0], -3.4, 0])
            t1 = rot_tex9("D_1", "· Decir 1", C1, 0.48).move_to([C.p(3.4)[0], -3.4, 0])
            self.play(FadeIn(eje), Create(c0), Create(c1), FadeIn(r0), FadeIn(r1), FadeIn(t0), FadeIn(t1),
                      run_time=self.dur(0.9))

            # «la altura»
            self.en("altura")
            self.play(c0.animate(rate_func=there_and_back).set_stroke(width=8),
                      c1.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.6))

            # «lo que sabías antes»
            self.en("antes")
            k0 = MathTex(r"\times\, 0{,}7", color=C0).scale(0.8).move_to(C.p(-1.6, 0.2))
            k1 = MathTex(r"\times\, 0{,}3", color=C1).scale(0.8).move_to(C.p(3.4, 0.2))
            self.pop(k0, k1)

            # «Ya tenemos la regla»
            self.en("regla")
            R = formula(r"p_1", r"\cdot f(r \mid H_1)", r"\gtrless", r"p_0", r"\cdot f(r \mid H_0)",
                        colores={0: C1, 1: C1, 2: ESTIMACION, 3: C0, 4: C0}).scale(0.95).move_to([0, 3.3, 0])
            self.play(FadeIn(R, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «es la mejor»
            self.en("mejor")
            mp = VGroup(Text("MAP", color=ESTIMACION, weight=BOLD).scale(0.6), tilde(VERDE, 0.5))
            mp.arrange(RIGHT, buff=0.25).move_to([0, 2.45, 0])
            self.pop(mp)

            # «cuánto se equivoca»
            self.en("cuanto")
            a0 = C.area(0, P0, CRUCE9, C.r1, ERROR, 0.6)
            a1 = C.area(2, P1, C.r0, CRUCE9, ERROR, 0.6)
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(0.8).move_to(C.p(CRUCE9, 0.13) + UP * 0.55)
            self.play(FadeIn(a0), FadeIn(a1), run_time=self.dur(0.5))
            self.pop(q)

            # «ni de qué»
            self.en("manera")
            self.play(a1.animate.set_fill("#ff9f43", 0.65), run_time=self.dur(0.5))

            # «más de una forma de fallar»
            self.en("formas")
            ne = MathTex(r"\neq", color=ESTIMACION).scale(1.1).move_to(q)
            self.play(ReplacementTransform(q, ne), run_time=self.dur(0.5))

            # «En el próximo episodio»
            self.en("proximo")
            todo = Group(*[m for m in self.mobjects if m is not self.camera.frame])
            self.play(todo.animate.fade(0.8), run_time=self.dur(0.6))

            # «Dos maneras de equivocarse»
            self.en("siguiente")
            sig = VGroup(self.palabra("Dos maneras", TXT, 1.3), self.palabra("de equivocarse", AMBAR, 1.3))
            sig.arrange(DOWN, buff=0.3).move_to([0, 0.3, 0])
            self.play(FadeOut(todo), run_time=self.dur(0.3))
            self.pop(*sig)
        self.wait(1.2)
        self.limpiar()
