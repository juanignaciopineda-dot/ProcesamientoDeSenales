"""Escena 07 — Las ecuaciones normales: C_xx h = c_xy, la inversa, el determinante 24 y el error."""
from comun.escena import *
from comun.figuras_c8e5 import *

MC = (-2.4, -0.4)          # la cuenta de la matriz, un poco más arriba y a la izquierda que en la escena 06


class EcuacionesNormales(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.en_una_linea()
        self.resolver()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def en_una_linea(self):
        ea = formula(r"5h_A+4h_B", "=", "4", escala=0.95).move_to([-3.6, 3.15, 0])
        eb = formula(r"4h_A+8h_B", "=", "4", escala=0.95).move_to([-3.6, 2.35, 0])
        M = Matriz8([["5", "4"], ["4", "8"]], centro=MC, dx=1.3, dy=1.1, escala=1.25)
        H = Matriz8([["h_A"], ["h_B"]], centro=(MC[0] + 2.3, MC[1]), dx=1.0, dy=1.1, escala=1.2, color=ESTIMACION)
        igual = MathTex("=", color=TXT).scale(1.2).move_to([MC[0] + 3.35, MC[1], 0])
        C = Matriz8([["4"], ["4"]], centro=(MC[0] + 4.3, MC[1]), dx=0.9, dy=1.1, escala=1.2, color=SENAL)
        ncy = MathTex(r"\mathrm{cov}(x,y)", color=INK).scale(0.8).next_to(C, DOWN, buff=0.25)
        dim = MathTex(r"2\times 2", color=INK).scale(0.85).next_to(M, DOWN, buff=0.25)
        dim_n = MathTex(r"n\times n", color=INK).scale(0.85).move_to(dim)
        caja_ = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.1, color=AMBAR, stroke_width=3)
        caja_.move_to([MC[0] + 1.8, -3.15, 0])
        lin = formula(r"C_{xx}", r"\,\mathbf{h}", "=", r"\mathbf{c}_{xy}", escala=1.3,
                      colores={1: ESTIMACION, 3: SENAL}).move_to(caja_)
        nombre = Text("Ecuaciones normales", color=AMBAR, weight=BOLD).scale(0.85).move_to([-2.0, 2.75, 0])
        o = np.array([4.6, 2.0, 0.0])
        geo_l = Line(o + LEFT * 1.4, o + RIGHT * 1.4, color=INK, stroke_width=4)
        geo_n = Line(o, o + UP * 1.1, color=AMBAR, stroke_width=5)
        s = 0.22
        geo_r = VMobject(stroke_color=AMBAR, stroke_width=3).set_fill(opacity=0)
        geo_r.set_points_as_corners([o + RIGHT * s, o + RIGHT * s + UP * s, o + UP * s])
        perp = Text("Normal = perpendicular", color=TXT).scale(0.5).move_to([4.6, 1.3, 0])

        with self.narrar("b1"):
            # «los lados derechos»
            self.en("der")
            self.play(FadeIn(ea), FadeIn(eb), FadeIn(M), FadeIn(H), run_time=self.dur(0.4))
            self.resaltar(ea[2], eb[2], color=AMBAR, escala=1.4, run_time=0.5)

            # «forman otra columna»
            self.en("col2")
            self.play(FadeIn(igual), TransformFromCopy(VGroup(ea[2], eb[2]), C.todas()), Create(C.corchetes),
                      run_time=self.dur(0.8))

            # «con la temperatura»
            self.en("cy")
            self.play(FadeIn(ncy, shift=UP * 0.1), run_time=self.dur(0.5))

            # «Así que las dos ecuaciones»
            self.en("dos")
            marco = SurroundingRectangle(VGroup(M, H, igual, C), color=AMBAR, buff=0.2)
            self.play(Create(marco), run_time=self.dur(0.6))

            # «cualquier número de mediciones»
            self.en("cualquier")
            self.play(FadeOut(marco), FadeIn(dim), run_time=self.dur(0.4))
            self.play(ReplacementTransform(dim, dim_n), run_time=self.dur(0.6))

            # «caben en una línea»
            self.en("linea")
            self.play(Create(caja_), run_time=self.dur(0.5))

            # «La matriz de covarianzas de las mediciones»
            self.en("cxx")
            self.play(FadeIn(lin[0], shift=UP * 0.1), run_time=0.4)
            self.resaltar(M.corchetes, color=AMBAR, escala=1.05)

            # «por los pesos»
            self.en("h")
            self.play(FadeIn(lin[1], shift=UP * 0.1), run_time=0.4)
            self.resaltar(H.corchetes, color=AMBAR, escala=1.05)

            # «igual a las covarianzas con lo que se estima»
            self.en("cxy")
            self.play(FadeIn(lin[2]), FadeIn(lin[3], shift=UP * 0.1), run_time=0.4)
            self.resaltar(C.corchetes, color=AMBAR, escala=1.05)

            # «Se llaman ecuaciones normales»
            self.en("normales")
            self.play(FadeOut(ea), FadeOut(eb), run_time=0.3)
            self.pop(nombre)

            # «normal, en geometría»
            self.en("geo")
            self.play(Create(geo_l), run_time=0.4)
            self.play(Create(geo_n), Create(geo_r), run_time=self.dur(0.5))

            # «significa perpendicular»
            self.en("perp")
            self.play(FadeIn(perp, shift=UP * 0.1), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b2
    def resolver(self):
        top = formula(r"C_{xx}", r"\,\mathbf{h}", "=", r"\mathbf{c}_{xy}", escala=1.2,
                      colores={1: ESTIMACION, 3: SENAL}).move_to([0, 3.1, 0])
        div = MathTex(r"\mathbf{h}=\mathbf{c}_{xy}\div C_{xx}", color=INK).scale(1.1).move_to([-3.4, 1.9, 0])
        inv = formula(r"\mathbf{h}", "=", r"C_{xx}^{-1}", r"\,\mathbf{c}_{xy}", escala=1.1,
                      colores={0: ESTIMACION, 2: AMBAR, 3: SENAL}).move_to([-3.4, 1.9, 0])
        D = Matriz8([["5", "4"], ["4", "8"]], centro=(-3.6, -0.6), dx=1.0, dy=0.85, escala=1.05)
        det = MathTex(r"\det", color=TXT).scale(1.0).next_to(D, LEFT, buff=0.25)
        ne0 = MathTex(r"\neq 0", color=TXT).scale(1.0).next_to(D, RIGHT, buff=0.25)
        n58 = MathTex(r"5\cdot 8", color=AMBAR).scale(1.0).move_to([-5.4, -2.3, 0], aligned_edge=LEFT)
        n44 = MathTex(r"-\,4\cdot 4", color=CIAN).scale(1.0).next_to(n58, RIGHT, buff=0.18)
        d24 = MathTex("=24", color=VERDE).scale(1.0).next_to(n44, RIGHT, buff=0.18)
        er = formula(r"\text{Error}", "=", r"\sigma_y^2", r"-(4h_A+4h_B)", escala=0.95,
                     colores={0: ERROR, 2: SENAL}).move_to([0.6, 1.9, 0], aligned_edge=LEFT)
        P = PlanoDos8(centro=(4.3, -1.5), k=1.05)
        figura = VGroup(P.plano, P.xa, P.xb, P.y, P.sombra, P.error, P.recto_a, P.recto_b, *P.rot.values())

        with self.narrar("b2"):
            # «Resolverlas»
            self.en("res")
            self.corte()
            self.play(FadeIn(top, shift=DOWN * 0.1), run_time=self.dur(0.5))

            # «dividir entre la matriz»
            self.en("div")
            self.play(FadeIn(div, shift=UP * 0.1), run_time=self.dur(0.5))

            # «multiplicar por su inversa»
            self.en("inv")
            self.play(ReplacementTransform(div, inv), run_time=self.dur(0.7))

            # «un número llamado determinante»
            self.en("det")
            self.play(FadeIn(D), FadeIn(det, shift=RIGHT * 0.1), run_time=self.dur(0.6))

            # «no es cero»
            self.en("ne0")
            self.play(FadeIn(ne0, shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «el producto de la diagonal»
            self.en("pd")
            self.play(D.c[0][0].animate.set_color(AMBAR).scale(1.25), D.c[1][1].animate.set_color(AMBAR).scale(1.25),
                      run_time=self.dur(0.5))

            # «menos el de fuera»
            self.en("pf")
            self.play(D.c[0][1].animate.set_color(CIAN).scale(1.25), D.c[1][0].animate.set_color(CIAN).scale(1.25),
                      run_time=self.dur(0.5))

            # «Cinco por ocho»
            self.en("n58")
            self.play(FadeIn(n58, shift=UP * 0.1), run_time=self.dur(0.4))

            # «menos cuatro por cuatro»
            self.en("n44")
            self.play(FadeIn(n44, shift=UP * 0.1), run_time=self.dur(0.4))

            # «veinticuatro»
            self.en("d24")
            self.pop(d24)

            # «Y el error es la varianza»
            self.en("err")
            self.play(*[FadeIn(er[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.5))

            # «menos los pesos por las covarianzas»
            self.en("menos")
            self.play(FadeIn(er[3], shift=LEFT * 0.15), run_time=self.dur(0.6))

            # «al ser perpendicular a las lecturas»
            self.en("perp2")
            self.play(FadeIn(figura), run_time=self.dur(0.8))

            # «el error solo comparte con la temperatura»
            self.en("comparte")
            self.resaltar(P.y, color=AMBAR, escala=1.06)

            # «su propio tamaño»
            self.en("tam")
            self.resaltar(P.error, color=AMBAR, escala=1.1)
