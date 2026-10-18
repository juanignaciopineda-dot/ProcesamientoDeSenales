"""Escena 17 — Chebyshev aplicado al promedio: la ley de los grandes números."""
from comun.escena import *


class GrandesNumeros(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        self.ley()
        self.forma()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def ley(self):
        cheb = self.palabra("Chebyshev", AMBAR, 1.0).move_to([-4.8, 3.4, 0])
        xn = MathTex(r"\bar X_n", color=SENAL).scale(1.4).move_to([-1.6, 3.4, 0])
        aleje = MathTex(r"P(|\bar X_n-\mu|\ge\varepsilon)", color=TXT).scale(1.3).move_to([-2.0, 2.2, 0])
        cota = MathTex(r"\le", r"\frac{\sigma^2}{n\,\varepsilon^2}", color=AMBAR).scale(1.4).next_to(aleje, RIGHT, buff=0.3)
        cero = MathTex(r"\to 0", color=VERDE).scale(1.4).next_to(cota, RIGHT, buff=0.3)
        L = Lienzo(ancho=10.0, alto=3.4, t_rango=(0, 4), v_max=1.5, centro=(0.0, -1.4))
        ns = np.unique(np.round(np.logspace(0, 4, 260)).astype(int))
        t = np.log10(ns)
        corridas = VGroup(*[L.curva(t, np.clip(promedios_ruido(10000, s)[ns - 1], -1.45, 1.45), c, 3.5)
                            for s, c in ((3, SENAL), (11, MEDIDA), (21, ESTIMACION))])
        mu = DashedLine(L.p(0, 0), L.p(4, 0), color=AMBAR, stroke_width=3)
        eps = 0.22
        banda = Rectangle(width=L.p(4)[0] - L.p(0)[0], height=float(L.y(eps) - L.y(-eps)), stroke_width=0
                         ).set_fill(AMBAR, 0.22).move_to(L.p(2, 0))
        eps_t = MathTex(r"\varepsilon", color=AMBAR).scale(0.9).move_to(L.p(4, eps) + RIGHT * 0.45)
        n_t = MathTex("n", color=INK).scale(0.8).move_to(L.p(4, -1.9) + RIGHT * 0.3)
        flecha_n = Arrow(L.p(0.2, -1.9), L.p(3.8, -1.9), color=INK, stroke_width=3, buff=0)
        titulo_ = self.palabra("Ley de los grandes números", AMBAR, 0.8).move_to([2.6, 3.4, 0])
        with self.narrar("b1"):
            # «le aplicamos Chebyshev al promedio»
            self.en("aplica")
            self.pop(cheb)
            self.play(FadeIn(xn, shift=DOWN * 0.15), run_time=self.dur(0.6))
            # «se aleje de la media verdadera»
            self.en("aleje")
            self.play(FadeIn(aleje, shift=DOWN * 0.15), run_time=self.dur(1.5))
            # «tan pequeña como quieras»
            self.en("epsilon")
            self.play(Create(mu), FadeIn(banda), FadeIn(eps_t), run_time=self.dur(1.0))
            # «sigma cuadrado dividido entre n por épsilon al cuadrado»
            self.en("cota")
            self.play(FadeIn(cota, shift=LEFT * 0.15), run_time=self.dur(1.6))
            # «cuando n crece»
            self.en("crece")
            self.play(Create(flecha_n), FadeIn(n_t), *[Create(c) for c in corridas],
                      run_time=self.dur(1.3), rate_func=linear)
            # «se va a cero»
            self.en("cero")
            self.play(FadeIn(cero, shift=LEFT * 0.15), run_time=self.dur(0.6))
            # «la ley de los grandes números»
            self.en("ley")
            self.pop(titulo_)
            # «pegándose a la media»
            self.en("pegado")
            self.play(Indicate(corridas, color=AMBAR), run_time=self.dur(0.9))

    # ---------------------------------------------------------------- b2
    def forma(self):
        y0 = 1.4
        formas = VGroup(
            campana7(-4.2, y0, 0.8, SENAL, ancho=0.7, alto=1.4, x_max=3),
            Polygon([-1.0, y0, 0], [-1.0, y0 + 1.2, 0], [1.0, y0 + 1.2, 0], [1.0, y0, 0], color=SENAL, stroke_width=4),
            VGroup(campana7(3.2, y0, 0.3, SENAL, ancho=0.7, alto=1.4, x_max=3),
                   campana7(5.0, y0, 0.3, SENAL, ancho=0.7, alto=1.4, x_max=3)))
        s2 = MathTex(r"\sigma^2", color=AMBAR).scale(2.0).move_to([0, 1.8, 0])
        cap10 = caja("Capítulo 10", AZUL, ancho=3.4, alto=0.9, scale=0.7).move_to([4.2, -0.3, 0])
        fl = flecha([1.0, 1.8, 0], [2.6, -0.3, 0], AMBAR, 4)
        Lt = Lienzo(ancho=11.0, alto=2.0, t_rango=(0, 1), v_max=1.4, centro=(0, -2.5))
        tt = np.linspace(0, 1, 260)
        senal = Lt.curva(tt, 0.5 * serie(4, 260, 0.85), SENAL, 3.5)
        ventana = Rectangle(width=0.05, height=2.4, stroke_width=3, color=AMBAR).set_fill(AMBAR, 0.18)
        ventana.move_to([float(Lt.x(0)) + 0.025, -2.5, 0])
        with self.narrar("b2"):
            # «la forma del ruido»
            self.en("forma")
            self.corte()
            self.play(FadeIn(formas), run_time=self.dur(1.0))
            # «solo su varianza»
            self.en("solo_var")
            self.play(FadeOut(formas), run_time=0.3)
            self.pop(s2)
            # «volverá con fuerza»
            self.en("volvera")
            self.play(GrowArrow(fl), FadeIn(cap10), run_time=self.dur(0.8))
            # «señales que cambian en el tiempo»
            self.en("cambian")
            self.play(Create(senal), run_time=self.dur(1.5), rate_func=linear)
            # «una sola grabación»
            self.en("grabacion")
            self.play(FadeIn(ventana), run_time=0.2)
            self.play(ventana.animate.stretch_to_fit_width(11.0, about_edge=LEFT), run_time=self.dur(1.8), rate_func=linear)
