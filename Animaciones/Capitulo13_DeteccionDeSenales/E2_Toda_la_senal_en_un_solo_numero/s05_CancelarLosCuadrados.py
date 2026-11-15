"""Escena 05 — La derivación, paso a paso: sustituir, logaritmo, desarrollar el cuadrado y cancelar Σ r²."""
from comun.escena import *


def sub(m, color=AMBAR, ancho=5):
    """Subrayado de una pieza (una línea: no cuenta como encimado)."""
    return Underline(m, color=color, buff=0.08, stroke_width=ancho)


def tachar_linea(m, color=ERROR):
    return Line(m.get_corner(DL) + DL * 0.05, m.get_corner(UR) + UR * 0.05, color=color, stroke_width=6)


class CancelarLosCuadrados(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.sustituir()
        self.logaritmo()
        self.desarrollar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def sustituir(self):
        A = formula("p_1", r"f(\mathbf{r}\mid H_1)", r"\gtrless", "p_0", r"f(\mathbf{r}\mid H_0)", escala=1.3,
                    colores={0: AMBAR, 3: AMBAR}).move_to([0, 3.0, 0])
        B = formula("p_1", "c^3", r"\exp\!\Big(-\tfrac{1}{2\sigma^2}\sum(r-s)^2\Big)", r"\gtrless",
                    "p_0", "c^3", r"\exp\!\Big(-\tfrac{1}{2\sigma^2}\sum r^2\Big)", escala=1.15,
                    colores={0: AMBAR, 4: AMBAR}).move_to([0, 1.2, 0])
        C = formula("p_1", r"\exp\!\Big(-\tfrac{1}{2\sigma^2}\sum(r-s)^2\Big)", r"\gtrless",
                    "p_0", r"\exp\!\Big(-\tfrac{1}{2\sigma^2}\sum r^2\Big)", escala=1.3,
                    colores={0: AMBAR, 3: AMBAR}).move_to([0, -1.2, 0])
        self.A, self.B, self.C = A, B, C
        us = []

        with self.narrar("b1"):
            # «hay señal si»
            self.en("senal")
            self.play(*[FadeIn(A[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.0))

            # «la densidad de la hipótesis uno»
            self.en("d1")
            u = sub(A[1], SENAL)
            us.append(u)
            self.play(Create(u), run_time=self.dur(0.4))

            # «por su a priori»
            self.en("p1")
            u = sub(A[0])
            us.append(u)
            self.play(Create(u), run_time=self.dur(0.4))

            # «es mayor que»
            self.en("mayor")
            self.play(Indicate(A[2], color=AMBAR, scale_factor=1.4), run_time=self.dur(0.5))

            # «la de la hipótesis cero por la suya»
            self.en("d0")
            u1, u2 = sub(A[4], RUIDO), sub(A[3])
            us += [u1, u2]
            self.play(Create(u1), Create(u2), run_time=self.dur(0.5))

            # «Sustituimos las dos densidades»
            self.en("sustituye")
            self.play(*[FadeOut(u) for u in us], run_time=0.2)
            self.play(*[FadeIn(B[i], shift=DOWN * 0.15) for i in range(7)], run_time=self.dur(1.2))

            # «La constante es la misma a los dos lados»
            self.en("misma")
            u1, u2 = sub(B[1]), sub(B[5])
            self.play(Create(u1), Create(u2), run_time=self.dur(0.5))

            # «se cancela»
            self.en("cancela")
            t1, t2 = tachar_linea(B[1]), tachar_linea(B[5])
            self.play(Create(t1), Create(t2), run_time=self.dur(0.5))
            self.play(FadeOut(u1), FadeOut(u2), run_time=0.2)

            # «dos exponenciales comparadas»
            self.en("quedan")
            self.play(*[FadeIn(C[i], shift=DOWN * 0.15) for i in range(5)], run_time=self.dur(1.0))

            # «cada una por su a priori»
            self.en("priors")
            v1, v2 = sub(C[0]), sub(C[3])
            self.play(Create(v1), Create(v2), run_time=self.dur(0.5))
        self.wait(0.2)

    # ------------------------------------------------------------ b2
    def logaritmo(self):
        C = self.C
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame and m is not C], run_time=0.3)
        self.play(C.animate.scale(0.8).move_to([0, 3.3, 0]), run_time=0.4)
        D = formula(r"\ln", r"\Big(p_1\exp\!\Big(-\tfrac{1}{2\sigma^2}\sum(r-s)^2\Big)\Big)", r"\gtrless",
                    r"\ln", r"\Big(p_0\exp\!\Big(-\tfrac{1}{2\sigma^2}\sum r^2\Big)\Big)", escala=1.0,
                    colores={0: AMBAR, 3: AMBAR}).move_to([0, 1.9, 0])
        # la inversa: x → e^x → x
        izq = MathTex("x", color=TXT).scale(1.3).move_to([-5.4, 0.3, 0])
        med = MathTex("e^x", color=TXT).scale(1.3).move_to([-2.9, 0.3, 0])
        der = MathTex("x", color=TXT).scale(1.3).move_to([-0.4, 0.3, 0])
        a1 = Arrow([-4.9, 0.3, 0], [-3.5, 0.3, 0], buff=0.05, color=INK, stroke_width=4, max_tip_length_to_length_ratio=0.25)
        a2 = Arrow([-2.3, 0.3, 0], [-0.9, 0.3, 0], buff=0.05, color=AMBAR, stroke_width=4, max_tip_length_to_length_ratio=0.25)
        l1 = MathTex("e", color=INK).scale(0.8).next_to(a1, UP, buff=0.1)
        l2 = MathTex(r"\ln", color=AMBAR).scale(0.8).next_to(a2, UP, buff=0.1)
        regla = formula(r"\ln(e^x)", "=", "x", escala=1.4, colores={2: AMBAR}).move_to([3.7, 0.3, 0])
        # mayor que → su logaritmo también
        tres = MathTex(r"3<5", color=TXT).scale(1.3).move_to([-3.2, -1.1, 0])
        tres_ln = MathTex(r"\ln 3<\ln 5", color=AMBAR).scale(1.3).move_to([2.2, -1.1, 0])
        ok = tilde(VERDE, 0.6).move_to([5.7, -1.1, 0])
        E = formula(r"\ln p_1-\tfrac{1}{2\sigma^2}\sum", r"(r-s)^2", r"\gtrless", r"\ln p_0-\tfrac{1}{2\sigma^2}\sum",
                    r"r^2", escala=1.25, colores={2: AMBAR}).move_to([0, -2.6, 0])
        self.E = E

        with self.narrar("b2"):
            # «un truco»
            self.en("truco")
            self.play(FadeIn(D, shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «logaritmos naturales»
            self.en("ln")
            self.play(Indicate(D[0], color=AMBAR, scale_factor=1.5), Indicate(D[3], color=AMBAR, scale_factor=1.5),
                      run_time=self.dur(0.8))

            # «la operación inversa de la exponencial»
            self.en("inversa")
            self.play(FadeIn(izq), Create(a1), FadeIn(l1), FadeIn(med), run_time=self.dur(0.8))
            self.play(Create(a2), FadeIn(l2), FadeIn(der), run_time=self.dur(0.7))

            # «el logaritmo de e elevado a algo es ese algo»
            self.en("regla")
            self.play(*[FadeIn(regla[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(1.2))

            # «Y si un número»
            self.en("ysi")
            self.play(FadeOut(izq), FadeOut(a1), FadeOut(l1), FadeOut(med), FadeOut(a2), FadeOut(l2), FadeOut(der),
                      run_time=0.3)
            self.play(FadeIn(tres), run_time=self.dur(0.5))

            # «mayor que otro»
            self.en("mayor")
            self.play(Indicate(tres, color=AMBAR, scale_factor=1.1), run_time=self.dur(0.6))

            # «su logaritmo también lo es»
            self.en("tambien")
            self.play(FadeIn(tres_ln, shift=LEFT * 0.2), FadeIn(ok), run_time=self.dur(0.7))

            # «la comparación se conserva»
            self.en("conserva")
            u = sub(D[2], VERDE)
            self.play(Create(u), run_time=self.dur(0.5))

            # «Las exponenciales desaparecen»
            self.en("desaparecen")
            t1, t2 = tachar_linea(D[0]), tachar_linea(D[3])
            self.play(Create(t1), Create(t2), run_time=self.dur(0.5))

            # «una comparación de sumas»
            self.en("sumas")
            self.play(*[FadeIn(E[i], shift=DOWN * 0.15) for i in range(5)], run_time=self.dur(1.0))
        self.wait(0.2)

    # ------------------------------------------------------------ b3
    def desarrollar(self):
        E = self.E
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame and m is not E], run_time=0.3)
        F = formula(r"(r-s)^2", "=", r"r^2", r"-2rs", r"+s^2", escala=1.4,
                    colores={2: MEDIDA, 3: AMBAR, 4: SENAL}).move_to([0, 1.2, 0])
        G = formula(r"\ln p_1-\tfrac{1}{2\sigma^2}\sum\big(", r"r^2", r"-2rs+s^2", r"\big)", r"\gtrless",
                    r"\ln p_0-\tfrac{1}{2\sigma^2}\sum", r"r^2", escala=1.1,
                    colores={1: MEDIDA, 4: AMBAR, 6: MEDIDA}).move_to([0, -1.2, 0])

        with self.narrar("b3"):
            # «Desarrollemos el cuadrado»
            self.en("desarrolla")
            self.play(E.animate.scale(0.9).move_to([0, 3.0, 0]), run_time=self.dur(0.6))
            u = sub(E[1])
            self.play(Create(u), run_time=0.3)

            # «Recibido menos señal, al cuadrado»
            self.en("rmenos")
            self.play(FadeIn(F[0], shift=UP * 0.1), run_time=self.dur(0.6))
            self.play(FadeIn(F[1]), run_time=0.2)

            # «es recibido al cuadrado»
            self.en("r2")
            self.play(FadeIn(F[2], shift=UP * 0.1), run_time=self.dur(0.5))

            # «menos dos por recibido por señal»
            self.en("dosrs")
            self.play(FadeIn(F[3], shift=UP * 0.1), run_time=self.dur(0.6))

            # «más señal al cuadrado»
            self.en("s2")
            self.play(FadeIn(F[4], shift=UP * 0.1), run_time=self.dur(0.6))

            # «la suma de los cuadrados de lo recibido»
            self.en("sumar2")
            self.play(FadeOut(u), *[FadeIn(G[i], shift=UP * 0.1) for i in range(7)], run_time=self.dur(1.2))
            u1, u2 = sub(G[1], MEDIDA), sub(G[6], MEDIDA)
            self.play(Create(u1), Create(u2), run_time=self.dur(0.4))

            # «a los dos lados de la desigualdad»
            self.en("dos")
            self.play(Indicate(G[1], color=AMBAR), Indicate(G[6], color=AMBAR), run_time=self.dur(0.8))

            # «Aparece igual en las dos hipótesis»
            self.en("igual")
            self.play(u1.animate.set_color(VERDE), u2.animate.set_color(VERDE), run_time=self.dur(0.6))

            # «se cancela»
            self.en("cancela")
            t1, t2 = tachar_linea(G[1]), tachar_linea(G[6])
            self.play(Create(t1), Create(t2), run_time=self.dur(0.5))
        self.wait(0.2)
