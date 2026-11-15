"""Escena 12 — Dos procesos a la vez: correlación y covarianza cruzadas; «no correlacionados» no es «independientes»."""
from comun.escena import *


class CorrelacionCruzada(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        Li = Lienzo(ancho=5.6, alto=3.0, t_rango=(0, 1), v_max=2.0, centro=(-3.7, 0.4))
        Ld = Lienzo(ancho=5.6, alto=3.0, t_rango=(0, 1), v_max=2.0, centro=(3.7, 0.4))
        pila_i = pila_de_curvas(Li, 16, semilla=11, a=0.93, color=SENAL, opacidad=0.5, ancho=2.0, escala=0.45)
        pila_d = pila_de_curvas(Ld, 16, semilla=12, a=0.93, color=MEDIDA, opacidad=0.5, ancho=2.0, escala=0.45)
        F = formula("R_{XY}", "(", "t_1", ",", "t_2", ")", "=", "E", "[", "X", "(", "t_1", ")", "Y", "(", "t_2", ")", "]",
                    escala=1.0, colores={0: AMBAR}).move_to([0, -2.6, 0])
        Fc = formula("C_{XY}", "=", "R_{XY}", "-", r"\mu_{X}", r"\mu_{Y}", escala=0.95,
                     colores={0: AMBAR}).move_to([0, -3.5, 0])
        with self.narrar("b1"):
            # «dos procesos a la vez»
            self.en("dos")
            self.play(LaggedStart(*[Create(c) for c in pila_i], lag_ratio=0.03),
                      LaggedStart(*[Create(c) for c in pila_d], lag_ratio=0.03), run_time=self.dur(1.2))

            # «lo que se envía»
            self.en("envia")
            e1 = Text("enviado", color=SENAL, weight=BOLD).scale(0.7).move_to([-3.7, 2.55, 0])
            self.pop(e1)

            # «lo que se recibe»
            self.en("recibe")
            e2 = Text("recibido", color=MEDIDA, weight=BOLD).scale(0.7).move_to([3.7, 2.55, 0])
            self.pop(e2)

            # «la voz y el ruido»
            self.en("voz_ruido")
            voz = persona(SENAL).scale(0.55).move_to([-5.9, 2.5, 0])
            murmullo = traza(np.linspace(5.3, 6.3, 60), 2.5 + 0.12 * serie(3, 60, 0.4), RUIDO, 3)
            self.play(FadeIn(voz), Create(murmullo), run_time=self.dur(0.7))

            # «Entre ellos»
            self.en("entre")
            fl = DoubleArrow([-0.7, 0.4, 0], [0.7, 0.4, 0], color=INK, stroke_width=4, buff=0, tip_length=0.2)
            self.play(GrowFromCenter(fl), run_time=0.4)

            # «los mismos momentos, pero cruzados»
            self.en("cruzados")
            ca = Li.vertical(0.3, AMBAR, 3.5)
            cb = Ld.vertical(0.7, AMBAR, 3.5)
            cur = CurvedArrow([float(Li.x(0.3)), -1.25, 0], [float(Ld.x(0.7)), -1.25, 0], angle=TAU / 6,
                              color=AMBAR, stroke_width=3)
            self.play(Create(ca), Create(cb), run_time=0.4)
            self.play(Create(cur), run_time=self.dur(0.7))

            # «La correlación cruzada»
            self.en("rxy")
            w = self.palabra("correlación cruzada", AMBAR, 1.0).move_to([0, 3.5, 0])
            self.play(FadeOut(cur), run_time=0.2)
            self.pop(w)

            # «erre sub equis i griega»
            self.en("rxy_f")
            self.play(FadeIn(F[0:6], shift=UP * 0.15), run_time=self.dur(0.7))

            # «la esperanza de equis en un instante»
            self.en("x_t1")
            self.play(FadeIn(F[6:13], shift=UP * 0.15), run_time=self.dur(1.0))

            # «por i griega en otro»
            self.en("y_t2")
            self.play(FadeIn(F[13:], shift=UP * 0.15), run_time=self.dur(0.9))

            # «la covarianza cruzada»
            self.en("cxy")
            self.play(FadeIn(Fc, shift=UP * 0.15), run_time=self.dur(0.9))

            # «con las medias restadas»
            self.en("restadas")
            self.play(Fc[4].animate.set_color(AMBAR), Fc[5].animate.set_color(AMBAR), run_time=0.5)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        rombo = Rombo(centro=(-4.4, -1.6), radio=0.85)
        F0 = formula("C_{XY}", "(", "t_1", ",", "t_2", ")", "=", "0", escala=1.2,
                     colores={0: AMBAR}).move_to([0, 2.9, 0])
        rng = np.random.default_rng(2)
        with self.narrar("b2"):
            # «vale cero»
            self.en("cero")
            self.corte()
            self.pop(F0)

            # «cualquier pareja de instantes»
            self.en("parejas")
            pares = VGroup(*[formula("(t_1,t_2)", escala=0.8, color=INK).move_to([x, y, 0])
                             for y in (2.0, 1.2, 0.4) for x in (-4.5, 0.0, 4.5)])
            self.play(LaggedStart(*[FadeIn(p, scale=0.6) for p in pares], lag_ratio=0.1), run_time=self.dur(1.0))

            # «se dice que los dos procesos»
            self.en("se_dice")
            self.play(FadeOut(pares), run_time=0.3)
            sd = etiqueta("se dice que están", INK, 0.65).move_to([0, 1.5, 0])
            self.play(FadeIn(sd), run_time=0.4)

            # «no correlacionados»
            self.en("nocorr")
            nc = self.palabra("no correlacionados", AMBAR, 1.2).move_to([0, 0.6, 0])
            eq = formula(r"\Leftrightarrow", "C_{XY}", "=", "0", escala=1.0, colores={1: AMBAR}).move_to([0, -0.5, 0])
            self.pop(nc)
            self.play(FadeIn(eq), run_time=0.5)

            # «Fíjate en el nombre»
            self.en("nombre")
            self.play(nc.animate(rate_func=there_and_back).scale(1.12), run_time=0.6)

            # «cuando la covarianza es cero»
            self.en("cov0")
            self.play(eq[1].animate(rate_func=there_and_back).scale(1.3), run_time=0.6)

            # «no la correlación»
            self.en("no_corr")
            cc = Text("correlación", color=INK).scale(0.7).move_to([4.6, -0.5, 0])
            self.play(FadeIn(cc), run_time=0.3)
            self.play(Create(tachar(cc)), run_time=0.3)

            # «con el rombo»
            self.en("rombo")
            self.play(Create(rombo.ejes), *[FadeIn(d, scale=0.4) for d in rombo.puntos], run_time=self.dur(0.7))

            # «que sean independientes»
            self.en("indep")
            ind = Text("≠  independientes", color=ROJO, weight=BOLD).scale(0.7).move_to([0.6, -1.6, 0])
            self.pop(ind)

            # «no hay relación en línea recta»
            self.en("recta")
            ajuste = Line(rombo.p(-1.25, 0), rombo.p(1.25, 0), color=ESTIMACION, stroke_width=6)
            sr = Text("sin relación en línea recta", color=ESTIMACION).scale(0.55).move_to([1.5, -2.6, 0])
            self.play(Create(ajuste), FadeIn(sr), run_time=self.dur(0.7))
