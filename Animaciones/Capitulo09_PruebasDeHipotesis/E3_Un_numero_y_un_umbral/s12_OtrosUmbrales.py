"""Escena 12 — Menos falsas alarmas, menos aviones: tres umbrales y la pregunta de la región rara."""
from comun.escena import *
from comun.figuras_c9e3 import *

U = 1.645
XC = (-3.6, 0.0, 3.6)            # columnas: umbral, falsa alarma, detección
Y_ENC, DY = -1.25, 0.72


class OtrosUmbrales(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.C = Campanas9(centro=(0, 0.1), ancho=10.0, alto=4.4, r_rango=(-3.0, 5.0))
        self.tabla()
        self.region_rara()
        self.wait(1.0)
        self.limpiar()

    def celda(self, txt, j, fila, color=TXT):
        return Text(txt, color=color).scale(0.5).move_to([XC[j], Y_ENC - DY * (fila + 1), 0])

    # ------------------------------------------------------------------ b1
    def tabla(self):
        C = self.C
        vt = ValueTracker(U)
        self.vt = vt
        with self.narrar("b1"):
            # «Comparemos con otros umbrales»
            self.en("tabla")
            eje = C.eje((0, 1, 2), rotulo=False, escala=0.45)
            c0, c1 = C.campana(0, 1, C0, 3.5), C.campana(2, 1, C1, 3.5)
            marca = always_redraw(lambda: Line(C.p(vt.get_value()) + DOWN * 0.1, C.p(vt.get_value()) + UP * 2.2,
                                               color=ESTIMACION, stroke_width=4))
            roja = always_redraw(lambda: C.area(0, 1, vt.get_value(), 5, ERROR, 0.55))
            verde = always_redraw(lambda: C.area(2, 1, vt.get_value(), 5, VERDE, 0.3))
            enc = VGroup(Text("Umbral", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([XC[0], Y_ENC, 0]),
                         Text("Falsa alarma", color=ERROR, weight=BOLD).scale(0.5).move_to([XC[1], Y_ENC, 0]),
                         Text("Detección", color=VERDE, weight=BOLD).scale(0.5).move_to([XC[2], Y_ENC, 0]))
            raya = Line([-5.6, Y_ENC - 0.38, 0], [5.6, Y_ENC - 0.38, 0], color=INK, stroke_width=1.5)
            f0 = VGroup(self.celda("1,645 V", 0, 0, ESTIMACION), self.celda("5 %", 1, 0, ERROR),
                        self.celda("64 %", 2, 0, VERDE))
            self.play(FadeIn(eje), FadeIn(c0), FadeIn(c1), FadeIn(roja), FadeIn(verde), FadeIn(marca),
                      run_time=self.dur(0.6))
            self.play(FadeIn(enc), Create(raya), FadeIn(f0), run_time=self.dur(0.6))

            # «En un voltio»
            self.en("u1")
            self.play(vt.animate.set_value(1.0), run_time=self.dur(0.6))
            f1 = [self.celda("1 V", 0, 1, ESTIMACION)]
            self.play(FadeIn(f1[0]), run_time=self.dur(0.3))

            # «dieciséis por ciento»
            self.en("fa16")
            f1.append(self.celda("16 %", 1, 1, ERROR))
            self.play(FadeIn(f1[1], shift=LEFT * 0.1), run_time=self.dur(0.3))

            # «ochenta y cuatro de detección»
            self.en("d84")
            f1.append(self.celda("84 %", 2, 1, VERDE))
            self.play(FadeIn(f1[2], shift=LEFT * 0.1), run_time=self.dur(0.3))

            # «solo un uno por ciento»
            self.en("fa1")
            f2 = [self.celda("1 %", 1, 2, ERROR)]
            self.play(FadeIn(f2[0], shift=LEFT * 0.1), run_time=self.dur(0.3))

            # «dos coma treinta y tres voltios»
            self.en("u233")
            self.play(vt.animate.set_value(2.33), run_time=self.dur(0.8))
            f2.insert(0, self.celda("2,33 V", 0, 2, ESTIMACION))
            self.play(FadeIn(f2[0]), run_time=self.dur(0.3))

            # «cae al treinta y siete»
            self.en("d37")
            f2.append(self.celda("37 %", 2, 2, VERDE))
            self.play(FadeIn(f2[2], shift=LEFT * 0.1), run_time=self.dur(0.3))

            # «Ninguno es mejor en abstracto»
            self.en("ninguno")
            F0, F1, F2 = f0, VGroup(*f1), VGroup(*f2)
            # se ordenan por umbral: 1 V, 1,645 V, 2,33 V
            self.play(F1.animate.shift(UP * DY), F0.animate.shift(DOWN * DY), run_time=self.dur(0.6))

            # «menos falsas alarmas»
            self.en("menosfa")
            y_top, y_bot = Y_ENC - DY + 0.15, Y_ENC - 3 * DY - 0.15
            a_fa = Arrow([XC[1] + 1.0, y_top, 0], [XC[1] + 1.0, y_bot, 0], color=ERROR, buff=0, stroke_width=5)
            self.play(GrowArrow(a_fa), run_time=self.dur(0.5))

            # «menos aviones vistos»
            self.en("menosdet")
            a_d = Arrow([XC[2] + 1.0, y_top, 0], [XC[2] + 1.0, y_bot, 0], color=VERDE, buff=0, stroke_width=5)
            self.play(GrowArrow(a_d), run_time=self.dur(0.5))
        self.tabla_g = VGroup(enc, raya, F0, F1, F2, a_fa, a_d)

    # ------------------------------------------------------------------ b2
    def region_rara(self):
        C, vt = self.C, self.vt
        with self.narrar("b2"):
            # «hemos dado algo por supuesto»
            self.en("supuesto")
            self.play(FadeOut(self.tabla_g), vt.animate.set_value(U), run_time=self.dur(0.7))

            # «todo lo que queda a la derecha»
            self.en("derecha")
            reg = C.region(U, 5, ESTIMACION)
            td = Text("Decir avión", color=ESTIMACION, weight=BOLD).scale(0.45).move_to([C.p(3.3)[0], -0.85, 0])
            self.play(FadeIn(reg), FadeIn(td), run_time=self.dur(0.5))

            # «¿Y si existiera»
            self.en("ysi")
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(0.6).next_to(td, RIGHT, buff=0.2)
            self.pop(q)

            # «otra región, más rara»
            self.en("rara")
            trozos = region_rara9(C, [(-2.6, -2.0), (0.7, 1.2), (2.0, 2.7), (3.5, 4.3)])
            self.play(ReplacementTransform(reg, trozos), run_time=self.dur(0.8))

            # «el mismo cinco por ciento»
            self.en("mismo")
            fa = Text("Falsa alarma = 5 %", color=ERROR, weight=BOLD).scale(0.55).move_to([-3.0, -2.2, 0])
            self.play(FadeIn(fa, shift=UP * 0.1), run_time=self.dur(0.4))

            # «y más detección?»
            self.en("mas")
            mas = Text("¿Detección > 0,64?", color=VERDE, weight=BOLD).scale(0.55).move_to([2.8, -2.2, 0])
            Q = Text("?", color=ESTIMACION, weight=BOLD).scale(2.0).move_to([0, -3.3, 0])
            self.play(FadeIn(mas, shift=UP * 0.1), run_time=self.dur(0.4))
            self.pop(Q)
