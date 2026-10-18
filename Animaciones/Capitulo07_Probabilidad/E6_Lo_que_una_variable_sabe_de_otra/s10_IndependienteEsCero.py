"""Escena 10 — Independientes implica covarianza cero (pero no al revés)."""
from comun.escena import *


class IndependienteEsCero(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def bloque1(self):
        # la tabla de dos variables independientes con las mismas medias del canal (0,3 y 0,34)
        indep = [[0.7 * 0.66, 0.7 * 0.34], [0.3 * 0.66, 0.3 * 0.34]]
        T = TablaCanal(centro=(-4.1, -0.2), lado=1.8, esc=0.7, probs=indep)
        etiqueta_i = Text("Independientes", color=AMBAR, weight=BOLD).scale(0.7).move_to([-4.1, 2.8, 0])
        r1 = formula("P(x,y)", "=", "P(x)", r"\cdot", "P(y)", escala=1.3).move_to([2.6, 2.6, 0])
        r2 = formula("E[XY]", "=", r"\sum_x\sum_y", r"x\,y", r"P(x)\,P(y)", escala=1.05,
                     colores={0: AMBAR}).move_to([2.6, 1.1, 0])
        r3 = formula("=", r"\Big(\sum_x x\,P(x)\Big)", r"\Big(\sum_y y\,P(y)\Big)", escala=1.05).move_to([2.6, -0.4, 0])
        r4 = formula("=", "E[X]", r"\cdot", "E[Y]", escala=1.4, colores={1: SENAL, 3: MEDIDA}).move_to([2.6, -1.8, 0])
        r5 = formula(r"r_{XY}", "=", r"\mu_X\mu_Y", escala=1.4, colores={0: AMBAR}).move_to([1.0, -3.1, 0])
        r6 = formula(r"\sigma_{XY}", "=", "0", escala=1.6, colores={0: AMBAR, 2: AMBAR}).move_to([5.0, -3.1, 0])
        for r in (r1, r2, r3, r4, r5, r6):
            oculta(r)
            self.add(r)
        r1.align_to([-1.2, 0, 0], LEFT)
        r2.align_to([-1.2, 0, 0], LEFT)
        r3.shift(RIGHT * (r2[1].get_left()[0] - r3[0].get_left()[0]))
        r4.shift(RIGHT * (r2[1].get_left()[0] - r4[0].get_left()[0]))
        self.r = [r1, r2, r3, r4, r5, r6]
        with self.narrar("b1"):
            # «¿Y si las variables son independientes?»
            self.en("indep")
            self.play(FadeIn(T.armazon()), FadeIn(T.probs()), FadeIn(etiqueta_i), run_time=self.dur(0.7))

            # «la probabilidad de cada pareja»
            self.en("pareja")
            self.play(*revelar(r1[0]), Create(T.marco(1, 1, AMBAR)), run_time=self.dur(0.6))

            # «el producto de las probabilidades de cada una»
            self.en("prod_p")
            cuenta = formula("0{,}3", r"\cdot", "0{,}34", "=", "0{,}102", escala=1.0).move_to([-4.1, -3.4, 0])
            self.play(*revelar(r1[1], r1[2], r1[3], r1[4]), FadeIn(cuenta), run_time=self.dur(0.8))

            # «Y al calcular»
            self.en("al_calc")
            self.resaltar(self.r[0], color=AMBAR, escala=1.05)

            # «la esperanza del producto»
            self.en("e_prod2")
            self.play(*revelar(*r2), run_time=self.dur(0.9))

            # «la suma se separa en dos»
            self.en("separa")
            self.play(*revelar(*r3), run_time=self.dur(0.8))

            # «la esperanza de equis por la de i griega»
            self.en("ex_ey")
            self.play(*revelar(*r4), run_time=self.dur(0.7))

            # «La correlación»
            self.en("la_corr")
            self.resaltar(self.r[1][0], color=AMBAR, escala=1.1)

            # «el producto de las medias»
            self.en("medias2")
            self.play(*revelar(*r5), run_time=self.dur(0.7))

            # «la covarianza da cero»
            self.en("cero_cov")
            self.play(*revelar(*r6), run_time=self.dur(0.6))
            self.sfx("exito")

    def bloque2(self):
        with self.narrar("b2"):
            # «Independientes, entonces»
            self.en("ind_cero")
            self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.camera.frame], run_time=0.3)
            i1 = Text("Independientes", color=TXT, weight=BOLD).scale(0.9)
            f1 = MathTex(r"\Rightarrow", color=VERDE).scale(1.8)
            s1 = formula(r"\sigma_{XY}", "=", "0", escala=1.8, colores={0: AMBAR, 2: AMBAR})
            fila1 = VGroup(i1, f1, s1).arrange(RIGHT, buff=0.5).move_to([0, 1.7, 0])
            self.play(FadeIn(fila1, shift=UP * 0.2), run_time=self.dur(0.7))

            # «significa covarianza cero»
            self.en("signif")
            self.resaltar(s1, color=AMBAR, escala=1.1)

            # «leerlo al revés»
            self.en("reves")
            s2 = formula(r"\sigma_{XY}", "=", "0", escala=1.8, colores={0: AMBAR, 2: AMBAR})
            f2 = MathTex(r"\Rightarrow\,?", color=AMBAR).scale(1.8)
            i2 = Text("Independientes", color=TXT, weight=BOLD).scale(0.9)
            fila2 = VGroup(s2, f2, i2).arrange(RIGHT, buff=0.5).move_to([0, -1.2, 0])
            self.play(FadeIn(fila2, shift=UP * 0.2), run_time=self.dur(0.7))

            # «si la covarianza es cero»
            self.en("si_cero")
            self.resaltar(s2, color=AMBAR, escala=1.1)

            # «serán independientes»
            self.en("seran")
            self.resaltar(i2, color=AMBAR, escala=1.1)

            # «Parece lógico»
            self.en("logico")
            ok = tilde(AMBAR, 0.6).next_to(fila2, RIGHT, buff=0.3)
            self.play(Create(ok), run_time=self.dur(0.5))

            # «uno de los errores más comunes»
            self.en("error")
            self.play(FadeOut(ok), Create(tachar(f2)), f2.animate.set_color(ROJO), run_time=self.dur(0.6))
            self.sfx("error")

            # «Vamos a ver por qué»
            self.en("por_que")
            q = Text("?", color=AMBAR, weight=BOLD).scale(3.2).move_to([0, -3.2, 0])
            self.pop(q)
