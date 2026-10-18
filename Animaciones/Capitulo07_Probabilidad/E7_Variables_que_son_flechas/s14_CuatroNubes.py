"""Escena 14 — Cuatro nubes con el mismo rho (≈ 0,85) y nada que ver entre sí."""
from comun.escena import *

CENTROS = [(-3.6, 1.55), (3.6, 1.55), (-3.6, -1.95), (3.6, -1.95)]
RHO = "ρ ≈ 0,85"


def marco_n(c):
    return Rectangle(width=5.4, height=3.1, color=INK, stroke_width=2, stroke_opacity=0.7).move_to([c[0], c[1], 0])


def puntos_en(c, xs, ys, color=SENAL, radio=0.06):
    """Puntos con coordenadas en [-1, 1] dentro del marco de centro c."""
    return VGroup(*[Dot([c[0] + x * 2.3, c[1] + y * 1.15, 0], radius=radio, color=color) for x, y in zip(xs, ys)])


class CuatroNubes(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        c1, c2, c3, c4 = CENTROS
        rng = np.random.default_rng(11)
        x1 = rng.uniform(-1, 1, 40)
        y1 = np.clip(0.85 * x1 + rng.normal(0, 0.25, 40), -1, 1)
        n1 = puntos_en(c1, x1, y1)
        x2 = np.linspace(-0.9, 0.9, 30)
        y2 = (x2 + 0.9) ** 2 / 3.24 * 1.8 - 0.9
        n2 = puntos_en(c2, x2, y2)
        x3 = np.linspace(-0.9, 0.9, 28)
        n3 = puntos_en(c3, x3, 0.85 * x3)
        esc = Dot([c3[0] + 0.6 * 2.3, c3[1] - 0.85 * 1.15, 0], radius=0.1, color=ROJO)
        x4 = rng.normal(-0.5, 0.03, 30)
        y4 = rng.uniform(-0.8, 0.8, 30)
        n4 = puntos_en(c4, x4, y4)
        lej = Dot([c4[0] + 0.9 * 2.3, c4[1] + 0.9 * 1.15, 0], radius=0.1, color=ROJO)
        marcos = [marco_n(c) for c in CENTROS]
        rhos = [Text(RHO, color=AMBAR).scale(0.5).move_to([c[0] - 1.7, c[1] + 1.2, 0]) for c in CENTROS]
        ajuste1 = Line([c1[0] - 2.3, c1[1] - 0.95, 0], [c1[0] + 2.3, c1[1] + 0.95, 0], color=AMBAR, stroke_width=4)
        ajuste2 = Line([c2[0] - 2.2, c2[1] - 1.0, 0], [c2[0] + 2.2, c2[1] + 1.0, 0], color=ROJO, stroke_width=4)
        ajuste4 = Line([c4[0] - 1.4, c4[1] - 1.0, 0], [c4[0] + 2.1, c4[1] + 1.1, 0], color=ROJO, stroke_width=4)
        col4 = SurroundingRectangle(n4, color=AMBAR, buff=0.12, stroke_width=3)

        nube0 = nube7((-3.2, 0.2), 0.85, n=45, ancho=4.0, semilla=5)
        marco0 = marco_n((-3.2, 0.2))
        r0 = Text(RHO, color=AMBAR, weight=BOLD).scale(1.4).move_to([3.4, 0.2, 0])
        flecha_ = Arrow([-0.2, 0.2, 0], [1.5, 0.2, 0], buff=0.0, color=INK, stroke_width=4)
        with self.narrar("b1"):
            self.en("resumen")
            self.play(FadeIn(marco0), FadeIn(nube0), run_time=self.dur(0.6))
            self.play(GrowArrow(flecha_), run_time=0.4)
            self.pop(r0)
            self.en("precio")
            self.play(FadeOut(nube0), FadeOut(marco0), FadeOut(flecha_), run_time=self.dur(0.6))
            self.sfx("error")
            self.en("cuatro")
            self.play(FadeOut(r0), *[FadeIn(m) for m in marcos], FadeIn(n1), FadeIn(n2), FadeIn(n3), FadeIn(n4),
                      FadeIn(esc), FadeIn(lej), run_time=self.dur(1.0))
            self.en("mismo")
            self.play(*[FadeIn(r) for r in rhos], run_time=self.dur(0.6))
            self.en("nada")
            for m in marcos:
                self.play(m.animate.set_stroke(AMBAR, opacity=1), run_time=0.25)
                self.play(m.animate.set_stroke(INK, opacity=0.7), run_time=0.2)
        with self.narrar("b2"):
            self.en("primera")
            self.play(marcos[0].animate.set_stroke(AMBAR, opacity=1), run_time=self.dur(0.4))
            self.en("ruido")
            self.play(Create(ajuste1), run_time=self.dur(0.6))
            self.en("segunda")
            self.play(marcos[0].animate.set_stroke(INK, opacity=0.7), marcos[1].animate.set_stroke(AMBAR, opacity=1),
                      run_time=self.dur(0.4))
            self.en("equivocado")
            self.play(Create(ajuste2), run_time=self.dur(0.7))
            self.en("tercera")
            self.play(marcos[1].animate.set_stroke(INK, opacity=0.7), marcos[2].animate.set_stroke(AMBAR, opacity=1),
                      run_time=self.dur(0.4))
            self.en("escapado")
            self.play(esc.animate.scale(2.0), run_time=0.4)
            self.play(esc.animate.scale(0.5), run_time=0.4)
            self.en("indique")
            self.resaltar(rhos[2], color=AMBAR, run_time=0.6)
            self.en("cuarta")
            self.play(marcos[2].animate.set_stroke(INK, opacity=0.7), marcos[3].animate.set_stroke(AMBAR, opacity=1),
                      run_time=self.dur(0.4))
            self.en("columna")
            self.play(Create(col4), run_time=self.dur(0.6))
            self.en("lejos")
            self.play(esc.animate.scale(1.0), lej.animate.scale(2.0), run_time=self.dur(0.5))
            self.play(lej.animate.scale(0.5), run_time=0.3)
            self.en("inventa")
            self.play(FadeOut(col4), Create(ajuste4), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
