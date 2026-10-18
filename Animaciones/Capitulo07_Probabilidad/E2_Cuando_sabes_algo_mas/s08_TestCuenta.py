"""Escena 08 — Test cuenta: de los sesenta positivos, solo diez están enfermos."""
from comun.escena import *


class TestCuenta(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.positivos()
        self.proporcion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def positivos(self):
        g = GrillaMil07(centro=(0, -0.2))
        for p in g.pts[:10]:
            p.set_fill(ROJO, 1)
        self.g = g
        rect10 = g.recuadro(0, 10, ROJO)
        tira = tira_test07(0.6).move_to([-5.5, 2.2, 0])
        mas = Text("+", color=ERROR, weight=BOLD).scale(1.3).move_to(tira.ventana)
        t10 = Text("10 positivos", color=ROJO, weight=BOLD).scale(0.8).move_to([-2.6, 1.5, 0])
        san = Text("990 sanas", color=VERDE, weight=BOLD).scale(0.8).move_to([0, -1.9, 0])
        cuenta = MathTex(r"5\,\%\ \text{de}\ 990", color=TXT).scale(1.5).move_to([-2.2, 2.9, 0])
        casi = MathTex(r"\approx 50", color=AMBAR).scale(1.5).next_to(cuenta, RIGHT, buff=0.4)
        falsos = Text("50 sanas con +", color=AMBAR, weight=BOLD).scale(0.75).move_to([1.2, 1.5, 0])
        rect60 = g.recuadro(0, 60, AMBAR)
        t60 = MathTex(r"\approx 60", color=AMBAR).scale(1.5).move_to([5.2, 1.5, 0])
        self.rect60 = rect60

        with self.narrar("b1"):
            # «De las diez enfermas»
            self.en("diez")
            self.play(FadeIn(g), run_time=self.dur(0.6))
            self.play(Create(rect10), run_time=self.dur(0.4))

            # «detecta prácticamente a todas»
            self.en("detecta")
            self.play(FadeIn(tira), run_time=self.dur(0.4))
            self.pop(mas, sonido="error")

            # «diez positivos»
            self.en("diez_pos")
            self.pop(t10)

            # «Ahora las sanas»
            self.en("sanas")
            self.play(FadeOut(rect10), FadeIn(san), run_time=self.dur(0.4))

            # «El cinco por ciento de novecientas noventa»
            self.en("cuenta")
            self.play(FadeIn(cuenta), run_time=self.dur(0.6))

            # «casi cincuenta»
            self.en("cincuenta")
            self.play(FadeIn(casi), run_time=self.dur(0.4))

            # «sanas que reciben un positivo»
            self.en("falsos")
            self.play(*[p.animate.set_fill(AMBAR, 1) for p in g.pts[10:60]], FadeIn(falsos),
                      run_time=self.dur(0.8))

            # «unos sesenta positivos»
            self.en("sesenta")
            self.play(Create(rect60), FadeIn(t60), run_time=self.dur(0.7))
        self.limpiar_b1 = VGroup(tira, mas, t10, san, cuenta, casi, falsos, t60)

    # ------------------------------------------------------------ b2
    def proporcion(self):
        g, rect60 = self.g, self.rect60
        fila = VGroup(*[p.copy() for p in g.pts[:60]])
        self.add(fila)
        marco10 = SurroundingRectangle(VGroup(*fila[:10]), color=ROJO, buff=0.08, stroke_width=4)
        t10 = Text("10", color=ROJO, weight=BOLD).scale(0.9)
        frac = formula(r"\frac{10}{60}", "=", r"\frac16", r"\approx", r"17\,\%", escala=1.7,
                       colores={4: ERROR}).move_to([0, -0.9, 0])
        test99 = Text("El test acierta: 99 %", color=VERDE, weight=BOLD).scale(0.6).move_to([-5.0, -2.5, 0])
        mas = Text("+", color=ERROR, weight=BOLD).scale(1.6).move_to([-2.5, -2.5, 0])
        ps = persona(VERDE).scale_to_fit_height(1.0).move_to([-0.7, -2.5, 0])
        flecha_ = Arrow([-2.0, -2.5, 0], [-1.3, -2.5, 0], color=INK, stroke_width=4, buff=0.0)
        sano = Text("Lo más probable: sano", color=VERDE, weight=BOLD).scale(0.6).move_to([3.0, -2.5, 0])
        barra_s = Rectangle(width=6.0, height=0.8, color=VERDE, stroke_width=3).set_fill(VERDE, 0.4).move_to([0.3, 1.0, 0])
        barra_e = Rectangle(width=0.5, height=0.8, color=ROJO, stroke_width=3).set_fill(ROJO, 0.4)
        barra_e.next_to(barra_s, RIGHT, buff=0.1)
        l_s = Text("990 sanas", color=TXT, weight=BOLD).scale(0.8).move_to(barra_s)
        l_e = Text("10 enfermas", color=ROJO, weight=BOLD).scale(0.7).next_to(barra_e, DOWN, buff=0.3)
        bal = Balanza(centro=(0, 1.2), semi=3.0)
        falsos_t = Text("50 falsos positivos", color=AMBAR, weight=BOLD).scale(0.85).move_to([-3.0, -2.4, 0])
        enfermos_t = Text("10 enfermos", color=ROJO, weight=BOLD).scale(0.85).move_to([3.0, -2.4, 0])
        dots_f = VGroup(*[Square(0.16, stroke_width=0).set_fill(AMBAR, 1) for _ in range(50)])
        dots_f.arrange_in_grid(rows=5, cols=10, buff=0.04)
        dots_e = VGroup(*[Square(0.16, stroke_width=0).set_fill(ROJO, 1) for _ in range(10)])
        dots_e.arrange_in_grid(rows=1, cols=10, buff=0.04)

        with self.narrar("b2"):
            # «de esos sesenta»
            self.en("esos")
            self.play(g.animate.fade(0.85), FadeOut(self.limpiar_b1), FadeOut(rect60), run_time=self.dur(0.4))
            self.play(fila.animate.scale(1.45).move_to([0, 1.7, 0]), run_time=self.dur(0.6))

            # «solo diez están enfermos»
            self.en("solo_diez")
            marco10.move_to(VGroup(*fila[:10]))
            t10.next_to(marco10, UP, buff=0.15)
            self.play(Create(marco10), FadeIn(t10), run_time=self.dur(0.5))

            # «Diez entre sesenta»
            self.en("diez_sesenta")
            self.play(FadeIn(frac[0]), run_time=self.dur(0.5))

            # «un sexto»
            self.en("sexto")
            self.play(FadeIn(frac[1]), FadeIn(frac[2]), run_time=self.dur(0.4))

            # «un diecisiete por ciento»
            self.en("17")
            self.play(FadeIn(frac[3]), FadeIn(frac[4]), run_time=self.dur(0.5))
            self.sfx("exito")

            # «acierta el noventa y nueve por ciento»
            self.en("acierta")
            self.play(FadeIn(test99), run_time=self.dur(0.5))

            # «un positivo significa»
            self.en("significa")
            self.play(FadeIn(mas), Create(flecha_), run_time=self.dur(0.5))

            # «lo más probable es que estés sano»
            self.en("sano")
            self.play(FadeIn(ps), FadeIn(sano), run_time=self.dur(0.5))

            # «tantísimos más sanos»
            self.en("tantos")
            self.corte()
            self.play(FadeIn(barra_s), FadeIn(l_s), FadeIn(barra_e), FadeIn(l_e), run_time=self.dur(0.8))

            # «superan a todos los enfermos juntos»
            self.en("superan")
            self.play(FadeOut(VGroup(barra_s, l_s, barra_e, l_e)), run_time=0.25)
            dots_f.move_to(bal.izq[1].get_center() + UP * 0.38 + LEFT * 0.0)
            dots_e.move_to(bal.der[1].get_center() + UP * 0.2)
            dots_f.scale(0.6)
            dots_e.scale(0.6)
            dots_f.move_to(bal.izq[1].get_center() + UP * 0.4)
            dots_e.move_to(bal.der[1].get_center() + UP * 0.15)
            self.play(FadeIn(bal), FadeIn(dots_f), FadeIn(dots_e), run_time=self.dur(0.6))
            self.play(*bal.inclinar("izq"), dots_f.animate.shift(DOWN * 0.65), dots_e.animate.shift(UP * 0.65),
                      FadeIn(falsos_t), FadeIn(enfermos_t), run_time=self.dur(0.9))
