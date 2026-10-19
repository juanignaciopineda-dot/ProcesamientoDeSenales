"""Escena 04 — El coste de cada decisión con el análisis en 1,3: decir sano cuesta 2,2; decir enfermo, 0,56."""
from comun.escena import *
from comun.figuras_c9e5 import *


class ElCosteDeCadaDecision(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.medicion()
        self.cuentas()
        self.regla()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def medicion(self):
        C = campanas_e5(centro=(-1.4, -2.7), ancho=9.6, alto=4.6)
        eje = C.eje((0, 1, 2), rotulo=False)
        c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
        with self.narrar("b1"):
            # «El análisis sale uno coma tres»
            self.en("regla")
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.7))
            rg = C.regla(MEDICION, alto=2.6)
            t13 = Text("1,3", color=MEDIDA, weight=BOLD).scale(0.5).next_to(rg, UP, buff=0.1)
            self.play(Create(rg), FadeIn(t13), run_time=self.dur(0.4))

            # «La regla del máximo a posteriori»
            self.en("rotulo")
            rot = Text("Máximo a posteriori", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([-4.3, 3.3, 0])
            self.play(FadeIn(rot, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «decía cero»
            self.en("map")
            um = umbral9_e5(C, U_MAP, alto=2.0)
            zona = C.region(C.r0, U_MAP, C0)
            sano = Text("Sano", color=C0, weight=BOLD).scale(0.5).next_to(rot, DOWN, buff=0.25)
            self.play(Create(um), FadeIn(zona), run_time=self.dur(0.5))
            self.pop(sano)

            # «Miremos los costes»
            self.en("tabla")
            mini = tabla_costes_mini9(centro=(5.0, 1.9))
            self.play(FadeIn(mini, shift=LEFT * 0.3), run_time=self.dur(0.5))

            # «la probabilidad a posteriori»
            self.en("post")
            s0 = C.segmento(0, MEDICION, P0, C0)
            s1 = C.segmento(2, MEDICION, P1, C1).shift(RIGHT * 0.09)
            s0.shift(LEFT * 0.09)
            self.play(Create(s0), Create(s1), run_time=self.dur(0.5))

            # «cero coma cuarenta y cuatro»
            self.en("p44")
            f1 = MathTex(r"P(\text{Enfermo}\mid 1{,}3) = 0{,}44", color=C1).scale(0.7).move_to([4.6, -0.3, 0])
            self.play(FadeIn(f1, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «cero coma cincuenta y seis»
            self.en("p56")
            f0 = MathTex(r"P(\text{Sano}\mid 1{,}3) = 0{,}56", color=C0).scale(0.7).next_to(f1, DOWN, buff=0.3)
            self.play(FadeIn(f0, shift=LEFT * 0.2), run_time=self.dur(0.4))

    # ------------------------------------------------------------ b2
    def cuentas(self):
        with self.narrar("b2"):
            # «Si digo sano»
            self.en("digosano")
            self.corte()
            mini = tabla_costes_mini9(centro=(4.9, 2.4))
            B = BarrasSE9(centro=(4.6, -1.6), alto=2.4, ancho=0.8, hueco=0.6, escala=0.42)
            B.fijar(1 - post_enfermo9(MEDICION))
            self.add(mini, B, B.vals[0], B.vals[1])
            ds = Text("Decir sano:", color=C0, weight=BOLD).scale(0.6).move_to([-5.0, 1.3, 0], aligned_edge=LEFT)
            self.play(FadeIn(ds, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «cero coma cuarenta y cuatro»
            self.en("x44")
            a44 = MathTex(r"0{,}44", color=C1).scale(0.9).next_to(ds, RIGHT, buff=1.2)
            self.play(FadeIn(a44, shift=DOWN * 0.6), run_time=self.dur(0.4))

            # «eso cuesta cinco»
            self.en("x5")
            c5 = MathTex(r"5", r"\cdot", color=ERROR).scale(0.9).next_to(a44, LEFT, buff=0.12)
            self.play(TransformFromCopy(mini.cinco, c5[0]), FadeIn(c5[1]), run_time=self.dur(0.5))

            # «dos coma dos»
            self.en("r22")
            r22 = MathTex(r"= 2{,}2", color=ERROR).scale(0.9).next_to(a44, RIGHT, buff=0.15)
            self.pop(r22)

            # «Si digo enfermo»
            self.en("digoenf")
            de = Text("Decir enfermo:", color=C1, weight=BOLD).scale(0.6).move_to([-5.0, -0.4, 0], aligned_edge=LEFT)
            self.play(FadeIn(de, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «probabilidad cero coma cincuenta y seis»
            self.en("x56")
            a56 = MathTex(r"0{,}56", color=C0).scale(0.9).move_to([a44.get_center()[0], -0.4, 0])
            self.play(FadeIn(a56, shift=DOWN * 0.6), run_time=self.dur(0.4))

            # «eso cuesta uno»
            self.en("x1")
            c1 = MathTex(r"1", r"\cdot", color=ESTIMACION).scale(0.9).next_to(a56, LEFT, buff=0.12)
            self.play(TransformFromCopy(mini.uno, c1[0]), FadeIn(c1[1]), run_time=self.dur(0.5))

            # «cero coma cincuenta y seis»
            self.en("r056")
            r056 = MathTex(r"= 0{,}56", color=VERDE).scale(0.9).next_to(a56, RIGHT, buff=0.15)
            self.pop(r056)

            # «cuatro veces más barato»
            self.en("cuatro")
            cu = MathTex(r"2{,}2 \div 0{,}56 \approx 4", color=TXT).scale(0.8).move_to([-2.2, -2.2, 0])
            marco = SurroundingRectangle(VGroup(de, r056), color=VERDE, buff=0.18, stroke_width=4)
            self.play(FadeIn(cu), Create(marco), run_time=self.dur(0.5))

            # «sano sea más probable»
            self.en("aunque")
            self.play(B.rellenos[0].animate(rate_func=there_and_back).set_fill(opacity=1),
                      B.vals[0].animate(rate_func=there_and_back).scale(1.3), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b3
    def regla(self):
        with self.narrar("b3"):
            # «la regla de riesgo mínimo»
            self.en("riesgo")
            self.corte()
            t = self.palabra("Riesgo mínimo", AMBAR, 1.2).move_to([0, 2.0, 0])
            self.pop(t)

            # «la hipótesis más probable»
            self.en("tacha")
            h = Text("La hipótesis más probable", color=INK).scale(0.6).move_to([0, 0.3, 0])
            self.play(FadeIn(h), run_time=self.dur(0.35))
            self.play(Create(tachar(h)), run_time=self.dur(0.35))

            # «menor coste esperado»
            self.en("coste")
            d = Text("La decisión de menor coste esperado", color=VERDE, weight=BOLD).scale(0.65).move_to([0, -1.2, 0])
            self.pop(d)
