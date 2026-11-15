"""Escena 03 — ¿Cuántas muestras hacen falta? El error baja y se aplana; dos razones."""
from comun.escena import *


class CuantoPasadoHaceFalta(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.barras()
        self.razones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def barras(self):
        vals = [4, 0.8, 0.74, 0.7387, 0.7386, 0.7386, 0.7386]
        rots = ["0", "1", "2", "3", "4", "5", "10"]
        B = barras_error(vals, rots, centro=(0.0, -0.8), ancho=9.0, alto=3.6, v_max=4.0)
        titulo_q = Text("¿Cuántas muestras hacen falta?", color=TXT, weight=BOLD).scale(0.91).move_to([0, 3.2, 0])
        ejeL = MathTex("L", color=INK).scale(1.04).next_to(B.base, RIGHT, buff=0.2)
        err = MathTex(r"\text{error}", color=ERROR).scale(0.91).move_to([-5.6, 2.0, 0])
        y_lin = B.base.get_center()[1] + 0.7386 / 4.0 * 3.6
        linea = DashedLine([-4.5, y_lin, 0], [4.5, y_lin, 0], color=AMBAR, stroke_width=3)
        lim = MathTex(r"0{,}7386", color=AMBAR).scale(0.91).next_to(linea, UP, buff=0.12).shift(RIGHT * 3.2)
        menos = Text("cada vez menos", color=INK).scale(0.72).move_to([3.0, 1.6, 0])

        with self.narrar("b1"):
            # «¿Cuántas muestras hacen falta?»
            self.en("pregunta")
            self.corte()
            self.play(FadeIn(titulo_q), Create(B.base), FadeIn(ejeL), FadeIn(err), run_time=self.dur(0.6))
            # «Sin mirar ninguna» / «el error es cuatro»
            self.en("cero")
            self.play(GrowFromEdge(B.barras[0], DOWN), FadeIn(B.etiquetas[0]), run_time=self.dur(0.5))
            self.en("e4")
            self.play(FadeIn(B.valores_txt[0]), run_time=0.3)
            # «Con una muestra» / «cero coma ocho»
            self.en("una")
            self.play(GrowFromEdge(B.barras[1], DOWN), FadeIn(B.etiquetas[1]), run_time=self.dur(0.5))
            self.en("e08")
            self.play(FadeIn(B.valores_txt[1]), run_time=0.3)
            # «Con dos» / «cero coma siete cuatro cero»
            self.en("dos")
            self.play(GrowFromEdge(B.barras[2], DOWN), FadeIn(B.etiquetas[2]), run_time=self.dur(0.5))
            self.en("e074")
            self.play(FadeIn(B.valores_txt[2]), run_time=0.3)
            # «Con tres» / «cero coma siete tres ocho siete»
            self.en("tres")
            self.play(GrowFromEdge(B.barras[3], DOWN), FadeIn(B.etiquetas[3]), run_time=self.dur(0.5))
            self.en("e0738")
            self.play(FadeIn(B.valores_txt[3]), run_time=0.3)
            # «Y con cuatro, cinco, diez»
            self.en("mas")
            self.play(*[GrowFromEdge(B.barras[i], DOWN) for i in (4, 5, 6)],
                      *[FadeIn(B.etiquetas[i]) for i in (4, 5, 6)], run_time=self.dur(0.6))
            # «cero coma siete tres ocho seis»
            self.en("limite")
            self.play(Create(linea), FadeIn(lim), run_time=self.dur(0.7))
            # «deja de bajar»
            self.en("plana")
            self.resaltar(linea, color=VERDE, run_time=0.5)
            # «Añadir muestras sirve cada vez menos»
            self.en("menos")
            self.play(FadeIn(menos), run_time=0.4)

    # ------------------------------------------------------------------ b2
    def razones(self):
        n1 = self.palabra("1", AMBAR, 1.2).move_to([-6.0, 2.4, 0])
        n2 = self.palabra("2", AMBAR, 1.2).move_to([-6.0, -0.9, 0])
        f = formula(r"\text{error}(L+1)", r"\le", r"\text{error}(L)", colores={0: ERROR, 2: ERROR}).move_to([0.3, 2.4, 0])
        tl = tilde(VERDE, 0.4).next_to(f, RIGHT, buff=0.4)
        fila = FilaMuestras([r"h_0", r"h_1"], centro=(-0.5, 0.9), lado=1.38, color=ESTIMACION, escala=1.04)
        nueva = FilaMuestras([r"h_2"], centro=(1.15, 0.9), lado=1.38, color=ESTIMACION, escala=1.04)
        cero_t = MathTex("0", color=AMBAR).scale(1.04).move_to(nueva.rots[0])
        pasos = FilaMuestras([r"n-5", r"n-4", r"n-3", r"n-2", r"n-1", r"n"], centro=(0.8, -0.9), lado=1.44,
                             color=MEDIDA, escala=0.91)
        flechas = VGroup(*[CurvedArrow(pasos.cas[i + 1].get_top() + UP * 0.05, pasos.cas[i].get_top() + UP * 0.05,
                                        angle=PI / 2.5, color=INK, stroke_width=3, tip_length=0.15)
                           for i in range(5)])
        por = VGroup(*[Text("×0,6", color=INK).scale(0.42).move_to(flechas[i].get_top() + UP * 0.2)
                       for i in range(5)])
        quinta = MathTex(r"0{,}6^5", color=AMBAR).scale(1.30).move_to([-1.4, -2.9, 0])
        ocho = MathTex(r"\approx 8\,\%", color=AMBAR).scale(1.30).next_to(quinta, RIGHT, buff=0.3)

        with self.narrar("b2"):
            # «Dos razones»
            self.en("razones")
            self.corte()
            self.play(FadeIn(n1), FadeIn(n2), run_time=0.4)
            # «La primera»
            self.en("primera")
            self.play(n2.animate.fade(0.7), run_time=0.3)
            # «añadir una muestra nunca empeora nada»
            self.en("nuncaempeora")
            self.play(LaggedStart(*[FadeIn(f[i]) for i in range(3)], lag_ratio=0.4), run_time=self.dur(0.9))
            self.play(FadeIn(tl), run_time=0.3)
            # «el filtro nuevo puede imitar al anterior»
            self.en("imitar")
            self.play(FadeIn(fila), run_time=0.4)
            self.play(FadeIn(nueva), run_time=self.dur(0.4))
            # «poniendo a cero el coeficiente extra»
            self.en("cerocoef")
            self.play(Transform(nueva.rots[0], cero_t), run_time=0.4)
            # «La segunda»
            self.en("segunda")
            self.play(FadeOut(f), FadeOut(tl), FadeOut(fila), FadeOut(nueva),
                      n1.animate.fade(0.7), n2.animate.set_opacity(1.0).move_to([-6.0, 0.3, 0]), run_time=0.4)
            # «la temperatura recuerda cero coma seis por paso»
            self.en("recuerda")
            self.play(FadeIn(pasos), run_time=0.4)
            self.play(LaggedStart(*[Create(a) for a in flechas], lag_ratio=0.2),
                      LaggedStart(*[FadeIn(p) for p in por], lag_ratio=0.2), run_time=self.dur(1.0))
            # «lo que pasó hace cinco pasos»
            self.en("cinco")
            self.play(pasos.cas[0].animate.set_stroke(AMBAR), run_time=0.4)
            # «cero coma seis a la quinta»
            self.en("quinta")
            self.pop(quinta)
            # «unos ocho por ciento»
            self.en("ocho")
            self.play(FadeIn(ocho), run_time=0.4)
            # «casi no dice nada de hoy»
            self.en("nada")
            self.play(VGroup(pasos.cas[0], pasos.rots[0]).animate.fade(0.7), run_time=0.5)
