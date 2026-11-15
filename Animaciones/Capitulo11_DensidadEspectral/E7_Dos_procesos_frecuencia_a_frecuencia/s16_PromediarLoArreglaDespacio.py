"""Escena 16 — Promediar arregla la trampa, pero despacio: 1/M, y la regla práctica."""
from comun.escena import *


class PromediarLoArreglaDespacio(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        t = np.linspace(0, 4, 200)
        L1 = Lienzo(ancho=5.2, alto=1.1, t_rango=(0, 4), v_max=1.0, centro=(-3.6, 2.5))
        L2 = Lienzo(ancho=5.2, alto=1.1, t_rango=(0, 4), v_max=1.0, centro=(-3.6, 1.2))
        g1 = ruido_t(L1, semilla=7, amp=0.2, color=CIAN)
        g2 = ruido_t(L2, semilla=12, amp=0.2, color=MAGENTA)
        sinrel = etiqueta("sin relación", INK, 0.5).move_to([-3.6, 0.2, 0])
        # promediar trozos: varias curvas finas y su promedio, que se calma despacio
        Lp = Lienzo(ancho=5.2, alto=1.6, t_rango=(0, 4), v_max=1.0, centro=(-3.6, -1.6))
        finas = VGroup(*[ruido_t(Lp, semilla=20 + i, amp=0.28, color=INK, ancho=1.5, puntos=120) for i in range(5)])
        for f_ in finas:
            f_.set_stroke(opacity=0.5)
        prom = Lp.curva(t, np.mean([0.28 * serie(20 + i, 200, 0.0) for i in range(5)], axis=0), AMBAR, 3.5)
        lento = flecha([-0.6, -1.0, 0], [-0.6, -2.4, 0], AMBAR, 3)
        l_len = etiqueta("despacio", AMBAR, 0.5).move_to([-0.3, -3.0, 0])
        l_c = formula(r"|\hat\gamma|^2", escala=0.9, colores={0: AMBAR}).move_to([2.6, 3.2, 0])
        l_m = etiqueta("M trozos", TXT, 0.55).move_to([5.4, 3.2, 0])
        filas = ["M = 1  →  1", "M = 2  →  0,5", "M = 8  →  0,12", "M = 64  →  0,016"]
        tabla = VGroup(*[Text(f, color=TXT).scale(0.55) for f in filas]).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        tabla.move_to([3.2, 0.8, 0])
        aprox = formula(r"|\hat\gamma|^2\approx\frac1M", escala=1.0, colores={0: AMBAR}).move_to([3.7, 2.4, 0])
        barra_ = Rectangle(width=0.5, height=0.35, color=ROJO, stroke_width=2).set_fill(ROJO, 0.5).move_to([6.2, -1.2, 0])
        interr = self.palabra("?", AMBAR, 0.8).move_to([6.2, -0.3, 0])
        l_nada = etiqueta("sin relación", INK, 0.5).move_to([5.6, -2.0, 0])
        # la regla
        Lm = Lienzo(ancho=6.0, alto=2.6, t_rango=(0, 1), v_max=1.0, centro=(-2.4, -0.2))
        ej = ejes_L(Lm, 0, 1.15, x_eje=0.0)
        umbral = Line(Lm.p(0, 0.15), Lm.p(1, 0.15), color=AMBAR, stroke_width=3)
        l_u = formula(r"1/M", escala=0.8, colores={0: AMBAR}).move_to(Lm.p(1.0, 0.15) + RIGHT * 0.75)
        d_bajo = Dot(Lm.p(0.35, 0.07), radius=0.1, color=INK)
        d_alto = Dot(Lm.p(0.7, 0.7), radius=0.1, color=VERDE)
        l_reg = caja("la regla", AMBAR, ancho=2.2, alto=0.7, scale=0.5).move_to([-2.4, 3.3, 0])
        ok = tilde(VERDE, 0.5).move_to(Lm.p(0.85, 0.7))
        diez = formula(r"M<10", escala=1.0, colores={0: ROJO}).move_to([4.2, 2.0, 0])
        norep = etiqueta("no reportar", ROJO, 0.6).move_to([4.2, 0.9, 0])
        sl = sello("prohibido", ROJO).scale(0.9).move_to([4.2, -0.6, 0])
        with self.narrar("b1"):
            # «Promediar lo arregla»
            self.en("promediar")
            self.play(*[Create(f_) for f_ in finas], Create(Lp.base()), run_time=self.dur(0.9), rate_func=linear)
            self.play(Create(prom), run_time=self.dur(0.4))

            # «pero despacio»
            self.en("despacio")
            self.play(GrowArrow(lento), FadeIn(l_len), run_time=self.dur(0.8))

            # «Con dos grabaciones sin relación»
            self.en("dos")
            self.play(Create(L1.base()), Create(g1), Create(L2.base()), Create(g2), FadeIn(sinrel),
                      run_time=self.dur(1.0), rate_func=linear)

            # «la coherencia al cuadrado estimada»
            self.en("cuadrado")
            self.pop(l_c)

            # «eme trozos»
            self.en("mtrozos")
            self.pop(l_m)

            # «uno sobre eme»
            self.en("unosobre")
            self.play(FadeIn(aprox), FadeIn(tabla[0]), FadeIn(tabla[1]), run_time=self.dur(0.8))

            # «Con ocho trozos, cero coma uno dos»
            self.en("ocho")
            self.play(FadeIn(tabla[2]), FadeIn(tabla[3]), run_time=self.dur(0.6))
            self.resaltar(tabla[2], color=AMBAR)

            # «parece que hay algo»
            self.en("algo")
            self.play(FadeIn(barra_), FadeIn(interr), run_time=self.dur(0.6))

            # «y no hay nada»
            self.en("nada")
            self.play(FadeIn(l_nada), Create(tachar(interr)), run_time=self.dur(0.6))

            # «La regla»
            self.en("regla")
            self.corte()
            self.play(FadeIn(l_reg), Create(ej), run_time=self.dur(0.7))

            # «bastante mayores que uno sobre eme»
            self.en("mayores")
            self.play(Create(umbral), FadeIn(l_u), FadeIn(d_bajo), FadeIn(d_alto), run_time=self.dur(0.9))
            self.play(FadeIn(ok), run_time=0.3)

            # «con menos de unos diez trozos»
            self.en("diez")
            self.pop(diez)

            # «no creer ninguna»
            self.en("ninguna")
            self.play(FadeIn(norep), run_time=0.3)
            self.pop(sl, sonido="impacto")

        self.wait(1.0)
        self.limpiar()
