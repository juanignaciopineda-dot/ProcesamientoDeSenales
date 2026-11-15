"""Escena 06 — El eco sin ruido: Yule-Walker da h = (0,6; 0); solo cuenta la última muestra."""
from comun.escena import *


class ElEcoSinRuido(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.cuentas()
        self.moraleja()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def cuentas(self):
        titulo_e = Text("las dos ecuaciones", color=INK).scale(0.72).move_to([-3.2, 3.3, 0])
        r1 = formula(r"4\,h_0", "+", r"2{,}4\,h_1", "=", r"2{,}4", escala=1.30).move_to([-3.2, 2.3, 0])
        r2 = formula(r"2{,}4\,h_0", "+", r"4\,h_1", "=", r"1{,}44", escala=1.30).move_to([-3.2, 1.2, 0])
        p0 = formula(r"h_0", "=", r"0{,}6", escala=1.30, colores={0: ESTIMACION, 2: AMBAR}).move_to([4.2, 2.3, 0])
        p1 = formula(r"h_1", "=", r"0", escala=1.30, colores={0: ESTIMACION, 2: AMBAR}).move_to([4.2, 1.2, 0])
        s1 = MathTex(r"4\cdot 0{,}6+2{,}4\cdot 0=2{,}4", color=TXT).scale(1.17).move_to([-3.2, -0.1, 0])
        s2 = MathTex(r"2{,}4\cdot 0{,}6+4\cdot 0=1{,}44", color=TXT).scale(1.17).move_to([-3.2, -1.1, 0])
        t1 = tilde(VERDE, 0.4).next_to(s1, RIGHT, buff=0.4)
        t2 = tilde(VERDE, 0.4).next_to(s2, RIGHT, buff=0.4)
        T = Tallos([0.6, 0.0], centro=(4.2, -2.6), paso=2.2, unidad=1.6, color=ESTIMACION)
        xs = [MathTex(r"x[n]", color=MEDIDA).scale(1.04).move_to([T.x(0), -3.2, 0]),
              MathTex(r"x[n-1]", color=MEDIDA).scale(1.04).move_to([T.x(1), -3.2, 0])]
        ult = Text("solo la última", color=VERDE).scale(0.65).move_to([4.2, -1.3, 0])

        with self.narrar("b1"):
            # «Las dos ecuaciones»
            self.en("eqs")
            self.play(FadeIn(titulo_e), run_time=0.3)
            # «cuatro hache cero más dos coma cuatro hache uno»
            self.en("e1a")
            self.play(LaggedStart(*[FadeIn(r1[i]) for i in range(3)], lag_ratio=0.3), run_time=self.dur(0.8))
            # «igual a dos coma cuatro, y»
            self.en("e1b")
            self.play(FadeIn(r1[3]), FadeIn(r1[4]), run_time=0.4)
            # «dos coma cuatro hache cero más cuatro hache uno»
            self.en("e2a")
            self.play(LaggedStart(*[FadeIn(r2[i]) for i in range(3)], lag_ratio=0.3), run_time=self.dur(0.8))
            # «igual a uno coma cuatro cuatro»
            self.en("e2b")
            self.play(FadeIn(r2[3]), FadeIn(r2[4]), run_time=0.4)
            # «Probamos hache cero igual a cero coma seis»
            self.en("p0")
            self.play(FadeIn(p0), run_time=0.5)
            # «y hache uno igual a cero»
            self.en("p1")
            self.play(FadeIn(p1), run_time=0.5)
            # «Primera: dos coma cuatro»
            self.en("ok1")
            self.play(FadeIn(s1), run_time=0.5)
            self.play(FadeIn(t1), run_time=0.3)
            # «Segunda: uno coma cuatro cuatro»
            self.en("ok2")
            self.play(FadeIn(s2), run_time=0.5)
            self.play(FadeIn(t2), run_time=0.3)
            # «Las dos salen»
            self.en("salen")
            self.resaltar(t1, t2, color=VERDE, escala=1.40, run_time=0.5)
            # «Solo importa la última muestra»
            self.en("ultima")
            self.play(FadeIn(T), *[FadeIn(x) for x in xs], FadeIn(ult), run_time=self.dur(0.7))

    # ------------------------------------------------------------------ b2
    def moraleja(self):
        eco = formula(r"x[n+1]", "=", r"0{,}6", r"x[n]", escala=1.43, colores={0: MEDIDA, 3: MEDIDA}).move_to([-2.0, 2.4, 0])
        moneda_w = formula(r"+\,w[n+1]", escala=1.43, colores={0: RUIDO}).next_to(eco, RIGHT, buff=0.3)
        mon = moneda("", RUIDO).scale(0.5).next_to(moneda_w, RIGHT, buff=0.3)
        marco_x = SurroundingRectangle(eco[3], color=VERDE, buff=0.1, stroke_width=4)
        err = MathTex(r"\text{error}=2{,}56", color=ERROR).scale(1.30).move_to([-3.6, 0.6, 0])
        P = parabola_l(centro=(3.6, 0.2), ancho=4.4, alto=2.6, fondo=0.45, color=AMBAR)
        vertice = Dot(P.L.p(0, 0.45), radius=0.1, color=ERROR)
        v_t = MathTex(r"2{,}56", color=ERROR).scale(0.91).next_to(vertice, DOWN, buff=0.35).shift(RIGHT * 0.9)
        c10 = Text("capítulo 10", color=INK).scale(0.59).move_to([3.6, -1.7, 0])
        tri = Triangle(color=AMBAR, stroke_width=6).scale(1.0).move_to([0, 1.0, 0])
        adm = Text("!", color=AMBAR, weight=BOLD).scale(1.30).move_to(tri).shift(DOWN * 0.1)
        cuid = Text("no siempre pasa", color=AMBAR).scale(0.91).move_to([0, -0.8, 0])
        otra = Lienzo(ancho=8.0, alto=2.0, t_rango=(0, 40), v_max=4.0, centro=(0, 2.0))
        cur = otra.curva(np.arange(40), 2.0 * serie(21, 40, 0.0), INK, 3)
        xn1 = MathTex(r"x[n-1]", color=MEDIDA).scale(1.30).move_to([-3.2, -0.2, 0])
        sinr = Text("correlación = 0", color=ERROR).scale(0.78).next_to(xn1, DOWN, buff=0.3)
        dist = MathTex(r"h_1 \neq 0", color=AMBAR).scale(1.56).move_to([3.2, -0.2, 0])
        interr = Text("?", color=AMBAR, weight=BOLD).scale(2.2).move_to([0, -2.3, 0])
        reloj = reloj_arena().scale(0.9).move_to([2.0, -2.3, 0])

        with self.narrar("b2"):
            # «el eco es cero coma seis por la salida anterior»
            self.en("eco")
            self.corte()
            self.play(LaggedStart(*[FadeIn(eco[i]) for i in range(4)], lag_ratio=0.3), run_time=self.dur(0.9))
            # «más una moneda nueva»
            self.en("moneda")
            self.play(FadeIn(moneda_w), FadeIn(mon), run_time=0.5)
            # «la última muestra ya lo contiene todo»
            self.en("todo")
            self.play(Create(marco_x), run_time=0.4)
            # «El error es dos coma cinco seis»
            self.en("error")
            self.play(FadeIn(err), run_time=0.5)
            # «el mínimo de la parábola del capítulo diez»
            self.en("parabola")
            self.play(Create(P), FadeIn(c10), run_time=self.dur(0.8))
            self.play(FadeIn(vertice), FadeIn(v_t), run_time=0.4)
            # «Pero cuidado con generalizar»
            self.en("cuidado")
            self.corte()
            self.play(Create(tri), FadeIn(adm), FadeIn(cuid), run_time=self.dur(0.6))
            # «Existe un proceso»
            self.en("existe")
            self.corte()
            self.play(Create(cur), run_time=self.dur(0.8))
            # «una muestra sin ninguna relación con el futuro»
            self.en("sinrel")
            self.play(FadeIn(xn1), FadeIn(sinr), run_time=0.5)
            # «un coeficiente distinto de cero»
            self.en("distinto")
            self.play(FadeIn(dist), run_time=0.5)
            # «¿Te atreves a imaginar cuál?»
            self.en("pregunta")
            self.play(FadeIn(interr), FadeIn(reloj), run_time=0.5)
