"""Escena 06 — Rebanada por rebanada: observado X = x, apuesta la media de la rebanada; el error es su varianza."""
from comun.escena import *


class RebanadaPorRebanada(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.nube = Nube8(centro=(-2.6, -0.2), ancho=7.0, alto=5.4, n=90, semilla=11)
        self.panel = Rectangle(width=2.0, height=4.4, color=INK, stroke_width=3).set_fill(INK, 0.06).move_to([4.4, 0.0, 0])
        self.una()
        self.todas()
        self.wait(1.0)
        self.limpiar()

    def una(self):
        n = self.nube
        x0 = 1.2
        idx = n.en_rebanada(x0, 0.6)
        with self.narrar("b1"):
            # «funciona siempre»
            self.en("siempre")
            self.play(Create(n.ax), FadeIn(n.etq), run_time=self.dur(0.5))
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in n.pts], lag_ratio=0.01), run_time=self.dur(1.2))

            # «equis»
            self.en("equis")
            X = MathTex("X", color=SENAL).scale(1.3).move_to([-2.6, -3.4, 0])
            self.pop(X)

            # «i griega»
            self.en("griega")
            Y = MathTex("Y", color=MEDIDA).scale(1.3).move_to([-6.3, 2.0, 0])
            self.pop(Y)

            # «equis vale un valor concreto»
            self.en("valor")
            self.reb = n.rebanada(x0, 0.6)
            xx = MathTex("X=x", color=AMBAR).scale(0.8).next_to(self.reb, DOWN, buff=0.15)
            resto = [p for i, p in enumerate(n.pts) if i not in idx]
            self.play(FadeIn(self.reb), FadeIn(xx), *[p.animate.set_opacity(0.15) for p in resto], run_time=self.dur(0.7))

            # «el mundo se achica»
            self.en("achica")
            copias = VGroup(*[n.pts[i].copy() for i in idx])
            self.copias = copias
            self.play(FadeIn(self.panel), run_time=self.dur(0.3))
            self.play(copias.animate.move_to([4.4, 0.1, 0]).scale(2.0), run_time=self.dur(0.9))

            # «los casos donde equis vale eso»
            self.en("casos")
            t = Text("Solo estos casos", color=INK).scale(0.5).move_to([4.4, -2.6, 0])
            self.play(FadeIn(t), run_time=self.dur(0.4))

            # «Dentro de ese mundo pequeño»
            self.en("pequeno")
            self.resaltar(self.panel, color=AMBAR)

            # «el problema es el de siempre»
            self.en("siempre2")
            self.dado = dado(TXT).scale(0.7).move_to([-5.5, 3.3, 0])
            t35 = MathTex(r"3{,}5", color=AMBAR).scale(0.7).next_to(self.dado, RIGHT, buff=0.3)
            self.play(FadeIn(self.dado), FadeIn(t35), run_time=self.dur(0.4))

            # «apuesta la media»
            self.en("apuesta")
            c = copias.get_center()
            self.punto = Dot(c, radius=0.14, color=AMBAR)
            self.pop(self.punto)

            # «la varianza»
            self.en("varianza")
            ll = Brace(copias, RIGHT, color=ROJO, buff=0.15)
            self.play(GrowFromCenter(ll), run_time=self.dur(0.5))
            self.ll = ll
            self.t35 = t35

    def todas(self):
        n = self.nube
        with self.narrar("b2"):
            # «la media y la varianza»
            self.en("mv")
            tm = Text("Media", color=AMBAR, weight=BOLD).scale(0.5).next_to(self.punto, LEFT, buff=0.2)
            tv = Text("Varianza", color=ROJO, weight=BOLD).scale(0.5).next_to(self.ll, RIGHT, buff=0.1)
            tm.move_to([2.0, float(self.punto.get_center()[1]), 0])
            self.play(FadeIn(tm), FadeIn(tv), run_time=self.dur(0.5))

            # «la esperanza condicional»
            self.en("esperanza")
            e = MathTex(r"E[Y\mid X=x]", color=AMBAR).scale(0.8).move_to([4.4, 3.5, 0])
            self.pop(e)

            # «la varianza condicional»
            self.en("var_cond")
            v = MathTex(r"\mathrm{Var}(Y\mid X=x)", color=ROJO).scale(0.8).move_to([4.4, 2.8, 0])
            self.pop(v)

            # «la regla del dado»
            self.en("dado")
            self.resaltar(self.dado, color=AMBAR)

            # «rebanada a rebanada»
            self.en("rebanadas")
            self.play(FadeOut(tm), FadeOut(tv), FadeOut(self.ll), FadeOut(self.copias), FadeOut(self.punto),
                      FadeOut(self.reb), FadeOut(self.panel), FadeOut(self.t35), FadeOut(self.dado),
                      *[p.animate.set_opacity(1.0) for p in n.pts], run_time=self.dur(0.5))
            self.dots = VGroup()
            self.rebs = VGroup()
            for x in (-1.8, 0.0, 1.8):
                r = n.rebanada(x, 0.6)
                d = Dot(n.p(x, x), radius=0.12, color=AMBAR)
                self.rebs.add(r)
                self.dots.add(d)
            self.play(LaggedStart(*[AnimationGroup(FadeIn(r), FadeIn(d)) for r, d in zip(self.rebs, self.dots)],
                                  lag_ratio=0.4), run_time=self.dur(1.2))

            # «Ningún cálculo nuevo»
            self.en("nuevo")
            nc = Text("Cálculo nuevo", color=TXT).scale(0.6).move_to([4.4, -1.0, 0])
            self.play(FadeIn(nc), run_time=self.dur(0.3))
            self.play(Create(tachar(nc)), run_time=self.dur(0.4))

            # «la misma idea»
            self.en("idea")
            self.play(*[r.animate(rate_func=there_and_back).set_stroke(color=VERDE, width=6) for r in self.rebs],
                      run_time=self.dur(0.8))

            # «para cada valor»
            self.en("cada")
            lin = Line(n.p(-2.6, -2.6), n.p(2.6, 2.6), color=AMBAR, stroke_width=5)
            self.play(Create(lin), run_time=self.dur(0.8))
