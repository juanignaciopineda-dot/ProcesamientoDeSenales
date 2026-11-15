"""Escena 10 — Tres muestras: la tabla de 3 × 3 de covarianzas."""
from comun.escena import *


class TablaDeTres(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        lado = 1.15
        cx, cy = -3.3, -0.5

        def celda(i, j):
            return np.array([cx + (j - 1) * lado, cy - (i - 1) * lado, 0])

        casillas = {(i, j): Square(lado, color=INK, stroke_width=2.5).move_to(celda(i, j))
                    for i in range(3) for j in range(3)}
        tabla = VGroup(*casillas.values())
        diag = [(0, 0), (1, 1), (2, 2)]
        vec = [(0, 1), (1, 0), (1, 2), (2, 1)]
        esq = [(0, 2), (2, 0)]

        def valor(ij, txt, color):
            return Text(txt, color=color, weight=BOLD).scale(0.5).move_to(celda(*ij))

        puntos = VGroup(*[Dot([-3.3 + 1.5 * (k - 1), 2.9, 0], radius=0.13, color=AMBAR) for k in range(3)])
        nombres = VGroup(*[MathTex(f"x_{k + 1}", color=TXT).scale(0.7).next_to(puntos[k], UP, buff=0.12) for k in range(3)])
        arcos = VGroup(
            ArcBetweenPoints(puntos[0].get_center(), puntos[1].get_center(), angle=-0.9, color=CIAN, stroke_width=3),
            ArcBetweenPoints(puntos[1].get_center(), puntos[2].get_center(), angle=-0.9, color=CIAN, stroke_width=3),
            ArcBetweenPoints(puntos[0].get_center(), puntos[2].get_center(), angle=0.9, color=MAGENTA, stroke_width=3))

        with self.narrar("b1"):
            # «Con tres muestras»
            self.en("tres")
            self.play(FadeIn(puntos), FadeIn(nombres), run_time=0.5)

            # «Hay que sumar las covarianzas»
            self.en("sumar")
            sm = MathTex(r"\sum C=?", color=AMBAR).scale(1.2).move_to([4.2, 3.0, 0])
            self.pop(sm)

            # «todas las parejas»
            self.en("parejas")
            self.play(Create(arcos), run_time=self.dur(1.0))

            # «una tabla de tres por tres»
            self.en("tabla")
            self.play(Create(tabla), run_time=self.dur(1.0))

            # «En la diagonal»
            self.en("diag")
            vd = VGroup(*[valor(ij, "4", AMBAR) for ij in diag])
            self.play(FadeIn(vd), *[casillas[ij].animate.set_stroke(AMBAR, 4) for ij in diag], run_time=0.5)

            # «tres por cuatro»
            self.en("d12")
            r1 = MathTex(r"3\times4=12", color=AMBAR).scale(1.1).move_to([4.2, 1.6, 0])
            self.play(FadeIn(r1), run_time=0.4)

            # «Junto a la diagonal»
            self.en("junto")
            self.play(*[casillas[ij].animate.set_stroke(CIAN, 4) for ij in vec], run_time=0.4)

            # «a un paso»
            self.en("vecinas")
            vv = VGroup(*[valor(ij, "2,4", CIAN) for ij in vec])
            self.play(FadeIn(vv), run_time=0.5)

            # «cuatro por dos coma cuatro»
            self.en("v96")
            r2 = MathTex(r"4\times2{,}4=9{,}6", color=CIAN).scale(1.1).move_to([4.2, 0.4, 0])
            self.play(FadeIn(r2), run_time=0.4)

            # «En las esquinas»
            self.en("esquinas")
            self.play(*[casillas[ij].animate.set_stroke(MAGENTA, 4) for ij in esq], run_time=0.4)

            # «a dos pasos»
            self.en("esq")
            ve = VGroup(*[valor(ij, "1,44", MAGENTA) for ij in esq])
            self.play(FadeIn(ve), run_time=0.5)

            # «dos por uno coma cuatro cuatro»
            self.en("v288")
            r3 = MathTex(r"2\times1{,}44=2{,}88", color=MAGENTA).scale(1.1).move_to([4.2, -0.8, 0])
            self.play(FadeIn(r3), run_time=0.4)

            # «veinticuatro coma cuatro ocho»
            self.en("total")
            r4 = MathTex(r"12+9{,}6+2{,}88=24{,}48", color=TXT).scale(1.0).move_to([4.2, -2.0, 0])
            self.play(FadeIn(r4), run_time=0.6)

            # «dos coma siete dos»
            self.en("res")
            r5 = MathTex(r"\frac{24{,}48}{9}=2{,}72", color=AMBAR).scale(1.3).move_to([4.2, -3.3, 0])
            self.pop(r5)
        self.wait(1.0)
        self.limpiar()
