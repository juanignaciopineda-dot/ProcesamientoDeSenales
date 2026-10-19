"""Escena 03 — Separar lo medido de lo que se sabía antes: la razón de verosimilitud."""
from comun.escena import *
from comun.figuras_c9e3 import *

R = 1.3
FR1 = r"f(r \mid H_1)"
FR0 = r"f(r \mid H_0)"
FRAC = r"\frac{f(r \mid H_1)}{f(r \mid H_0)}"
Y_F = 1.9


class SepararLoMedido(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.reordenar()
        self.razon()
        self.umbral()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def reordenar(self):
        with self.narrar("b1"):
            # «la regla del máximo a posteriori»
            self.en("regla")
            F = formula("p_1", r"\cdot", FR1, ">", "p_0", r"\cdot", FR0, escala=1.1).move_to([0, Y_F, 0])
            mapa = Text("Máximo a posteriori (MAP)", color=INK).scale(0.45).move_to([0, 3.35, 0])
            self.play(Write(F), FadeIn(mapa), run_time=self.dur(1.0))

            # «cada lado mezcla dos cosas»
            self.en("lados")
            r_izq = SurroundingRectangle(F[0:3], color=INK, buff=0.15)
            r_der = SurroundingRectangle(F[4:7], color=INK, buff=0.15)
            # marcan piezas de una misma fórmula: tocarla es a propósito
            r_izq.permitir_encima = r_der.permitir_encima = True
            self.play(Create(r_izq), Create(r_der), run_time=self.dur(0.5))

            # «lo que has medido»
            self.en("medido")
            self.play(F[2].animate.set_color(MEDIDA), F[6].animate.set_color(MEDIDA), run_time=self.dur(0.4))

            # «lo que sabías antes»
            self.en("antes")
            self.play(F[0].animate.set_color(ESTIMACION), F[4].animate.set_color(ESTIMACION),
                      run_time=self.dur(0.4))

            # «Vamos a separarlas»
            self.en("separar")
            self.play(FadeOut(r_izq), FadeOut(r_der), F[0:3].animate.shift(LEFT * 0.25),
                      F[4:7].animate.shift(RIGHT * 0.25), run_time=self.dur(0.5))

            # «Para decir uno»
            self.en("decir1")
            d1 = Text("Decir 1", color=ESTIMACION, weight=BOLD).scale(0.5).next_to(F[3], UP, buff=0.35)
            self.pop(d1)

            # «tiene que superar»
            self.en("superar")
            self.play(Indicate(F[3], color=ESTIMACION, scale_factor=1.6), run_time=self.dur(0.6))

            # «Dividimos los dos lados»
            self.en("dividir")
            M1 = formula("p_1", r"\cdot", FRAC, ">", "p_0", escala=1.1,
                         colores={0: ESTIMACION, 2: MEDIDA, 4: ESTIMACION}).move_to([0, Y_F, 0])
            self.play(ReplacementTransform(F[0], M1[0]), ReplacementTransform(F[1], M1[1]),
                      ReplacementTransform(VGroup(F[2], F[6]), M1[2]), ReplacementTransform(F[3], M1[3]),
                      ReplacementTransform(F[4], M1[4]), FadeOut(F[5]),
                      d1.animate.move_to([M1[3].get_center()[0], Y_F + 0.95, 0]), run_time=self.dur(0.9))

            # «y entre pe uno»
            self.en("pe1")
            M2 = formula(FRAC, ">", r"\frac{p_0}{p_1}", escala=1.1,
                         colores={0: MEDIDA, 2: ESTIMACION}).move_to([0, Y_F, 0])
            self.play(ReplacementTransform(M1[2], M2[0]), ReplacementTransform(M1[3], M2[1]),
                      ReplacementTransform(VGroup(M1[4], M1[0]), M2[2]), FadeOut(M1[1]),
                      d1.animate.move_to([M2[1].get_center()[0], Y_F + 0.95, 0]), run_time=self.dur(0.9))

            # «Son números positivos»
            self.en("positivos")
            nota_ = etiqueta("Dividir entre algo positivo: la desigualdad no gira", INK, 0.45).move_to([0, 0.55, 0])
            self.play(FadeIn(nota_, shift=UP * 0.15), run_time=self.dur(0.5))

            # «no se da la vuelta»
            self.en("nogira")
            self.play(Indicate(M2[1], color=VERDE, scale_factor=1.6), run_time=self.dur(0.6))
        self.M2, self.d1, self.mapa, self.nota_ = M2, d1, mapa, nota_

    # ------------------------------------------------------------------ b2
    def razon(self):
        M2 = self.M2
        C = Campanas9(centro=(3.4, -3.15), ancho=6.2, alto=3.0, r_rango=(-2.2, 4.2), v_max=0.45)
        self.C = C
        with self.narrar("b2"):
            # «A la izquierda queda»
            self.en("izq")
            rect = SurroundingRectangle(M2[0], color=MEDIDA, buff=0.12)
            rect.permitir_encima = True
            self.play(FadeOut(self.nota_), FadeOut(self.mapa), Create(rect), run_time=self.dur(0.5))

            # «la altura de la campana del uno»
            self.en("alto1")
            eje = C.eje((0, 1, 2), rotulo=False, escala=0.4)
            c0, c1 = C.campana(0, 1, C0, 3), C.campana(2, 1, C1, 3)
            regla = C.regla(R, alto=1.6, ancho=3)
            s1 = C.segmento(2, R, 1, C1, 6).shift(RIGHT * 0.05)
            self.play(FadeOut(rect), FadeIn(eje), Create(c0), Create(c1), Create(regla), run_time=self.dur(0.8))
            self.play(Create(s1), run_time=self.dur(0.4))

            # «la altura de la campana del cero»
            self.en("alto0")
            s0 = C.segmento(0, R, 1, C0, 6).shift(LEFT * 0.05)
            self.play(Create(s0), run_time=self.dur(0.4))

            # «en el punto medido»
            self.en("punto")
            rt = MathTex("r", color=MEDIDA).scale(0.6).next_to(regla, UP, buff=0.08)
            self.play(FadeIn(rt), Indicate(regla, color=MEDIDA, scale_factor=1.05), run_time=self.dur(0.6))

            # «la razón de verosimilitud»
            self.en("razon")
            lam = formula(LAMBDA, "=", escala=1.1, colores={0: MEDIDA}).next_to(M2, LEFT, buff=0.2)
            grupo = VGroup(lam, M2)
            dx = -grupo.get_center()[0]
            rot = Text("Razón de verosimilitud", color=MEDIDA, weight=BOLD).scale(0.45)
            rot.move_to([lam.get_center()[0] + dx, 3.25, 0])
            self.play(M2.animate.shift(RIGHT * dx), self.d1.animate.shift(RIGHT * dx), run_time=self.dur(0.4))
            lam.shift(RIGHT * dx)
            self.play(Write(lam), FadeIn(rot), run_time=self.dur(0.6))

            # «lambda mayúscula de erre»
            self.en("lambda")
            self.play(lam[0].animate(rate_func=there_and_back).scale(1.35), run_time=self.dur(0.6))

            # «cuántas veces más compatible»
            self.en("veces")
            v1 = etiqueta("¿Cuántas veces más compatible", TXT, 0.45).move_to([-3.9, -1.2, 0])
            self.play(FadeIn(v1, shift=UP * 0.15), run_time=self.dur(0.5))

            # «con hache uno que con hache cero»
            self.en("h1h0")
            v2 = rot_tex9("H_1", "frente a", C1, 0.45)
            v2.add(MathTex("H_0", color=C0).scale(0.6).next_to(v2, RIGHT, buff=0.14))
            v2.add(Text("?", color=TXT).scale(0.45).next_to(v2, RIGHT, buff=0.06))
            v2.next_to(v1, DOWN, buff=0.25)
            self.play(FadeIn(v2, shift=UP * 0.15), run_time=self.dur(0.5))
        self.lam, self.rot = lam, rot
        self.regla, self.rt, self.segs = regla, rt, VGroup(s0, s1)

    # ------------------------------------------------------------------ b3
    def umbral(self):
        M2, C = self.M2, self.C
        with self.narrar("b3"):
            # «A la derecha queda un número fijo»
            self.en("der")
            rect = SurroundingRectangle(M2[2], color=ESTIMACION, buff=0.12)
            rect.permitir_encima = True
            self.play(Create(rect), run_time=self.dur(0.4))

            # «no depende de la medición»
            self.en("nodep")
            mover = VGroup(self.regla, self.rt)
            self.play(FadeOut(self.segs), run_time=self.dur(0.2))
            self.play(mover.animate.shift(LEFT * float(C.L.x(1.3) - C.L.x(0.2))), run_time=self.dur(0.7),
                      rate_func=there_and_back)

            # «pe cero entre pe uno»
            self.en("p0p1")
            self.play(FadeOut(rect), Indicate(M2[2], color=ESTIMACION, scale_factor=1.25), run_time=self.dur(0.6))

            # «se llama eta»
            self.en("eta")
            eta = formula("=", r"\eta", escala=1.1, colores={1: ESTIMACION}).next_to(M2, RIGHT, buff=0.2)
            gl = MathTex(r"\gtrless", color=TXT).scale(1.1).move_to(M2[1])
            self.play(Write(eta), FadeOut(self.d1), ReplacementTransform(M2[1], gl), run_time=self.dur(0.7))

            # «Todo lo que has medido»
            self.en("llave_izq")
            b_izq = Brace(VGroup(self.lam, M2[0]), DOWN, buff=0.15, color=MEDIDA)
            t_izq = Text("Lo que has medido", color=MEDIDA, weight=BOLD).scale(0.45).next_to(b_izq, DOWN, buff=0.12)
            self.play(GrowFromCenter(b_izq), FadeIn(t_izq), run_time=self.dur(0.6))

            # «Todo lo que sabías antes»
            self.en("llave_der")
            b_der = Brace(VGroup(M2[2], eta), DOWN, buff=0.15, color=ESTIMACION)
            t_der = Text("Lo que sabías antes", color=ESTIMACION, weight=BOLD).scale(0.45)
            t_der.next_to(b_der, DOWN, buff=0.12)
            self.play(GrowFromCenter(b_der), FadeIn(t_der), run_time=self.dur(0.6))
