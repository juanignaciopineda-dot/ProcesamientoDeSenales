"""Escena 05 — Los dos errores son áreas de colas; la campana estándar y la función Q."""
from comun.escena import *
from comun.figuras_c9e2 import *


class ElAreaDeLaCola(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.colas()
        self.herramienta()
        self.valores()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def colas(self):
        C = Campanas9()
        eje = C.eje(marcas=(0, 1, 2))
        c0 = C.campana(0, 1, C0)
        c1 = C.campana(2, 1, C1)
        u = umbral9(C, 1)
        punto = Dot(C.p(0), radius=0.11, color=MEDIDA)
        cola_fa = C.area(0, 1, 1, 5)
        cola_m = C.area(2, 1, -3, 1)
        et_fa = Text("Falsa alarma", color=ERROR).scale(0.5).move_to([4.3, 0.0, 0])
        et_m = Text("Fallo", color=ERROR).scale(0.5).move_to([-3.9, 0.0, 0])
        fl_fa = Arrow(et_fa.get_bottom(), C.p(1.5, 0.06), buff=0.08, color=ERROR, stroke_width=3)
        fl_m = Arrow(et_m.get_bottom(), C.p(0.5, 0.06), buff=0.08, color=ERROR, stroke_width=3)

        with self.narrar("b1"):
            # «Volvamos a las campanas»
            self.en("campanas")
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.9))

            # «con el umbral en un voltio»
            self.en("umbral")
            self.play(Create(u.linea), FadeIn(u.rot), run_time=self.dur(0.5))

            # «se envió un cero»
            self.en("cero")
            self.play(c0.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.7))

            # «el ruido empujó la medición»
            self.en("empuja")
            self.play(FadeIn(punto, scale=0.4), run_time=0.2)
            for r in (0.35, 0.7, 1.05):
                self.play(punto.animate.move_to(C.p(r)), run_time=self.dur(0.35))

            # «por encima del umbral»
            self.en("encima")
            self.play(punto.animate.move_to(C.p(1.6)), run_time=self.dur(0.4))
            self.sfx("alarma", gain=-22)

            # «el área de la campana del cero a la derecha del umbral»
            self.en("cola_fa")
            self.play(FadeIn(cola_fa), FadeOut(punto), run_time=self.dur(0.6))
            self.play(FadeIn(et_fa), Create(fl_fa), run_time=self.dur(0.4))

            # «Y el fallo»
            self.en("fallo")
            self.play(c1.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.7))

            # «a la izquierda»
            self.en("cola_m")
            self.play(FadeIn(cola_m), run_time=self.dur(0.6))
            self.play(FadeIn(et_m), Create(fl_m), run_time=self.dur(0.4))

            # «áreas de colas»
            self.en("colas")
            self.play(cola_fa.animate(rate_func=there_and_back).set_fill(ERROR, 0.95),
                      cola_m.animate(rate_func=there_and_back).set_fill(ERROR, 0.95), run_time=self.dur(0.9))

    # ------------------------------------------------------------ b2
    def herramienta(self):
        L = Lienzo(ancho=10.0, alto=5.0, t_rango=(-4.0, 6.0), v_max=0.45, centro=(0.0, -2.0))
        self.L = L
        t = np.linspace(-4, 6, 200)
        base = L.base(ancho=2.4)
        gen = L.curva(t, gaussiana(t, 3, 1.6), MEDIDA, 4)
        fantasma = DashedVMobject(L.curva(t, gaussiana(t, 0, 1), INK, 3), num_dashes=60)
        resta = Text("Restar el centro", color=ESTIMACION, weight=BOLD).scale(0.55).move_to([-4.3, 2.9, 0])
        divide = Text("Dividir entre el desvío", color=ESTIMACION, weight=BOLD).scale(0.55).move_to([-3.85, 2.1, 0])
        self.nums = VGroup(*[Text(str(k), color=INK).scale(0.45).move_to(L.p(k) + DOWN * 0.32) for k in (0, 1, 2, 3)])
        desv = Text("Desvíos", color=INK).scale(0.45).move_to(L.p(5.2) + DOWN * 0.32)
        area_t = Text("Área de la cola", color=ESTIMACION).scale(0.5).move_to([3.4, 1.5, 0])
        self.xv = ValueTracker(1.5)
        xv = self.xv

        def cola_viva():
            a = xv.get_value()
            tt = np.linspace(a, 6, 80)
            pts = [L.p(a)] + [L.p(x, gaussiana(x, 0, 1)) for x in tt] + [L.p(6)]
            return Polygon(*pts, stroke_width=0, stroke_opacity=0).set_fill(ERROR, 0.5)

        def marca_viva():
            a = xv.get_value()
            return DashedLine(L.p(a), L.p(a, gaussiana(a, 0, 1) + 0.03), color=ESTIMACION, stroke_width=3)

        def x_vivo():
            return MathTex("x", color=ESTIMACION).scale(0.8).move_to(L.p(xv.get_value()) + DOWN * 0.36)

        self._cola_viva = cola_viva
        self.cola = always_redraw(cola_viva)
        self.marca = always_redraw(marca_viva)
        self.xlbl = always_redraw(x_vivo)
        self.q = MathTex("Q(x)", color=ESTIMACION).scale(1.0).move_to([3.0, 0.65, 0])
        self.area_t, self.desv = area_t, desv

        with self.narrar("b2"):
            # «hay una herramienta»
            self.en("herramienta")
            self.corte()
            self.play(Create(base), Create(gen), run_time=self.dur(0.8))

            # «la campana estándar»
            self.en("estandar")
            self.play(Create(fantasma), run_time=self.dur(0.7))

            # «restando su centro»
            self.en("restar")
            self.play(FadeIn(resta, shift=RIGHT * 0.2),
                      Transform(gen, L.curva(t, gaussiana(t, 0, 1.6), MEDIDA, 4)), run_time=self.dur(0.9))

            # «dividiendo entre su desvío»
            self.en("dividir")
            self.play(FadeIn(divide, shift=RIGHT * 0.2),
                      Transform(gen, L.curva(t, gaussiana(t, 0, 1), TXT, 4)), run_time=self.dur(0.9))
            self.play(FadeOut(fantasma), run_time=0.25)

            # «medir las distancias en desvíos»
            self.en("desvios")
            self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in self.nums], lag_ratio=0.25),
                      FadeIn(desv), run_time=self.dur(0.9))

            # «El área de la cola»
            self.en("area")
            self.play(FadeIn(area_t), FadeOut(resta), FadeOut(divide), run_time=self.dur(0.4))

            # «desde un punto equis en adelante»
            self.en("x")
            self.play(FadeIn(self.cola), Create(self.marca), FadeIn(self.xlbl), run_time=self.dur(0.6))

            # «se llama función cu de equis»
            self.en("q")
            self.pop(self.q)

    # ------------------------------------------------------------ b3
    def valores(self):
        xv = self.xv
        q_eq = MathTex("=", r"\ ?", color=TXT).scale(1.0)
        destino_q = np.array([-4.6, 2.9, 0])
        q_eq.next_to(destino_q + RIGHT * 0.55, RIGHT, buff=0.15)
        pc = ordenador(INK).scale(0.95).move_to([-1.4, 2.9, 0])
        filas = [(r"Q(0)", r"0{,}5"), (r"Q(1)", r"0{,}16"), (r"Q(2)", r"0{,}023"), (r"Q(3)", r"0{,}0013")]
        tab = VGroup(*[MathTex(a, "=", b, color=TXT).scale(0.75) for a, b in filas])
        for k, m in enumerate(tab):
            m.move_to([4.7, 3.1 - 0.6 * k, 0])
            m[2].set_color(ERROR)
        marco_tab = SurroundingRectangle(tab, color=INK, buff=0.2, stroke_width=2.5)
        alturas = [0.5, 0.16, 0.023, 0.0013]
        barras = VGroup(*[Rectangle(width=0.4, height=max(a * 3.2, 0.03), color=ERROR, stroke_width=0)
                          .set_fill(ERROR, 0.8) for a in alturas])
        for k, b in enumerate(barras):
            b.move_to([1.0 + 0.55 * k, 0.6 + b.height / 2, 0])

        with self.narrar("b3"):
            # «No tiene una fórmula sencilla»
            self.en("nofor")
            self.play(FadeOut(self.area_t), self.q.animate.move_to(destino_q), run_time=self.dur(0.5))
            self.play(FadeIn(q_eq), run_time=self.dur(0.3))
            tacha = tachar(VGroup(self.q, q_eq))
            self.play(Create(tacha), run_time=self.dur(0.3))

            # «se mira en una tabla»
            self.en("tabla")
            self.play(Create(marco_tab), run_time=self.dur(0.5))

            # «se le pide al ordenador»
            self.en("ordenador")
            self.play(FadeIn(pc, shift=UP * 0.2), run_time=self.dur(0.5))

            # «Algunos valores para orientarse»
            self.en("valores")
            self.play(FadeOut(self.nums), FadeOut(self.desv), run_time=self.dur(0.3))
            self.play(Circumscribe(self.xlbl, color=ESTIMACION, buff=0.12), run_time=self.dur(0.6))

            # «Cu de cero es un medio»
            self.en("q0")
            self.play(xv.animate.set_value(0), run_time=self.dur(0.7))
            self.play(Write(tab[0]), run_time=self.dur(0.4))

            # «media campana»
            self.en("media")
            brillo = self._cola_viva().set_fill(ERROR, 0.9)
            self.play(FadeIn(brillo), run_time=self.dur(0.3))
            self.play(FadeOut(brillo), run_time=self.dur(0.3))

            # «uno, cero coma dieciséis»
            self.en("q1")
            self.play(xv.animate.set_value(1), run_time=self.dur(0.6))
            self.play(Write(tab[1]), run_time=self.dur(0.4))

            # «Cu de dos»
            self.en("q2")
            self.play(xv.animate.set_value(2), run_time=self.dur(0.6))
            self.play(Write(tab[2]), run_time=self.dur(0.4))

            # «Cu de tres»
            self.en("q3")
            self.play(xv.animate.set_value(3), run_time=self.dur(0.6))
            self.play(Write(tab[3]), run_time=self.dur(0.4))

            # «La cola cae muy deprisa»
            self.en("deprisa")
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in barras], lag_ratio=0.3), run_time=self.dur(1.0))
        for m in (self.cola, self.marca, self.xlbl):
            m.clear_updaters()
