"""Escena 08 — Rho es el coseno del ángulo: u·v = |u||v|cosθ traducido a σ_XY = σ_X σ_Y cosθ."""
from comun.escena import *

O = (-5.2, -2.3)
O3 = np.array([O[0], O[1], 0.0])
K = 1.3


class CosenoDelAngulo(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.X = flecha_c(O, np.sqrt(6) * K, 52.2, COL_U7)
        self.Y = flecha_c(O, 2 * K, 0, COL_V7)
        self.arco = arco7(O, 0, 52.2, 1.1, AMBAR)
        self.add(self.X, self.Y, self.arco)
        self.coseno()
        self.nombre()
        self.wait(1.0)
        self.limpiar()

    def coseno(self):
        f1 = oculta(MathTex("u", r"\cdot", "v", "=", "|u|", "|v|", r"\cos\theta", color=TXT)
                    .scale(1.1).move_to([2.2, 3.0, 0]))
        f1[0].set_color(COL_U7)
        f1[2].set_color(COL_V7)
        f1[6].set_color(AMBAR)
        f2 = oculta(MathTex(r"\sigma_{XY}", "=", r"\sigma_X", r"\sigma_Y", r"\cos\theta", color=TXT)
                    .scale(1.1).move_to([2.2, 1.6, 0]))
        f2[0].set_color(AMBAR)
        f2[4].set_color(AMBAR)
        desp = Text("Despejando", color=INK).scale(0.5).move_to([-0.2, 0.6, 0])
        f3 = oculta(MathTex(r"\cos\theta", "=", r"\dfrac{\sigma_{XY}}{\sigma_X\,\sigma_Y}", color=TXT)
                    .scale(1.2).move_to([2.2, -0.5, 0]))
        f3[0].set_color(AMBAR)
        self.f3 = f3
        self.add(f1, f2, f3)
        with self.narrar("b1"):
            self.en("plano")
            self.play(*revelar(f1[0], f1[1], f1[2], f1[3]), run_time=0.5)
            self.play(*revelar(f1[4], f1[5]), run_time=0.7)
            self.en("cos")
            self.play(*revelar(f1[6]), run_time=0.4)
            self.resaltar(self.arco, color=AMBAR, escala=1.2, run_time=0.6)
            self.en("traduce")
            self.play(*revelar(f2), run_time=self.dur(0.9))
            self.en("sigmas")
            self.resaltar(f2[2], f2[3], color=AMBAR, run_time=0.6)
            self.en("despeja")
            self.play(FadeIn(desp), run_time=self.dur(0.4))
            self.en("cociente")
            self.play(*revelar(f3), run_time=self.dur(1.2))
            self.play(FadeOut(desp), run_time=0.3)
        self.rest = [f1, f2]

    def nombre(self):
        f3 = self.f3
        caja_ = SurroundingRectangle(f3, color=AMBAR, buff=0.15, stroke_width=3)
        pregunta = Text("Número nuevo", color=AMBAR).scale(0.6).next_to(caja_, UP, buff=0.1)
        rho = MathTex("=", r"\rho", color=TXT).scale(1.3).next_to(f3, RIGHT, buff=0.2)
        rho[1].set_color(AMBAR)
        grande = MathTex(r"\rho", "=", r"\cos\theta", color=TXT).scale(1.7).move_to([2.2, -2.0, 0])
        grande[0].set_color(AMBAR)
        grande[2].set_color(AMBAR)
        rotx = MathTex(r"X-\mu_X", color=COL_U7).scale(0.8).move_to(self.X.get_end() + UP * 0.55)
        roty = MathTex(r"Y-\mu_Y", color=COL_V7).scale(0.8).move_to(self.Y.get_end() + RIGHT * 0.9)
        cuenta = MathTex(r"\dfrac{3}{\sqrt{6}\cdot 2}", color=TXT).scale(1.1).move_to([2.2, -3.2, 0])
        v612 = MathTex(r"\approx", num_tex(0.612), color=AMBAR).scale(1.3).next_to(cuenta, RIGHT, buff=0.3)
        th = MathTex(r"\theta\approx 52^\circ", color=AMBAR).scale(0.8).move_to(O3 + np.array([2.2, 0.75, 0]))
        with self.narrar("b2"):
            self.en("nombre")
            self.play(Create(caja_), FadeIn(pregunta), run_time=self.dur(0.5))
            self.en("rho")
            self.play(FadeOut(pregunta), FadeIn(rho), run_time=self.dur(0.5))
            self.sfx("pop")
            self.en("literal")
            self.play(FadeIn(grande), run_time=self.dur(0.6))
            self.resaltar(self.arco, color=AMBAR, escala=1.2, run_time=0.6)
            self.en("centradas")
            self.play(FadeIn(rotx), FadeIn(roty), run_time=self.dur(0.6))
            self.en("ejemplo")
            self.play(FadeOut(self.rest[0]), FadeOut(self.rest[1]), FadeOut(caja_), run_time=self.dur(0.5))
            self.en("cuenta")
            self.play(FadeIn(cuenta), run_time=self.dur(0.8))
            self.en("v612")
            self.play(FadeIn(v612), run_time=self.dur(0.5))
            self.en("grados")
            self.play(FadeIn(th), run_time=self.dur(0.5))
