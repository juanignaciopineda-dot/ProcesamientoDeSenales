"""Escena 12 — El caso fácil: la moneda es i.i.d. y su conjunta es un producto."""
from comun.escena import *

CONJUNTA = r"f_{X(t_1),X(t_2),X(t_3),\ldots,X(t_n)}(x_1,x_2,x_3,\ldots,x_n)"


class IidMoneda(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.tirada()
        self.sigla()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1: la moneda
    def tirada(self):
        valores = [-1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1]
        with self.narrar("b1"):
            # «imposible de manejar»
            self.en("imposible")
            f = formula(CONJUNTA, color=TXT, escala=0.8).move_to([0, 1.2, 0])
            self.play(FadeIn(f), run_time=0.4)
            self.play(f.animate.scale(1.35), run_time=self.dur(1.6))
            tach = tachar(f)
            self.play(Create(tach), run_time=self.dur(0.5))

            # «la moneda»
            self.en("moneda")
            self.play(FadeOut(f), FadeOut(tach), run_time=0.3)
            c = moneda("", AMBAR).scale(1.4).move_to([-5.8, 3.0, 0])
            self.pop(c)
            self.play(Rotate(c, angle=PI, axis=UP), run_time=0.5)

            # «independiente de las demás»
            self.en("indep")
            tira = tira_pm1(valores, lado=0.8, escala_txt=0.5).move_to([0, 0.3, 0])
            llave = Brace(VGroup(*tira.celdas), DOWN, buff=0.15, color=INK)
            l_ind = Text("cada una independiente", color=INK).scale(0.6).next_to(llave, DOWN, buff=0.15)
            self.play(LaggedStart(*[FadeIn(cl, shift=DOWN * 0.2) for cl in tira.celdas], lag_ratio=0.15),
                      run_time=self.dur(1.6))
            self.play(GrowFromCenter(llave), FadeIn(l_ind), run_time=self.dur(0.5))

            # «las mismas probabilidades»
            self.en("mismas")
            l_mis = Text("siempre ½ | ½", color=AMBAR, weight=BOLD).scale(0.7).move_to(l_ind)
            self.play(ReplacementTransform(l_ind, l_mis), run_time=self.dur(0.5))

            # «más uno, más uno y menos uno»
            self.en("trio")
            self.play(FadeOut(llave), FadeOut(l_mis), run_time=0.25)
            trio = VGroup(*tira.celdas[4:7])
            marco = SurroundingRectangle(trio, color=AMBAR, buff=0.08, corner_radius=0.1, stroke_width=5)
            self.play(Create(marco), run_time=self.dur(0.6))

            # «Un medio por un medio por un medio»
            self.en("producto")
            prod = Text("½ · ½ · ½", color=AMBAR, weight=BOLD).scale(1.1).next_to(marco, DOWN, buff=0.4)
            self.pop(prod)

            # «un octavo»
            self.en("octavo")
            res = Text("½ · ½ · ½ = ⅛", color=AMBAR, weight=BOLD).scale(1.1).move_to(prod)
            self.play(ReplacementTransform(prod, res), run_time=self.dur(0.5))

            # «el producto de las de cada instante»
            self.en("prod")
            F = formula("P(x_1,x_2,x_3)", "=", "P(x_1)", "P(x_2)", "P(x_3)", escala=1.3,
                        colores={2: AMBAR, 3: AMBAR, 4: AMBAR}).move_to([0, -2.7, 0])
            self.play(FadeIn(F[0:2]), run_time=0.4)
            self.play(LaggedStart(*[FadeIn(F[i], shift=UP * 0.15) for i in (2, 3, 4)], lag_ratio=0.3),
                      run_time=self.dur(1.2))

    # ---------------------------------------------------------------- b2: i.i.d. y la memoria
    def sigla(self):
        L = Lienzo(ancho=10.0, alto=2.6, t_rango=(0, 1), v_max=2.6, centro=(0, -0.9))
        t = np.linspace(0, 1, 240)
        with self.narrar("b2"):
            self.corte()
            # «i.i.d.»
            self.en("iid")
            sig = self.palabra("i.i.d.", AMBAR, 2.2).move_to([0, 1.4, 0])
            self.pop(sig)

            # «independiente e idénticamente distribuido»
            self.en("despliega")
            l1 = Text("independiente", color=TXT, weight=BOLD).scale(0.9).move_to([0, 1.3, 0])
            l2 = Text("idénticamente distribuido", color=TXT, weight=BOLD).scale(0.9).move_to([0, 0.3, 0])
            self.play(sig.animate.scale(0.5).move_to([0, 3.1, 0]), run_time=0.5)
            self.pop(l1, sonido=None)
            self.pop(l2, sonido=None)

            # «el modelo de ruido más sencillo»
            self.en("ruido")
            self.play(FadeOut(l1), FadeOut(l2), run_time=0.25)
            base = L.base()
            c_r = L.curva(t, serie(61, 240, 0.0) * 0.75, RUIDO, 3.0)
            self.play(Create(base), Create(c_r), run_time=self.dur(1.6), rate_func=linear)

            # «las señales interesantes»
            self.en("interesantes")
            c_s = L.curva(t, serie(62, 240, 0.97) * 0.9, MEDIDA, 3.5)
            self.play(Transform(c_r, c_s), run_time=self.dur(1.1))

            # «tienen memoria»
            self.en("memoria")
            ts = (0.3, 0.38, 0.46)
            dots = VGroup(*[Dot(L.p(x, float(np.interp(x, t, serie(62, 240, 0.97) * 0.9))), radius=0.12, color=AMBAR)
                            for x in ts])
            arcos = VGroup(*[CurvedArrow(dots[i].get_center() + UP * 0.15, dots[i + 1].get_center() + UP * 0.15,
                                         angle=-PI / 2.5, color=AMBAR, stroke_width=4) for i in range(2)])
            self.play(FadeIn(dots), LaggedStart(*[Create(a) for a in arcos], lag_ratio=0.4), run_time=self.dur(1.3))

            # «inmanejable»
            self.en("inmanejable")
            self.play(FadeOut(c_r), FadeOut(dots), FadeOut(arcos), FadeOut(base), run_time=0.25)
            f = formula(CONJUNTA, color=TXT, escala=1.05).move_to([0, 0.5, 0])
            self.play(FadeIn(f), run_time=0.3)
            tach = tachar(f)
            self.play(Create(tach), run_time=self.dur(0.5))

            # «Hay que resumir»
            self.en("resumir")
            self.play(FadeOut(f), FadeOut(tach), run_time=0.25)
            cur = L.curva(t, serie(62, 240, 0.97) * 0.9, MEDIDA, 3.5).shift(UP * 1.8)
            self.play(Create(cur), run_time=self.dur(1.2), rate_func=linear)
            c_media = caja("media", AMBAR, 2.2, 0.9, 0.7).move_to([-2.4, -2.3, 0])
            c_var = caja("varianza", AMBAR, 2.6, 0.9, 0.7).move_to([2.4, -2.3, 0])
            self.play(FadeIn(c_media, shift=UP * 0.2), FadeIn(c_var, shift=UP * 0.2), run_time=self.dur(0.6))

            # «su media y su varianza»
            self.en("resumen")
            mu = formula(r"\mu", color=AMBAR, escala=1.4).move_to([-2.4, -3.35, 0])
            sg = formula(r"\sigma^2", color=AMBAR, escala=1.4).move_to([2.4, -3.35, 0])
            self.play(cur.animate.scale(0.45).move_to([0, 0.2, 0]).set_stroke(opacity=0.5), run_time=self.dur(0.6))
            self.pop(mu, sg)
