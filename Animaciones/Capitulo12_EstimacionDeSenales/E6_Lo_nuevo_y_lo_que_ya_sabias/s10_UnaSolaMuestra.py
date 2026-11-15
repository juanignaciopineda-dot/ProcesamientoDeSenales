"""Escena 10 — Predecir con una sola muestra: h = 2,4 / 5 = 0,48, error 2,848."""
from comun.escena import *


class UnaSolaMuestra(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        fila = FilaMuestras([r"x[n{-}1]"], centro=(-5.0, 3.0), lado=1.5, color=MEDIDA, escala=0.65)
        h1 = formula("h", "=", escala=1.0, colores={0: ESTIMACION}).move_to([-5.6, 1.3, 0])
        fr1 = fraccion(MathTex(r"C_{yx}[1]", color=TXT).scale(0.9), MathTex(r"C_{xx}[0]", color=TXT).scale(0.9))
        fr1.move_to([-3.6, 1.3, 0])
        oculta(fr1)
        ig2 = MathTex(r"=", color=TXT).scale(0.9).move_to([-2.1, 1.3, 0])
        fr2 = fraccion(MathTex(r"2{,}4", color=TXT).scale(0.9), MathTex(r"5", color=TXT).scale(0.9))
        fr2.move_to([-1.0, 1.3, 0])
        oculta(fr2)
        res = MathTex(r"=\,0{,}48", color=ESTIMACION).scale(1.0).move_to([0.8, 1.3, 0])

        E = formula(r"\text{error}", "=", "4", "-", r"2{,}4", r"\cdot", r"0{,}48", "=", r"2{,}848",
                    escala=1.0, colores={0: ERROR, 8: ERROR}).move_to([-0.8, -0.2, 0])
        oculta(E)

        x0 = -2.4
        l_f = etiqueta("filtrar, una muestra", ESTIMACION, 0.5).move_to([-5.0, -1.7, 0])
        l_p = etiqueta("predecir, una muestra", ERROR, 0.5).move_to([-5.0, -2.7, 0])
        b_f = barra_h(0.8, -1.7, x0, 1.6, ESTIMACION)
        b_p = barra_h(2.848, -2.7, x0, 1.6, ERROR)
        v_f = MathTex(r"0{,}8", color=ESTIMACION).scale(0.8).next_to(b_f, RIGHT, buff=0.2)
        v_p = MathTex(r"2{,}848", color=ERROR).scale(0.8).next_to(b_p, RIGHT, buff=0.2)

        with self.narrar("b1"):
            # «Con una sola muestra»
            self.en("una")
            self.play(FadeIn(fila), run_time=self.dur(0.5))

            # «la anterior»
            self.en("anterior")
            self.resaltar(fila.cas[0], color=AMBAR)

            # «la correlación cruzada a un paso»
            self.en("cruz")
            self.add(fr1, fr2, E)
            self.play(FadeIn(h1), *revelar(fr1.num), run_time=self.dur(0.8))
            self.play(*revelar(fr1.barra, fr1.den), run_time=self.dur(0.5))

            # «dos coma cuatro, entre»
            self.en("n24")
            self.play(FadeIn(ig2), *revelar(fr2.num, fr2.barra), run_time=self.dur(0.6))

            # «de lo medido»
            self.en("medido")
            self.play(fr1.den.animate.set_color(MEDIDA), run_time=self.dur(0.4))

            # «cinco»
            self.en("n5")
            self.play(*revelar(fr2.den), run_time=self.dur(0.4))

            # «cero coma cuatro ocho. Y el error»
            self.en("h048")
            self.pop(res)

            # «el error»
            self.en("err")
            self.play(*revelar(E[0], E[1]), run_time=self.dur(0.5))

            # «cuatro menos dos coma cuatro por cero coma cuatro ocho»
            self.en("cuenta")
            self.play(LaggedStart(*[a.animate.set_opacity(1) for a in E[2:7]], lag_ratio=0.3), run_time=self.dur(1.5))

            # «dos coma ocho cuatro ocho»
            self.en("e2848")
            self.play(*revelar(E[7], E[8]), run_time=self.dur(0.6))

            # «el cero coma ocho de filtrar con una muestra»
            self.en("cmp")
            self.play(FadeIn(l_f), GrowFromEdge(b_f, LEFT), FadeIn(v_f), run_time=self.dur(0.8))

            # «es mucho más»
            self.en("mucho")
            self.play(FadeIn(l_p), GrowFromEdge(b_p, LEFT), FadeIn(v_p), run_time=self.dur(0.8))

        self.wait(1.0)
        self.limpiar()
