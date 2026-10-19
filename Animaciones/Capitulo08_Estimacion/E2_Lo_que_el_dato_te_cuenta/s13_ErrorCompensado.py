"""Escena 13 — Dentro de cada columna el error se compensa: 0,27·0,21 − 0,07·0,79 = 0."""
from comun.escena import *


class ErrorCompensado(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.T = Tabla2x2(centro=(-3.2, -0.8), lado=2.0)
        self.vals = [[self.T.valor(i, j, CANAL8[i][j], TXT, 1.1) for j in range(2)] for i in range(2)]
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def bloque1(self):
        T = self.T
        with self.narrar("b1"):
            # «una propiedad que lo explica todo»
            self.en("propiedad")
            self.play(Create(VGroup(*[x for f in T.cel for x in f])), FadeIn(VGroup(*T.rot_f, *T.rot_c)),
                      FadeIn(VGroup(*[v for f in self.vals for v in f])), run_time=self.dur(1.0))

            # «se ve en el canal»
            self.en("canal")
            self.canal = canal7(centro=(3.0, 3.2), ancho=6.0, escala=0.7)
            self.play(FadeIn(self.canal), run_time=self.dur(0.5))

            # «la columna de recibir un uno»
            self.en("col1")
            self.col1 = Rectangle(width=T.lado, height=2 * T.lado, color=AMBAR, stroke_width=6)
            self.col1.move_to((T.c(0, 1) + T.c(1, 1)) / 2)
            self.play(Create(self.col1), run_time=self.dur(0.5))

            # «Cuando se envió un uno»
            self.en("env1")
            self.m11 = T.marco(1, 1, VERDE, 4)
            self.play(Create(self.m11), run_time=self.dur(0.4))

            # «uno menos cero coma setenta y nueve»
            self.en("cuenta")
            self.c1 = MathTex(r"1-0{,}79", color=TXT).scale(1.2).move_to([2.6, -1.8, 0])
            self.pop(self.c1)

            # «cero coma dos uno»
            self.en("e21")
            self.r1 = MathTex(r"=\ +0{,}21", color=VERDE).scale(1.2).next_to(self.c1, RIGHT, buff=0.2)
            self.pop(self.r1)

            # «Cuando se envió un cero»
            self.en("env0")
            self.m01 = T.marco(0, 1, ROJO, 4)
            self.play(Create(self.m01), run_time=self.dur(0.4))

            # «menos cero coma setenta y nueve»
            self.en("e79")
            self.c0 = MathTex(r"0-0{,}79=-0{,}79", color=ROJO).scale(1.2).move_to([3.6, 0.2, 0])
            self.pop(self.c0)

            # «nos quedamos cortos»
            self.en("cortos")
            self.cor = Text("Nos quedamos cortos", color=VERDE).scale(0.7).move_to([4.2, -2.6, 0])
            self.play(FadeIn(self.cor, shift=UP * 0.2), run_time=self.dur(0.4))

            # «nos pasamos»
            self.en("pasamos")
            self.pas = Text("Nos pasamos", color=ROJO).scale(0.7).move_to([4.2, 1.0, 0])
            self.play(FadeIn(self.pas, shift=DOWN * 0.2), run_time=self.dur(0.4))

    def bloque2(self):
        T = self.T
        bal = Balanza(centro=(4.0, 2.4), semi=1.9)
        a = MathTex(r"0{,}27\cdot 0{,}21=0{,}056", color=VERDE).scale(1.0).move_to([4.0, 0.7, 0])
        b = MathTex(r"-\,0{,}07\cdot 0{,}79=-0{,}056", color=ROJO).scale(1.0).move_to([4.0, -0.1, 0])
        resta = MathTex(r"0{,}056-0{,}056", color=TXT).scale(1.1).move_to([4.0, -1.1, 0])
        cero = MathTex(r"=\ 0", color=VERDE).scale(2.0).move_to([4.0, -2.3, 0])
        with self.narrar("b2"):
            # «en promedio dentro de esa columna»
            self.en("promedio")
            self.play(FadeOut(self.canal), FadeOut(self.c1), FadeOut(self.r1), FadeOut(self.c0), FadeOut(self.cor),
                      FadeOut(self.pas), run_time=self.dur(0.4))
            self.play(FadeIn(bal), run_time=self.dur(0.5))

            # «Cero coma veintisiete por cero coma dos uno»
            self.en("a")
            self.play(FadeIn(a, shift=UP * 0.2), *bal.inclinar("izq", 0.2), run_time=self.dur(0.6))

            # «menos cero coma cero siete por cero coma setenta y nueve»
            self.en("b")
            self.play(FadeIn(b, shift=UP * 0.2), *bal.inclinar("der", 0.2), run_time=self.dur(0.6))

            # «Cero coma cero cinco seis menos cero coma cero cinco seis»
            self.en("resta")
            self.play(FadeIn(resta, shift=UP * 0.2), run_time=self.dur(0.5))

            # «seis: cero»
            self.en("cero")
            self.pop(cero)
            self.sfx("exito")

            # «en la otra columna»
            self.en("otra")
            col0 = Rectangle(width=T.lado, height=2 * T.lado, color=AMBAR, stroke_width=6)
            col0.move_to((T.c(0, 0) + T.c(1, 0)) / 2)
            self.play(FadeOut(self.m11), FadeOut(self.m01), ReplacementTransform(self.col1, col0),
                      run_time=self.dur(0.5))

            # «pasa lo mismo»
            self.en("mismo")
            t = MathTex(r"0{,}03\cdot 0{,}955\approx 0{,}63\cdot 0{,}045", color=TXT).scale(0.9).move_to([3.6, -3.4, 0])
            self.pop(t)

            # «se compensa exactamente»
            self.en("compensa")
            ok = Text("Se compensa", color=VERDE, weight=BOLD).scale(0.9).move_to([-3.2, -3.4, 0])
            self.pop(ok)
