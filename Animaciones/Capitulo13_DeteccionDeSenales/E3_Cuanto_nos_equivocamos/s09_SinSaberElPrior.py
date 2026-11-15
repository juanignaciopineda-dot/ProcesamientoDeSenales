"""Escena 09 — Sin conocer el prior: Neyman-Pearson con P_FA = 1 %: umbral 6,98 y P_D = 0,75."""
from comun.escena import *


class SinSaberElPrior(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.L = lienzo_g3(centro=(0.0, -1.5))
        L = self.L
        self.base = eje_g3(L, marcas=(0, 9))
        self.cam0 = dens3(L, 0, 3, RUIDO)
        self.cam1 = dens3(L, 9, 3, SENAL)
        self.umb = umbral3(L, 4.5, alto=2.0)
        self.problema()
        self.buscar_umbral()
        self.cuantos_detectamos()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def problema(self):
        L = self.L
        p1 = formula("p_1", "=", "0{,}2", escala=1.1, colores={0: SENAL, 2: AMBAR}).move_to([-4.6, 3.2, 0])
        tacha = Line(p1.get_corner(DL), p1.get_corner(UR), color=ERROR, stroke_width=6)
        p1q = formula("p_1", "=", "?", escala=1.1, colores={0: SENAL, 2: ERROR}).move_to([-4.6, 3.2, 0])
        ant = antena(TXT).scale(1.0).move_to([-5.6, 1.0, 0])
        cielo = VGroup(*[VGroup(avion(INK).scale(0.5), Text("?", color=AMBAR, weight=BOLD).scale(0.5)).arrange(RIGHT, buff=0.1)
                         for _ in range(3)]).arrange(RIGHT, buff=0.7).move_to([0.8, 3.2, 0])
        cap9 = Text("Capítulo 9", color=INK).scale(0.5).move_to([5.7, 3.4, 0])
        np_t = Text("Neyman-Pearson", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([5.0, 2.5, 0])
        tol = formula("P_{FA}", r"\le", r"1\,\%", escala=1.1, colores={0: ERROR, 2: AMBAR}).move_to([-2.4, 2.1, 0])
        pequena = cola3(L, 0, 3, 6.979, 17)
        uno = Text("1 %", color=ERROR, weight=BOLD).scale(0.55).move_to(L.p(8.6, 0.6))
        detecta = cola3(L, 9, 3, 6.979, 17, VERDE, 0.5)

        with self.narrar("b1"):
            # «Hay un problema»
            self.en("problema")
            self.play(FadeIn(self.base), Create(self.cam0), Create(self.cam1), FadeIn(self.umb), run_time=self.dur(0.7))
            self.play(FadeIn(p1, shift=UP * 0.1), run_time=self.dur(0.4))
            self.play(Create(tacha), run_time=self.dur(0.3))

            # «Para poner el umbral»
            self.en("poner")
            self.play(self.umb.animate.shift(RIGHT * (L.x(5.886) - L.x(4.5))), run_time=self.dur(0.9))

            # «saber la probabilidad de que haya un avión»
            self.en("saber")
            self.play(FadeOut(p1), FadeOut(tacha), FadeIn(p1q), FadeIn(ant), run_time=self.dur(0.6))

            # «¿Y si no la sabemos?»
            self.en("nosabemos")
            self.play(p1q.animate(rate_func=there_and_back).scale(1.25), run_time=self.dur(0.7))

            # «En un radar»
            self.en("enradar")
            self.play(Create(ant.ondas.set_color(TXT)), run_time=self.dur(0.6))

            # «¿cuántos aviones vendrán hoy?»
            self.en("hoy")
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in cielo], lag_ratio=0.3), run_time=self.dur(1.2))

            # «Del capítulo nueve»
            self.en("cap9")
            self.play(FadeIn(cap9), run_time=self.dur(0.4))

            # «Neyman-Pearson»
            self.en("np")
            self.pop(np_t)

            # «cuántas falsas alarmas se toleran»
            self.en("toleran")
            self.play(FadeIn(tol, shift=UP * 0.1), run_time=self.dur(0.8))

            # «un uno por ciento»
            self.en("uno")
            self.play(FadeIn(pequena), FadeIn(uno), run_time=self.dur(0.6))

            # «detecta más aviones»
            self.en("detecta")
            self.play(FadeIn(detecta), run_time=self.dur(0.7))
        self.wait(0.3)
        self.b1 = [p1q, ant, cielo, cap9, np_t, tol, detecta, uno]
        self.pequena = pequena

    # ------------------------------------------------------------ b2
    def buscar_umbral(self):
        L = self.L
        inv = MathTex(r"Q^{-1}", color=ESTIMACION).scale(1.4).move_to([-4.6, 3.2, 0])
        area = formula(r"\text{área}\ 0{,}01", r"\to", "x", escala=1.0, colores={0: ERROR, 2: AMBAR}).move_to([-4.3, 2.2, 0])
        z = formula(r"Q^{-1}(0{,}01)", "=", "2{,}33", escala=1.0, colores={2: AMBAR}).move_to([-4.3, 1.2, 0])
        prod = formula(r"\gamma", "=", "3", r"\cdot", "2{,}33", escala=1.0, colores={0: ESTIMACION}).move_to([-4.6, 0.2, 0])
        gam = formula("=", "6{,}98", escala=1.1, colores={1: AMBAR}).move_to([-4.6, -0.7, 0])
        uno = Text("1 %", color=ERROR, weight=BOLD).scale(0.55).move_to(L.p(8.6, 0.6))

        with self.narrar("b2"):
            # «el umbral que deja un uno por ciento de cola»
            self.en("busca")
            self.play(*[FadeOut(m) for m in self.b1 if m not in (self.b1[6], self.b1[7])], run_time=self.dur(0.4))
            self.play(self.umb.animate.shift(RIGHT * (L.x(6.979) - L.x(5.886))), run_time=self.dur(0.9))

            # «en la campana de la hipótesis cero»
            self.en("encero")
            self.play(self.cam0.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.8))

            # «la operación inversa de cu»
            self.en("inversa")
            self.pop(inv)

            # «dado un área, qué punto la deja»
            self.en("area")
            self.play(FadeIn(area, shift=UP * 0.1), run_time=self.dur(0.8))

            # «Para un uno por ciento»
            self.en("para1")
            self.play(self.pequena.animate(rate_func=there_and_back).set_fill(ERROR, 0.95), run_time=self.dur(0.8))

            # «dos coma tres tres desvíos»
            self.en("z233")
            self.play(FadeIn(z, shift=UP * 0.1), run_time=self.dur(1.0))

            # «tres por dos coma tres tres»
            self.en("prod")
            self.play(*[FadeIn(prod[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.2))

            # «seis coma nueve ocho»
            self.en("gam")
            self.play(FadeIn(gam, shift=UP * 0.1), run_time=self.dur(0.7))
        self.wait(0.3)
        self.b2 = [inv, area, z, prod, gam]

    # ------------------------------------------------------------ b3
    def cuantos_detectamos(self):
        L = self.L
        pd_q = formula("P_D", "=", "?", escala=1.3, colores={0: VERDE, 2: AMBAR}).move_to([-4.6, 3.2, 0])
        en9 = Text("media 9 · desvío 3", color=SENAL).scale(0.55).move_to([0.9, 1.9, 0])
        est = formula("(", "6{,}98", "-", "9", ")", "/", "3", escala=1.1).move_to([-4.3, 2.2, 0])
        zz = formula("=", "-0{,}67", escala=1.1, colores={1: AMBAR}).move_to([-3.5, 1.2, 0])
        pd = formula("P_D", "=", "Q(-0{,}67)", "=", "0{,}75", escala=1.0,
                     colores={0: VERDE, 4: VERDE}).move_to([-3.7, 0.0, 0])
        aviones = VGroup(*[avion(VERDE if i < 3 else ERROR).scale(0.5) for i in range(4)]).arrange(RIGHT, buff=0.4)
        aviones.move_to([4.4, 2.9, 0])
        fa1 = formula("P_{FA}", "=", r"1\,\%", escala=0.95, colores={0: ERROR}).move_to([4.2, 1.6, 0])
        pd75 = formula("P_D", "=", r"75\,\%", escala=0.95, colores={0: VERDE, 2: VERDE}).move_to([4.2, 0.8, 0])

        with self.narrar("b3"):
            # «¿cuántos aviones detectamos con ese umbral?»
            self.en("cuantos")
            self.play(*[FadeOut(m) for m in self.b2], run_time=self.dur(0.4))
            self.pop(pd_q)

            # «el área a la derecha de seis coma nueve ocho»
            self.en("areader")
            self.play(self.b1[6].animate(rate_func=there_and_back).set_fill(VERDE, 0.95), run_time=self.dur(0.9))

            # «la campana centrada en nueve»
            self.en("en9")
            self.play(self.cam1.animate(rate_func=there_and_back).set_stroke(width=9), FadeIn(en9), run_time=self.dur(0.8))

            # «seis coma nueve ocho menos nueve, entre tres»
            self.en("estand")
            self.play(LaggedStart(*[FadeIn(est[i], shift=UP * 0.1) for i in range(7)], lag_ratio=0.12),
                      run_time=self.dur(1.6))

            # «menos cero coma seis siete»
            self.en("z")
            self.play(FadeIn(zz, shift=UP * 0.1), run_time=self.dur(0.7))

            # «cero coma siete cinco»
            self.en("pd")
            self.play(*[FadeIn(pd[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.0))

            # «tres de cada cuatro aviones»
            self.en("tres4")
            self.play(LaggedStart(*[FadeIn(a, scale=0.5) for a in aviones], lag_ratio=0.2), run_time=self.dur(1.0))

            # «un uno por ciento de falsas alarmas»
            self.en("uno")
            self.play(FadeIn(fa1, shift=UP * 0.1), FadeIn(pd75, shift=UP * 0.1), run_time=self.dur(0.8))
        self.wait(0.3)
