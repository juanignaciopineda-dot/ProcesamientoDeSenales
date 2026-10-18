"""Escena 08 — La covarianza: definición, desarrollo y fórmula práctica."""
from comun.escena import *


class FormulaDeLaCovarianza(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        # cuatro renglones, alineados a la izquierda
        L1 = formula(r"\sigma_{XY}", "=", "E", r"\big[", r"(X-\mu_X)", r"(Y-\mu_Y)", r"\big]", escala=1.2,
                     colores={0: AMBAR})
        L2 = formula("=", "E", r"\big[", r"XY", r"-\mu_Y X", r"-\mu_X Y", r"+\mu_X\mu_Y", r"\big]", escala=1.2)
        L3 = formula("=", "E[XY]", r"-\mu_Y\,\mu_X", r"-\mu_X\,\mu_Y", r"+\mu_X\mu_Y", escala=1.2)
        L4 = formula("=", "E[XY]", r"-\mu_X\mu_Y", escala=1.4, colores={1: AMBAR, 2: MEDIDA})
        for L, y in ((L1, 2.9), (L2, 1.4), (L3, -0.1), (L4, -1.7)):
            L.move_to([0, y, 0]).align_to([-6.6, 0, 0], LEFT)
            oculta(L)
            self.add(L)
        # el signo «=» de L2, L3 y L4 queda bajo el de L1
        for L in (L2, L3, L4):
            L.shift(RIGHT * (L1[1].get_left()[0] - L[0].get_left()[0]))
        self.L1, self.L2, self.L3, self.L4 = L1, L2, L3, L4
        with self.narrar("b1"):
            # «La esperanza de ese producto»
            self.en("esp")
            self.play(LaggedStart(*revelar(L1[2], L1[3], L1[4], L1[5], L1[6]), lag_ratio=0.3), run_time=self.dur(1.0))

            # «medido desde el centro»
            self.en("centro")
            self.play(L1[4].animate.set_color(AMBAR), L1[5].animate.set_color(AMBAR), run_time=self.dur(0.6))

            # «es la covarianza»
            self.en("cov")
            self.play(*revelar(L1[0], L1[1]), run_time=self.dur(0.5))

            # «la misma cuenta que hicimos para la varianza»
            self.en("misma")
            rot = Text("Como con la varianza", color=INK, slant=ITALIC).scale(0.6).move_to([4.6, 2.9, 0])
            self.play(FadeIn(rot, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «desarrollando el producto»
            self.en("desarrollo")
            self.play(LaggedStart(*revelar(*L2), lag_ratio=0.12), run_time=self.dur(1.2))

            # «usando la linealidad»
            self.en("lineal")
            self.play(LaggedStart(*revelar(*L3), lag_ratio=0.12), run_time=self.dur(1.1))

            # «la fórmula práctica»
            self.en("practica")
            self.play(*revelar(*L4), run_time=self.dur(0.6))
            caja_f = SurroundingRectangle(L4, color=AMBAR, buff=0.18, stroke_width=3)
            self.play(Create(caja_f), run_time=self.dur(0.5))

            # «la correlación menos el producto de las medias»
            self.en("lectura")
            t1 = Text("Correlación", color=AMBAR).scale(0.6).next_to(L4[1], DOWN, buff=0.3).shift(LEFT * 0.5)
            t2 = Text("Producto de las medias", color=MEDIDA).scale(0.6).next_to(L4[2], DOWN, buff=0.3).shift(RIGHT * 1.0)
            self.play(FadeIn(t1), FadeIn(t2), run_time=self.dur(0.7))

            # «la diferencia que vimos antes»
            self.en("antes")
            gris = Rectangle(width=0.102 * 14, height=0.6, color=INK, fill_opacity=0.7, stroke_width=0)
            ambar = Rectangle(width=(0.27 - 0.102) * 14, height=0.6, color=AMBAR, fill_opacity=0.8, stroke_width=0)
            gris.move_to([3.2 + gris.width / 2, -1.3, 0])
            ambar.next_to(gris, RIGHT, buff=0)
            n1 = Text("0,102", color=INK).scale(0.6).next_to(gris, DOWN, buff=0.12, aligned_edge=LEFT)
            n2 = Text("0,168", color=AMBAR).scale(0.6).next_to(ambar, DOWN, buff=0.12, aligned_edge=RIGHT)
            self.play(FadeIn(gris), FadeIn(ambar), FadeIn(n1), FadeIn(n2), run_time=self.dur(0.7))

            # «la varianza es la covarianza de una variable consigo misma»
            self.en("var_cov")
            vc = formula(r"\sigma_{XX}", "=", r"\sigma_X^2", escala=1.6, colores={0: AMBAR, 2: AMBAR}).move_to([4.4, -3.0, 0])
            self.pop(vc)
        self.wait(1.0)
        self.limpiar()
