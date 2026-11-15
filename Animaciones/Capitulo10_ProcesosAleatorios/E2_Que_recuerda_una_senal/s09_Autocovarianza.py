"""Escena 09 — Autocovarianza: restar las medias, la fórmula práctica C = R − μμ y el caso de la moneda."""
from comun.escena import *


class Autocovarianza(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        w1 = self.palabra("medias restadas", AMBAR, 1.2).move_to([0, 3.3, 0])
        x12 = formula("X(t_1)", r"\times", "X(t_2)", escala=1.2).move_to([0, 2.0, 0])
        x12r = formula(r"\big(X(t_1)-\mu(t_1)\big)", r"\times", r"\big(X(t_2)-\mu(t_2)\big)",
                       escala=1.0).move_to([0, 2.0, 0])
        Fc = formula("C_{XX}", "(", "t_1", ",", "t_2", ")", "=", "E", r"\big[", r"\big(X(t_1)-\mu(t_1)\big)",
                     r"\big(X(t_2)-\mu(t_2)\big)", r"\big]", escala=0.8, colores={0: AMBAR}).move_to([0, 0.6, 0])
        Fa = formula("=", "E[X(t_1)X(t_2)]", r"-\mu(t_1)E[X(t_2)]", escala=0.85).move_to([0, -0.5, 0])
        Fb = formula(r"-\mu(t_2)E[X(t_1)]", r"+\mu(t_1)\mu(t_2)", escala=0.85).move_to([0, -1.3, 0])
        Fa2 = formula("=", "R_{XX}(t_1,t_2)", r"-\mu(t_1)\mu(t_2)", escala=0.85).move_to([0, -0.5, 0])
        Fb2 = formula(r"-\mu(t_2)\mu(t_1)", r"+\mu(t_1)\mu(t_2)", escala=0.85).move_to([0, -1.3, 0])
        fin = formula("C_{XX}(t_1,t_2)", "=", "R_{XX}(t_1,t_2)", "-", r"\mu(t_1)\mu(t_2)", escala=1.0,
                      colores={0: AMBAR}).move_to([0, -1.1, 0])
        cap7 = etiqueta("como en el capítulo 7", INK, 0.55).move_to([0, -3.2, 0])
        with self.narrar("b1"):
            # «con las medias restadas»
            self.en("restadas")
            self.pop(w1)

            # «Antes de multiplicar»
            self.en("antes")
            self.play(FadeIn(x12, shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «se le resta la media»
            self.en("resta")
            self.play(ReplacementTransform(x12, x12r), run_time=self.dur(1.0))

            # «la autocovarianza»
            self.en("autocov")
            w2 = self.palabra("autocovarianza", AMBAR, 1.2).move_to([0, 3.3, 0])
            self.play(FadeOut(w1), run_time=0.2)
            self.pop(w2)

            # «ce sub equis equis de te uno, te dos»
            self.en("c")
            self.play(FadeIn(Fc[0:6], shift=DOWN * 0.15), run_time=self.dur(0.6))
            self.play(FadeIn(Fc[6:], shift=DOWN * 0.15), run_time=self.dur(0.8))

            # «desarrollando el producto»
            self.en("desarrolla")
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.1) for p in (*Fa, *Fb)], lag_ratio=0.3),
                      run_time=self.dur(1.4))

            # «la linealidad»
            self.en("lineal")
            self.play(*[ReplacementTransform(a, b) for a, b in zip((*Fa, *Fb), (*Fa2, *Fb2))], run_time=self.dur(1.0))

            # «la fórmula práctica»
            self.en("practica")
            self.play(FadeOut(Fa2), FadeOut(Fb2), run_time=0.3)
            self.play(FadeIn(fin, shift=UP * 0.15), run_time=self.dur(0.6))

            # «la autocorrelación menos el producto»
            self.en("formula")
            self.play(FadeIn(cap7), fin[2].animate.set_color(AMBAR), fin[4].animate.set_color(ESTIMACION),
                      run_time=self.dur(0.8))

            # «las dos medias»
            self.en("dos_medias")
            self.play(fin[4].animate.scale(1.2), run_time=0.4)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        cos = CuatroCosenos(ancho=8.0, paso=0.8, amp=0.3, centro=(0.8, 1.9))
        rng = np.random.default_rng(6)
        tira = tira_pm1(rng.choice([-1, 1], 9), lado=0.66).move_to([0, 2.3, 0])
        pares = ["(+,+)", "(+,-)", "(-,+)", "(-,-)"]
        prods = ["+1", "−1", "−1", "+1"]
        xs = [-4.2, -1.4, 1.4, 4.2]
        with self.narrar("b2"):
            # «los cuatro osciladores la media es cero»
            self.en("osc0")
            self.corte()
            planas = [Line(b.get_start(), b.get_end(), color=AMBAR, stroke_width=5) for b in cos.bases]
            self.play(Create(VGroup(*cos.bases, *cos.curvas)), FadeIn(cos.rotulos), run_time=self.dur(0.9))
            self.play(LaggedStart(*[Create(p) for p in planas], lag_ratio=0.1), run_time=self.dur(0.6))

            # «autocovarianza y autocorrelación coinciden»
            self.en("coinciden")
            igual = formula("C_{XX}", "=", "R_{XX}", escala=1.4, colores={0: AMBAR, 2: AMBAR}).move_to([0.8, -0.6, 0])
            self.pop(igual)

            # «Veamos la moneda»
            self.en("moneda")
            self.corte()
            c = moneda("", AMBAR).scale(1.0).move_to([-5.4, 2.3, 0])
            self.pop(c)
            self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.1) for x in tira.celdas], lag_ratio=0.1), run_time=self.dur(1.0))

            # «Su media también es cero»
            self.en("moneda0")
            plana2 = Line(tira.get_left() + LEFT * 0.1, tira.get_right() + RIGHT * 0.1, color=AMBAR, stroke_width=5)
            mu = formula(r"\mu", "=", "0", colores={0: AMBAR}, escala=1.0).move_to([5.5, 2.3, 0])
            self.play(Create(plana2), run_time=0.4)
            self.pop(mu)

            # «En el mismo instante»
            self.en("mismo")
            marco = SurroundingRectangle(tira.celdas[4], color=AMBAR, buff=0.06, stroke_width=4)
            self.play(Create(marco), run_time=0.4)

            # «vale uno»
            self.en("vale1")
            v1 = formula(r"(\pm1)^{2}", "=", "1", colores={2: AMBAR}, escala=1.2).move_to([0, 1.0, 0])
            self.pop(v1)

            # «cuatro parejas»
            self.en("parejas")
            self.play(FadeOut(marco), FadeOut(v1), run_time=0.3)
            pr = [formula(p, escala=1.1).move_to([x, -0.2, 0]) for p, x in zip(pares, xs)]
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.1) for p in pr], lag_ratio=0.15), run_time=self.dur(0.9))

            # «más por más»
            self.en("mm")
            res = [Text(s, color=TXT, weight=BOLD).scale(0.8).move_to([x, -1.3, 0]) for s, x in zip(prods, xs)]
            self.play(pr[0].animate.set_color(AMBAR), FadeIn(res[0], shift=DOWN * 0.1), run_time=0.4)

            # «más por menos, menos por más»
            self.en("mixtas")
            self.play(pr[1].animate.set_color(AMBAR), pr[2].animate.set_color(AMBAR),
                      FadeIn(res[1], shift=DOWN * 0.1), FadeIn(res[2], shift=DOWN * 0.1), run_time=0.5)

            # «menos por menos»
            self.en("menosmenos")
            self.play(pr[3].animate.set_color(AMBAR), FadeIn(res[3], shift=DOWN * 0.1), run_time=0.4)

            # «Los productos se cancelan»
            self.en("cancelan")
            suma = formula("+1", "-1", "-1", "+1", "=", "0", escala=1.4, colores={5: AMBAR}).move_to([0, -2.6, 0])
            self.pop(suma)
