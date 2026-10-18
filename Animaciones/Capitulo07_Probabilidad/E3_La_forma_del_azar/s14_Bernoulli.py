"""Escena 14 — Bernoulli: la distribución del bit."""
from comun.escena import *


class Bernoulli(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        g, huecos, centros = huecos_tres()
        ax = Axes(x_range=[-0.8, 1.8, 1], y_range=[0, 1.0, 0.25], x_length=8.0, y_length=3.8,
                  axis_config={"color": INK, "stroke_width": 2, "include_ticks": False,
                               "tip_width": 0.16, "tip_height": 0.16}).move_to([0, -0.7, 0])
        n0 = formula("0", escala=0.9, colores={0: INK}).next_to(ax.c2p(0, 0), DOWN, buff=0.15)
        n1 = formula("1", escala=0.9, colores={0: INK}).next_to(ax.c2p(1, 0), DOWN, buff=0.15)
        p = 0.7

        def barra(x, h, color):
            a, b = ax.c2p(x - 0.2, 0), ax.c2p(x + 0.2, h)
            return Rectangle(width=b[0] - a[0], height=b[1] - a[1], stroke_color=color, stroke_width=3,
                             fill_color=color, fill_opacity=0.5).move_to([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0])

        with self.narrar("b1"):
            self.en("pocas")                                  # «unas pocas distribuciones»
            self.play(Create(huecos), run_time=self.dur(0.8))
            self.en("todo_tiempo")                            # «todo el tiempo»
            self.play(LaggedStart(*[h.animate(rate_func=there_and_back).scale(1.08) for h in huecos],
                                  lag_ratio=0.25), run_time=self.dur(1.2))
            self.en("nombre")                                 # «por su nombre»
            self.play(huecos[0].animate.set_stroke(AMBAR), run_time=self.dur(0.4))
            self.en("bernoulli")                              # «la de Bernoulli»
            nom = Text("Bernoulli", color=AMBAR, weight=BOLD).scale(0.65).move_to(centros[0])
            self.pop(nom)
            self.en("bit")                                    # «cero o uno, como un bit»
            self.play(Create(ax), FadeIn(n0), FadeIn(n1), run_time=self.dur(0.9))
            self.en("p")                                      # «Vale uno con probabilidad pe»
            b1 = barra(1, p, VERDE)
            lp = formula("p", escala=1.2, colores={0: VERDE}).next_to(b1, UP, buff=0.2)
            self.play(GrowFromEdge(b1, DOWN), FadeIn(lp), run_time=self.dur(0.9))
            self.en("uno_menos_p")                            # «cero con probabilidad uno menos pe»
            b0 = barra(0, 1 - p, AZUL)
            l0 = formula("1", "-", "p", escala=1.2, colores={2: VERDE}).next_to(b0, UP, buff=0.2)
            self.play(GrowFromEdge(b0, DOWN), FadeIn(l0), run_time=self.dur(0.9))
            self.en("barras")                                 # «dos barras»
            marco = SurroundingRectangle(VGroup(b0, b1, lp, l0, n0, n1), color=AMBAR, buff=0.25, corner_radius=0.12)
            self.play(Create(marco), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
