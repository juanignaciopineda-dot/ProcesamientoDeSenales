"""Escena 15 — Mirar la nube antes que el número, y el salto a la proyección."""
from comun.escena import *

O = (-5.0, -2.2)
O3 = np.array([O[0], O[1], 0.0])


class MirarLaNube(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        self.nube()
        self.proyeccion()
        self.wait(1.0)
        self.limpiar()

    def nube(self):
        prom = MathTex(r"\sigma_{XY}", "=", r"\text{promedio de}\ (X-\mu_X)(Y-\mu_Y)", color=TXT)
        prom.scale(0.9).move_to([0, 3.3, 0])
        prom[0].set_color(AMBAR)
        c = (-3.4, -0.3)
        marco = Rectangle(width=5.4, height=3.8, color=INK, stroke_width=2, stroke_opacity=0.7).move_to([c[0], c[1], 0])
        rng = np.random.default_rng(4)
        xs, ys = rng.normal(0, 0.35, 28), rng.normal(0, 0.35, 28)
        pts = VGroup(*[Dot([c[0] + x * 2.2, c[1] + y * 1.5, 0], radius=0.06, color=SENAL) for x, y in zip(xs, ys)])
        lejano = Dot([c[0] + 2.2, c[1] + 1.5, 0], radius=0.1, color=ROJO)
        cen = Dot([c[0], c[1], 0], radius=0.07, color=TXT)
        rect = Rectangle(width=2.2, height=1.5, color=ROJO, fill_color=ROJO, fill_opacity=0.25, stroke_width=3)
        rect.move_to([c[0] + 1.1, c[1] + 0.75, 0])
        c2 = (3.6, -0.3)
        marco2 = Rectangle(width=5.4, height=3.8, color=INK, stroke_width=2, stroke_opacity=0.7).move_to([c2[0], c2[1], 0])
        xx = np.linspace(-1, 1, 24)
        curva = VGroup(*[Dot([c2[0] + x * 2.2, c2[1] + (x ** 2 - 0.35) * 2.6, 0], radius=0.06, color=SENAL) for x in xx])
        r0 = Text("ρ ≈ 0", color=AMBAR, weight=BOLD).scale(0.7).move_to([c2[0], c2[1] + 2.35, 0])
        lup = lupa(TXT).scale(1.4).move_to([c[0] - 1.6, c[1] - 0.3, 0])
        lup.permitir_encima = True
        for m in lup.get_family():
            m.permitir_encima = True
        lema = Text("Mirar la nube antes que el número", color=AMBAR, weight=BOLD).scale(0.75).move_to([0, -3.3, 0])
        with self.narrar("b1"):
            self.en("promedio")
            self.play(FadeIn(prom), run_time=self.dur(1.0))
            self.en("lejano")
            self.play(FadeIn(marco), FadeIn(pts), FadeIn(cen), FadeIn(lejano), run_time=self.dur(0.8))
            self.play(FadeIn(rect), run_time=0.5)
            self.en("domina")
            self.resaltar(rect, color=ROJO, run_time=0.8)
            self.en("recta")
            self.play(FadeOut(rect), FadeIn(marco2), FadeIn(curva), FadeIn(r0), run_time=self.dur(0.8))
            self.en("regla")
            self.play(FadeIn(lema), run_time=self.dur(0.5))
            self.en("mira")
            self.play(FadeIn(lup), run_time=0.4)
            self.play(lup.animate.move_to([c[0] + 1.0, c[1] + 0.4, 0]), run_time=self.dur(1.6))
            self.en("despues")
            self.resaltar(lema, color=AMBAR, run_time=0.6)

    def proyeccion(self):
        self.corte()
        capitulos = Text("8 · 10 · 11 · 12 · 13", color=INK, weight=BOLD).scale(0.8).move_to([2.6, 3.3, 0])
        ang_x, largo_x = 10, 6.4
        X = flecha_c(O, largo_x, ang_x, COL_U7)
        Y = flecha_c(O, 3.9, 55, COL_V7)
        rx = MathTex("X", color=COL_U7).scale(1.0).move_to(X.get_end() + RIGHT * 0.4)
        ry = MathTex("Y", color=COL_V7).scale(1.0).move_to(Y.get_end() + UP * 0.45)
        ux = np.array([np.cos(np.deg2rad(ang_x)), np.sin(np.deg2rad(ang_x)), 0.0])
        pie = O3 + (3.9 * np.cos(np.deg2rad(45))) * ux
        arco = arco7(O, 10, 55, 1.2, AMBAR)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.2).move_to(Y.get_end() + RIGHT * 0.9 + UP * 0.1)
        geo = MathTex(r"\text{¿Qué punto de}\ X\ \text{queda más cerca de}\ Y\,?", color=TXT).scale(0.85).move_to([2.6, 2.1, 0])
        perp = DashedLine(Y.get_end(), pie, color=AMBAR, stroke_width=3)
        sombra = Line(O3, pie, color=ESTIMACION, stroke_width=9)
        dpie = Dot(pie, radius=0.11, color=ESTIMACION)
        pro = self.palabra("Proyección", ESTIMACION, 1.4).move_to([3.2, 0.4, 0])
        with self.narrar("b2"):
            self.en("flechas")
            self.play(GrowArrow(X), GrowArrow(Y), FadeIn(rx), FadeIn(ry), Create(arco), run_time=self.dur(0.9))
            self.en("asignatura")
            self.play(FadeIn(capitulos), run_time=self.dur(0.6))
            self.en("adivinar")
            self.play(FadeIn(interr), run_time=self.dur(0.4))
            self.en("geometrica")
            self.play(FadeIn(geo), run_time=self.dur(0.8))
            self.en("cerca")
            self.play(Create(perp), run_time=self.dur(0.8))
            self.en("siglos")
            self.play(FadeIn(dpie), Create(sombra), run_time=self.dur(0.7))
            self.en("proyeccion")
            self.pop(pro)
            self.sfx("exito")
