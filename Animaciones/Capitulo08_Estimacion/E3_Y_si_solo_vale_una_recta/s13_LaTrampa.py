"""Escena 13 — La trampa: la recta para adivinar x desde y no es la inversa; hay dos rectas distintas."""
from comun.escena import *
from comun.figuras_cap08_e3 import *

AMARILLO = "#f2d04b"


class LaTrampa(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.al_reves()
        self.dos_rectas()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def al_reves(self):
        trampa = Text("Trampa", color=ROJO, weight=BOLD).scale(1.3).move_to([0, 3.3, 0])
        antes = Text("Antes", color=INK).scale(0.6).move_to([-5.9, 1.9, 0], aligned_edge=LEFT)
        f_antes = MathTex("x", r"\to", "y").scale(1.0).move_to([-3.6, 1.9, 0])
        f_antes[0].set_color(MEDIDA)
        f_antes[2].set_color(SENAL)
        ahora = Text("Ahora", color=AMBAR, weight=BOLD).scale(0.6).move_to([-5.9, 0.8, 0], aligned_edge=LEFT)
        f_ahora = MathTex("y", r"\to", "x").scale(1.0).move_to([-3.6, 0.8, 0])
        f_ahora[0].set_color(SENAL)
        f_ahora[2].set_color(MEDIDA)
        marca = Text("Adivinar la lectura", color=MEDIDA).scale(0.55).move_to([-6.2, -0.2, 0], aligned_edge=LEFT)
        rev = formula(r"\hat{x}", "=", r"\mu_x", "+", r"\rho", r"\frac{\sigma_x}{\sigma_y}", "(", "y", "-", r"\mu_y",
                      ")", escala=0.85, colores={0: ESTIMACION, 2: MEDIDA, 7: SENAL, 9: SENAL}).move_to([2.6, 1.9, 0])
        r_fac = SurroundingRectangle(VGroup(rev[4], rev[5]), color=AMBAR, buff=0.08)
        inv = formula(r"\frac{1}{0{,}8}", "=", r"1{,}25", escala=1.2, colores={2: ERROR}).move_to([2.6, 0.5, 0])
        tach = tachar(inv[2])
        S = formula(r"\frac{\sigma_{xy}}{\sigma_y^2}", "=", r"\frac{4}{\sigma_y^2}", "=", r"\frac{4}{4}", "=", "1",
                    escala=1.1, colores={6: VERDE}).move_to([1.2, -1.1, 0])
        misma = MathTex(r"\hat{x}=y", color=AMBAR).scale(1.6).move_to([0.5, -2.7, 0])
        f_arr = Arrow([5.6, -2.5, 0], [5.6, -1.6, 0], buff=0, color=RUIDO, stroke_width=6,
                      max_tip_length_to_length_ratio=0.35)
        f_abj = Arrow([5.6, -2.5, 0], [5.6, -3.4, 0], buff=0, color=RUIDO, stroke_width=6,
                      max_tip_length_to_length_ratio=0.35)
        t_v = MathTex("v", color=RUIDO).scale(0.9).move_to([6.3, -2.5, 0])

        with self.narrar("b1"):
            # «una trampa»
            self.en("trampa")
            self.pop(trampa)

            # «Cambiemos la pregunta»
            self.en("cambio")
            self.play(FadeIn(antes), FadeIn(f_antes), run_time=self.dur(0.5))
            self.play(FadeIn(ahora), FadeIn(f_ahora), run_time=self.dur(0.6))

            # «adivina qué marcará el termómetro»
            self.en("marca")
            self.play(FadeIn(marca, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Si fuera la misma recta al revés»
            self.en("reves")
            self.play(*[FadeIn(rev[i], shift=UP * 0.1) for i in range(11)], run_time=self.dur(1.2))

            # «el factor sería»
            self.en("sera")
            self.play(Create(r_fac), run_time=self.dur(0.5))

            # «uno entre cero coma ocho»
            self.en("inv")
            self.play(FadeIn(inv[0], shift=UP * 0.1), run_time=self.dur(0.6))

            # «uno coma veinticinco»
            self.en("v125")
            self.play(FadeIn(inv[1]), FadeIn(inv[2], shift=UP * 0.1), run_time=self.dur(0.6))

            # «Pero la fórmula dice covarianza»
            self.en("forml")
            self.play(FadeOut(r_fac), FadeIn(S[0], shift=UP * 0.1), run_time=self.dur(0.7))

            # «covarianza, cuatro,»
            self.en("cov4")
            self.play(FadeIn(S[1]), FadeIn(S[2], shift=UP * 0.1), run_time=self.dur(0.6))

            # «la varianza de lo que observas»
            self.en("ent")
            self.play(Indicate(S[2], color=AMBAR), run_time=self.dur(0.8))

            # «ahora la temperatura, cuatro»
            self.en("var4")
            self.play(FadeIn(S[3]), FadeIn(S[4], shift=UP * 0.1), run_time=self.dur(0.7))

            # «Uno.»
            self.en("uno")
            self.play(FadeIn(S[5]), FadeIn(S[6], shift=UP * 0.1), Create(tach), run_time=self.dur(0.6))

            # «La apuesta es la temperatura misma»
            self.en("misma")
            self.pop(misma, sonido="exito")

            # «el ruido es igual de probable»
            self.en("ruido")
            self.play(GrowArrow(f_arr), GrowArrow(f_abj), FadeIn(t_v), run_time=self.dur(0.7))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def dos_rectas(self):
        nube = NubeRhoE3(centro=(0.0, -0.2), sx=1.7, sy=1.15, n=50, rho=0.9)
        l1 = nube.recta(0.9, ESTIMACION)
        l2 = nube.recta_inv(0.9, AMARILLO)
        t1 = MathTex("x", r"\to", "y").scale(0.9).move_to([5.8, 2.6, 0])
        t1.set_color(ESTIMACION)
        t2 = MathTex("y", r"\to", "x").scale(0.9).move_to([3.0, 3.45, 0])
        t2.set_color(AMARILLO)
        b = nube.b(0.9)
        idx = list(range(0, len(nube.a), 3))
        verticales = VGroup(*[Line(nube.p(nube.a[i], b[i]), nube.p(nube.a[i], 0.9 * nube.a[i]),
                                   color=ERROR, stroke_width=3) for i in idx])
        horizontales = VGroup(*[Line(nube.p(nube.a[i], b[i]), nube.p(0.9 * b[i], b[i]),
                                     color=ERROR, stroke_width=3) for i in idx])
        tr = ValueTracker(0.9)
        t_v = Text("Errores en vertical", color=ERROR).scale(0.5).move_to([-4.6, 2.6, 0])
        t_h = Text("Errores en horizontal", color=ERROR).scale(0.5).move_to([-4.6, 2.6, 0])

        with self.narrar("b2"):
            # «sobre la misma nube»
            self.en("nube")
            self.corte()
            self.play(FadeIn(nube), run_time=self.dur(0.8))

            # «la que adivina i griega a partir de equis»
            self.en("r1")
            self.play(Create(l1), FadeIn(t1), run_time=self.dur(0.9))

            # «y la que adivina equis a partir de i griega»
            self.en("r2")
            self.play(Create(l2), FadeIn(t2), run_time=self.dur(0.9))

            # «mide los errores en vertical»
            self.en("vert")
            self.play(LaggedStart(*[Create(s) for s in verticales], lag_ratio=0.06), FadeIn(t_v),
                      run_time=self.dur(1.3))

            # «la segunda, en horizontal»
            self.en("hori")
            self.play(FadeOut(verticales), FadeOut(t_v), run_time=self.dur(0.3))
            self.play(LaggedStart(*[Create(s) for s in horizontales], lag_ratio=0.06), FadeIn(t_h),
                      run_time=self.dur(1.3))

            # «Solo coinciden cuando rho vale uno o menos uno»
            self.en("coin")
            self.play(FadeOut(horizontales), FadeOut(t_h), run_time=self.dur(0.3))
            nube.add_updater(lambda m: m.colocar(tr.get_value()))
            l1.add_updater(lambda m: m.become(nube.recta(tr.get_value(), ESTIMACION)))
            l2.add_updater(lambda m: m.become(nube.recta_inv(tr.get_value(), AMARILLO)))
            self.play(tr.animate.set_value(0.999), run_time=self.dur(2.2), rate_func=linear)
            nube.clear_updaters()
            l1.clear_updaters()
            l2.clear_updaters()
