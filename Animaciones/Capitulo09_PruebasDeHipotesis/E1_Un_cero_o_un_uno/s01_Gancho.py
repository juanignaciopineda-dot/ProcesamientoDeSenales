"""Escena 01 — Gancho: la misma medición, dos decisiones."""
from comun.escena import *
from comun.figuras_c9e1 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        C = Campanas9()
        R = 1.3
        eje = C.eje((0, 1, 2))
        c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        regla = C.regla(R)
        r_txt = MathTex(r"r = 1{,}3", color=MEDIDA).scale(0.7).next_to(regla, UP, buff=0.1)

        with self.narrar("b1"):
            # «Mides uno coma tres voltios»
            self.en("medida")
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(1.0))
            self.play(Create(regla), FadeIn(r_txt, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «Si ceros y unos»
            self.en("apriori")
            ceros = Text("Ceros", color=C0, weight=BOLD).scale(0.55).move_to([-3.4, 3.35, 0])
            unos = Text("Unos", color=C1, weight=BOLD).scale(0.55).move_to([3.4, 3.35, 0])
            v0 = Text("?", color=INK).scale(0.6).next_to(ceros, DOWN, buff=0.2)
            v1 = Text("?", color=INK).scale(0.6).next_to(unos, DOWN, buff=0.2)
            self.play(FadeIn(ceros), FadeIn(unos), FadeIn(v0), FadeIn(v1), run_time=self.dur(0.5))

            # «igual de a menudo»
            self.en("iguales")
            v0n = Text("0,5", color=C0).scale(0.6).move_to(v0)
            v1n = Text("0,5", color=C1).scale(0.6).move_to(v1)
            self.play(ReplacementTransform(v0, v0n), ReplacementTransform(v1, v1n), run_time=self.dur(0.4))

            # «dices uno»
            self.en("uno")
            s0 = C.segmento(0, R, 1, C0).shift(LEFT * 0.06)
            s1 = C.segmento(2, R, 1, C1).shift(RIGHT * 0.06)
            d0, d1 = C.punto(0, R, 1, C0), C.punto(2, R, 1, C1)
            decir1 = Text("Decir 1", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([3.6, 1.55, 0])
            self.play(Create(s0), Create(s1), FadeIn(d0), FadeIn(d1), run_time=self.dur(0.4))
            self.play(d1.animate.scale(1.6), run_time=self.dur(0.3))
            self.pop(decir1)

            # «Si hay más ceros»
            self.en("masceros")
            v0b = Text("0,7", color=C0).scale(0.6).move_to(v0n)
            v1b = Text("0,3", color=C1).scale(0.6).move_to(v1n)
            # campanas escaladas por 2·p (la suma de alturas no cambia y se ven grandes)
            c0b, c1b = C.campana(0, 1.4, C0), C.campana(2, 0.6, C1)
            s0b = C.segmento(0, R, 1.4, C0).shift(LEFT * 0.06)
            s1b = C.segmento(2, R, 0.6, C1).shift(RIGHT * 0.06)
            d0b, d1b = C.punto(0, R, 1.4, C0).scale(1.6), C.punto(2, R, 0.6, C1)
            self.play(ReplacementTransform(v0n, v0b), ReplacementTransform(v1n, v1b),
                      Transform(c0, c0b), Transform(c1, c1b), Transform(s0, s0b), Transform(s1, s1b),
                      Transform(d0, d0b), Transform(d1, d1b), run_time=self.dur(1.0))

            # «con la misma medición»
            self.en("misma")
            self.resaltar(regla, color=MEDIDA, escala=1.0)

            # «dices cero»
            self.en("cero")
            tacha = tachar(decir1)
            decir0 = Text("Decir 0", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(decir1)
            self.play(Create(tacha), run_time=self.dur(0.3))
            self.play(FadeOut(decir1), FadeOut(tacha), run_time=self.dur(0.25))
            self.pop(decir0)

            # «Hoy veremos por qué»
            self.en("porque")
            todo = Group(*[m for m in self.mobjects if m is not self.camera.frame])
            preg = Text("?", color=ESTIMACION, weight=BOLD).scale(2.6).move_to([0, 0.45, 0])
            self.play(todo.animate.fade(0.75), run_time=self.dur(0.4))
            self.pop(preg)

            # «ninguna regla lo hace mejor»
            self.en("mejor")
            frase = Text("Ninguna regla falla menos", color=TXT, weight=BOLD).scale(0.7).move_to([-0.4, 0.45, 0])
            ok = tilde(VERDE, 0.7).next_to(frase, RIGHT, buff=0.3)
            self.play(ReplacementTransform(preg, frase), run_time=self.dur(0.5))
            self.play(Create(ok), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)
        self.wait(0.6)
        self.limpiar()
