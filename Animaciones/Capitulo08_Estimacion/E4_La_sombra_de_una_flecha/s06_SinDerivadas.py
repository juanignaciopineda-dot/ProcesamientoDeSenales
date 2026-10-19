"""Escena 06 — h sin derivadas: 4 − 5h = 0; los tres caminos al 0,8; y la fórmula de la proyección."""
from comun.escena import *
from comun.figuras_c8e4 import *


class SinDerivadas(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.sin_derivar()
        self.tres_caminos()
        self.proyeccion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def sin_derivar(self):
        X = 0.8
        lab1 = Text("Condición 1", color=AMBAR).scale(0.55).move_to([-5.6, 2.9, 0])
        c1 = formula("E[e]", "=", "0", escala=1.2, colores={0: ERROR}).move_to([-2.4, 2.9, 0])
        ok = tilde(VERDE, 0.5).move_to([-0.6, 2.9, 0])
        bb = formula(r"\Rightarrow", "b", "=", "20-20h", escala=1.2).move_to([2.4, 2.9, 0])
        lab2 = Text("Condición 2", color=AMBAR).scale(0.55).move_to([-5.6, 1.6, 0])
        c2 = formula("E[", "e", r"\cdot", r"\tilde{x}", "]", "=", "0", escala=1.2,
                     colores={1: ERROR, 3: MEDIDA}).move_to([-1.9, 1.6, 0])
        e_f = formula("E[(", r"\tilde{y}", "-", "h", r"\tilde{x}", ")", r"\tilde{x}", "]", "=", "0", escala=1.25,
                      colores={1: SENAL, 3: ESTIMACION, 4: MEDIDA, 6: MEDIDA}).move_to([X, 0.2, 0])
        l_f = formula(r"E[\tilde{y}\,\tilde{x}]", "-", "h", r"E[\tilde{x}^2]", "=", "0", escala=1.25,
                      colores={2: ESTIMACION}).move_to([X, -1.1, 0])
        k_f = formula("4", "-", "5h", "=", "0", escala=1.4, colores={2: ESTIMACION}).move_to([X, -2.3, 0])
        h_f = formula("h", "=", num_tex(0.8), escala=1.6, colores={0: ESTIMACION, 2: VERDE}).move_to([X + 4.4, -2.3, 0])
        marco = SurroundingRectangle(h_f, color=VERDE, buff=0.18, stroke_width=3)

        with self.narrar("b1"):
            # «La primera condición»
            self.en("c1")
            self.play(FadeIn(lab1), *[FadeIn(c1[i]) for i in range(len(c1))], run_time=self.dur(0.6))

            # «fijaba be»
            self.en("fijaba")
            self.play(FadeIn(ok, scale=0.4), *[FadeIn(bb[i]) for i in range(len(bb))], run_time=self.dur(0.7))

            # «La segunda es nueva»
            self.en("c2")
            self.play(FadeIn(lab2), *[FadeIn(c2[i]) for i in range(len(c2))], run_time=self.dur(0.8))

            # «La media de la temperatura centrada»
            self.en("m1")
            self.play(FadeIn(e_f[0]), FadeIn(e_f[1]), run_time=self.dur(0.5))

            # «menos hache por la lectura centrada»
            self.en("m2")
            self.play(*[FadeIn(e_f[i]) for i in (2, 3, 4, 5)], run_time=self.dur(0.6))

            # «todo por la lectura centrada»
            self.en("m3")
            self.play(FadeIn(e_f[6]), FadeIn(e_f[7]), run_time=self.dur(0.5))

            # «tiene que ser cero»
            self.en("m4")
            self.play(FadeIn(e_f[8]), FadeIn(e_f[9]), run_time=self.dur(0.4))

            # «Por linealidad»
            self.en("lineal")
            self.play(*[FadeIn(l_f[i]) for i in range(len(l_f))], run_time=self.dur(0.8))

            # «cuatro menos cinco hache»
            self.en("cuatro")
            self.play(*[FadeIn(k_f[i]) for i in range(len(k_f))], run_time=self.dur(0.8))

            # «Hache vale cero coma ocho»
            self.en("h08")
            self.play(*[FadeIn(h_f[i]) for i in range(len(h_f))], Create(marco), run_time=self.dur(0.8))

    # ------------------------------------------------------------ b2
    def tres_caminos(self):
        xs = (-4.6, 0.0, 4.6)
        yc = 1.55
        tarjetas = VGroup(*[RoundedRectangle(corner_radius=0.15, width=4.1, height=3.5, color=INK, stroke_width=2.5)
                            .set_fill(INK, 0.08).move_to([x, yc, 0]) for x in xs])
        # 1 · el fondo de la parábola
        p1 = ParabolaJ(centro=(xs[0], 2.1), ancho=2.6, alto=1.5)
        # 2 · la pendiente cero
        p2 = ParabolaJ(centro=(xs[1], 2.1), ancho=2.6, alto=1.5)
        tg = p2.pendiente(0.8, largo=1.5, color=ROJO)
        # 3 · el ángulo recto
        o3 = np.array([xs[2] - 0.9, 1.6, 0.0])
        a_h = Line(o3, o3 + RIGHT * 1.8, color=MEDIDA, stroke_width=5)
        a_v = Line(o3 + RIGHT * 0.9, o3 + RIGHT * 0.9 + UP * 1.2, color=ERROR, stroke_width=5)
        a_c = VMobject(stroke_color=ERROR, stroke_width=3).set_fill(opacity=0)
        a_c.set_points_as_corners([o3 + [0.9 - 0.2, 0, 0], o3 + [0.9 - 0.2, 0.2, 0], o3 + [0.9, 0.2, 0]])
        nombres = ["Fondo de la parábola", "Pendiente = 0", "Ángulo recto"]
        textos = VGroup(*[Text(n, color=TXT).scale(0.5).move_to([x, 0.7, 0]) for n, x in zip(nombres, xs)])
        valores = VGroup(*[MathTex("h=" + num_tex(0.8), color=VERDE).scale(0.8).move_to([x, 0.15, 0]) for x in xs])
        jp = formula("J'(h)", escala=1.3).move_to([-4.9, -1.5, 0])
        medias = formula("=", "-2", "E[", escala=1.3).next_to(jp, RIGHT, buff=0.15)
        elerror = formula("e", r"\cdot", r"\tilde{x}", "]", escala=1.3, colores={0: ERROR, 2: MEDIDA}).next_to(medias, RIGHT, buff=0.1)
        cero = formula("=", "0", escala=1.3).next_to(elerror, RIGHT, buff=0.2)
        misma = formula("J'(h)=0", r"\iff", "e", r"\perp", "X", escala=1.4, colores={2: ERROR, 4: MEDIDA}).move_to([0, -3.0, 0])

        with self.narrar("b2"):
            # «Tres caminos»
            self.en("tres")
            self.corte()
            self.play(FadeIn(tarjetas), run_time=self.dur(0.5))

            # «el fondo de la parábola»
            self.en("fondo")
            self.play(Create(p1.eje), Create(p1.curva), FadeIn(p1.vertice), FadeIn(textos[0]), FadeIn(valores[0]),
                      run_time=self.dur(0.9))

            # «la pendiente igual a cero»
            self.en("pend")
            self.play(Create(p2.eje), Create(p2.curva), FadeIn(p2.vertice), Create(tg), FadeIn(textos[1]),
                      FadeIn(valores[1]), run_time=self.dur(0.9))

            # «el ángulo recto»
            self.en("angr")
            self.play(Create(a_h), Create(a_v), Create(a_c), FadeIn(textos[2]), FadeIn(valores[2]),
                      run_time=self.dur(0.9))

            # «No es casualidad»
            self.en("casual")
            self.resaltar(*tarjetas, color=AMBAR, escala=1.03)

            # «La pendiente de la parábola»
            self.en("jp")
            self.play(FadeIn(jp), run_time=self.dur(0.5))

            # «es menos dos por la media»
            self.en("medias")
            self.play(*[FadeIn(medias[i]) for i in range(len(medias))], run_time=self.dur(0.6))

            # «del error por la lectura»
            self.en("elerror")
            self.play(*[FadeIn(elerror[i]) for i in range(len(elerror))], run_time=self.dur(0.7))

            # «sea cero»
            self.en("cero")
            self.play(*[FadeIn(cero[i]) for i in range(len(cero))], run_time=self.dur(0.5))

            # «la misma condición»
            self.en("misma")
            self.play(*[FadeIn(misma[i]) for i in range(len(misma))], run_time=self.dur(0.9))

    # ------------------------------------------------------------ b3
    def proyeccion(self):
        def fraccion_tex(a, b, escala, colores=(TXT, TXT)):
            return fraccion(MathTex(a, color=colores[0]).scale(escala), MathTex(b, color=colores[1]).scale(escala))

        proy = MathTex(r"\mathrm{proy}_X\,Y", color=ESTIMACION).scale(1.4)
        igual = MathTex("=").scale(1.4)
        fr = fraccion_tex(r"\langle Y, X\rangle", r"\langle X, X\rangle", 1.3)
        punto = MathTex(r"\cdot").scale(1.4)
        X = MathTex("X", color=MEDIDA).scale(1.4)
        fila = VGroup(proy, igual, fr, punto, X).arrange(RIGHT, buff=0.35).move_to([0, 1.3, 0])
        n_cov = MathTex(r"\sigma_{YX}", color=AMBAR).scale(1.3).move_to(fr.num)
        d_var = MathTex(r"\sigma_X^2", color=AMBAR).scale(1.3).move_to(fr.den)
        marco = SurroundingRectangle(fr, color=AMBAR, buff=0.2, stroke_width=3)
        etq_h = MathTex("h", color=ESTIMACION).scale(1.4).next_to(marco, UP, buff=0.15)
        res = formula("h", "=", r"\frac{\sigma_{YX}}{\sigma_X^2}", "=", r"\frac{4}{5}", "=", num_tex(0.8), escala=1.5,
                      colores={0: ESTIMACION, 6: VERDE}).move_to([0, -2.2, 0])
        marco2 = SurroundingRectangle(res, color=AMBAR, buff=0.2, stroke_width=3)

        with self.narrar("b3"):
            # «La proyección de una flecha sobre otra»
            self.en("proy")
            self.corte()
            self.play(FadeIn(proy), FadeIn(igual), run_time=self.dur(0.7))

            # «el producto escalar de las dos»
            self.en("num")
            self.play(FadeIn(fr.num), run_time=self.dur(0.6))

            # «dividido entre el largo al cuadrado de la segunda»
            self.en("den")
            self.play(Create(fr.barra), FadeIn(fr.den), run_time=self.dur(0.8))

            # «por esa segunda flecha»
            self.en("porx")
            self.play(FadeIn(punto), FadeIn(X), run_time=self.dur(0.6))

            # «El producto escalar es la covarianza»
            self.en("cov")
            self.play(ReplacementTransform(fr.num, n_cov), run_time=self.dur(0.7))

            # «la varianza de equis»
            self.en("var")
            self.play(ReplacementTransform(fr.den, d_var), run_time=self.dur(0.7))

            # «El factor hache»
            self.en("fh")
            self.play(Create(marco), FadeIn(etq_h), run_time=self.dur(0.6))

            # «covarianza entre varianza»
            self.en("cv")
            self.play(*[FadeIn(res[i]) for i in range(len(res))], run_time=self.dur(1.0))

            # «leyendo el dibujo»
            self.en("dibujo")
            self.play(Create(marco2), run_time=self.dur(0.5))
