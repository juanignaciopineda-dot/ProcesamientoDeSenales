"""Escena 07 — Cuando lo de antes pesa más que el dato: los unos rarísimos."""
from comun.escena import *
from comun.figuras_c9e1 import *


class UnosRarisimos(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.cuenta()
        self.siempre_cero()
        self.wait(1.0)
        self.limpiar()

    def cuenta(self):
        with self.narrar("b1"):
            # «Ahora una pregunta»
            self.en("pregunta")
            preg = Text("?", color=ESTIMACION, weight=BOLD).scale(2.6).move_to([0, 0.6, 0])
            self.pop(preg)

            # «piénsala antes de seguir»
            self.en("pausa")
            rel = reloj().scale(0.9).move_to([1.6, 0.6, 0])
            self.play(FadeIn(rel), run_time=self.dur(0.3))
            self.play(Rotate(rel.minutero, -2 * PI, about_point=rel.aro.get_center()), run_time=self.dur(2.4))

            # «los unos fueran»
            self.en("raros")
            unos = casilla9("Unos", C1, ancho=1.8, alto=0.7, escala=0.55).move_to([-1.0, 2.8, 0])
            self.play(FadeOut(preg), FadeOut(rel), FadeIn(unos), run_time=self.dur(0.4))
            self.play(unos.animate.scale(0.7), run_time=self.dur(0.5))

            # «uno de cada veinte»
            self.en("veinte")
            fila = fila_bits9(1, 20, centro=(0, 1.75), lado=0.42, hueco=0.1)
            p1 = MathTex(r"p_1 = 0{,}05", color=C1).scale(0.8).next_to(unos, RIGHT, buff=0.5)
            self.play(LaggedStart(*[FadeIn(b) for b in fila], lag_ratio=0.05), FadeIn(p1), run_time=self.dur(0.8))
            self.arriba = VGroup(unos, fila, p1)

            # «Recibes un uno»
            self.en("recibe")
            rec = VGroup(Text("Recibido", color=MEDIDA).scale(0.5), bit9(1, color=MEDIDA, lado=0.45))
            rec.arrange(RIGHT, buff=0.2).move_to([-4.6, 0.5, 0])
            self.rec = rec
            self.play(FadeIn(rec, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «¿Qué dices?»
            self.en("que")
            dz = casilla9("Decir 0", C0, ancho=2.0, alto=0.7).move_to([-1.0, 0.5, 0])
            du = casilla9("Decir 1", C1, ancho=2.0, alto=0.7).move_to([1.5, 0.5, 0])
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(0.8).move_to([3.6, 0.5, 0])
            self.botones = VGroup(dz, du)
            self.dz, self.q = dz, q
            self.play(FadeIn(dz), FadeIn(du), run_time=self.dur(0.4))
            self.pop(q)

            # «se envió un uno y llegó bien»
            self.en("rama1")
            c1 = rot_tex9(r"1 \to 1", "· Se envió 1 y llegó bien", C1, 0.48).move_to([-3.2, -1.2, 0])
            self.play(FadeIn(c1, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «cero coma cero cinco por»
            self.en("m1")
            f1 = formula(r"0{,}05 \cdot 0{,}9", r"= 0{,}045", colores={0: C1, 1: C1}).scale(0.85)
            f1.move_to([2.6, -1.2, 0])
            self.play(FadeIn(f1[0]), run_time=self.dur(0.4))

            # «cero coma cero cuarenta y cinco»
            self.en("c045")
            self.play(FadeIn(f1[1], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «Se envió un cero y se cambió»
            self.en("rama0")
            c0 = rot_tex9(r"0 \to 1", "· Se envió 0 y se cambió", C0, 0.48)
            c0.move_to([-3.2, -2.4, 0]).align_to(c1, LEFT)
            self.play(FadeIn(c0, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «cero coma noventa y cinco por»
            self.en("m0")
            f0 = formula(r"0{,}95 \cdot 0{,}1", r"= 0{,}095", colores={0: C0, 1: C0}).scale(0.85)
            f0.move_to([2.6, -2.4, 0])
            self.play(FadeIn(f0[0]), run_time=self.dur(0.4))

            # «cero coma cero noventa y cinco»
            self.en("c095")
            self.play(FadeIn(f0[1], shift=LEFT * 0.2), run_time=self.dur(0.4))
            self.abajo = VGroup(c1, c0, f1, f0)

    def siempre_cero(self):
        with self.narrar("b2"):
            # «un cero estropeado»
            self.en("gana0")
            ineq = MathTex(r"0{,}095 > 0{,}045", color=C0).scale(0.75).move_to([5.0, 0.5, 0])
            self.play(ReplacementTransform(self.q, ineq), self.dz.marco.animate.set_stroke(ESTIMACION, 6),
                      run_time=self.dur(0.5))

            # «decir siempre»
            self.en("siempre0")
            self.play(FadeOut(self.arriba), FadeOut(self.abajo), FadeOut(self.botones), FadeOut(ineq),
                      self.rec.animate.move_to([-3.2, 2.8, 0]), run_time=self.dur(0.5))
            card = casilla9("Siempre 0", C0, ancho=2.6, alto=0.8, escala=0.6).move_to([1.8, 2.8, 0])
            self.pop(card)

            # «sin mirar lo recibido»
            self.en("sinmirar")
            self.play(Create(tachar(self.rec)), run_time=self.dur(0.4))

            # «un cinco por ciento»
            self.en("e5")
            e5 = Text("Siempre 0 → 0,05", color=VERDE, weight=BOLD).scale(0.55).move_to([-3.2, 1.4, 0])
            self.pop(e5)

            # «fallaría un diez»
            self.en("e10")
            e10 = Text("Creer → 0,10", color=ERROR, weight=BOLD).scale(0.55).move_to([3.2, 1.4, 0])
            self.pop(e10)

            # «puede pesar más»
            self.en("balanza")
            B = balanza9(centro=(0, -0.9), semi=2.4)
            self.play(FadeIn(B), run_time=self.dur(0.4))
            self.play(*B.inclinar("izq"), run_time=self.dur(0.7))

            # «combinar las dos cosas»
            self.en("combinar")
            self.play(*B.inclinar("der"), run_time=self.dur(0.7))
            dec = Text("Decidir = combinar", color=ESTIMACION, weight=BOLD).scale(0.65).move_to([0, -3.4, 0])
            self.pop(dec)
