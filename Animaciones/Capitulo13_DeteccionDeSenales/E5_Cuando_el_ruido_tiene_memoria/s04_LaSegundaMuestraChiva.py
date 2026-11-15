"""Escena 04 — La segunda muestra chiva: restar 0,6 veces la vecina baja la varianza a 0,64."""
from comun.escena import *


class LaSegundaMuestraChiva(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.idea()
        self.varianza()
        self.resultado()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def idea(self):
        self.P = P = PlanoV(centro=(-4.0, -0.6), lado=2.4, esc=1.0)
        self.nube = P.puntos(0.6, n=34)
        self.el = P.elipse(0.6)
        r1 = MathTex("r_1", color=MEDIDA).scale(1.4).move_to([3.4, 2.6, 0])
        x = cruz(ERROR, 0.7).move_to(r1)
        v0 = Dot([1.8, 0.7, 0], radius=0.14, color=RUIDO)
        v1 = Dot([4.6, 0.7, 0], radius=0.14, color=RUIDO)
        l0 = MathTex("v_0", color=RUIDO).scale(0.7).next_to(v0, DOWN, buff=0.15)
        l1 = MathTex("v_1", color=RUIDO).scale(0.7).next_to(v1, DOWN, buff=0.15)
        hilo = Line(v0.get_center(), v1.get_center(), color=RUIDO, stroke_width=4)
        flecha_ = CurvedArrow(v1.get_top() + UP * 0.05, v0.get_top() + UP * 0.05, angle=PI / 2.2,
                              color=AMBAR, stroke_width=5)
        pista = Text("pista", color=AMBAR).scale(0.55).next_to(flecha_, UP, buff=0.08)
        comb = MathTex("r_0", "-", "?", r"\cdot", "r_1", color=TXT).scale(1.0).move_to([3.2, -1.4, 0])
        comb[0].set_color(MEDIDA); comb[4].set_color(MEDIDA); comb[2].set_color(AMBAR)
        fin = MathTex("r_0", "-", "0{,}6", r"\cdot", "r_1", color=TXT).scale(1.0).move_to(comb)
        fin[0].set_color(MEDIDA); fin[4].set_color(MEDIDA); fin[2].set_color(AMBAR)
        # un caso con v0 alto
        alto = Dot(P.p(1.5, 0.95), radius=0.11, color=AMBAR)
        guia = DashedLine(P.p(1.5, 0), P.p(1.5, 0.95), color=AMBAR, stroke_width=2.5)
        vuelve = Arrow(P.p(1.5, 0.95), P.p(1.5, 0.1), color=VERDE, stroke_width=4, buff=0.05,
                       max_tip_length_to_length_ratio=0.2)

        with self.narrar("b1"):
            # «no es basura»
            self.en("basura")
            self.play(FadeIn(r1), run_time=self.dur(0.4))
            self.play(FadeIn(x), run_time=self.dur(0.3))
            self.play(FadeOut(x), run_time=self.dur(0.4))

            # «se parece al de la primera»
            self.en("parece")
            self.play(Create(P.ejes), FadeIn(P.rot0), FadeIn(P.rot1), FadeIn(self.nube), Create(self.el),
                      run_time=self.dur(0.9))

            # «nos chiva»
            self.en("chiva")
            self.play(FadeIn(v0), FadeIn(v1), FadeIn(l0), FadeIn(l1), Create(hilo), run_time=self.dur(0.5))
            self.play(Create(flecha_), run_time=self.dur(0.5))

            # «algo del ruido de la primera»
            self.en("algo")
            self.play(FadeIn(pista), run_time=self.dur(0.4))

            # «una combinación»
            self.en("comb")
            self.play(FadeIn(comb, shift=UP * 0.1), run_time=self.dur(0.6))

            # «la primera menos cero coma seis veces la segunda»
            self.en("formula")
            self.play(ReplacementTransform(comb, fin), run_time=self.dur(0.7))

            # «Si el ruido de la primera»
            self.en("si")
            self.play(Create(guia), FadeIn(alto), run_time=self.dur(0.6))

            # «fue alto»
            self.en("alto")
            self.play(alto.animate(rate_func=there_and_back).scale(1.8), run_time=self.dur(0.5))

            # «la resta lo compensa»
            self.en("compensa")
            self.play(GrowArrow(vuelve), run_time=self.dur(0.7))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def varianza(self):
        regla_a = MathTex(r"\mathrm{Var}(aX+bY)", "=", r"a^2\sigma_X^2", "+", r"b^2\sigma_Y^2", "+",
                          r"2ab\,\mathrm{Cov}", color=TXT).scale(0.8).move_to([0.8, 3.4, 0])
        A = MathTex(r"\mathrm{Var}", "=", "1", "+", r"0{,}6^2", "-", r"2\cdot 0{,}6\cdot 0{,}6",
                    color=TXT).scale(0.95).move_to([2.6, 1.7, 0])
        B = MathTex("=", "1", "+", "0{,}36", "-", "0{,}72", "=", "0{,}64", color=TXT).scale(0.95)
        B.next_to(A, DOWN, buff=0.45).align_to(A, LEFT)
        A[2].set_color(MEDIDA); A[4].set_color(MEDIDA)
        cov = Text("covarianza", color=RUIDO).scale(0.5).next_to(A[6], UP, buff=0.5)
        llave = Brace(A[6], UP, color=RUIDO, buff=0.08)
        cuadro = SurroundingRectangle(B, color=AMBAR, buff=0.12, stroke_width=3)

        with self.narrar("b2"):
            # «con la regla del capítulo siete»
            self.en("regla")
            self.corte()
            self.play(FadeIn(regla_a[0]), FadeIn(regla_a[1]), run_time=self.dur(0.6))

            # «varianza de una combinación»
            self.en("varcomb")
            self.play(*[FadeIn(regla_a[i]) for i in range(2, 7)], run_time=self.dur(1.2))

            # «Uno, de la primera»
            self.en("t1")
            self.play(*[FadeIn(A[i]) for i in range(3)], run_time=self.dur(0.6))

            # «más cero coma seis al cuadrado»
            self.en("t2")
            self.play(FadeIn(A[3]), FadeIn(A[4]), run_time=self.dur(0.6))

            # «cero coma tres seis»
            self.en("t36")
            self.play(*[FadeIn(B[i]) for i in range(4)], run_time=self.dur(0.7))

            # «menos dos por cero coma seis por cero coma seis»
            self.en("t3")
            self.play(FadeIn(A[5]), FadeIn(A[6]), run_time=self.dur(0.7))

            # «de la covarianza»
            self.en("cov")
            self.play(Create(llave), FadeIn(cov), run_time=self.dur(0.6))

            # «cero coma siete dos»
            self.en("t72")
            self.play(FadeIn(B[4]), FadeIn(B[5]), run_time=self.dur(0.6))

            # «Uno más cero coma tres seis menos cero coma siete dos»
            self.en("suma")
            self.play(Create(cuadro), run_time=self.dur(0.5))

            # «cero coma seis cuatro»
            self.en("v64")
            self.play(FadeIn(B[6]), FadeIn(B[7]), run_time=self.dur(0.5))
            self.resaltar(B[7], color=AMBAR, escala=1.25)
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def resultado(self):
        S = Tallos([2, 0], centro=(-4.8, 1.3), paso=1.2, unidad=0.8, color=SENAL, indices=True)
        lmed = Text("media = 2", color=INK).scale(0.5).next_to(S, UP, buff=0.4)
        asi = MathTex("d^2", "=", color=TXT).scale(1.0).move_to([1.3, 2.5, 0])
        cuenta = MathTex(r"\frac{4}{0{,}64}", color=TXT).scale(1.0).next_to(asi, RIGHT, buff=0.15)
        r625 = MathTex("=", num_tex(6.25), color=AMBAR).scale(1.0).next_to(cuenta, RIGHT, buff=0.15)
        antes = MathTex("d^2", "=", "4", color=INK).scale(0.85).move_to([1.4, 1.2, 0])
        tach = Line(antes.get_left() + LEFT * 0.1, antes.get_right() + RIGHT * 0.1, color=ERROR, stroke_width=5)
        e1 = MathTex("Q(1)", "=", num_tex(0.1587, 4), color=ERROR).scale(1.1).move_to([2.6, -0.1, 0])
        e2 = MathTex("Q(1{,}25)", "=", num_tex(0.1056, 4), color=ERROR).scale(1.1).move_to([2.6, -1.2, 0])
        pes = Tallos([1, -0.6], centro=(-4.8, -1.8), paso=1.2, unidad=0.8, color=ESTIMACION)
        pes_l = MathTex(r"(1,\ -0{,}6)", color=ESTIMACION).scale(1.0).next_to(pes, UP, buff=0.55)
        rev = Tallos([0, 2], centro=(-1.0, -2.8), paso=1.2, unidad=0.8, color=SENAL, indices=True)
        rev_l = MathTex(r"(0,\ 2)", color=SENAL).scale(1.0).next_to(rev, UP, buff=0.5)
        dist = MathTex(r"\neq", color=TXT).scale(1.3).move_to([-2.9, -1.7, 0])
        receta = Text("receta distinta", color=AMBAR, weight=BOLD).scale(0.8).move_to([4.2, -2.9, 0])

        with self.narrar("b3"):
            # «La media sigue siendo dos»
            self.en("media")
            self.corte()
            self.play(FadeIn(lmed), run_time=self.dur(0.4))

            # «solo está en la primera muestra»
            self.en("sola")
            self.play(Create(S.base), Create(S.palito(0)), Create(S.palito(1)), FadeIn(S.ks), run_time=self.dur(0.7))

            # «Así que la relación vale»
            self.en("asi")
            self.play(FadeIn(asi), run_time=self.dur(0.4))

            # «cuatro entre cero coma seis cuatro»
            self.en("cuenta")
            self.play(FadeIn(cuenta, shift=UP * 0.1), run_time=self.dur(0.6))

            # «seis coma dos cinco»
            self.en("s625")
            self.play(FadeIn(r625, shift=UP * 0.1), run_time=self.dur(0.5))

            # «Mucho mejor que cuatro»
            self.en("mejor")
            self.play(FadeIn(antes), Create(tach), run_time=self.dur(0.6))

            # «de cero coma uno cinco ocho siete»
            self.en("e1587")
            self.play(FadeIn(e1, shift=UP * 0.1), run_time=self.dur(0.5))

            # «a cero coma uno cero cinco seis»
            self.en("e1056")
            self.play(FadeIn(e2, shift=UP * 0.1), run_time=self.dur(0.5))

            # «los pesos del mejor filtro»
            self.en("pesos")
            self.play(Create(pes.base), Create(pes.palito(0)), Create(pes.palito(1)),
                      FadeIn(pes_l), run_time=self.dur(0.7))

            # «no son la señal al revés»
            self.en("noalreves")
            self.play(Create(rev.base), Create(rev.palito(0)), Create(rev.palito(1)), FadeIn(rev.ks),
                      FadeIn(rev_l), FadeIn(dist), run_time=self.dur(0.8))

            # «La receta cambia»
            self.en("receta")
            self.pop(receta)
