"""Escena 09 — El reparto del modelador, y predecir con ruido: el coeficiente de ahora vale cero."""
from comun.escena import *


class ElReparto(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.parte_reparto()
        self.wait(0.6)
        self.parte_retardo()
        self.wait(1.0)
        self.limpiar()

    def parte_reparto(self):
        bl = BloqueLTI(r"F", centro=(-3.6, 1.2), ancho=1.8, alto=1.2, largo=1.5, color=AZUL, escala=1.0)
        l_mod = etiqueta("modelador", INK, 0.55).next_to(bl.caja, DOWN, buff=0.3)
        pz = plano_c(centro=(-3.6, -1.9), radio=0.8)
        cero = Circle(radius=0.09, color=AMBAR, stroke_width=4).move_to([-3.6 + 0.3, -1.9, 0])
        l_fm = etiqueta("fase mínima", AMBAR, 0.5).move_to([-0.9, -1.9, 0])
        ya = caja("ya sabía", VERDE, ancho=2.4, alto=0.8, scale=0.55).move_to([3.8, 2.1, 0])
        nu = caja("nuevo", ERROR, ancho=2.4, alto=0.8, scale=0.55).move_to([3.8, 0.3, 0])
        a_ya = flecha([-0.9, 1.2, 0], [2.5, 2.1, 0], VERDE)
        a_nu = flecha([-0.9, 1.2, 0], [2.5, 0.3, 0], ERROR)

        y_t = MathTex(r"y[n]", color=SENAL).scale(0.9).move_to([-5.2, 1.0, 0])
        circ = Circle(radius=0.45, color=INK, stroke_width=4).move_to([-1.6, 1.0, 0])
        mas = Text("+", color=TXT, weight=BOLD).scale(0.6).move_to(circ)
        a1 = flecha([-4.6, 1.0, 0], [-2.1, 1.0, 0], SENAL)
        a2 = flecha([-1.1, 1.0, 0], [1.5, 1.0, 0], MEDIDA)
        x_t = MathTex(r"x[n]", color=MEDIDA).scale(0.9).move_to([2.4, 1.0, 0])
        v_t = MathTex(r"v[n]", color=RUIDO).scale(0.9).move_to([-1.6, 3.2, 0])
        a_v = flecha([-1.6, 2.8, 0], [-1.6, 1.5, 0], RUIDO)
        pr = self.palabra("predecir", AMBAR, 0.9).move_to([-3.4, -1.6, 0])
        fi = self.palabra("filtrar", VERDE, 0.9).move_to([3.4, -1.6, 0])
        dist = MathTex(r"\neq", color=ERROR).scale(2.0).move_to([0, -1.6, 0])

        with self.narrar("b1"):
            # «el reparto»
            self.en("reparto")
            self.corte()
            self.play(FadeIn(bl), FadeIn(l_mod), run_time=self.dur(0.6))

            # «el filtro modelador de fase mínima»
            self.en("modelador")
            self.play(FadeIn(pz), Create(cero), FadeIn(l_fm), run_time=self.dur(0.6))

            # «lo que ya sabía»
            self.en("yasabia")
            self.play(GrowArrow(a_ya), FadeIn(ya), run_time=self.dur(0.6))

            # «lo genuinamente nuevo»
            self.en("nuevo")
            self.play(GrowArrow(a_nu), FadeIn(nu), run_time=self.dur(0.6))

            # «el sensor real»
            self.en("sensor")
            self.corte()
            self.play(FadeIn(y_t), GrowArrow(a1), FadeIn(circ), FadeIn(mas), GrowArrow(a2), FadeIn(x_t),
                      run_time=self.dur(1.0))

            # «lleva ruido»
            self.en("ruido")
            self.play(FadeIn(v_t), GrowArrow(a_v), run_time=self.dur(0.6))

            # «predecir y filtrar»
            self.en("pf")
            self.pop(pr)
            self.pop(fi)

            # «dejan de ser lo mismo»
            self.en("distinto")
            self.pop(dist)

    def parte_retardo(self):
        f1 = FilaMuestras([r"x[n{-}3]", r"x[n{-}2]", r"x[n{-}1]", r"x[n]"], centro=(0.8, 2.2), lado=1.35,
                          color=MEDIDA, escala=0.6)
        f2 = FilaMuestras([r"x[n{-}3]", r"x[n{-}2]", r"x[n{-}1]", r"x[n]"], centro=(0.8, -0.2), lado=1.35,
                          color=MEDIDA, escala=0.6)
        l_pred = self.palabra("predecir", AMBAR, 0.6).move_to([-4.9, 2.2, 0])
        l_filt = self.palabra("filtrar", VERDE, 0.6).move_to([-4.9, -0.2, 0])
        y_q = MathTex(r"y[n]=\,?", color=SENAL).scale(0.9).move_to([5.3, 2.2, 0])
        m1 = f1.marco(0, 2, AMBAR)
        k1 = MathTex(r"k\le n-1", color=AMBAR).scale(0.65).move_to([f1.x(1), 1.15, 0])
        m2 = f2.marco(0, 3, VERDE)
        k2 = MathTex(r"k\le n", color=VERDE).scale(0.65).move_to([f2.x(1.5), -1.25, 0])
        retardo = caja_tex(r"z^{-1}", AMBAR, ancho=1.5, alto=0.8, escala=0.8).move_to([5.4, 0.6, 0])
        l_ret = etiqueta("retardo", INK, 0.5).next_to(retardo, DOWN, buff=0.2)
        tach = tachar(VGroup(f1.cas[3], f1.rots[3]))
        h0 = formula("h[0]", "=", "0", escala=1.0, colores={0: ESTIMACION, 2: ERROR}).move_to([-4.0, -2.5, 0])
        T = Tallos([0, 0.74, 0.12, 0.02], centro=(2.8, -2.8), paso=0.8, unidad=1.2, color=ESTIMACION, extra=0)

        with self.narrar("b2"):
            # «Ahora predecir»
            self.en("ahora")
            self.corte()
            self.play(FadeIn(f1), FadeIn(l_pred), run_time=self.dur(0.7))

            # «estimar la temperatura de ahora»
            self.en("est")
            self.play(FadeIn(y_q), run_time=self.dur(0.5))

            # «hasta el instante anterior»
            self.en("hasta")
            self.play(Create(m1), FadeIn(k1), run_time=self.dur(0.6))

            # «No es lo mismo que filtrar»
            self.en("nolo")
            self.play(FadeIn(f2), FadeIn(l_filt), Create(m2), FadeIn(k2), run_time=self.dur(0.8))

            # «también la de ahora»
            self.en("tambien")
            self.resaltar(f2.cas[3], color=AMBAR)

            # «un retardo de más»
            self.en("retardo")
            self.play(FadeIn(retardo), FadeIn(l_ret), run_time=self.dur(0.5))

            # «vale cero»
            self.en("cero")
            self.play(Create(tach), run_time=self.dur(0.4))

            # «hache de cero igual a cero»
            self.en("h0")
            self.pop(h0)

            # «una posición después»
            self.en("despues")
            self.play(Create(T.base), run_time=self.dur(0.3))
            self.play(LaggedStart(*[FadeIn(T.palito(i)) for i in range(4)], lag_ratio=0.25), run_time=self.dur(1.0))
