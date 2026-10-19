"""Escena 04 — La regla del máximo a posteriori con el árbol del canal."""
from comun.escena import *
from comun.figuras_c9e1 import *


def nodo(txt, color, pos, escala=0.48):
    return casilla9(txt, color, ancho=2.5, alto=0.7, escala=escala).move_to([pos[0], pos[1], 0])


class MaximoAPosteriori(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.arbol()
        self.posteriori()
        self.cree()
        self.wait(1.0)
        self.limpiar()

    def arbol(self):
        with self.narrar("b1"):
            # «Recibes un uno»
            self.en("recibe")
            rec = VGroup(Text("Recibido", color=MEDIDA).scale(0.55), bit9(1, color=MEDIDA, lado=0.5))
            rec.arrange(RIGHT, buff=0.25).move_to([4.6, 3.3, 0])
            self.rec = rec
            self.play(FadeIn(rec), run_time=self.dur(0.4))

            # «dos caminos»
            self.en("arbol")
            raiz = nodo("Envío", INK, (-5.6, 0.2))
            n1 = nodo("Se envió 1", C1, (-2.3, 1.6))
            n0 = nodo("Se envió 0", C0, (-2.3, -1.2))
            h1 = nodo("Llega bien", VERDE, (1.1, 1.6))
            h0 = nodo("Se cambia", ERROR, (1.1, -1.2))
            l1 = Line(raiz.get_right(), n1.get_left(), color=INK, stroke_width=3)
            l0 = Line(raiz.get_right(), n0.get_left(), color=INK, stroke_width=3)
            l11 = Line(n1.get_right(), h1.get_left(), color=INK, stroke_width=3)
            l00 = Line(n0.get_right(), h0.get_left(), color=INK, stroke_width=3)
            e1 = MathTex(r"0{,}3", color=TXT).scale(0.6).move_to(l1.get_center() + UL * 0.3)
            e0 = MathTex(r"0{,}7", color=TXT).scale(0.6).move_to(l0.get_center() + DL * 0.3)
            e11 = MathTex(r"0{,}9", color=TXT).scale(0.6).move_to(l11.get_center() + UP * 0.3)
            e00 = MathTex(r"0{,}1", color=TXT).scale(0.6).move_to(l00.get_center() + UP * 0.3)
            self.play(FadeIn(raiz), Create(l1), Create(l0), FadeIn(n1), FadeIn(n0), FadeIn(e1), FadeIn(e0),
                      run_time=self.dur(0.6))
            self.play(Create(l11), Create(l00), FadeIn(h1), FadeIn(h0), FadeIn(e11), FadeIn(e00),
                      run_time=self.dur(0.5))
            self.arbol_g = VGroup(raiz, n1, n0, h1, h0, l1, l0, l11, l00, e1, e0, e11, e00)

            # «Se envió un uno y llegó bien»
            self.en("rama1")
            r1 = VGroup(l1.copy(), l11.copy()).set_stroke(C1, 7)
            self.play(Create(r1), run_time=self.dur(0.5))

            # «cero coma tres por»
            self.en("m1")
            f1 = formula(r"0{,}3 \cdot 0{,}9", r"= 0{,}27", colores={0: C1, 1: C1}).scale(0.85)
            f1.next_to(h1, RIGHT, buff=0.4)
            self.play(FadeIn(f1[0]), run_time=self.dur(0.4))

            # «cero coma veintisiete»
            self.en("c027")
            self.play(FadeIn(f1[1], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «el canal lo cambió»
            self.en("rama0")
            r0 = VGroup(l0.copy(), l00.copy()).set_stroke(C0, 7)
            self.play(Create(r0), run_time=self.dur(0.5))

            # «cero coma siete por»
            self.en("m0")
            f0 = formula(r"0{,}7 \cdot 0{,}1", r"= 0{,}07", colores={0: C0, 1: C0}).scale(0.85)
            f0.next_to(h0, RIGHT, buff=0.4)
            self.play(FadeIn(f0[0]), run_time=self.dur(0.4))

            # «cero coma cero siete»
            self.en("c007")
            self.play(FadeIn(f0[1], shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «la regla de Bayes»
            self.en("bayes")
            self.play(FadeOut(self.arbol_g), FadeOut(r1), FadeOut(r0),
                      f1.animate.move_to([-4.0, 1.9, 0]), f0.animate.move_to([-4.0, 1.0, 0]), run_time=self.dur(0.6))
            suma = MathTex(r"0{,}27 + 0{,}07 = 0{,}34", color=TXT).scale(0.85).move_to([-4.0, 0.1, 0])
            div = MathTex(r"P(H_1 \mid 1) = \frac{0{,}27}{0{,}34}", color=C1).scale(0.85).move_to([-4.0, -1.3, 0])
            self.play(FadeIn(suma), run_time=self.dur(0.4))
            self.play(FadeIn(div), run_time=self.dur(0.4))
            self.izq = VGroup(f1, f0, suma, div)

            # «cero coma setenta y nueve»
            self.en("p79")
            P = ParBarras9([0.79, 0.21], [C1, C0], ["H_1", "H_0"], "Recibido 1", centro=(3.0, 0.0))
            self.P = P
            self.play(Create(P.base), GrowFromEdge(P.barras[0], DOWN), FadeIn(P.rots[0]), FadeIn(P.titulo),
                      run_time=self.dur(0.6))
            self.play(FadeIn(P.valores[0]), run_time=self.dur(0.3))

            # «cero coma veintiuno»
            self.en("p21")
            self.play(GrowFromEdge(P.barras[1], DOWN), FadeIn(P.rots[1]), run_time=self.dur(0.5))
            self.play(FadeIn(P.valores[1]), run_time=self.dur(0.3))

    def posteriori(self):
        P = self.P
        with self.narrar("b2"):
            # «probabilidades a posteriori»
            self.en("apost")
            ap = Text("A posteriori", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([0, 2.5, 0])
            self.play(FadeOut(self.izq), P.animate.move_to([-2.6, -0.2, 0]), FadeIn(ap), run_time=self.dur(0.7))

            # «¿Con cuál»
            self.en("cual")
            preg = Text("?", color=ESTIMACION, weight=BOLD).scale(0.8).move_to(P.base.get_center() + UP * 2.2)
            self.pop(preg)

            # «Con la mayor»
            self.en("mayor")
            m1 = P.marco(0)
            self.play(Create(m1), FadeOut(preg), run_time=self.dur(0.4))

            # «dices uno»
            self.en("di1")
            d1 = Text("Decir 1", color=ESTIMACION, weight=BOLD).scale(0.55).next_to(P.titulo, DOWN, buff=0.3)
            self.pop(d1)

            # «si recibes un cero»
            self.en("rec0")
            Q = ParBarras9([0.045, 0.955], [C1, C0], ["H_1", "H_0"], "Recibido 0", centro=(2.6, -0.2))
            self.play(FadeIn(Q.base), FadeIn(Q.rots), FadeIn(Q.titulo), run_time=self.dur(0.4))

            # «cero coma noventa y cinco»
            self.en("p95")
            self.play(GrowFromEdge(Q.barras[0], DOWN), GrowFromEdge(Q.barras[1], DOWN), run_time=self.dur(0.6))
            self.play(FadeIn(Q.valores), run_time=self.dur(0.3))

            # «dices cero»
            self.en("di0")
            m0 = Q.marco(1)
            d0 = Text("Decir 0", color=ESTIMACION, weight=BOLD).scale(0.55).next_to(Q.titulo, DOWN, buff=0.3)
            self.play(Create(m0), run_time=self.dur(0.4))
            self.pop(d0)

            # «máximo a posteriori»
            self.en("map")
            tit =Text("Máximo a posteriori · MAP", color=ESTIMACION, weight=BOLD).scale(0.65).move_to([0, 2.5, 0])
            self.play(FadeOut(ap), run_time=self.dur(0.2))
            self.pop(tit)
            self.tit = tit

            # «la tercera forma»
            self.en("tres")
            self.play(FadeOut(VGroup(P, Q, m1, m0, d1, d0)), run_time=self.dur(0.4))
            cap = etiqueta("Capítulo 8", INK, 0.45).move_to([0, 1.25, 0])
            cs = VGroup(casilla9("Cuadrado → media", INK, ancho=3.8),
                        casilla9("Tamaño → mediana", INK, ancho=3.8),
                        casilla9("Acierto → moda", INK, ancho=3.8)).arrange(RIGHT, buff=0.35).move_to([0, 0.2, 0])
            self.play(FadeIn(cap), LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cs], lag_ratio=0.3),
                      run_time=self.dur(0.9))
            self.cs = cs

            # «la de acertar o fallar»
            self.en("acierto")
            self.play(cs[2].marco.animate.set_stroke(ESTIMACION, 5), run_time=self.dur(0.4))

            # «lo más probable»
            self.en("probable")
            prob = Text("Lo más probable", color=ESTIMACION).scale(0.5).next_to(cs[2], DOWN, buff=0.3)
            self.play(FadeIn(prob, shift=UP * 0.15), run_time=self.dur(0.4))

            # «la moda»
            self.en("moda")
            marco = SurroundingRectangle(cs[2], color=ESTIMACION, buff=0.1, stroke_width=5)
            fl = Arrow(cs[2].get_top(), tit.get_bottom() + RIGHT * 2.2, color=ESTIMACION, buff=0.1,
                       stroke_width=4, max_tip_length_to_length_ratio=0.2)
            self.play(Create(marco), GrowArrow(fl), run_time=self.dur(0.6))

    def cree(self):
        with self.narrar("b3"):
            # «algo muy simple»
            self.en("simple")
            self.corte()
            l1 = Text("Recibido 1 → Decir 1", color=TXT).scale(0.6).move_to([-2.6, 0.9, 0])
            l0 = Text("Recibido 0 → Decir 0", color=TXT).scale(0.6).move_to([-2.6, -0.1, 0])
            self.play(FadeIn(l1, shift=RIGHT * 0.2), FadeIn(l0, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «cree lo que recibes»
            self.en("cree")
            llave = Brace(VGroup(l1, l0), RIGHT, color=INK)
            frase = Text("Cree lo que recibes", color=ESTIMACION, weight=BOLD).scale(0.6).next_to(llave, RIGHT,
                                                                                                buff=0.25)
            self.play(GrowFromCenter(llave), FadeIn(frase), run_time=self.dur(0.5))

            # «Parece»
            self.en("obvio")
            ok = tilde(INK, 0.6).next_to(frase, DOWN, buff=0.45)
            self.play(Create(ok), run_time=self.dur(0.4))

            # «lo mejor que se puede hacer»
            self.en("lamejor")
            mej = Text("¿La mejor?", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(ok)
            self.play(ReplacementTransform(ok, mej), run_time=self.dur(0.4))

            # «¿Y será siempre así?»
            self.en("siempre")
            sie = Text("¿Siempre?", color=ESTIMACION, weight=BOLD).scale(0.6).next_to(mej, DOWN, buff=0.4)
            self.pop(sie)
            self.play(sie.animate(rate_func=there_and_back).scale(1.15), run_time=self.dur(0.6))
            self.play(sie.animate(rate_func=there_and_back).scale(1.15), run_time=self.dur(0.6))
