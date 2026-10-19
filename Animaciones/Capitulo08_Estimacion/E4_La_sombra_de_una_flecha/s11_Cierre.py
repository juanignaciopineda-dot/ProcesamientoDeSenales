"""Escena 11 — Cierre: estimar con una recta es proyectar; anuncia «¿Dos termómetros mejor que uno?»."""
from comun.escena import *
from comun.figuras_c8e4 import *


class Cierre(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        F, r = flechas8(origen=(-3.0, -2.0), k=1.9)
        fig = VGroup(F.presente, F.futuro, F.sombra, F.error, F.recto, r["x"], r["y"], r["yh"], r["e"])
        xs = np.linspace(-3, 3, 80)
        campana = traza(3.4 + xs * 0.7, -1.6 + 3.6 * gaussiana(xs, 0, 1), SENAL, 5)
        base = Line([1.0, -1.6, 0], [5.8, -1.6, 0], color=INK, stroke_width=2)
        ok = tilde(VERDE, 0.6).move_to([3.4, 2.2, 0])
        t1 = termometro(alto=2.6)
        t1.move_to([0, -0.4, 0])
        t2 = t1.copy()
        rng = np.random.default_rng(3)
        xr = np.linspace(-3.6, 3.6, 70)
        ruido = traza(xr, -0.4 + 0.35 * rng.normal(0, 1, 70), RUIDO, 3, 0.8)
        titulo_p = Text("¿Dos termómetros mejor que uno?", color=AMBAR, weight=BOLD).scale(0.95).move_to([0, 3.0, 0])

        with self.narrar("b1"):
            # «estimar con una recta es proyectar»
            self.en("proyectar")
            self.play(Create(F.presente), Create(F.futuro), FadeIn(r["x"]), FadeIn(r["y"]), run_time=self.dur(0.7))
            self.play(Create(F.sombra), Create(F.error), Create(F.recto), FadeIn(r["yh"]), FadeIn(r["e"]),
                      run_time=self.dur(0.7))

            # «la sombra de la temperatura»
            self.en("sombra")
            self.resaltar(F.sombra, color=AMBAR, escala=1.04)

            # «el error es el cateto»
            self.en("cateto")
            self.resaltar(F.error, color=ERROR, escala=1.06)

            # «Con gaussianas»
            self.en("congauss")
            self.play(fig.animate.scale(0.6, about_point=F.o).shift(LEFT * 0.6 + UP * 0.3), Create(base), Create(campana),
                      run_time=self.dur(0.9))

            # «ninguna otra regla la supera»
            self.en("supera")
            self.play(FadeIn(ok, scale=0.4), run_time=self.dur(0.5))

            # «un termómetro tiene un límite»
            self.en("limite")
            self.play(*[FadeOut(m) for m in (fig, base, campana, ok)], run_time=self.dur(0.4))
            self.play(FadeIn(t1, shift=UP * 0.3), run_time=self.dur(0.6))

            # «el ruido»
            self.en("ruido")
            self.play(Create(ruido), run_time=self.dur(0.9))

            # «¿Y si pusiéramos dos?»
            self.en("dos")
            self.play(FadeOut(ruido), t1.animate.shift(LEFT * 1.6), FadeIn(t2.shift(RIGHT * 1.6)), run_time=self.dur(0.8))

            # «¿Dos termómetros mejor que uno?»
            self.en("titulo")
            self.pop(titulo_p)
        self.wait(0.8)
        self.limpiar()
