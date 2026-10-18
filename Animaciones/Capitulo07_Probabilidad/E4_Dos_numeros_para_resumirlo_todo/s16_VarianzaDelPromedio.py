"""Escena 16 — La varianza del promedio de n medidas independientes es σ²/n."""
from comun.escena import *


class VarianzaDelPromedio(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        self.suma()
        self.promedio()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def suma(self):
        disp = MathTex(r"\mathrm{Var}(\bar X_n)", "=", "?", color=TXT).scale(1.4).move_to([0, 3.3, 0])
        rots = ["X_1", "X_2", "X_3", r"\cdots", "X_n"]
        cajas = VGroup()
        for i, r in enumerate(rots):
            if r == r"\cdots":
                cajas.add(MathTex(r, color=INK).scale(1.0))
            else:
                cajas.add(VGroup(Square(side_length=0.9, color=SENAL, stroke_width=3).set_fill(SENAL, 0.15),
                                 MathTex(r, color=TXT).scale(0.9)))
        cajas.arrange(RIGHT, buff=0.5).move_to([0, 2.0, 0])
        sig = VGroup(*[MathTex(r"\sigma^2", color=AMBAR).scale(0.8).next_to(c, DOWN, buff=0.15)
                       for c in cajas if not isinstance(c, MathTex)])
        v_suma = MathTex(r"\mathrm{Var}(X_1+\cdots+X_n)", color=TXT).scale(1.2).move_to([0, 0.1, 0])
        s_var = MathTex("=", r"\sigma^2+\cdots+\sigma^2", color=TXT).scale(1.2).move_to([0, -0.95, 0])
        dos_ep = Text("(Lo demostramos en el episodio 6)", color=INK).scale(0.55).move_to([0, -1.8, 0])
        sello_ = sello("De momento", AMBAR).scale(0.8).move_to([5.0, -0.95, 0])
        n_s2 = MathTex("=", r"n\,\sigma^2", color=AMBAR).scale(1.5).move_to([0, -2.9, 0])
        with self.narrar("b1"):
            # «cuánto se dispersa el promedio»
            self.en("dispersa")
            self.play(FadeIn(disp, shift=DOWN * 0.15), run_time=self.dur(1.0))
            # «independientes»
            self.en("indep")
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in cajas], lag_ratio=0.12), run_time=self.dur(0.9))
            # «la varianza de su suma»
            self.en("var_suma")
            self.play(FadeIn(v_suma, shift=DOWN * 0.15), run_time=self.dur(1.0))
            # «la suma de sus varianzas»
            self.en("suma_var")
            self.play(FadeIn(s_var, shift=DOWN * 0.15), run_time=self.dur(1.2))
            # «dentro de dos episodios»
            self.en("dos_ep")
            self.play(FadeIn(dos_ep), run_time=self.dur(0.7))
            # «créetelo»
            self.en("creetelo")
            self.pop(sello_)
            # «n medidas de varianza sigma cuadrado»
            self.en("n_medidas")
            self.play(LaggedStart(*[FadeIn(s) for s in sig], lag_ratio=0.12), run_time=self.dur(1.0))
            # «n por sigma cuadrado»
            self.en("n_sigma2")
            self.play(FadeIn(n_s2, shift=DOWN * 0.15), run_time=self.dur(0.8))
            self.play(Create(SurroundingRectangle(n_s2, color=AMBAR, buff=0.2)), run_time=0.4)

    # ---------------------------------------------------------------- b2
    def promedio(self):
        prom = MathTex(r"\bar X_n", "=", r"\frac{X_1+\cdots+X_n}{n}", color=TXT).scale(1.3).move_to([0, 3.2, 0])
        divide = MathTex(r"\mathrm{Var}\!\left(\frac{X}{c}\right)", color=TXT).scale(1.2).move_to([-4.3, 1.5, 0])
        c2 = MathTex("=", r"\frac{\mathrm{Var}(X)}{c^2}", color=TXT).scale(1.2).next_to(divide, RIGHT, buff=0.3)
        d_lin = Line([3.9, 1.5, 0], [4.9, 1.5, 0], color=AMBAR, stroke_width=6)
        d_cua = Square(side_length=1.0, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.3).move_to([6.0, 1.5, 0])
        coc = MathTex(r"\frac{n\,\sigma^2}{n^2}", color=TXT).scale(1.4).move_to([-1.2, -0.3, 0])
        sn = MathTex("=", r"\frac{\sigma^2}{n}", color=AMBAR).scale(1.6).next_to(coc, RIGHT, buff=0.3)
        etiq = MathTex("n", "=", color=TXT).scale(1.2).move_to([-4.6, -2.4, 0])
        cnt = Integer(2, group_with_commas=False, color=AMBAR).scale(1.2).next_to(etiq, RIGHT, buff=0.2)
        ancha = campana7(3.0, -3.5, 1.7, SENAL, ancho=0.9, alto=1.8)
        estrecha = campana7(3.0, -3.5, 0.25, SENAL, ancho=0.9, alto=1.8)
        base = Line([-0.8, -3.5, 0], [6.8, -3.5, 0], color=INK, stroke_width=2)
        with self.narrar("b2"):
            # «la suma dividida entre n»
            self.en("prom")
            self.corte()
            self.play(FadeIn(prom, shift=DOWN * 0.15), run_time=self.dur(1.2))
            # «divides una variable entre un número»
            self.en("divides")
            self.play(FadeIn(divide, shift=DOWN * 0.15), run_time=self.dur(1.0))
            # «se divide entre ese número al cuadrado»
            self.en("c2")
            self.play(FadeIn(c2, shift=LEFT * 0.15), run_time=self.dur(1.0))
            # «mide distancias al cuadrado»
            self.en("dist2")
            self.play(Create(d_lin), FadeIn(d_cua), run_time=self.dur(0.9))
            # «n por sigma cuadrado dividido entre n al cuadrado»
            self.en("cociente")
            self.play(FadeIn(coc, shift=DOWN * 0.15), run_time=self.dur(1.5))
            # «sigma cuadrado dividido entre n»
            self.en("sn")
            self.play(FadeIn(sn, shift=LEFT * 0.15), run_time=self.dur(0.8))
            self.play(Create(SurroundingRectangle(VGroup(coc, sn), color=AMBAR, buff=0.2)), run_time=0.4)
            # «Cuantas más medidas»
            self.en("mas")
            self.play(FadeIn(etiq), FadeIn(cnt), Create(base), Create(ancha), run_time=0.5)
            self.play(ChangeDecimalToValue(cnt, 100), run_time=self.dur(1.2), rate_func=linear)
            # «menos se dispersa el promedio»
            self.en("menos")
            self.play(Transform(ancha, estrecha), run_time=self.dur(1.4))
