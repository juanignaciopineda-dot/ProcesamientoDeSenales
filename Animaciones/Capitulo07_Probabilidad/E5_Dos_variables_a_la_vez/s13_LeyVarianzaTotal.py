"""Escena 13 — La ley de la varianza total y su lectura: lo que explica el grupo y lo que no."""
from comun.escena import *


class LeyVarianzaTotal(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        bar = BarrasVar7(origen=(-4.09, 0.2), esc=0.1, alto=1.0)
        self.bar = bar
        ini_d, ini_e = bar.dentro.get_center().copy(), bar.entre.get_center().copy()
        bar.dentro.shift(LEFT * 2.0 + UP * 1.1)
        bar.entre.shift(RIGHT * 2.0 + UP * 1.1)
        t1 = MathTex(r"41{,}2", color=TXT).scale(1.0).move_to(ini_d)
        t2 = MathTex(r"40{,}56", color=TXT).scale(1.0).move_to(ini_e)
        suma = MathTex(r"41{,}2+40{,}56=81{,}76", color=AMBAR).scale(1.2).move_to([0, 1.7, 0])
        sig = MathTex(r"\sigma\approx9\ \text{cm}", color=TXT).scale(1.1).move_to([0, 1.7, 0])
        mitad = DashedLine([float(bar.o[0]) + 41.2 * 0.1, 0.2 - 0.8, 0], [float(bar.o[0]) + 41.2 * 0.1, 0.2 + 0.8, 0],
                           color=TXT, stroke_width=3)
        ley = self.palabra("ley de la varianza total", AMBAR, 0.9).move_to([0, 3.4, 0])
        formula_ = formula(r"\mathrm{Var}(X)", "=", r"E\big[\mathrm{Var}(X\mid Y)\big]", "+",
                           r"\mathrm{Var}\big(E[X\mid Y]\big)", escala=1.05,
                           colores={2: ROJO, 4: VERDE}).move_to([0, -2.1, 0])
        rot_d = Text("dentro de los grupos", color=ROJO).scale(0.55).next_to(formula_[2], DOWN, buff=0.3)
        rot_e = Text("entre los grupos", color=VERDE).scale(0.55).next_to(formula_[4], DOWN, buff=0.3)
        with self.narrar("b1"):
            # «la suma de los dos trozos»
            self.en("suma")
            self.play(FadeIn(bar.dentro), FadeIn(bar.entre), FadeIn(t1.move_to(bar.dentro)), FadeIn(t2.move_to(bar.entre)),
                      run_time=self.dur(0.5))
            self.play(bar.dentro.animate.move_to(ini_d), bar.entre.animate.move_to(ini_e),
                      t1.animate.move_to(ini_d), t2.animate.move_to(ini_e), run_time=self.dur(0.9))

            # «ochenta y uno coma setenta y seis»
            self.en("r8176")
            self.play(FadeIn(suma, shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «unos nueve centímetros»
            self.en("sigma9")
            self.play(ReplacementTransform(suma, sig), run_time=self.dur(0.6))

            # «Casi mitad y mitad»
            self.en("mitad")
            self.play(Create(mitad), run_time=self.dur(0.5))

            # «la ley de la varianza total»
            self.en("ley")
            self.pop(ley)

            # «la media de las varianzas dentro de los grupos»
            self.en("f_dentro")
            self.play(FadeIn(formula_[0:3], shift=UP * 0.15), run_time=self.dur(0.9))
            self.play(FadeIn(rot_d), run_time=0.3)
            self.resaltar(bar.dentro, color=ROJO, escala=1.1, run_time=0.5)

            # «la varianza de las medias de los grupos»
            self.en("f_entre")
            self.play(FadeIn(formula_[3:], shift=UP * 0.15), run_time=self.dur(0.9))
            self.play(FadeIn(rot_e), run_time=0.3)
            self.resaltar(bar.entre, color=VERDE, escala=1.1, run_time=0.5)
        self.resto = VGroup(sig, mitad, ley, formula_, rot_d, rot_e, t1, t2)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        bar = self.bar
        explica = Text("lo que explica el grupo", color=VERDE).scale(0.7).next_to(bar.entre, DOWN, buff=0.35)
        no_explica = Text("lo que no explica el grupo", color=ROJO).scale(0.7).next_to(bar.dentro, UP, buff=0.35)
        marco = SurroundingRectangle(bar.dentro, color=AMBAR, buff=0.12, stroke_width=6)
        x = MathTex("X", color=SENAL).scale(1.3).move_to([-2.6, -2.3, 0])
        y = MathTex("Y", color=MEDIDA).scale(1.3).move_to([-0.6, -2.3, 0])
        flecha_ = Arrow(y.get_left() + LEFT * 0.1, x.get_right() + RIGHT * 0.1, color=INK, buff=0.1, stroke_width=5)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.2).next_to(flecha_, UP, buff=0.1)
        sello = Text("lo mejor posible", color=AMBAR, weight=BOLD).scale(0.7).move_to([3.9, -2.3, 0])
        with self.narrar("b2"):
            # «lo que saber el grupo explica»
            self.en("explica")
            self.play(FadeOut(self.resto), run_time=0.3)
            bar.entre.set_fill(VERDE, 0.7)
            self.play(FadeIn(explica, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «El primero»
            self.en("primero")
            self.resaltar(bar.dentro, color=ROJO, escala=1.1, run_time=0.5)

            # «sigue sin saberse»
            self.en("sin_saber")
            self.play(FadeIn(no_explica, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «Guarda esta idea»
            self.en("guarda")
            self.play(Create(marco), run_time=self.dur(0.5))

            # «adivinar una variable a partir de otra»
            self.en("adivinar")
            self.play(FadeIn(x), FadeIn(y), run_time=0.3)
            self.play(GrowArrow(flecha_), FadeIn(interr), run_time=self.dur(0.6))

            # «el error que cometeremos»
            self.en("error")
            err = Text("error", color=ERROR, weight=BOLD).scale(0.8).move_to([-1.6, -3.1, 0])
            self.pop(err)

            # «lo mejor posible»
            self.en("mejor")
            self.pop(sello)

            # «ese primer trozo»
            self.en("trozo")
            self.resaltar(marco, color=AMBAR, escala=1.1, run_time=0.7)
