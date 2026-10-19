"""Escena 04 — Probabilidades de falsa alarma, fallo y detección; la probabilidad de error total."""
from comun.escena import *
from comun.figuras_c9e2 import *


class ProbabilidadDeError(EscenaCurso):
    ESCENA = "04"

    X0, X1 = -1.0, 5.5          # extremos de las barras de cada fila
    Y0, Y1 = 2.5, 0.2           # altura de la barra «Sin avión» y de la barra «Con avión»

    def construct(self):
        self.condicionadas()
        self.deteccion()
        self.arbol()
        self.canal()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def condicionadas(self):
        T = Tabla22_9(("Solo ruido", "Hay avión"), ("Nada", "Avión"), centro=(-3.9, 0.3), ancho=1.1, alto=1.1,
                      escala=0.36)
        marcas = VGroup(*[T.marca(i, j, tam=0.24) for i in range(2) for j in range(2)])
        aviso = aviso_triangulo().scale(0.9).move_to([-3.9, 2.7, 0])
        X0, X1, Y0, Y1 = self.X0, self.X1, self.Y0, self.Y1
        xc = X1 - 0.25 * (X1 - X0)          # corte: el trozo rojo de la fila «Sin avión» es un 25 %
        b0 = barra9(X0, X1, Y0, color=C0)
        b0_azul = barra9(X0, xc, Y0, color=C0)
        b0_rojo = barra9(xc, X1, Y0, color=ERROR, opacidad=0.6)
        rot0 = Text("Sin avión", color=C0).scale(0.42).move_to([X0, Y0 + 0.55, 0], aligned_edge=LEFT)
        f_fa = MathTex("P_{FA}", "=", r"P(\text{Decir } 1", r"\mid", "H_0", ")", color=TXT).scale(0.85)
        f_fa.move_to([(X0 + X1) / 2, Y0 - 0.95, 0])
        f_fa[0].set_color(ERROR)
        f_fa[4].set_color(C0)
        et_fa = MathTex("P_{FA}", color=TXT).scale(0.7).move_to(b0_rojo)
        xm = X0 + 0.3 * (X1 - X0)           # corte: el trozo rojo de la fila «Con avión» es un 30 %
        b1 = barra9(X0, X1, Y1, color=C1)
        b1_rojo = barra9(X0, xm, Y1, color=ERROR, opacidad=0.6)
        b1_resto = barra9(xm, X1, Y1, color=C1)
        rot1 = Text("Con avión", color=C1).scale(0.42).move_to([X0, Y1 + 0.55, 0], aligned_edge=LEFT)
        f_m = MathTex("P_M", "=", r"P(\text{Decir } 0", r"\mid", "H_1", ")", color=TXT).scale(0.85)
        f_m.move_to([(X0 + X1) / 2, Y1 - 0.95, 0])
        f_m[0].set_color(ERROR)
        f_m[4].set_color(C1)
        et_m = MathTex("P_M", color=TXT).scale(0.7).move_to(b1_rojo)
        self.piezas = dict(T=T, marcas=marcas, aviso=aviso, b0=b0, b0_azul=b0_azul, b0_rojo=b0_rojo, rot0=rot0,
                           f_fa=f_fa, et_fa=et_fa, b1=b1, b1_rojo=b1_rojo, b1_resto=b1_resto, rot1=rot1,
                           f_m=f_m, et_m=et_m)

        with self.narrar("b1"):
            # «Cada error tiene su probabilidad»
            self.en("probs")
            self.play(FadeIn(T), FadeIn(marcas), run_time=self.dur(0.6))

            # «cuidado con cómo se definen»
            self.en("cuidado")
            self.pop(aviso)

            # «probabilidad de falsa alarma»
            self.en("pfa")
            self.pop(f_fa[0])

            # «de todas las veces que no había avión»
            self.en("fila0")
            self.play(T.rot_f[0].animate(rate_func=there_and_back).scale(1.25), FadeIn(rot0),
                      GrowFromEdge(b0, LEFT), run_time=self.dur(0.7))

            # «la fracción en que el radar dice que sí»
            self.en("trozo_fa")
            self.play(FadeOut(b0), FadeIn(b0_azul), FadeIn(b0_rojo), run_time=self.dur(0.4))
            self.play(FadeIn(et_fa, scale=0.6), run_time=self.dur(0.3))

            # «condicionada a hache cero»
            self.en("cond0")
            self.play(Write(f_fa[1:]), run_time=self.dur(0.8))
            self.resaltar(f_fa[4], color=C0)

            # «La probabilidad de fallo»
            self.en("pm")
            self.pop(f_m[0])

            # «de las veces que sí había avión»
            self.en("fila1")
            self.play(T.rot_f[1].animate(rate_func=there_and_back).scale(1.25), FadeIn(rot1),
                      GrowFromEdge(b1, LEFT), run_time=self.dur(0.7))

            # «la fracción que se le escapa»
            self.en("trozo_m")
            self.play(FadeOut(b1), FadeIn(b1_rojo), FadeIn(b1_resto), run_time=self.dur(0.4))
            self.play(FadeIn(et_m, scale=0.6), run_time=self.dur(0.3))

            # «condicionada a hache uno»
            self.en("cond1")
            self.play(Write(f_m[1:]), run_time=self.dur(0.8))
            self.resaltar(f_m[4], color=C1)

    # ------------------------------------------------------------ b2
    def deteccion(self):
        P = self.piezas
        xm = self.X0 + 0.3 * (self.X1 - self.X0)
        b1_verde = barra9(xm, self.X1, self.Y1, color=VERDE, opacidad=0.5)
        et_d = MathTex("P_D", color=TXT).scale(0.7).move_to(b1_verde)
        f_d = MathTex("P_D", "=", "1", "-", "P_M", color=TXT).scale(0.95).move_to([(self.X0 + self.X1) / 2, -1.95, 0])
        f_d[0].set_color(VERDE)
        f_d[4].set_color(ERROR)
        uno = MathTex("= 1", color=ESTIMACION).scale(0.85).next_to(P["b1"], RIGHT, buff=0.25)

        with self.narrar("b2"):
            # «Hay una tercera»
            self.en("tercera")
            self.play(P["f_fa"].animate.fade(0.4), P["f_m"].animate.fade(0.4), run_time=self.dur(0.4))

            # «la probabilidad de detección»
            self.en("pd")
            self.pop(f_d[0])

            # «De las veces que había avión»
            self.en("fila1d")
            self.resaltar(P["b1_resto"], P["b1_rojo"], color=C1, escala=1.05)

            # «la fracción que el radar ve»
            self.en("trozo_d")
            self.play(FadeOut(P["b1_resto"]), FadeIn(b1_verde), FadeIn(et_d, scale=0.6), run_time=self.dur(0.5))

            # «Es uno menos la probabilidad de fallo»
            self.en("formula")
            self.play(Write(f_d[1:]), run_time=self.dur(0.9))

            # «o se ve o se escapa»
            self.en("suma")
            self.resaltar(P["b1_rojo"], b1_verde, color=ESTIMACION, escala=1.04)
            self.pop(uno)

    # ------------------------------------------------------------ b3
    def arbol(self):
        pe = MathTex("P_e", "=", "?", color=ERROR).scale(1.0).move_to([0, 3.3, 0])
        raiz = Dot([-5.6, 0.6, 0], radius=0.12, color=TXT)
        n0 = casilla9("Solo ruido", C0, ancho=2.6, alto=0.7, escala=0.45).move_to([-2.0, 1.8, 0])
        n1 = casilla9("Hay avión", C1, ancho=2.6, alto=0.7, escala=0.45).move_to([-2.0, -0.6, 0])
        h0 = casilla9("Falsa alarma", ERROR, ancho=2.8, alto=0.7, escala=0.45).move_to([3.0, 1.8, 0])
        h1 = casilla9("Fallo", ERROR, ancho=2.8, alto=0.7, escala=0.45).move_to([3.0, -0.6, 0])
        l0 = Line(raiz.get_center(), n0.get_left(), color=INK, stroke_width=3)
        l1 = Line(raiz.get_center(), n1.get_left(), color=INK, stroke_width=3)
        l2 = Line(n0.get_right(), h0.get_left(), color=INK, stroke_width=3)
        l3 = Line(n1.get_right(), h1.get_left(), color=INK, stroke_width=3)
        e0 = MathTex("p_0", color=C0).scale(0.8).next_to(l0.get_center(), UL, buff=0.08)
        e1 = MathTex("p_1", color=C1).scale(0.8).next_to(l1.get_center(), DL, buff=0.08)
        e2 = MathTex("P_{FA}", color=ERROR).scale(0.8).next_to(l2, UP, buff=0.12)
        e3 = MathTex("P_M", color=ERROR).scale(0.8).next_to(l3, UP, buff=0.12)
        f = MathTex("P_e", "=", "p_0", r"\cdot", "P_{FA}", "+", "p_1", r"\cdot", "P_M", color=TXT).scale(1.05)
        f.move_to([0, -2.4, 0])
        f[0].set_color(ERROR)
        f[2].set_color(C0)
        f[4].set_color(ERROR)
        f[6].set_color(C1)
        f[8].set_color(ERROR)
        marco = SurroundingRectangle(f, color=ESTIMACION, buff=0.18, stroke_width=4)
        self.arbol_g = VGroup(raiz, n0, n1, h0, h1, l0, l1, l2, l3, e0, e1, e2, e3)
        self.f, self.marco, self.pe = f, marco, pe

        with self.narrar("b3"):
            # «¿Y la probabilidad de equivocarse»
            self.en("pe")
            self.corte()
            self.pop(pe)

            # «dos caminos para fallar»
            self.en("arbol")
            self.play(FadeIn(raiz, scale=0.5), run_time=0.25)
            self.play(Create(l0), Create(l1), run_time=self.dur(0.5))

            # «con probabilidad pe cero»
            self.en("rama0")
            self.play(FadeIn(n0, shift=RIGHT * 0.2), FadeIn(e0), l0.animate.set_stroke(C0, 5), run_time=self.dur(0.5))

            # «y hubo falsa alarma»
            self.en("hoja0")
            self.play(Create(l2), FadeIn(h0, shift=RIGHT * 0.2), FadeIn(e2), run_time=self.dur(0.6))

            # «con probabilidad pe uno»
            self.en("rama1")
            self.play(FadeIn(n1, shift=RIGHT * 0.2), FadeIn(e1), l1.animate.set_stroke(C1, 5), run_time=self.dur(0.5))

            # «y hubo fallo»
            self.en("hoja1")
            self.play(Create(l3), FadeIn(h1, shift=RIGHT * 0.2), FadeIn(e3), run_time=self.dur(0.6))

            # «La probabilidad de error es pe cero por la de falsa alarma»
            self.en("term0")
            self.play(Write(f[0:5]), run_time=self.dur(0.9))

            # «más pe uno por la de fallo»
            self.en("term1")
            self.play(Write(f[5:]), run_time=self.dur(0.8))
            self.play(Create(marco), FadeOut(pe), run_time=self.dur(0.4))

    # ------------------------------------------------------------ b4
    def canal(self):
        f, marco = self.f, self.marco
        canal = canal9(centro=(5.3, 2.3), ancho=3.0, escala=0.6)
        creer = Text("Creer lo recibido", color=TXT).scale(0.5).move_to([-6.4, 1.3, 0], aligned_edge=LEFT)
        fa01 = MathTex("P_{FA}", "=", "0{,}1", color=TXT).scale(0.8).move_to([-2.2, 1.3, 0])
        m01 = MathTex("P_M", "=", "0{,}1", color=TXT).scale(0.8).move_to([0.2, 1.3, 0])
        fa01[0].set_color(ERROR)
        m01[0].set_color(ERROR)
        c1 = MathTex(r"0{,}7 \cdot 0{,}1", color=TXT).scale(0.85).move_to([-5.2, 0.4, 0])
        c2 = MathTex(r"+\ 0{,}3 \cdot 0{,}1", color=TXT).scale(0.85).move_to([-3.0, 0.4, 0])
        diez = MathTex(r"=\ 0{,}10", color=VERDE).scale(0.85).move_to([-1.0, 0.4, 0])
        siempre = Text("Siempre 0", color=TXT).scale(0.5).move_to([-6.4, -1.0, 0], aligned_edge=LEFT)
        fa0 = MathTex(r"0{,}7 \cdot 0", color=TXT).scale(0.85).move_to([-5.2, -1.9, 0])
        m1 = MathTex(r"+\ 0{,}3 \cdot 1", color=TXT).scale(0.85).move_to([-3.0, -1.9, 0])
        treinta = MathTex(r"=\ 0{,}30", color=ERROR).scale(0.85).move_to([-1.0, -1.9, 0])
        R = TablaReglas9()
        tabla = VGroup(R, *[R.fila(i) for i in range(4)]).scale(0.6).move_to([4.0, -1.0, 0])
        ok0 = SurroundingRectangle(R.errores[0], color=VERDE, buff=0.06, stroke_width=4)
        ok1 = SurroundingRectangle(R.errores[1], color=VERDE, buff=0.06, stroke_width=4)

        with self.narrar("b4"):
            # «Comprobémoslo con el canal»
            self.en("canal")
            self.play(FadeOut(self.arbol_g), FadeOut(marco), f.animate.scale(0.8).move_to([-1.6, 2.9, 0]),
                      FadeIn(canal), run_time=self.dur(0.7))

            # «Creyendo lo recibido»
            self.en("creer")
            self.play(FadeIn(creer, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «la falsa alarma vale cero coma uno»
            self.en("fa01")
            self.play(Write(fa01), run_time=self.dur(0.5))

            # «el fallo también»
            self.en("m01")
            self.play(Write(m01), run_time=self.dur(0.5))

            # «Cero coma siete por cero coma uno»
            self.en("c1")
            self.play(Write(c1), run_time=self.dur(0.5))

            # «más cero coma tres por cero coma uno»
            self.en("c2")
            self.play(Write(c2), run_time=self.dur(0.5))

            # «un diez por ciento»
            self.en("diez")
            self.pop(diez)

            # «diciendo siempre cero»
            self.en("siempre")
            self.play(FadeIn(siempre, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «no hay falsas alarmas»
            self.en("fa0")
            self.play(Write(fa0), run_time=self.dur(0.5))

            # «se fallan todos los unos»
            self.en("m1")
            self.play(Write(m1), run_time=self.dur(0.5))

            # «un treinta por ciento»
            self.en("treinta")
            self.pop(treinta)

            # «Lo mismo que antes»
            self.en("antes")
            self.play(FadeIn(tabla, shift=LEFT * 0.3), run_time=self.dur(0.5))
            self.play(Create(ok0), Create(ok1), run_time=self.dur(0.4))
            self.sfx("exito", gain=-20)
