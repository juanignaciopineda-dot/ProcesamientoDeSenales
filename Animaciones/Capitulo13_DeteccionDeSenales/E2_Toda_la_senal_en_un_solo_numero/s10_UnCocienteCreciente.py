"""Escena 10 — La razón de verosimilitud es creciente en g: cualquier criterio da el mismo detector."""
from comun.escena import *


class UnCocienteCreciente(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.cociente()
        self.cierre_del_bucle()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def cociente(self):
        segunda = Text("¿y con otros criterios?", color=AMBAR, weight=BOLD).scale(0.85).move_to([-4.0, 3.55, 0])
        otros = VGroup(*[Text(t, color=TXT).scale(0.6) for t in ("error mínimo", "Neyman-Pearson", "riesgo mínimo")])
        otros.arrange(RIGHT, buff=0.6).move_to([0.0, 2.6, 0])
        L1 = formula(r"\Lambda", "=", r"\frac{f(\mathbf{r}\mid H_1)}{f(\mathbf{r}\mid H_0)}", escala=1.5,
                     colores={0: AMBAR}).move_to([-3.9, 1.1, 0])
        L2 = formula(r"\Lambda", "=", r"e^{\frac{2g-E}{2\sigma^2}}", escala=1.5,
                     colores={0: AMBAR}).move_to([3.0, 1.1, 0])
        ax, etq = ejes((0, 7), (0, 8), ancho=6.4, alto=2.7, x_label="g", y_label=r"\Lambda")
        ax.move_to([-0.2, -1.9, 0])
        etq = VGroup(*[e for e in etq])
        etq.shift(ax.get_center() - Axes(x_range=(0, 7), y_range=(0, 8), x_length=6.4, y_length=2.7).get_center())
        curva = ax.plot(lambda g: np.exp((2 * g - 9) / 2), x_range=(0.0, 6.55), color=ESTIMACION, stroke_width=5)
        eta = DashedLine(ax.c2p(0, 1), ax.c2p(6.6, 1), color=INK, stroke_width=3)
        eta_l = MathTex(r"\eta", color=INK).scale(1.1).next_to(ax.c2p(0, 1), LEFT, buff=0.15)
        corte = Dot(ax.c2p(4.5, 1), radius=0.12, color=AMBAR)
        baja = DashedLine(ax.c2p(4.5, 1), ax.c2p(4.5, 0), color=AMBAR, stroke_width=3)
        gam = MathTex(r"\gamma", color=AMBAR).scale(1.2).next_to(ax.c2p(4.5, 0), DOWN, buff=0.12)

        with self.narrar("b1"):
            # «Segunda pregunta»
            self.en("segunda")
            self.pop(segunda)

            # «¿por qué con otros criterios sigue valiendo?»
            self.en("otros")
            self.play(LaggedStart(*[FadeIn(o, shift=LEFT * 0.2) for o in otros], lag_ratio=0.3), run_time=self.dur(1.2))

            # «la razón de verosimilitud»
            self.en("razon")
            self.play(FadeIn(L1[0]), FadeIn(L1[1]), run_time=self.dur(0.5))

            # «el cociente de las dos densidades»
            self.en("cociente")
            self.play(FadeIn(L1[2], shift=UP * 0.1), run_time=self.dur(0.9))

            # «e elevado a dos ge menos la energía»
            self.en("exp")
            self.play(*[FadeIn(L2[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(1.2))

            # «entre dos sigma cuadrado»
            self.en("dossigma")
            self.play(Create(subrayado(L2[2])), run_time=self.dur(0.5))

            # «siempre creciente de ge»
            self.en("creciente")
            self.play(Create(ax), FadeIn(etq), Create(curva), run_time=self.dur(1.6))

            # «Comparar ese cociente con un umbral»
            self.en("umbral_l")
            self.play(Create(eta), FadeIn(eta_l), FadeIn(corte), run_time=self.dur(0.8))

            # «lo mismo que comparar ge con otro umbral»
            self.en("umbral_g")
            self.play(Create(baja), FadeIn(gam), run_time=self.dur(0.8))
        self.wait(0.2)

    # ------------------------------------------------------------ b2
    def cierre_del_bucle(self):
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
        tres = VGroup(*[Text(t, color=TXT).scale(0.8) for t in ("error mínimo", "Neyman-Pearson", "riesgo mínimo")])
        tres.arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([-4.6, 2.2, 0])
        det = caja("g ≷ γ", AMBAR, ancho=3.0, alto=1.2, scale=0.9).move_to([0.8, 2.2, 0])
        flechas = VGroup(*[Arrow(t.get_right() + RIGHT * 0.1, det.get_left() + LEFT * 0.05, buff=0.05, color=INK,
                                 stroke_width=3, max_tip_length_to_length_ratio=0.12) for t in tres])
        recta = recta_g(-0.3)
        marcas = VGroup(*[VGroup(Line([gx(v), -0.3 - 0.2, 0], [gx(v), -0.3 + 0.5, 0], color=c, stroke_width=5))
                          for v, c in ((3.4, CIAN), (4.5, AMBAR), (5.3, VERDE))])
        # el bucle: las dos mediciones del episodio anterior
        gran = Square(side_length=1.9, color=RUIDO, stroke_width=4).move_to([-5.0, -1.6, 0])
        peq = Square(side_length=0.95, color=SENAL, stroke_width=4).set_fill(SENAL, 0.3).move_to([-5.0, -1.6, 0])
        prom = formula("a", "=", r"\frac{r_1+r_2}{2}", escala=1.3, colores={0: AMBAR}).move_to([-2.2, -1.6, 0])
        perd = Text("error ¼: como no medir", color=ERROR, weight=BOLD).scale(0.6).move_to([-3.1, -3.0, 0])
        gg = MathTex("g", color=AMBAR).scale(2.0).move_to([2.2, -1.6, 0])
        suf = Text("suficiente", color=VERDE, weight=BOLD).scale(0.7).next_to(gg, DOWN, buff=0.3)
        nube = nube_de_puntos((5.4, -1.6), 0.9, 70, 7, RUIDO)
        oj = ojo(TXT).scale(0.8).move_to([0.8, -3.1, 0])
        no_oj = cruz(ROJO, 0.9).move_to(oj)

        with self.narrar("b2"):
            # «Neyman-Pearson, riesgo mínimo o error mínimo»
            self.en("tres")
            self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.2) for t in tres], lag_ratio=0.3), run_time=self.dur(1.2))

            # «el mismo detector»
            self.en("mismo")
            self.play(FadeIn(det), *[GrowArrow(a) for a in flechas], run_time=self.dur(0.8))

            # «dónde se pone la marca»
            self.en("marca")
            self.play(Create(recta), *[FadeIn(m) for m in marcas], run_time=self.dur(0.8))

            # «el bucle del episodio»
            self.en("bucle")
            self.play(FadeIn(gran), FadeIn(peq), run_time=self.dur(0.8))

            # «el promedio de las dos mediciones»
            self.en("promedio")
            self.play(*[FadeIn(prom[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.9))

            # «tiraba información»
            self.en("tiraba")
            self.play(FadeIn(perd, shift=UP * 0.1), run_time=self.dur(0.6))

            # «ge no tira nada»
            self.en("gnada")
            self.pop(gg)
            self.play(FadeIn(suf), run_time=self.dur(0.5))

            # «mirar cómo es el ruido»
            self.en("ruido")
            self.play(FadeIn(nube), run_time=self.dur(0.8))

            # «un resumen a ojo»
            self.en("ojo")
            self.play(FadeIn(oj), Create(no_oj), run_time=self.dur(0.7))
        self.wait(0.2)
