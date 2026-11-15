"""Escena 06 — Un paso adelante: predicción 21,8 con error 2,56, y la parábola del sensor vuelve."""
from comun.escena import *


def g_sensor(x):
    return 4 - 4.8 * x + 4 * x ** 2


class UnPasoAdelante(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.P = PanelSensor(centro=(-2.8, 0.2), ancho=6.2, alto=3.2, n=44, n0=30)
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        P, n0 = self.P, self.P.n0
        dato = P.punto(n0, 3.0, TXT, 0.1)
        lm = Text("m = 1", color=AMBAR, weight=BOLD).scale(0.8).move_to([-2.8, 2.45, 0])
        hueco = Circle(radius=0.09, color=INK, stroke_width=3).move_to(P.p(n0 + 1, 2.2))
        flecha3 = Arrow(P.p(n0 + 1, 0), P.p(n0 + 1, 3.0), buff=0, color=SENAL, stroke_width=5,
                        max_tip_length_to_length_ratio=0.18)
        flecha18 = Arrow(P.p(n0 + 1, 0), P.p(n0 + 1, 1.8), buff=0, color=AMBAR, stroke_width=5,
                         max_tip_length_to_length_ratio=0.25)
        dpred = P.punto(n0 + 1, 1.8, AMBAR, 0.1)
        barra_err = Line(P.p(n0 + 1.8, 1.8 - 1.6), P.p(n0 + 1.8, 1.8 + 1.6), color=AMBAR, stroke_width=9,
                         stroke_opacity=0.4)

        rho = MathTex(r"\rho", "=", num_tex(0.6), color=TXT).scale(1.25).move_to([4.0, 3.0, 0])
        rho[0].set_color(AMBAR)
        cuenta = MathTex("20", "+", num_tex(0.6), r"\cdot", "3", color=TXT).scale(1.25).move_to([4.0, 2.0, 0])
        xh = MathTex(r"\hat x", "=", num_tex(21.8), color=ESTIMACION).scale(1.45).move_to([4.0, 1.0, 0])
        mm = MathTex("MMSE", "=", "4", "(1-0{,}36)", color=TXT).scale(1.25).move_to([4.0, -0.2, 0])
        mm[0].set_color(ERROR)
        e256 = MathTex("=", num_tex(2.56), color=ERROR).scale(1.45).move_to([4.0, -1.0, 0])

        sin_linea = Line(P.p(n0 + 2.6, -2.0), P.p(n0 + 2.6, 2.0), color=INK, stroke_width=9, stroke_opacity=0.4)
        dsin = Circle(radius=0.09, color=INK, stroke_width=3).move_to(P.p(n0 + 2.6, 0))
        b_sin = Rectangle(width=3.0, height=0.42, stroke_width=2, color=INK).set_fill(INK, 0.5).move_to([3.1, -2.4, 0])
        b_sin.align_to([1.6, 0, 0], LEFT)
        t_sin = Text("4", color=TXT).scale(0.42).next_to(b_sin, RIGHT, buff=0.15)
        b_con = Rectangle(width=1.92, height=0.42, stroke_width=2, color=ERROR).set_fill(ERROR, 0.5)
        b_con.move_to([3.1, -3.0, 0]).align_to([1.6, 0, 0], LEFT)
        t_con = Text("2,56", color=TXT).scale(0.42).next_to(b_con, RIGHT, buff=0.15)
        menos = Text("−36 %", color=AMBAR, weight=BOLD).scale(0.55).move_to([6.1, -2.7, 0])

        with self.narrar("b1"):
            # «Un paso adelante»
            self.en("paso1")
            self.play(Create(P.media), FadeIn(P.rotulo_media), Create(P.pasado), FadeIn(dato), FadeIn(lm),
                      FadeIn(hueco), run_time=self.dur(1.0))

            # «La correlación es cero coma seis»
            self.en("r06")
            self.play(FadeIn(rho), run_time=0.5)

            # «veinte más cero coma seis por tres»
            self.en("cuenta")
            self.play(FadeIn(cuenta), Create(flecha3), run_time=self.dur(0.8))

            # «veintiuno coma ocho grados»
            self.en("p218")
            self.play(ReplacementTransform(flecha3, flecha18), FadeOut(hueco), FadeIn(dpred), FadeIn(barra_err),
                      FadeIn(xh), run_time=0.7)

            # «El error cuadrático medio»
            self.en("mmse")
            self.play(FadeIn(mm[0]), FadeIn(mm[1]), run_time=0.4)

            # «cuatro por uno menos cero coma tres seis»
            self.en("ecm")
            self.play(FadeIn(mm[2]), FadeIn(mm[3]), run_time=0.6)

            # «dos coma cinco seis»
            self.en("e256")
            self.pop(e256)

            # «apostando a la media»
            self.en("sindato")
            self.play(FadeIn(sin_linea), FadeIn(dsin), run_time=0.5)

            # «la varianza entera, cuatro»
            self.en("v4")
            self.play(GrowFromEdge(b_sin, LEFT), FadeIn(t_sin), run_time=0.6)

            # «Mirar el presente»
            self.en("mirar")
            self.play(barra_err.animate.set_stroke(opacity=0.8), run_time=0.4)

            # «en más de un tercio»
            self.en("tercio")
            self.play(GrowFromEdge(b_con, LEFT), FadeIn(t_con), run_time=0.5)
            self.play(FadeIn(menos), run_time=0.4)

        self.derecha = VGroup(rho, cuenta, xh, mm, e256, sin_linea, dsin, b_sin, t_sin, b_con, t_con, menos)
        self.restos = VGroup(flecha18, dpred, barra_err, lm, dato)

    def parte_b2(self):
        P, n0 = self.P, self.P.n0
        ax, etq = ejes([-0.3, 1.3, 0.5], [0, 6, 2], ancho=4.6, alto=3.0, x_label=r"\lambda")
        parabola = ax.plot(g_sensor, x_range=[-0.3, 1.3, 0.02], color=ESTIMACION, stroke_width=5)
        grupo = VGroup(ax, etq, parabola).move_to([4.3, 0.4, 0])
        ax2, parabola2 = ax, parabola

        f3 = Arrow(P.p(n0 + 2, 0), P.p(n0 + 2, 3.0), buff=0, color=INK, stroke_width=4,
                   max_tip_length_to_length_ratio=0.18)
        f18 = Arrow(P.p(n0 + 3.2, 0), P.p(n0 + 3.2, 1.8), buff=0, color=AMBAR, stroke_width=6,
                    max_tip_length_to_length_ratio=0.22)
        t3 = Text("+3", color=INK, weight=BOLD).scale(0.45).next_to(f3, UP, buff=0.08)
        t18 = Text("+1,8", color=AMBAR, weight=BOLD).scale(0.45).next_to(f18, RIGHT, buff=0.08)
        tira = Arrow(P.p(n0 + 5, 1.8), P.p(n0 + 5, 0.05), buff=0, color=AMBAR, stroke_width=4,
                     max_tip_length_to_length_ratio=0.2)
        e = MathTex(num_tex(2.56), "?", color=ERROR).scale(1.1).move_to([-3.3, -2.5, 0])
        dmin = Dot(ax.c2p(0.6, g_sensor(0.6)), radius=0.11, color=ERROR)
        vmin = DashedLine(ax.c2p(0.6, g_sensor(0.6)), ax.c2p(0.6, 0), color=ERROR, stroke_width=3)
        lam = MathTex(r"\lambda=" + num_tex(0.6), color=ERROR).scale(0.9).next_to(ax.c2p(0.6, 0), DOWN, buff=0.25)
        rot = Text("error de predicción", color=INK).scale(0.45).move_to([4.3, -2.3, 0])

        with self.narrar("b2"):
            # «los tres grados enteros»
            self.en("tres")
            self.play(FadeOut(self.derecha), FadeOut(self.restos), run_time=0.5)
            self.play(Create(f3), FadeIn(t3), run_time=0.5)

            # «solo uno coma ocho»
            self.en("uno8")
            self.play(Create(f18), FadeIn(t18), run_time=0.5)

            # «Tira hacia la media»
            self.en("tira")
            self.play(Create(tira), run_time=0.5)

            # «¿Y ese dos coma cinco seis?»
            self.en("pregunta")
            self.pop(e)

            # «el punto más bajo de la parábola»
            self.en("parabola")
            self.play(Create(ax), FadeIn(etq), Create(parabola), run_time=self.dur(1.2))

            # «lambda igual a cero coma seis»
            self.en("lam")
            self.play(FadeIn(dmin), Create(vmin), FadeIn(lam), run_time=0.6)

            # «Aquella parábola»
            self.en("aquella")
            self.play(parabola.animate.set_stroke(width=8), run_time=0.4)

            # «el error de predecir una muestra»
            self.en("error")
            self.play(FadeIn(rot), run_time=0.4)
