"""Escena 09 — Las ecuaciones normales y la matriz de Toeplitz, deducidas entera."""
from comun.escena import *


class EcuacionesNormales(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.derivar()
        self.ortogonalidad()
        self.toeplitz()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def derivar(self):
        J = MathTex(r"J(h) = E\Big[\Big(y - \sum_{k} h_k\, x[n-k]\Big)^2\Big]", color=TXT).scale(1.0)
        J.move_to([0, 3.2, 0])
        hs = MathTex(r"h_0,\; h_1,\; \dots,\; h_{L-1}", color=ESTIMACION).scale(0.9).move_to([0, 2.2, 0])
        par = parabola_l(centro=(-4.6, 0.3), ancho=3.2, alto=1.8, fondo=0.25, color=ERROR)
        elipses = VGroup(*[Ellipse(width=3.6 * s, height=2.2 * s, color=ERROR, stroke_width=3, stroke_opacity=0.9)
                          for s in (1.0, 0.7, 0.4)]).move_to([2.2, 0.1, 0]).rotate(0.3)
        ejh = VGroup(Text("h₀", color=INK).scale(0.5).move_to([4.6, -1.3, 0]),
                     Text("h₁", color=INK).scale(0.5).move_to([0.2, 1.6, 0]))
        fondo = Dot([2.2, 0.1, 0], radius=0.13, color=AMBAR)
        t_h = Line([1.2, 0.1, 0], [3.2, 0.1, 0], color=TXT, stroke_width=3)
        t_v = Line([2.2, -0.9, 0], [2.2, 1.1, 0], color=TXT, stroke_width=3)
        d = formula(r"\frac{\partial J}{\partial h_j}", "=", r"-2\,E\big[\,e[n]\,", r"x[n-j]\,\big]", "=", "0",
                    escala=1.15, colores={2: ERROR}).move_to([0, -2.7, 0])

        with self.narrar("b1"):
            # «hacen mínimo el error cuadrático medio»
            self.en("min")
            self.corte()
            self.play(FadeIn(J, shift=DOWN * 0.2), run_time=self.dur(0.8))

            # «los ele coeficientes a la vez»
            self.en("alavez")
            self.play(FadeIn(hs), run_time=self.dur(0.5))

            # «la parábola de antes»
            self.en("parab")
            self.play(Create(par), run_time=self.dur(0.8))

            # «varias dimensiones»
            self.en("dim")
            self.play(Create(elipses), FadeIn(ejh), run_time=self.dur(0.8))

            # «un único punto más bajo»
            self.en("bajo")
            self.play(FadeIn(fondo, scale=2), run_time=self.dur(0.4))

            # «la pendiente respecto de cada coeficiente es cero»
            self.en("pend")
            self.play(Create(t_h), Create(t_v), run_time=self.dur(0.6))

            # «Derivamos respecto de hache de jota»
            self.en("deriv")
            self.play(FadeIn(d[0]), run_time=self.dur(0.6))

            # «menos dos por la media del error»
            self.en("res")
            self.play(FadeIn(d[1]), FadeIn(d[2]), run_time=self.dur(0.7))

            # «equis de ene menos jota»
            self.en("xj")
            self.play(FadeIn(d[3]), run_time=self.dur(0.5))

            # «Igualamos a cero»
            self.en("cero")
            self.play(FadeIn(d[4]), FadeIn(d[5]), run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def ortogonalidad(self):
        perp = MathTex(r"e \perp x[n-j]", color=ERROR).scale(1.4).move_to([-2.5, 3.0, 0])
        rango = MathTex(r"j = 0, \dots, L-1", color=INK).scale(0.95).move_to([3.6, 3.0, 0])
        mete = MathTex(r"E\Big[\Big(y - \sum_k h_k\,x[n-k]\Big)\,x[n-j]\Big] = 0", color=TXT).scale(1.0)
        mete.move_to([0, 1.5, 0])
        f = formula(r"E[\,y\,x[n-j]\,]", "=", r"\sum_k h_k\;E[\,x[n-k]\,x[n-j]\,]", escala=1.1).move_to([0, 0.0, 0])
        r_izq = SurroundingRectangle(f[0], color=AMBAR, buff=0.1)
        r_der = SurroundingRectangle(f[2], color=AMBAR, buff=0.1)
        cruz_l = MathTex(r"C_{yx}[j]", color=AMBAR).scale(1.0).next_to(f[0], DOWN, buff=0.5)
        distj = Text("distancia j", color=INK).scale(0.6).next_to(cruz_l, DOWN, buff=0.15)
        auto_l = MathTex(r"C_{xx}[j-k]", color=AMBAR).scale(1.0).next_to(f[2], DOWN, buff=0.5)
        distjk = Text("distancia j − k", color=INK).scale(0.6).next_to(auto_l, DOWN, buff=0.15)

        with self.narrar("b2"):
            # «el error es perpendicular a cada muestra»
            self.en("perp")
            self.corte()
            self.pop(perp)

            # «jota desde cero hasta ele menos uno»
            self.en("rango")
            self.play(FadeIn(rango), run_time=self.dur(0.5))

            # «Metemos dentro la estimación»
            self.en("mete")
            self.play(FadeIn(mete, shift=DOWN * 0.2), run_time=self.dur(0.8))

            # «pasamos la suma al otro lado»
            self.en("pasa")
            self.play(FadeOut(mete), *[FadeIn(f[i]) for i in range(len(f))], run_time=self.dur(0.9))

            # «A la izquierda»
            self.en("izq")
            self.play(Create(r_izq), run_time=self.dur(0.4))

            # «la correlación cruzada entre i griega y equis»
            self.en("cruz")
            self.play(FadeIn(cruz_l, shift=UP * 0.1), run_time=self.dur(0.5))

            # «a distancia jota»
            self.en("distj")
            self.play(FadeIn(distj), run_time=self.dur(0.4))

            # «A la derecha»
            self.en("der")
            self.play(FadeOut(r_izq), Create(r_der), run_time=self.dur(0.4))

            # «la autocorrelación de equis»
            self.en("auto")
            self.play(FadeIn(auto_l, shift=UP * 0.1), run_time=self.dur(0.5))

            # «a distancia jota menos ka»
            self.en("dist")
            self.play(FadeIn(distjk), run_time=self.dur(0.4))
            self.resaltar(auto_l, color=AMBAR, escala=1.1)
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def toeplitz(self):
        sel = sello("ecuaciones normales", AMBAR).move_to([-4.6, 3.4, 0])
        fila = formula(r"\sum_k h_k", r"C_{xx}[j-k]", "=", r"C_{yx}[j]", escala=1.3).move_to([0.5, 1.8, 0])
        M = MatrizT([["C[0]", "C[1]", "C[2]"], ["C[1]", "C[0]", "C[1]"], ["C[2]", "C[1]", "C[0]"]],
                    centro=(-3.6, -0.9), lado=1.5, escala=0.8)
        hcol = VGroup(*[MathTex(f"h_{i}", color=ESTIMACION).scale(0.8).move_to([0.2, -0.9 - (i - 1) * 1.2, 0])
                        for i in range(3)])
        igual = MathTex("=", color=TXT).scale(1.1).move_to([1.1, -0.9, 0])
        ccol = VGroup(*[MathTex(f"C_{{yx}}[{i}]", color=SENAL).scale(0.8).move_to([2.7, -0.9 - (i - 1) * 1.2, 0])
                        for i in range(3)])
        marco = SurroundingRectangle(M, color=AMBAR, buff=0.2)
        barra = MathTex(r"\lvert i - j \rvert", color=AMBAR).scale(0.9).move_to([-3.6, 1.1, 0])
        fila_r = Rectangle(width=4.7, height=0.9, stroke_width=0).set_fill(CIAN, 0.25).move_to(M.p(0, 1))
        col_r = Rectangle(width=1.3, height=3.7, stroke_width=0).set_fill(CIAN, 0.25).move_to(M.p(1, 2))
        toep = Text("Toeplitz", color=AMBAR, weight=BOLD).scale(0.8).move_to([-3.6, -3.3, 0])
        diagonal = DashedLine(M.p(0, 0) + UL * 0.5, M.p(2, 2) + DR * 0.5, color=INK, stroke_width=3)
        cols = [AMBAR, CIAN, VERDE]

        with self.narrar("b3"):
            # «las ecuaciones normales»
            self.en("sello")
            self.corte()
            self.pop(sel)

            # «la suma de hache de ka»
            self.en("sumahk")
            self.play(FadeIn(fila[0]), FadeIn(fila[1]), run_time=self.dur(0.7))

            # «es la correlación cruzada en jota»
            self.en("igual")
            self.play(FadeIn(fila[2]), FadeIn(fila[3]), run_time=self.dur(0.6))

            # «Escritas ordenadas»
            self.en("ordenadas")
            self.play(FadeIn(M), FadeIn(hcol), FadeIn(igual), FadeIn(ccol), run_time=self.dur(1.0))

            # «una matriz cuadrada»
            self.en("cuadrada")
            self.play(Create(marco), run_time=self.dur(0.5))

            # «depende solo de la distancia»
            self.en("distfc")
            self.play(FadeOut(marco), FadeIn(barra), run_time=self.dur(0.5))

            # «entre su fila y su columna»
            self.en("filacol")
            self.play(FadeIn(fila_r), FadeIn(col_r), run_time=self.dur(0.6))

            # «cada diagonal es constante»
            self.en("diag")
            self.play(FadeOut(fila_r), FadeOut(col_r), run_time=0.25)
            self.play(*[M.diag(k).animate.set_color(c) for k, c in enumerate(cols)], run_time=self.dur(0.8))

            # «matriz de Toeplitz»
            self.en("toeplitz")
            self.pop(toep)

            # «además es simétrica»
            self.en("simetrica")
            self.play(Create(diagonal), run_time=self.dur(0.6))
