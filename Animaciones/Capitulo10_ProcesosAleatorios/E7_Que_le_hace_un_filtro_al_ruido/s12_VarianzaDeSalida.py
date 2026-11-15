"""Escena 12 — Varianza de la salida: R_yy(0) = 3/5 = 0,6, y la carrera β/(α + β) entre dos memorias."""
from comun.escena import *


class VarianzaDeSalida(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.cuenta()
        self.lectura()

    # ------------------------------------------------------------------ b1
    def cuenta(self):
        f_a = formula(r"\mathrm{Var}(y)", "=", r"R_{yy}(0)", escala=1.1).move_to([-3.6, 3.0, 0])
        f_b = formula("=", r"(R_{hh} * R_{xx})", r"(0)", escala=1.1).move_to([-3.4, 1.85, 0])
        f_c = formula("=", r"\int R_{hh}(s)\,R_{xx}(s)\,ds", escala=1.1).move_to([-3.0, 0.7, 0])
        f_c.align_to(f_b, LEFT)
        ax, lab = ejes((-2, 2), (0, 1.8), ancho=5.4, alto=3.4, x_label="s")
        g = VGroup(ax, lab).move_to([3.9, 0.3, 0])
        c_x = ax.plot(lambda s: np.exp(-2 * abs(s)), x_range=[-2, 2], color=SENAL, stroke_width=4)
        c_h = ax.plot(lambda s: 1.5 * np.exp(-3 * abs(s)), x_range=[-2, 2], color=ESTIMACION, stroke_width=4)
        c_p = ax.plot(lambda s: 1.5 * np.exp(-5 * abs(s)), x_range=[-2, 2], color=AMBAR, stroke_width=5)
        area = ax.get_area(c_p, x_range=(-2, 2), color=AMBAR, opacity=0.35)
        lab_x = formula(r"e^{-2|s|}", escala=0.75, colores={0: SENAL}).move_to([2.6, 2.5, 0])
        lab_h = formula(r"\tfrac32 e^{-3|s|}", escala=0.75, colores={0: ESTIMACION}).move_to([5.4, 2.5, 0])
        f_d = formula(r"\tfrac32\,e^{-5|s|}", escala=1.0, colores={0: AMBAR}).move_to([-4.0, -0.5, 0])
        f_e = formula(r"\tfrac15", "+", r"\tfrac15", "=", r"\tfrac25", escala=1.1).move_to([-3.9, -1.5, 0])
        f_f = formula(r"\tfrac32\cdot\tfrac25", "=", r"\tfrac35", "=", r"0{,}6", escala=1.3).move_to([-3.0, -2.6, 0])
        caja_f = SurroundingRectangle(f_f, color=AMBAR, buff=0.18, stroke_width=3)
        cero = Dot(ax.c2p(0, 1.5), radius=0.001, color=AMBAR)

        with self.narrar("b1"):
            # «La varianza de la salida»
            self.en("varianza")
            self.play(FadeIn(f_a), run_time=self.dur(0.8))

            # «su autocorrelación en cero»
            self.en("r_cero")
            self.resaltar(f_a[2], color=AMBAR, escala=1.15)

            # «la convolución de las dos autocorrelaciones»
            self.en("dos_autocorr")
            self.play(FadeIn(f_b[:2]), run_time=self.dur(0.8))

            # «evaluada en cero»
            self.en("en_cero")
            self.play(FadeIn(f_b[2]), run_time=self.dur(0.4))

            # «el área del producto»
            self.en("area_prod")
            self.play(FadeIn(f_c), run_time=self.dur(0.8))

            # «las dos curvas»
            self.en("dos_curvas")
            self.play(FadeIn(g), Create(c_x), Create(c_h), FadeIn(lab_x), FadeIn(lab_h), run_time=self.dur(1.0))

            # «Al multiplicar las exponenciales»
            self.en("multiplicar")
            self.play(Create(c_p), run_time=self.dur(0.8))

            # «los exponentes se suman»
            self.en("suman")
            self.play(FadeIn(area), run_time=self.dur(0.6))

            # «cinco por el valor absoluto»
            self.en("cinco")
            self.play(FadeIn(f_d), run_time=self.dur(0.6))

            # «un quinto a cada lado»
            self.en("quinto")
            self.play(FadeIn(f_e), run_time=self.dur(0.8))

            # «tres medios»
            self.en("tm")
            self.play(FadeIn(f_f[0]), run_time=self.dur(0.5))

            # «tres quintos»
            self.en("tq")
            self.play(FadeIn(f_f[1:3]), run_time=self.dur(0.5))

            # «cero coma seis»
            self.en("c06")
            self.play(FadeIn(f_f[3:]), Create(caja_f), run_time=self.dur(0.6))
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def lectura(self):
        L = Lienzo(ancho=3.0, alto=1.3, t_rango=(0, 6), v_max=1.4, centro=(-4.7, 2.7))
        onda = onda_tel(L, nivel0=1, color=AMBAR, ancho=4.0)
        bl = BloqueLTI(r"h", centro=(0.4, 2.7), ancho=1.6, alto=1.0, largo=1.3, escala=0.8)
        Ls = Lienzo(ancho=2.6, alto=1.3, t_rango=(0, 1), v_max=1.4, centro=(5.4, 2.7))
        suave = Ls.curva(np.linspace(0, 1, 120), 0.5 * serie(9, 120, 0.97), MEDIDA, 3.5)
        sim = formula(r"\text{simulación: } 0{,}61", escala=0.95).move_to([5.2, 1.2, 0])
        ok = tilde().scale(0.8).next_to(sim, LEFT, buff=0.3)
        # barras de potencia
        base_y, unidad = -2.6, 2.6
        b_in = Rectangle(width=0.9, height=unidad, color=SENAL, stroke_width=2).set_fill(SENAL, 0.5).move_to([-5.6, base_y + unidad / 2, 0])
        b_out = Rectangle(width=0.9, height=0.6 * unidad, color=MEDIDA, stroke_width=2).set_fill(MEDIDA, 0.5).move_to([-4.2, base_y + 0.3 * unidad, 0])
        l_in = Text("entrada", color=SENAL).scale(0.4).next_to(b_in, DOWN, buff=0.15)
        l_out = Text("salida", color=MEDIDA).scale(0.4).next_to(b_out, DOWN, buff=0.15)
        n_in = MathTex("1", color=TXT).scale(0.8).next_to(b_in, UP, buff=0.12)
        n_out = MathTex("0{,}6", color=TXT).scale(0.8).next_to(b_out, UP, buff=0.12)
        cuanto = Text("¿cuánto?", color=ROJO, weight=BOLD).scale(0.6).move_to([-4.9, 1.4, 0])
        caja_f = caja("filtro: β = 3", ESTIMACION, ancho=3.0, alto=0.7, scale=0.5).move_to([0.6, 0.6, 0])
        caja_p = caja("proceso: α = 2", SENAL, ancho=3.0, alto=0.7, scale=0.5).move_to([0.6, -0.4, 0])
        ff = formula(r"\frac{\beta}{\alpha+\beta}", "=", r"\frac{3}{2+3}", escala=1.3).move_to([0.6, -1.9, 0])
        # deslizador
        pista = Line([2.2, -3.4, 0], [6.4, -3.4, 0], color=INK, stroke_width=4)
        s = ValueTracker(0.54)
        punto = always_redraw(lambda: Dot([2.2 + 4.2 * s.get_value(), -3.4, 0], radius=0.17, color=AMBAR))
        barra_v = always_redraw(lambda: Rectangle(width=0.9, height=max(0.05, unidad * (lambda b: b / (2 + b))(0.2 * 150 ** s.get_value())),
                                                  color=AMBAR, stroke_width=2).set_fill(AMBAR, 0.35)
                                .move_to([-4.2, base_y + max(0.05, unidad * (lambda b: b / (2 + b))(0.2 * 150 ** s.get_value())) / 2, 0]))
        lab_b = MathTex(r"\beta", color=AMBAR).scale(0.9).next_to(pista, LEFT, buff=0.3)

        with self.narrar("b2"):
            # «Una simulación»
            self.en("simula")
            self.corte()
            self.play(Create(L.base()), Create(onda), FadeIn(bl), Create(suave), run_time=self.dur(1.2))

            # «cero coma seis uno»
            self.en("c061")
            self.play(FadeIn(sim), FadeIn(ok, scale=0.6), run_time=self.dur(0.6))

            # «la cuenta funciona»
            self.en("funciona")
            self.resaltar(sim, color=VERDE, escala=1.08)

            # «le ha quitado potencia»
            self.en("quita")
            self.play(FadeIn(b_in), FadeIn(n_in), FadeIn(l_in), run_time=self.dur(0.5))
            self.play(FadeIn(b_out), FadeIn(n_out), FadeIn(l_out), run_time=self.dur(0.5))

            # «recorta las variaciones rápidas»
            self.en("rapidas")
            self.resaltar(suave, color=AMBAR, escala=1.08)

            # «Cuánto quita depende»
            self.en("cuanto")
            self.pop(cuanto)

            # «una carrera entre dos memorias»
            self.en("carrera")
            self.play(FadeIn(caja_f), FadeIn(caja_p), run_time=self.dur(0.6))

            # «la del filtro y la del proceso»
            self.en("ambas")
            self.resaltar(caja_f, color=AMBAR, escala=1.08)
            self.resaltar(caja_p, color=AMBAR, escala=1.08)

            # «tres entre tres más dos»
            self.en("formula")
            self.play(FadeIn(ff), run_time=self.dur(0.8))

            # «mucho más rápido»
            self.en("rapido")
            self.play(FadeOut(cuanto), FadeOut(b_out), FadeIn(pista), FadeIn(punto), FadeIn(barra_v), FadeIn(lab_b), run_time=0.4)
            self.play(s.animate.set_value(0.95), run_time=self.dur(1.8), rate_func=smooth)

            # «mucho más lento»
            self.en("lento")
            self.play(s.animate.set_value(0.05), run_time=self.dur(2.2), rate_func=smooth)
        punto.clear_updaters()
        barra_v.clear_updaters()
        self.wait(1.0)
        self.limpiar()
