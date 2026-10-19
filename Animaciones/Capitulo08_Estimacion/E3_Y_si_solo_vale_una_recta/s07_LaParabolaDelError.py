"""Escena 07 — La parábola del error: J(h) = 4 − 8h + 5h², mínimo en h = 0,8 y apuesta 22,4."""
from comun.escena import *


class LaParabolaDelError(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        P = ParabolaJ(centro=(-1.6, -0.5), ancho=7.5, alto=4.0)
        form = formula("J(h)", "=", "4", "-8h", "+5h^2", escala=1.4, colores={0: ERROR}).move_to([0, 3.3, 0])
        n_h = MathTex("h", color=INK).scale(0.7).move_to(P.p(1.8, 0) + RIGHT * 0.3 + UP * 0.25)
        h = ValueTracker(-0.2)
        mov = Dot(radius=0.11, color=TXT)
        mov.add_updater(lambda m: m.move_to(P.p(h.get_value())))
        d0, d1 = P.punto(0, AMBAR), P.punto(1, AMBAR)
        l4 = MathTex("4", color=AMBAR).scale(0.8).move_to(P.p(0) + RIGHT * 0.5 + UP * 0.1)
        l1 = MathTex("1", color=AMBAR).scale(0.8).move_to(P.p(1) + UP * 0.5 + LEFT * 0.3)
        vert = P.p(0.8)
        guia_v = DashedLine(vert, P.p(0.8, 0), color=INK, stroke_width=2)
        h08 = MathTex("h=0{,}8", color=AMBAR).scale(0.85).move_to(P.p(0.8, 0) + DOWN * 0.5)
        guia_h = DashedLine(vert, [3.2, vert[1], 0], color=INK, stroke_width=2)
        j08 = MathTex(r"J=0{,}8", color=ERROR).scale(0.95).move_to([4.6, vert[1], 0])
        n23 = Text("23", color=MEDIDA, weight=BOLD).scale(1.0).move_to([4.6, 2.2, 0])
        tach = tachar(n23)
        cuenta = MathTex(r"\hat{y}=20+0{,}8\cdot 3", color=TXT).scale(0.85).move_to([4.6, 0.9, 0])
        r224 = MathTex(r"=22{,}4", color=ESTIMACION).scale(1.5).move_to([4.6, -0.4, 0])

        with self.narrar("b1"):
            # «El error queda cuatro»
            self.en("j1")
            self.play(*[FadeIn(form[i]) for i in range(3)], run_time=self.dur(0.6))

            # «menos ocho hache»
            self.en("j2")
            self.play(FadeIn(form[3], shift=UP * 0.1), run_time=self.dur(0.4))

            # «más cinco hache al cuadrado»
            self.en("j3")
            self.play(FadeIn(form[4], shift=UP * 0.1), run_time=self.dur(0.4))

            # «otra parábola»
            self.en("parabola")
            self.play(Create(P.eje), FadeIn(n_h), run_time=self.dur(0.4))
            self.add(mov)
            self.play(Create(P.curva), h.animate.set_value(1.8), run_time=self.dur(1.5), rate_func=linear)

            # «Con hache igual a cero da cuatro»
            self.en("p0")
            self.pop(d0)
            self.play(FadeIn(l4), run_time=self.dur(0.4))

            # «con hache igual a uno, uno»
            self.en("p1")
            self.pop(d1)
            self.play(FadeIn(l1), run_time=self.dur(0.4))

            # «su punto más bajo»
            self.en("bajo")
            self.play(h.animate.set_value(0.8), run_time=self.dur(1.6))
            mov.clear_updaters()
            self.play(FadeOut(mov), FadeIn(P.vertice), run_time=0.3)

            # «hache igual a cero coma ocho»
            self.en("h08")
            self.play(Create(guia_v), FadeIn(h08), run_time=self.dur(0.6))

            # «el error baja a cero coma ocho»
            self.en("j08")
            self.play(Create(guia_h), FadeIn(j08), run_time=self.dur(0.7))

            # «no es veintitrés»
            self.en("no23")
            self.pop(n23)
            self.play(Create(tach), run_time=self.dur(0.4))

            # «veinte más cero coma ocho por tres»
            self.en("cuenta")
            self.play(FadeIn(cuenta, shift=UP * 0.1), run_time=self.dur(0.8))

            # «veintidós coma cuatro»
            self.en("r224")
            self.pop(r224, sonido="exito")
        self.wait(1.0)
        self.limpiar()
