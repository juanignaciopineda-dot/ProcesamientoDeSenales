"""Escena 09 — Leer rho de un vistazo: flechas, nube y deslizador (1, 0, −1 y el canal de bits)."""
from comun.escena import *

O = (-3.6, 0.7)
O3 = np.array([O[0], O[1], 0.0])
DESL_Y = -2.9
DESL_X = (-4.0, 4.0)


class LeerRho(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        rho = ValueTracker(0.6)

        def ang():
            return float(np.arccos(np.clip(rho.get_value(), -1, 1)))

        X = flecha_c(O, 2.6, 0, COL_U7)
        Y = always_redraw(lambda: flecha_c(O, 2.6, np.rad2deg(ang()), COL_V7))
        rx = MathTex("X", color=COL_U7).scale(0.9).move_to(O3 + np.array([2.9, -0.4, 0]))
        ry = always_redraw(lambda: MathTex("Y", color=COL_V7).scale(0.9).move_to(
            O3 + 3.1 * np.array([np.cos(ang()), np.sin(ang()), 0.0]) + np.array([0, 0.05, 0])))
        arco = always_redraw(lambda: Arc(radius=0.9, start_angle=0, angle=max(ang(), 1e-3), arc_center=O3,
                                         color=AMBAR, stroke_width=4))
        nube = always_redraw(lambda: nube7((3.2, 0.7), rho.get_value(), n=45, ancho=4.2, semilla=5, color=SENAL))
        marco = Rectangle(width=4.6, height=4.2, color=INK, stroke_width=2, stroke_opacity=0.6).move_to([3.2, 0.7, 0])
        linea = Line([DESL_X[0], DESL_Y, 0], [DESL_X[1], DESL_Y, 0], color=INK, stroke_width=3)
        marcas = VGroup(*[Line([x, DESL_Y - 0.12, 0], [x, DESL_Y + 0.12, 0], color=INK, stroke_width=3)
                          for x in (-4.0, 0.0, 4.0)])
        nums = VGroup(MathTex("-1", color=INK).scale(0.7).move_to([-4.0, DESL_Y - 0.45, 0]),
                      MathTex("0", color=INK).scale(0.7).move_to([0, DESL_Y - 0.45, 0]),
                      MathTex("1", color=INK).scale(0.7).move_to([4.0, DESL_Y - 0.45, 0]))
        bola = always_redraw(lambda: Dot([4.0 * rho.get_value(), DESL_Y, 0], radius=0.14, color=AMBAR))
        lab = always_redraw(lambda: Text(f"ρ = {num(rho.get_value())}", color=AMBAR, weight=BOLD).scale(0.7)
                            .move_to([0, DESL_Y + 0.65, 0]))
        sube = Text("Sube", color=VERDE).scale(0.55).move_to([3.2, 3.15, 0])
        redonda = Text("Sin recta", color=INK).scale(0.55).move_to([3.2, 3.15, 0])
        baja = Text("Baja", color=ROJO).scale(0.55).move_to([3.2, 3.15, 0])
        canal = caja("Canal de bits", AMBAR, ancho=3.4, alto=0.8, scale=0.5).move_to([-4.0, 3.0, 0])
        v077 = Text("ρ ≈ 0,77", color=AMBAR, weight=BOLD).scale(0.7).move_to([-4.0, 2.2, 0])
        with self.narrar("b1"):
            self.en("vistazo")
            self.play(Create(linea), FadeIn(marcas), FadeIn(nums), FadeIn(X), FadeIn(rx), FadeIn(marco),
                      run_time=self.dur(0.7))
            self.add(Y, ry, arco, nube, bola, lab)
            self.en("uno")
            self.play(rho.animate.set_value(1.0), run_time=self.dur(1.2))
            self.en("mismo")
            self.resaltar(X, color=AMBAR, run_time=0.5)
            self.en("sube")
            self.play(FadeIn(sube), run_time=0.4)
            self.en("cero")
            self.play(FadeOut(sube), rho.animate.set_value(0.0), run_time=self.dur(1.4))
            self.en("redonda")
            self.play(FadeIn(redonda), run_time=0.4)
            self.en("menos")
            self.play(FadeOut(redonda), rho.animate.set_value(-1.0), run_time=self.dur(1.6))
            self.en("baja")
            self.play(FadeIn(baja), run_time=0.4)
            self.en("canal")
            self.play(FadeOut(baja), FadeIn(canal), rho.animate.set_value(0.77), run_time=self.dur(1.2))
            self.en("v077")
            self.play(FadeIn(v077), run_time=self.dur(0.4))
        self.wait(1.0)
        self.limpiar()
