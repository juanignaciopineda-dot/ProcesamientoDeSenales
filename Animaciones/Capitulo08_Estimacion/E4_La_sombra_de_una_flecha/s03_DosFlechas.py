"""Escena 03 — El termómetro como flechas: largos 2 y √5, producto escalar 4, ángulo de ≈ 27° y la recta h · X."""
from comun.escena import *
from comun.figuras_c8e4 import *


class DosFlechas(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.F, self.r = flechas8()
        self.presentar()
        self.estimacion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def presentar(self):
        F, r = self.F, self.r
        o = F.o
        G = Flechas(origen=(o[0], o[1]), largo=4.6, angulo=40, largo_objetivo=3.8, color_dato=INK, color_objetivo=INK)
        arco_g = Arc(radius=1.1, start_angle=0, angle=np.deg2rad(40), arc_center=G.o, color=AMBAR, stroke_width=4)
        p1 = Text("Largo = desviación estándar", color=TXT).scale(0.62).move_to([3.4, 2.6, 0])
        p2 = Text("Producto escalar = covarianza", color=TXT).scale(0.62).move_to([3.4, 1.4, 0])
        p3 = formula(r"\cos\theta", "=", r"\rho", escala=1.2, colores={2: AMBAR}).move_to([3.4, 0.2, 0])
        n_dos = MathTex("2", color=SENAL).scale(0.9)
        n_dos.move_to((F.o + F.fin_futuro) / 2 + np.array([-np.sin(np.deg2rad(ANG8)), np.cos(np.deg2rad(ANG8)), 0]) * 0.45)
        n_r5 = MathTex(r"\sqrt{5}", color=MEDIDA).scale(0.9).move_to((F.o + F.fin_presente) / 2 + DOWN * 0.5)
        n_r5b = MathTex(r"\sqrt{5}\approx 2{,}24", color=MEDIDA).scale(0.9).move_to(n_r5)

        with self.narrar("b1"):
            # «se comportan como flechas»
            self.en("flechas")
            self.play(Create(G.presente), Create(G.futuro), run_time=self.dur(0.8))

            # «El largo de cada flecha»
            self.en("largo")
            self.play(FadeIn(p1, shift=LEFT * 0.2), run_time=self.dur(0.5))
            self.resaltar(G.futuro, color=AMBAR, escala=1.04)

            # «su producto escalar»
            self.en("escalar")
            self.play(FadeIn(p2, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «el coseno del ángulo»
            self.en("coseno")
            self.play(Create(arco_g), run_time=self.dur(0.5))
            self.play(FadeIn(p3, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Dibujemos así el termómetro»
            self.en("termo")
            self.play(FadeOut(G), FadeOut(arco_g), FadeOut(p1), FadeOut(p2), FadeOut(p3), run_time=self.dur(0.4))
            self.play(Create(F.presente), Create(F.futuro), run_time=self.dur(0.7))

            # «La temperatura»
            self.en("temp")
            self.play(FadeIn(r["y"]), run_time=self.dur(0.4))

            # «de largo dos»
            self.en("dos")
            self.pop(n_dos)

            # «La lectura»
            self.en("lectura")
            self.play(FadeIn(r["x"]), run_time=self.dur(0.4))

            # «raíz de cinco»
            self.en("r5")
            self.pop(n_r5)

            # «algo más de dos coma dos»
            self.en("dosdos")
            self.play(ReplacementTransform(n_r5, n_r5b), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b2
    def estimacion(self):
        F, r = self.F, self.r
        o = F.o
        pe = formula(r"\langle", "Y", ",", "X", r"\rangle", "=", r"\sigma_{YX}", "=", "4", escala=1.15,
                     colores={1: SENAL, 3: MEDIDA, 8: AMBAR}).move_to([3.7, 2.8, 0])
        cs = formula(r"\cos\theta", "=", r"\frac{4}{2\cdot\sqrt{5}}", escala=1.15).move_to([2.6, 1.3, 0])
        c89 = formula(r"\approx", num_tex(0.89), escala=1.15, colores={1: AMBAR}).next_to(cs, RIGHT, buff=0.25)
        arco = Arc(radius=1.0, start_angle=0, angle=np.deg2rad(ANG8), arc_center=o, color=AMBAR, stroke_width=4)
        r27 = MathTex(r"\approx 27^\circ", color=AMBAR).scale(0.9).move_to(o + 2.5 * np.array([np.cos(0.23), np.sin(0.23), 0]))
        est = formula(r"\hat{y}", "=", "h", r"\cdot", "X", escala=1.2,
                      colores={0: ESTIMACION, 2: ESTIMACION, 4: MEDIDA}).move_to([3.7, -0.5, 0])
        est_t = Text("Estimación", color=ESTIMACION).scale(0.6).next_to(est, UP, buff=0.3)
        tr = ValueTracker(0.5)
        trozo = always_redraw(lambda: Line(o, en_recta8(F, tr.get_value()), color=ESTIMACION, stroke_width=11))
        punta = always_redraw(lambda: Dot(en_recta8(F, tr.get_value()), radius=0.12, color=ESTIMACION))
        fantasmas = VGroup(*[Dot(en_recta8(F, h), radius=0.08, color=ESTIMACION).set_opacity(0.45)
                             for h in (-0.1, 0.2, 0.35, 0.65, 0.85, 1.15, 1.3)])
        v = F.fin_presente - o
        recta = DashedLine(o - 0.1 * v, o + 1.25 * v, color=INK, dash_length=0.18, stroke_width=3)

        with self.narrar("b2"):
            # «Su producto escalar»
            self.en("pe")
            self.play(*[FadeIn(pe[i]) for i in range(6)], run_time=self.dur(0.6))

            # «la covarianza, cuatro»
            self.en("cuatro")
            self.play(*[FadeIn(pe[i]) for i in range(6, 9)], run_time=self.dur(0.6))

            # «el coseno del ángulo es»
            self.en("cos")
            self.play(FadeIn(cs), run_time=self.dur(0.9))

            # «cero coma ocho nueve»
            self.en("cos89")
            self.play(FadeIn(c89), run_time=self.dur(0.5))

            # «Forman unos veintisiete grados»
            self.en("ang")
            self.play(Create(arco), FadeIn(r27), run_time=self.dur(0.7))

            # «la estimación»
            self.en("estim")
            self.play(FadeIn(est_t), run_time=self.dur(0.4))

            # «hache por la lectura»
            self.en("hx")
            self.play(*[FadeIn(est[i]) for i in range(5)], run_time=self.dur(0.6))
            self.play(FadeIn(trozo), FadeIn(punta), run_time=self.dur(0.3))

            # «estirada o encogida»
            self.en("estira")
            for h in (1.0, 0.25, 0.7):
                self.play(tr.animate.set_value(h), run_time=self.dur(0.7))

            # «Todas las opciones»
            self.en("todas")
            self.play(LaggedStart(*[FadeIn(d) for d in fantasmas], lag_ratio=0.2), run_time=self.dur(1.2))

            # «una misma recta»
            self.en("recta")
            self.play(Create(recta), run_time=self.dur(0.8))

            # «la dirección de la lectura»
            self.en("direccion")
            self.resaltar(F.presente, color=MEDIDA, escala=1.04)
        trozo.clear_updaters()
        punta.clear_updaters()
