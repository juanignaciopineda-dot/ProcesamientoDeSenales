"""Escena 18 — Mil muestras del sensor: ¿a cuántas independientes equivalen?"""
from comun.escena import *


class CuantasValen(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        with self.narrar("b1"):
            # «mil muestras del sensor»
            self.en("mil")
            q = Text("1.000 muestras del sensor ≈ ¿? independientes", color=TXT, weight=BOLD).scale(0.75).move_to([0, 3.2, 0])
            q[0:5].set_color(AMBAR)
            self.play(FadeIn(q, shift=DOWN * 0.2), run_time=0.6)

            # «Si fueran independientes»
            self.en("indep")
            fila = fila_puntos(28, 10.0, (0, 1.6), SENAL, 0.1)
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in fila], lag_ratio=0.04), run_time=self.dur(1.2))

            # «cuatro entre mil»
            self.en("cuatro")
            v = MathTex(r"\mathrm{Var}=\frac{4}{1000}", color=AMBAR).scale(1.2).move_to([0, 0.3, 0])
            self.play(Write(v), run_time=self.dur(1.0))

            # «tienen memoria»
            self.en("memoria")
            hl = hilos_entre(fila, AMBAR, 3)
            self.play(Create(hl), run_time=self.dur(1.0))

            # «¿A cuántas muestras independientes equivalen?»
            self.en("equivalen")
            qq = self.palabra("¿?", ROJO, 1.6).move_to([0, -0.9, 0])
            self.pop(qq)

            # «¿Mil?»
            self.en("o1")
            o1 = caja("1.000", AZUL, ancho=2.6, alto=1.0, scale=0.8).move_to([-4.2, -2.7, 0])
            self.play(FadeIn(o1, shift=UP * 0.2), run_time=0.4)

            # «¿Quinientas?»
            self.en("o2")
            o2 = caja("500", AZUL, ancho=2.6, alto=1.0, scale=0.8).move_to([0, -2.7, 0])
            self.play(FadeIn(o2, shift=UP * 0.2), run_time=0.4)

            # «¿Doscientas cincuenta?»
            self.en("o3")
            o3 = caja("250", AZUL, ancho=2.6, alto=1.0, scale=0.8).move_to([4.2, -2.7, 0])
            self.play(FadeIn(o3, shift=UP * 0.2), run_time=0.4)

            # «Piénsalo un momento»
            self.en("pausa")
            ra = reloj_arena().scale(0.8).move_to([0, -0.9, 0])
            self.play(FadeOut(qq), FadeIn(ra), run_time=0.3)
            self.play(Rotate(ra, angle=PI), run_time=self.dur(1.6))
        self.wait(0.6)
        self.limpiar()
