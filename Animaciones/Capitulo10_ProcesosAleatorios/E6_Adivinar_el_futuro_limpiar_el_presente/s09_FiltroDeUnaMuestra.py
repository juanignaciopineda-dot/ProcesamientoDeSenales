"""Escena 09 — El filtro de una sola muestra: h = E[sr]/E[r²] = 0,8, por ortogonalidad."""
from comun.escena import *


class FiltroDeUnaMuestra(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        # r (cian) y s (azul): cos θ = 4 / (2·√5) → θ = 26,57°; la sombra de s sobre r mide 0,8 · |r|
        self.F = Flechas(origen=(-6.3, -1.9), largo=5.4, angulo=26.57, largo_objetivo=4.83,
                         color_dato=MEDIDA, color_objetivo=SENAL)
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        F = self.F
        ecu = MathTex(r"\hat s", "=", "h", r"\cdot", "r", color=TXT).scale(1.5).move_to([3.6, 3.0, 0])
        ecu[0].set_color(ESTIMACION)
        ecu[2].set_color(ESTIMACION)
        ecu[4].set_color(MEDIDA)
        mini = MathTex(r"E\big[(s-h\,r)^2\big]", r"\to", r"\min", color=TXT).scale(1.25).move_to([3.6, 1.9, 0])
        mini[0].set_color(ERROR)
        lr = MathTex("r", color=MEDIDA).scale(0.9).next_to(F.fin_presente, RIGHT, buff=0.15)
        ls = MathTex("s", color=SENAL).scale(0.9).next_to(F.fin_futuro, UR, buff=0.1)
        le = MathTex(r"s-h\,r", color=ERROR).scale(0.8).next_to((F.fin_sombra + F.fin_futuro) / 2, RIGHT, buff=0.2)
        self.lr, self.ls, self.le = lr, ls, le
        ortog = MathTex(r"E\big[(s-h\,r)\,r\big]", "=", "0", color=TXT).scale(1.25).move_to([3.6, 0.7, 0])
        despeja = MathTex(r"E[s\,r]", "-", r"h\,E[r^2]", "=", "0", color=TXT).scale(1.25).move_to([3.6, -0.5, 0])
        den = MathTex("h", "=", fr"\frac{{E[s\,r]}}{{E[r^2]}}", color=TXT).scale(1.4).move_to([3.6, -2.2, 0])
        den[0].set_color(ESTIMACION)
        marco = SurroundingRectangle(den, color=AMBAR, buff=0.18, stroke_width=3.5)
        self.derecha = VGroup(ecu, mini, ortog, despeja, den, marco)

        with self.narrar("b1"):
            # «hache por lo recibido ahora»
            self.en("hr")
            self.play(FadeIn(ecu), run_time=0.6)

            # «¿Qué hache?»
            self.en("que")
            self.resaltar(ecu[2], color=AMBAR, escala=1.4)

            # «mínimo el error cuadrático medio»
            self.en("minimo")
            self.play(FadeIn(mini), run_time=0.7)

            # «es la de la proyección»
            self.en("regla")
            self.play(Create(F.presente), Create(F.futuro), FadeIn(lr), FadeIn(ls), run_time=self.dur(1.0))
            self.play(Create(F.sombra), run_time=0.5)

            # «la señal menos hache por lo recibido»
            self.en("resto")
            self.play(Create(F.error), FadeIn(le), run_time=0.6)

            # «perpendicular al dato»
            self.en("perp")
            self.play(Create(F.recto), run_time=0.4)

            # «la esperanza del error por lo recibido»
            self.en("ortog")
            self.play(FadeIn(ortog[0]), FadeIn(ortog[1]), run_time=0.6)

            # «tiene que ser cero»
            self.en("cero")
            ortog[2].set_color(VERDE)
            self.pop(ortog[2])

            # «Despejando»
            self.en("despeja")
            self.play(FadeIn(despeja), run_time=0.7)

            # «entre la esperanza de lo recibido al cuadrado»
            self.en("den")
            self.play(FadeIn(den), run_time=0.6)
            self.play(Create(marco), run_time=0.4)

    def parte_b2(self):
        c1 = MathTex("E[s\\,r]", "=", "E[s^2]", "+", "E[s\\,d]", color=TXT).scale(1.2).move_to([3.6, 2.6, 0])
        c1[2].set_color(SENAL)
        c1[4].set_color(RUIDO)
        v4 = MathTex("4", color=SENAL).scale(1.2).next_to(c1[2], DOWN, buff=0.25)
        v0 = MathTex("0", color=RUIDO).scale(1.2).next_to(c1[4], DOWN, buff=0.25)
        c2 = MathTex("E[r^2]", "=", "4", "+", "1", "=", "5", color=TXT).scale(1.2).move_to([3.6, 0.6, 0])
        c2[2].set_color(SENAL)
        c2[4].set_color(RUIDO)
        q45 = MathTex("h", "=", r"\frac{4}{5}", color=TXT).scale(1.4).move_to([2.7, -1.6, 0])
        q45[0].set_color(ESTIMACION)
        h08 = MathTex("=", num_tex(0.8), color=ESTIMACION).scale(1.5).move_to([5.7, -1.6, 0])

        with self.narrar("b2"):
            # «Hagamos las cuentas»
            self.en("cuentas")
            self.play(FadeOut(self.derecha), FadeOut(self.lr), FadeOut(self.ls), FadeOut(self.le), run_time=0.4)

            # «la señal al cuadrado más la señal por el ruido»
            self.en("suma")
            self.play(FadeIn(c1), run_time=0.8)

            # «La primera esperanza»
            self.en("primera")
            self.play(c1[2].animate.set_color(AMBAR), run_time=0.4)

            # «la varianza, cuatro»
            self.en("c4")
            self.play(FadeIn(v4), run_time=0.4)

            # «es cero, porque no están relacionados»
            self.en("c0")
            self.play(c1[2].animate.set_color(SENAL), FadeIn(v0), run_time=0.5)

            # «Lo recibido al cuadrado»
            self.en("r2")
            self.play(FadeIn(c2[:2]), run_time=0.5)

            # «la varianza de la señal más la del ruido»
            self.en("sumvar")
            self.play(FadeIn(c2[2:5]), run_time=0.7)

            # «cuatro más uno, cinco»
            self.en("c5")
            self.play(FadeIn(c2[5:]), run_time=0.5)

            # «cuatro quintos»
            self.en("q45")
            self.play(FadeIn(q45), run_time=0.6)

            # «cero coma ocho»
            self.en("h08")
            self.pop(h08)
        self.cuentas = VGroup(c1, v4, v0, c2, q45, h08)

    def parte_b3(self):
        F = self.F
        parte = Arrow(F.fin_futuro, F.fin_presente, buff=0, color=RUIDO, stroke_width=5)
        ld = MathTex("d", color=RUIDO).scale(0.8).next_to((F.fin_futuro + F.fin_presente) / 2, RIGHT, buff=0.15)
        l08 = MathTex("h=" + num_tex(0.8), color=ESTIMACION).scale(0.8).next_to((F.o + F.fin_sombra) / 2, DOWN, buff=0.22)
        b_con = Rectangle(width=2.4, height=0.5, stroke_width=2, color=ERROR).set_fill(ERROR, 0.5)
        b_con.move_to([4.0, 2.4, 0]).align_to([2.6, 0, 0], LEFT)
        t_con = Text("con h: 0,8", color=TXT).scale(0.42).move_to(b_con)
        b_sin = Rectangle(width=3.0, height=0.5, stroke_width=2, color=INK).set_fill(INK, 0.5)
        b_sin.move_to([4.0, 1.6, 0]).align_to([2.6, 0, 0], LEFT)
        t_sin = Text("sin filtrar: 1", color=TXT).scale(0.42).move_to(b_sin)
        mejora = Arrow([6.2, 1.6 + 0.3, 0], [5.2, 2.4 - 0.05, 0], buff=0, color=VERDE, stroke_width=4)
        r_entera = Arrow(F.o, F.fin_presente, buff=0, color=MEDIDA, stroke_width=6)
        c_r = caja("r[n − 1]", MEDIDA, alto=0.7, scale=0.5).move_to([3.2, -2.9, 0])
        c_r0 = caja("r[n]", MEDIDA, alto=0.7, scale=0.5).move_to([5.3, -2.9, 0])

        with self.narrar("b3"):
            # «lo encoge un veinte por ciento»
            self.en("encoge")
            self.play(FadeOut(self.cuentas), FadeIn(l08), self.F.sombra.animate.set_stroke(width=14),
                      run_time=self.dur(0.8))

            # «una parte es ruido»
            self.en("parte")
            self.play(Create(parte), FadeIn(ld), run_time=0.6)

            # «El error que queda es cero coma ocho»
            self.en("e08")
            self.play(GrowFromEdge(b_con, LEFT), FadeIn(t_con), run_time=0.6)

            # «Si nos quedáramos»
            self.en("quedar")
            self.play(FadeIn(r_entera), run_time=0.4)

            # «tal cual»
            self.en("tal")
            self.resaltar(r_entera, color=MEDIDA, escala=1.05)

            # «todo el ruido: uno»
            self.en("e1")
            self.play(GrowFromEdge(b_sin, LEFT), FadeIn(t_sin), run_time=0.6)

            # «ya mejoramos»
            self.en("mejora")
            self.play(Create(mejora), run_time=0.5)

            # «también la muestra anterior»
            self.en("anterior")
            self.play(FadeIn(c_r0), FadeIn(c_r), run_time=0.6)
