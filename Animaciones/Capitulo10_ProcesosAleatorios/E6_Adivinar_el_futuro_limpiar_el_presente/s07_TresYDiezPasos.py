"""Escena 07 — Tres y diez pasos adelante: el predictor tira hacia la media y la predicción tiene un horizonte."""
from comun.escena import *


class TresYDiezPasos(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.P = PanelSensor(centro=(-2.8, 0.2), ancho=6.2, alto=3.2, n=44, n0=30)
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        P, n0 = self.P, self.P.n0
        self.dato = P.punto(n0, 3.0, TXT, 0.1)
        self.lm = Text("m = 3", color=AMBAR, weight=BOLD).scale(0.8).move_to([-2.8, 2.45, 0])
        hueco = Circle(radius=0.09, color=INK, stroke_width=3).move_to(P.p(n0 + 3, 1.2))
        rho = MathTex(r"\rho", "=", r"0{,}6^3", "=", "0{,}216", color=TXT).scale(1.25).move_to([4.0, 3.0, 0])
        rho[0].set_color(AMBAR)
        cuenta = MathTex("20", "+", "0{,}216", r"\cdot", "3", color=TXT).scale(1.25).move_to([4.0, 2.0, 0])
        xh = MathTex(r"\hat x", r"\approx", num_tex(20.65), color=ESTIMACION).scale(1.45).move_to([4.0, 1.0, 0])
        mm = MathTex("MMSE", "=", "4", r"(1-0{,}216^2)", color=TXT).scale(1.0).move_to([4.0, -0.2, 0])
        mm[0].set_color(ERROR)
        e381 = MathTex(r"\approx", num_tex(3.81), color=ERROR).scale(1.45).move_to([4.0, -1.0, 0])
        dpred = P.punto(n0 + 3, 0.65, AMBAR, 0.1)
        b_con = Line(P.p(n0 + 3, 0.65 - 1.95), P.p(n0 + 3, 0.65 + 1.95), color=AMBAR, stroke_width=9, stroke_opacity=0.5)
        b_sin = Line(P.p(n0 + 4.4, -2.0), P.p(n0 + 4.4, 2.0), color=INK, stroke_width=9, stroke_opacity=0.4)
        self.col1 = VGroup(rho, cuenta, xh, mm, e381)
        self.obj1 = VGroup(hueco, dpred, b_con, b_sin)

        with self.narrar("b1"):
            # «Tres pasos adelante»
            self.en("paso3")
            self.play(Create(P.media), FadeIn(P.rotulo_media), Create(P.pasado), FadeIn(self.dato), FadeIn(self.lm),
                      FadeIn(hueco), run_time=self.dur(1.0))

            # «cero coma seis al cubo»
            self.en("cubo")
            self.play(FadeIn(rho[:3]), run_time=0.5)

            # «cero coma dos uno seis»
            self.en("r216")
            self.play(FadeIn(rho[3:]), run_time=0.5)

            # «veinte más cero coma dos uno seis por tres»
            self.en("cuenta")
            self.play(FadeIn(cuenta), run_time=0.6)

            # «unos veinte coma seis cinco grados»
            self.en("p2065")
            self.play(ReplacementTransform(hueco, dpred), FadeIn(xh), run_time=0.6)

            # «cuatro por uno menos»
            self.en("ecm")
            self.play(FadeIn(mm), run_time=0.6)

            # «tres coma ocho uno»
            self.en("e381")
            self.pop(e381)

            # «ya casi no ayuda»
            self.en("poco")
            self.play(FadeIn(b_con), FadeIn(b_sin), run_time=0.5)

    def parte_b2(self):
        P, n0 = self.P, self.P.n0
        lm10 = Text("m = 10", color=AMBAR, weight=BOLD).scale(0.8).move_to([-2.8, 2.45, 0])
        hueco = Circle(radius=0.09, color=INK, stroke_width=3).move_to(P.p(n0 + 10, 1.0))
        rho = MathTex(r"0{,}6^{10}", r"\approx", "0{,}006", color=TXT).scale(1.25).move_to([4.0, 3.0, 0])
        xh = MathTex(r"\hat x", r"\approx", num_tex(20.02), color=ESTIMACION).scale(1.45).move_to([4.0, 1.6, 0])
        mm = MathTex("MMSE", r"\approx", "4", color=TXT).scale(1.45).move_to([4.0, 0.4, 0])
        mm[0].set_color(ERROR)
        dmed = P.punto(n0 + 10, 0.0, AMBAR, 0.1)
        b_sin = Line(P.p(n0 + 10, -2.0), P.p(n0 + 10, 2.0), color=INK, stroke_width=9, stroke_opacity=0.4)
        veinte = Text("20 °C", color=AMBAR, weight=BOLD).scale(1.5).move_to([4.0, -1.1, 0])

        with self.narrar("b2"):
            # «Diez pasos adelante»
            self.en("paso10")
            self.play(FadeOut(self.col1), FadeOut(self.obj1), ReplacementTransform(self.lm, lm10), run_time=0.4)
            self.play(FadeIn(hueco), run_time=0.3)

            # «Cero coma seis elevado a diez»
            self.en("elev")
            self.play(FadeIn(rho[0]), run_time=0.4)

            # «unas seis milésimas»
            self.en("mil")
            self.play(FadeIn(rho[1:]), run_time=0.4)

            # «prácticamente la media»
            self.en("media")
            self.play(ReplacementTransform(hueco, dmed), run_time=0.5)

            # «veinte coma cero dos»
            self.en("p2002")
            self.play(FadeIn(xh), run_time=0.5)

            # «prácticamente cuatro»
            self.en("e4")
            self.play(FadeIn(mm), FadeIn(b_sin), run_time=0.5)

            # «Da igual lo que marque ahora»
            self.en("igual")
            self.play(self.dato.animate.set_fill(TXT, 0.15).set_stroke(opacity=0.15), run_time=0.5)

            # «la mejor apuesta es veinte grados»
            self.en("veinte")
            self.pop(veinte)
        self.lm = lm10
        self.col2 = VGroup(rho, xh, mm, veinte)
        self.obj2 = VGroup(dmed, b_sin)

    def parte_b3(self):
        P, n0 = self.P, self.P.n0
        ms = np.arange(0, 11)
        pred = 3.0 * 0.6 ** ms
        curva = P.L.curva(n0 + ms, pred, AMBAR, 4)
        bd = banda(P.L, n0 + ms, pred, 2.0 * np.sqrt(1 - 0.36 ** ms), AMBAR, 0.2)
        hor = DashedLine(P.p(n0 + 8, -4.6), P.p(n0 + 8, 4.6), color=INK, stroke_width=2.5)
        rh = Text("horizonte", color=INK).scale(0.45).next_to(hor, UP, buff=0.1)
        pal = Palitos(range(6), [1, .6, .36, .22, .13, .08], ancho=3.0, alto=1.2, v_max=1.0, centro=(4.6, 2.3))
        mon = moneda("±1", RUIDO).scale(0.6).move_to([2.6, -0.5, 0])
        lmon = Text("horizonte 0", color=TXT).scale(0.5).move_to([4.9, -0.5, 0])
        x_mon = cruz(ROJO, 0.3).move_to([6.5, -0.5, 0])
        bat = pila_icono(AMBAR).scale(0.9).move_to([2.6, -1.8, 0])
        lbat = Text("horizonte ∞", color=TXT).scale(0.5).move_to([4.9, -1.8, 0])
        plana = Line([2.0, -2.7, 0], [6.6, -2.7, 0], color=AMBAR, stroke_width=5)
        dplana = Dot([2.0, -2.7, 0], radius=0.11, color=AMBAR)

        F = Flechas(origen=(-4.6, -1.6), largo=3.6, angulo=53.13)
        flecha_a = Arrow([0.4, 0.0, 0], [2.2, 0.0, 0], buff=0, color=AMBAR, stroke_width=6)
        q = Text("¿filtrar?", color=AMBAR, weight=BOLD).scale(0.7).move_to([3.5, 0.0, 0])
        Ln = Lienzo(ancho=4.6, alto=1.5, t_rango=(0, 1), v_max=2.4, centro=(4.2, 1.9))
        Lc = Lienzo(ancho=4.6, alto=1.5, t_rango=(0, 1), v_max=2.4, centro=(4.2, -2.3))
        t = np.linspace(0, 1, 200)
        limpia = 1.0 * serie(91, 200, 0.97)
        ruido = 0.55 * np.random.default_rng(5).normal(0, 1, 200)
        c_ruido = Ln.curva(t, limpia + ruido, MEDIDA, 2.5)
        c_limpia = Lc.curva(t, limpia, SENAL, 4)
        flecha_b = Arrow([4.2, 0.9, 0], [4.2, -1.0, 0], buff=0, color=AMBAR, stroke_width=6)
        palabra = self.palabra("limpiar", AMBAR, 1.0).move_to([4.2, 3.4, 0])

        with self.narrar("b3"):
            # «tiene un horizonte»
            self.en("horizonte")
            self.play(FadeOut(self.col2), FadeOut(self.obj2), FadeOut(self.dato), FadeOut(self.lm), run_time=0.4)
            self.play(Create(curva), FadeIn(bd), Create(hor), FadeIn(rh), run_time=self.dur(1.0))

            # «la memoria del proceso»
            self.en("memoria")
            self.play(FadeIn(pal), run_time=0.6)

            # «la moneda»
            self.en("moneda")
            self.play(FadeIn(mon), FadeIn(lmon), run_time=0.5)

            # «ni un paso adelante»
            self.en("ni")
            self.play(FadeIn(x_mon), run_time=0.3)

            # «Con la pila»
            self.en("pila")
            self.play(FadeIn(bat), FadeIn(lbat), run_time=0.5)

            # «el valor de ahora es el de siempre»
            self.en("siempre")
            self.play(Create(plana), FadeIn(dplana), run_time=0.6)

            # «proyectar y dejar el error perpendicular»
            self.en("proy")
            self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.camera.frame], run_time=0.3)
            self.play(Create(F.presente), Create(F.futuro), Create(F.sombra), Create(F.error), Create(F.recto),
                      run_time=self.dur(1.2))

            # «más útil que predecir»
            self.en("util")
            self.play(Create(flecha_a), FadeIn(q), run_time=0.6)

            # «limpiar una señal»
            self.en("limpiar")
            self.play(FadeOut(flecha_a), FadeOut(q), run_time=0.2)
            self.pop(palabra)
            self.play(Create(c_ruido), run_time=0.6)
            self.play(Create(flecha_b), Create(c_limpia), run_time=0.8)
