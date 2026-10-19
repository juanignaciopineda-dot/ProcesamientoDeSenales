"""Escena 13 — La sorpresa como dato nuevo: ganancia 0,8 / 4,8 = 1/6; 22,33 y 0,67, como con el sistema."""
from comun.escena import *
from comun.figuras_c8e5 import *


class LaGanancia(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.factor()
        self.corregir()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def factor(self):
        dato = caja("Sorpresa = −0,4", CIAN, scale=0.6).move_to([-4.2, 3.0, 0])
        recta = MathTex(r"\hat{y}=20+h\,(x-20)", color=INK).scale(0.85).move_to([3.6, 3.05, 0])
        cv = MathTex(r"\text{Factor}=\frac{\mathrm{cov}}{\mathrm{var}}", color=TXT).scale(0.95).move_to([3.6, 1.8, 0])
        f = formula(r"\text{Sorpresa}", "=", r"(y-\hat{y})", "+", "v_B", escala=1.1,
                    colores={2: ERROR, 4: RUIDO}).move_to([-1.4, 0.4, 0])
        v08 = MathTex(r"\sigma^2=0{,}8", color=ERROR).scale(0.8).next_to(f[2], DOWN, buff=0.3)
        v4 = MathTex(r"\sigma^2=4", color=RUIDO).scale(0.8).next_to(f[4], DOWN, buff=0.3)
        v48 = MathTex(r"\mathrm{var}=0{,}8+4=4{,}8", color=TXT).scale(0.95).move_to([-3.4, -1.65, 0])
        comp = MathTex(r"\mathrm{cov}=0{,}8", color=TXT).scale(0.95).move_to([2.4, -1.65, 0])
        fac = formula(r"\text{Factor}=", r"\frac{0{,}8}{4{,}8}", r"=\frac{1}{6}", escala=1.1, colores={2: VERDE})
        fac.move_to([-0.6, -3.0, 0])

        with self.narrar("b1"):
            # «La sorpresa es un dato nuevo»
            self.en("dato")
            self.play(FadeIn(dato, shift=DOWN * 0.1), run_time=self.dur(0.5))

            # «la fórmula de la recta de siempre»
            self.en("recta")
            self.play(FadeIn(recta), run_time=self.dur(0.5))

            # «covarianza entre varianza»
            self.en("cv")
            self.play(FadeIn(cv, shift=UP * 0.1), run_time=self.dur(0.5))

            # «del error que todavía tenías»
            self.en("err")
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.6))

            # «de varianza cero coma ocho»
            self.en("v08")
            self.play(FadeIn(v08, shift=UP * 0.1), run_time=self.dur(0.4))

            # «más el ruido de B»
            self.en("vb")
            self.play(FadeIn(f[3]), FadeIn(f[4], shift=UP * 0.1), run_time=self.dur(0.4))

            # «de varianza cuatro»
            self.en("v4")
            self.play(FadeIn(v4, shift=UP * 0.1), run_time=self.dur(0.4))

            # «la suma, cuatro coma ocho»
            self.en("v48")
            self.play(FadeIn(v48, shift=UP * 0.1), run_time=self.dur(0.6))

            # «lo que comparte con tu error»
            self.en("comp")
            self.resaltar(f[2], color=AMBAR, escala=1.15)
            self.play(FadeIn(comp, shift=UP * 0.1), run_time=self.dur(0.5))

            # «El factor es»
            self.en("factor")
            self.play(FadeIn(fac[0]), run_time=self.dur(0.3))

            # «cero coma ocho entre cuatro coma ocho»
            self.en("div")
            self.play(FadeIn(fac[1], shift=UP * 0.1), run_time=self.dur(0.5))

            # «un sexto»
            self.en("sexto")
            self.pop(fac[2])

    # ------------------------------------------------------------ b2
    def corregir(self):
        X0 = -6.4
        f1 = formula(r"\hat{y}_{\text{nueva}}", "=", r"22{,}4", r"+\frac{1}{6}\cdot(-0{,}4)", escala=1.05,
                     colores={0: ESTIMACION}).move_to([X0, 2.4, 0], aligned_edge=LEFT)
        f2 = formula("=", r"22{,}4", r"-0{,}067", r"\approx 22{,}33", escala=1.05, colores={3: ESTIMACION})
        f2.move_to([0, 0.9, 0])
        f2.shift(RIGHT * (f1[1].get_x() - f2[0].get_x()))
        f3 = formula(r"\text{Error}", "=", r"0{,}8\cdot\frac{5}{6}", r"\approx 0{,}67", escala=1.05,
                     colores={0: ERROR, 3: ERROR}).move_to([X0, -1.2, 0], aligned_edge=LEFT)
        tarjeta = RoundedRectangle(corner_radius=0.2, width=2.6, height=4.0, color=INK, stroke_width=3)
        tarjeta.set_fill(INK, 0.08).move_to([5.4, 0.1, 0])
        tit = Text("Sistema", color=INK, weight=BOLD).scale(0.55).move_to([5.4, 1.75, 0])
        s1 = MathTex(r"22{,}33", color=ESTIMACION).scale(1.05).move_to([5.4, f2.get_y(), 0])
        s2 = MathTex(r"0{,}67", color=ERROR).scale(1.05).move_to([5.4, f3.get_y(), 0])
        x_ig = tarjeta.get_left()[0] - 0.5
        ig1 = MathTex("=", color=VERDE).scale(1.2).move_to([x_ig, f2.get_y(), 0])
        ig2 = MathTex("=", color=VERDE).scale(1.2).move_to([x_ig, f3.get_y(), 0])
        ok = tilde(VERDE, 0.5).move_to([6.35, 2.55, 0])

        with self.narrar("b2"):
            # «La estimación nueva»
            self.en("nueva")
            self.corte()
            self.play(FadeIn(f1[0]), FadeIn(f1[1]), run_time=self.dur(0.4))

            # «es la vieja»
            self.en("vieja")
            self.play(FadeIn(f1[2], shift=UP * 0.1), run_time=self.dur(0.3))

            # «más un sexto por la sorpresa»
            self.en("mas")
            self.play(FadeIn(f1[3], shift=UP * 0.1), run_time=self.dur(0.6))

            # «Veintidós coma cuatro, menos»
            self.en("v224")
            self.play(FadeIn(f2[0]), FadeIn(f2[1], shift=UP * 0.1), run_time=self.dur(0.4))

            # «menos cero coma cero seis siete»
            self.en("m067")
            self.play(FadeIn(f2[2], shift=UP * 0.1), run_time=self.dur(0.4))

            # «veintidós coma tres tres»
            self.en("r2233")
            self.pop(f2[3])

            # «resolviendo el sistema entero»
            self.en("sis")
            self.play(FadeIn(tarjeta), FadeIn(tit), FadeIn(s1), run_time=self.dur(0.5))
            self.play(FadeIn(ig1, scale=0.5), run_time=0.3)

            # «el error baja»
            self.en("eb")
            self.play(FadeIn(f3[0]), FadeIn(f3[1]), run_time=self.dur(0.4))

            # «cero coma ocho por cinco sextos»
            self.en("p56")
            self.play(FadeIn(f3[2], shift=UP * 0.1), run_time=self.dur(0.5))

            # «que da cero coma seis siete»
            self.en("e067")
            self.play(FadeIn(f3[3], shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «También coincide»
            self.en("coinc")
            self.play(FadeIn(s2), FadeIn(ig2, scale=0.5), run_time=self.dur(0.4))
            self.play(Create(ok), run_time=0.4)
            self.sfx("exito")
