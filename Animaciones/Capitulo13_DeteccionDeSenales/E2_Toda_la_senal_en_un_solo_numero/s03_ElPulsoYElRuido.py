"""Escena 03 — El pulso conocido, el ruido gaussiano independiente y la densidad conjunta."""
from comun.escena import *


class ElPulsoYElRuido(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.modelo()
        self.supuestos()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def modelo(self):
        ant = antena(TXT).scale(0.8).move_to([-6.0, 2.9, 0])
        s = Barras((2, 2, 1), centro=(-0.5, 0.5), paso=2.0, unidad=0.65, color=SENAL, ancho=0.95, indices=True, nums=True)
        w = Barras((0.6, -0.5, 0.4), centro=(-0.5, -1.0), paso=2.0, unidad=0.8, color=RUIDO, ancho=0.95)
        r = Barras((3, 1, 2), centro=(-0.5, -2.45), paso=2.0, unidad=0.45, color=MEDIDA, ancho=0.95, indices=True)
        llave = Brace(VGroup(*s.barras), UP, color=INK, buff=0.45)
        objetivo = Text("la señal objetivo, conocida", color=SENAL).scale(0.62).next_to(llave, UP, buff=0.12)
        sn = MathTex("s[n]", color=SENAL).scale(1.2).move_to([-4.6, 1.0, 0])
        wn = MathTex("w[n]", color=RUIDO).scale(1.1).move_to([-4.6, -1.0, 0])
        rn = MathTex("r[n]", color=MEDIDA).scale(1.1).move_to([-4.6, -2.0, 0])
        av = avion(AZUL).scale(0.7).move_to([5.3, 2.6, 0])
        erres = [MathTex(f"r[{i}]", color=MEDIDA).scale(0.85).move_to([r.x(i), -3.45, 0]) for i in range(3)]
        pulso_onda = Arc(radius=0.8, start_angle=-PI / 4, angle=PI / 2, color=SENAL, stroke_width=5).move_to([-5.2, 2.9, 0])

        with self.narrar("b1"):
            # «un pulso que conocemos de antemano»
            self.en("pulso")
            self.play(FadeIn(ant), Create(pulso_onda), run_time=self.dur(0.7))

            # «tres muestras»
            self.en("tres")
            self.play(Create(s.base), FadeIn(s.ks), run_time=self.dur(0.6))

            # «dos, dos y uno»
            self.en("valores")
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in s.barras], lag_ratio=0.3),
                      FadeIn(s.nums, shift=UP * 0.1), run_time=self.dur(1.2))

            # «la señal objetivo»
            self.en("objetivo")
            self.play(GrowFromCenter(llave), FadeIn(objetivo), run_time=self.dur(0.6))

            # «ese de ene»
            self.en("sn")
            self.pop(sn)

            # «Si hay un avión»
            self.en("avion")
            self.play(FadeIn(av, shift=LEFT * 0.4), run_time=self.dur(0.5))

            # «ese pulso más ruido»
            self.en("mas")
            self.play(Create(w.base), *[GrowFromEdge(b, DOWN) for b in w.barras], FadeIn(wn), run_time=self.dur(0.8))

            # «muestra a muestra»
            self.en("muestra")
            marco = Rectangle(width=1.3, height=3.3, color=AMBAR, stroke_width=3).move_to([s.x(0), 0.3, 0])
            self.play(Create(marco), run_time=self.dur(0.3))
            for i in (1, 2):
                self.play(marco.animate.move_to([s.x(i), 0.3, 0]), run_time=self.dur(0.4))

            # «Si no, solo ruido»
            self.en("solo")
            self.play(FadeOut(marco), *[b.animate.fade(0.8) for b in s.barras], s.nums.animate.fade(0.8),
                      run_time=self.dur(0.5))

            # «tres números recibidos»
            self.en("recibidos")
            self.play(Create(r.base), FadeIn(r.ks), *[GrowFromEdge(b, DOWN) for b in r.barras], FadeIn(rn),
                      run_time=self.dur(0.8))

            # «erre de cero, erre de uno y erre de dos»
            self.en("erres")
            self.play(LaggedStart(*[FadeIn(e, shift=UP * 0.1) for e in erres], lag_ratio=0.35), run_time=self.dur(1.0))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def supuestos(self):
        self.corte()
        L = Lienzo(ancho=4.6, alto=2.2, t_rango=(-3.5, 3.5), v_max=1.15, centro=(-3.0, 2.2))
        ejeb = L.base()
        cam = campana_curva(L, 0, 1.0, RUIDO, 4)
        cero = DashedLine(L.p(0, 0), L.p(0, 1.05), color=INK, stroke_width=2.5)
        sigma = MathTex(r"\sigma^2", color=RUIDO).scale(1.3).move_to([0.2, 2.2, 0])
        vale1 = MathTex(r"\sigma^2=1", color=RUIDO).scale(1.4).move_to([2.2, 2.2, 0])
        b1 = Circle(radius=0.3, color=RUIDO, stroke_width=4).move_to([-6.2, 2.2, 0])
        n1 = Text("1", color=RUIDO, weight=BOLD).scale(0.5).move_to(b1)
        b2 = Circle(radius=0.3, color=RUIDO, stroke_width=4).move_to([-6.2, -0.5, 0])
        n2 = Text("2", color=RUIDO, weight=BOLD).scale(0.5).move_to(b2)
        bella = []
        for i, cx in enumerate((-3.9, -0.6, 2.7)):
            Li = Lienzo(ancho=3.0, alto=1.5, t_rango=(-3.5, 3.5), v_max=1.15, centro=(cx, -0.4))
            bella.append(VGroup(Li.base(), campana_curva(Li, 0, 1.0, RUIDO, 3.5, pico=1.0)))
        wl = [MathTex(f"w[{i}]", color=RUIDO).scale(0.85).next_to(bella[i], DOWN, buff=0.15) for i in range(3)]
        cap7 = Text("Capítulo 7", color=INK).scale(0.6).move_to([6.0, -0.5, 0])
        prod = formula("f(w_0,w_1,w_2)", "=", "f(w_0)", r"\cdot", "f(w_1)", r"\cdot", "f(w_2)",
                       escala=1.25, colores={2: RUIDO, 4: RUIDO, 6: RUIDO}).move_to([0, -2.9, 0])

        with self.narrar("b2"):
            # «dos cosas»
            self.en("dos")
            self.play(FadeIn(b1), FadeIn(n1), FadeIn(b2), FadeIn(n2), run_time=self.dur(0.5))

            # «Primera»
            self.en("p1")
            self.play(b1.animate.set_fill(RUIDO, 0.5), run_time=self.dur(0.4))

            # «una campana de Gauss»
            self.en("campana")
            self.play(Create(ejeb), Create(cam), run_time=self.dur(0.9))

            # «centrada en cero»
            self.en("cero")
            self.play(Create(cero), run_time=self.dur(0.4))

            # «sigma cuadrado»
            self.en("sigma")
            self.pop(sigma)

            # «aquí vale uno»
            self.en("vale1")
            self.play(ReplacementTransform(sigma, vale1), run_time=self.dur(0.5))

            # «Segunda»
            self.en("p2")
            self.play(b1.animate.set_fill(RUIDO, 0.0), b2.animate.set_fill(RUIDO, 0.5), run_time=self.dur(0.4))

            # «independiente de las demás»
            self.en("indep")
            self.play(LaggedStart(*[FadeIn(b) for b in bella], lag_ratio=0.3), FadeIn(VGroup(*wl)), run_time=self.dur(1.0))

            # «el capítulo siete»
            self.en("cap7")
            self.play(FadeIn(cap7), run_time=self.dur(0.4))

            # «el producto de las densidades de cada una»
            self.en("producto")
            self.play(*[FadeIn(prod[i], shift=UP * 0.1) for i in range(len(prod))], run_time=self.dur(1.4))
        self.wait(0.3)
