"""Escena 01 — Gancho: una medición, dos, y el promedio que vuelve al error de una."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        base_y = -2.0
        R = RectaR(centro=(-3.4, 0.8), ancho=5.6, x_rango=(-1.5, 1.5))
        punto = Dot(R.p(0.35), radius=0.18, color=MEDIDA)
        r_et = MathTex("r", color=MEDIDA).scale(1.0).next_to(punto, UP, buff=0.12)
        cas = casillas(4, rojas=(0,), centro=(-3.4, -1.0), lado=0.8)

        P = Plano2(centro=(-3.4, 0.1), u=1.45)
        d1 = Dot(P.p(0.7, -0.4), radius=0.14, color=MEDIDA)
        d2 = Dot(P.p(-0.3, 0.6), radius=0.14, color=MEDIDA)
        d3 = Dot(P.p(-0.6, -0.5), radius=0.14, color=MEDIDA)
        puntos = VGroup(d1, d2, d3)
        diag = DashedLine(P.p(-1.3, -1.3), P.p(1.3, 1.3), color=AMBAR, stroke_width=3)
        promedio = MathTex(r"\frac{r_1+r_2}{2}", color=AMBAR).scale(1.2).move_to([-3.4, 3.3, 0])

        b1 = barra_v(2.4, base_y, 3.0, 1.2)
        b2 = barra_v(4.1, base_y, 2.25, 1.2)
        b3 = barra_v(5.8, base_y, 3.0, 1.2)
        l1 = MathTex(r"\tfrac14", color=ERROR).scale(1.1).next_to(b1, UP, buff=0.1)
        l2 = MathTex(r"\tfrac{3}{16}", color=ERROR).scale(1.1).next_to(b2, UP, buff=0.1)
        l3 = MathTex(r"\tfrac14", color=ERROR).scale(1.1).next_to(b3, UP, buff=0.1)
        suelo = Line([1.5, base_y, 0], [6.7, base_y, 0], color=INK, stroke_width=2)
        frase = self.palabra("Más datos no bastan", AMBAR, 1.4).move_to([0, -3.2, 0])

        with self.narrar("b1"):
            # «Con una medición»
            self.en("una")
            self.play(FadeIn(R), FadeIn(punto), FadeIn(r_et), run_time=self.dur(0.6))

            # «una de cada cuatro veces»
            self.en("cuatro")
            self.play(FadeIn(cas), FadeIn(suelo), run_time=self.dur(0.4))
            self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=self.dur(0.6))

            # «Con dos»
            self.en("dos")
            self.play(FadeOut(R), FadeOut(punto), FadeOut(r_et), FadeOut(cas), run_time=0.25)
            self.play(FadeIn(P), FadeIn(puntos), run_time=self.dur(0.5))

            # «menos»
            self.en("menos")
            self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=self.dur(0.6))

            # «si las promedias»
            self.en("promedias")
            self.play(FadeIn(promedio), Create(diag), run_time=self.dur(0.5))
            destinos = []
            for p in puntos:
                x, y = (p.get_center()[0] - P.cx) / P.u, (p.get_center()[1] - P.cy) / P.u
                destinos.append(P.p((x + y) / 2, (x + y) / 2))
            self.play(*[p.animate.move_to(d) for p, d in zip(puntos, destinos)], run_time=self.dur(0.4))

            # «vuelves a equivocarte»
            self.en("vuelves")
            self.play(GrowFromEdge(b3, DOWN), FadeIn(l3), run_time=self.dur(0.5))

            # «Más datos no bastan»
            self.en("nobastan")
            self.pop(frase)
        self.wait(1.0)
        self.limpiar()
