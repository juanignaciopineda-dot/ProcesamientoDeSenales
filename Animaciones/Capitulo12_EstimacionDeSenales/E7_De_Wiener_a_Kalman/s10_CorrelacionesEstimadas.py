"""Escena 10 — En la práctica solo hay un registro: las correlaciones se estiman y el filtro hereda sus errores."""
from comun.escena import *


class CorrelacionesEstimadas(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        m = np.arange(0, 15)
        real = np.where(m == 0, 5.0, 4.0 * 0.6 ** m)
        rng = np.random.default_rng(5)
        est = real + rng.normal(0, 0.05 + 0.07 * m, len(m)) + 0.04 * m
        cx = formula("C_{xx}[m]", escala=1.0, colores={0: MEDIDA}).move_to([-3.4, 3.2, 0])
        conocida = etiqueta("conocida", VERDE, 0.5).move_to([-1.2, 3.2, 0])
        L1 = Lienzo(ancho=5.4, alto=1.5, t_rango=(0, 40), v_max=5.0, centro=(-3.4, 1.4))
        t, y, v, x = sensor12(40, 31)
        reg = L1.curva(t, x, MEDIDA, 3.0)
        solo = etiqueta("solo datos", INK, 0.5).move_to([-3.4, 0.2, 0])
        cq = formula("C_{xx}[m]", "=", "?", escala=1.0, colores={0: MEDIDA, 2: AMBAR}).move_to([-3.4, -0.6, 0])
        L2 = Lienzo(ancho=5.4, alto=2.2, t_rango=(0, 14), v_max=6.0, centro=(3.6, 1.5))
        base2 = Line(L2.p(0, -3.0), L2.p(14, -3.0), color=INK, stroke_width=2)
        yy = lambda a: a - 3.0
        c_real = L2.curva(m, yy(real), INK, 2.5, 0.8)
        c_est = L2.curva(m, yy(est), AMBAR, 3.5)
        l_ses = etiqueta("sesgo", ERROR, 0.45).move_to([6.2, 0.2, 0])
        l_var = etiqueta("varianza", ERROR, 0.45).move_to([4.6, 2.9, 0])
        zona = Rectangle(width=2.0, height=2.3, color=ERROR, stroke_width=0).set_fill(ERROR, 0.15).move_to(
            [L2.x(11.5), L2.cy, 0])
        filt = caja("filtro h", AZUL, ancho=2.2, alto=0.8, scale=0.5).move_to([3.6, -0.7, 0])
        tor = Tallos([0.85, 0.05, 0.12], centro=(3.6, -1.9), paso=0.8, unidad=0.9, color=SENAL)
        ar = flecha([3.6, 0.3, 0], [3.6, -0.25, 0])
        L3 = Lienzo(ancho=11.0, alto=0.9, t_rango=(0, 120), v_max=5.0, centro=(0.0, -3.1))
        rr = L3.curva(np.arange(120), 2 * serie(8, 120, 0.6) + serie(9, 120, 0.0), MEDIDA, 2.2)
        vent = Rectangle(width=L3.ancho * 6 / 120 * 1.0, height=1.0, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.2
                                                                                                             ).move_to([L3.x(8), L3.cy, 0])
        nl = formula("N", "\\gg", "L", escala=0.9, colores={0: MEDIDA, 2: AMBAR}).move_to([-5.9, -2.2, 0])
        diez = formula("N", "\\geq", "10\\,L", escala=0.9, colores={0: MEDIDA, 2: AMBAR}).move_to([-5.9, -2.2, 0])
        with self.narrar("b1"):
            # «conocemos las correlaciones»
            self.en("conocemos")
            self.corte()
            self.play(FadeIn(cx), FadeIn(conocida), run_time=self.dur(0.7))
            # «solo tenemos un registro»
            self.en("registro")
            self.play(FadeOut(conocida), Create(L1.base()), Create(reg), FadeIn(solo), FadeIn(cq), run_time=self.dur(1.2))
            # «Hay que estimarlas»
            self.en("estimar")
            self.play(Create(base2), Create(c_est), run_time=self.dur(1.2))
            # «sesgo y varianza»
            self.en("sesgo")
            self.play(Create(c_real), FadeIn(l_ses), FadeIn(l_var), run_time=self.dur(0.9))
            # «sobre todo en los desfases grandes»
            self.en("desfases")
            self.play(FadeIn(zona), run_time=self.dur(0.6))
            # «El filtro que sale»
            self.en("filtro")
            self.play(FadeIn(filt), run_time=self.dur(0.6))
            # «hereda esos errores»
            self.en("hereda")
            self.play(GrowArrow(ar), Create(tor.base), *[Create(t_) for t_ in tor.tallos],
                      *[FadeIn(p) for p in tor.puntos], run_time=self.dur(0.9))
            # «un registro mucho más largo que la ventana»
            self.en("largo")
            self.play(Create(L3.base()), Create(rr), run_time=self.dur(0.8))
            self.play(FadeIn(vent), FadeIn(nl), run_time=self.dur(0.6))
            # «al menos diez veces»
            self.en("diez")
            self.play(Transform(nl, diez), vent.animate.stretch_to_fit_width(L3.ancho * 6 / 120 * 1.0), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
