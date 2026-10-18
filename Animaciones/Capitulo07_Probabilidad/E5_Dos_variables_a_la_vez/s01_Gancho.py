"""Escena 01 — Gancho: se recibe un uno, ¿qué se envió? Una tabla lo responde; y la varianza de las alturas se parte en dos."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        canal = canal7(centro=(0, 2.4), ancho=7.4, escala=0.8)
        tabla = Tabla2x2(centro=(0, -1.45), lado=1.7)
        with self.narrar("b1"):
            # «Se recibe un uno»
            self.en("recibe")
            uno = MathTex("R=1", color=MEDIDA).scale(1.1).next_to(canal.sal, RIGHT, buff=0.2)
            self.play(FadeIn(canal), run_time=self.dur(0.5))
            self.pop(uno)

            # «¿Qué se envió?»
            self.en("pregunta")
            que = MathTex(r"S=\,?", color=SENAL).scale(0.9).next_to(canal.ent, LEFT, buff=0.2)
            self.pop(que)

            # «Una tabla de cuatro números»
            self.en("tabla")
            self.play(Create(VGroup(*[c for f in tabla.cel for c in f])), FadeIn(VGroup(*tabla.rot_f, *tabla.rot_c)),
                      run_time=self.dur(1.0))

            # «lo responde»
            self.en("responde")
            marco = tabla.marco(1, 1)
            r79 = MathTex(r"0{,}79", color=VERDE).scale(1.3).move_to([4.2, -1.45 - 0.85, 0])
            fl = flecha(marco.get_right() + RIGHT * 0.1, r79.get_left() + LEFT * 0.15, VERDE, 3)
            self.play(Create(marco), GrowArrow(fl), run_time=self.dur(0.5))
            self.pop(r79)

            # «la varianza de las alturas»
            self.en("alturas")
            self.corte()
            al = Alturas7(centro=(0, 0.6), ancho=8.6, alto=2.8)
            self.play(Create(al.base), Create(al.h), Create(al.m), run_time=self.dur(1.2), rate_func=linear)

            # «dos mitades casi iguales»
            self.en("mitades")
            barras = BarrasVar7(origen=(-3.05, -2.5))
            t1 = MathTex(r"41{,}2", color=TXT).scale(0.8).move_to(barras.dentro)
            t2 = MathTex(r"40{,}56", color=TXT).scale(0.8).move_to(barras.entre)
            self.play(FadeIn(barras.dentro, shift=RIGHT * 0.2), run_time=self.dur(0.5))
            self.play(FadeIn(barras.entre, shift=LEFT * 0.2), run_time=self.dur(0.5))
            self.play(FadeIn(t1), FadeIn(t2), run_time=0.3)
        self.wait(1.0)
        self.limpiar()
