"""Escena 20 — El umbral sube de 3,09 a 4,75 desvíos al buscar en mil sitios."""
from comun.escena import *


def _g(x):
    return gaussiana(x, 0.0, 1.0)


class ElUmbralSube(EscenaCurso):
    ESCENA = "20"

    def construct(self):
        L = Lienzo(ancho=11.0, alto=3.0, t_rango=(-4, 7), v_max=0.45, centro=(0.0, -0.4))
        base = L.base()
        camp = curva_f(L, _g, -4, 7, RUIDO, 4.0, n=200)
        una = Text("una posición", color=TXT, weight=BOLD).scale(0.6).move_to([-4.6, 3.3, 0])
        cola1 = area_f(L, _g, 3.09, 7, ROJO, 0.7, n=60)
        e3 = MathTex(r"10^{-3}", color=ROJO).scale(0.8).move_to(L.p(4.6, 0.12))
        inv = formula(r"Q^{-1}(10^{-3})", escala=0.95, colores={}).move_to([-4.0, 2.4, 0])
        m1 = DashedLine(L.p(3.09, 0), L.p(3.09, 0.36), color=AMBAR, stroke_width=4)
        v1 = MathTex(r"3{,}09\,\sigma", color=AMBAR).scale(0.8).move_to(L.p(3.09, 0.5))
        cola2 = area_f(L, _g, 4.75, 7, ROJO, 0.9, n=40)
        e6 = MathTex(r"10^{-6}", color=ROJO).scale(0.8).move_to(L.p(6.0, 0.1))
        m2 = DashedLine(L.p(4.75, 0), L.p(4.75, 0.36), color=AMBAR, stroke_width=4)
        v2 = MathTex(r"4{,}75\,\sigma", color=AMBAR).scale(0.8).move_to(L.p(4.75, 0.5))
        sube = Arrow(L.p(3.09, 0.30), L.p(4.75, 0.30), color=VERDE, buff=0, stroke_width=6)
        tira = celdas13(40, ancho=8.0, centro=(0.0, -3.4), alto=0.45)
        sit = Text("1.000 sitios", color=AMBAR, weight=BOLD).scale(0.55).next_to(tira, RIGHT, buff=0.2)
        with self.narrar("b1"):
            # «Traducido al umbral»
            self.en("traducido")
            self.play(FadeIn(base), Create(camp), run_time=self.dur(0.8))
            # «una sola posición»
            self.en("una")
            self.play(FadeIn(una), run_time=0.4)
            # «una falsa alarma de una entre mil»
            self.en("unaentremil")
            self.play(FadeIn(cola1), FadeIn(e3), run_time=self.dur(0.8))
            # «la inversa de cu»
            self.en("inversa")
            self.play(FadeIn(inv), run_time=self.dur(0.9))
            # «tres coma cero nueve desvíos»
            self.en("v309")
            self.play(Create(m1), FadeIn(v1), run_time=self.dur(0.8))
            # «Para una entre un millón»
            self.en("millon")
            self.play(cola1.animate.set_fill(ROJO, 0.25), FadeOut(e3), FadeIn(cola2), FadeIn(e6), run_time=self.dur(0.8))
            # «cuatro coma siete cinco»
            self.en("v475")
            self.play(Create(m2), FadeIn(v2), run_time=self.dur(0.8))
            # «subir casi dos desvíos completos»
            self.en("subir")
            self.play(GrowArrow(sube), run_time=self.dur(0.8))
            # «buscar en mil sitios»
            self.en("sitios")
            self.play(FadeIn(tira), FadeIn(sit), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
