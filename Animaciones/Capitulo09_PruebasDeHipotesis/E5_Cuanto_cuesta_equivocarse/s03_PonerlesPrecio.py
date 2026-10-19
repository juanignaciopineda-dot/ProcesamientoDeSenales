"""Escena 03 — Ponerles precio: la pregunta pendiente del test médico, el análisis de sangre y la tabla de costes."""
from comun.escena import *
from comun.figuras_c9e5 import *


class PonerlesPrecio(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.pendiente()
        self.analisis()
        self.costes()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pendiente(self):
        with self.narrar("b1"):
            # «Hace tres episodios»
            self.en("tarjeta")
            tj = tarjeta9("Siempre sano → 1 %", ERROR, ancho=4.4, alto=0.95, escala=0.6).move_to([0, 2.4, 0])
            q = Text("?", color=AMBAR, weight=BOLD).scale(0.9).next_to(tj, RIGHT, buff=0.3)
            self.play(FadeIn(tj, shift=DOWN * 0.2), run_time=self.dur(0.4))
            self.pop(q)

            # «En el test médico»
            self.en("test")
            gr = rejilla3(1, lado=0.3, centro=(0.0, -0.9))
            gr.save_state()
            self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in gr], lag_ratio=0.01), run_time=self.dur(1.0))

            # «lo mejor era decir siempre sano»
            self.en("siempre")
            self.resaltar(tj, color=ERROR)
            self.play(gr.animate.set_color(C0), run_time=self.dur(0.4))

            # «Era absurdo»
            self.en("absurdo")
            tc = tachar(tj)
            self.sfx("error", gain=-16)
            self.play(Create(tc), run_time=self.dur(0.35))

            # «mandar a casa a un enfermo»
            self.en("casa")
            self.play(FadeOut(gr), FadeOut(q), VGroup(tj, tc).animate.scale(0.7).move_to([0, 3.3, 0]),
                      run_time=self.dur(0.35))
            ca = casita9(1.3).move_to([-4.4, 0.2, 0])
            en = persona(ERROR).scale(1.1).move_to([-2.6, 0.1, 0])
            self.play(FadeIn(ca), FadeIn(en), run_time=self.dur(0.4))
            self.play(en.animate.move_to([-3.4, 0.1, 0]), run_time=self.dur(0.6))

            # «repetirle la prueba a un sano»
            self.en("repetir")
            sa = persona(SENAL).scale(1.1).move_to([3.0, 0.1, 0])
            tb = tubo9(alto=1.2).move_to([4.2, 0.25, 0])
            self.play(FadeIn(sa), FadeIn(tb, shift=UP * 0.2), run_time=self.dur(0.4))

            # «cuenta los dos fallos igual»
            self.en("balanza")
            b = Balanza(centro=(0.0, 1.0), semi=3.2)
            self.play(FadeIn(b), run_time=self.dur(0.35))
            izq = VGroup(ca, en)
            der = VGroup(sa, tb)
            self.play(izq.animate.scale(0.6).next_to(b.izq[1], UP, buff=0.05),
                      der.animate.scale(0.6).next_to(b.der[1], UP, buff=0.05), run_time=self.dur(0.6))
            b.izq.add(izq)
            b.der.add(der)
            self.b = b

    # ------------------------------------------------------------ b2
    def analisis(self):
        b = self.b
        with self.narrar("b2"):
            # «Pongámosles precio»
            self.en("precio")
            e1 = etiqueta_precio9().next_to(b.izq[1], DOWN, buff=0.25)
            e2 = etiqueta_precio9().next_to(b.der[1], DOWN, buff=0.25)
            self.play(FadeIn(e1, shift=DOWN * 0.2), FadeIn(e2, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «las mismas campanas»
            self.en("campanas")
            self.corte()
            C = campanas_e5(centro=(0.0, -2.4), alto=4.6)
            eje = C.eje((0, 1, 2), rotulo=False)
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            self.play(Create(eje.base), run_time=0.3)
            self.play(Create(c0), Create(c1), FadeIn(eje.nums), run_time=self.dur(0.9))

            # «un análisis de sangre»
            self.en("analisis")
            ra = Text("Resultado del análisis", color=INK).scale(0.42).move_to(C.p(3.9) + DOWN * 0.34)
            tb = tubo9(alto=0.9).move_to(C.p(4.4) + UP * 0.8)
            self.play(FadeIn(ra), FadeIn(tb, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «En los sanos, centro cero»
            self.en("sanos")
            r0 = Text("Sano · Centro 0", color=C0).scale(0.48).move_to(C.p(-1.6, 0.49))
            self.play(FadeIn(r0, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «En los enfermos, centro dos»
            self.en("enfermos")
            r1 = Text("Enfermo · Centro 2", color=C1).scale(0.48).move_to(C.p(3.7, 0.49))
            self.play(FadeIn(r1, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «De cada diez personas»
            self.en("diez")
            fila = fila_personas7(10, centro=(-0.6, 3.1), paso=0.72, escala=0.62)
            for p in fila.personas:
                p.set_color(INK)
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.15) for p in fila.personas], lag_ratio=0.08),
                      run_time=self.dur(0.8))

            # «tres están enfermas»
            self.en("tres")
            self.play(*[fila.personas[i].animate.set_color(ERROR) for i in (2, 5, 8)], run_time=self.dur(0.4))
            pp = VGroup(MathTex(r"p_1 = 0{,}3", color=C1), MathTex(r"p_0 = 0{,}7", color=C0)).scale(0.75)
            pp.arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(fila, RIGHT, buff=0.45)
            self.play(FadeIn(pp), run_time=self.dur(0.4))

    # ------------------------------------------------------------ b3
    def costes(self):
        with self.narrar("b3"):
            # «una tabla de costes»
            self.en("tabla")
            self.corte()
            T = tabla_costes9(centro=(0.9, -0.7))
            self.play(FadeIn(T), run_time=self.dur(0.5))

            # «Acertar no cuesta nada»
            self.en("aciertos")
            ceros = VGroup(*[Text("0", color=INK, weight=BOLD).scale(0.8).move_to(T.c(i, i)) for i in (0, 1)])
            self.play(FadeIn(ceros, scale=0.5), run_time=self.dur(0.4))

            # «Una falsa alarma»
            self.en("fa")
            rfa = Text("Falsa alarma", color=ESTIMACION).scale(0.4).move_to(T.c(0, 1) + UP * 0.48)
            self.play(T.cel[(0, 1)].animate.set_stroke(ESTIMACION, 5), FadeIn(rfa), run_time=self.dur(0.4))

            # «tratar a un sano»
            self.en("fa_ico")
            ico = VGroup(persona(SENAL).scale(0.55), pastilla9(escala=0.9)).arrange(RIGHT, buff=0.12)
            ico.move_to(T.c(0, 1) + LEFT * 0.75 + DOWN * 0.12)
            self.play(FadeIn(ico), run_time=self.dur(0.4))

            # «cuesta uno»
            self.en("fa1")
            uno = Text("1", color=ESTIMACION, weight=BOLD).scale(0.9).move_to(T.c(0, 1) + RIGHT * 0.65 + DOWN * 0.12)
            self.pop(uno)

            # «Un fallo»
            self.en("fallo")
            rfl = Text("Fallo", color=ERROR).scale(0.4).move_to(T.c(1, 0) + UP * 0.48)
            self.play(T.cel[(1, 0)].animate.set_stroke(ERROR, 5), FadeIn(rfl), run_time=self.dur(0.4))

            # «dejar ir a un enfermo»
            self.en("fallo_ico")
            ico2 = VGroup(persona(ERROR).scale(0.55), casita9(0.6)).arrange(RIGHT, buff=0.12)
            ico2.move_to(T.c(1, 0) + LEFT * 0.75 + DOWN * 0.12)
            self.play(FadeIn(ico2), run_time=self.dur(0.4))

            # «cuesta cinco»
            self.en("fallo5")
            cinco = Text("5", color=ERROR, weight=BOLD).scale(1.2).move_to(T.c(1, 0) + RIGHT * 0.65 + DOWN * 0.12)
            self.sfx("impacto", gain=-18)
            self.pop(cinco, sonido=None)

            # «Los números son inventados»
            self.en("inventados")
            self.play(uno.animate(rate_func=there_and_back).scale(1.35),
                      cinco.animate(rate_func=there_and_back).scale(1.35), run_time=self.dur(0.6))

            # «cinco veces más grave»
            self.en("cinco")
            b = Balanza(centro=(-5.2, 2.5), semi=1.3)
            x5 = Text("× 5", color=ERROR, weight=BOLD).scale(0.6).move_to([-5.2, 0.6, 0])
            self.play(FadeIn(b), run_time=self.dur(0.3))
            self.play(*b.inclinar("der", ang=0.3), FadeIn(x5), run_time=self.dur(0.5))
