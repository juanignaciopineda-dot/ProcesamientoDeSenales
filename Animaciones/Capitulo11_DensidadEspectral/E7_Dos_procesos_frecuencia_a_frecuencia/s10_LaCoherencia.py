"""Escena 10 — La coherencia: un rho por cada frecuencia."""
from comun.escena import *


class LaCoherencia(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        gam = oculta(formula(r"\gamma_{yx}", "=", escala=1.1, colores={0: AMBAR}).move_to([-5.0, 1.2, 0]))
        num = oculta(formula(r"D_{yx}", escala=1.1, colores={0: MEDIDA}))
        den = oculta(formula(r"\sqrt{D_{xx}\,D_{yy}}", escala=1.1))
        fr = fraccion(num, den).move_to([-2.9, 1.2, 0])
        fr.barra.set_stroke(opacity=0)
        menor1 = formula(r"|\gamma|\le 1", escala=1.0, colores={0: AMBAR}).move_to([-3.3, -0.5, 0])
        # el rho del capítulo 7
        rho_l = formula(r"\rho", "=", escala=1.1, colores={0: INK}).move_to([2.4, 1.2, 0])
        n7 = formula(r"\sigma_{XY}", escala=1.1)
        d7 = formula(r"\sigma_X\,\sigma_Y", escala=1.1)
        fr7 = fraccion(n7, d7).move_to([4.5, 1.2, 0])
        c7 = etiqueta("capítulo 7", INK, 0.5).move_to([4.0, -0.5, 0])
        # una gamma para cada frecuencia
        L = Lienzo(ancho=11.0, alto=1.8, t_rango=(0, 1), v_max=1.0, centro=(0.8, -3.0))
        eje = L.base(INK, 2.5)
        l_w = MathTex(r"\omega", color=INK).scale(0.6).move_to([6.8, -2.75, 0])
        marcas = VGroup(*[Dot(L.p(x, 0), radius=0.08, color=AMBAR) for x in (0.12, 0.34, 0.56, 0.78)])
        gammas = VGroup(*[MathTex(r"\gamma", color=AMBAR).scale(0.6).move_to(L.p(x, 0) + DOWN * 0.4)
                          for x in (0.12, 0.34, 0.56, 0.78)])
        f = lambda u: 0.15 + 0.7 * np.exp(-((u - 0.3) / 0.1) ** 2) + 0.45 * np.exp(-((u - 0.75) / 0.12) ** 2)
        cur = curva_f(L, f, 0.0, 1.0, AMBAR, 4.0)
        l_rho = formula(r"\rho(\omega)", escala=0.8, colores={0: AMBAR}).move_to([-5.6, -2.0, 0])
        with self.narrar("b1"):
            # «dividimos la densidad cruzada»
            self.en("cruzada")
            self.corte()
            self.add(gam, num, den, fr.barra)
            self.play(*revelar(gam, num), run_time=self.dur(0.8))

            # «la raíz del producto de las dos densidades»
            self.en("raiz")
            self.play(fr.barra.animate.set_stroke(TXT, opacity=1.0), *revelar(den), run_time=self.dur(0.9))

            # «nunca pasa de uno en módulo»
            self.en("menor1")
            self.pop(menor1)

            # «la coherencia»
            self.en("coh")
            self.play(gam[0].animate.scale(1.25), run_time=0.4)
            self.play(gam[0].animate.scale(1 / 1.25), run_time=0.3)

            # «lo que era rho»
            self.en("rho")
            self.play(FadeIn(rho_l), FadeIn(n7), FadeIn(d7), FadeIn(fr7.barra), FadeIn(c7), run_time=self.dur(0.9))

            # «la covarianza dividida»
            self.en("cov")
            self.play(num.animate.set_color(AMBAR), n7.animate.set_color(AMBAR), run_time=self.dur(0.7))

            # «las desviaciones típicas»
            self.en("desv")
            self.play(den.animate.set_color(AMBAR), d7.animate.set_color(AMBAR), run_time=self.dur(0.7))

            # «en cada frecuencia»
            self.en("cadafreq")
            self.play(Create(eje), FadeIn(l_w), FadeIn(marcas), run_time=self.dur(0.6))
            self.play(FadeIn(gammas), run_time=self.dur(0.5))

            # «Un rho para cada frecuencia»
            self.en("unrho")
            self.play(Create(cur), FadeIn(l_rho), run_time=self.dur(1.2))

        self.wait(1.0)
        self.limpiar()
