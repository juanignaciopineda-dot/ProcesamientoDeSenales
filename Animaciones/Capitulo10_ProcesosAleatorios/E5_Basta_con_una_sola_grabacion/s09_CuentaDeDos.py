"""Escena 09 — La cuenta con dos muestras: sensor, independientes y pila."""
from comun.escena import *


class CuentaDeDos(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        xs = (-4.7, 0.0, 4.7)

        def cabecera(txt, color, x):
            return caja(txt, color, ancho=3.4, alto=0.8).move_to([x, 3.0, 0])

        def cuenta(tex, x, y, color=TXT, escala=1.0):
            return MathTex(tex, color=color).scale(escala).move_to([x, y, 0])

        with self.narrar("b1"):
            # «Con el sensor»
            self.en("sensor")
            h1 = cabecera("sensor", SENAL, xs[0])
            c1 = cuenta(r"C[1]=2{,}4", xs[0], 1.9, CIAN, 1.1)
            self.play(FadeIn(h1), run_time=0.3)
            self.play(FadeIn(c1), run_time=0.4)

            # «cuatro más cuatro más dos por dos coma cuatro»
            self.en("formula")
            f1 = cuenta(r"\frac{4+4+2\cdot 2{,}4}{4}", xs[0], 0.4, TXT, 1.1)
            self.play(Write(f1), run_time=self.dur(1.6))

            # «doce coma ocho»
            self.en("v128")
            r1 = cuenta(r"=\frac{12{,}8}{4}", xs[0], -1.0, TXT, 1.1)
            self.play(FadeIn(r1), run_time=0.4)

            # «tres coma dos»
            self.en("v32")
            g1 = cuenta(r"=3{,}2", xs[0], -2.4, AMBAR, 1.6)
            self.pop(g1)

            # «independientes»
            self.en("indep")
            h2 = cabecera("independientes", CIAN, xs[1])
            c2 = cuenta(r"C[1]=0", xs[1], 1.9, CIAN, 1.1)
            self.play(FadeIn(h2), FadeIn(c2), run_time=0.5)

            # «quedaría dos»
            self.en("v2")
            f2 = cuenta(r"\frac{4+4+0}{4}", xs[1], 0.4, TXT, 1.1)
            g2 = cuenta(r"=2", xs[1], -1.6, AMBAR, 1.6)
            self.play(Write(f2), run_time=0.8)
            self.pop(g2)

            # «con la pila»
            self.en("pila")
            h3 = cabecera("pila", AMBAR, xs[2])
            self.play(FadeIn(h3), run_time=0.3)

            # «la covarianza es cuatro»
            self.en("c4")
            c3 = cuenta(r"C[1]=4", xs[2], 1.9, CIAN, 1.1)
            self.play(FadeIn(c3), run_time=0.4)

            # «dieciséis»
            self.en("v16")
            f3 = cuenta(r"\frac{4+4+8}{4}", xs[2], 0.4, TXT, 1.1)
            r3 = cuenta(r"=\frac{16}{4}", xs[2], -1.0, TXT, 1.1)
            self.play(Write(f3), run_time=0.8)
            self.play(FadeIn(r3), run_time=0.4)

            # «entre cuatro, cuatro»
            self.en("v4")
            g3 = cuenta(r"=4", xs[2], -2.4, ROJO, 1.6)
            self.pop(g3)

            # «no sirve de nada»
            self.en("nada")
            eq = MathTex(r"4=4", color=ROJO).scale(1.2).move_to([0, -3.4, 0])
            x = cruz(ROJO, 0.4).next_to(eq, RIGHT, buff=0.3)
            self.sfx("error")
            self.play(FadeIn(eq), FadeIn(x, scale=0.5), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
