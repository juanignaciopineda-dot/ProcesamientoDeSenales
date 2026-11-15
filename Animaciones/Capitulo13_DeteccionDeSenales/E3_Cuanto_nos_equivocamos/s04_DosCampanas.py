"""Escena 04 — Bajo H1, g es la misma campana corrida en E; todo se reduce a separar dos campanas."""
from comun.escena import *


class DosCampanas(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.bajo_h1()
        self.separar_campanas()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bajo_h1(self):
        L = Lienzo(ancho=7.2, alto=3.2, t_rango=(-7, 16), v_max=1.2, centro=(3.5, -1.0))
        base = eje_g3(L, marcas=(0, 9))
        c1 = casilla_h3(1, "señal + ruido", centro=(-4.0, 3.2))
        rec = formula("r", "=", "s", "+", "W", escala=1.1,
                      colores={0: MEDIDA, 2: SENAL, 4: RUIDO}).move_to([-4.0, 2.1, 0])
        mult = formula("g", "=", r"\sum", "(", "s", "+", "W", ")", "s", escala=1.1,
                       colores={0: ESTIMACION, 4: SENAL, 6: RUIDO, 8: SENAL}).move_to([-4.0, 1.0, 0])
        cuad = formula(r"\sum s^2", "=", "4+4+1", escala=1.0, colores={0: SENAL}).move_to([-4.3, -0.2, 0])
        eneg = formula("=", "E", "=", "9", escala=1.1, colores={1: ESTIMACION, 3: AMBAR}).move_to([-4.6, -1.15, 0])
        parte = formula("+", r"\sum W\,s", escala=1.1, colores={1: RUIDO}).move_to([-4.6, -2.2, 0])
        cam = dens3(L, 0, 3, RUIDO)
        cam_final = dens3(L, 9, 3, SENAL)
        cam0 = dens3(L, 0, 3, RUIDO)
        desvios = VGroup(*[DoubleArrow(L.p(9 - 3, 0.62), L.p(9, 0.62), buff=0, color=ESTIMACION, stroke_width=4,
                                       tip_length=0.18),
                           DoubleArrow(L.p(9, 0.62), L.p(9 + 3, 0.62), buff=0, color=ESTIMACION, stroke_width=4,
                                       tip_length=0.18)])
        tres = VGroup(*[MathTex("3", color=ESTIMACION).scale(0.7).next_to(a, UP, buff=0.05) for a in desvios])

        with self.narrar("b1"):
            # «Bajo la hipótesis uno»
            self.en("h1")
            self.play(FadeIn(c1), run_time=self.dur(0.5))

            # «lo recibido es señal más ruido»
            self.en("recibido")
            self.play(*[FadeIn(rec[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.0))

            # «Al multiplicar por la señal y sumar»
            self.en("mult")
            self.play(LaggedStart(*[FadeIn(mult[i], shift=UP * 0.1) for i in range(9)], lag_ratio=0.12),
                      run_time=self.dur(1.5))

            # «la suma de los cuadrados de la señal»
            self.en("cuadrados")
            self.play(FadeIn(cuad, shift=UP * 0.1), run_time=self.dur(0.9))

            # «que es la energía»
            self.en("eneg")
            self.play(FadeIn(eneg, shift=UP * 0.1), run_time=self.dur(0.7))
            self.play(eneg[3].animate(rate_func=there_and_back).scale(1.4), run_time=self.dur(0.4))

            # «la parte del ruido»
            self.en("parte")
            self.play(FadeIn(parte, shift=UP * 0.1), Create(base.base), Create(cam), run_time=self.dur(0.9))

            # «la misma campana, corrida en nueve»
            self.en("corrida")
            self.play(Transform(cam, cam_final), FadeIn(base.nums[1]), run_time=self.dur(1.2))

            # «el mismo desvío de tres»
            self.en("mismo")
            self.play(*[Create(a) for a in desvios], FadeIn(tres), run_time=self.dur(0.6))

            # «Dos campanas iguales»
            self.en("dos")
            self.play(Create(cam0), run_time=self.dur(0.7))

            # «una en cero y otra en nueve»
            self.en("cerono")
            self.play(FadeIn(base.nums[0]), run_time=self.dur(0.4))
            self.play(Indicate(base.nums[1], color=AMBAR, scale_factor=1.3), run_time=self.dur(0.4))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def separar_campanas(self):
        L = lienzo_g3(centro=(0.0, -1.3))
        base = eje_g3(L, marcas=(0, 9))
        cam0 = dens3(L, 0, 3, RUIDO)
        cam1 = dens3(L, 9, 3, SENAL)
        umb = umbral3(L, 4.5, alto=2.4)
        g45 = MathTex(r"\gamma=4{,}5", color=ESTIMACION).scale(0.8).move_to(L.p(4.5, 0) + DOWN * 0.95)
        mitad = VGroup(
            DoubleArrow(L.p(0, 0) + DOWN * 0.6, L.p(4.5, 0) + DOWN * 0.6, buff=0, color=INK, stroke_width=3, tip_length=0.15),
            DoubleArrow(L.p(4.5, 0) + DOWN * 0.6, L.p(9, 0) + DOWN * 0.6, buff=0, color=INK, stroke_width=3, tip_length=0.15))
        det = self.palabra("detección", AMBAR, 1.0).move_to([-3.6, 3.2, 0])
        sep = DoubleArrow(L.p(0, 1.22), L.p(9, 1.22), buff=0, color=ESTIMACION, stroke_width=5, tip_length=0.22)
        dist = MathTex(r"E=9", color=ESTIMACION).scale(0.9).next_to(sep, UP, buff=0.1)
        cap9 = Text("Capítulo 9", color=INK).scale(0.5).move_to([5.3, 3.3, 0])
        una = Text("una medición", color=TXT).scale(0.5).next_to(cap9, DOWN, buff=0.2)
        esge = MathTex(r"\text{medición}", "=", "g", color=TXT).scale(0.9).move_to([0, -3.5, 0])
        esge[2].set_color(ESTIMACION)

        with self.narrar("b2"):
            # «el umbral, cuatro coma cinco»
            self.en("umbral")
            self.corte()
            self.play(FadeIn(base), Create(cam0), Create(cam1), run_time=self.dur(0.4))
            self.play(Create(umb), FadeIn(g45), run_time=self.dur(0.6))

            # «cae justo en medio»
            self.en("medio")
            self.play(*[Create(a) for a in mitad], run_time=self.dur(0.7))

            # «Todo el problema de detección»
            self.en("todo")
            self.pop(det)

            # «separar dos campanas del mismo ancho»
            self.en("separar")
            self.play(FadeOut(mitad), FadeOut(umb), FadeOut(g45), Create(sep), run_time=self.dur(0.7))

            # «una distancia igual a la energía»
            self.en("distancia")
            self.pop(dist)

            # «el problema del capítulo nueve»
            self.en("cap9")
            self.play(FadeIn(cap9), run_time=self.dur(0.4))

            # «la medición es ge»
            self.en("esge")
            self.play(FadeIn(una), FadeIn(esge, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Más energía, más separadas»
            self.en("maseng")
            self.play(FadeOut(sep), FadeOut(dist),
                      cam1.animate.shift(RIGHT * (L.x(14) - L.x(9))), base.nums[1].animate.shift(RIGHT * (L.x(14) - L.x(9))),
                      run_time=self.dur(1.2))

            # «Más ruido, más anchas»
            self.en("masrui")
            self.play(cam1.animate.shift(LEFT * (L.x(14) - L.x(9))), base.nums[1].animate.shift(LEFT * (L.x(14) - L.x(9))),
                      run_time=self.dur(0.7))
            self.play(Transform(cam0, dens3(L, 0, 4.5, RUIDO)), Transform(cam1, dens3(L, 9, 4.5, SENAL)),
                      run_time=self.dur(0.9))
        self.wait(0.3)
