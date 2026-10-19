"""Escena 13 — Cierre: resumen del episodio y anuncio del capítulo 10, «Mil grabaciones del mismo ruido»."""
from comun.escena import *
from comun.figuras_c9e6 import *


class Cierre(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.resumen()
        self.lo_que_viene()
        self.wait(1.2)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resumen(self):
        with self.narrar("b1"):
            # «dejado las campanas»
            self.en("campanas")
            C = Campanas9(centro=(0.0, -1.8), ancho=8.0, alto=5.0, r_rango=(-3.0, 5.0), v_max=0.45)
            camp = VGroup(C.campana(0, 1, C0), C.campana(2, 1, C1))
            self.add(camp)
            self.play(FadeOut(camp, shift=DOWN * 0.3), run_time=self.dur(0.5))

            # «decidido con datos»
            self.en("datos")
            tira = tira6(centro=(-3.3, 2.9), lado=0.5)
            self.play(LaggedStart(*[FadeIn(f, shift=DOWN * 0.15) for f in tira], lag_ratio=0.08), run_time=self.dur(0.6))

            # «una escalera»
            self.en("escalera")
            P = PlanoRoc9(origen=(-5.6, -2.6), lado=4.6)
            E = Escalera6(P)
            esc = E.todo()
            diag = P.diagonal()
            self.play(FadeIn(P), Create(diag), Create(esc), run_time=self.dur(0.8))

            # «su área»
            self.en("area")
            ar = E.area()
            v = Text("0,81", color=ROC, weight=BOLD).scale(0.6).move_to(P.p(0.66, 0.3))
            self.play(FadeIn(ar), FadeIn(v), run_time=self.dur(0.4))

            # «lo bien que el detector ordena»
            self.en("ordena")
            t1 = tarjeta6("Área = Lo bien que ordena", ROC, ancho=5.2).move_to([3.2, 1.6, 0])
            self.pop(t1)

            # «ordenar no es cortar»
            self.en("cortar")
            t2 = tarjeta6("Ordenar ≠ Cortar", ESTIMACION, ancho=5.2).move_to([3.2, 0.3, 0])
            self.pop(t2)

            # «cero errores vistos no es error cero»
            self.en("vistos")
            t3 = tarjeta6("Cero errores vistos ≠ Error cero", ERROR, ancho=5.2).move_to([3.2, -1.0, 0])
            self.pop(t3)
            self.todo = VGroup(tira, P, diag, esc, ar, v)
            self.tarjetas = VGroup(t1, t2, t3)

    # ------------------------------------------------------------ b2
    def lo_que_viene(self):
        with self.narrar("b2"):
            # «cerramos las pruebas de hipótesis»
            self.en("cierre")
            cap = etiqueta("Capítulo 9 · Pruebas de hipótesis", TXT, 0.6, weight=BOLD)
            tic = tilde(VERDE, 0.45)
            cab = VGroup(cap, tic).arrange(RIGHT, buff=0.3).move_to([0, 2.6, 0])
            self.play(FadeOut(self.todo), self.tarjetas.animate.arrange(DOWN, buff=0.3).move_to([0, -0.2, 0]),
                      run_time=self.dur(0.6))
            self.play(FadeIn(cap, shift=DOWN * 0.15), run_time=self.dur(0.35))
            self.pop(tic)

            # «el próximo episodio»
            self.en("proximo")
            self.corte()
            c10 = etiqueta("Capítulo 10 · Procesos aleatorios", ESTIMACION, 0.6, weight=BOLD).move_to([0, 3.3, 0])
            self.pop(c10)

            # «empezamos justo por ahí»
            self.en("ahi")
            pila = VGroup(*[ruido6(centro=(0, 2.2 - 0.62 * i), ancho=11.5, alto=0.55, n=80, semilla=8 if i == 0 else 40 + i,
                                   ancho_trazo=2.5 if i == 0 else 2.0, opacidad=1.0 if i == 0 else 0.7)
                            for i in range(10)])
            for c in pila:
                c.permitir_encima = True
            self.play(Create(pila[0]), run_time=self.dur(0.8), rate_func=linear)

            # «muchas grabaciones»
            self.en("grabaciones")
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in pila[1:4]], lag_ratio=0.3), run_time=self.dur(0.8))

            # «una encima de otra»
            self.en("apila")
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in pila[4:]], lag_ratio=0.15), run_time=self.dur(1.0))

            # «Mil grabaciones del mismo ruido»
            self.en("titulo")
            fondo = RoundedRectangle(corner_radius=0.2, width=9.6, height=1.5, color=ESTIMACION, stroke_width=3)
            fondo.set_fill(FONDO, 0.92).move_to([0, -0.3, 0])
            fondo.permitir_encima = True
            ep = Text("Episodio 1", color=INK).scale(0.45)
            tt = Text("Mil grabaciones del mismo ruido", color=TXT, weight=BOLD).scale(0.7)
            g = VGroup(ep, tt).arrange(DOWN, buff=0.15).move_to(fondo)
            self.play(pila.animate.set_stroke(opacity=0.35), FadeIn(fondo), run_time=0.3)
            self.pop(g)
