"""Escena 11 — Sucesos raros: mil pruebas sin falsas alarmas pasan un 26 % de las veces."""
from comun.escena import *
from comun.figuras_c9e6 import *


class SucesosRaros(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.mil_pruebas()
        self.regla()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def mil_pruebas(self):
        with self.narrar("b1"):
            # «los sucesos raros»
            self.en("raros")
            C = Campanas9(centro=(-1.0, -2.2), ancho=9.0, alto=6.6, r_rango=(-3.0, 4.5), v_max=0.45)
            eje = C.eje((0, 1, 2, 3))
            c0 = C.campana(0, 1, C0)
            self.play(FadeIn(eje), Create(c0), run_time=self.dur(0.6))

            # «el umbral en tres voltios»
            self.en("tres")
            u = Line(C.p(3) + DOWN * 0.1, C.p(3) + UP * 3.4, color=ESTIMACION, stroke_width=4)
            ru = Text("3 V", color=ESTIMACION).scale(0.45).next_to(u, UP, buff=0.1)
            self.play(Create(u), FadeIn(ru), run_time=self.dur(0.4))

            # «la falsa alarma»
            self.en("cola")
            cola = C.area(0, 1, 3, 4.5, FA, 0.85)
            lp = lupa(TXT).scale(0.7).move_to(C.p(3.5, 0.06) + UP * 0.35 + RIGHT * 0.15)
            lp.permitir_encima = True
            self.play(FadeIn(cola), run_time=self.dur(0.3))
            self.play(FadeIn(lp, scale=0.5), run_time=self.dur(0.4))

            # «una entre mil»
            self.en("fa")
            fa = MathTex(r"P_{FA} = 0{,}00135", color=FA).scale(0.9).move_to([3.4, 1.8, 0])
            self.play(Write(fa), run_time=self.dur(0.6))

            # «mil pruebas sin señal»
            self.en("mil")
            arriba = VGroup(eje, c0, u, ru, cola)
            self.play(FadeOut(lp), arriba.animate.scale(0.42).move_to([-4.9, 2.6, 0]),
                      fa.animate.scale(0.75).move_to([-1.6, 2.7, 0]), run_time=self.dur(0.5))
            rej = rejilla6(centro=(-3.3, -0.9), ancho=5.6, radio=0.03)
            self.play(LaggedStart(*[FadeIn(d) for d in rej], lag_ratio=0.002), run_time=self.dur(0.8))
            self.rej = rej

            # «¿Cuántas»
            self.en("pregunta")
            pq = Text("¿Cuántas falsas alarmas?", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([3.6, 2.7, 0])
            self.pop(pq)

            # «vas a ver?»
            self.en("ver")
            ops = VGroup(*[Text(f"{k} ?", color=TXT).scale(0.5) for k in (0, 1, 2)]).arrange(RIGHT, buff=0.7)
            ops.move_to([3.6, 1.95, 0])
            self.play(LaggedStart(*[FadeIn(o, shift=UP * 0.1) for o in ops], lag_ratio=0.25), run_time=self.dur(0.6))

            # «una y pico»
            self.en("esperado")
            es = Text("Esperado: 1,35", color=TXT).scale(0.5).move_to([3.6, 1.2, 0])
            self.play(FadeIn(es, shift=UP * 0.1), run_time=self.dur(0.4))

            # «no ver ninguna»
            self.en("hist")
            H = Histograma6(centro=(3.6, -1.6), ancho=5.0, alto=2.8)
            self.play(Create(H.base), FadeIn(H.nums), GrowFromEdge(H.barras[0], DOWN), run_time=self.dur(0.5))

            # «veintiséis por ciento»
            self.en("veintiseis")
            self.play(H.barras[0].animate.set_fill(ESTIMACION, 0.85).set_stroke(ESTIMACION),
                      FadeIn(H.vals[0]), run_time=self.dur(0.35))
            H.vals[0].set_color(ESTIMACION)
            resto = VGroup(*[VGroup(H.barras[i], H.vals[i]) for i in range(1, 5)])
            self.play(LaggedStart(*[FadeIn(g) for g in resto], lag_ratio=0.15), run_time=self.dur(0.6))
            self.play(resto.animate.set_opacity(0.4), run_time=self.dur(0.3))

    # ------------------------------------------------------------ b2
    def regla(self):
        with self.narrar("b2"):
            # «Una de cada cuatro veces»
            self.en("cuatro")
            self.corte()
            rejs = VGroup(*[rejilla6(n=200, columnas=20, ancho=2.2, radio=0.035) for _ in range(4)])
            rejs.arrange_in_grid(2, 2, buff=0.55).move_to([-2.4, -0.2, 0])
            self.play(LaggedStart(*[FadeIn(r) for r in rejs], lag_ratio=0.2), run_time=self.dur(0.5))
            marco = SurroundingRectangle(rejs[3], color=ESTIMACION, buff=0.12, stroke_width=4)
            self.play(rejs[3].animate.set_color(ESTIMACION), Create(marco), run_time=self.dur(0.4))

            # «nunca da falsas alarmas»
            self.en("nunca")
            cero = VGroup(Text("Falsas alarmas: 0", color=VERDE, weight=BOLD).scale(0.55), tilde(VERDE, 0.35))
            cero.arrange(RIGHT, buff=0.2).next_to(marco, RIGHT, buff=0.5)
            self.pop(cero)

            # «La regla práctica»
            self.en("regla")
            self.corte()
            tr = tarjeta6("Regla práctica", ESTIMACION, ancho=3.4).move_to([-3.4, 2.9, 0])
            self.pop(tr)

            # «para medir una probabilidad»
            self.en("medir")
            cont = MathTex(r"\frac{\text{Fallos}}{\text{Pruebas}}", color=INK).scale(0.6).next_to(tr, RIGHT, buff=0.6)
            self.play(FadeIn(cont, shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «al menos unos diez sucesos»
            self.en("diez")
            d = MathTex(r"\text{Ver} \geq 10 \text{ sucesos}", r"\;\Rightarrow\;", r"N \geq 10\,/\,p", color=TXT).scale(0.85)
            d.move_to([0, 1.6, 0])
            self.play(Write(d[0]), run_time=self.dur(0.5))
            self.play(Write(d[1:]), run_time=self.dur(0.5))

            # «Aquí, unas»
            self.en("aqui")
            p1 = MathTex(r"p = 0{,}00135", color=FA).scale(0.8).move_to([-3.4, 0.4, 0])
            self.play(FadeIn(p1, shift=RIGHT * 0.15), run_time=self.dur(0.35))

            # «siete mil cuatrocientas pruebas»
            self.en("n7400")
            n1 = MathTex(r"N \approx 10\,/\,0{,}00135 \approx 7.400", color=TXT).scale(0.8).move_to([2.2, 0.4, 0])
            self.play(Write(n1), run_time=self.dur(0.6))

            # «Para un error de»
            self.en("error")
            hueco = VGroup(DashedLine([-4.8, -0.5, 0], [-2.0, -0.5, 0], color=INK, stroke_width=2),
                           DashedLine([0.0, -0.5, 0], [4.4, -0.5, 0], color=INK, stroke_width=2))
            self.play(Create(hueco), run_time=self.dur(0.35))

            # «uno entre un millón»
            self.en("millon")
            p2 = MathTex(r"p = 1\,/\,1.000.000", color=FA).scale(0.8).move_to([-3.4, -0.3, 0])
            self.play(FadeOut(hueco[0]), FadeIn(p2, shift=RIGHT * 0.15), run_time=self.dur(0.4))

            # «diez millones»
            self.en("diezmillones")
            n2 = MathTex(r"N \approx 10.000.000", color=TXT).scale(0.8).move_to([2.2, -0.3, 0])
            self.play(FadeOut(hueco[1]), Write(n2), run_time=self.dur(0.5))

            # «Cero errores vistos»
            self.en("vistos")
            a = Text("Cero errores vistos", color=TXT, weight=BOLD).scale(0.8)
            b = VGroup(Text("≠", color=ERROR, weight=BOLD).scale(0.9), Text("Error cero", color=TXT, weight=BOLD).scale(0.8))
            b.arrange(RIGHT, buff=0.25)
            fila = VGroup(a, b).arrange(RIGHT, buff=0.35).move_to([0, -1.9, 0])
            self.pop(a)

            # «no es error cero»
            self.en("noes")
            self.pop(b)

            # «no has probado lo bastante»
            self.en("bastante")
            rot = Text("Pruebas:", color=INK).scale(0.48).move_to([-1.2, -3.2, 0])
            n = Integer(1000, group_with_commas=False, color=INK).scale(0.6).next_to(rot, RIGHT, buff=0.2)
            self.play(FadeIn(rot), FadeIn(n), run_time=0.3)
            self.play(ChangeDecimalToValue(n, 9999), run_time=self.dur(1.6), rate_func=linear)
