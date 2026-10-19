"""Escena 10 — Por probabilidad de error, «siempre sano» (1 %) gana al test (5 %): el absurdo queda pendiente."""
from comun.escena import *
from comun.figuras_c9e2 import *


class NoHacerElTest(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.sorpresa()
        self.absurdo()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def sorpresa(self):
        bang = Text("!", color=ESTIMACION, weight=BOLD).scale(4.0)
        f = MathTex("P_e", "=", "p_0", r"\cdot", "P_{FA}", "+", "p_1", r"\cdot", "P_M", color=TXT).scale(0.85)
        f.move_to([-3.2, 3.1, 0])
        for i, c in ((0, ERROR), (2, C0), (4, ERROR), (6, C1), (8, ERROR)):
            f[i].set_color(c)
        t0 = MathTex(r"0{,}99 \cdot 0{,}05", color=TXT).scale(0.8).move_to([-5.0, 2.1, 0])
        t1 = MathTex(r"+\ 0{,}01 \cdot 0{,}01", color=TXT).scale(0.8).move_to([-2.7, 2.1, 0])
        cinco = MathTex(r"\approx 5\,\%", color=ERROR).scale(0.85).move_to([-0.9, 2.1, 0])
        B = Barras9([0.05, 0.01], ["Test", "Siempre sano"], [ERROR, VERDE], xs=[2.6, 5.0], base_y=-2.6, esc=50.0,
                    ancho=1.4, escala=0.45, textos=["5 %", "1 %"])
        mini = tira_test07(0.45).move_to([-6.3, -1.0, 0])
        G = rejilla3(0, centro=(-3.4, -0.9), lado=0.3)
        for p in G.pts:
            p.set_color(C0)
        G.pts[0].set_color(C1)
        self.B = B

        with self.narrar("b1"):
            # «una sorpresa»
            self.en("sorpresa")
            self.corte()
            self.pop(bang, sonido="impacto")
            self.play(FadeOut(bang, scale=1.4), run_time=self.dur(0.4))

            # «La probabilidad de error de este test»
            self.en("formula")
            self.play(Write(f), run_time=self.dur(0.8))

            # «cero coma noventa y nueve por cero coma cero cinco»
            self.en("t0")
            self.play(Write(t0), run_time=self.dur(0.6))

            # «más cero coma cero uno por cero coma cero uno»
            self.en("t1")
            self.play(Write(t1), run_time=self.dur(0.6))

            # «Casi un cinco por ciento»
            self.en("cinco")
            self.pop(cinco)
            self.play(Create(B.base), GrowFromEdge(B.barras[0], DOWN), FadeIn(B.rots[0]), FadeIn(B.vals[0]),
                      run_time=self.dur(0.7))

            # «siempre sano»
            self.en("siempre")
            self.play(FadeIn(B.rots[1], shift=UP * 0.2), run_time=self.dur(0.4))

            # «sin mirar a nadie»
            self.en("nadie")
            self.play(FadeIn(mini), run_time=0.25)
            self.play(Create(tachar(mini)), run_time=self.dur(0.3))

            # «solo fallaría con los enfermos»
            self.en("enfermos")
            self.play(FadeIn(G), run_time=self.dur(0.4))
            self.play(G.pts[0].animate.set_color(ERROR).scale(1.8), run_time=self.dur(0.4))

            # «un uno por ciento»
            self.en("uno")
            self.play(GrowFromEdge(B.barras[1], DOWN), FadeIn(B.vals[1]), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b2
    def absurdo(self):
        B = self.B
        mejor = Text("Mejor: No hacer el test", color=VERDE, weight=BOLD).scale(0.5).move_to([3.8, 0.8, 0])
        enf = casilla9("Enfermo enviado a casa", C1, ancho=5.2, alto=0.9, escala=0.45).move_to([-3.6, 0.8, 0])
        san = casilla9("Sano que repite la prueba", C0, ancho=5.2, alto=0.9, escala=0.45).move_to([3.6, 0.8, 0])
        igual = MathTex("=", color=TXT).scale(1.6).move_to([0, 0.8, 0])
        duda = Text("?", color=ESTIMACION, weight=BOLD).scale(2.4).move_to([0, -1.4, 0])
        promesa = Text("Dentro de tres episodios", color=ESTIMACION).scale(0.5).move_to([0, -2.9, 0])

        with self.narrar("b2"):
            # «lo mejor sería no hacer el test»
            self.en("nohacer")
            self.play(FadeIn(mejor, shift=DOWN * 0.2), run_time=self.dur(0.5))
            self.resaltar(B.barras[1], color=VERDE)

            # «Es absurdo»
            self.en("absurdo")
            self.play(Create(tachar(mejor)), run_time=self.dur(0.35))
            self.sfx("error", gain=-20)

            # «los dos errores»
            self.en("dos")
            self.corte()
            self.play(FadeIn(enf, shift=RIGHT * 0.3), FadeIn(san, shift=LEFT * 0.3), run_time=self.dur(0.6))

            # «como si costaran lo mismo»
            self.en("igual")
            self.pop(igual)
            self.play(Wiggle(igual, scale_value=1.3), run_time=self.dur(0.8))

            # «dentro de tres episodios»
            self.en("promesa")
            self.pop(duda)
            self.play(FadeIn(promesa, shift=UP * 0.2), run_time=self.dur(0.4))

            # «Guárdate la pregunta»
            self.en("guarda")
            self.play(VGroup(duda, promesa).animate.scale(0.4).move_to([5.6, 3.2, 0]), run_time=self.dur(0.8))
