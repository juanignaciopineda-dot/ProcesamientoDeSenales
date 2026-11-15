"""Escena 03 — Las dos partes de cada muestra: lo que ya se conoce y la moneda nueva."""
from comun.escena import *


class DosPartes(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        previa = formula("H", "=", r"\tfrac{1}{F}", r"\left[\,\cdot\,\right]_{+}", escala=0.9,
                         colores={0: ESTIMACION}).move_to([0, 3.0, 0])
        previa.set_opacity(0.35)
        p_innov = self.palabra("innovación", AMBAR, 1.0).move_to([0, 1.8, 0])

        bl = BloqueLTI(r"\text{eco}", centro=(0.0, 1.9), ancho=2.2, alto=1.2, largo=1.9, color=AZUL, escala=0.8)
        mon = moneda("", AMBAR).scale(0.5).move_to(bl.p_ent() + LEFT * 0.5)
        l_w = MathTex(r"w[n]", color=SENAL).scale(0.8).next_to(mon, DOWN, buff=0.15)
        l_x = MathTex(r"x[n]", color=MEDIDA).scale(0.8).next_to(bl.p_sal(), RIGHT, buff=0.2)
        v_t = MathTex(r"v[n]", color=RUIDO).scale(0.8).move_to([1.9, 3.3, 0])
        v_a = Arrow([1.9, 2.95, 0], [1.9, 2.0, 0], color=RUIDO, buff=0, stroke_width=4,
                    max_tip_length_to_length_ratio=0.25)
        v_x = Line(v_t.get_corner(DL) + DL * 0.05, [2.3, 2.0, 0], color=ROJO, stroke_width=7)

        f1 = formula("x[n]", "=", r"0{,}6\,", "x[n-1]", "+", "w[n]", escala=1.1,
                     colores={0: MEDIDA, 3: MEDIDA, 5: SENAL}).move_to([0, -0.1, 0])
        s2 = MathTex(r"\sigma^2 = 2{,}56", color=SENAL).scale(0.7).next_to(f1[5], DOWN, buff=0.3)
        oculta(f1)
        f2 = formula("x[n+1]", "=", r"0{,}6\,x[n]", "+", "w[n+1]", escala=1.1,
                     colores={0: MEDIDA}).move_to([0, -1.9, 0])
        oculta(f2)
        llave = Brace(VGroup(f2[2], f2[3], f2[4]), DOWN, color=INK, buff=0.15)

        with self.narrar("b1"):
            # «otra forma»
            self.en("otra")
            self.play(FadeIn(previa), run_time=self.dur(0.5))

            # «con la innovación»
            self.en("innovacion")
            self.pop(p_innov)

            # «Volvamos al eco»
            self.en("eco")
            self.corte(f1, f2)
            self.play(FadeIn(bl), FadeIn(mon), FadeIn(l_w), FadeIn(l_x), run_time=self.dur(0.8))

            # «sin ruido»
            self.en("sinruido")
            self.play(FadeIn(v_t), GrowArrow(v_a), run_time=self.dur(0.5))
            self.play(Create(v_x), run_time=self.dur(0.4))

            # «cero coma seis por la anterior»
            self.en("por06")
            self.play(*revelar(*f1[0:4]), run_time=self.dur(0.9))

            # «más una moneda nueva»
            self.en("moneda")
            self.play(*revelar(f1[4], f1[5]), FadeIn(s2), run_time=self.dur(0.7))

            # «la muestra siguiente»
            self.en("siguiente")
            self.play(*revelar(f2[0], f2[1]), run_time=self.dur(0.6))

            # «dos partes»
            self.en("dospartes")
            self.play(*revelar(f2[2], f2[3], f2[4]), run_time=self.dur(0.5))
            self.play(GrowFromCenter(llave), run_time=self.dur(0.5))

            # «que ya conocemos»
            self.en("conocemos")
            self.play(f2[2].animate.set_color(VERDE), run_time=self.dur(0.5))
            tk = tilde(VERDE, 0.5).next_to(f2[2], UP, buff=0.15)
            self.play(FadeIn(tk), run_time=self.dur(0.3))

            # «que todavía no ha llegado»
            self.en("nollego")
            self.play(f2[4].animate.set_color(ERROR), run_time=self.dur(0.4))
            q = self.palabra("?", ERROR, 0.9).next_to(f2[4], UP, buff=0.15)
            self.pop(q)

        self.wait(1.0)
        self.limpiar()
