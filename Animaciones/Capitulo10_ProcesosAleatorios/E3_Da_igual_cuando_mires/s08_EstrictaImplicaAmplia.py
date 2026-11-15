"""Escena 08 — SSS implica WSS, en dos pasos."""
from comun.escena import *


class EstrictaImplicaAmplia(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        L = Lienzo(ancho=9.0, alto=2.6, t_rango=(0, 1), v_max=2.2, centro=(0, 0.3))
        pila = pila_de_curvas(L, 12, semilla=9, a=0.93, color=SENAL, opacidad=0.5, ancho=2.2, escala=0.55)
        self.L, self.pila = L, pila
        self.cuerpo1()
        self.cuerpo2()
        self.wait(1.0)
        self.limpiar()

    def cuerpo1(self):
        L, pila = self.L, self.pila
        with self.narrar("b1"):
            # «las dos versiones»
            self.en("versiones")
            a = caja("SSS", AZUL, ancho=1.8, alto=0.7).move_to([-2.6, 3.4, 0])
            b = caja("WSS", VERDE, ancho=1.8, alto=0.7).move_to([2.6, 3.4, 0])
            self.play(FadeIn(a), FadeIn(b), FadeIn(pila), run_time=self.dur(0.6))

            # «La estricta implica la amplia»
            self.en("implica")
            imp = Arrow(a.get_right() + RIGHT * 0.1, b.get_left() + LEFT * 0.1, color=VERDE, buff=0, stroke_width=6)
            self.play(Create(imp), run_time=self.dur(0.6))

            # «en dos pasos»
            self.en("dos_pasos")
            p1 = Text("paso 1", color=AMBAR, weight=BOLD).scale(0.55).move_to([-5.5, 3.4, 0])
            p2 = Text("paso 2", color=INK, weight=BOLD).scale(0.55).move_to([5.5, 3.4, 0])
            self.play(FadeIn(p1), FadeIn(p2), run_time=0.4)

            # «con un solo corte»
            self.en("un_corte")
            self.corte1 = L.vertical(0.3, AMBAR, 3.5)
            self.play(Create(self.corte1), run_time=self.dur(0.5))

            # «la densidad de cada instante»
            self.en("densidad")
            self.camp = campana_mini((float(L.x(0.3)) + 0.9, -2.2), 1.5, 0.9, AMBAR, 3.5)
            self.play(Create(self.camp), run_time=self.dur(0.6))

            # «la misma que la de cualquier otro»
            self.en("otro")
            d = 0.35 * L.ancho
            self.play(self.corte1.animate.shift(RIGHT * d), self.camp.animate.shift(RIGHT * d), run_time=self.dur(1.0))

            # «Y si la densidad es la misma»
            self.en("si_misma")
            ghosts = VGroup(*[self.camp.copy().shift(LEFT * k * 1.2).set_stroke(opacity=0.5) for k in (1, 2, 3)])
            self.play(FadeIn(ghosts), run_time=self.dur(0.6))

            # «la media también»
            self.en("media")
            centros = VGroup(*[Dot([self.camp.get_center()[0] - k * 1.2, self.camp.get_center()[1] - 0.35 + 0.35, 0],
                                   radius=0.08, color=VERDE) for k in (0, 1, 2, 3)])
            lm = Line(centros[3].get_center(), centros[0].get_center(), color=VERDE, stroke_width=3)
            self.play(FadeIn(centros), Create(lm), run_time=self.dur(0.7))

            # «La media es constante»
            self.en("cte")
            cte = Text("μ constante", color=VERDE, weight=BOLD).scale(0.7).move_to([4.8, -2.5, 0])
            self.pop(cte)
            self.tilde1 = tilde(VERDE, 0.3).next_to(cte, LEFT, buff=0.2)
            self.play(FadeIn(self.tilde1), run_time=0.2)
        self.play(*[FadeOut(m) for m in (self.corte1, self.camp, ghosts, centros, lm, cte, self.tilde1)], run_time=0.3)

    def cuerpo2(self):
        L = self.L
        with self.narrar("b2"):
            # «con dos cortes»
            self.en("dos_cortes")
            c1, c2 = L.vertical(0.25, AMBAR, 3.5), L.vertical(0.6, AMBAR, 3.5)
            self.play(Create(c1), Create(c2), run_time=self.dur(0.5))

            # «en te uno y en te dos»
            self.en("t1t2")
            l1 = MathTex("t_1", color=AMBAR).scale(0.8).next_to(c1, UP, buff=0.1)
            l2 = MathTex("t_2", color=AMBAR).scale(0.8).next_to(c2, UP, buff=0.1)
            self.play(FadeIn(l1), FadeIn(l2), run_time=0.4)

            # «hacia atrás»
            self.en("atras")
            d = -float(L.x(0.25) - L.x(0.0))
            self.play(c1.animate.shift(RIGHT * d), c2.animate.shift(RIGHT * d), l1.animate.shift(RIGHT * d),
                      l2.animate.shift(RIGHT * d), run_time=self.dur(1.0))

            # «el primero caiga en cero»
            self.en("en_cero")
            l1c = MathTex("0", color=AMBAR).scale(0.8).move_to(l1)
            l2c = MathTex("t_2-t_1", color=AMBAR).scale(0.8).move_to(l2)
            self.play(ReplacementTransform(l1, l1c), ReplacementTransform(l2, l2c), run_time=self.dur(0.6))

            # «la conjunta no cambia»
            self.en("no_cambia")
            fj = formula(r"\big(X(t_1),\,X(t_2)\big)", "=", r"\big(X(0),\,X(t_2-t_1)\big)", escala=0.85).move_to([0, -2.0, 0])
            self.play(FadeIn(fj[0]), run_time=0.4)
            self.play(FadeIn(fj[1]), FadeIn(fj[2]), run_time=self.dur(0.6))

            # «la pareja en cero»
            self.en("pareja")
            self.resaltar(fj[2], escala=1.06)

            # «te dos menos te uno»
            self.en("dif")
            self.resaltar(l2c, escala=1.2)

            # «Solo depende de la separación»
            self.en("separacion")
            ll = BraceBetweenPoints(L.p(0.6 - 0.25, -1.2), L.p(0.0, -1.2), color=AMBAR)
            self.play(Create(ll), run_time=self.dur(0.6))

            # «la autocorrelación»
            self.en("autoc")
            fa = formula("R_{XX}(t_1,t_2)", "=", "R_{XX}(t_2-t_1)", escala=0.85).move_to([0, -3.2, 0])
            self.play(FadeIn(fa[0]), FadeIn(fa[1]), FadeIn(fa[2]), run_time=self.dur(0.9))

            # «esa conjunta»
            self.en("esa")
            fl = Arrow(fj.get_bottom() + DOWN * 0.05, fa.get_top() + UP * 0.05, color=AMBAR, buff=0, stroke_width=4)
            self.play(Create(fl), run_time=self.dur(0.5))

            # «Las dos condiciones de la amplia se cumplen»
            self.en("cumplen")
            t1, t2 = tilde(VERDE, 0.35).move_to([-4.5, 3.4, 0]), tilde(VERDE, 0.35).move_to([4.15, 3.4, 0])
            self.pop(t1, t2)
