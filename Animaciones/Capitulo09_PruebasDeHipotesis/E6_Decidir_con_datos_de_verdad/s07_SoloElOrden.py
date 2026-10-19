"""Escena 07 — Solo el orden: elevar las puntuaciones al cuadrado no cambia la curva ni el área."""
from comun.escena import *
from comun.figuras_c9e6 import *


class SoloElOrden(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.dos_cosas()
        self.experimento()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def dos_cosas(self):
        with self.narrar("b1"):
            # «En una puntuación»
            self.en("ficha")
            f = ficha6(1, None, lado=1.4)
            n = Text("0,65", color=TXT, weight=BOLD).scale(0.9).next_to(f, RIGHT, buff=0.3)
            g = VGroup(f, n).move_to(ORIGIN)
            self.pop(g)

            # «dos cosas distintas»
            self.en("dos")
            ta = RoundedRectangle(corner_radius=0.2, width=4.6, height=5.0, color=SENAL, stroke_width=3).set_fill(SENAL, 0.06)
            tb = RoundedRectangle(corner_radius=0.2, width=4.6, height=5.0, color=ESTIMACION, stroke_width=3).set_fill(ESTIMACION, 0.06)
            ta.move_to([-1.2, -0.3, 0])
            tb.move_to([1.2, -0.3, 0])
            self.play(g.animate.scale(0.6).move_to([0, 2.9, 0]), FadeIn(ta), FadeIn(tb), run_time=self.dur(0.5))

            # «conviene separarlas»
            self.en("separar")
            self.play(ta.animate.move_to([-3.4, -0.4, 0]), tb.animate.move_to([3.4, -0.4, 0]), run_time=self.dur(0.5))

            # «ordene bien»
            self.en("orden")
            ra = Text("Orden", color=SENAL, weight=BOLD).scale(0.6).move_to(ta.get_top() + DOWN * 0.45)
            col = columna6(centro=(-3.6, -0.75), paso=0.52, lado=0.44, escala=0.34)
            self.play(FadeIn(ra), FadeIn(col), run_time=self.dur(0.5))

            # «los positivos, por encima»
            self.en("encima")
            self.play(*[col.fichas[i].animate(rate_func=there_and_back).shift(UP * 0.12) for i in (0, 1, 3, 5)],
                      *[col.fichas[i].marco.animate.set_fill(opacity=0.65) for i in (0, 1, 3, 5)],
                      run_time=self.dur(0.5))

            # «La otra»
            self.en("otra")
            self.play(tb.animate.set_fill(ESTIMACION, 0.2).set_stroke(width=5), run_time=self.dur(0.4))

            # «qué significa el número»
            self.en("significa")
            rb = Text("Significado", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(tb.get_top() + DOWN * 0.45)
            q = Text("0,65 = ?", color=TXT).scale(0.75).move_to(tb.get_center())
            self.play(FadeIn(rb), FadeIn(q, shift=UP * 0.1), run_time=self.dur(0.45))

    # ------------------------------------------------------------ b2
    def experimento(self):
        with self.narrar("b2"):
            # «Haz un experimento»
            self.en("exp")
            self.corte()
            col = columna6(centro=(-5.0, -0.2), paso=0.76)
            P = PlanoRoc9()
            E = Escalera6(P)
            esc = E.todo()
            self.add(col, P, P.diagonal(), esc)
            self.play(FadeIn(col), run_time=self.dur(0.3))

            # «al cuadrado»
            self.en("cuadrado")
            x2 = MathTex(r"x^2", color=ESTIMACION).scale(1.1).move_to([-4.6, 3.35, 0])
            self.pop(x2)

            # «Los números cambian»
            self.en("cambian")
            nuevos = [Text(num(p * p), color=ESTIMACION).scale(0.4).move_to(f.num, aligned_edge=LEFT)
                      for (p, _), f in zip(CASOS6, col.fichas)]
            self.play(LaggedStart(*[Transform(f.num, n) for f, n in zip(col.fichas, nuevos)], lag_ratio=0.12),
                      run_time=self.dur(1.2))

            # «el orden no»
            self.en("orden")
            self.play(LaggedStart(*[f.marco.animate(rate_func=there_and_back).scale(1.2) for f in col.fichas],
                                  lag_ratio=0.1), run_time=self.dur(0.8))

            # «La escalera es idéntica»
            self.en("identica")
            copia = E.todo(color=VERDE, ancho=6).shift(RIGHT * 1.0 + UP * 0.6)
            self.add(copia)
            self.play(copia.animate.shift(LEFT * 1.0 + DOWN * 0.6), run_time=self.dur(0.6))
            self.play(copia.animate.set_stroke(ROC), run_time=self.dur(0.3))

            # «y el área también»
            self.en("area")
            ar = E.area()
            ig = MathTex(r"\frac{13}{16}", "=", r"\frac{13}{16}", color=TXT).scale(1.0)
            ig[1].set_color(VERDE)
            ig.move_to([-1.6, 1.4, 0])
            self.play(FadeIn(ar), Write(ig), run_time=self.dur(0.6))

            # «solo ve el orden»
            self.en("solo")
            t = tarjeta6("Mismo orden = Misma curva", VERDE, ancho=4.4).move_to([-1.0, -3.3, 0])
            self.pop(t)
