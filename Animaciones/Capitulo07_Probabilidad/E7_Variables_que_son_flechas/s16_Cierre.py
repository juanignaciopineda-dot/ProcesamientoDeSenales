"""Escena 16 — Cierre: el capítulo 7 en una flecha y el anuncio del capítulo 8."""
from comun.escena import *

O = (-4.6, -2.0)
O3 = np.array([O[0], O[1], 0.0])


class Cierre(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        X = flecha_c(O, 3.4, 68, COL_U7)
        Y = flecha_c(O, 3.0, 12, COL_V7)
        rx = MathTex("X", color=COL_U7).scale(1.0).move_to(X.get_end() + UP * 0.45)
        ry = MathTex("Y", color=COL_V7).scale(1.0).move_to(Y.get_end() + RIGHT * 0.5)
        arco = arco7(O, 12, 68, 1.0, AMBAR)
        va = Text("Variable aleatoria = flecha", color=TXT, weight=BOLD).scale(0.6).move_to([2.8, 2.9, 0])
        lg = MathTex(r"\text{Largo}", "=", r"\sigma_X", color=TXT).scale(1.2).move_to([2.8, 1.6, 0])
        lg[2].set_color(AMBAR)
        rho = MathTex(r"\rho", "=", r"\cos\theta", color=TXT).scale(1.5).move_to([2.8, 0.1, 0])
        rho[0].set_color(AMBAR)
        rho[2].set_color(AMBAR)
        barra0 = Rectangle(width=8.0, height=0.4, color=INK, stroke_width=3).move_to([0, -3.4, 0])
        barra = Rectangle(width=8.0, height=0.4, color=VERDE, fill_color=VERDE, fill_opacity=0.7,
                          stroke_width=0).move_to([0, -3.4, 0])
        cap = Text("Capítulo 7", color=TXT).scale(0.55).move_to([0, -2.8, 0])
        ok = tilde(VERDE, 0.9).move_to([4.9, -3.4, 0])
        d = dado(TXT).scale(1.8).move_to([-3.0, 0.6, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(2.0).move_to([-1.0, 0.6, 0])
        pregunta = Text("¿Cuál es tu mejor apuesta?", color=AMBAR, weight=BOLD).scale(1.1).move_to([0, -1.6, 0])
        prox = Text("Capítulo 8 · Estimación", color=INK).scale(0.7).move_to([0, 2.7, 0])
        with self.narrar("b1"):
            self.en("flecha")
            self.play(GrowArrow(X), FadeIn(rx), FadeIn(va), run_time=self.dur(0.9))
            self.en("largo")
            self.play(FadeIn(lg), run_time=self.dur(0.6))
            self.en("rho")
            self.play(GrowArrow(Y), FadeIn(ry), Create(arco), FadeIn(rho), run_time=self.dur(0.9))
            self.en("conesto")
            self.resaltar(rho, color=AMBAR, run_time=0.6)
            self.en("completo")
            self.play(FadeIn(barra0), FadeIn(cap), run_time=0.3)
            self.play(GrowFromEdge(barra, LEFT), run_time=self.dur(1.0))
            self.play(FadeIn(ok), run_time=0.3)
            self.sfx("exito")
            self.en("usarlo")
            self.play(*[FadeOut(m) for m in (X, Y, rx, ry, arco, va, lg, rho, barra0, barra, cap, ok)],
                      FadeIn(d), run_time=self.dur(0.7))
            self.en("adivinar")
            self.pop(q)
            self.en("apuesta")
            self.pop(pregunta)
            self.en("proximo")
            self.play(FadeIn(prox), run_time=self.dur(0.6))
        self.wait(1.2)
        self.limpiar()
