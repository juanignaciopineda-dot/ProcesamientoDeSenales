"""Escena 15 — La respuesta: la muestra de ahora vale más que todo el futuro, y el orden de los errores."""
from comun.escena import *


class LaRespuesta(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        ys = [2.5, 1.5, 0.5, -0.5]
        x0, esc = -3.4, 1.0
        nombres = ["sin datos", "predicción", "filtrado", "suavizado"]
        rots = [Text(n, color=TXT, weight=BOLD).scale(0.5).move_to([-5.7, y, 0]) for n, y in zip(nombres, ys)]
        vals = [4.0, 2.826, 0.7386, 0.686]
        colores = [INK, ERROR, ESTIMACION, VERDE]
        barras = [barra_h(v, y, x0, esc, c) for v, y, c in zip(vals, ys, colores)]
        txt_v = [r"4", r"2{,}826", r"0{,}7386", r"0{,}686"]
        etqs = [MathTex(s, color=c).scale(0.7).next_to(b, RIGHT, buff=0.2) for s, b, c in zip(txt_v, barras, colores)]
        grupo = VGroup(*rots, *barras, *etqs)

        let_a = self.palabra("A", VERDE, 2.0).move_to([5.6, 2.6, 0])
        tk = tilde(VERDE, 0.8).next_to(let_a, DOWN, buff=0.3)
        a_dos = Arrow([3.4, ys[1] - 0.15, 0], [3.4, ys[2] + 0.15, 0], color=ERROR, buff=0, stroke_width=4,
                      max_tip_length_to_length_ratio=0.3)
        t_dos = MathTex(r"-2{,}09", color=ERROR).scale(0.8).move_to([4.5, (ys[1] + ys[2]) / 2, 0])
        a_cin = Arrow([3.4, ys[2] - 0.15, 0], [3.4, ys[3] + 0.15, 0], color=VERDE, buff=0, stroke_width=4,
                      max_tip_length_to_length_ratio=0.5)
        t_cin = MathTex(r"-0{,}05", color=VERDE).scale(0.8).move_to([4.5, (ys[2] + ys[3]) / 2, 0])

        bal = Balanza(centro=(0, -2.3), semi=1.6)
        sq_i = Square(side_length=0.5, color=MEDIDA, stroke_width=3).set_fill(MEDIDA, 0.35).move_to([-1.6, -2.75, 0])
        sqs_d = VGroup(*[Square(side_length=0.26, color=INK, stroke_width=2).set_fill(INK, 0.3)
                         .move_to([1.6 + (i - 2.5) * 0.31, -2.85, 0]) for i in range(6)])
        l_ahora = Text("ahora", color=MEDIDA, weight=BOLD).scale(0.5).move_to([-1.6, -1.6, 0])
        l_futuro = Text("futuro", color=INK, weight=BOLD).scale(0.5).move_to([1.6, -1.6, 0])

        cad = formula(r"\text{suavizado}", r"\le", r"\text{filtrado}", r"\le", r"\text{predicción}", r"\le",
                      r"\text{varianza}", escala=0.95, colores={0: VERDE, 2: ESTIMACION, 4: ERROR}).move_to([0, 2.0, 0])
        oculta(cad)
        marco = SurroundingRectangle(cad, color=AMBAR, buff=0.3, stroke_width=4)
        mas = Text("más datos, menos error", color=AMBAR, weight=BOLD).scale(0.7).move_to([0, 0.6, 0])

        with self.narrar("b1"):
            # «la A, y de lejos»
            self.en("resp")
            self.corte()
            self.add(cad)
            self.play(FadeIn(grupo, lag_ratio=0.05), run_time=self.dur(0.7))
            self.pop(let_a)
            self.play(FadeIn(tk), run_time=self.dur(0.4))

            # «Pasar de predecir a filtrar»
            self.en("paf")
            self.resaltar(barras[1], barras[2], color=AMBAR)

            # «más de dos unidades»
            self.en("dos")
            self.play(GrowArrow(a_dos), FadeIn(t_dos), run_time=self.dur(0.6))

            # «solo cinco centésimas»
            self.en("cinco")
            self.play(GrowArrow(a_cin), FadeIn(t_cin), run_time=self.dur(0.6))

            # «vale más que todo el futuro junto»
            self.en("vale")
            self.play(FadeIn(bal), FadeIn(sq_i), FadeIn(sqs_d), FadeIn(l_ahora), FadeIn(l_futuro), run_time=self.dur(0.5))
            dy = bal.semi * np.sin(0.22)
            self.play(*bal.inclinar("izq"), sq_i.animate.shift(DOWN * dy), sqs_d.animate.shift(UP * dy),
                      run_time=self.dur(0.8))

            # «el orden se cumple siempre»
            self.en("orden")
            self.play(FadeOut(bal), FadeOut(sq_i), FadeOut(sqs_d), FadeOut(l_ahora), FadeOut(l_futuro),
                      FadeOut(a_dos), FadeOut(t_dos), FadeOut(a_cin), FadeOut(t_cin), FadeOut(let_a), FadeOut(tk),
                      grupo.animate.shift(DOWN * 2.7), run_time=self.dur(0.7))

            # «el suavizado es menor o igual que el filtrado»
            self.en("suavfilt")
            self.play(*revelar(cad[0], cad[1], cad[2]), run_time=self.dur(0.8))

            # «este que la predicción»
            self.en("filtpred")
            self.play(*revelar(cad[3], cad[4]), run_time=self.dur(0.6))

            # «esta que la varianza»
            self.en("predvar")
            self.play(*revelar(cad[5], cad[6]), run_time=self.dur(0.6))

            # «Más datos, menos error»
            self.en("masdatos")
            self.play(Create(marco), FadeIn(mas), run_time=self.dur(0.7))

        self.wait(1.0)
        self.limpiar()
