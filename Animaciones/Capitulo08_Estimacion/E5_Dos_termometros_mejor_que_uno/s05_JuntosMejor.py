"""Escena 05 — Juntos, mejor: apuesta 22,33 y error 2/3, contra 0,8 (solo A) y 2 (solo B)."""
from comun.escena import *
from comun.figuras_c8e5 import *


class JuntosMejor(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        X0 = -6.5
        ap = formula(r"\hat{y}", "=", "20", "+", r"\frac{2}{3}\cdot 3", "+", r"\frac{1}{6}\cdot 2",
                     r"\approx 22{,}33", escala=1.05, colores={0: ESTIMACION, 7: ESTIMACION})
        ap.move_to([X0, 2.7, 0], aligned_edge=LEFT)
        n3 = MathTex("23-20", color=INK).scale(0.7).next_to(ap[4], DOWN, buff=0.2).shift(RIGHT * 0.25)
        n2 = MathTex("22-20", color=INK).scale(0.7).next_to(ap[6], DOWN, buff=0.2).shift(RIGHT * 0.25)
        er = formula(r"\text{Error}", "=", "4", r"-h_A\cdot 4-h_B\cdot 4", escala=1.05, colores={0: ERROR})
        er.move_to([X0, 0.5, 0], aligned_edge=LEFT)
        er[3].set_color(INK)
        en = formula("=", "4", r"-\frac{2}{3}\cdot 4", r"-\frac{1}{6}\cdot 4", "=", r"\frac{2}{3}", escala=1.05)
        en.next_to(er[1], DOWN, buff=0.9, aligned_edge=LEFT)
        en[5].set_color(ERROR)
        e067 = MathTex(r"\approx 0{,}67", color=ERROR).scale(1.05).next_to(en, DOWN, buff=0.45).align_to(en[4], LEFT)
        d = barras8([0.8, 2.0, 0.67], ["Solo A", "Solo B", "A y B"], centro=(4.6, -0.5), ancho=3.8, alto=3.4,
                    v_max=2.2, textos=["0,8", "2", "0,67"])
        ok = tilde(VERDE, 0.5).next_to(d["vals"][2], UP, buff=0.15)

        with self.narrar("b1"):
            # «La apuesta queda en veinte»
            self.en("ap")
            self.play(*[FadeIn(ap[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.5))

            # «más dos tercios por tres»
            self.en("t1")
            self.play(FadeIn(ap[3]), FadeIn(ap[4], shift=UP * 0.1), FadeIn(n3), run_time=self.dur(0.5))

            # «más un sexto por dos»
            self.en("t2")
            self.play(FadeIn(ap[5]), FadeIn(ap[6], shift=UP * 0.1), FadeIn(n2), run_time=self.dur(0.5))

            # «Veintidós coma tres tres»
            self.en("res")
            self.pop(ap[7])

            # «¿Y el error?»
            self.en("err")
            self.play(FadeIn(er[0]), FadeIn(er[1]), run_time=self.dur(0.4))

            # «Es la varianza, cuatro»
            self.en("e4")
            self.play(FadeIn(er[2], shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «menos cada peso por su covarianza»
            self.en("ec")
            self.play(FadeIn(er[3], shift=LEFT * 0.15), run_time=self.dur(0.6))

            # «Cuatro, menos dos tercios por cuatro»
            self.en("en1")
            self.play(*[FadeIn(en[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.6))

            # «menos un sexto por cuatro»
            self.en("en2")
            self.play(FadeIn(en[3], shift=UP * 0.1), run_time=self.dur(0.4))

            # «da dos tercios»
            self.en("e23")
            self.play(FadeIn(en[4]), FadeIn(en[5], shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «cero coma seis siete»
            self.en("e067")
            self.play(FadeIn(e067, shift=UP * 0.1), run_time=self.dur(0.4))

            # «Con A solo era cero coma ocho»
            self.en("ba")
            self.play(Create(d["base"]), GrowFromEdge(d["barras"][0], DOWN), FadeIn(d["rots"][0]), run_time=self.dur(0.6))
            self.play(FadeIn(d["vals"][0]), run_time=0.25)

            # «con B solo, dos»
            self.en("bb")
            self.play(GrowFromEdge(d["barras"][1], DOWN), FadeIn(d["rots"][1]), run_time=self.dur(0.6))
            self.play(FadeIn(d["vals"][1]), run_time=0.25)

            # «Juntos»
            self.en("bab")
            self.play(GrowFromEdge(d["barras"][2], DOWN), FadeIn(d["rots"][2]), FadeIn(d["vals"][2]),
                      run_time=self.dur(0.5))

            # «mejor que el mejor de los dos»
            self.en("mejor")
            self.play(d["barras"][2].animate.set_fill(VERDE, 0.9), FadeIn(ok, scale=0.5), run_time=self.dur(0.6))
            self.sfx("exito")
        self.wait(1.0)
        self.limpiar()
