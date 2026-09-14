"""Escena 7 - Cuando la recta alcanza y cuando no.

Si (X, Y) son gaussianas bivariadas, E[Y|X] YA ES una recta y el LMMSE
coincide con el MMSE: no se pierde nada. Si la relacion es no lineal, la
mejor recta puede ser inutil aunque E[Y|X] describa todo perfectamente.

    manim -pql s07_lineal_o_no.py LinealONo
"""
from manim import *
import numpy as np
from comun import *

N = 240
_rng = np.random.default_rng(77)


class LinealONo(Scene):
    def construct(self):
        configurar()

        tit = titulo("¿Cuándo alcanza con una recta?")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # =========================================== CASO 1: gaussiano
        cabeza1 = VGroup(
            Text("Caso 1:", color=INK).scale(0.55),
            Text("(X, Y) gaussianas bivariadas", color=VERDE).scale(0.6),
        ).arrange(RIGHT, buff=0.22)
        cabeza1.next_to(tit, DOWN, buff=0.35)
        self.play(FadeIn(cabeza1))

        ax, lab = ejes([-3.2, 3.2, 3.2], [-3.2, 3.2, 3.2], ancho=5.4, alto=4.0,
                       x_label="x", y_label="y")
        ax.shift(DOWN * 0.7)
        lab[0].next_to(ax.x_axis.get_end(), DR, buff=0.1)
        lab[1].next_to(ax.y_axis.get_end(), UR, buff=0.08)

        rho = 0.75
        xs, ys = muestras_gauss(N, rho, semilla=3)
        puntos = nube(ax, xs, ys, color=AZUL, radio=0.032, opacidad=0.55)

        self.play(Create(ax), FadeIn(lab))
        self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in puntos],
                              lag_ratio=0.003, run_time=1.4))
        self.wait(0.4)

        mmse1 = ax.plot(lambda x: rho * x, x_range=[-3.2, 3.2], color=VERDE,
                        stroke_width=6)
        lmmse1 = ax.plot(lambda x: rho * x, x_range=[-3.2, 3.2], color=AMBAR,
                         stroke_width=3)
        m_lbl = MathTex(r"E[Y|X]", color=VERDE).scale(0.6)
        m_lbl.next_to(ax.c2p(2.2, rho * 2.2), UL, buff=0.05)
        l_lbl = MathTex(r"\hat{Y}_\ell", color=AMBAR).scale(0.6)
        l_lbl.next_to(ax.c2p(-2.4, rho * -2.4), DR, buff=0.05)

        self.play(Create(mmse1), FadeIn(m_lbl))
        self.wait(0.5)
        self.play(Create(lmmse1), FadeIn(l_lbl))
        self.wait(0.8)

        v1 = veredicto(True, "la media condicional YA es una recta")
        v1.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(v1, scale=1.15))
        self.wait(1.2)
        igual = MathTex(r"\text{LMMSE} \;=\; \text{MMSE}", color=VERDE).scale(0.7)
        igual.next_to(v1, UP, buff=0.28)
        self.play(Write(igual))
        self.wait(2.0)

        # =========================================== CASO 2: no lineal
        self.play(FadeOut(VGroup(v1, igual, mmse1, lmmse1, m_lbl, l_lbl,
                                 puntos)))

        cabeza2 = VGroup(
            Text("Caso 2:", color=INK).scale(0.55),
            Text("Y = X²  con  X uniforme en [−1, 1]", color=ROJO).scale(0.6),
        ).arrange(RIGHT, buff=0.22)
        cabeza2.move_to(cabeza1)
        self.play(Transform(cabeza1, cabeza2))

        # se reescala el eje para que la parabola se vea comoda; una pizca
        # de ruido vertical hace visibles los puntos alrededor de la curva
        xs2 = _rng.uniform(-1, 1, N) * 2.6
        ys2 = (xs2 / 2.6) ** 2 * 5.0 - 2.2 + _rng.normal(0, 0.14, N)
        puntos2 = nube(ax, xs2, ys2, color=MAGENTA, radio=0.034, opacidad=0.7)
        self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in puntos2],
                              lag_ratio=0.003, run_time=1.4))
        self.wait(0.4)

        mmse2 = ax.plot(lambda x: (x / 2.6) ** 2 * 5.0 - 2.2,
                        x_range=[-2.6, 2.6, 0.02], color=VERDE, stroke_width=5,
                        use_smoothing=False)
        m2_lbl = MathTex(r"E[Y|X]", color=VERDE).scale(0.6)
        m2_lbl.next_to(ax.c2p(2.2, (2.2 / 2.6) ** 2 * 5.0 - 2.2), UL, buff=0.05)
        self.play(Create(mmse2), FadeIn(m2_lbl))
        self.wait(0.6)

        exacto = nota("acá $E[Y|X]$ describe la relación EXACTAMENTE: "
                      "el error es cero", scale=0.44)
        exacto.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(exacto))
        self.wait(1.6)
        self.play(FadeOut(exacto))

        # la mejor recta: por simetria, pendiente cero
        lmmse2 = ax.plot(lambda x: float(np.mean(ys2)), x_range=[-3.2, 3.2],
                         color=AMBAR, stroke_width=4)
        l2_lbl = MathTex(r"\hat{Y}_\ell", color=AMBAR).scale(0.6)
        l2_lbl.next_to(ax.c2p(-2.9, float(np.mean(ys2))), UL, buff=0.06)
        self.play(Create(lmmse2), FadeIn(l2_lbl))
        self.wait(0.6)

        v2 = veredicto(False, "la mejor recta es horizontal: ρ = 0")
        v2.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(v2, scale=1.15))
        self.wait(1.4)

        peor = nota("X determina Y por completo, y aun así el estimador lineal "
                    "ignora la medición", scale=0.44)
        peor.next_to(v2, UP, buff=0.26)
        self.play(FadeIn(peor))
        self.wait(2.4)

        # =========================================== cierre
        self.play(FadeOut(VGroup(ax, lab, puntos2, mmse2, m2_lbl, lmmse2,
                                 l2_lbl, v2, peor, cabeza1)))
        cierre = VGroup(
            Text("ρ = 0 no significa “independientes”.", color=TXT).scale(0.62),
            Text("Significa “sin relación LINEAL”.", color=AMBAR).scale(0.62),
            nota("El LMMSE solo ve la parte lineal del vínculo.\n"
                 "Cuando E[Y|X] es una recta —caso gaussiano— no pierde nada.",
                 scale=0.5),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0], shift=UP * 0.12))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
