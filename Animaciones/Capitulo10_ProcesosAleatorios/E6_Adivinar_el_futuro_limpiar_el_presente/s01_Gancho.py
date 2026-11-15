"""Escena 01 — Gancho: el sensor marca 23; a un paso, 21,8; a diez pasos, 20."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        P = PanelSensor(centro=(-0.3, -0.4), ancho=9.6, alto=3.6, n=36, n0=22)
        n0 = P.n0
        d23 = P.punto(n0, 3.0, TXT, 0.11)
        r23 = Text("23 °C", color=TXT).scale(0.5).next_to(d23, UR, buff=0.12)
        h1 = Circle(radius=0.1, color=INK, stroke_width=3).move_to(P.p(n0 + 1, 2.2))
        q1 = Text("?", color=INK, weight=BOLD).scale(0.6).next_to(h1, RIGHT, buff=0.15)
        a1 = P.punto(n0 + 1, 1.8, AMBAR)
        r1 = Text("21,8", color=AMBAR, weight=BOLD).scale(0.5).next_to(a1, RIGHT, buff=0.15)
        h2 = Circle(radius=0.1, color=INK, stroke_width=3).move_to(P.p(n0 + 10, 1.4))
        q2 = Text("?", color=INK, weight=BOLD).scale(0.6).next_to(h2, RIGHT, buff=0.15)
        a2 = P.punto(n0 + 10, 0.0, AMBAR)
        r2 = Text("20", color=AMBAR, weight=BOLD).scale(0.5).next_to(a2, UP, buff=0.15)
        ms = np.arange(0, 11)
        pred = 3.0 * 0.6 ** ms
        curva = P.L.curva(n0 + ms, pred, AMBAR, 4)
        err = 2.0 * np.sqrt(1 - 0.36 ** ms)
        bd = banda(P.L, n0 + ms, pred, err, AMBAR, 0.2)
        hor = DashedLine(P.p(n0 + 8, -4.6), P.p(n0 + 8, 4.6), color=INK, stroke_width=2.5)
        rh = Text("horizonte", color=INK).scale(0.45).next_to(hor, UP, buff=0.1)

        with self.narrar("b1"):
            # «veintitrés grados»
            self.en("v23")
            self.play(Create(P.media), FadeIn(P.rotulo_media), Create(P.pasado), run_time=self.dur(1.0))
            self.play(FadeIn(d23), FadeIn(r23), run_time=0.3)

            # «Un paso después»
            self.en("uno")
            self.play(FadeIn(h1), FadeIn(q1), run_time=0.4)

            # «veintiuno coma ocho»
            self.en("p218")
            self.play(ReplacementTransform(h1, a1), ReplacementTransform(q1, r1), run_time=0.5)

            # «Diez pasos después»
            self.en("diez")
            self.play(FadeIn(h2), FadeIn(q2), run_time=0.4)

            # «veinte»
            self.en("v20")
            self.play(ReplacementTransform(h2, a2), ReplacementTransform(q2, r2), run_time=0.5)

            # «ya no sabe nada»
            self.en("nada")
            self.play(FadeOut(r1), FadeOut(r2), Create(curva), run_time=self.dur(1.2))

            # «Así de corto»
            self.en("corto")
            self.play(FadeOut(r23), FadeIn(bd), Create(hor), FadeIn(rh), run_time=self.dur(0.8))
        self.wait(0.8)
        self.limpiar()
