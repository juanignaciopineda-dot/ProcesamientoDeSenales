"""Escena 01 — Gancho: adivinar una altura; con un dato el error se reduce a la mitad y lo que queda no tiene patrón."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        pu = puerta8(4.6).move_to([-4.6, -0.4, 0])
        per = persona(SENAL).scale(2.2).move_to(pu.marco.get_center() + DOWN * 1.2)
        with self.narrar("b1"):
            # «Alguien entra por la puerta»
            self.en("puerta")
            self.play(FadeIn(pu), run_time=self.dur(0.4))
            self.play(FadeIn(per, shift=RIGHT * 0.3), run_time=self.dur(0.4))
            self.play(per.animate.move_to([-1.6, -1.6, 0]), run_time=self.dur(1.0))

            # «adivinar su altura»
            self.en("altura")
            pies, cabeza = per.get_bottom() + DOWN * 0.05 + RIGHT * 0.9, per.get_top() + UP * 0.05 + RIGHT * 0.9
            regla = VGroup(Line(pies, cabeza, color=INK, stroke_width=3),
                           Line(pies + LEFT * 0.12, pies + RIGHT * 0.12, color=INK, stroke_width=3),
                           Line(cabeza + LEFT * 0.12, cabeza + RIGHT * 0.12, color=INK, stroke_width=3))
            que = Text("?", color=AMBAR, weight=BOLD).scale(1.8).next_to(regla, RIGHT, buff=0.3)
            self.play(Create(regla), run_time=self.dur(0.5))
            self.pop(que)

            # «una sola cosa»
            self.en("dato")
            tarjeta = caja("Es mujer", MAGENTA, ancho=3.2, alto=1.0, scale=0.8).move_to([-1.6, 2.3, 0])
            self.pop(tarjeta)

            # «se reduce a la mitad»
            self.en("mitad")
            esc = 0.065
            b1 = Rectangle(width=81.76 * esc, height=1.0, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
            b1.move_to([1.2 + 81.76 * esc / 2, 1.2, 0])
            b2 = Rectangle(width=41.2 * esc, height=1.0, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
            b2.move_to([1.2 + 41.2 * esc / 2, 1.2, 0])
            t1 = MathTex(r"81{,}76", color=TXT).scale(1.2).next_to(b1, DOWN, buff=0.3).align_to(b1, LEFT)
            t2 = MathTex(r"41{,}2", color=TXT).scale(1.2).next_to(b2, DOWN, buff=0.3).align_to(b2, LEFT)
            self.play(FadeIn(b1, shift=RIGHT * 0.3), FadeIn(t1), run_time=self.dur(0.5))
            self.play(Transform(b1, b2), Transform(t1, t2), run_time=self.dur(0.9))

            # «ningún patrón»
            self.en("patron")
            self.corte()
            errs = PuntosErr8(centro=(0, 0), ancho=10.5, alto=4.0, n=42, semilla=5)
            et = Text("Error", color=ERROR, weight=BOLD).scale(0.9).move_to([-6.0, 1.6, 0])
            self.play(Create(errs.cero), FadeIn(et), run_time=self.dur(0.4))
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in errs.pts], lag_ratio=0.04), run_time=self.dur(1.3))
        self.wait(1.0)
        self.limpiar()
