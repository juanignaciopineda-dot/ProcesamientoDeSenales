"""Escena 03 — Dos termómetros: ruidos 1 y 4, lecturas 23 y 22; la apuesta con dos pesos y dos condiciones."""
from comun.escena import *
from comun.figuras_c8e5 import *


class DosTermometros(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.planteo()
        self.condiciones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def planteo(self):
        A = Termo8("A", centro=(-5.2, 0.7), alto=3.0, escala_letra=1.0)
        B = Termo8("B", centro=(-2.2, 0.7), alto=3.0, escala_letra=1.0)
        ra = A.debajo(ruido8(ancho=1.9, amp=0.07, semilla=2, grosor=4), 0.3)
        rb = B.debajo(ruido8(ancho=1.9, amp=0.3, semilla=5, grosor=4), 0.3)
        va = MathTex(r"\sigma^2=1", color=RUIDO).scale(0.85).next_to(ra, DOWN, buff=0.25)
        vb = MathTex(r"\sigma^2=4", color=RUIDO).scale(0.85).next_to(rb, DOWN, buff=0.25)
        va.set_y(-2.75)
        vb.set_y(-2.75)
        sin = Text("Sin relación", color=INK).scale(0.5).move_to([-3.7, -3.5, 0])
        lbl = Text("Temperatura", color=SENAL).scale(0.6).move_to([2.9, 3.0, 0])
        ty = MathTex("y", color=SENAL).scale(1.1).move_to([1.0, 2.1, 0])
        mu = MathTex(r"\mu=20", color=SENAL).scale(0.95).move_to([2.6, 2.1, 0])
        s2 = MathTex(r"\sigma^2=4", color=SENAL).scale(0.95).move_to([4.6, 2.1, 0])
        n23 = Text("23", color=MEDIDA, weight=BOLD).scale(0.8).move_to([-4.3, 1.6, 0])
        n22 = Text("22", color=MEDIDA, weight=BOLD).scale(0.8).move_to([-1.3, 1.3, 0])
        que = MathTex(r"y=\;?", color=AMBAR).scale(1.6).move_to([2.8, 0.0, 0])

        with self.narrar("b1"):
            # «Pongamos»
            self.en("a")
            self.play(FadeIn(A, shift=UP * 0.2), run_time=self.dur(0.4))

            # «un segundo termómetro»
            self.en("b")
            self.play(FadeIn(B, shift=LEFT * 0.4), run_time=self.dur(0.6))

            # «más barato que el primero»
            self.en("barato")
            self.play(Wiggle(B, scale_value=1.04, rotation_angle=0.04 * TAU), run_time=self.dur(0.9))

            # «El primero, el A»
            self.en("ra")
            self.resaltar(A.letra, color=AMBAR, escala=1.3)

            # «de varianza uno»
            self.en("r1")
            self.play(Create(ra), FadeIn(va), run_time=self.dur(0.7))

            # «El segundo, el B»
            self.en("rb")
            self.resaltar(B.letra, color=AMBAR, escala=1.3)

            # «de varianza cuatro»
            self.en("r4")
            self.play(Create(rb), FadeIn(vb), run_time=self.dur(0.7))

            # «no tienen nada que ver»
            self.en("indep")
            self.play(FadeIn(sin, shift=UP * 0.1), run_time=self.dur(0.5))

            # «ni con la temperatura»
            self.en("temp")
            self.play(FadeIn(lbl), FadeIn(ty), run_time=self.dur(0.4))
            self.play(FadeIn(mu, shift=LEFT * 0.2), FadeIn(s2, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «A marca veintitrés»
            self.en("m23")
            self.play(A.nivel(0.7), run_time=self.dur(0.5))
            self.pop(n23)

            # «B marca veintidós»
            self.en("m22")
            self.play(B.nivel(0.6), run_time=self.dur(0.5))
            self.pop(n22)

            # «¿Qué temperatura hace?»
            self.en("que")
            self.pop(que)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def condiciones(self):
        f = formula(r"\hat{y}", "=", "20", "+", "h_A", r"(x_A-20)", "+", "h_B", r"(x_B-20)", escala=1.15,
                    colores={0: ESTIMACION, 4: ESTIMACION, 5: MEDIDA, 7: ESTIMACION, 8: MEDIDA}).move_to([0, 3.0, 0])
        marcos = VGroup(SurroundingRectangle(f[4], color=AMBAR, buff=0.08),
                        SurroundingRectangle(f[7], color=AMBAR, buff=0.08))
        P = PlanoDos8(centro=(-1.4, -1.0), k=1.45)
        dosc = Text("2 condiciones", color=TXT, weight=BOLD).scale(0.6).move_to([4.5, 0.9, 0])
        pa = MathTex(r"e\perp x_A", color=TXT).scale(1.0).move_to([4.5, -0.2, 0])
        pb = MathTex(r"e\perp x_B", color=TXT).scale(1.0).move_to([4.5, -1.2, 0])
        for m, c in ((pa, MEDIDA), (pb, MEDIDA)):
            m[0][0].set_color(ERROR)
            m[0][2:].set_color(c)

        with self.narrar("b2"):
            # «La apuesta es ahora veinte»
            self.en("veinte")
            self.corte()
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.5))

            # «el peso de A»
            self.en("ha")
            self.play(FadeIn(f[3]), FadeIn(f[4], shift=UP * 0.1), run_time=self.dur(0.4))

            # «por lo que A se aparta de veinte»
            self.en("xa")
            self.play(FadeIn(f[5], shift=UP * 0.1), run_time=self.dur(0.5))

            # «el peso de B»
            self.en("hb")
            self.play(FadeIn(f[6]), FadeIn(f[7], shift=UP * 0.1), run_time=self.dur(0.4))

            # «por lo que se aparta B»
            self.en("xb")
            self.play(FadeIn(f[8], shift=UP * 0.1), run_time=self.dur(0.5))

            # «Dos pesos por elegir»
            self.en("dos")
            self.play(Create(marcos), run_time=self.dur(0.6))

            # «la regla es la de siempre»
            self.en("regla")
            self.play(FadeIn(P.plano), GrowArrow(P.xa), GrowArrow(P.xb), FadeIn(P.rot["xa"]), FadeIn(P.rot["xb"]),
                      run_time=self.dur(0.8))

            # «el error tiene que ser ortogonal»
            self.en("orto")
            self.play(GrowArrow(P.y), FadeIn(P.rot["y"]), run_time=self.dur(0.5))
            self.play(Create(P.sombra), Create(P.error), FadeIn(P.rot["yh"]), FadeIn(P.rot["e"]), run_time=self.dur(0.6))

            # «todo lo que usa la estimación»
            self.en("todo")
            self.play(P.plano.animate(rate_func=there_and_back).set_fill(AMBAR, 0.3), run_time=self.dur(1.0))

            # «Como usa dos lecturas»
            self.en("dosl")
            self.resaltar(P.xa, P.xb, color=AMBAR, escala=1.06)

            # «hay dos condiciones»
            self.en("doscond")
            self.pop(dosc)

            # «perpendicular a A»
            self.en("pa")
            self.play(Create(P.recto_a), FadeIn(pa, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «y también a B»
            self.en("pb")
            self.play(Create(P.recto_b), FadeIn(pb, shift=LEFT * 0.2), run_time=self.dur(0.5))
