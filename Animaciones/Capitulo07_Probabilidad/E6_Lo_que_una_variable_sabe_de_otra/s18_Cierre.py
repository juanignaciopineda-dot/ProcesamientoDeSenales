"""Escena 18 — Cierre: resumen y anuncio del E7, «Variables que son flechas»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def bloque1(self):
        ax, et = ejes((-3, 3, 1), (-3, 3, 1), ancho=4.6, alto=3.2, x_label="x", y_label="y")
        g = VGroup(ax, et).move_to([-4.0, 1.6, 0])
        a, b = puntos_corr(0.85, 26, 21)
        nube = VGroup(*[Dot(ax.c2p(np.clip(x, -2.4, 2.4), np.clip(y, -2.4, 2.4)), radius=0.08, color=SENAL)
                        for x, y in zip(a, b)])
        self.nube = nube
        recta = Line(ax.c2p(-2.7, -2.7), ax.c2p(2.7, 2.7), color=ESTIMACION, stroke_width=5)
        corr = formula("r_{XY}", "=", "E[XY]", escala=1.4, colores={0: AMBAR}).move_to([3.4, 3.0, 0])
        cov = formula(r"\sigma_{XY}", "=", "E[XY]", "-", r"\mu_X\mu_Y", escala=1.4,
                      colores={0: AMBAR}).move_to([3.4, 1.7, 0])
        ax2, et2 = ejes((-1.3, 1.3, 1), (-0.2, 1.3, 1), ancho=3.8, alto=2.6, x_label="x", y_label="y")
        g2 = VGroup(ax2, et2).move_to([-4.2, -2.1, 0])
        par = VGroup(*[Dot(ax2.c2p(x, x * x), radius=0.06, color=SENAL) for x in np.linspace(-1, 1, 25)])
        txt0 = formula(r"\sigma_{XY}", "=", "0", escala=1.3, colores={0: AMBAR, 2: AMBAR}).move_to([-0.3, -2.1, 0])
        ne = MathTex(r"\neq", color=ROJO).scale(1.4).move_to([1.4, -2.1, 0])
        ind = Text("Independientes", color=TXT, weight=BOLD).scale(0.6).move_to([3.4, -2.1, 0])
        a2, b2 = puntos_corr(0.0, 40, 5)
        ng = nube6((5.6, -3.2), 0.5, 0.4, np.clip(a2, -2, 2), np.clip(b2, -2, 2))
        with self.narrar("b1"):
            # «cómo medir si dos variables se mueven juntas»
            self.en("medir")
            self.play(Create(g), LaggedStart(*[FadeIn(p, scale=0.4) for p in nube], lag_ratio=0.03), run_time=self.dur(1.0))

            # «la correlación»
            self.en("corr")
            self.play(FadeIn(corr, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «la covarianza»
            self.en("cov")
            self.play(FadeIn(cov, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «descontando las medias»
            self.en("descontando")
            self.resaltar(cov[3], cov[4], color=AMBAR, escala=1.1)

            # «solo ven lo que va en línea recta»
            self.en("recta")
            self.play(Create(recta), run_time=self.dur(0.7))

            # «covarianza cero no es independencia»
            self.en("no_indep")
            self.play(Create(g2), FadeIn(par), FadeIn(txt0), run_time=self.dur(0.8))
            self.play(FadeIn(ne), FadeIn(ind), run_time=self.dur(0.5))

            # «salvo en las gaussianas»
            self.en("gaussianas")
            self.play(FadeIn(ng), Create(tilde(VERDE, 0.5).move_to([5.4, -1.9, 0])), run_time=self.dur(0.7))

    def bloque2(self):
        R = formula(r"\sigma_Z^2", "=", r"\alpha^2\sigma_X^2", "+", r"\beta^2\sigma_Y^2", "+", r"2\alpha\beta\,\sigma_{XY}",
                    escala=1.3, colores={0: AMBAR}).move_to([0, 3.0, 0])
        oculta(R)
        self.add(R)
        nums = Text("6    4    3", color=TXT, weight=BOLD).scale(1.3).move_to([-4.2, 0.2, 0])
        o = np.array([-4.8, -2.4, 0.0])
        ang = np.deg2rad(52)
        fx = Arrow(o, o + np.array([2.45 * 1.4, 0, 0]), color=SENAL, stroke_width=7, buff=0)
        fy = Arrow(o, o + 2.0 * 1.4 * np.array([np.cos(ang), np.sin(ang), 0]), color=MEDIDA, stroke_width=7, buff=0)
        lx = formula(r"\sqrt{6}", escala=1.1, colores={0: SENAL}).next_to(fx, DOWN, buff=0.15)
        ly = formula("2", escala=1.1, colores={0: MEDIDA}).next_to(fy.get_end(), UP, buff=0.12)
        arco = Arc(radius=0.9, start_angle=0, angle=ang, arc_center=o, color=AMBAR, stroke_width=4)
        with self.narrar("b2"):
            # «la varianza de una combinación»
            self.en("combi")
            self.play(*[FadeOut(m) for m in list(self.mobjects) if m not in (R, self.camera.frame)], run_time=0.3)
            self.play(LaggedStart(*revelar(*R), lag_ratio=0.12), run_time=self.dur(1.6))

            # «dos cuadrados y un término cruzado»
            self.en("tres_t")
            self.play(R[2].animate.set_color(SENAL), R[4].animate.set_color(MEDIDA), R[6].animate.set_color(AMBAR),
                      run_time=self.dur(0.8))

            # «te suena de otro sitio»
            self.en("suena")
            q = Text("?", color=AMBAR, weight=BOLD).scale(3.0).move_to([4.6, 0.4, 0])
            self.pop(q)

            # «dejar de pensar en las variables como números»
            self.en("numeros")
            self.play(FadeIn(nums, shift=UP * 0.2), run_time=self.dur(0.6))

            # «pensarlas como flechas»
            self.en("flechas")
            self.play(FadeOut(nums), GrowArrow(fx), GrowArrow(fy), run_time=self.dur(0.8))
            self.play(Create(arco), FadeIn(lx), FadeIn(ly), run_time=self.dur(0.5))

            # «De eso va»
            self.en("deeso")
            self.resaltar(fx, fy, color=AMBAR, escala=1.05)

            # «Variables que son flechas»
            self.en("titulo")
            t1 = self.palabra("Variables que", TXT, 0.9).move_to([3.4, -1.7, 0])
            t2 = self.palabra("Son flechas", AMBAR, 0.9).move_to([3.4, -2.7, 0])
            self.pop(t1)
            self.pop(t2)
