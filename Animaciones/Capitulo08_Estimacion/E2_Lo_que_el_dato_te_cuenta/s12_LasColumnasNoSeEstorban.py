"""Escena 12 — Las columnas no se estorban: cada una ya está en su mínimo, así que la media condicional es la mejor regla."""
from comun.escena import *


class LasColumnasNoSeEstorban(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        cy = 1.0
        curva0, min0, p0 = parabola8((-3.5, cy), ancho=5.0, alto=2.8)
        curva1, min1, p1 = parabola8((3.5, cy), ancho=5.0, alto=2.8)
        min0.move_to(p0(0.0))
        h0 = MathTex(r"R=0", color=MEDIDA).scale(1.2).move_to([-3.5, 3.3, 0])
        h1 = MathTex(r"R=1", color=MEDIDA).scale(1.2).move_to([3.5, 3.3, 0])
        otra = caja("Otra regla: 0,6 y 0,1", AMBAR, ancho=5.6, alto=0.9, scale=0.65).move_to([-1.2, 2.2, 0])
        menor = MathTex(r"<\ 0{,}084\ ?", color=ROJO).scale(1.3).next_to(otra, RIGHT, buff=0.4)
        pared = DashedLine([0, 3.6, 0], [0, -1.0, 0], color=INK, stroke_width=4)
        l0 = MathTex(r"0{,}045", color=VERDE).scale(1.0).move_to([-3.5, -0.8, 0])
        l1 = MathTex(r"0{,}79", color=VERDE).scale(1.0).move_to([3.5, -0.8, 0])
        f1 = MathTex(r"\hat{Y}=E[Y\mid X]", color=ESTIMACION).scale(1.3).move_to([-3.5, -2.0, 0])
        f2 = MathTex(r"\text{Error}=E\big[\mathrm{Var}(Y\mid X)\big]", color=ERROR).scale(1.1).move_to([3.5, -2.0, 0])
        mm = caja("Estimador de mínimo error cuadrático medio", VERDE, ancho=10.0, alto=0.95, scale=0.7).move_to([-0.8, -3.3, 0])
        sig = Text("MMSE", color=INK).scale(0.6).next_to(mm, RIGHT, buff=0.3)
        with self.narrar("b1"):
            # «otra regla»
            self.en("otra")
            self.pop(otra)

            # «un error total más pequeño»
            self.en("menor")
            self.pop(menor)

            # «No.»
            self.en("no")
            x = cruz(ROJO, 1.1).move_to(menor)
            self.play(Create(x), run_time=self.dur(0.4))

            # «un promedio de los errores de cada columna»
            self.en("promedio")
            self.play(FadeOut(otra), FadeOut(menor), FadeOut(x), run_time=0.2)
            self.play(FadeIn(h0), FadeIn(h1), Create(curva0), Create(curva1), run_time=self.dur(1.0))

            # «el más pequeño posible»
            self.en("minimo")
            self.play(FadeIn(min0, scale=0.3), FadeIn(min1, scale=0.3), FadeIn(l0), FadeIn(l1), run_time=self.dur(0.6))

            # «no se estorban»
            self.en("pared")
            self.play(Create(pared), run_time=self.dur(0.5))

            # «mejorar una no empeora la otra»
            self.en("mejorar")
            self.play(min1.animate.move_to(p1(0.45)), run_time=self.dur(0.6))
            self.play(min1.animate.move_to(p1(0.0)), run_time=self.dur(0.5))

            # «la media condicional es la mejor regla»
            self.en("mejor")
            self.pop(f1)

            # «la media de las varianzas condicionales»
            self.en("err")
            self.pop(f2)

            # «Se llama estimador»
            self.en("llama")
            self.resaltar(f1, color=AMBAR)

            # «mínimo error cuadrático medio»
            self.en("mmse")
            self.pop(mm)
            self.play(FadeIn(sig), run_time=self.dur(0.3))
        self.wait(1.0)
        self.limpiar()
