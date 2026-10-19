"""Escena 11 — El error total: 0,34·0,16 + 0,66·0,04 ≈ 0,084 frente a 0,21 (un 60 % menos)."""
from comun.escena import *


class ErrorTotal(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        c0 = caja("Recibo 0", MEDIDA, ancho=3.2, alto=0.9, scale=0.75).move_to([-3.4, 3.3, 0])
        c1 = caja("Recibo 1", MEDIDA, ancho=3.2, alto=0.9, scale=0.75).move_to([3.4, 3.3, 0])
        w0 = MathTex(r"0{,}66", color=AMBAR).scale(1.4).move_to([-3.4, 2.2, 0])
        w1 = MathTex(r"0{,}34", color=AMBAR).scale(1.4).move_to([3.4, 2.2, 0])
        e0 = MathTex(r"0{,}04", color=ROJO).scale(1.4).move_to([-3.4, 1.1, 0])
        e1 = MathTex(r"0{,}16", color=ROJO).scale(1.4).move_to([3.4, 1.1, 0])
        pw = Text("Peso", color=AMBAR).scale(0.7).move_to([0, 2.2, 0])
        pe = Text("Error", color=ROJO).scale(0.7).move_to([0, 1.1, 0])
        l1 = MathTex(r"0{,}34\cdot 0{,}16", color=TXT).scale(1.4).move_to([0, -0.1, 0])
        l2 = MathTex(r"+\ 0{,}66\cdot 0{,}04", color=TXT).scale(1.4).move_to([0.3, -1.0, 0])
        r084 = MathTex(r"\approx\ 0{,}084", color=VERDE).scale(2.0).move_to([0.2, -2.0, 0])
        esc = 14.0
        ybar = -3.3
        barra = Rectangle(width=0.21 * esc, height=0.7, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
        barra.move_to([-6.0 + 0.21 * esc / 2, ybar, 0])
        corta = Rectangle(width=0.084 * esc, height=0.7, color=ROJO, stroke_width=2.5).set_fill(ROJO, 0.4)
        corta.move_to([-6.0 + 0.084 * esc / 2, ybar, 0])
        var_s = MathTex(r"\sigma^2=0{,}3\cdot 0{,}7=0{,}21", color=TXT).scale(1.1).move_to([2.6, ybar, 0])
        with self.narrar("b1"):
            # «error total»
            self.en("total")
            self.play(FadeIn(c0), FadeIn(c1), FadeIn(w0), FadeIn(w1), FadeIn(e0), FadeIn(e1), FadeIn(pw), FadeIn(pe),
                      run_time=self.dur(0.8))

            # «Cero coma treinta y cuatro por cero coma uno seis»
            self.en("c1")
            self.play(FadeIn(l1, shift=UP * 0.2), run_time=self.dur(0.5))

            # «más cero coma sesenta y seis por cero coma cero cuatro»
            self.en("c2")
            self.play(FadeIn(l2, shift=UP * 0.2), run_time=self.dur(0.5))

            # «cero coma cero ocho cuatro»
            self.en("r084")
            self.pop(r084)

            # «Sin mirar el canal»
            self.en("sin_mirar")
            self.play(FadeIn(barra, shift=RIGHT * 0.3), run_time=self.dur(0.6))

            # «la varianza de lo enviado»
            self.en("var_s")
            self.pop(var_s)

            # «cero coma dos uno»
            self.en("n021")
            self.resaltar(barra, color=AMBAR)

            # «Mirar lo recibido»
            self.en("mirar")
            lp = lupa(TXT).scale(1.8).move_to([5.8, -0.6, 0])
            self.play(FadeIn(lp), run_time=self.dur(0.4))

            # «un sesenta por ciento»
            self.en("sesenta")
            m60 = Text("−60 %", color=VERDE, weight=BOLD).scale(1.1).move_to([-2.0, ybar, 0])
            self.play(Transform(barra, corta), FadeOut(lp), FadeOut(var_s), run_time=self.dur(0.8))
            self.pop(m60)
        self.wait(1.0)
        self.limpiar()
