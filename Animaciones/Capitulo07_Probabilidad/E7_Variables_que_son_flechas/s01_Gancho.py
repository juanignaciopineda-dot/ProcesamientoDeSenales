"""Escena 01 — Gancho: la correlación es el coseno de un ángulo."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        o = (-3.2, -1.9)
        F = oculta(formula(r"\rho", "=", r"\cos", r"\theta", escala=2.0,
                           colores={0: AMBAR, 3: AMBAR}).move_to([3.0, 2.4, 0]))
        X = flecha_c(o, 3.8, 66, COL_U7)
        Y = flecha_c(o, 3.2, 14, COL_V7)
        arco = arco7(o, 14, 66, 1.1, AMBAR)
        o3 = np.array([o[0], o[1], 0.0])
        rx = MathTex("X", color=COL_U7).scale(1.1).move_to(X.get_end() + UP * 0.6)
        ry = MathTex("Y", color=COL_V7).scale(1.1).move_to(Y.get_end() + RIGHT * 0.65)
        with self.narrar("b1"):
            self.en("rho")
            self.add(F)
            self.play(*revelar(F[0]), run_time=self.dur(0.5))
            self.sfx("pop")
            self.en("coseno")
            self.play(*revelar(F[1], F[2], F[3]), GrowArrow(X), GrowArrow(Y), Create(arco),
                      run_time=self.dur(1.1))
            self.en("flechas")
            self.pop(rx, ry)
            self.en("demostrar")
            self.resaltar(arco, color=AMBAR, escala=1.25, run_time=0.8)
            self.play(X.animate.scale(1.08, about_point=o3),
                      Y.animate.scale(1.08, about_point=o3), run_time=0.6)
        self.wait(1.0)
        self.limpiar()
