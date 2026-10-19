"""Escena 05 — La promesa del capítulo 7: el 41,2 es el primer trozo de la ley de la varianza total."""
from comun.escena import *


class LaPromesaDelCapitulo7(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        grande = MathTex(r"41{,}2", color=TXT).scale(2.4).move_to([0, 3.0, 0])
        interrog = Text("?", color=AMBAR, weight=BOLD).scale(1.8).next_to(grande, RIGHT, buff=0.5)
        bar = BarrasVar7(origen=(-4.9, 0.4), esc=0.12, alto=1.3)
        t_dentro = MathTex(r"41{,}2", color=TXT).scale(1.0).move_to(bar.dentro)
        t_entre = MathTex(r"40{,}56", color=TXT).scale(1.0).move_to(bar.entre)
        total = BraceBetweenPoints(bar.dentro.get_corner(DL), bar.entre.get_corner(DR), DOWN, color=INK)
        t_total = MathTex(r"=\ 81{,}76", color=INK).scale(0.8).next_to(total, DOWN, buff=0.1)
        with self.narrar("b1"):
            # «no es un número nuevo»
            self.en("nuevo")
            self.pop(grande)
            self.pop(interrog)

            # «la ley de la varianza total»
            self.en("ley")
            self.play(FadeIn(bar.dentro, shift=RIGHT * 0.3), FadeIn(bar.entre, shift=LEFT * 0.3), run_time=self.dur(0.7))
            self.play(FadeIn(t_dentro), FadeIn(t_entre), GrowFromCenter(total), FadeIn(t_total), run_time=self.dur(0.6))

            # «lo que el grupo no explica»
            self.en("no_explica")
            no_exp = Text("Lo que el grupo no explica", color=ROJO).scale(0.55).next_to(bar.dentro, UP, buff=0.3)
            self.play(FadeIn(no_exp), run_time=self.dur(0.4))

            # «prometimos»
            self.en("prometimos")
            self.play(FadeOut(interrog), run_time=0.2)
            meta = Text("Error del mejor estimador", color=AMBAR, weight=BOLD).scale(0.65).move_to([-2.4, -2.4, 0])

            # «al final de aquel capítulo»
            self.en("final")
            cap = etiqueta("Capítulo 7", INK, 0.6).move_to([-5.8, 3.6, 0])
            self.play(FadeIn(cap), run_time=self.dur(0.3))

            # «el error del mejor estimador»
            self.en("mejor_est")
            self.play(FadeIn(meta, shift=UP * 0.2), run_time=self.dur(0.4))

            # «exactamente ese trozo»
            self.en("exacto")
            marco = Rectangle(width=bar.dentro.width + 0.2, height=bar.dentro.height + 0.2, color=AMBAR, stroke_width=6)
            marco.move_to(bar.dentro)
            self.play(Create(marco), run_time=self.dur(0.5))

            # «aquí está»
            self.en("aqui")
            tick = tilde(VERDE, 0.8).move_to([-1.7, 3.0, 0]).shift(RIGHT * 4.4)
            ok = Text("Promesa cumplida", color=VERDE, weight=BOLD).scale(0.65).next_to(tick, RIGHT, buff=0.3)
            grupo = VGroup(tick, ok).move_to([0, 3.0, 0])
            self.sfx("exito")
            self.play(FadeOut(grande), run_time=0.2)
            self.play(Create(tick), FadeIn(ok), run_time=self.dur(0.6))

            # «cuarenta coma cinco seis»
            self.en("n4056")
            self.resaltar(bar.entre, color=VERDE)

            # «nos ha ahorrado»
            self.en("ahorrado")
            ah = Text("Lo que ahorra el grupo", color=VERDE).scale(0.55).next_to(bar.entre, UP, buff=0.3)
            self.play(FadeIn(ah), run_time=self.dur(0.4))
        self.wait(1.0)
        self.limpiar()
