"""Escena 09 — Demostración, primera parte: sumar y restar la media parte el error en dos trozos."""
from comun.escena import *


class SumarYRestar(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.planteo()
        self.cuadrado_de_la_suma()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def planteo(self):
        cY = caja("Y", SENAL, ancho=1.5, alto=1.5, scale=1.5).move_to([0, 0.9, 0])
        mu = MathTex(r"\mu", color=ESTIMACION).scale(1.6).next_to(cY, RIGHT, buff=0.8)
        sg = MathTex(r"\sigma^2", color=RUIDO).scale(1.6).next_to(cY, DOWN, buff=0.4)
        yh = MathTex(r"\hat{y}", color=ESTIMACION).scale(2.6).move_to([-3.6, -1.9, 0])

        F1 = formula("E[", "(", "Y", "-", r"\hat{y}", ")^2", "]", escala=1.8,
                     colores={2: SENAL, 4: ESTIMACION}).move_to([0.2, 1.7, 0])
        sr = MathTex(r"-\mu+\mu", color=ESTIMACION).scale(1.4).next_to(F1[3], UP, buff=0.5)
        nada = MathTex(r"-\mu+\mu=0", color=INK).scale(1.2).move_to([5.3, 1.7, 0])
        F2 = formula(r"Y-\hat{y}", "=", r"(Y-\mu)", "+", r"(\mu-\hat{y})", escala=1.5,
                     colores={0: TXT, 2: SENAL, 4: ESTIMACION}).move_to([0, -0.5, 0])
        self.F2 = F2

        with self.narrar("b1"):
            # «en general»
            self.en("general")
            self.play(FadeIn(cY, scale=0.6), run_time=self.dur(0.5))

            # «de media mu»
            self.en("mu")
            self.pop(mu)

            # «varianza sigma cuadrado»
            self.en("sigma")
            self.pop(sg)

            # «Queremos el número»
            self.en("quiero")
            self.pop(yh)

            # «hace más pequeña la media de»
            self.en("media")
            self.play(FadeOut(cY), FadeOut(mu), FadeOut(sg), FadeOut(yh), run_time=0.3)
            self.play(FadeIn(F1[0]), FadeIn(F1[6]), run_time=self.dur(0.5))

            # «i griega menos i griega sombrero»
            self.en("resta")
            self.play(LaggedStart(*[FadeIn(F1[i], shift=UP * 0.1) for i in (1, 2, 3, 4)], lag_ratio=0.2), run_time=self.dur(1.0))

            # «al cuadrado»
            self.en("cuad")
            self.play(FadeIn(F1[5], shift=UP * 0.1), run_time=self.dur(0.4))

            # «sumar y restar la media»
            self.en("sumar")
            self.play(FadeIn(sr, shift=DOWN * 0.2), run_time=self.dur(0.6))

            # «No cambia nada»
            self.en("nada")
            self.play(FadeIn(nada, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «en dos trozos»
            self.en("trozos")
            self.play(FadeIn(F2[0], shift=UP * 0.1), FadeIn(F2[1]), run_time=self.dur(0.5))
            self.play(FadeIn(F2[2], shift=UP * 0.1), FadeIn(F2[3]), FadeIn(F2[4], shift=UP * 0.1), run_time=self.dur(0.8))
        self.wait(0.3)
        self.F1 = VGroup(F1, sr, nada)

    # ------------------------------------------------------------ b2
    def cuadrado_de_la_suma(self):
        F2 = self.F2
        R = Line([-4.0, 0.2, 0], [4.0, 0.2, 0], color=INK, stroke_width=2.5)
        pY = Dot([-3.0, 0.2, 0], radius=0.14, color=SENAL)
        pM = Dot([0.0, 0.2, 0], radius=0.14, color=TXT)
        pH = Dot([2.6, 0.2, 0], radius=0.14, color=ESTIMACION)
        lY = MathTex("Y", color=SENAL).scale(0.9).next_to(pY, DOWN, buff=0.2)
        lM = MathTex(r"\mu", color=TXT).scale(0.9).next_to(pM, DOWN, buff=0.2)
        lH = MathTex(r"\hat{y}", color=ESTIMACION).scale(0.9).next_to(pH, DOWN, buff=0.2)
        aY = Arrow(pY.get_center() + UP * 0.35, pM.get_center() + UP * 0.35, buff=0.05, color=SENAL, stroke_width=5)
        aH = Arrow(pH.get_center() + UP * 0.35, pM.get_center() + UP * 0.35, buff=0.05, color=ESTIMACION, stroke_width=5)
        recta = VGroup(R, pY, pM, pH, lY, lM, lH)

        AB = formula("(", "A", "+", "B", ")^2", escala=1.5, colores={1: SENAL, 3: ESTIMACION}).move_to([-3.8, 0.5, 0])
        abc = MathTex(r"(a+b)^2=a^2+2ab+b^2", color=INK).scale(1.25).move_to([2.9, 0.5, 0])
        fila = formula(r"(Y-\mu)^2", "+", r"2(Y-\mu)(\mu-\hat{y})", "+", r"(\mu-\hat{y})^2", escala=1.15,
                       colores={0: SENAL, 2: ERROR, 4: ESTIMACION}).move_to([0, -2.4, 0])
        r1 = SurroundingRectangle(F2[2], buff=0.12, color=SENAL, stroke_width=4)
        r1.permitir_encima = True
        r2 = SurroundingRectangle(F2[4], buff=0.12, color=ESTIMACION, stroke_width=4)
        r2.permitir_encima = True

        with self.narrar("b2"):
            # «El primer trozo»
            self.en("primero")
            self.play(FadeOut(self.F1), F2.animate.move_to([0, 2.8, 0]), run_time=0.5)
            r1.move_to(F2[2])
            r2.move_to(F2[4])
            self.play(FadeIn(r1), run_time=0.3)

            # «cuánto se aparta la variable»
            self.en("apartay")
            self.play(FadeIn(recta), run_time=self.dur(0.5))
            self.play(GrowArrow(aY), run_time=self.dur(0.5))

            # «El segundo es»
            self.en("segundo")
            self.play(FadeOut(r1), FadeIn(r2), run_time=self.dur(0.4))

            # «cuánto se aparta nuestra apuesta»
            self.en("apartaapuesta")
            self.play(GrowArrow(aH), run_time=self.dur(0.5))

            # «Elevamos al cuadrado la suma»
            self.en("elevamos")
            self.play(FadeOut(recta), FadeOut(aY), FadeOut(aH), FadeOut(r2), run_time=0.3)
            self.play(FadeIn(AB, shift=UP * 0.1), run_time=self.dur(0.5))

            # «como a más be al cuadrado»
            self.en("abc")
            self.play(FadeIn(abc, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «el primero al cuadrado»
            self.en("p1")
            self.play(FadeIn(fila[0], shift=UP * 0.1), run_time=self.dur(0.5))

            # «dos veces el producto»
            self.en("p2")
            self.play(FadeIn(fila[1]), FadeIn(fila[2], shift=UP * 0.1), run_time=self.dur(0.6))

            # «el segundo al cuadrado»
            self.en("p3")
            self.play(FadeIn(fila[3]), FadeIn(fila[4], shift=UP * 0.1), run_time=self.dur(0.6))
