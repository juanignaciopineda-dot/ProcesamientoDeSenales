"""Escena 08 — El error total con prior 0,2 es 0,0498, mejor que el 0,0668 del umbral sin prior."""
from comun.escena import *


class ElErrorConPrior(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.media_ponderada()
        self.mismo_detector()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def media_ponderada(self):
        pe = formula("P_e", "=", "p_0", "P_{FA}", "+", "p_1", "P_M", escala=1.5,
                     colores={0: ESTIMACION, 2: RUIDO, 3: ERROR, 5: SENAL, 6: ERROR}).move_to([0, 2.5, 0])
        f2 = formula("=", "0{,}8", r"\cdot", "0{,}0249", "+", "0{,}2", r"\cdot", "0{,}1497", escala=1.4,
                     colores={1: AMBAR, 3: ERROR, 5: AMBAR, 7: ERROR}).move_to([0, 0.8, 0])
        f3 = formula("=", "0{,}0199", "+", "0{,}0299", escala=1.4).move_to([0, -0.8, 0])
        f4 = formula("P_e", "=", "0{,}0498", r"\approx", r"5\,\%", escala=1.6,
                     colores={0: ESTIMACION, 2: VERDE, 4: VERDE}).move_to([0, -2.5, 0])
        marco = SurroundingRectangle(f4, color=VERDE, buff=0.25, stroke_width=4)

        with self.narrar("b1"):
            # «La probabilidad de error es la media ponderada»
            self.en("pe")
            self.play(Write(pe), run_time=self.dur(1.4))

            # «cero coma ocho por cero coma cero dos cuatro nueve»
            self.en("t1")
            self.play(*[FadeIn(f2[i], shift=UP * 0.1) for i in range(4)], run_time=self.dur(1.2))

            # «más cero coma dos»
            self.en("t2")
            self.play(*[FadeIn(f2[i], shift=UP * 0.1) for i in (4, 5, 6)], run_time=self.dur(0.8))

            # «cero coma uno cuatro nueve siete»
            self.en("t2b")
            self.play(FadeIn(f2[7], shift=UP * 0.1), run_time=self.dur(0.7))

            # «Cero coma cero uno nueve nueve»
            self.en("r1")
            self.play(FadeIn(f3[0]), FadeIn(f3[1], shift=UP * 0.1), run_time=self.dur(0.7))

            # «más cero coma cero dos nueve nueve»
            self.en("r2")
            self.play(FadeIn(f3[2]), FadeIn(f3[3], shift=UP * 0.1), run_time=self.dur(0.7))

            # «casi cinco por ciento»
            self.en("res")
            self.play(Write(f4), Create(marco), run_time=self.dur(1.0))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def mismo_detector(self):
        L = lienzo_g3(centro=(0.0, -1.5))
        base = eje_g3(L, marcas=(0, 9))
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        umb = umbral3(L, 5.886, alto=2.0)
        cola_d = cola3(L, 0, 3, 5.886, 17)
        cola_i = cola3(L, 9, 3, -8, 5.886)
        pfa = MathTex("P_{FA}", color=ERROR).scale(0.8).move_to(L.p(8.0, 0) + DOWN * 0.9)
        pm = MathTex("P_M", color=ERROR).scale(0.8).move_to(L.p(2.2, 0) + DOWN * 0.9)
        v1 = MathTex("0{,}0668", color=ERROR).scale(0.8).move_to(L.p(8.0, 0) + DOWN * 0.9)
        v2 = MathTex("0{,}0668", color=ERROR).scale(0.8).move_to(L.p(2.2, 0) + DOWN * 0.9)
        err = formula("0{,}8", r"\cdot", "0{,}0668", "+", "0{,}2", r"\cdot", "0{,}0668", "=", r"6{,}7\,\%", escala=1.0,
                      colores={8: ERROR}).move_to([0, 3.4, 0])
        peor = formula(r"6{,}7\,\%", ">", r"5\,\%", escala=1.2, colores={0: ERROR, 2: VERDE}).move_to([0, 2.4, 0])
        c_calc = caja("calcular g", ESTIMACION, ancho=2.8, alto=0.8, scale=0.5).move_to([-2.6, 3.0, 0])
        c_comp = caja("comparar con γ", ESTIMACION, ancho=3.2, alto=0.8, scale=0.5).move_to([1.8, 3.0, 0])
        flecha_c = Arrow(c_calc.get_right(), c_comp.get_left(), buff=0.1, color=INK, stroke_width=4)
        p1 = MathTex("p_1=0{,}2", color=SENAL).scale(0.85).move_to([3.6, 1.6, 0])
        rebaja = VGroup(Text("6,7 %", color=ERROR).scale(0.6), Arrow(ORIGIN, DOWN * 0.6, buff=0, color=VERDE, stroke_width=6),
                        Text("5 %", color=VERDE, weight=BOLD).scale(0.6)).arrange(DOWN, buff=0.12).move_to([5.9, 2.9, 0])

        with self.narrar("b2"):
            # «¿Y si hubiéramos dejado el umbral»
            self.en("vuelta")
            self.corte()
            self.play(FadeIn(base), Create(cam0), Create(cam1), FadeIn(umb), FadeIn(cola_d), FadeIn(cola_i),
                      run_time=self.dur(0.7))

            # «en cuatro coma cinco»
            self.en("c45")
            self.play(umb.animate.shift(LEFT * (L.x(5.886) - L.x(4.5))),
                      Transform(cola_d, cola3(L, 0, 3, 4.5, 17)), Transform(cola_i, cola3(L, 9, 3, -8, 4.5)),
                      run_time=self.dur(1.0))

            # «Cada probabilidad»
            self.en("cada")
            self.play(cola_d.animate(rate_func=there_and_back).set_fill(ERROR, 0.95),
                      cola_i.animate(rate_func=there_and_back).set_fill(ERROR, 0.95), run_time=self.dur(0.8))

            # «cero coma cero seis seis ocho»
            self.en("val")
            self.play(FadeIn(v1), FadeIn(v2), run_time=self.dur(0.6))

            # «el error sería seis coma siete por ciento»
            self.en("error")
            self.play(Write(err), run_time=self.dur(1.8))

            # «Peor que el cinco por ciento»
            self.en("peor")
            self.play(FadeIn(peor, shift=UP * 0.1), run_time=self.dur(0.7))

            # «Es el mismo detector»
            self.en("mismo")
            self.play(FadeOut(err), FadeOut(peor), run_time=self.dur(0.3))
            self.play(FadeIn(c_calc), FadeIn(c_comp), Create(flecha_c), run_time=self.dur(0.7))

            # «calcular ge y compararlo»
            self.en("calc")
            self.play(c_calc[0].animate(rate_func=there_and_back).set_stroke(AMBAR, width=8),
                      c_comp[0].animate(rate_func=there_and_back).set_stroke(AMBAR, width=8), run_time=self.dur(1.0))

            # «solo hemos movido la marca»
            self.en("movida")
            self.play(umb.animate.shift(RIGHT * (L.x(5.886) - L.x(4.5))),
                      Transform(cola_d, cola3(L, 0, 3, 5.886, 17)), Transform(cola_i, cola3(L, 9, 3, -8, 5.886)),
                      run_time=self.dur(1.0))

            # «usando lo que sabíamos de antemano»
            self.en("antemano")
            self.play(FadeIn(p1, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Y rebaja el error»
            self.en("rebaja")
            self.play(FadeIn(rebaja, shift=DOWN * 0.1), run_time=self.dur(0.7))
        self.wait(0.3)
