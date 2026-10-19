"""Escena 09 — Decidir y estimar: acertar o fallar da la moda; con un continuo de hipótesis y el cuadrado
del error sale la media condicional del capítulo 8."""
from comun.escena import *
from comun.figuras_c9e5 import *


class DeElegirADarUnValor(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.circulo()
        self.juntar()
        self.cuadrado()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def circulo(self):
        with self.narrar("b1"):
            a = casilla9("Capítulo 8", MEDIDA, ancho=2.6).move_to([-3.0, 0, 0])
            b = casilla9("Capítulo 9", AMBAR, ancho=2.6).move_to([3.0, 0, 0])
            # «Con los costes sobre la mesa» (arranque del bloque)
            self.play(FadeIn(a, shift=RIGHT * 0.2), FadeIn(b, shift=LEFT * 0.2), run_time=0.5)

            # «se cierra el círculo»
            self.en("circulo")
            arc1 = ArcBetweenPoints(a.get_top() + UP * 0.1, b.get_top() + UP * 0.1, angle=-PI / 2, color=INK,
                                    stroke_width=4)
            arc2 = ArcBetweenPoints(b.get_bottom() + DOWN * 0.1, a.get_bottom() + DOWN * 0.1, angle=-PI / 2,
                                    color=INK, stroke_width=4)
            self.play(Create(arc1), run_time=self.dur(0.5))
            self.play(Create(arc2), run_time=self.dur(0.5))

            # «Allí vimos»
            self.en("alli")
            self.play(FadeOut(VGroup(b, arc1, arc2)), a.animate.move_to([0, 3.1, 0]), run_time=self.dur(0.5))

            # «la mejor apuesta depende»
            self.en("casillas")
            filas = VGroup()
            for i, (k, v) in enumerate((("Cuadrado", "Media"), ("Tamaño", "Mediana"), ("Acierto", "Moda"))):
                ck = casilla9(k, INK, ancho=2.4, alto=0.75, escala=0.48)
                cv = casilla9(v, INK, ancho=2.4, alto=0.75, escala=0.48)
                fl = Arrow(LEFT * 0.5, RIGHT * 0.5, color=INK, buff=0, stroke_width=3,
                           max_tip_length_to_length_ratio=0.25)
                filas.add(VGroup(ck, fl, cv).arrange(RIGHT, buff=0.25))
            filas.arrange(DOWN, buff=0.3).move_to([-2.4, 0.3, 0])
            self.play(LaggedStart(*[FadeIn(f, shift=RIGHT * 0.2) for f in filas], lag_ratio=0.25),
                      run_time=self.dur(0.8))

            # «Con el cuadrado sale la media»
            self.en("media")
            self.play(filas[0][0].marco.animate.set_stroke(VERDE, 4), filas[0][2].marco.animate.set_stroke(VERDE, 4),
                      run_time=self.dur(0.4))

            # «Con acertar o fallar»
            self.en("acierto")
            self.play(filas[0][0].marco.animate.set_stroke(INK, 3), filas[0][2].marco.animate.set_stroke(INK, 3),
                      filas[2][0].marco.animate.set_stroke(AMBAR, 5), run_time=self.dur(0.4))

            # «la moda»
            self.en("moda")
            self.play(filas[2][2].marco.animate.set_stroke(AMBAR, 5), run_time=self.dur(0.35))

            # «La regla del máximo a posteriori»
            self.en("map")
            mp = casilla9("Máximo a posteriori", AMBAR, ancho=3.4, alto=0.75, escala=0.48)
            mp.next_to(filas[2], RIGHT, buff=1.0)
            fl = Arrow(filas[2][2].get_right(), mp.get_left(), color=AMBAR, buff=0.1, stroke_width=4,
                       max_tip_length_to_length_ratio=0.2)
            self.play(Create(fl), FadeIn(mp, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «coste cero si aciertas»
            self.en("cero")
            T = Tabla22_9(("Sano", "Enfermo"), ("Sano", "Enfermo"), centro=(4.6, 1.1), ancho=1.0, alto=0.65,
                          escala=0.34)
            ceros = VGroup(*[Text("0", color=VERDE, weight=BOLD).scale(0.45).move_to(T.c(i, i)) for i in (0, 1)])
            self.play(FadeIn(T), FadeIn(ceros), run_time=self.dur(0.4))

            # «uno si fallas»
            self.en("uno")
            unos = VGroup(*[Text("1", color=ERROR, weight=BOLD).scale(0.45).move_to(T.c(i, 1 - i)) for i in (0, 1)])
            self.pop(unos)

    # ------------------------------------------------------------ b2
    def juntar(self):
        C = campanas_e5(centro=(0.0, -1.6), ancho=11.0, alto=4.4)
        with self.narrar("b2"):
            # «Ahora junta las hipótesis»
            self.en("eje")
            self.corte()
            base = C.L.base(INK, 2.4)
            g = campanitas9(C, 2)
            self.play(Create(base), run_time=0.3)
            self.play(Create(g), run_time=self.dur(0.7))

            # «Con dos amplitudes posibles»
            self.en("amp")
            v0 = Text("0 V", color=INK).scale(0.45).move_to(C.p(0) + DOWN * 0.35)
            v2 = Text("2 V", color=INK).scale(0.45).move_to(C.p(2) + DOWN * 0.35)
            self.play(FadeIn(v0), FadeIn(v2), run_time=self.dur(0.4))

            # «eliges entre dos»
            self.en("dos")
            preg = Text("¿Cuál de estas?", color=AMBAR, weight=BOLD).scale(0.65).move_to([0, 2.9, 0])
            self.play(FadeIn(preg, shift=DOWN * 0.15), run_time=self.dur(0.4))
            self.play(g.animate(rate_func=there_and_back).set_stroke(width=8), run_time=self.dur(0.5))

            for marca, n in (("tres", 3), ("nueve", 9), ("cien", 100)):
                self.en(marca)
                nuevo = campanitas9(C, n, ancho=3.5 if n < 20 else 1.5)
                self.play(ReplacementTransform(g, nuevo), run_time=self.dur(0.7))
                g = nuevo

            # «En el límite»
            self.en("limite")
            banda = Rectangle(width=float(C.L.x(2) - C.L.x(0)), height=0.8 * C.L.alto / 2 * 1.0, stroke_width=0)
            banda.set_fill(C1, 0.35).move_to(C.p(1, 0.8 * C.L.v_max / 2))
            self.play(FadeIn(banda), g.animate.set_stroke(opacity=0.3), run_time=self.dur(0.6))

            # «cualquier número»
            self.en("continuo")
            eje_c = Line(C.p(0), C.p(2), color=C1, stroke_width=10)
            self.play(FadeOut(banda), FadeOut(g), Create(eje_c), run_time=self.dur(0.6))

            # «das un valor»
            self.en("valor")
            mk = Triangle(color=AMBAR).set_fill(AMBAR, 1).scale(0.18).rotate(PI).move_to(C.p(1.37) + UP * 0.35)
            v = Text("1,37", color=AMBAR, weight=BOLD).scale(0.5).next_to(mk, LEFT, buff=0.2)
            p2 = Text("¿Cuánto?", color=AMBAR, weight=BOLD).scale(0.65).move_to(preg)
            self.play(FadeIn(mk, shift=DOWN * 0.3), FadeIn(v), ReplacementTransform(preg, p2), run_time=self.dur(0.5))

            # «Eso es estimar»
            self.en("estimar")
            es = self.palabra("Estimar", AMBAR, 1.1).move_to([0, 1.6, 0])
            self.pop(es)
            self.C, self.mk, self.v = C, mk, v

    # ------------------------------------------------------------ b3
    def cuadrado(self):
        C = self.C
        x_v = 1.37
        with self.narrar("b3"):
            # «acertar o fallar deja de servir»
            self.en("dardo")
            self.play(*[FadeOut(m) for m in self.mobjects if isinstance(m, Text) and m is not self.v],
                      run_time=0.25)
            d = dardo9(escala=1.6).move_to(C.p(x_v + 0.35) + UP * 3.0)
            self.add(d)
            self.play(d.animate.shift(C.p(x_v + 0.35) - d.punta.get_bottom()), run_time=self.dur(0.45),
                      rate_func=rate_functions.ease_in_quad)
            self.sfx("tick")

            # «nunca vas a dar con el valor exacto»
            self.en("prob0")
            p0 = MathTex(r"\text{Acertar: } P = 0", color=ERROR).scale(0.75).move_to([-3.8, 2.6, 0])
            self.play(FadeIn(p0, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «cuánto te alejas»
            self.en("distancia")
            dist = DoubleArrow(C.p(x_v) + DOWN * 0.45, C.p(x_v + 0.35) + DOWN * 0.45, buff=0, color=ERROR,
                               stroke_width=4, tip_length=0.12, max_tip_length_to_length_ratio=0.5)
            self.play(GrowFromCenter(dist), run_time=self.dur(0.4))

            # «el cuadrado del error»
            self.en("parabola")
            ax = Line([2.6, 1.2, 0], [6.4, 1.2, 0], color=INK, stroke_width=2)
            par = FunctionGraph(lambda x: 1.2 + 0.55 * (x - 4.5) ** 2, x_range=[3.0, 6.0], color=ERROR, stroke_width=4)
            ct = MathTex(r"\text{Coste} = \text{Error}^2", color=ERROR).scale(0.65).move_to([4.5, 3.2, 0])
            self.play(Create(ax), Create(par), FadeIn(ct), run_time=self.dur(0.6))

            # «la regla de riesgo mínimo»
            self.en("rm")
            rm = Text("Riesgo mínimo", color=AMBAR, weight=BOLD).scale(0.45).move_to([4.5, 0.75, 0])
            caja_rm = SurroundingRectangle(VGroup(ax, par, ct, rm), color=AMBAR, buff=0.2, stroke_width=3)
            self.play(FadeIn(rm), Create(caja_rm), run_time=self.dur(0.4))

            # «la media condicional»
            self.en("media")
            t = np.linspace(-0.6, 3.0, 120)
            v = 0.32 * np.exp(-(t - 1.0) ** 2 / 0.25) + 0.18 * np.exp(-(t - 1.9) ** 2 / 0.12)
            curva = C.L.curva(t, v, MEDIDA, 4)
            media = float(np.sum(t * v) / np.sum(v))
            mm = Line(C.p(media), C.p(media) + UP * 2.4, color=VERDE, stroke_width=4)
            self.play(FadeOut(d), FadeOut(dist), Create(curva), run_time=self.dur(0.6))
            self.play(Create(mm), self.mk.animate.move_to(C.p(media) + UP * 0.35),
                      FadeOut(self.v),
                      run_time=self.dur(0.5))

            # «el estimador del capítulo ocho»
            self.en("cap8")
            et = Text("Media condicional · Capítulo 8", color=VERDE).scale(0.48).move_to(C.p(media) + UP * 2.75 + LEFT * 0.7)
            self.pop(et)
