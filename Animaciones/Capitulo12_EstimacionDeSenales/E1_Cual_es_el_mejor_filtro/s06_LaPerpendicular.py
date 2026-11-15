"""Escena 06 — La parábola y el ángulo recto: la misma condición; y con varias mediciones, las ecuaciones normales."""
from comun.escena import *


class LaPerpendicular(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.con_flechas()
        self.varias_mediciones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def con_flechas(self):
        F, r = flechas_xy(origen=(-3.8, -1.7), largo=4.4, angulo=50)
        d1 = formula("J'(h)", "=", "-8+10h", escala=1.2).move_to([3.8, 2.8, 0])
        d2 = formula("J'(h)", "=", r"-2\,E[\,e\,x\,]", "=", "0", escala=1.2,
                     colores={2: ERROR}).move_to([3.8, 2.8, 0])
        par = parabola_l(centro=(4.9, -0.7), ancho=3.4, alto=2.0, fondo=0.25, color=ERROR)
        igual = MathTex("=", color=TXT).scale(1.6).move_to([2.2, -0.9, 0])
        caps = Text("Caps. 7 y 8", color=INK).scale(0.5).move_to([-3.2, -3.4, 0])

        with self.narrar("b1"):
            # «lo mismo con flechas»
            self.en("flechas")
            self.corte()
            self.play(Create(F.presente), Create(F.futuro), FadeIn(r["x"]), FadeIn(r["y"]), run_time=self.dur(0.8))

            # «Esa derivada»
            self.en("esa")
            self.play(FadeIn(d1, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «menos dos por la media del error por equis»
            self.en("dermedia")
            self.play(FadeOut(d1), *[FadeIn(d2[i]) for i in range(3)], run_time=self.dur(0.8))

            # «Que valga cero»
            self.en("cero")
            self.play(FadeIn(d2[3]), FadeIn(d2[4]), run_time=self.dur(0.4))

            # «el error es perpendicular al dato»
            self.en("perp")
            self.play(Create(F.error), FadeIn(r["e"]), run_time=self.dur(0.6))

            # «La mejor estimación»
            self.en("mejor")
            self.play(Create(F.sombra), run_time=self.dur(0.5))

            # «la proyección de la flecha de i griega»
            self.en("proy")
            self.play(FadeIn(r["yh"]), run_time=self.dur(0.4))
            self.resaltar(F.sombra, color=AMBAR, escala=1.05)

            # «sobre la flecha de equis»
            self.en("sobre")
            self.resaltar(F.presente, color=MEDIDA, escala=1.05)

            # «el error en ángulo recto»
            self.en("recto")
            self.play(Create(F.recto), run_time=self.dur(0.4))
            self.resaltar(F.error, color=ERROR, escala=1.08)

            # «los capítulos siete y ocho»
            self.en("caps78")
            self.pop(caps)

            # «son la misma condición»
            self.en("igual")
            self.play(FadeIn(igual), Create(par), run_time=self.dur(0.8))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def varias_mediciones(self):
        o = np.array([-4.8, -2.2, 0.0])
        xs = [flecha_c(o, 3.0, g, MEDIDA, 5) for g in (10, 40, 70)]
        lxs = [MathTex(f"x_{i + 1}", color=MEDIDA).scale(0.8).move_to(o + 3.45 * np.array([np.cos(np.deg2rad(g)), np.sin(np.deg2rad(g)), 0]))
               for i, g in enumerate((10, 40, 70))]
        yf = flecha_c(o, 4.0, 110, SENAL, 6)
        ly = MathTex("y", color=SENAL).scale(0.9).move_to(o + 4.4 * np.array([np.cos(np.deg2rad(110)), np.sin(np.deg2rad(110)), 0]))
        perps = [MathTex(f"e \\perp x_{i + 1}", color=ERROR).scale(1.05).move_to([4.2, 3.1 - 0.75 * i, 0]) for i in range(3)]
        ec = formula("C_{xx}", "a", "=", "c", escala=1.4, colores={0: MEDIDA, 3: SENAL}).move_to([3.7, 0.0, 0])
        ex = formula(r"\sigma_y^2", "-", r"c^{T} C_{xx}^{-1} c", escala=1.1).move_to([3.7, -1.3, 0])
        rho = formula(r"\sigma_y^2", r"(1-\rho^2)", escala=1.3).move_to([3.7, -2.6, 0])
        marco = SurroundingRectangle(rho, color=AMBAR, buff=0.15)
        r_mat = SurroundingRectangle(ec[0], color=AMBAR, buff=0.08)
        r_a = SurroundingRectangle(ec[1], color=AMBAR, buff=0.08)
        r_c = SurroundingRectangle(ec[3], color=AMBAR, buff=0.08)
        nov = self.palabra("novedad", AMBAR, 0.85).move_to([3.7, 1.0, 0])
        Lp = Lienzo(ancho=6.0, alto=2.0, t_rango=(0, 39), v_max=7, centro=(-2.5, -0.6))
        t, yy, vv, xx = sensor12(40)
        curva = Lp.curva(t, xx, MEDIDA, 3.4)
        pts = VGroup(*[Dot(Lp.p(k, xx[k]), radius=0.1, color=AMBAR) for k in (26, 27, 28)])

        with self.narrar("b2"):
            # «varias mediciones»
            self.en("varias")
            self.corte()
            self.play(*[GrowArrow(a) for a in xs], *[FadeIn(l) for l in lxs], run_time=self.dur(0.9))

            # «perpendicularidad con cada una»
            self.en("cada")
            self.play(*[FadeIn(p, shift=LEFT * 0.2) for p in perps], run_time=self.dur(1.0))

            # «las ecuaciones normales»
            self.en("normales")
            self.play(*[FadeIn(ec[i]) for i in range(len(ec))], run_time=self.dur(0.8))

            # «la matriz de covarianzas»
            self.en("matriz")
            self.play(Create(r_mat), run_time=self.dur(0.4))

            # «por los coeficientes»
            self.en("coefs")
            self.play(FadeOut(r_mat), Create(r_a), run_time=self.dur(0.4))

            # «al vector de covarianzas»
            self.en("vector")
            self.play(FadeOut(r_a), Create(r_c), run_time=self.dur(0.4))

            # «con lo que se estima»
            self.en("estima")
            self.play(GrowArrow(yf), FadeIn(ly), run_time=self.dur(0.6))

            # «la varianza menos lo que la proyección explica»
            self.en("explica")
            self.play(FadeOut(r_c), *[FadeIn(ex[i]) for i in range(len(ex))], run_time=self.dur(1.0))

            # «uno menos rho al cuadrado»
            self.en("rho")
            self.play(*[FadeIn(rho[i]) for i in range(len(rho))], run_time=self.dur(0.8))

            # «Todo el capítulo es este resultado»
            self.en("todo")
            self.play(Create(marco), run_time=self.dur(0.5))

            # «La única novedad»
            self.en("novedad")
            self.pop(nov)

            # «muestras de un proceso»
            self.en("proceso")
            self.play(*[FadeOut(m) for m in xs + lxs + [yf, ly] + perps], run_time=self.dur(0.4))
            self.play(Create(curva), run_time=self.dur(0.6))
            self.play(FadeIn(pts), run_time=self.dur(0.4))
