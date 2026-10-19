"""Escena 15 — El lema de Neyman-Pearson: dos criterios, el mismo test."""
from comun.escena import *
from comun.figuras_c9e3 import *

U = 1.645


class ElLemaDeNeymanPearson(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        self.enunciado()
        self.mismo_test()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def enunciado(self):
        with self.narrar("b1"):
            # «el lema de Neyman-Pearson»
            self.en("lema")
            tit = Text("Lema de Neyman-Pearson", color=TXT, weight=BOLD).scale(0.75).move_to([0, 3.2, 0])
            self.pop(tit)

            # «Para un presupuesto de falsas alarmas»
            self.en("presup")
            pre = Text("Falsa alarma ≤ α", color=ERROR, weight=BOLD).scale(0.6).move_to([0, 2.3, 0])
            self.play(FadeIn(pre, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «la mejor región»
            self.en("region")
            mr = Text("Mejor región:", color=TXT).scale(0.6).move_to([-1.3, 1.4, 0])
            self.play(FadeIn(mr, shift=RIGHT * 0.1), run_time=self.dur(0.4))

            # «mayor que un umbral»
            self.en("lr")
            lr = formula(LAMBDA, ">", r"\eta", escala=1.0, colores={0: MEDIDA, 2: ESTIMACION}).next_to(mr, RIGHT, buff=0.3)
            self.play(Write(lr), run_time=self.dur(0.5))

            # «gastar justo el presupuesto»
            self.en("gastar")
            ga = Text("η tal que Falsa alarma = α", color=ESTIMACION).scale(0.5).move_to([0, 0.55, 0])
            self.play(FadeIn(ga, shift=UP * 0.1), run_time=self.dur(0.4))

            # «Con mediciones continuas»
            self.en("cont")
            enun = VGroup(tit, pre, mr, lr, ga)
            C = Campanas9(centro=(0.6, -3.3), ancho=10.0, alto=3.9, r_rango=(-3.0, 5.0))
            eje = C.eje((0, 1, 2), escala=0.42)
            c0, c1 = C.campana(0, 1, C0, 3.5), C.campana(2, 1, C1, 3.5)
            self.play(enun.animate.scale(0.85).move_to([0, 2.45, 0]), run_time=self.dur(0.5))
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.8))

            # «rebanadas finas»
            self.en("rebanadas")
            rr = np.arange(-2.5, 4.6, 0.25)
            reb = VGroup(*[Line(C.p(r), C.p(r, max(C.f(0, r), C.f(2, r))), color=INK, stroke_width=2,
                                stroke_opacity=0.7) for r in rr])
            self.play(LaggedStart(*[Create(l) for l in reb], lag_ratio=0.03), run_time=self.dur(0.7))

            # «en vez de casillas»
            self.en("casillas")
            cas = VGroup(*[Square(0.45, color=ESTIMACION, stroke_width=3).set_fill(ESTIMACION, 0.15)
                           for _ in range(5)]).arrange(RIGHT, buff=0.12).move_to([-4.6, -0.3, 0])
            self.play(FadeIn(cas, shift=DOWN * 0.15), run_time=self.dur(0.3))
            self.play(cas.animate.move_to(C.p(1.0, 0.12)).scale(0.3).set_opacity(0), run_time=self.dur(0.7))
            self.remove(cas)

        self.C, self.enun, self.reb = C, enun, reb

    # ------------------------------------------------------------------ b2
    def mismo_test(self):
        C = self.C
        with self.narrar("b2"):
            # «la razón crece con erre»
            self.en("crece")
            G = CurvaLambda9(origen=(-6.7, -1.3), ancho=2.4, alto=1.9, r_rango=(-0.6, 2.1), v_top=9.0, escala=0.7)
            G.ejes.nums.set_opacity(0)
            cur = G.curva(ancho=3.5)
            self.play(FadeOut(self.reb), FadeIn(G.ejes), Create(cur), run_time=self.dur(0.8))

            # «todo lo que queda a la derecha»
            self.en("derecha")
            reg = C.region(U, 5, ESTIMACION)
            tr = MathTex(r"r \geq 1{,}645", color=ESTIMACION).scale(0.65).move_to([C.p(3.4)[0], -3.95 + 0.2, 0])
            self.play(FadeIn(reg), FadeIn(tr), run_time=self.dur(0.5))

            # «No había una región mejor»
            self.en("nohabia")
            base = Line([3.6, -0.5, 0], [6.6, -0.5, 0], color=INK, stroke_width=2)
            trozos = VGroup(*[Rectangle(width=w, height=0.14, stroke_width=0).set_fill(ESTIMACION, 0.8)
                              .move_to([x, -0.43, 0]) for x, w in ((3.9, 0.3), (4.7, 0.25), (5.4, 0.35), (6.2, 0.4))])
            rara = VGroup(base, trozos)
            t = Line(rara.get_corner(DL) + LEFT * 0.1 + DOWN * 0.1, rara.get_corner(UR) + RIGHT * 0.1 + UP * 0.25,
                     color=ERROR, stroke_width=5)
            self.play(FadeIn(rara), run_time=self.dur(0.3))
            self.play(Create(t), run_time=self.dur(0.4))

            # «dos criterios distintos»
            self.en("dos")
            self.corte()
            k1 = casilla9("Máximo a posteriori: η = p₀ / p₁", C1, ancho=5.6, alto=1.0, escala=0.48).move_to([-3.4, 2.0, 0])
            k2 = casilla9("Neyman-Pearson: η por presupuesto", ERROR, ancho=5.6, alto=1.0, escala=0.48).move_to([3.4, 2.0, 0])
            self.play(FadeIn(k1, shift=UP * 0.15), FadeIn(k2, shift=UP * 0.15), run_time=self.dur(0.5))

            # «el mismo test»
            self.en("test")
            caja_ = caja_lrt9(escala=1.4).move_to([0, -1.2, 0])
            a1 = flecha(k1.get_bottom() + DOWN * 0.1, caja_.get_top() + LEFT * 0.6 + UP * 0.1, INK, 3.5)
            a2 = flecha(k2.get_bottom() + DOWN * 0.1, caja_.get_top() + RIGHT * 0.6 + UP * 0.1, INK, 3.5)
            self.play(GrowArrow(a1), GrowArrow(a2), FadeIn(caja_), run_time=self.dur(0.7))

            # «Un número»
            self.en("num")
            self.play(Indicate(caja_.f[0], color=MEDIDA, scale_factor=1.3), run_time=self.dur(0.6))

            # «y un umbral»
            self.en("umb")
            self.play(Indicate(caja_.f[2], color=ESTIMACION, scale_factor=1.4), run_time=self.dur(0.6))

            # «de dónde sale el umbral»
            self.en("sale")
            self.play(a1.animate(rate_func=there_and_back).set_color(ESTIMACION),
                      a2.animate(rate_func=there_and_back).set_color(ESTIMACION), run_time=self.dur(0.7))
