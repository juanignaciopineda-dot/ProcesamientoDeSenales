"""Escena 16 — Cierre: un número y un umbral; lo que viene, la curva de todos los umbrales."""
from comun.escena import *
from comun.figuras_c9e3 import *


def q(x):
    """Cola derecha de la normal estándar."""
    return 1 - float(cdf_normal(x))


class Cierre(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        self.resumen()
        self.lo_que_viene()
        self.wait(1.2)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def resumen(self):
        with self.narrar("b1"):
            # «decidir bien»
            self.en("decidir")
            caja_ = caja_lrt9(escala=1.5).move_to([0, 1.6, 0])
            self.play(FadeIn(caja_, scale=0.8), run_time=self.dur(0.5))

            # «calcular un número»
            self.en("numero")
            self.play(Indicate(caja_.f[0], color=MEDIDA, scale_factor=1.3), run_time=self.dur(0.6))

            # «compararlo con un umbral»
            self.en("umbral")
            self.play(Indicate(caja_.f[2], color=ESTIMACION, scale_factor=1.4), run_time=self.dur(0.6))

            # «Si conoces las probabilidades a priori»
            self.en("apriori")
            ap = Text("Probabilidades a priori", color=TXT, weight=BOLD).scale(0.5).move_to([-3.4, -0.3, 0])
            a1 = flecha(ap.get_top() + UP * 0.1, caja_.get_bottom() + LEFT * 0.8 + DOWN * 0.05, INK, 3)
            self.play(FadeIn(ap, shift=UP * 0.1), GrowArrow(a1), run_time=self.dur(0.5))

            # «el umbral es pe cero entre pe uno»
            self.en("p0p1")
            e1 = MathTex(r"\eta = \frac{p_0}{p_1}", color=ESTIMACION).scale(0.95).next_to(ap, DOWN, buff=0.35)
            self.play(FadeIn(e1, shift=UP * 0.1), run_time=self.dur(0.4))

            # «Si no»
            self.en("sino")
            mon = monedero9("5 %", color=ERROR, escala=0.8).move_to([3.4, -0.6, 0])
            a2 = flecha(mon.get_top() + UP * 0.15, caja_.get_bottom() + RIGHT * 0.8 + DOWN * 0.05, INK, 3)
            self.play(FadeIn(mon, shift=UP * 0.1), GrowArrow(a2), run_time=self.dur(0.5))

            # «el presupuesto de falsas alarmas»
            self.en("presup")
            pr = Text("Falsa alarma ≤ 5 %", color=ERROR, weight=BOLD).scale(0.5).next_to(mon, DOWN, buff=0.3)
            self.play(FadeIn(pr, shift=UP * 0.1), run_time=self.dur(0.4))

    # ------------------------------------------------------------------ b2
    def lo_que_viene(self):
        C = Campanas9(centro=(-3.6, -2.4), ancho=6.4, alto=5.0, r_rango=(-3.0, 5.0))
        umbrales = (0.6, 1.6, 2.6)
        # plano de la ROC: falsa alarma en horizontal, detección en vertical
        ox, oy, lado = 1.6, -2.6, 4.4

        def P(fa, de):
            return np.array([ox + fa * lado, oy + de * lado, 0.0])

        with self.narrar("b2"):
            # «cada umbral da un detector distinto»
            self.en("umbrales")
            self.corte()
            eje = C.eje((0, 2), rotulo=False, escala=0.4)
            c0, c1 = C.campana(0, 1, C0, 3.5), C.campana(2, 1, C1, 3.5)
            marcas = VGroup(*[Line(C.p(u) + DOWN * 0.1, C.p(u) + UP * 3.1, color=ESTIMACION, stroke_width=3.5)
                              for u in umbrales])
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.6))
            self.play(LaggedStart(*[Create(m) for m in marcas], lag_ratio=0.2), run_time=self.dur(0.5))

            # «con su falsa alarma»
            self.en("fa")
            rojas = VGroup(*[C.area(0, 1, u, 5, ERROR, 0.25) for u in umbrales])
            self.play(FadeIn(rojas), run_time=self.dur(0.4))

            # «y su detección»
            self.en("det")
            verdes = VGroup(*[C.area(2, 1, u, 5, VERDE, 0.15) for u in umbrales])
            self.play(FadeIn(verdes), run_time=self.dur(0.4))

            # «todos a la vez»
            self.en("todos")
            muchas = VGroup(*[Line(C.p(u) + DOWN * 0.1, C.p(u) + UP * 3.1, color=ESTIMACION, stroke_width=1.6,
                                   stroke_opacity=0.6) for u in np.arange(-1.6, 4.6, 0.3)])
            self.play(FadeOut(rojas), FadeOut(verdes), LaggedStart(*[Create(m) for m in muchas], lag_ratio=0.05),
                      run_time=self.dur(0.8))

            # «en un solo dibujo»
            self.en("dibujo")
            marco = Square(lado, color=INK, stroke_width=2.5).move_to(P(0.5, 0.5))
            tx = Text("Falsa alarma", color=ERROR).scale(0.42).next_to(marco, DOWN, buff=0.2)
            ty = Text("Detección", color=VERDE).scale(0.42).rotate(PI / 2).next_to(marco, LEFT, buff=0.2)
            us = np.arange(-1.6, 4.6, 0.3)
            pts = VGroup(*[Dot(P(q(u), q(u - 2)), radius=0.06, color=ESTIMACION) for u in us])
            self.play(Create(marco), FadeIn(tx), FadeIn(ty), run_time=self.dur(0.5))
            self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in pts], lag_ratio=0.08), run_time=self.dur(1.4))

            # «en el próximo episodio»
            self.en("proximo")
            uu = np.linspace(-3.5, 6.0, 120)
            curva = traza([P(q(u), q(u - 2))[0] for u in uu], [P(q(u), q(u - 2))[1] for u in uu], ESTIMACION, 4)
            self.play(Create(curva), run_time=self.dur(0.9))

            # «la curva de todos los umbrales»
            self.en("titulo")
            tit = Text("La curva de todos los umbrales", color=AMBAR, weight=BOLD).scale(0.85).move_to([0, 3.2, 0])
            self.pop(tit)
