"""Escena 07 — La media no lo cuenta todo: un dado y una constante con la misma media."""
from comun.escena import *


class LaMediaNoBasta(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        mu = MathTex(r"\mu", "=", "3{,}5", color=TXT).scale(1.6).move_to([-1.5, 3.0, 0])
        mu[0].set_color(AMBAR)
        todo = Text("¿Todo?", color=INK).scale(0.7).move_to([2.0, 3.0, 0])
        RL = Regla7(centro=(-3.7, -1.9), ancho=5.6, v0=0.4, v1=6.6)
        RR = Regla7(centro=(3.7, -1.9), ancho=5.6, v0=0.4, v1=6.6)
        barras_dado = VGroup(*[Rectangle(width=0.55, height=1.0, color=SENAL, stroke_width=3)
                               .set_fill(SENAL, 0.45).move_to(RL.p(v) + UP * 0.5) for v in range(1, 7)])
        barra_cte = Rectangle(width=0.55, height=2.4, color=SENAL, stroke_width=3).set_fill(SENAL, 0.45)
        barra_cte.move_to(RR.p(3.5) + UP * 1.2)
        linea_l = DashedLine(RL.p(3.5) + DOWN * 0.2, RL.p(3.5) + UP * 2.8, color=AMBAR, stroke_width=3)
        linea_r = DashedLine(RR.p(3.5) + DOWN * 0.2, RR.p(3.5) + UP * 2.8, color=AMBAR, stroke_width=3)
        igual = MathTex("=", color=AMBAR).scale(1.6).move_to([0, 0.3, 0])
        distinto = MathTex(r"\neq", color=ROJO).scale(1.6).move_to([0, 0.3, 0])
        punto_l = Dot(RL.p(3) + UP * 1.5, radius=0.13, color=ESTIMACION)
        punto_r = Dot(RR.p(3.5) + UP * 2.9, radius=0.13, color=ESTIMACION)
        cuadro = Square(side_length=0.9, color=AMBAR, stroke_width=3).move_to([2.0, 3.0, 0])
        interr = Text("?", color=AMBAR, weight=BOLD).scale(0.8).move_to(cuadro)
        with self.narrar("b1"):
            # «la media no lo cuenta todo»
            self.en("no_todo")
            self.play(FadeIn(mu, shift=DOWN * 0.15), run_time=self.dur(0.6))
            self.play(FadeIn(todo), run_time=0.3)
            self.play(Create(tachar(todo)), run_time=0.4)

            # «Un dado»
            self.en("dado")
            self.play(FadeIn(RL), LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in barras_dado], lag_ratio=0.1),
                      run_time=self.dur(0.9))
            # «una variable que siempre vale»
            self.en("cte")
            self.play(FadeIn(RR), run_time=self.dur(0.5))
            # «tres coma cinco»
            self.en("siempre")
            self.play(FadeIn(barra_cte, shift=UP * 0.3), run_time=self.dur(0.7))

            # «la misma media»
            self.en("misma")
            self.play(Create(linea_l), Create(linea_r), FadeIn(igual), run_time=self.dur(0.8))
            # «no se parecen en nada»
            self.en("distintas")
            self.play(Transform(igual, distinto), run_time=self.dur(0.5))

            # «salta de uno a seis»
            self.en("salta")
            self.play(FadeIn(punto_l), FadeIn(punto_r), run_time=0.2)
            for v in (1, 6, 2, 5, 3):
                self.play(punto_l.animate.move_to(RL.p(v) + UP * 1.5), run_time=0.22, rate_func=linear)
            # «la otra no se mueve»
            self.en("quieta")
            self.play(Indicate(punto_r, color=AMBAR, scale_factor=1.5), run_time=self.dur(0.7))

            # «un segundo número»
            self.en("segundo")
            self.play(FadeOut(todo), FadeIn(cuadro), FadeIn(interr), run_time=self.dur(0.6))
            # «se aleja la variable de su media»
            self.en("aleja")
            fl = VGroup(flecha(RL.p(3.5) + UP * 2.2, RL.p(1.0) + UP * 2.2, AMBAR, 4),
                        flecha(RL.p(3.5) + UP * 2.2, RL.p(6.0) + UP * 2.2, AMBAR, 4))
            self.play(LaggedStart(*[GrowArrow(a) for a in fl], lag_ratio=0.2), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
