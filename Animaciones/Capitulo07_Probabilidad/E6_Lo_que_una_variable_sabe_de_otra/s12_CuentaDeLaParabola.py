"""Escena 12 — La cuenta: la covarianza de (X, X²) da cero por simetría."""
from comun.escena import *


class CuentaDeLaParabola(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        # izquierda: la uniforme con su espejo, y la curva x³ con sus dos áreas
        rect = Rectangle(width=5.0, height=1.0, color=SENAL, fill_opacity=0.35, stroke_width=3).move_to([-3.4, 2.6, 0])
        espejo = DashedLine([-3.4, 3.4, 0], [-3.4, 1.4, 0], color=AMBAR, stroke_width=3)
        cero = Text("0", color=AMBAR).scale(0.6).move_to([-3.4, 1.1, 0])
        ax, et = ejes((-1.3, 1.3, 1), (-1.3, 1.3, 1), ancho=6.0, alto=3.4, x_label="x", y_label="x^3")
        g = VGroup(ax, et).move_to([-3.4, -1.3, 0])
        cub = ax.plot(lambda x: x ** 3, x_range=[-1, 1, 0.02], color=SENAL, stroke_width=4)
        a_izq = ax.get_area(cub, x_range=[-1, 0], color=ROJO, opacity=0.5)
        a_der = ax.get_area(cub, x_range=[0, 1], color=VERDE, opacity=0.5)
        # derecha: las cuentas
        f = formula(r"\sigma_{XY}", "=", "E[XY]", "-", r"\mu_X\mu_Y", escala=1.3, colores={0: AMBAR}).move_to([3.5, 3.0, 0])
        mu = formula(r"\mu_X", "=", "0", escala=1.4, colores={0: SENAL}).move_to([3.5, 1.7, 0])
        cu = formula("E[XY]", "=", r"E[X\cdot X^2]", "=", "E[X^3]", escala=1.1).move_to([3.3, 0.3, 0])
        m0 = formula("E[X^3]", "=", "0", escala=1.4).move_to([3.5, -1.3, 0])
        c0 = formula(r"\sigma_{XY}", "=", "0", escala=1.9, colores={0: AMBAR, 2: AMBAR}).move_to([3.5, -2.9, 0])
        for m in (f, mu, cu, m0, c0):
            oculta(m)
            self.add(m)
        with self.narrar("b1"):
            # «Calculemos su covarianza»
            self.en("calc")
            self.play(*revelar(*f), run_time=self.dur(0.8))

            # «La media de equis es cero»
            self.en("mu0")
            self.play(*revelar(*mu), run_time=self.dur(0.6))
            self.play(f[3].animate.set_opacity(0.25), f[4].animate.set_opacity(0.25), run_time=self.dur(0.4))

            # «simétrica alrededor de cero»
            self.en("simetria")
            self.play(FadeIn(rect), Create(espejo), FadeIn(cero), run_time=self.dur(0.8))
            fl = CurvedArrow(rect.get_corner(UL) + DOWN * 0.45 + RIGHT * 0.4, rect.get_corner(UR) + DOWN * 0.45 + LEFT * 0.4,
                             color=AMBAR, angle=-PI / 3, stroke_width=3)
            self.play(Create(fl), run_time=self.dur(0.5))

            # «la covarianza es simplemente la esperanza de equis por i griega»
            self.en("exy")
            self.play(f[3].animate.set_opacity(0), f[4].animate.set_opacity(0), f[2].animate.set_color(AMBAR),
                      run_time=self.dur(0.7))

            # «la esperanza de equis al cubo»
            self.en("cubo")
            self.play(*revelar(*cu), run_time=self.dur(1.0))

            # «negativo a la izquierda»
            self.en("izq")
            self.play(FadeOut(VGroup(rect, espejo, cero, fl)), Create(g), Create(cub), FadeIn(a_izq),
                      run_time=self.dur(0.9))

            # «positivo a la derecha»
            self.en("der")
            self.play(FadeIn(a_der), run_time=self.dur(0.6))

            # «en la misma medida»
            self.en("medida")
            igual = MathTex("=", color=AMBAR).scale(1.4).move_to(ax.c2p(-0.25, 1.15))
            self.play(FadeIn(igual, scale=0.5), run_time=self.dur(0.5))

            # «Su media es cero»
            self.en("media0")
            self.play(*revelar(*m0), run_time=self.dur(0.6))

            # «La covarianza es cero»
            self.en("cov0")
            self.play(*revelar(*c0), run_time=self.dur(0.5))
            self.sfx("exito")
        self.wait(1.0)
        self.limpiar()
