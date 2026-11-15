"""Escena 12 — Por qué predecir cuesta cuatro veces más que filtrar; los números 0,443 y 0,157 se guardan."""
from comun.escena import *


class CuatroVecesMas(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.parte_razon()
        self.wait(0.6)
        self.parte_guardar()
        self.wait(1.0)
        self.limpiar()

    def parte_razon(self):
        x0 = -4.6
        b_f = barra_h(0.7386, 2.9, x0, 1.5, ESTIMACION)
        l_f = MathTex(r"\text{filtrar}\ 0{,}7386", color=ESTIMACION).scale(0.7).next_to(b_f, RIGHT, buff=0.25)
        b_p = barra_h(2.826, 2.0, x0, 1.5, ERROR)
        l_p = MathTex(r"\text{predecir}\ 2{,}826", color=ERROR).scale(0.7).next_to(b_p, RIGHT, buff=0.25)
        veces = MathTex(r"\times 3{,}8", color=AMBAR).scale(1.0).move_to([5.0, 2.45, 0])
        porque = self.palabra("¿por qué?", AMBAR, 0.8).move_to([4.8, 0.9, 0])

        p_y = np.array([1.6, -0.1, 0.0])
        p_xn = np.array([1.6, -2.2, 0.0])
        p_x1 = np.array([-2.4, -2.2, 0.0])
        d_y = Dot(p_y, radius=0.13, color=SENAL)
        l_y = MathTex(r"y[n]", color=SENAL).scale(0.8).next_to(d_y, UP, buff=0.2)
        d_xn = Dot(p_xn, radius=0.13, color=MEDIDA)
        l_xn = MathTex(r"x[n]", color=MEDIDA).scale(0.8).next_to(d_xn, DOWN, buff=0.2)
        d_x1 = Dot(p_x1, radius=0.13, color=MEDIDA)
        l_x1 = MathTex(r"x[n-1]", color=MEDIDA).scale(0.8).next_to(d_x1, DOWN, buff=0.2)
        directa = Line(p_xn + UP * 0.15, p_y + DOWN * 0.15, color=VERDE, stroke_width=5)
        oj = ojo(TXT).scale(0.8).move_to([4.0, -1.15, 0])
        v_t = MathTex(r"v", color=RUIDO).scale(0.8).move_to([0.2, -1.15, 0])
        v_a = Arrow([0.5, -1.15, 0], [1.4, -1.15, 0], color=RUIDO, buff=0, stroke_width=4,
                    max_tip_length_to_length_ratio=0.3)
        tach_x = tachar(VGroup(d_xn, l_xn))
        a_ex = Arrow(p_x1 + RIGHT * 0.2 + UP * 0.1, p_y + LEFT * 0.2 + DOWN * 0.1, color=AMBAR, buff=0,
                     stroke_width=6, max_tip_length_to_length_ratio=0.1)
        q_ex = self.palabra("?", AMBAR, 0.7).move_to([-0.6, -1.0, 0])
        x06 = MathTex(r"\times 0{,}6", color=AMBAR).scale(0.8).move_to([-1.8, -0.6, 0])
        un_paso = DoubleArrow(p_x1 + DOWN * 0.95 + RIGHT * 0.2, p_xn + DOWN * 0.95 + LEFT * 0.2, color=INK, buff=0,
                              stroke_width=3, tip_length=0.15)
        l_paso = etiqueta("un paso", INK, 0.5).next_to(un_paso, DOWN, buff=0.12)

        with self.narrar("b1"):
            # «Filtrar daba»
            self.en("filtrar")
            self.corte()
            self.play(GrowFromEdge(b_f, LEFT), FadeIn(l_f), run_time=self.dur(0.7))

            # «predecir, dos coma ocho dos seis»
            self.en("predecir")
            self.play(GrowFromEdge(b_p, LEFT), FadeIn(l_p), run_time=self.dur(0.9))

            # «casi cuatro veces más error»
            self.en("veces")
            self.pop(veces)

            # «La razón es sencilla»
            self.en("razon")
            self.pop(porque)

            # «una mirada directa»
            self.en("mirada")
            self.play(FadeIn(d_y), FadeIn(l_y), FadeIn(d_xn), FadeIn(l_xn), run_time=self.dur(0.5))
            self.play(Create(directa), FadeIn(oj, shift=LEFT * 0.3), run_time=self.dur(0.5))

            # «aunque ruidosa»
            self.en("ruidosa")
            self.play(FadeIn(v_t), GrowArrow(v_a), run_time=self.dur(0.5))

            # «Sin ella»
            self.en("sin")
            self.play(FadeIn(d_x1), FadeIn(l_x1), Create(tach_x), FadeOut(oj), run_time=self.dur(0.6))

            # «extrapolar desde el pasado»
            self.en("extra")
            self.play(GrowArrow(a_ex), FadeIn(q_ex), run_time=self.dur(0.7))

            # «se acuerda un cero coma seis»
            self.en("acuerda")
            self.play(FadeIn(x06), run_time=self.dur(0.4))

            # «de lo anterior»
            self.en("anterior")
            self.play(a_ex.animate.set_stroke(width=2.5), run_time=self.dur(0.5))

            # «Un paso de extrapolación»
            self.en("paso")
            self.play(GrowFromCenter(un_paso), FadeIn(l_paso), run_time=self.dur(0.5))

            # «ya cuesta mucho»
            self.en("cuesta")
            self.play(a_ex.animate.set_color(ERROR), run_time=self.dur(0.4))
            self.resaltar(a_ex, color=ERROR)

    def parte_guardar(self):
        c1 = RoundedRectangle(corner_radius=0.12, width=1.9, height=0.9, color=AMBAR, stroke_width=3.5).move_to([-3.6, 2.2, 0])
        c2 = RoundedRectangle(corner_radius=0.12, width=1.9, height=0.9, color=AMBAR, stroke_width=3.5).move_to([-0.8, 2.2, 0])
        v1 = MathTex(r"0{,}443", color=AMBAR).scale(0.8).move_to(c1)
        v2 = MathTex(r"0{,}157", color=AMBAR).scale(0.8).move_to(c2)
        pred = formula(r"\frac{0{,}443\,z^{-1}}{1-0{,}157\,z^{-1}}", escala=0.9).move_to([-2.2, 0.2, 0])
        lbl_p = etiqueta("el predictor", INK, 0.5).next_to(pred, DOWN, buff=0.3)
        cand = candado(AMBAR).scale(0.8).move_to([3.0, 2.2, 0])
        e7 = etiqueta("E7", AMBAR, 0.7).move_to([3.0, 1.35, 0])
        sit = self.palabra("?", AMBAR, 1.2).move_to([4.7, 2.2, 0])
        cajas = [RoundedRectangle(corner_radius=0.12, width=3.6, height=1.0, color=AMBAR, stroke_width=3.5)
                 .move_to([x, -2.0, 0]) for x in (-4.2, 0.0, 4.2)]
        t_p = Text("predecir", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(cajas[0])
        t_f = Text("filtrar", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(cajas[1])
        t_s = Text("suavizar", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(cajas[2])

        with self.narrar("b2"):
            # «Guarda dos números»
            self.en("guarda")
            self.corte()
            self.play(Create(c1), Create(c2), run_time=self.dur(0.5))

            # «cero coma cuatro cuatro tres»
            self.en("n443")
            self.pop(v1)

            # «cero coma uno cinco siete»
            self.en("n157")
            self.pop(v2)

            # «los del predictor»
            self.en("predictor")
            self.play(FadeIn(pred), FadeIn(lbl_p), run_time=self.dur(0.7))

            # «Volverán en el último episodio»
            self.en("vuelven")
            self.play(FadeIn(cand, scale=0.7), FadeIn(e7), run_time=self.dur(0.5))

            # «en un sitio en el que no los esperas»
            self.en("sitio")
            self.pop(sit)

            # «Ahora tenemos casi todo»
            self.en("casi")
            self.play(FadeOut(pred), FadeOut(lbl_p), FadeOut(cand), FadeOut(e7), FadeOut(sit), run_time=self.dur(0.5))

            # «comparar de una vez»
            self.en("comparar")
            self.play(*[Create(c) for c in cajas], run_time=self.dur(0.7))

            # «predecir, filtrar»
            self.en("pf")
            self.play(FadeIn(t_p), FadeIn(t_f), run_time=self.dur(0.5))

            # «suavizar»
            self.en("suav")
            self.play(FadeIn(t_s), run_time=self.dur(0.4))
