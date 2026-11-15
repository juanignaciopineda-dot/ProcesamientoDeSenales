"""Escena 19 — La cuenta: al menos una falsa alarma entre N posiciones es casi N por p."""
from comun.escena import *


class LaCuentaDeLasPosiciones(EscenaCurso):
    ESCENA = "19"

    def construct(self):
        tira = celdas13(20, ancho=8.0, centro=(0.0, 2.4), alto=0.55)
        p = MathTex("p", color=ROJO).scale(1.0).move_to(tira[5].get_center() + UP * 0.7)
        falsa = formula("p", "=", r"P(\text{falsa alarma})", escala=0.9, colores={0: ROJO}).move_to([0, 1.1, 0])
        brace = BraceBetweenPoints(tira[0].get_corner(DL) + DOWN * 0.0, tira[19].get_corner(DR), direction=DOWN, color=AMBAR)
        nl = MathTex("N", color=AMBAR).scale(0.9)
        brace.next_to(tira, DOWN, buff=0.1)
        nl.next_to(brace, DOWN, buff=0.05)
        # la fórmula se arma en la fila central
        # cuando entra la brace, la fórmula de "falsa" baja un poco
        fo = formula(r"P(\text{al menos una})", r"\approx", "N", r"\cdot", "p", escala=1.0,
                     colores={2: AMBAR, 4: ROJO}).move_to([0, -0.1, 0])
        tot = formula(r"P_{FA}", "=", r"10^{-3}", escala=1.0, colores={0: ROJO, 2: ROJO}).move_to([-3.7, -1.5, 0])
        nmil = formula("N", "=", r"1\,000", escala=1.0, colores={0: AMBAR, 2: AMBAR}).move_to([3.7, -1.5, 0])
        cada = formula("p", "=", r"\frac{10^{-3}}{1\,000}", escala=1.1, colores={0: ROJO}).move_to([-1.2, -2.8, 0])
        mill = formula("=", r"10^{-6}", escala=1.1, colores={1: ROJO}).move_to([2.2, -2.8, 0])
        comp = formula(r"1\,000", r"\cdot", r"10^{-6}", "=", r"10^{-3}", escala=0.8, colores={4: VERDE}).move_to([5.3, -2.8, 0])
        ok = tilde(VERDE, 0.4).next_to(comp, DOWN, buff=0.1)
        with self.narrar("b1"):
            # «Hagamos la cuenta»
            self.en("cuenta")
            self.play(FadeIn(tira), run_time=self.dur(0.6))
            # «cada posición tiene una probabilidad pequeña, pe»
            self.en("pe")
            self.play(tira[5].animate.set_fill(ROJO, 0.5).set_stroke(ROJO), run_time=0.3)
            self.pop(p)
            # «de falsa alarma»
            self.en("falsa")
            self.play(FadeIn(falsa), run_time=self.dur(0.7))
            # «la probabilidad de que salte al menos una»
            self.en("alomenos")
            self.play(FadeOut(falsa), FadeOut(p), FadeIn(fo[0]), run_time=self.dur(0.8))
            # «entre ene posiciones»
            self.en("ene")
            self.play(Create(brace), FadeIn(nl), run_time=self.dur(0.7))
            # «aproximadamente ene por pe»
            self.en("nporp")
            self.play(FadeIn(fo[1]), FadeIn(fo[2]), FadeIn(fo[3]), FadeIn(fo[4]), run_time=self.dur(1.2))
            # «Queremos una falsa alarma total de una entre mil»
            self.en("total")
            self.play(FadeIn(tot), run_time=self.dur(0.8))
            # «buscando en mil posiciones»
            self.en("milpos")
            self.play(FadeIn(nmil), run_time=self.dur(0.8))
            # «cada posición tiene que tener»
            self.en("cada")
            self.play(FadeIn(cada), run_time=self.dur(1.0))
            # «una falsa alarma de una entre un millón»
            self.en("millon")
            self.play(FadeIn(mill), run_time=0.5)
            self.play(FadeIn(comp), FadeIn(ok), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
