"""Escena 13 — El paso del LMS marca el compromiso entre velocidad y precisión."""
from comun.escena import *


class ElCompromisoDelPaso(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        P = ParabolaJ(centro=(-0.6, -0.6), ancho=7.0, alto=3.4)
        bal = balancin().scale(0.7).move_to([-5.2, 3.0, 0])
        lv = etiqueta("velocidad", AMBAR, 0.45).move_to([-6.1, 2.2, 0])
        lp = etiqueta("precisión", VERDE, 0.45).move_to([-4.3, 2.2, 0])
        alt = altavoz().scale(0.9).move_to([5.7, 2.6, 0])
        aur = auriculares().scale(1.1).move_to([5.7, 0.7, 0])
        bru = brujula().move_to([5.7, -1.2, 0])
        lw = etiqueta("Wiener", AZUL, 0.45, BOLD).move_to([5.7, -2.1, 0])
        mapa = etiqueta("mapa", INK, 0.5).move_to([5.7, -3.0, 0])
        tm = tachar(mapa)
        g = P.punto(-0.1, AMBAR)
        zig = [1.5, 0.2, 1.3, 0.4, 1.2, 0.5, 1.1, 0.5, 1.1]
        c = P.punto(-0.1, CIAN)
        with self.narrar("b1"):
            # «El paso marca el compromiso»
            self.en("compromiso")
            self.play(Create(P.eje), Create(P.curva), FadeIn(P.vertice), FadeIn(bal), FadeIn(lv), FadeIn(lp),
                      run_time=self.dur(0.9))
            # «grande, converge deprisa»
            self.en("grande")
            self.play(FadeIn(g), run_time=0.2)
            self.play(g.animate.move_to(P.p(1.5)), run_time=self.dur(0.35))
            self.play(g.animate.move_to(P.p(0.2)), run_time=self.dur(0.35))
            # «tiembla lejos del óptimo»
            self.en("tiembla")
            for h in zig[2:]:
                self.play(g.animate.move_to(P.p(h)), run_time=0.22, rate_func=linear)
            # «chico, converge despacio»
            self.en("chico")
            self.play(FadeIn(c), run_time=0.2)
            self.play(c.animate.move_to(P.p(0.4)), run_time=self.dur(1.0), rate_func=linear)
            # «pero fino»
            self.en("fino")
            self.play(c.animate.move_to(P.p(0.8)), run_time=self.dur(1.0))
            # «los ecos de una llamada»
            self.en("eco")
            self.play(FadeIn(alt), run_time=self.dur(0.6))
            # «el ruido en unos auriculares»
            self.en("auri")
            self.play(FadeIn(aur), run_time=self.dur(0.6))
            # «El filtro de Wiener es el norte»
            self.en("norte")
            self.play(FadeIn(bru), FadeIn(lw), run_time=self.dur(0.7))
            # «el LMS es cómo llegar»
            self.en("llegar")
            self.play(FadeOut(g), c.animate.move_to(P.p(0.0)), run_time=self.dur(0.6))
            self.play(c.animate.move_to(P.p(0.8)), run_time=self.dur(1.2))
            # «sin mapa»
            self.en("mapa")
            self.play(FadeIn(mapa), run_time=0.3)
            self.play(Create(tm), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
