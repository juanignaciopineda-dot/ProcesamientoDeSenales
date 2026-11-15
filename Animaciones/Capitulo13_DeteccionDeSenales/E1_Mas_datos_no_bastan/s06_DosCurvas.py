"""Escena 06 — Una medición: dos densidades uniformes y sus alturas."""
from comun.escena import *

ESC = 3.0           # centímetros de pantalla por unidad de densidad


class DosCurvas(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.R = RectaR(centro=(0.0, -1.2), ancho=9.5, x_rango=(-1.5, 1.5))
        self.mediciones()
        self.alturas()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def mediciones(self):
        R = self.R
        punto = Dot(R.p(0.3), radius=0.18, color=MEDIDA)
        r_et = MathTex("r", color=MEDIDA).scale(1.1).next_to(punto, UP, buff=0.15)
        h0 = MathTex("H_0", color=RUIDO).scale(1.5).move_to([-5.6, 1.6, 0])
        h1 = MathTex("H_1", color=SENAL).scale(1.5).move_to([-5.6, 0.4, 0])
        m_1, m1 = R.marca(-1, "-1", escala=0.7), R.marca(1, "1", escala=0.7)
        tramo0 = Line(R.p(-1), R.p(1), color=RUIDO, stroke_width=8).shift(UP * 0.0)
        mm, m_m = R.marca(-0.5, r"-\tfrac12", escala=0.7), R.marca(0.5, r"\tfrac12", escala=0.7)
        tramo1 = Line(R.p(-0.5), R.p(0.5), color=SENAL, stroke_width=8).shift(UP * 0.18)
        rng = np.random.default_rng(5)
        caen = VGroup(*[Dot(R.p(x) + UP * 0.45 + UP * rng.uniform(0, 0.25), radius=0.07, color=RUIDO)
                        for x in np.linspace(-0.95, 0.95, 14)])
        apriori = Text("a priori", color=AMBAR, weight=BOLD).scale(1.1).move_to([-4.8, 3.1, 0])
        grande = MathTex("H_0", color=RUIDO).scale(2.0).move_to([-1.4, 3.0, 0])
        peque = MathTex("H_1", color=SENAL).scale(1.0).move_to([0.5, 3.0, 0])
        p34 = MathTex("p_0=", r"\tfrac34", r"\;\cdot\;", "p_1=", r"\tfrac14", color=TXT).scale(1.3).move_to([3.9, 3.0, 0])
        p34[0].set_color(RUIDO)
        p34[1].set_color(RUIDO)
        p34[3].set_color(SENAL)
        p34[4].set_color(SENAL)

        with self.narrar("b1"):
            # «Imagina una medición»
            self.en("medicion")
            self.play(FadeIn(R), FadeIn(punto), run_time=self.dur(0.5))

            # «un solo número»
            self.en("numero")
            self.play(FadeIn(r_et), run_time=self.dur(0.4))

            # «Bajo la hipótesis cero»
            self.en("bajoh0")
            self.pop(h0)

            # «entre menos uno y uno»
            self.en("m11")
            self.play(FadeIn(m_1), FadeIn(m1), run_time=self.dur(0.4))
            self.play(Create(tramo0), run_time=self.dur(0.5))

            # «con la misma probabilidad»
            self.en("igual")
            self.play(FadeIn(caen, lag_ratio=0.12), run_time=self.dur(1.3))

            # «Bajo la hipótesis uno»
            self.en("bajoh1")
            self.pop(h1)

            # «entre menos un medio y un medio»
            self.en("mm")
            self.play(FadeIn(mm), FadeIn(m_m), run_time=self.dur(0.4))
            self.play(Create(tramo1), run_time=self.dur(0.5))

            # «a priori»
            self.en("apriori")
            self.pop(apriori)

            # «tres veces más probable»
            self.en("tres")
            self.play(FadeIn(grande, scale=0.5), FadeIn(peque, scale=0.5), run_time=self.dur(0.6))

            # «tres cuartos frente a un cuarto»
            self.en("p34")
            self.play(FadeIn(p34, shift=UP * 0.1), run_time=self.dur(0.7))
        self.wait(0.3)
        self.R_marcas = VGroup(m_1, m1, mm, m_m)
        self.quitar = VGroup(punto, r_et, h0, h1, tramo0, tramo1, caen, apriori, grande, peque, p34)

    # ------------------------------------------------------------ b2
    def alturas(self):
        R = self.R
        r0 = rect_dens(R, -1, 1, 0.001, ESC, RUIDO)
        r1 = rect_dens(R, -0.5, 0.5, 0.001, ESC, SENAL)
        r0f = rect_dens(R, -1, 1, 0.5, ESC, RUIDO)
        r1f = rect_dens(R, -0.5, 0.5, 1.0, ESC, SENAL)
        interrog = Text("?", color=AMBAR, weight=BOLD).scale(1.2).move_to([-3.2, 0.2, 0])
        area = MathTex(r"\text{área}=1", color=AMBAR).scale(1.2).move_to([-5.0, 2.4, 0])
        lla2 = BraceBetweenPoints(R.p(-1) + DOWN * 0.7, R.p(1) + DOWN * 0.7, direction=DOWN, color=RUIDO)
        t2 = MathTex("2", color=RUIDO).scale(0.8).next_to(lla2, DOWN, buff=0.05).shift(LEFT * 2.2)
        lla1 = BraceBetweenPoints(R.p(-0.5) + DOWN * 1.6, R.p(0.5) + DOWN * 1.6, direction=DOWN, color=SENAL)
        t1 = MathTex("1", color=SENAL).scale(0.8).next_to(lla1, DOWN, buff=0.05)
        c0 = MathTex(r"2\cdot \text{alto}=1\;\Rightarrow\;\text{alto}=\tfrac12", color=RUIDO).scale(1.0).move_to([-3.5, 3.4, 0])
        c1 = MathTex(r"1\cdot \text{alto}=1\;\Rightarrow\;\text{alto}=1", color=SENAL).scale(1.0).move_to([3.6, 3.4, 0])
        f0 = MathTex(r"f(r\mid H_0)", color=RUIDO).scale(0.9).move_to([-4.4, 0.6, 0])
        f1 = MathTex(r"f(r\mid H_1)", color=SENAL).scale(1.0).next_to(r1f, UP, buff=0.15).shift(RIGHT * 1.3)

        with self.narrar("b2"):
            # «¿Qué altura tienen esas dos curvas?»
            self.en("altura")
            self.play(FadeOut(self.quitar), FadeOut(self.R_marcas), run_time=0.3)
            self.play(FadeIn(r0), FadeIn(r1), FadeIn(interrog), run_time=self.dur(0.5))

            # «El área de cada una tiene que valer uno»
            self.en("area")
            self.play(FadeOut(interrog), FadeIn(area), run_time=self.dur(0.4))

            # «La primera mide dos de ancho»
            self.en("ancho2")
            self.play(FadeIn(lla2), FadeIn(t2), run_time=self.dur(0.5))

            # «su altura es un medio»
            self.en("alto12")
            self.play(FadeIn(c0, shift=UP * 0.1), run_time=self.dur(0.5))
            self.play(Transform(r0, r0f), run_time=self.dur(0.7))

            # «La segunda mide uno de ancho»
            self.en("ancho1")
            self.play(FadeIn(lla1), FadeIn(t1), run_time=self.dur(0.5))

            # «su altura es uno»
            self.en("alto1")
            self.play(FadeIn(c1, shift=UP * 0.1), run_time=self.dur(0.5))
            self.play(Transform(r1, r1f), run_time=self.dur(0.7))

            # «las densidades»
            self.en("densidades")
            self.play(FadeIn(f0), FadeIn(f1), FadeOut(area), run_time=self.dur(0.5))

            # «cuánto cabe esperar cada valor»
            self.en("esperar")
            rng = np.random.default_rng(11)
            gotas = VGroup(*[Dot(R.p(rng.uniform(-1, 1)) + UP * 2.6, radius=0.07, color=MEDIDA)
                             for _ in range(10)])
            self.add(gotas)
            self.play(*[g.animate.shift(DOWN * 2.6) for g in gotas], run_time=self.dur(1.2))

            # «según quién sea la verdadera»
            self.en("verdadera")
            self.play(r0.animate.set_fill(RUIDO, 0.55), r1.animate.set_fill(SENAL, 0.1), run_time=self.dur(0.4))
            self.play(r0.animate.set_fill(RUIDO, 0.1), r1.animate.set_fill(SENAL, 0.55), run_time=self.dur(0.4))
        self.wait(0.3)
