"""Escena 06 — Autocorrelación: multiplicar dos cortes del ensemble (cuatro osciladores desfasados)."""
from comun.escena import *


class ProductoDeCortes(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.cos = CuatroCosenos(ancho=6.0, paso=1.45, amp=0.5, centro=(3.5, -0.1))
        self.tab = TablaCortes(["0°", "90°", "180°", "270°"])
        self.c1 = self.cos.corte(0.0, AMBAR)
        self.c2 = self.cos.corte(0.25, TXT)
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        cos = self.cos
        L = Lienzo(ancho=6.6, alto=2.6, t_rango=(0, 1), v_max=2.4, centro=(-3.4, 1.6))
        t = np.linspace(0, 1, 240)
        v = 1.3 * serie(31, 240, 0.93)
        curva = L.curva(t, v, SENAL, 3.5)
        i1, i2 = 72, 168
        rng = np.random.default_rng(8)
        xs = rng.normal(0, 1, 34)
        ys = 0.75 * xs + rng.normal(0, 0.5, 34)
        centro = np.array([3.6, 0.3, 0])
        nube = VGroup(*[Dot(centro + np.array([0.75 * x, 0.75 * y, 0]), radius=0.06, color=SENAL) for x, y in zip(xs, ys)])
        recta = Line(centro + np.array([-1.9, -1.42, 0]), centro + np.array([1.9, 1.42, 0]), color=ESTIMACION, stroke_width=4)
        with self.narrar("b1"):
            # «cuánto vale la señal en un instante»
            self.en("un_inst")
            d1 = Dot(L.p(t[i1], v[i1]), radius=0.1, color=AMBAR)
            v1 = L.vertical(t[i1], AMBAR, 3)
            x1 = formula("x_1", colores={0: AMBAR}, escala=0.8).next_to(d1, UP, buff=0.2)
            self.play(Create(L.base()), Create(curva), run_time=self.dur(0.6), rate_func=linear)
            self.play(Create(v1), FadeIn(d1), FadeIn(x1), run_time=self.dur(0.6))

            # «de otro instante»
            self.en("otro")
            d2 = Dot(L.p(t[i2], v[i2]), radius=0.1, color=TXT)
            v2 = L.vertical(t[i2], TXT, 3)
            q = Text("?", color=AMBAR, weight=BOLD).scale(0.8).next_to(d2, UP, buff=0.2)
            self.play(Create(v2), FadeIn(d2), FadeIn(q), run_time=self.dur(0.6))

            # «En el capítulo anterior»
            self.en("anterior")
            cap7 = etiqueta("capítulo 7", INK, 0.55).move_to([3.6, 3.4, 0])
            self.play(FadeIn(cap7), run_time=0.4)

            # «dos variables se mueven juntas»
            self.en("juntas")
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in nube], lag_ratio=0.03), Create(recta),
                      run_time=self.dur(1.4))

            # «multiplicábamos una por la otra»
            self.en("mult")
            p0 = nube[0]
            marca = Dot(p0.get_center(), radius=0.13, color=AMBAR)
            xy = formula("x", r"\cdot", "y", colores={0: AMBAR, 2: AMBAR}, escala=1.0).move_to([6.0, 2.0, 0])
            self.play(FadeIn(marca, scale=2), FadeIn(xy), run_time=self.dur(0.6))

            # «promediábamos»
            self.en("prom")
            barra = MathTex(r"\overline{x\,y}", color=AMBAR).scale(1.2).move_to([3.6, -2.1, 0])
            self.pop(barra)

            # «la esperanza del producto»
            self.en("esp_prod")
            esp = MathTex(r"E[X\,Y]", color=AMBAR).scale(1.2).move_to([3.6, -2.1, 0])
            self.play(ReplacementTransform(barra, esp), run_time=self.dur(0.6))

            # «dos cortes del ensemble»
            self.en("dos_cortes")
            self.corte()
            self.play(Create(VGroup(*cos.bases, *cos.curvas)), FadeIn(cos.rotulos), Create(self.c1), Create(self.c2),
                      run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        cos, tab = self.cos, self.tab
        with self.narrar("b2"):
            # «en el mismo instante»
            self.en("mismo")
            self.play(self.c2.animate.set_x(float(cos.x(0.0))), FadeIn(tab.armazon()),
                      FadeIn(tab.enc(0, "X(t₁)")), FadeIn(tab.enc(1, "X(t₂)")), run_time=self.dur(0.7))

            # «te igual a cero»
            self.en("t0")
            lab = MathTex(r"t_1=t_2=0", color=TXT).scale(0.9).move_to([3.5, 3.5, 0])
            col0 = [tab.celda(0, i, s) for i, s in enumerate(["1", "0", "−1", "0"])]
            col1 = [tab.celda(1, i, s) for i, s in enumerate(["1", "0", "−1", "0"])]
            self.play(FadeIn(lab), LaggedStart(*[FadeIn(c) for c in col0 + col1], lag_ratio=0.08),
                      run_time=self.dur(0.9))

            # «Los productos son»
            self.en("productos")
            self.play(FadeIn(tab.enc(2, "producto")), run_time=0.4)

            # «uno por uno, cero por cero»
            self.en("prod1")
            prods = [tab.celda(2, 0, "1·1"), tab.celda(2, 1, "0·0")]
            self.play(*[FadeIn(p, shift=DOWN * 0.1) for p in prods], run_time=0.5)

            # «menos uno por menos uno»
            self.en("prod2")
            prods += [tab.celda(2, 2, "(−1)(−1)"), tab.celda(2, 3, "0·0")]
            self.play(*[FadeIn(p, shift=DOWN * 0.1) for p in prods[2:]], run_time=0.5)

            # «uno, cero, uno y cero»
            self.en("res1")
            self.play(*[Transform(p, tab.celda(2, i, s)) for i, (p, s) in enumerate(zip(prods, ["1", "0", "1", "0"]))],
                      run_time=self.dur(0.7))

            # «El promedio es un medio»
            self.en("medio")
            pm = tab.prom(2, "½")
            self.pop(pm)

            # «Ahora»
            self.en("ahora")
            self.play(*[FadeOut(m) for m in col1 + prods], FadeOut(pm), FadeOut(lab), run_time=0.4)

            # «un cuarto de período más tarde»
            self.en("cuarto")
            lab2 = MathTex(r"t_1=0,\;t_2=\tfrac14", color=TXT).scale(0.9).move_to([3.5, 3.5, 0])
            col1 = [tab.celda(1, i, s) for i, s in enumerate(["0", "−1", "0", "1"])]
            self.play(self.c2.animate.set_x(float(cos.x(0.25))), FadeIn(lab2),
                      LaggedStart(*[FadeIn(c) for c in col1], lag_ratio=0.1), run_time=self.dur(0.9))

            # «uno por cero, cero por menos uno»
            self.en("prod3")
            prods = [tab.celda(2, 0, "1·0"), tab.celda(2, 1, "0·(−1)")]
            self.play(*[FadeIn(p, shift=DOWN * 0.1) for p in prods], run_time=0.5)

            # «menos uno por cero y cero por uno»
            self.en("prod4")
            prods += [tab.celda(2, 2, "(−1)·0"), tab.celda(2, 3, "0·1")]
            self.play(*[FadeIn(p, shift=DOWN * 0.1) for p in prods[2:]], run_time=0.5)

            # «Todos cero»
            self.en("todos0")
            self.play(*[Transform(p, tab.celda(2, i, "0")) for i, p in enumerate(prods)], run_time=self.dur(0.6))

            # «El promedio es cero»
            self.en("prom0")
            self.pop(tab.prom(2, "0"))
