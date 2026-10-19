"""Escena 12 — Las llamadas de la centralita: 0 · 1 · 2 · 10 con 0,4 · 0,3 · 0,2 · 0,1; con el cuadrado, la media (1,7)."""
from comun.escena import *


class LasLlamadas(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.B = BarrasLlamadas8(centro=(0, -1.3), ancho=10.0, alto=2.8)
        self.pregunta()
        self.media()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pregunta(self):
        B = self.B
        porque = Text("¿Por qué el cuadrado?", color=ESTIMACION, weight=BOLD).scale(1.0).move_to([0, 3.0, 0])
        cas = casillas(3, rojas=(), centro=(0, 0.6), lado=1.4, hueco=0.6)
        qs = VGroup(*[Text("?", color=c, weight=BOLD).scale(1.2).move_to(cas.cas[i]) for i, c in
                      enumerate((ESTIMACION, VERDE, CIAN))])
        centralita = caja("Centralita", INK, ancho=3.2, alto=1.0, scale=0.8).move_to([-4.8, 3.0, 0])
        entradas = VGroup(*[Arrow([-7.0, 2.6 + 0.27 * i, 0], [-6.4, 2.6 + 0.27 * i, 0], buff=0, color=MEDIDA,
                                  stroke_width=3, max_tip_length_to_length_ratio=0.5) for i in range(4)])
        cuentas = Text("Llamadas por minuto", color=INK, weight=BOLD).scale(0.65).move_to([3.0, 3.0, 0])
        reloj_m = reloj(TXT).scale(0.7).move_to([5.9, 3.0, 0])
        self.reloj = reloj_m
        self.cuentas = cuentas
        self.centralita = VGroup(centralita, entradas)

        with self.narrar("b1"):
            # «¿Por qué el cuadrado»
            self.en("porque")
            self.pop(porque)

            # «otra forma de medir el error»
            self.en("otra")
            self.play(FadeIn(cas, lag_ratio=0.3), run_time=self.dur(0.7))

            # «es una elección»
            self.en("eleccion")
            self.resaltar(cas, color=ESTIMACION, escala=1.08, run_time=0.6)

            # «cada elección da otra respuesta»
            self.en("respuesta")
            self.play(LaggedStart(*[FadeIn(q, scale=0.5) for q in qs], lag_ratio=0.3), run_time=self.dur(0.8))

            # «Veámoslo con un ejemplo»
            self.en("ejemplo")
            self.corte()
            self.play(FadeIn(centralita, shift=DOWN * 0.2), FadeIn(entradas, lag_ratio=0.2), run_time=self.dur(0.7))

            # «Cuentas las llamadas»
            self.en("cuentas")
            self.play(FadeIn(cuentas), FadeIn(B.base), FadeIn(VGroup(*B.nums.values())), run_time=self.dur(0.7))

            # «en un minuto»
            self.en("minuto")
            self.play(FadeIn(reloj_m, scale=0.6), run_time=self.dur(0.5))

            # «Ninguna, el cuarenta por ciento»
            self.en("ninguna")
            self.play(GrowFromEdge(B.barras[0], DOWN), run_time=self.dur(0.5))
            self.play(FadeIn(B.pct(0)), run_time=self.dur(0.3))

            # «Una, el treinta»
            self.en("una")
            self.play(GrowFromEdge(B.barras[1], DOWN), FadeIn(B.pct(1)), run_time=self.dur(0.5))

            # «Dos, el veinte»
            self.en("dos")
            self.play(GrowFromEdge(B.barras[2], DOWN), FadeIn(B.pct(2)), run_time=self.dur(0.5))

            # «diez de golpe»
            self.en("diez")
            self.play(GrowFromEdge(B.barras[10], DOWN), run_time=self.dur(0.5))

            # «el diez por ciento restante»
            self.en("restante")
            self.pop(B.pct(10))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def media(self):
        B = self.B
        cuad = Text("Error al cuadrado → Media", color=ESTIMACION, weight=BOLD).scale(0.75).move_to([-3.9, 3.1, 0])
        F = formula(r"0\cdot 0{,}4", "+", r"1\cdot 0{,}3", "+", r"2\cdot 0{,}2", "+", r"10\cdot 0{,}1", "=", r"1{,}7",
                    escala=0.9, colores={8: ESTIMACION}).move_to([3.0, 2.5, 0])
        mk = B.marcador(1.7, ESTIMACION)
        et = Text("1,7", color=ESTIMACION, weight=BOLD).scale(0.6).next_to(mk, DOWN, buff=0.12)
        tira = Arrow(B.p(1.7) + DOWN * 1.05 + RIGHT * 0.5, B.p(10) + DOWN * 1.05 + LEFT * 0.3, buff=0, color=ERROR,
                     stroke_width=5)
        llave = BraceBetweenPoints(B.p(1) + DOWN * 1.7, B.p(10) + DOWN * 1.7, direction=DOWN, color=ERROR)
        nueve = Text("9", color=ERROR, weight=BOLD).scale(0.7).next_to(llave, DOWN, buff=0.05)

        with self.narrar("b2"):
            # «Con el error al cuadrado»
            self.en("cuadrado")
            self.play(FadeOut(self.cuentas), FadeOut(self.centralita), FadeOut(self.reloj), run_time=0.25)
            self.play(FadeIn(cuad, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «la mejor apuesta es la media»
            self.en("media")
            self.resaltar(cuad, color=ESTIMACION, escala=1.05, run_time=0.5)

            # «Cero por cero coma cuatro»
            self.en("c0")
            self.play(FadeIn(F[0], shift=UP * 0.1), run_time=self.dur(0.4))

            # «más uno por cero coma tres»
            self.en("c1")
            self.play(FadeIn(F[1]), FadeIn(F[2], shift=UP * 0.1), run_time=self.dur(0.4))

            # «más dos por cero coma dos»
            self.en("c2")
            self.play(FadeIn(F[3]), FadeIn(F[4], shift=UP * 0.1), run_time=self.dur(0.4))

            # «más diez por cero coma uno»
            self.en("c10")
            self.play(FadeIn(F[5]), FadeIn(F[6], shift=UP * 0.1), run_time=self.dur(0.4))

            # «uno coma siete llamadas»
            self.en("res")
            self.play(FadeIn(F[7]), FadeIn(F[8], scale=1.3), run_time=self.dur(0.4))
            self.play(FadeIn(mk, shift=UP * 0.3), FadeIn(et), run_time=self.dur(0.5))

            # «Ese diez raro tira de la media»
            self.en("tira")
            self.play(GrowArrow(tira), run_time=self.dur(0.7))

            # «castiga mucho fallar por nueve»
            self.en("castiga")
            self.play(FadeIn(llave), FadeIn(nueve), run_time=self.dur(0.6))
