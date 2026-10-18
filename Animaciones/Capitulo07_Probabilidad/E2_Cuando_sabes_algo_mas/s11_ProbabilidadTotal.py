"""Escena 11 — Probabilidad total: el denominador es la suma de todos los caminos."""
from comun.escena import *


class ProbabilidadTotal(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        pb = MathTex(r"P(B)", color=AMBAR).scale(2.0).move_to([-5.0, 3.2, 0])
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.5).next_to(pb, RIGHT, buff=0.2)
        tira = tira_test07(0.6).move_to([-5.9, 1.0, 0])
        mas = Text("+", color=ERROR, weight=BOLD).scale(1.3).move_to(tira.ventana)
        a = Arbol07("Mundo", [("Enfermo", ROJO), ("Sano", VERDE)],
                    [[("+", ERROR), ("−", INK)], [("+", ERROR), ("−", INK)]],
                    [r"0{,}01", r"0{,}99"], [[r"0{,}99", r"0{,}01"], [r"0{,}05", r"0{,}95"]],
                    centro=(-0.8, -0.2), ancho=8.6, alto=4.4, escala=0.65)
        r_e = a.rama(0, 0, AMBAR)
        r_s = a.rama(1, 0, AMBAR)
        prod_e = MathTex(r"0{,}01\cdot 0{,}99", color=AMBAR).scale(1.0).next_to(a.hojas[0][0], RIGHT, buff=0.3)
        prod_s = MathTex(r"0{,}99\cdot 0{,}05", color=AMBAR).scale(1.0).next_to(a.hojas[1][0], RIGHT, buff=0.3)
        suma = MathTex("+", color=TXT).scale(1.6).move_to([(prod_e.get_center()[0]), (prod_e.get_center()[1] + prod_s.get_center()[1]) / 2, 0])
        total = Text("Ley de probabilidad total", color=AMBAR, weight=BOLD).scale(0.85).move_to([3.0, 3.2, 0])
        mundo = Rectangle(width=8.0, height=2.2, color=INK, stroke_width=3).move_to([0, 1.0, 0])
        mitad = Rectangle(width=1.6, height=2.2, color=ROJO, stroke_width=3).set_fill(ROJO, 0.25)
        mitad.align_to(mundo, LEFT).match_y(mundo)
        resto = Rectangle(width=6.4, height=2.2, color=VERDE, stroke_width=3).set_fill(VERDE, 0.2)
        resto.align_to(mundo, RIGHT).match_y(mundo)
        t_m = Text("Caso 1", color=ROJO, weight=BOLD).scale(0.6).move_to(mitad)
        t_r = Text("Caso 2", color=VERDE, weight=BOLD).scale(0.8).move_to(resto)
        nosolapan = Text("No se solapan", color=INK).scale(0.7).move_to([0, -0.4, 0])
        f = formula("P(B)", "=", r"P(B\mid A)P(A)", "+", r"P(B\mid \bar A)P(\bar A)", escala=1.3).move_to([0, -2.4, 0])

        with self.narrar("b1"):
            # «Falta el denominador»
            self.en("falta")
            self.pop(pb)
            self.play(FadeIn(interr), run_time=self.dur(0.3))

            # «En el test»
            self.en("en_test")
            self.play(FadeIn(tira), run_time=self.dur(0.4))
            self.pop(mas, sonido="error")

            # «¿de cuántas formas se puede dar positivo?»
            self.en("formas")
            self.play(FadeIn(a), run_time=self.dur(1.2))

            # «Estando enfermo»
            self.en("enfermo")
            self.play(Create(r_e), run_time=self.dur(0.6))

            # «estando sano»
            self.en("sano")
            self.play(Create(r_s), run_time=self.dur(0.6))

            # «Cada camino vale»
            self.en("camino")
            self.play(FadeIn(prod_e), FadeIn(prod_s), run_time=self.dur(0.7))

            # «de dar positivo por ese camino»
            self.en("por_camino")
            self.resaltar(prod_e, prod_s, color=AMBAR, escala=1.2)

            # «y se suman»
            self.en("suman")
            self.pop(suma)

            # «ley de probabilidad total»
            self.en("total")
            self.pop(total)

            # «casos que no se solapan»
            self.en("casos")
            self.corte()
            self.play(Create(mundo), FadeIn(mitad), FadeIn(resto), FadeIn(t_m), FadeIn(t_r), run_time=self.dur(0.9))
            self.play(FadeIn(nosolapan), run_time=self.dur(0.4))

            # «calculas cada caso, y sumas»
            self.en("sumas")
            self.play(LaggedStart(*[FadeIn(p) for p in f], lag_ratio=0.3), run_time=self.dur(1.6))
        self.wait(1.0)
        self.limpiar()
