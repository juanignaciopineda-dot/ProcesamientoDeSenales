"""Escena 08 — La cuenta: h₀ = 0,476 y h₁ = −0,19, un coeficiente que no es cero."""
from comun.escena import *


class LaCuentaDeLaMuestraVieja(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.ecuaciones()
        self.resultado()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def ecuaciones(self):
        tit = Text("las ecuaciones", color=INK).scale(0.72).move_to([-3.4, 3.4, 0])
        ra = formula("h_0", "+", r"0{,}4\,h_1", "=", r"0{,}4", escala=1.30).move_to([-3.4, 2.4, 0])
        rb = formula(r"0{,}4\,h_0", "+", "h_1", "=", "0", escala=1.30).move_to([-3.4, 1.3, 0])
        desp = MathTex(r"h_1", "=", r"-0{,}4\,h_0", color=TXT).scale(1.30).move_to([4.0, 1.3, 0])
        desp[0].set_color(ESTIMACION)
        fl = CurvedArrow([2.2, 1.7, 0], [-0.3, 2.2, 0], angle=-PI / 4, color=AMBAR, stroke_width=4, tip_length=0.18)
        sust = MathTex(r"h_0", r"+", r"0{,}4\,(-0{,}4\,h_0)", "=", r"0{,}4", color=TXT).scale(1.30).move_to([-3.4, 0.0, 0])
        fact = formula(r"h_0", r"\left(1-0{,}16\right)", "=", r"0{,}4", escala=1.30).move_to([-3.4, -1.1, 0])
        h0 = MathTex(r"h_0", "=", r"0{,}476", color=AMBAR).scale(1.4).move_to([-3.4, -2.5, 0])

        with self.narrar("b1"):
            # «Las ecuaciones»
            self.en("eqs")
            self.play(FadeIn(tit), run_time=0.3)
            # «hache cero más cero coma cuatro hache uno»
            self.en("ea")
            self.play(LaggedStart(*[FadeIn(ra[i]) for i in range(3)], lag_ratio=0.3), run_time=self.dur(0.8))
            # «igual a cero coma cuatro, y»
            self.en("eb")
            self.play(FadeIn(ra[3]), FadeIn(ra[4]), run_time=0.4)
            # «cero coma cuatro hache cero más hache uno»
            self.en("ec")
            self.play(LaggedStart(*[FadeIn(rb[i]) for i in range(3)], lag_ratio=0.3), run_time=self.dur(0.8))
            # «igual a cero. La segunda»
            self.en("ed")
            self.play(FadeIn(rb[3]), FadeIn(rb[4]), run_time=0.4)
            # «La segunda dice»
            self.en("seg")
            self.resaltar(rb, color=AMBAR, run_time=0.5)
            # «hache uno es menos cero coma cuatro hache cero»
            self.en("desp")
            self.play(FadeIn(desp), run_time=self.dur(0.7))
            # «Lo llevamos a la primera»
            self.en("sust")
            self.play(Create(fl), run_time=0.4)
            self.play(FadeIn(sust), run_time=self.dur(0.5))
            # «hache cero por uno menos cero coma dieciséis»
            self.en("fact")
            self.play(FadeIn(fact[0]), FadeIn(fact[1]), run_time=self.dur(0.6))
            # «igual a cero coma cuatro. Hache cero»
            self.en("igual")
            self.play(FadeIn(fact[2]), FadeIn(fact[3]), run_time=0.4)
            # «cero coma cuatro siete seis»
            self.en("h0")
            self.pop(h0)

    # ------------------------------------------------------------------ b2
    def resultado(self):
        h1c = MathTex(r"h_1", "=", r"-0{,}4\cdot", r"0{,}476", color=TXT).scale(1.43).move_to([-3.0, 3.0, 0])
        h1c[0].set_color(ESTIMACION)
        h1 = MathTex(r"=\,-0{,}19", color=AMBAR).scale(1.56).next_to(h1c, RIGHT, buff=0.2)
        nocero = Text("¡no es cero!", color=AMBAR, weight=BOLD).scale(0.91).move_to([4.2, 1.9, 0])
        cer = Text("0", color=INK).scale(1.04).move_to([4.2, 3.0, 0])
        cr = cruz(ROJO, 0.5).move_to(cer)
        F = FilaMuestras([r"x[n-1]", r"x[n]", r"x[n+1]"], centro=(-4.0, 1.2), lado=1.62, color=MEDIDA, escala=0.91)
        llave = BraceBetweenPoints(F.cas[0].get_bottom() + DOWN * 0.1, F.cas[2].get_bottom() + DOWN * 0.1,
                                   direction=DOWN, color=INK)
        sincorr = Text("correlación = 0", color=ERROR).scale(0.72).next_to(llave, DOWN, buff=0.15)
        T = Tallos([-0.19, 0.476], centro=(4.2, -0.6), paso=2.0, unidad=2.6, color=ESTIMACION)
        T.tallos[0].set_color(ERROR), T.puntos[0].set_color(ERROR)
        t_lab = [MathTex(r"x[n-1]", color=MEDIDA).scale(0.91).move_to([T.x(0), -1.4, 0]),
                 MathTex(r"x[n]", color=MEDIDA).scale(0.91).move_to([T.x(1), -1.4, 0])]
        err = MathTex(r"\text{error}", "=", "1", "-", r"0{,}476\cdot 0{,}4", "=", r"0{,}810", color=TXT).scale(1.23)
        err.move_to([-1.8, -2.4, 0])
        err[0].set_color(ERROR), err[6].set_color(ERROR)
        antes = Text("antes: 0,84", color=INK).scale(0.65).move_to([4.0, -2.2, 0])
        baja = Arrow([4.0, -2.0, 0], [4.0, -3.0, 0], color=VERDE, stroke_width=5, buff=0)

        with self.narrar("b2"):
            # «Y hache uno, menos cero coma cuatro por»
            self.en("h1c")
            self.corte()
            self.play(LaggedStart(*[FadeIn(h1c[i]) for i in range(3)], lag_ratio=0.3), run_time=self.dur(0.8))
            # «cero coma cuatro siete seis:»
            self.en("x476")
            self.play(FadeIn(h1c[3]), run_time=0.4)
            # «menos cero coma uno nueve»
            self.en("h1")
            self.pop(h1)
            # «¡No es cero!»
            self.en("nocero")
            self.play(FadeIn(cer), FadeIn(nocero), run_time=0.4)
            self.play(Create(cr), run_time=0.3)
            # «La muestra de hace dos pasos»
            self.en("vieja")
            self.play(FadeIn(F), Create(llave), run_time=self.dur(0.7))
            # «ninguna correlación con la que queremos adivinar»
            self.en("sincorr")
            self.play(FadeIn(sincorr), run_time=0.4)
            # «recibe un coeficiente, y negativo»
            self.en("neg")
            self.play(FadeIn(T), *[FadeIn(m) for m in t_lab], run_time=self.dur(0.7))
            # «Y se nota en el error»
            self.en("nota")
            self.play(FadeIn(err[0]), FadeIn(err[1]), run_time=0.4)
            # «uno menos cero coma cuatro siete seis por cero coma cuatro»
            self.en("cuenta")
            self.play(LaggedStart(*[FadeIn(err[i]) for i in (2, 3, 4)], lag_ratio=0.3), run_time=self.dur(0.9))
            # «cero coma ocho uno. Baja»
            self.en("e081")
            self.play(FadeIn(err[5]), FadeIn(err[6]), run_time=0.4)
            # «Baja.»
            self.en("baja")
            self.play(FadeIn(antes), Create(baja), run_time=0.5)
