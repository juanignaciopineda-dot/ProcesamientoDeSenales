"""Escena 04 — La proyección, otra vez: el dibujo del capítulo 8 y la fórmula de la estimación lineal."""
from comun.escena import *


class ProyeccionDeFlechas(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        sello_ = caja("Cap. 8 · estimación lineal", AZUL, alto=0.75, scale=0.55).move_to([0, 3.45, 0])
        lineal = formula(r"\hat y", "=", r"a\,x", "+", "b", escala=1.0, colores={0: ESTIMACION}).move_to([3.6, 2.3, 0])
        cx = Circle(radius=0.4, color=SENAL, stroke_width=3).set_fill(SENAL, 0.15).move_to([-4.6, 2.3, 0])
        cy = Circle(radius=0.4, color=ESTIMACION, stroke_width=3).set_fill(ESTIMACION, 0.15).move_to([-2.4, 2.3, 0])
        mx = MathTex("X", color=TXT).scale(0.8).move_to(cx)
        my = MathTex("Y", color=TXT).scale(0.8).move_to(cy)
        entre = Arrow(cx.get_right(), cy.get_left(), buff=0.1, color=INK, stroke_width=4)

        F = Flechas(origen=(-5.6, -2.0), largo=4.4, angulo=53.13)
        self.F = F
        origen = Dot(F.o, radius=0.09, color=TXT)
        centrada = formula(r"\tilde x", "=", "x", "-", r"\mu", escala=1.3).move_to([3.6, 0.3, 0])
        q = Text("?", color=ESTIMACION, weight=BOLD).scale(0.8).next_to(F.fin_futuro, UR, buff=0.1)
        multiplos = VGroup(*[Dot(F.o + RIGHT * 3.6 * t, radius=0.07, color=AMBAR) for t in (0.25, 0.55, 0.8, 1.15, 1.4)])
        guia = DashedLine(F.o, F.o + RIGHT * 5.4, color=INK, stroke_width=2)
        lp = MathTex(r"x[n_0]", color=SENAL).scale(0.8).next_to(F.fin_presente, RIGHT, buff=0.15)
        lf = MathTex(r"x[n_0+m]", color=TXT).scale(0.8).next_to(F.fin_futuro, UR, buff=0.1)
        ls = MathTex(r"\hat x", color=ESTIMACION).scale(0.8).next_to((F.o + F.fin_sombra) / 2, DOWN, buff=0.22)
        le = Text("error", color=ERROR).scale(0.45).next_to((F.fin_sombra + F.fin_futuro) / 2, RIGHT, buff=0.25)
        self.lp = lp

        with self.narrar("b1"):
            # «capítulo de estimación»
            self.en("cap8")
            self.pop(sello_)

            # «la mejor estimación lineal»
            self.en("lineal")
            self.play(FadeIn(lineal), run_time=0.6)

            # «a partir de otra»
            self.en("otra")
            self.play(FadeIn(cx), FadeIn(mx), Create(entre), FadeIn(cy), FadeIn(my), run_time=0.8)

            # «con flechas»
            self.en("flechas")
            self.play(FadeOut(lineal), FadeOut(VGroup(cx, mx, cy, my, entre)), run_time=0.3)
            self.play(FadeIn(origen), Create(F.presente), Create(F.futuro), run_time=self.dur(0.9))

            # «variables centradas»
            self.en("centradas")
            self.play(FadeIn(centrada), run_time=0.6)

            # «Estimar el futuro»
            self.en("estimar")
            self.play(FadeIn(q), run_time=0.4)

            # «el múltiplo»
            self.en("multiplo")
            self.play(Create(guia), FadeIn(multiplos, lag_ratio=0.3), run_time=self.dur(1.0))

            # «flecha del presente»
            self.en("presente")
            self.play(FadeIn(lp), FadeOut(guia), FadeOut(multiplos), run_time=0.5)

            # «flecha del futuro»
            self.en("futuro")
            self.play(ReplacementTransform(q, lf), run_time=0.5)

            # «la proyección»
            self.en("proyeccion")
            self.play(Create(F.sombra), FadeIn(ls), run_time=self.dur(0.8))

            # «perpendicular al dato»
            self.en("perp")
            self.play(Create(F.error), Create(F.recto), FadeIn(le), run_time=self.dur(0.8))

    def parte_b2(self):
        yh = MathTex(r"\hat y", color=ESTIMACION)
        eq = MathTex("=", color=TXT)
        mu = MathTex(r"\mu_Y", color=TXT)
        mas = MathTex("+", color=TXT)
        fr = fraccion(MathTex(r"\sigma_{XY}", color=TXT), MathTex(r"\sigma_X^2", color=TXT))
        par = MathTex(r"(x-\mu_X)", color=TXT)
        fila = VGroup(yh, eq, mu, mas, fr, par).arrange(RIGHT, buff=0.18).scale(1.2).move_to([3.6, 1.6, 0])
        mm = MathTex("MMSE", color=ERROR)
        eq2 = MathTex("=", color=TXT)
        s2 = MathTex(r"\sigma_Y^2", color=TXT)
        r2 = MathTex(r"(1-\rho^2)", color=TXT)
        fila2 = VGroup(mm, eq2, s2, r2).arrange(RIGHT, buff=0.18).scale(1.2).move_to([3.6, -1.0, 0])

        with self.narrar("b2"):
            # «De esa proyección»
            self.en("fml")
            self.play(FadeIn(yh), run_time=0.4)

            # «La estimación es»
            self.en("estima")
            self.play(FadeIn(eq), run_time=0.3)

            # «la media de lo que se quiere adivinar»
            self.en("mu")
            self.play(FadeIn(mu), run_time=0.4)

            # «la covarianza entre las dos variables»
            self.en("cov")
            self.play(FadeIn(mas), FadeIn(fr.num), Create(fr.barra), run_time=0.6)

            # «la varianza del dato»
            self.en("var")
            self.play(FadeIn(fr.den), run_time=0.5)

            # «se aparta de su media»
            self.en("aparta")
            self.play(FadeIn(par), run_time=0.5)

            # «el error cuadrático medio»
            self.en("mmse")
            self.play(FadeIn(mm), FadeIn(eq2), run_time=0.5)

            # «uno menos rho al cuadrado»
            self.en("rho2")
            self.play(FadeIn(s2), run_time=0.3)
            self.play(FadeIn(r2), run_time=0.4)
