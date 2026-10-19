"""Escena 07 — Dos varas: las dos reglas medidas por su probabilidad de error y por su coste medio."""
from comun.escena import *
from comun.figuras_c9e5 import *


class DosVaras(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.reglas()
        self.map()
        self.riesgo()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def reglas(self):
        C = campanas_e5(centro=(0.2, 0.3), ancho=9.0, alto=4.0)
        self.C = C
        eje = C.eje((0, 1, 2), rotulo=False, escala=0.42)
        c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        with self.narrar("b1"):
            # «Tenemos dos reglas»
            self.en("campanas")
            l1 = umbral9_e5(C, U_MAP, alto=2.4)
            l2 = umbral9_e5(C, U_R, alto=2.4)
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.7))
            self.play(Create(l1), Create(l2), run_time=self.dur(0.4))

            # «la del máximo a posteriori»
            self.en("map")
            r1 = Text("Máximo a posteriori", color=ESTIMACION).scale(0.42)
            r1.next_to(l1.get_top(), UP, buff=0.12).align_to(l1, LEFT)
            self.play(FadeIn(r1, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «uno coma cuarenta y dos»
            self.en("u142")
            n1 = Text("1,42", color=ESTIMACION, weight=BOLD).scale(0.4).move_to(C.p(U_MAP) + DOWN * 0.72)
            self.play(FadeIn(n1), run_time=self.dur(0.3))

            # «la de riesgo mínimo»
            self.en("riesgo")
            r2 = Text("Riesgo mínimo", color=ESTIMACION).scale(0.42)
            r2.next_to(l2.get_top(), UP, buff=0.55).align_to(l2, RIGHT)
            self.play(FadeIn(r2, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «cero coma sesenta y dos»
            self.en("u062")
            n2 = Text("0,62", color=ESTIMACION, weight=BOLD).scale(0.4).move_to(C.p(U_R) + DOWN * 0.72)
            self.play(FadeIn(n2), run_time=self.dur(0.3))

            # «Midamos las dos»
            self.en("tabla")
            T = TablaDosReglas9()
            self.T = T
            self.play(FadeIn(T), run_time=self.dur(0.5))
            self.play(FadeIn(T.cabecera(0)), FadeIn(T.cabecera(1)), run_time=self.dur(0.3))

            # «la probabilidad de error»
            self.en("colerr")
            self.pop(T.cabecera(2))

            # «el coste medio»
            self.en("colcoste")
            self.pop(T.cabecera(3))
            self.l1, self.l2 = l1, l2

    # ------------------------------------------------------------ b2
    def map(self):
        C, T = self.C, self.T
        y_c = -3.55
        with self.narrar("b2"):
            # «falsa alarma cero coma cero setenta y siete»
            self.en("fa")
            self.play(self.l1.animate.set_stroke(width=7), run_time=0.2)
            k0 = C.area(0, 1, U_MAP, C.r1, ERROR, 0.55)
            self.play(FadeIn(k0), FadeIn(T.celda(0, 0, "0,077")), run_time=self.dur(0.5))

            # «fallo cero coma veintiocho»
            self.en("fallo")
            k1 = C.area(2, 1, C.r0, U_MAP, ERROR, 0.35)
            self.play(FadeIn(k1), FadeIn(T.celda(0, 1, "0,28")), run_time=self.dur(0.5))

            # «Su error ya lo sabemos»
            self.en("errya")
            e = MathTex(r"\text{Error} = 0{,}7 \cdot 0{,}077 + 0{,}3 \cdot 0{,}28", color=INK).scale(0.65)
            e.move_to([0.3, y_c, 0])
            self.play(FadeIn(e, shift=UP * 0.15), run_time=self.dur(0.4))

            # «cero coma ciento treinta y nueve»
            self.en("err")
            self.pop(T.celda(0, 2, "0,139", ERROR))

            # «Su coste»
            self.en("coste")
            a = MathTex(r"\text{Coste} = 0{,}7 \cdot 0{,}077 \cdot 1 + 0{,}3 \cdot 0{,}28 \cdot 5", color=INK)
            a.scale(0.65).move_to(e)
            self.play(FadeOut(e, shift=UP * 0.15), FadeIn(a, shift=UP * 0.15), run_time=self.dur(0.4))

            # «cero coma cero cincuenta y cuatro»
            self.en("c1")
            b = MathTex(r"\text{Coste} =", r"0{,}054", "+", r"0{,}085", r"\cdot 5", r"= 0{,}48", color=INK)
            b.scale(0.65).move_to([0.3, y_c, 0])
            self.play(FadeOut(a), FadeIn(b[:2]), run_time=self.dur(0.4))

            # «de las falsas alarmas»
            self.en("cfa_lbl")
            self.play(b[1].animate.set_color(ESTIMACION).scale(1.15), run_time=self.dur(0.4))

            # «cero coma cero ochenta y cinco»
            self.en("c085")
            b[3].set_color(ERROR)
            self.play(FadeIn(b[2]), FadeIn(b[3]), run_time=self.dur(0.4))

            # «multiplicado por cinco»
            self.en("c2")
            b[4].set_color(ERROR)
            self.pop(b[4])

            # «cero coma cuarenta y ocho»
            self.en("c048")
            self.play(FadeIn(b[5]), run_time=self.dur(0.3))
            self.pop(T.celda(0, 3, "0,48", ESTIMACION))
            self.k0, self.k1, self.cuenta = k0, k1, b

    # ------------------------------------------------------------ b3
    def riesgo(self):
        C, T = self.C, self.T
        y_c = -3.55
        with self.narrar("b3"):
            # «la falsa alarma sube»
            self.en("fa")
            k0 = C.area(0, 1, U_R, C.r1, ERROR, 0.55)
            self.play(self.l1.animate.set_stroke(width=4, opacity=0.4), self.l2.animate.set_stroke(width=7),
                      FadeOut(self.cuenta), run_time=0.25)
            self.play(Transform(self.k0, k0), FadeIn(T.celda(1, 0, "0,27")), run_time=self.dur(0.6))

            # «el fallo baja»
            self.en("fallo")
            k1 = C.area(2, 1, C.r0, U_R, ERROR, 0.35)
            self.play(Transform(self.k1, k1), FadeIn(T.celda(1, 1, "0,084")), run_time=self.dur(0.6))

            # «Su error»
            self.en("errlbl")
            e = MathTex(r"\text{Error} = 0{,}7 \cdot 0{,}27 + 0{,}3 \cdot 0{,}084", color=INK).scale(0.65)
            e.move_to([0.3, y_c, 0])
            self.play(FadeIn(e, shift=UP * 0.15), run_time=self.dur(0.4))

            # «cero coma veintiuno»
            self.en("err")
            self.pop(T.celda(1, 2, "0,21", ERROR))

            # «cero coma diecinueve»
            self.en("c1")
            b = MathTex(r"\text{Coste} =", r"0{,}19", "+", r"0{,}125", r"= 0{,}31", color=INK).scale(0.65)
            b.move_to([0.3, y_c, 0])
            b[1].set_color(ESTIMACION)
            b[3].set_color(ERROR)
            self.play(FadeOut(e, shift=UP * 0.15), FadeIn(b[:3], shift=UP * 0.15), run_time=self.dur(0.4))

            # «cero coma ciento veinticinco»
            self.en("c2")
            self.play(FadeIn(b[3]), run_time=self.dur(0.35))

            # «Cero coma treinta y uno»
            self.en("c031")
            self.play(FadeIn(b[4]), run_time=self.dur(0.3))
            self.pop(T.celda(1, 3, "0,31", ESTIMACION))
