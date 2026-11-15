"""Escena 07 — De variables a procesos: la ventana de L muestras y por qué es un filtro FIR."""
from comun.escena import *


class LaVentana(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.ventana_y_suma()
        self.se_desliza()
        self.es_un_filtro()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def ventana_y_suma(self):
        t, y, v, x = sensor12(40)
        L = Lienzo(ancho=11.0, alto=3.0, t_rango=(0, 39), v_max=7, centro=(0.0, 1.0))
        self.L = L
        self.x, self.n0 = x, 26
        curva = L.curva(t, x, MEDIDA, 3.2)
        puntos = VGroup(*[Dot(L.p(k, x[k]), radius=0.05, color=MEDIDA) for k in range(40)])
        yq = MathTex(r"y[n] = \,?", color=SENAL).scale(0.95).move_to([-4.8, 3.3, 0])
        self.marca = L.vertical(self.n0, AMBAR, 3, mitad=1.6)
        self.lab_n = MathTex("n", color=AMBAR).scale(0.9).next_to(self.marca, UP, buff=0.05)
        self.vent = Rectangle(width=3 * 11.0 / 39, height=3.2, stroke_width=2, color=AMBAR).set_fill(AMBAR, 0.2)
        self.vent.move_to([float(L.x(self.n0 - 1)), 1.0, 0])
        self.lab_L = MathTex("L = 3", color=AMBAR).scale(0.8).move_to([float(L.x(self.n0 - 1)), -0.9, 0])
        labs = []
        pos = [(-0.7, "x[n-2]", self.n0 - 2), (1.5, "x[n-1]", self.n0 - 1), (3.7, "x[n]", self.n0)]
        self.lineas = []
        for px, s, k in pos:
            lab = MathTex(s, color=MEDIDA).scale(0.8).move_to([px, -1.5, 0])
            lin = Line(L.p(k, x[k]), [px, -1.2, 0], color=INK, stroke_width=1.8)
            circ = Circle(radius=0.15, color=AMBAR, stroke_width=3.5).move_to(L.p(k, x[k]))
            labs.append((lab, lin, circ))
        f = formula(r"\hat{y}[n]", "=", "h_0", "x[n]", "+", "h_1", "x[n-1]", r"+\cdots+", "h_{L-1}", "x[n-L+1]",
                    escala=1.05,
                    colores={0: ESTIMACION, 2: ESTIMACION, 3: MEDIDA, 5: ESTIMACION, 6: MEDIDA, 8: ESTIMACION,
                             9: MEDIDA}).move_to([0, -2.9, 0])
        self.f_suma = f
        self.curva, self.puntos = curva, puntos
        self.labs = labs

        with self.narrar("b1"):
            # «muestras de un proceso»
            self.en("proceso")
            self.play(Create(curva), run_time=self.dur(0.9))
            self.play(FadeIn(puntos), run_time=self.dur(0.4))

            # «Para estimar la temperatura»
            self.en("estimar")
            self.play(FadeIn(yq, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «en el instante ene»
            self.en("ene")
            self.play(Create(self.marca), FadeIn(self.lab_n), run_time=self.dur(0.5))

            # «las ele últimas muestras»
            self.en("ventana")
            self.play(FadeIn(self.vent), FadeIn(self.lab_L), run_time=self.dur(0.6))

            # «la de ahora»
            self.en("ahora")
            lab, lin, circ = labs[2]
            self.play(Create(circ), Create(lin), FadeIn(lab), run_time=self.dur(0.4))

            # «la anterior»
            self.en("anterior")
            lab, lin, circ = labs[1]
            self.play(Create(circ), Create(lin), FadeIn(lab), run_time=self.dur(0.4))

            # «la anterior a esa»
            self.en("anterior2")
            lab, lin, circ = labs[0]
            self.play(Create(circ), Create(lin), FadeIn(lab), run_time=self.dur(0.4))

            # «La estimación es una suma»
            self.en("sumaest")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.4))

            # «hache cero por equis de ene»
            self.en("h0")
            self.play(FadeIn(f[2]), FadeIn(f[3]), run_time=self.dur(0.5))

            # «más hache uno por equis de ene menos uno»
            self.en("h1")
            self.play(FadeIn(f[4]), FadeIn(f[5]), FadeIn(f[6]), run_time=self.dur(0.6))

            # «y así hasta ele muestras»
            self.en("asi")
            self.play(FadeIn(f[7]), FadeIn(f[8]), FadeIn(f[9]), run_time=self.dur(0.7))
        self.wait(0.3)
        self.yq = yq

    # ------------------------------------------------------------ b2
    def se_desliza(self):
        L = self.L
        paso = 11.0 / 39
        interr = Text("?", color=AMBAR, weight=BOLD).scale(0.7).move_to([self.f_suma[2].get_center()[0], -2.2, 0])
        interr2 = Text("?", color=AMBAR, weight=BOLD).scale(0.7).move_to([self.f_suma[5].get_center()[0], -2.2, 0])
        nuevo = MathTex(r"\hat{y}[n+1] = \,?", color=ESTIMACION).scale(0.95).move_to([4.2, 3.3, 0])
        cand_a = candado(AMBAR, abierto=True).scale(0.6).move_to([6.3, -2.9, 0])
        cand_c = candado(AMBAR, abierto=False).scale(0.6).move_to([6.3, -2.9, 0])
        conj = Text("conjuntamente estacionarios", color=TXT).scale(0.6).move_to([-3.2, 3.4, 0])
        k0, k1 = 20, 25
        dist = DoubleArrow(L.p(k0, 0) + UP * 2.0, L.p(k1, 0) + UP * 2.0, buff=0, color=AMBAR, stroke_width=3,
                           max_tip_length_to_length_ratio=0.1)
        lk = MathTex("k", color=AMBAR).scale(0.8).next_to(dist, UP, buff=0.05)
        c_n = cruz(ROJO, 0.5).move_to(self.lab_n.get_center())
        mover = [self.marca, self.lab_n, self.vent, self.lab_L]

        with self.narrar("b2"):
            # «avanzamos un instante»
            self.en("avanza")
            self.play(FadeOut(self.yq), run_time=0.2)
            self.play(self.marca.animate.shift(RIGHT * paso), self.lab_n.animate.shift(RIGHT * paso),
                      run_time=self.dur(0.6))

            # «La ventana se desliza»
            self.en("desliza")
            self.play(self.vent.animate.shift(RIGHT * paso), self.lab_L.animate.shift(RIGHT * paso),
                      run_time=self.dur(0.7))

            # «volver a estimar»
            self.en("volver")
            self.pop(nuevo)

            # «¿Cambian los coeficientes?»
            self.en("cambian")
            self.play(FadeIn(interr), FadeIn(interr2), run_time=self.dur(0.4))

            # «No.»
            self.en("no")
            self.play(FadeOut(interr), FadeOut(interr2), FadeIn(cand_a), run_time=self.dur(0.4))

            # «conjuntamente estacionarios»
            self.en("conj")
            self.play(FadeOut(nuevo), run_time=0.2)
            self.pop(conj)

            # «depende solo de la distancia»
            self.en("dist")
            self.play(GrowFromCenter(dist), FadeIn(lk), run_time=self.dur(0.6))

            # «no del instante en que miremos»
            self.en("instante")
            self.play(Create(c_n), run_time=self.dur(0.4))

            # «La cuenta sale igual»
            self.en("igual")
            self.resaltar(self.f_suma, color=AMBAR, escala=1.04)

            # «valen siempre»
            self.en("siempre")
            self.play(FadeOut(cand_a), FadeIn(cand_c), run_time=0.3)
            self.sfx("tick")
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def es_un_filtro(self):
        bl = BloqueLTI("h", centro=(0.0, 0.8), ancho=2.6, alto=1.4, color=AMBAR, largo=2.4)
        lx = MathTex("x[n]", color=MEDIDA).scale(0.9).next_to(bl.p_ent(), UP, buff=0.15)
        ly = MathTex(r"\hat{y}[n]", color=ESTIMACION).scale(0.9).next_to(bl.p_sal(), UP, buff=0.4)
        tira = Tallos([0.3, 0.6, 0.8], centro=(-4.4, -1.8), paso=0.75, unidad=1.4, color=MEDIDA)
        h_t = Tallos([0.74, 0.12, 0.02], centro=(0.0, -1.8), paso=0.75, unidad=1.8, color=ESTIMACION)
        cand = candado(AMBAR, abierto=False).scale(0.8).move_to([2.0, -1.6, 0])
        conv = formula(r"\hat{y}", "=", "h", r"\ast", "x", escala=1.3,
                       colores={0: ESTIMACION, 2: ESTIMACION, 4: MEDIDA}).move_to([0, 2.9, 0])
        prom = Tallos([0.5, 0.5], centro=(5.0, -1.6), paso=0.75, unidad=1.8, color=ESTIMACION)
        prom_l = Text("promediador", color=INK).scale(0.6).move_to([5.0, -2.65, 0])
        lti = sello("LTI", AMBAR).move_to([4.7, 2.5, 0])
        resp = MathTex("h[k]", color=ESTIMACION).scale(1.0).move_to([0.0, -2.75, 0])
        mx = MathTex(r"\mu_x", color=MEDIDA).scale(0.8).move_to([-2.6, 0.2, 0])
        my = MathTex(r"\mu_y", color=SENAL).scale(0.8).move_to([2.6, 0.2, 0])
        rmx = MathTex(r"-\mu_x", color=AMBAR).scale(0.9).move_to([-2.6, 1.5, 0])
        rmy = MathTex(r"+\mu_y", color=AMBAR).scale(0.9).move_to([2.6, 1.5, 0])

        with self.narrar("b3"):
            # «en un filtro»
            self.en("filtro")
            self.corte()
            self.play(FadeIn(bl), FadeIn(lx), FadeIn(ly), run_time=self.dur(0.8))

            # «Una suma de muestras recientes»
            self.en("sumamr")
            self.play(Create(tira.base), *[Create(a) for a in tira.tallos], *[FadeIn(p) for p in tira.puntos],
                      run_time=self.dur(0.6))

            # «con coeficientes fijos»
            self.en("fijos")
            self.play(Create(h_t.base), *[Create(a) for a in h_t.tallos], *[FadeIn(p) for p in h_t.puntos],
                      FadeIn(cand), run_time=self.dur(0.6))

            # «una convolución»
            self.en("conv")
            self.play(*[FadeIn(conv[i]) for i in range(len(conv))], run_time=self.dur(0.8))

            # «el promediador del capítulo diez»
            self.en("prom")
            self.play(Create(prom.base), *[Create(a) for a in prom.tallos], *[FadeIn(p) for p in prom.puntos],
                      FadeIn(prom_l), run_time=self.dur(0.6))

            # «lineal e invariante en el tiempo»
            self.en("lti")
            self.pop(lti)

            # «respuesta al impulso hache»
            self.en("resp")
            self.pop(resp)

            # «Si las señales tienen media»
            self.en("media")
            self.play(FadeIn(mx), FadeIn(my), run_time=self.dur(0.5))

            # «se le resta a la entrada»
            self.en("resta")
            self.pop(rmx)

            # «se le suma a la salida»
            self.en("suma")
            self.pop(rmy)
