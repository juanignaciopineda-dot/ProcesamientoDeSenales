"""Escena 08 — Bajar el umbral un poquito: la pendiente y la rebanada fina (altura por ancho)."""
from comun.escena import *
from comun.figuras_c9e4 import *

U1, U2 = 1.0, 0.88        # el segundo umbral se dibuja más lejos que 0,99 para que se vea la rebanada


class LaRebanada(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.pendiente()
        self.rebanada()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pendiente(self):
        P = PlanoRoc9(**PLANO_C)
        cur = P.curva()
        x0, y0 = roc9(1.0)
        with self.narrar("b1"):
            # «La pendiente de una curva»
            self.en("pendiente")
            dot = P.punto(x0, y0, color=TXT, radio=0.1)
            self.play(FadeIn(P), Create(cur), run_time=self.dur(0.8))
            self.play(FadeIn(dot, scale=0.4), run_time=self.dur(0.25))

            # «cuánto sube»
            self.en("sube")
            tri = triangulo9(P, (x0, y0), 0.16, 0.85, ancho=5)
            ts = Text("Lo que sube", color=DET).scale(0.42).next_to(tri.v, RIGHT, buff=0.15)
            self.play(Create(tri.v), FadeIn(ts), run_time=self.dur(0.45))

            # «hacia la derecha»
            self.en("paso")
            tp = Text("Paso a la derecha", color=FA).scale(0.42).next_to(tri.h, DOWN, buff=0.15)
            self.play(Create(tri.h), FadeIn(tp), run_time=self.dur(0.45))

            # «cuánta detección ganas»
            self.en("gana")
            ts2 = Text("+ Detección", color=DET, weight=BOLD).scale(0.45).move_to(ts, aligned_edge=LEFT)
            self.play(ReplacementTransform(ts, ts2), run_time=self.dur(0.4))

            # «falsa alarma que aceptas»
            self.en("acepta")
            tp2 = Text("+ Falsa alarma", color=FA, weight=BOLD).scale(0.45).move_to(tp)
            self.play(ReplacementTransform(tp, tp2), run_time=self.dur(0.4))

    # ------------------------------------------------------------ b2
    def rebanada(self):
        C = Campanas9()
        with self.narrar("b2"):
            # «Baja el umbral un poquito»
            self.en("baja")
            self.corte()
            eje = C.eje((0, 1, 2))
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            l1 = C.regla(U1, color=ROC, alto=3.6)
            t1 = Text("1", color=ROC, weight=BOLD).scale(0.45).next_to(l1, UP, buff=0.1).shift(RIGHT * 0.12)
            self.add(eje, c0, c1)
            self.play(Create(l1), FadeIn(t1), run_time=self.dur(0.4))

            # «cero coma noventa y nueve»
            self.en("u099")
            l2 = C.regla(U2, color=ROC, alto=3.6).set_stroke(opacity=0.8)
            t2 = Text("0,99", color=ROC, weight=BOLD).scale(0.45).next_to(l2, UP, buff=0.1).shift(LEFT * 0.3)
            self.play(TransformFromCopy(l1, l2), FadeIn(t2), run_time=self.dur(0.6))

            # «La región donde»
            self.en("region")
            reg = C.region(U2, C.r1, ROC, grosor=0.18, opacidad=0.6)
            self.play(FadeIn(reg), run_time=self.dur(0.45))

            # «una rebanada muy fina»
            self.en("rebanada")
            centro = C.p((U1 + U2) / 2, 0.13)
            self.play(FadeOut(t1), FadeOut(t2), run_time=0.2)
            self.zoom(centro, 5.0, run_time=self.dur(1.0))

            # «La falsa alarma aumenta»
            self.en("fa")
            fa = Text("+ Falsa alarma", color=FA, weight=BOLD).scale(0.24).move_to(C.p(0.94, 0.3) + LEFT * 1.25)
            self.play(FadeIn(fa), run_time=self.dur(0.35))

            # «bajo la campana del cero»
            self.en("r0")
            h0 = C.f(0, U1)
            x_a, x_b = C.p(U2), C.p(U1)
            r0 = Polygon(x_a, x_b, C.p(U1, h0), C.p(U2, h0), color=FA, stroke_width=2).set_fill(FA, 0.55)
            self.play(GrowFromEdge(r0, DOWN), run_time=self.dur(0.5))

            # «su altura por el ancho»
            self.en("area0")
            a0 = MathTex(r"f_0 \cdot \text{Ancho}", color=FA).scale(0.32).next_to(r0, LEFT, buff=0.15)
            a0.shift(DOWN * 0.4)
            self.play(FadeIn(a0), run_time=self.dur(0.35))

            # «Y la detección aumenta»
            self.en("pd")
            pd = Text("+ Detección", color=DET, weight=BOLD).scale(0.24).move_to(C.p(0.94, 0.3) + RIGHT * 1.15)
            self.play(FadeIn(pd), run_time=self.dur(0.35))

            # «bajo la campana del uno»
            self.en("r1")
            h1 = C.f(2, U1)
            r1 = Polygon(x_a, x_b, C.p(U1, h1), C.p(U2, h1), color=DET, stroke_width=4).set_fill(DET, 0.0)
            self.play(Create(r1), run_time=self.dur(0.5))

            # «por el mismo ancho»
            self.en("area1")
            a1 = MathTex(r"f_1 \cdot \text{Ancho}", color=DET).scale(0.32).next_to(r1, RIGHT, buff=0.15)
            a1.shift(DOWN * 0.4)
            ancho = BraceBetweenPoints(C.p(U2, h1), C.p(U1, h1), UP, color=TXT, buff=0.05)
            self.play(FadeIn(a1), GrowFromCenter(ancho), run_time=self.dur(0.45))
        self.wait(0.5)
        self.zoom_reset(run_time=0.6)
