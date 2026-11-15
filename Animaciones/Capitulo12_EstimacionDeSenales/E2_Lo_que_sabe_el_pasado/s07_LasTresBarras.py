"""Escena 07 — Las tres barras (ρ = 0,4): predecir x[n+1] con una y con dos muestras."""
from comun.escena import *


class LasTresBarras(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.recordar()
        self.predecir()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def recordar(self):
        T = Tallos([0, 0, 0.4, 1, 0.4, 0, 0], centro=(-0.5, -1.2), paso=1.3, unidad=2.6, color=AZUL,
                   k0=-3, indices=True)
        ro = MathTex(r"\rho = 0{,}4", color=AMBAR).scale(1.56).move_to([4.5, 2.4, 0])
        c11 = sello("Cap. 11", INK).move_to([5.6, 3.3, 0])
        filtro = caja("(2, 1) / √5", AZUL, ancho=2.4, alto=0.8, scale=0.5).move_to([-5.0, 2.4, 0])
        mon = moneda("", RUIDO).scale(0.45).move_to([-6.5, 2.4, 0])
        f_in = flecha([-6.0, 2.4, 0], [-6.25, 2.4, 0], INK, 3)
        vecinas = VGroup(
            CurvedArrow(T.pos(3) + UP * 0.35, T.pos(2) + UP * 0.35, angle=PI / 2, color=INK, stroke_width=3, tip_length=0.15),
            CurvedArrow(T.pos(3) + UP * 0.35, T.pos(4) + UP * 0.35, angle=-PI / 2, color=INK, stroke_width=3, tip_length=0.15))
        ceros = VGroup(*[Text("0", color=ERROR).scale(0.78).move_to([T.x(i), T.cy + 0.45, 0]) for i in (0, 1, 5, 6)])

        with self.narrar("b1"):
            # «Recordemos el proceso de las tres barras»
            self.en("barras")
            self.corte()
            self.play(FadeIn(T.base), FadeIn(T.ks), *[FadeIn(T.palito(i)) for i in (2, 3, 4)], run_time=self.dur(0.8))
            # «ro igual a cero coma cuatro»
            self.en("ro")
            self.play(FadeIn(ro), run_time=0.4)
            # «el capítulo once»
            self.en("cap11")
            self.pop(c11)
            # «el filtro de dos coeficientes»
            self.en("filtro")
            self.play(FadeIn(mon), FadeIn(filtro), run_time=0.5)
            # «Cada muestra se parece solo a sus vecinas»
            self.en("vecinas")
            self.play(*[Create(v) for v in vecinas], run_time=self.dur(0.6))
            # «correlación uno consigo misma»
            self.en("uno")
            self.resaltar(T.palito(3), color=AMBAR, run_time=0.5)
            # «cero coma cuatro con la de al lado»
            self.en("cuatro")
            self.resaltar(T.palito(2), T.palito(4), color=AMBAR, run_time=0.5)
            # «cero con cualquiera a dos pasos o más»
            self.en("cero")
            self.play(FadeIn(ceros), run_time=0.5)

    # ------------------------------------------------------------------ b2
    def predecir(self):
        F = FilaMuestras([r"x[n-1]", r"x[n]", r"x[n+1]"], centro=(0.0, 2.0), lado=2.00, color=MEDIDA, escala=1.10)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.17).next_to(F.cas[2], RIGHT, buff=0.25)
        coef = MathTex(r"h", "=", r"\rho", "=", r"0{,}4", color=TXT).scale(1.30).move_to([-4.2, -0.3, 0])
        coef[0].set_color(ESTIMACION), coef[2].set_color(AMBAR), coef[4].set_color(AMBAR)
        err = formula(r"\text{error}", "=", "1", "-", r"0{,}4^2", escala=1.30, colores={0: ERROR}).move_to([-4.2, -1.5, 0])
        e084 = MathTex(r"=\,0{,}84", color=ERROR).scale(1.30).next_to(err, RIGHT, buff=0.25)
        h1 = MathTex(r"h_1", color=ESTIMACION).scale(1.17).next_to(F.cas[0], UP, buff=0.2)
        ojo = Text("¡ojo!", color=AMBAR, weight=BOLD).scale(1.04).move_to([0, 3.5, 0])
        llave = BraceBetweenPoints(F.cas[0].get_bottom() + DOWN * 0.1, F.cas[2].get_bottom() + DOWN * 0.1,
                                   direction=DOWN, color=INK)
        dos_p = Text("2 pasos", color=INK).scale(0.65).next_to(llave, DOWN, buff=0.1)
        cero = Text("correlación = 0", color=ERROR).scale(0.78).next_to(dos_p, DOWN, buff=0.15)
        interr.permitir_fuera = True

        with self.narrar("b2"):
            # «Predecimos equis de ene más uno»
            self.en("pred")
            self.corte()
            self.play(FadeIn(F), FadeIn(interr), run_time=self.dur(0.6))
            # «Con una sola muestra»
            self.en("una")
            self.play(F.cas[1].animate.set_stroke(AMBAR), run_time=0.4)
            # «el coeficiente es la correlación»
            self.en("coef")
            self.play(LaggedStart(*[FadeIn(coef[i]) for i in range(5)], lag_ratio=0.25), run_time=self.dur(0.9))
            # «el error, uno menos cero coma cuatro al cuadrado»
            self.en("err")
            self.play(LaggedStart(*[FadeIn(err[i]) for i in range(5)], lag_ratio=0.25), run_time=self.dur(1.0))
            # «cero coma ocho cuatro»
            self.en("e084")
            self.play(FadeIn(e084), run_time=0.4)
            # «Y ahora añadimos la anterior»
            self.en("anade")
            self.play(F.cas[0].animate.set_stroke(AMBAR), FadeIn(h1), run_time=0.5)
            # «la anterior, equis de ene menos uno»
            self.en("xnm1")
            self.resaltar(F.cas[0], color=AMBAR, run_time=0.5)
            # «Pero ojo»
            self.en("ojo")
            self.pop(ojo)
            # «hay dos pasos»
            self.en("dospasos")
            self.play(Create(llave), FadeIn(dos_p), run_time=self.dur(0.6))
            # «su correlación es cero»
            self.en("cero")
            self.play(FadeIn(cero), run_time=0.4)
