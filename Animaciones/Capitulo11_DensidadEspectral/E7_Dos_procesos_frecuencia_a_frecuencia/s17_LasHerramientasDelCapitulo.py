"""Escena 17 — Las herramientas del capítulo y el paso a estimar una variable a partir de otra."""
from comun.escena import *


def tarjeta(y, color=INK):
    return RoundedRectangle(corner_radius=0.12, width=4.6, height=1.3, color=color, stroke_width=2.5
                            ).set_fill(color, 0.08).move_to([-4.2, y, 0])


class LasHerramientasDelCapitulo(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        marco = caja("el capítulo 11", AMBAR, ancho=3.6, alto=0.8).move_to([0, 3.5, 0])
        t1, t2, t3 = tarjeta(1.9), tarjeta(0.4), tarjeta(-1.1)
        # tarjeta 1: la densidad
        Lc = Lienzo(ancho=2.2, alto=0.9, t_rango=(-6, 6), v_max=1.0, centro=(-5.2, 1.9))
        c_xx = curva_f(Lc, psd_tele, -6, 6, AMBAR, 3.5)
        n1 = formula(r"S_{xx}(j\omega)", escala=0.8, colores={0: AMBAR}).move_to([-2.9, 1.9, 0])
        # tarjeta 2: la cruzada
        fz = flecha_c([-5.6, 0.2, 0], 0.9, 35, AMBAR, ancho=5)
        n2 = formula(r"S_{yx}(j\omega)", escala=0.8, colores={0: AMBAR}).move_to([-2.9, 0.4, 0])
        # tarjeta 3: la forma honesta
        n3 = etiqueta("trozos + promedio", TXT, 0.5).move_to([-4.6, -1.1, 0])
        ok = tilde(VERDE, 0.4).move_to([-2.4, -1.1, 0])
        # las rebanadas y las flechas
        cortes = VGroup(*[Line([x, 2.4, 0], [x, -2.4, 0], color=INK, stroke_width=2, stroke_opacity=0.7)
                          for x in (0.3, 2.3, 4.3, 6.3)])
        pares = VGroup(*[VGroup(flecha_c([xc - 0.6, -0.6], 1.0, 0, SENAL, ancho=5),
                                flecha_c([xc - 0.6, -0.6], 1.0, a, MEDIDA, ancho=5))
                         for xc, a in zip((1.3, 3.3, 5.3), (30, 75, 50))])
        l_var = etiqueta("dos variables", INK, 0.55).move_to([3.3, -1.7, 0])
        # separar la voz del murmullo
        t = np.linspace(0, 4, 200)
        L1 = Lienzo(ancho=4.0, alto=1.1, t_rango=(0, 4), v_max=1.0, centro=(-2.8, 2.2))
        L2 = Lienzo(ancho=4.0, alto=0.9, t_rango=(0, 4), v_max=1.0, centro=(-2.8, 0.7))
        voz = L1.curva(t, 0.8 * voz_valores(200), SENAL, 2.4)
        mur = ruido_t(L2, semilla=4, amp=0.2, color=RUIDO)
        pers = persona(AZUL).scale(0.9).move_to([-5.9, 2.2, 0])
        col = colador(CIAN, 1.5, 1.2).move_to([1.2, 1.5, 0])
        a1 = flecha([-0.6, 1.5, 0], [0.3, 1.5, 0])
        F = Flechas(origen=(-4.6, -2.8), largo=2.8, angulo=50, largo_objetivo=2.8)
        l_est = etiqueta("estimar una a partir de la otra", AMBAR, 0.55).move_to([3.0, -2.5, 0])
        Lg = Lienzo(ancho=4.0, alto=1.4, t_rango=(0, 1), v_max=1.0, centro=(4.6, 2.2))
        f1 = lambda u: 0.15 + 0.8 * np.exp(-((u - 0.28) / 0.12) ** 2)
        f2 = lambda u: 0.9 - 0.7 * np.exp(-((u - 0.55) / 0.15) ** 2)
        g1 = curva_f(Lg, f1, 0, 1, CIAN, 4.0)
        g2 = curva_f(Lg, f2, 0, 1, CIAN, 4.0)
        l_g = etiqueta("ganancia en cada ω", CIAN, 0.5).move_to([4.6, 3.4, 0])
        with self.narrar("b1"):
            # «todas sus herramientas»
            self.en("herr")
            self.corte()
            self.play(FadeIn(marco), FadeIn(t1), FadeIn(t2), FadeIn(t3), run_time=self.dur(0.8))

            # «un espectro para cada proceso»
            self.en("espectro")
            self.play(Create(c_xx), FadeIn(n1), run_time=self.dur(0.9))

            # «uno cruzado para cada pareja»
            self.en("cruzado")
            self.play(GrowArrow(fz), FadeIn(n2), run_time=self.dur(0.8))

            # «una forma honesta de medirlos»
            self.en("honesta")
            self.play(FadeIn(n3), run_time=self.dur(0.5))
            self.play(Create(ok), run_time=0.4)

            # «Y en cada frecuencia»
            self.en("encada")
            self.play(Create(cortes), run_time=self.dur(0.8))

            # «dos procesos son dos variables»
            self.en("variables")
            self.play(LaggedStart(*[FadeIn(p) for p in pares], lag_ratio=0.25), FadeIn(l_var),
                      run_time=self.dur(1.2))

            # «Separar la voz del murmullo»
            self.en("separar")
            self.corte()
            self.play(FadeIn(pers), Create(L1.base()), Create(voz), Create(L2.base()), Create(mur),
                      FadeIn(col), GrowArrow(a1), run_time=self.dur(1.4), rate_func=linear)

            # «estimar una variable a partir de otra»
            self.en("estimar")
            self.play(GrowArrow(F.presente), GrowArrow(F.futuro), run_time=self.dur(0.8))
            self.play(Create(F.sombra), FadeIn(l_est), run_time=self.dur(0.6))

            # «frecuencia por frecuencia»
            self.en("fxf")
            self.play(Create(Lg.base()), Create(g1), FadeIn(l_g), run_time=self.dur(0.8))
            self.play(Transform(g1, g2), run_time=self.dur(1.2))

        self.wait(1.0)
        self.limpiar()
