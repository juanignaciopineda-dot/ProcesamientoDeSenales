"""Escena 06 — Cuanto más separadas las campanas, mejor curva; y por debajo de la diagonal, al revés."""
from comun.escena import *
from comun.figuras_c9e4 import *

COLORES = {1: CIAN, 2: ROC, 3: VERDE}


class FamiliaDeCurvas(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.P = PlanoRoc9(origen=(0.6, -2.6), lado=5.2)
        self.C = Campanas9(centro=(-4.0, -0.6), ancho=5.4, alto=3.6, r_rango=(-3.0, 6.0))
        self.separacion()
        self.al_reves()
        self.wait(1.0)
        self.limpiar()

    def llave(self, d: float) -> VGroup:
        C = self.C
        br = BraceBetweenPoints(C.p(0) + DOWN * 0.15, C.p(d) + DOWN * 0.15, DOWN, color=INK)
        t = Text(f"{d:g} desvío" + ("s" if d != 1 else ""), color=INK).scale(0.42).next_to(br, DOWN, buff=0.1)
        return VGroup(br, t)

    def marca(self, d: int) -> VGroup:
        P = self.P
        pd = Q(1.645 - d)
        dot = P.punto(0.05, pd, color=COLORES[d], radio=0.1)
        t = Text(num(pd, 2), color=COLORES[d], weight=BOLD).scale(0.45).move_to(P.p(0, pd) + LEFT * 0.45)
        return VGroup(dot, t)

    # ------------------------------------------------------------ b1
    def separacion(self):
        P, C = self.P, self.C
        dg = P.diagonal()
        with self.narrar("b1"):
            # «Todo lo útil»
            self.en("util")
            zona = Polygon(P.p(0, 0), P.p(0, 1), P.p(1, 1), stroke_width=0, stroke_opacity=0).set_fill(ROC, 0.1)
            self.play(FadeIn(P), Create(dg), run_time=self.dur(0.5))
            self.play(FadeIn(zona), run_time=self.dur(0.4))
            self.zona, self.dg = zona, dg

            # «cuánto se separan las campanas»
            self.en("campanas")
            dsep = ValueTracker(2.0)
            self.dsep = dsep
            base = Line(C.p(C.r0), C.p(C.r1), color=INK, stroke_width=2.2)
            c0 = C.campana(0, 1, C0, ancho=3.5)
            c1 = always_redraw(lambda: C.campana(dsep.get_value(), 1, C1, ancho=3.5))
            self.play(Create(base), Create(c0), Create(c1), run_time=self.dur(0.6))
            self.c1 = c1

            # «medido en desvíos»
            self.en("desvios")
            ll = self.llave(2)
            self.play(GrowFromCenter(ll[0]), FadeIn(ll[1]), run_time=self.dur(0.45))
            self.ll = ll

            # «un cinco por ciento»
            self.en("cinco")
            v = DashedLine(P.p(0.05, 0), P.p(0.05, 1), color=TXT, stroke_width=2.5, dash_length=0.1)
            vt = Text("5 %", color=TXT, weight=BOLD).scale(0.42).move_to(P.p(0.14, 0.05))
            self.play(Create(v), FadeIn(vt), run_time=self.dur(0.5))

            self.curvas = VGroup()
            self.marcas = VGroup()
            for d, marca in ((1, "d1"), (2, "d2"), (3, "d3")):
                # «Con un desvío» / «Con dos» / «Con tres»
                self.en(marca)
                ll = self.llave(d)
                cur = P.curva(d, COLORES[d], 4.5)
                self.play(dsep.animate.set_value(d), ReplacementTransform(self.ll, ll), run_time=self.dur(0.6))
                self.ll = ll
                self.play(Create(cur), run_time=self.dur(0.7))
                self.curvas.add(cur)
                m = self.marca(d)
                if d == 1:
                    self.play(FadeIn(m[0], scale=0.4), run_time=self.dur(0.3))
                    # «del veintiséis por»
                    self.en("v26")
                    self.pop(m[1])
                else:
                    self.play(FadeIn(m[0], scale=0.4), run_time=0.25)
                    self.pop(m[1])
                self.marcas.add(m)

    # ------------------------------------------------------------ b2
    def al_reves(self):
        P = self.P
        with self.narrar("b2"):
            # «¿Y una curva por debajo»
            self.en("debajo")
            us = np.linspace(6.0, -4.0, 140)
            mala = VMobject(stroke_color=ERROR, stroke_width=5)
            mala.set_points_as_corners([P.p(Q(u - 2), Q(u)) for u in us])
            self.play(self.curvas.animate.set_stroke(opacity=0.25), FadeOut(self.marcas), FadeOut(self.zona),
                      Create(mala), run_time=self.dur(0.8))

            # «de la diagonal?»
            self.en("diag")
            self.play(self.dg.animate.set_stroke(TXT, width=4.5), run_time=self.dur(0.3))
            self.play(self.dg.animate.set_stroke(INK, width=3), run_time=self.dur(0.3))

            # «peor que el azar»
            self.en("peor")
            peor = Text("Peor que el azar", color=ERROR, weight=BOLD).scale(0.48).move_to(P.p(0.62, 0.3))
            self.pop(peor)

            # «puesto al revés»
            self.en("reves")
            a = casilla9("0 → 1", INK, ancho=1.9, alto=0.7, escala=0.48).move_to([-5.2, 2.6, 0])
            b = casilla9("1 → 0", INK, ancho=1.9, alto=0.7, escala=0.48).move_to([-2.8, 2.6, 0])
            self.play(FadeIn(a), FadeIn(b), run_time=self.dur(0.4))

            # «invertir todas sus decisiones»
            self.en("invertir")
            self.play(Swap(a, b), run_time=self.dur(0.8))

            # «se refleja»
            self.en("refleja")
            buena = P.curva(2, ROC, 5)
            self.play(FadeOut(peor), ReplacementTransform(mala, buena), run_time=self.dur(1.0))
        self.c1.clear_updaters()
