"""Escena 08 — El paso de corrección: el filtro es el predictor más una corrección con K = 0,7386."""
from comun.escena import *


class ElPasoDeCorreccion(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.correccion()
        self.wait(0.6)
        self.lectura()
        self.wait(1.0)
        self.limpiar()

    def correccion(self):
        xn = MathTex("x[n]", color=MEDIDA).scale(0.95).move_to([2.0, 3.55, 0])
        axn = flecha([2.0, 3.25, 0], [2.0, 2.95, 0], color=MEDIDA)
        cb = caja("paso de corrección", AMBAR, ancho=3.6, alto=0.8, scale=0.5).move_to([2.0, 2.5, 0])
        ca = caja("se predice", AZUL, ancho=3.0, alto=0.8, scale=0.5).move_to([-3.2, 2.5, 0])
        a_ab = flecha([-1.7, 2.5, 0], [0.2, 2.5, 0])
        f = formula("\\hat q[n|n]", "=", "\\hat q[n|n-1]", "+", "K", "\\,(", "x[n]-\\hat q[n|n-1]", ")", escala=0.85,
                    colores={0: ESTIMACION, 2: ESTIMACION, 4: AMBAR, 6: MEDIDA}).move_to([0, 0.8, 0])
        k = formula("K", "=", "0{,}7386", escala=1.0, colores={0: AMBAR}).move_to([-3.2, -0.5, 0])
        tal = Tallos([0.7386, 0.1158, 0.0182], centro=(4.6, -0.6), paso=0.8, unidad=1.2, color=SENAL)
        tl = etiqueta("filtro causal del sensor", INK, 0.42).move_to([4.6, -1.5, 0])
        sello_ = sello("comprobado", VERDE).scale(0.7).move_to([-5.6, -2.5, 0])
        c1 = formula("0{,}6", "(1-K)", "=", "0{,}6\\cdot0{,}2614", escala=0.9).move_to([-1.5, -2.5, 0])
        c2 = formula("=", "0{,}157", escala=0.9, colores={1: ESTIMACION}).move_to([1.9, -2.5, 0])
        ok = tilde(VERDE, 0.4).move_to([3.4, -2.5, 0])
        with self.narrar("b1"):
            # «el que sí la usa»
            self.en("usa")
            self.play(FadeIn(xn), GrowArrow(axn), run_time=self.dur(0.6))
            # «añadimos un paso»
            self.en("paso")
            self.play(FadeIn(cb), run_time=self.dur(0.6))
            # «Primero se predice»
            self.en("predice")
            self.play(FadeIn(ca), GrowArrow(a_ab), run_time=self.dur(0.7))
            # «se corrige con lo que llega»
            self.en("corrige")
            self.play(FadeIn(f), run_time=self.dur(1.0))
            # «una ganancia, k»
            self.en("k")
            self.resaltar(f[4], color=AMBAR, run_time=0.6)
            # «cero coma siete tres ocho seis»
            self.en("k7386")
            self.play(FadeIn(k), run_time=self.dur(0.6))
            # «el primer coeficiente del filtro»
            self.en("h0")
            self.play(Create(tal.base), *[Create(t) for t in tal.tallos], *[FadeIn(p) for p in tal.puntos],
                      FadeIn(tl), run_time=self.dur(0.9))
            self.resaltar(tal.palito(0), color=AMBAR, run_time=0.5)
            # «Comprobación»
            self.en("comprob")
            self.play(FadeIn(sello_), run_time=self.dur(0.5))
            # «cero coma seis por uno menos k»
            self.en("c1")
            self.play(FadeIn(c1), run_time=self.dur(0.8))
            # «el polo cero coma uno cinco siete»
            self.en("c2")
            self.play(FadeIn(c2), Create(ok), run_time=self.dur(0.7))

    def lectura(self):
        self.corte()
        esc = 1.2
        x0 = -5.5
        b1 = barra_h(2.826, 2.4, x0, esc, ERROR)
        l1 = MathTex("2{,}826", color=ERROR).scale(0.8).next_to(b1, RIGHT, buff=0.2)
        t1 = etiqueta("error de la predicción", INK, 0.45).move_to([x0 + 1.7, 3.1, 0])
        b2 = barra_h(1.0, 1.4, x0, esc, RUIDO)
        l2 = MathTex("1", color=RUIDO).scale(0.8).next_to(b2, RIGHT, buff=0.2)
        t2 = etiqueta("ruido", INK, 0.45).move_to([x0 + 0.5, 1.95, 0])
        sr = barra_h(2.826, 0.1, x0, esc, ERROR)
        sm = barra_h(1.0, 0.1, x0 + 2.826 * esc, esc, RUIDO)
        ls = etiqueta("sorpresa: 3,826", INK, 0.45).move_to([x0 + 2.2, -0.45, 0])
        K1 = formula("K", "=", "\\frac{2{,}826}{2{,}826+1}", escala=1.0, colores={0: AMBAR}).move_to([3.6, 1.3, 0])
        K2 = formula("=", "0{,}7386", escala=1.0, colores={1: AMBAR}).move_to([3.4, -0.4, 0])
        Kb = formula("K", "=", "0{,}7386", escala=0.9, colores={0: AMBAR}).move_to([-3.0, -2.4, 0])
        eq = MathTex("=", color=VERDE).scale(1.0).move_to([0.3, -2.4, 0])
        Kb2 = formula("K", "=", "0{,}7386", escala=0.9, colores={0: AMBAR}).move_to([3.0, -2.4, 0])
        ok = tilde(VERDE, 0.4).move_to([5.7, -2.4, 0])
        sm2 = barra_h(0.25, 0.1, x0 + 2.826 * esc, esc, RUIDO)
        Kx = formula("K", "\\to", "1", escala=0.9, colores={0: AMBAR}).move_to([5.0, -0.4, 0])
        with self.narrar("b2"):
            # «lectura sencilla»
            self.en("lectura")
            self.play(FadeIn(Kb), run_time=self.dur(0.5))
            # «El error de la predicción es dos coma ocho dos seis»
            self.en("errpred")
            self.play(FadeIn(t1), GrowFromEdge(b1, LEFT), FadeIn(l1), run_time=self.dur(1.0))
            # «el ruido, uno»
            self.en("ruido1")
            self.play(FadeIn(t2), GrowFromEdge(b2, LEFT), FadeIn(l2), run_time=self.dur(0.8))
            # «la sorpresa que trae cada medición»
            self.en("sorp")
            self.play(FadeIn(sr), FadeIn(sm), FadeIn(ls), run_time=self.dur(0.8))
            # «la parte que viene de la señal»
            self.en("parte")
            self.play(sr.animate.set_stroke(AMBAR, 4, 1.0), run_time=0.5)
            # «dos coma ocho dos seis entre»
            self.en("entre")
            self.play(FadeIn(K1), run_time=self.dur(0.9))
            # «cero coma siete tres ocho seis»
            self.en("r")
            self.play(FadeIn(K2), run_time=self.dur(0.6))
            # «Justo la ganancia»
            self.en("justo")
            self.play(FadeIn(eq), FadeIn(Kb2), Create(ok), run_time=self.dur(0.8))
            # «cuando el ruido molesta menos»
            self.en("menos")
            self.play(Transform(sm, sm2), FadeIn(Kx), run_time=self.dur(1.2))
