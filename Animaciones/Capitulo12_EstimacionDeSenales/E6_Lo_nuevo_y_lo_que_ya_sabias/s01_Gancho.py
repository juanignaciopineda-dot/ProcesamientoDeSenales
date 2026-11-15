"""Escena 01 — Gancho: cada muestra casi no trae nada nuevo; la de ahora vale más que todo el futuro."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        fila = FilaMuestras([r"x[n{-}3]", r"x[n{-}2]", r"x[n{-}1]", r"x[n]"], centro=(0, 3.0), lado=1.35, escala=0.6)
        ultima = VGroup(fila.cas[3], fila.rots[3])
        resto = VGroup(*fila.cas[:3], *fila.rots[:3])
        # la muestra grande: casi toda verde (lo que ya sabías) y una astilla roja (lo nuevo)
        contorno = Rectangle(width=6.0, height=1.5, color=MEDIDA, stroke_width=4).move_to([0, 0.6, 0])
        verde = Rectangle(width=5.6, height=1.5, stroke_width=0).set_fill(VERDE, 0.7).move_to([-0.2, 0.6, 0])
        roja = Rectangle(width=0.4, height=1.5, stroke_width=0).set_fill(ERROR, 0.9).move_to([2.8, 0.6, 0])
        rot_x = MathTex(r"x[n]", color=MEDIDA).scale(0.8).move_to([-4.3, 0.6, 0])
        tj = tijeras().scale(0.55).move_to([2.6, 1.9, 0])
        l_nuevo = Text("nuevo", color=ERROR, weight=BOLD).scale(0.7)
        l_sabias = Text("ya sabías", color=VERDE, weight=BOLD).scale(0.7)

        bal = Balanza(centro=(0, -0.7), semi=2.4)
        sq_i = Square(side_length=0.55, color=MEDIDA, stroke_width=3).set_fill(MEDIDA, 0.35).move_to([-2.4, -1.15, 0])
        sqs_d = VGroup(*[Square(side_length=0.3, color=INK, stroke_width=2).set_fill(INK, 0.3)
                         .move_to([2.4 + (i - 2.5) * 0.36, -1.28, 0]) for i in range(6)])
        l_ahora = Text("ahora", color=MEDIDA, weight=BOLD).scale(0.6).move_to([-2.4, 1.6, 0])
        l_futuro = Text("futuro", color=INK, weight=BOLD).scale(0.6).move_to([2.4, 1.6, 0])

        with self.narrar("b1"):
            # «Cada muestra que llega»
            self.en("llega")
            self.play(FadeIn(resto, lag_ratio=0.2), run_time=self.dur(0.6))
            self.play(FadeIn(ultima, shift=LEFT * 1.2), run_time=self.dur(0.5))

            # «casi no trae nada nuevo»
            self.en("nada")
            self.play(Create(contorno), FadeIn(rot_x), run_time=self.dur(0.4))
            self.play(FadeIn(verde), FadeIn(roja), run_time=self.dur(0.5))

            # «separar»
            self.en("separar")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.4))

            # «lo nuevo»
            self.en("nuevo")
            self.sfx("tick")
            l_nuevo.move_to([4.2, 1.7, 0])
            self.play(roja.animate.shift(UP * 1.1), FadeIn(l_nuevo), run_time=self.dur(0.5))

            # «lo que ya sabías»
            self.en("sabias")
            l_sabias.next_to(verde, DOWN, buff=1.0)
            self.play(FadeOut(tj), verde.animate.shift(DOWN * 0.9), FadeIn(l_sabias), run_time=self.dur(0.5))

            # «la muestra de ahora»
            self.en("ahora")
            self.corte()
            self.play(FadeIn(bal), FadeIn(sq_i), FadeIn(l_ahora), run_time=self.dur(0.7))

            # «vale más que todo el futuro»
            self.en("futuro")
            self.play(FadeIn(sqs_d), FadeIn(l_futuro), run_time=self.dur(0.4))
            dy = bal.semi * np.sin(0.22)
            self.sfx("impacto", gain=-18)
            self.play(*bal.inclinar("izq"), sq_i.animate.shift(DOWN * dy), sqs_d.animate.shift(UP * dy),
                      run_time=self.dur(0.8))

        self.wait(1.0)
        self.limpiar()
