"""Escena 10 — Al deslizar el umbral se traza la curva ROC, que depende solo de d = √E / σ."""
import math

from comun.escena import *


def qf(x: float) -> float:
    """Función Q: cola de la campana estándar."""
    return 0.5 * math.erfc(x / math.sqrt(2.0))


class CurvaRoc(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.L = Lienzo(ancho=7.0, alto=3.2, t_rango=(-8, 17), v_max=1.2, centro=(-3.0, -1.2))
        self.R = Lienzo(ancho=4.2, alto=8.4, t_rango=(0, 1), v_max=1.0, centro=(4.3, -2.0))
        self.g = ValueTracker(16.5)
        self.deslizar()
        self.depende_de_d()
        self.wait(1.0)
        self.limpiar()

    def roc(self, d: float, color=ESTIMACION, ancho: float = 5.0) -> VMobject:
        """Curva ROC de distancia d sobre el plano de la derecha."""
        gs = np.linspace(-4 * 3.0, 4 * 3.0 + 9, 220)
        sig = 3.0
        pfa = np.array([qf(g / sig) for g in gs])
        pd = np.array([qf(g / sig - d) for g in gs])
        return traza(self.R.x(pfa), self.R.y(pd), color, ancho)

    # ------------------------------------------------------------ b1
    def deslizar(self):
        L, R, g = self.L, self.R, self.g
        base = eje_g3(L, marcas=(0, 9))
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        umb = always_redraw(lambda: Line(L.p(g.get_value(), 0) + DOWN * 0.15, L.p(g.get_value(), 0) + UP * 2.0,
                                         color=ESTIMACION, stroke_width=4))
        cola_d = always_redraw(lambda: cola3(L, 0, 3, min(g.get_value(), 16.9), 17))
        area_d = always_redraw(lambda: cola3(L, 9, 3, min(g.get_value(), 16.9), 17, VERDE, 0.45))
        ejes = VGroup(Arrow(R.p(0, 0), R.p(1.08, 0), buff=0, color=INK, stroke_width=3, tip_length=0.2, max_tip_length_to_length_ratio=0.1),
                      Arrow(R.p(0, 0), R.p(0, 1.08), buff=0, color=INK, stroke_width=3, tip_length=0.2, max_tip_length_to_length_ratio=0.1))
        marco = Rectangle(width=4.2, height=4.2, color=INK, stroke_width=1.5, stroke_opacity=0.5).move_to(R.p(0.5, 0.5))
        pfa_t = MathTex("P_{FA}", color=ERROR).scale(0.8).move_to(R.p(0.5, 0) + DOWN * 0.6)
        pd_t = MathTex("P_D", color=VERDE).scale(0.8).next_to(R.p(0, 0.5), LEFT, buff=0.25)
        punto = always_redraw(lambda: Dot(R.p(qf(g.get_value() / 3.0), qf(g.get_value() / 3.0 - 3.0)), radius=0.13, color=ESTIMACION))
        uno_x = MathTex("1", color=ERROR).scale(0.7).move_to(R.p(1.0, 0) + DOWN * 0.3)
        curva = self.roc(3.0)
        roc_t = Text("curva ROC", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(R.p(0.5, 1.0) + UP * 0.55)
        azar = DashedLine(R.p(0, 0), R.p(1, 1), color=INK, stroke_width=2.5)
        azar_t = Text("azar", color=INK).scale(0.45).move_to(R.p(0.72, 0.42))
        esquina = Circle(radius=0.28, color=VERDE, stroke_width=4).move_to(R.p(0, 1))
        ok = tilde(VERDE, 0.5).move_to(R.p(0.2, 0.86) + RIGHT * 0.3)

        with self.narrar("b1"):
            # «desliza el umbral de derecha a izquierda»
            self.en("desliza")
            self.play(FadeIn(base), Create(cam0), Create(cam1), run_time=self.dur(0.5))
            self.add(umb, cola_d, area_d)
            self.play(g.animate.set_value(8.0), run_time=self.dur(2.6), rate_func=linear)

            # «Cada posición es un punto»
            self.en("punto")
            self.play(Create(marco), Create(ejes), FadeIn(punto), run_time=self.dur(0.7))
            self.play(g.animate.set_value(5.5), run_time=self.dur(0.9), rate_func=linear)

            # «falsa alarma en un eje»
            self.en("ejex")
            self.play(FadeIn(pfa_t), run_time=self.dur(0.4))
            self.play(g.animate.set_value(3.5), run_time=self.dur(1.0), rate_func=linear)

            # «detección en el otro»
            self.en("ejey")
            self.play(FadeIn(pd_t), run_time=self.dur(0.4))

            # «muy a la derecha, no detectamos nada»
            self.en("nada")
            self.play(g.animate.set_value(16.5), run_time=self.dur(1.2))

            # «muy a la izquierda»
            self.en("izq")
            self.play(g.animate.set_value(-6.0), run_time=self.dur(2.2), rate_func=linear)

            # «lo detectamos todo»
            self.en("todo")
            self.play(Indicate(punto, color=AMBAR, scale_factor=1.8), run_time=self.dur(0.6))

            # «con todas las falsas alarmas»
            self.en("todas")
            self.play(FadeIn(uno_x), run_time=self.dur(0.4))

            # «Los puntos dibujan una curva»
            self.en("curva")
            self.play(Create(curva), run_time=self.dur(1.6))

            # «la curva ROC»
            self.en("roc")
            self.pop(roc_t)

            # «la esquina de arriba a la izquierda»
            self.en("esquina")
            self.play(Create(esquina), Create(azar), FadeIn(azar_t), run_time=self.dur(0.8))

            # «mejor»
            self.en("mejor")
            self.play(FadeIn(ok, scale=0.5), run_time=self.dur(0.4))
        self.wait(0.3)
        self.curva = curva

    # ------------------------------------------------------------ b2
    def depende_de_d(self):
        L, R, g = self.L, self.R, self.g
        d_grande = MathTex("d", color=ESTIMACION).scale(2.0).move_to([-3.0, 3.1, 0])
        sep = DoubleArrow(L.p(0, 1.15), L.p(9, 1.15), buff=0, color=ESTIMACION, stroke_width=5, tip_length=0.22)
        dist = Text("distancia en desvíos", color=ESTIMACION).scale(0.5).next_to(sep, UP, buff=0.08)
        d_formula = formula("d", "=", r"\frac{\sqrt{E}}{\sigma}", escala=1.2, colores={0: ESTIMACION}).move_to([-3.0, 3.1, 0])
        tres = formula("d", "=", "3", escala=1.2, colores={0: ESTIMACION, 2: AMBAR}).move_to([-3.0, 3.1, 0])
        c1 = self.roc(1.0, CIAN, 4.0)
        c5 = self.roc(5.0, VERDE, 4.0)
        t1 = MathTex("d=1", color=CIAN).scale(0.65).move_to(R.p(0.8, 0.3))
        t5 = MathTex("d=5", color=VERDE).scale(0.65).move_to([1.5, float(R.y(0.97)), 0])
        form = formula("P_D", "=", "Q", "(", "Q^{-1}", "(", "P_{FA}", ")", "-", "d", ")", escala=0.95,
                       colores={0: VERDE, 6: ERROR, 9: ESTIMACION}).move_to([-3.4, 2.0, 0])
        e_up = formula("E", r"\uparrow", escala=1.0, colores={0: SENAL, 1: VERDE}).move_to([-5.0, -3.4, 0])
        s_dn = formula(r"\sigma^2", r"\downarrow", escala=1.0, colores={0: RUIDO, 1: VERDE}).move_to([-3.0, -3.4, 0])
        pd_up = formula("P_D", r"\uparrow", escala=1.0, colores={0: VERDE, 1: VERDE}).move_to([4.3, -3.4, 0])

        with self.narrar("b2"):
            # «depende de un solo número»
            self.en("solo")
            self.play(self.g.animate.set_value(4.5), run_time=self.dur(0.7))
            self.pop(d_grande)

            # «la distancia entre las dos campanas medida en desvíos»
            self.en("dist")
            self.play(Create(sep), FadeIn(dist), run_time=self.dur(0.9))

            # «la raíz de la energía entre sigma»
            self.en("d")
            self.play(ReplacementTransform(d_grande, d_formula), run_time=self.dur(1.0))

            # «Aquí, tres»
            self.en("tres")
            self.play(ReplacementTransform(d_formula, tres), self.curva.animate.set_stroke(width=8), run_time=self.dur(0.8))

            # «Con un valor mayor, la curva se pega a la esquina»
            self.en("mayor")
            self.play(Create(c1), FadeIn(t1), run_time=self.dur(0.8))
            self.play(Create(c5), FadeIn(t5), run_time=self.dur(1.0))

            # «La detección vale cu de la inversa de cu de la falsa alarma»
            self.en("form")
            self.play(LaggedStart(*[FadeIn(form[i], shift=UP * 0.1) for i in range(8)], lag_ratio=0.15),
                      run_time=self.dur(2.4))

            # «menos ese número»
            self.en("menos")
            self.play(*[FadeIn(form[i], shift=UP * 0.1) for i in (8, 9, 10)], run_time=self.dur(0.8))
            self.play(form[9].animate(rate_func=there_and_back).scale(1.5), run_time=self.dur(0.6))

            # «Para detectar más»
            self.en("detectar")
            self.pop(pd_up)

            # «subir la energía»
            self.en("subir")
            self.play(FadeIn(e_up, shift=UP * 0.1), c5.animate(rate_func=there_and_back).set_stroke(width=9),
                      run_time=self.dur(0.8))

            # «bajar el ruido»
            self.en("bajar")
            self.play(FadeIn(s_dn, shift=UP * 0.1), c5.animate(rate_func=there_and_back).set_stroke(width=9),
                      run_time=self.dur(0.8))
        self.wait(0.3)
