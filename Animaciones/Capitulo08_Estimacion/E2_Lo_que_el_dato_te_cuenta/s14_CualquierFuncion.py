"""Escena 14 — Ortogonal a cualquier función del dato: la regla de ortogonalidad."""
from comun.escena import *


class CualquierFuncion(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        self.columnas()
        self.flechas()
        self.wait(1.0)
        self.limpiar()

    def columnas(self):
        h1 = caja("Recibo 1", MEDIDA, ancho=3.0, alto=0.9, scale=0.75).move_to([-3.4, 3.2, 0])
        h0 = caja("Recibo 0", MEDIDA, ancho=3.0, alto=0.9, scale=0.75).move_to([3.4, 3.2, 0])
        e1 = MathTex(r"E[e\mid R=1]=0", color=VERDE).scale(1.0).move_to([-3.4, 2.1, 0])
        e0 = MathTex(r"E[e\mid R=0]=0", color=VERDE).scale(1.0).move_to([3.4, 2.1, 0])
        g1 = MathTex(r"g=5", color=AMBAR).scale(1.5).move_to([-3.4, 0.9, 0])
        g0 = MathTex(r"g=-2", color=AMBAR).scale(1.5).move_to([3.4, 0.9, 0])
        formula_ = MathTex("E", "[", "e", r"\cdot", "g(R)", "]", color=TXT).scale(1.7).move_to([0, -0.6, 0])
        formula_[2].set_color(ERROR)
        formula_[4].set_color(AMBAR)
        l2 = MathTex(r"5\cdot E[e\mid R=1]\ \to\ 5\cdot 0", color=TXT).scale(1.1).move_to([0, -1.8, 0])
        l3 = MathTex(r"0{,}34\cdot 5\cdot 0\ +\ 0{,}66\cdot(-2)\cdot 0\ =\ 0", color=VERDE).scale(1.1).move_to([0, -3.0, 0])
        with self.narrar("b1"):
            # «una consecuencia fuerte»
            self.en("fuerte")
            self.play(FadeIn(h1), FadeIn(h0), FadeIn(e1), FadeIn(e0), run_time=self.dur(0.8))

            # «cualquier función de lo recibido»
            self.en("funcion")
            self.play(FadeIn(g1), FadeIn(g0), run_time=self.dur(0.5))

            # «un número para la columna del uno»
            self.en("n1")
            self.resaltar(g1, color=AMBAR)

            # «otro para la del cero»
            self.en("n0")
            self.resaltar(g0, color=AMBAR)

            # «Multiplícala por el error»
            self.en("mult")
            self.play(LaggedStart(*[FadeIn(formula_[i], scale=0.5) for i in range(6)], lag_ratio=0.2),
                      run_time=self.dur(1.5))

            # «haz la media»
            self.en("haz")
            self.resaltar(formula_, color=AMBAR, escala=1.06)

            # «Dentro de cada columna»
            self.en("dentro")
            m1 = SurroundingRectangle(VGroup(h1, e1, g1), color=AMBAR, buff=0.2, stroke_width=3)
            m0 = SurroundingRectangle(VGroup(h0, e0, g0), color=AMBAR, buff=0.2, stroke_width=3)
            self.play(Create(m1), Create(m0), run_time=self.dur(0.5))

            # «ese número es fijo y sale fuera»
            self.en("fuera")
            self.play(FadeIn(l2, shift=UP * 0.2), run_time=self.dur(0.6))

            # «la media del error en la columna»
            self.en("media_e")
            self.resaltar(e1, e0, color=VERDE)

            # «que es cero»
            self.en("cero")
            self.play(FadeIn(l3, shift=UP * 0.2), run_time=self.dur(0.6))

            # «sea cual sea la función»
            self.en("sea")
            for a, b in ((r"g=-7", r"g=3"), (r"g=1", r"g=100")):
                self.play(Transform(g1, MathTex(a, color=AMBAR).scale(1.5).move_to(g1)),
                          Transform(g0, MathTex(b, color=AMBAR).scale(1.5).move_to(g0)), run_time=0.5)

    def flechas(self):
        o = np.array([-2.6, -1.6, 0.0])
        e = Arrow(o, o + UP * 4.0, color=INK, buff=0, stroke_width=8)
        g = Arrow(o, o + RIGHT * 4.6, color=INK, buff=0, stroke_width=8)
        u = MathTex("U", color=TXT).scale(1.3).next_to(e.get_end(), UP, buff=0.1)
        v = MathTex("V", color=TXT).scale(1.3).next_to(g.get_end(), RIGHT, buff=0.1)
        with self.narrar("b2"):
            # «el capítulo siete»
            self.en("cap7")
            self.corte()
            cap = etiqueta("Capítulo 7", INK, 0.6).move_to([-5.8, 3.6, 0])
            self.play(FadeIn(cap), Create(e), Create(g), FadeIn(u), FadeIn(v), run_time=self.dur(0.8))

            # «cuya esperanza del producto vale cero»
            self.en("producto")
            eq = MathTex(r"E[U\cdot V]=0", color=AMBAR).scale(1.4).move_to([3.6, 2.4, 0])
            self.pop(eq)

            # «ortogonales»
            self.en("ortog")
            ang = VMobject(color=AMBAR, stroke_width=6).set_points_as_corners(
                [o + UP * 0.6, o + UP * 0.6 + RIGHT * 0.6, o + RIGHT * 0.6])
            self.play(Create(ang), run_time=self.dur(0.4))

            # «flechas perpendiculares»
            self.en("perp")
            ne = MathTex(r"\text{Error}", color=ERROR).scale(1.3).next_to(e.get_end(), UP, buff=0.1)
            ng = MathTex(r"g(R)", color=MEDIDA).scale(1.3).next_to(g.get_end(), RIGHT, buff=0.1)
            self.play(e.animate.set_color(ERROR), g.animate.set_color(MEDIDA), Transform(u, ne), Transform(v, ng),
                      run_time=self.dur(0.7))

            # «el error del mejor estimador»
            self.en("err")
            self.resaltar(e, color=AMBAR)

            # «cualquier función de lo observado»
            self.en("cualquier")
            extra = VGroup(Arrow(o, o + RIGHT * 2.4, color=MEDIDA, buff=0, stroke_width=6).shift(UP * 0.01),
                           Arrow(o, o + RIGHT * 3.4, color=MEDIDA, buff=0, stroke_width=6).shift(UP * 0.02),
                           Arrow(o, o + LEFT * 2.2, color=MEDIDA, buff=0, stroke_width=6))
            self.play(LaggedStart(*[Create(a) for a in extra], lag_ratio=0.3), run_time=self.dur(1.2))

            # «regla de ortogonalidad»
            self.en("regla")
            reg = Text("Regla de ortogonalidad", color=AMBAR, weight=BOLD).scale(1.0).move_to([3.4, -0.6, 0])
            self.pop(reg)

            # «la idea más importante»
            self.en("importante")
            marco = SurroundingRectangle(reg, color=AMBAR, buff=0.3, stroke_width=5)
            self.play(Create(marco), run_time=self.dur(0.5))
