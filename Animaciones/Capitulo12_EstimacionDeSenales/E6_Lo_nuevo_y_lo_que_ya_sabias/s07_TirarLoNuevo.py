"""Escena 07 — Predecir es tirar lo impredecible: el error es la varianza de lo tirado."""
from comun.escena import *


class TirarLoNuevo(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.parte_error()
        self.wait(0.6)
        self.parte_parabola()
        self.wait(1.0)
        self.limpiar()

    def parte_error(self):
        F1 = formula("x[n+1]", "=", "f_0", r"\,w[n+1]", "+", r"\text{lo que ya sé}", escala=1.0,
                     colores={0: MEDIDA, 2: ERROR, 3: ERROR, 5: VERDE}).move_to([0, 2.7, 0])
        oculta(F1)
        tj = tijeras().scale(0.45).next_to(F1[3], UP, buff=0.25)
        l_innov = etiqueta("innovación", ERROR, 0.55).next_to(F1[3], DOWN, buff=0.3)
        F2 = formula(r"\hat{x}[n+1]", "=", r"\text{lo que ya sé}", escala=1.0,
                     colores={0: ESTIMACION, 2: VERDE}).move_to([0, 1.2, 0])
        F3 = formula(r"\text{error}", "=", r"\text{varianza de lo tirado}", escala=1.0,
                     colores={0: ERROR}).move_to([0, 0.0, 0])
        F4 = formula("f_0^2", r"\sigma^2", escala=1.0).move_to(F3[2])
        F4.align_to(F3[2], LEFT)
        c_f0 = MathTex(r"f_0=1", color=TXT).scale(0.85).move_to([5.2, 1.3, 0])
        c_s2 = MathTex(r"\sigma^2=2{,}56", color=SENAL).scale(0.85).move_to([5.2, 0.5, 0])
        F5 = formula(r"\text{error}", "=", r"2{,}56", escala=1.6, colores={0: ERROR, 2: ERROR}).move_to([0, -1.7, 0])

        with self.narrar("b1"):
            # «tirar lo que no se puede predecir»
            self.en("tirar")
            self.add(F1)
            self.play(*revelar(*F1), run_time=self.dur(1.0))
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))

            # «la parte que ya sabemos»
            self.en("sabemos")
            self.play(FadeIn(F2, shift=UP * 0.2), run_time=self.dur(0.6))

            # «el error es la varianza de lo tirado»
            self.en("errvar")
            self.play(FadeIn(F3), run_time=self.dur(0.7))

            # «Si la innovación entra»
            self.en("entra")
            self.play(FadeOut(tj), FadeIn(l_innov), run_time=self.dur(0.4))

            # «multiplicada por efe cero»
            self.en("f0")
            self.resaltar(F1[2], color=ERROR)

            # «efe cero al cuadrado por la varianza de la moneda»
            self.en("formula")
            self.play(ReplacementTransform(F3[2], F4[0]), run_time=self.dur(0.7))
            self.play(FadeIn(F4[1], shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Con el eco, efe cero es uno»
            self.en("f01")
            self.play(FadeIn(c_f0), run_time=self.dur(0.4))

            # «tiene varianza dos coma cinco seis»
            self.en("s256")
            self.play(FadeIn(c_s2), run_time=self.dur(0.4))

            # «el error es dos coma cinco seis»
            self.en("e256")
            self.pop(F5)

    def parte_parabola(self):
        par = parabola_l(centro=(-3.6, 1.0), ancho=4.2, alto=2.6, fondo=0.3, color=AMBAR)
        l_par = etiqueta("la parábola del capítulo 10", INK, 0.5).move_to([-3.6, 3.0, 0])
        pmin = Dot(par.L.p(0, 0.3), radius=0.09, color=VERDE)
        l_min = MathTex(r"2{,}56", color=ERROR).scale(0.8).move_to(par.L.p(0, 0) + DOWN * 0.45)
        l_yw = etiqueta("Yule-Walker", AMBAR, 0.55).move_to([3.6, 2.7, 0])
        f_yw = formula(r"\mathbf{R}\,\mathbf{h}", "=", r"\mathbf{r}", escala=0.9).move_to([3.6, 1.9, 0])
        r_yw = formula(r"\text{error}", "=", r"2{,}56", escala=0.9, colores={0: ERROR, 2: ERROR}).move_to([3.6, 1.0, 0])
        igual = MathTex(r"=", color=VERDE).scale(1.8).move_to([0.0, 1.0, 0])
        mat = MathTex(r"\begin{pmatrix}5&2{,}4\\2{,}4&5\end{pmatrix}", color=INK).scale(0.75).move_to([3.6, -0.7, 0])
        f_c = formula(r"f_0^2\,\sigma^2", escala=1.0).move_to([-3.6, -1.7, 0])
        lup = lupa(TXT).scale(0.9).move_to([-2.6, -1.4, 0])
        lup.permitir_encima = True
        for m in lup.get_family():
            m.permitir_encima = True
        f_ig = formula(r"\text{error}", "=", r"\sigma_\varepsilon^2", escala=1.2, colores={0: ERROR}).move_to([0, -3.1, 0])
        marco = SurroundingRectangle(f_ig, color=ERROR, buff=0.2, stroke_width=4)
        puntos = VGroup(*[Dot(par.L.p(x, 0.45 * x * x + 0.3), radius=0.08, color=INK) for x in (-1.5, -1.0, 1.0, 1.5)])

        with self.narrar("b2"):
            # «la parábola del capítulo diez»
            self.en("parab")
            self.corte()
            self.play(Create(par.eje), Create(par.curva), FadeIn(l_par), run_time=self.dur(1.0))

            # «en su punto más bajo»
            self.en("minimo")
            self.play(FadeIn(pmin), FadeIn(l_min), run_time=self.dur(0.5))

            # «las ecuaciones de Yule-Walker»
            self.en("yw")
            self.play(FadeIn(l_yw), FadeIn(f_yw), FadeIn(r_yw), run_time=self.dur(0.7))

            # «No es casualidad»
            self.en("nocasual")
            self.pop(igual)

            # «con matrices»
            self.en("matrices")
            self.play(FadeIn(mat), run_time=self.dur(0.5))

            # «de un vistazo»
            self.en("vistazo")
            self.play(FadeIn(f_c), run_time=self.dur(0.4))
            self.play(FadeIn(lup, shift=LEFT * 0.3), run_time=self.dur(0.4))

            # «un error igual a la varianza de la innovación»
            self.en("igual")
            self.play(FadeOut(lup), FadeIn(f_ig), Create(marco), run_time=self.dur(0.7))

            # «ninguna otra puede mejorarlo»
            self.en("ninguna")
            self.play(FadeIn(puntos, lag_ratio=0.2), run_time=self.dur(0.6))
            self.resaltar(pmin, color=VERDE)
