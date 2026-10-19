"""Escena 10 — La copia empeorada: A más un ruido propio. Su peso sale cero y el error se queda en 0,8."""
from comun.escena import *
from comun.figuras_c8e5 import *

ESQ = [(5.0, 3.3), (6.1, 3.3)]


class LaCopiaEmpeorada(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        espera = [tarjeta8(t, centro=(0, 0)).scale(0.3).move_to([x, y, 0]) for t, (x, y) in zip((r"B_2", r"B_3"), ESQ)]
        self.add(*espera)
        A = Termo8("A", centro=(-5.0, 1.0), alto=2.2, escala_letra=0.9)
        suma = VGroup(Circle(radius=0.38, color=TXT, stroke_width=4),
                      MathTex("+", color=TXT).scale(1.1)).move_to([-2.2, 1.0, 0])
        B2 = Termo8("B_2", centro=(0.8, 1.0), alto=2.2, escala_letra=0.9)
        f1 = Arrow([-4.5, 1.0, 0], suma.get_left(), buff=0.08, color=INK, stroke_width=4,
                   max_tip_length_to_length_ratio=0.15)
        f2 = Arrow(suma.get_right(), [0.35, 1.0, 0], buff=0.08, color=INK, stroke_width=4,
                   max_tip_length_to_length_ratio=0.15)
        ficha = VGroup(Circle(radius=0.32, color=MEDIDA, stroke_width=0).set_fill(MEDIDA, 1),
                       MathTex("x_A", color=FONDO).scale(0.65)).move_to([-4.3, 1.55, 0])
        r3 = ruido8(centro=(-2.2, -0.9), ancho=1.6, amp=0.13, semilla=12, grosor=4)
        f3 = Arrow([-2.2, -0.55, 0], suma.get_bottom(), buff=0.08, color=RUIDO, stroke_width=4,
                   max_tip_length_to_length_ratio=0.2)
        v3 = MathTex(r"\sigma^2=3", color=RUIDO).scale(0.85).move_to([-3.9, -0.9, 0])
        v4 = MathTex(r"\sigma^2=1+3=4", color=RUIDO).scale(0.85).move_to([0.8, -0.85, 0])
        Bv = Termo8("B", centro=(4.4, 1.0), alto=2.2, escala_letra=0.9)
        Bv.fade(0.55)
        vbv = MathTex(r"\sigma^2=4", color=RUIDO).scale(0.85).move_to([4.4, -0.85, 0]).fade(0.4)
        M, H, igual, C, sis = sistema8([["5", "5"], ["5", "8"]], centro=(-1.5, -2.6), escala=0.85)
        h = formula(r"\mathbf{h}=(0{,}8\,;\,", "0", ")", escala=1.0, colores={1: ERROR}).move_to([3.4, -2.2, 0])
        e08 = MathTex(r"\text{Error}=0{,}8", color=ERROR).scale(1.0).move_to([3.4, -3.05, 0])
        como = Text("Igual que solo A", color=INK).scale(0.5).move_to([3.4, -3.65, 0])

        with self.narrar("b1"):
            # «una copia empeorada»
            self.en("b2")
            self.play(espera[0].animate.scale(1 / 0.3).move_to([0.8, 0.6, 0]), run_time=self.dur(0.4))
            self.play(espera[0].animate.stretch(0.03, 0), run_time=0.2)
            self.remove(espera[0])
            self.play(FadeIn(A), GrowArrow(f1), FadeIn(suma), GrowArrow(f2), FadeIn(B2), run_time=self.dur(0.6))

            # «Marca lo mismo que A»
            self.en("igual")
            self.play(FadeIn(ficha, scale=0.5), run_time=0.25)
            self.play(ficha.animate.move_to([-3.0, 1.55, 0]), run_time=self.dur(0.6))
            self.play(FadeOut(ficha), run_time=0.2)

            # «un ruido propio de varianza tres»
            self.en("r3")
            self.play(Create(r3), GrowArrow(f3), FadeIn(v3), run_time=self.dur(0.7))

            # «su ruido tiene varianza cuatro»
            self.en("r4")
            self.play(FadeIn(v4, shift=UP * 0.1), run_time=self.dur(0.6))

            # «como el B de antes»
            self.en("antes")
            self.play(FadeIn(Bv), FadeIn(vbv), run_time=self.dur(0.6))

            # «al resolver»
            self.en("res")
            self.play(FadeIn(sis), run_time=self.dur(0.6))

            # «su peso sale cero»
            self.en("cero")
            self.play(FadeIn(h[0]), FadeIn(h[2]), run_time=0.3)
            self.pop(h[1], sonido="error")

            # «ya lo sabía A»
            self.en("sabia")
            self.resaltar(A.letra, color=AMBAR, escala=1.4)

            # «ruido añadido»
            self.en("anadido")
            self.resaltar(r3, color=AMBAR, escala=1.15)

            # «se queda en cero coma ocho»
            self.en("e08")
            self.play(FadeIn(e08, shift=UP * 0.1), run_time=self.dur(0.5))

            # «igual que con A solo»
            self.en("igual_a")
            self.play(FadeIn(como), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
