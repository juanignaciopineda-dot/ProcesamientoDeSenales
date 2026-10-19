"""Escena 04 — El punto de la recta más cercano a Y es el pie de la perpendicular: la sombra, con h = 0,8."""
from comun.escena import *
from comun.figuras_c8e4 import *


class ElPuntoMasCercano(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.F, self.r = flechas8()
        F, r = self.F, self.r
        self.add(F.presente, F.futuro, r["x"], r["y"])
        self.cercano()
        self.colegio()
        self.cuanto()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def cercano(self):
        F = self.F
        tr = ValueTracker(0.45)
        punto = always_redraw(lambda: Dot(en_recta8(F, tr.get_value()), radius=0.13, color=ESTIMACION))
        seg = always_redraw(lambda: Line(en_recta8(F, tr.get_value()), F.fin_futuro, color=ERROR, stroke_width=5))
        et_e = always_redraw(lambda: MathTex("e", color=ERROR).scale(0.9).move_to(
            (en_recta8(F, tr.get_value()) + F.fin_futuro) / 2 + RIGHT * 0.35))
        est = formula(r"\hat{y}", "=", "h", r"\cdot", "X", escala=1.2,
                      colores={0: ESTIMACION, 2: ESTIMACION, 4: MEDIDA}).move_to([3.7, 2.8, 0])
        largo2 = MathTex(r"|e|^2", color=ERROR).scale(1.0)
        ecm = Text("= error cuadrático medio", color=TXT).scale(0.55)
        panel = VGroup(largo2, ecm).arrange(RIGHT, buff=0.2).move_to([3.7, 1.3, 0])
        cual = Text("?", color=AMBAR, weight=BOLD).scale(2.2).move_to([3.7, -0.9, 0])

        with self.narrar("b1"):
            # «el punto de esa recta»
            self.en("punto")
            self.play(FadeIn(punto, scale=0.4), FadeIn(est), run_time=self.dur(0.6))

            # «la punta de la flecha de la temperatura»
            self.en("punta")
            self.play(Create(seg), run_time=self.dur(0.7))

            # «el error es la flecha»
            self.en("error")
            self.play(FadeIn(et_e), run_time=self.dur(0.4))

            # «su largo al cuadrado»
            self.en("largo2")
            self.play(FadeIn(largo2), run_time=self.dur(0.5))

            # «error cuadrático medio»
            self.en("ecm")
            self.play(FadeIn(ecm), run_time=self.dur(0.6))

            # «Probemos puntos»
            self.en("probemos")
            self.play(tr.animate.set_value(0.9), run_time=self.dur(0.9))
            self.play(tr.animate.set_value(0.3), run_time=self.dur(0.9))

            # «Uno muy atrás»
            self.en("atras")
            self.play(tr.animate.set_value(-0.2), run_time=self.dur(1.2))

            # «Uno muy adelante»
            self.en("adelante")
            self.play(tr.animate.set_value(1.4), run_time=self.dur(1.6))

            # «¿Cuál es el más cercano?»
            self.en("cual")
            self.pop(cual)
            self.play(tr.animate.set_value(0.8), run_time=self.dur(1.2))
            punto.clear_updaters()
            seg.clear_updaters()
            et_e.clear_updaters()
            self.play(FadeOut(punto), FadeOut(seg), FadeOut(et_e), FadeOut(cual), FadeOut(est), FadeOut(largo2),
                      FadeOut(ecm), run_time=0.4)

    # ------------------------------------------------------------ b2
    def colegio(self):
        F, r = self.F, self.r
        grises = VGroup(*[Line(en_recta8(F, h), F.fin_futuro, color=INK, stroke_width=3) for h in (0.1, 0.45, 1.2, 1.5)])
        perp = Line(F.fin_sombra, F.fin_futuro, color=ERROR, stroke_width=8)
        pie = Dot(F.fin_sombra, radius=0.13, color=ESTIMACION)
        sol_ = sol().scale(1.0).move_to([-4.0, 3.3, 0])
        luces = VGroup(*[DashedLine(F.o + f * (F.fin_futuro - F.o), F.o + f * (F.fin_futuro - F.o) * np.array([1, 0, 0]),
                                    color="#f2d04b", dash_length=0.12, stroke_width=3)
                         for f in (0.2, 0.4, 0.6, 0.8)])
        palabra_p = self.palabra("Proyección", AMBAR, 1.0).move_to([3.7, 1.6, 0])

        with self.narrar("b2"):
            # «una regla del colegio»
            self.en("colegio")
            self.play(LaggedStart(*[Create(g) for g in grises], lag_ratio=0.3), run_time=self.dur(1.0))

            # «la distancia más corta»
            self.en("corta")
            self.play(LaggedStart(*[Indicate(g, color=AMBAR, scale_factor=1.0) for g in grises], lag_ratio=0.35),
                      run_time=self.dur(1.6))

            # «la perpendicular»
            self.en("perp")
            self.play(Create(perp), *[g.animate.set_stroke(opacity=0.25) for g in grises], FadeIn(r["e"]),
                      run_time=self.dur(0.7))

            # «el pie de esa perpendicular»
            self.en("pie")
            self.play(FadeIn(pie, scale=0.4), Create(F.recto), run_time=self.dur(0.6))

            # «la sombra»
            self.en("sombra")
            self.play(FadeIn(sol_, shift=DOWN * 0.3), run_time=self.dur(0.6))

            # «sobre la recta de la lectura»
            self.en("sobre")
            self.play(Create(F.sombra), FadeIn(r["yh"]), run_time=self.dur(0.7))

            # «la luz cayendo»
            self.en("luz")
            self.play(LaggedStart(*[Create(l) for l in luces], lag_ratio=0.25), run_time=self.dur(1.0))

            # «Se llama proyección»
            self.en("proy")
            self.pop(palabra_p)
            self.play(FadeOut(sol_), FadeOut(luces), FadeOut(grises), FadeOut(palabra_p), run_time=0.5)
        self.perp, self.pie = perp, pie

    # ------------------------------------------------------------ b3
    def cuanto(self):
        F, r = self.F, self.r
        interr = MathTex("?", color=ESTIMACION).scale(1.1).move_to(r["yh"])
        valor = MathTex(num_tex(1.79), color=ESTIMACION).scale(0.9).move_to(r["yh"])
        f1 = formula(r"\text{Sombra}", "=", "2", r"\cdot", r"\cos\theta", escala=1.1,
                     colores={0: ESTIMACION, 2: SENAL}).move_to([3.9, 2.8, 0])
        f2 = formula("=", "2", r"\cdot", num_tex(0.89), escala=1.1, colores={1: SENAL}).move_to([3.9, 1.9, 0])
        f3 = formula(r"\approx", num_tex(1.79), escala=1.1, colores={1: ESTIMACION}).next_to(f2, RIGHT, buff=0.2)
        g1 = formula("h", "=", num_tex(1.79), "/", escala=1.05, colores={0: ESTIMACION}).move_to([2.6, 0.7, 0])
        g2 = MathTex(r"\sqrt{5}", color=MEDIDA).scale(1.05).next_to(g1, RIGHT, buff=0.15)
        g3 = MathTex("=", num_tex(0.8), color=VERDE).scale(1.05).next_to(g2, RIGHT, buff=0.25)
        marco = SurroundingRectangle(VGroup(g1, g2, g3), color=VERDE, buff=0.18, stroke_width=3)
        P = ParabolaJ(centro=(4.6, -2.4), ancho=3.2, alto=1.6)
        et_p = MathTex("h=" + num_tex(0.8), color=VERDE).scale(0.8).next_to(P.vertice, DOWN, buff=0.25)

        with self.narrar("b3"):
            # «¿Cuánto mide la sombra?»
            self.en("cuanto")
            self.play(ReplacementTransform(r["yh"], interr), run_time=self.dur(0.5))
            self.resaltar(F.sombra, color=AMBAR, escala=1.04)

            # «El largo de la flecha por el coseno»
            self.en("lc")
            self.play(FadeIn(f1), run_time=self.dur(0.9))

            # «dos por cero coma ocho nueve»
            self.en("dosx")
            self.play(FadeIn(f2), run_time=self.dur(0.7))

            # «uno coma siete nueve»
            self.en("s179")
            self.play(FadeIn(f3), ReplacementTransform(interr, valor), run_time=self.dur(0.6))

            # «qué múltiplo de la lectura es»
            self.en("mult")
            self.resaltar(F.presente, color=MEDIDA, escala=1.04)

            # «la dividimos»
            self.en("divide")
            self.play(FadeIn(g1), run_time=self.dur(0.6))

            # «raíz de cinco»
            self.en("r5")
            self.play(FadeIn(g2), run_time=self.dur(0.5))

            # «Da cero coma ocho»
            self.en("h08")
            self.play(FadeIn(g3), Create(marco), run_time=self.dur(0.6))

            # «El mismo número que salió de la parábola»
            self.en("parab")
            self.play(Create(P.eje), Create(P.curva), run_time=self.dur(0.8))
            self.play(FadeIn(P.vertice), FadeIn(et_p), run_time=self.dur(0.5))

            # «solo un dibujo»
            self.en("dib")
            self.resaltar(F.sombra, color=AMBAR, escala=1.04)
