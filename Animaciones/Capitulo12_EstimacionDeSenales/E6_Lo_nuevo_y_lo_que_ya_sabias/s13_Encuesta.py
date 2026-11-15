"""Escena 13 — Encuesta: ¿qué salto baja más el error, poder usar la muestra de ahora o el futuro?"""
from comun.escena import *


class Encuesta(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        t_enc = Text("Encuesta", color=INK, weight=BOLD).scale(0.7).move_to([-5.4, 3.3, 0])
        caja_a = RoundedRectangle(corner_radius=0.2, width=6.0, height=3.4, color=INK, stroke_width=3).move_to([-3.6, 0.0, 0])
        caja_b = RoundedRectangle(corner_radius=0.2, width=6.0, height=3.4, color=INK, stroke_width=3).move_to([3.6, 0.0, 0])
        let_a = Text("A", color=TXT, weight=BOLD).scale(0.8).move_to([-6.3, 1.2, 0])
        let_b = Text("B", color=TXT, weight=BOLD).scale(0.8).move_to([0.9, 1.2, 0])
        barra = Rectangle(width=0.5, height=1.0, stroke_width=0).set_fill(ERROR, 0.85).move_to([6.2, 3.0, 0])
        barra_baja = Rectangle(width=0.5, height=0.4, stroke_width=0).set_fill(ERROR, 0.85).move_to([6.2, 2.7, 0])
        pregunta = Text("¿qué salto es mayor?", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.3, 0])

        fa = FilaMuestras([r"\cdots", r"x[n{-}1]", r"x[n]"], centro=(-3.6, 0.2), lado=1.5, color=MEDIDA, escala=0.6)
        fb = FilaMuestras([r"x[n]", r"x[n{+}1]", r"x[n{+}2]", r"\cdots"], centro=(3.6, 0.2), lado=1.35, color=MEDIDA,
                          escala=0.55)
        t_a = Text("predecir → filtrar", color=ESTIMACION).scale(0.6).move_to([-3.6, -1.0, 0])
        t_b = Text("filtrar → suavizar", color=ESTIMACION).scale(0.6).move_to([3.6, -1.0, 0])
        cuenta = [Text(s, color=AMBAR, weight=BOLD).scale(1.2).move_to([0, -3.0, 0]) for s in ("3", "2", "1")]

        with self.narrar("b1"):
            # «Una encuesta»
            self.en("enc")
            self.corte()
            self.play(FadeIn(t_enc), Create(caja_a), Create(caja_b), run_time=self.dur(0.6))

            # «bajar el error»
            self.en("bajar")
            self.add(barra)
            self.play(Transform(barra, barra_baja), run_time=self.dur(0.8))

            # «¿qué salto es mayor?»
            self.en("salto")
            self.pop(pregunta)

            # «La opción A»
            self.en("a")
            self.pop(let_a)

            # «la muestra de ahora»
            self.en("ahora")
            self.play(FadeIn(fa), run_time=self.dur(0.5))
            self.resaltar(fa.cas[2], color=AMBAR)

            # «pasar de predecir a filtrar»
            self.en("paf")
            self.play(FadeIn(t_a), run_time=self.dur(0.5))

            # «La opción B»
            self.en("b")
            self.pop(let_b)

            # «además el futuro»
            self.en("futuro")
            self.play(FadeIn(fb), run_time=self.dur(0.5))
            self.resaltar(fb.cas[1], color=AMBAR)

            # «pasar de filtrar a suavizar»
            self.en("afs")
            self.play(FadeIn(t_b), run_time=self.dur(0.5))

            # «Piénsalo»
            self.en("piensa")
            self.play(FadeIn(cuenta[0]), run_time=0.3)
            self.wait(0.6)
            self.play(Transform(cuenta[0], cuenta[1]), run_time=0.3)
            self.wait(0.6)
            self.play(Transform(cuenta[0], cuenta[2]), run_time=0.3)

        self.wait(1.0)
        self.limpiar()
