"""Escena 04 — La curva ROC: los extremos, el barrido continuo del umbral y que no dependa de los a priori."""
from comun.escena import *
from comun.figuras_c9e4 import *


class LaCurvaRoc(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        C, P = campanas_izq9(), PlanoRoc9()
        self.C, self.P = C, P
        eje = eje_izq9(C)
        self.c0, self.c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        # los cuatro puntos de la escena anterior
        self.pts = VGroup()
        for u, txt in ((3.0, "3"), (2.0, "2"), (1.0, "1"), (0.0, "0")):
            d = P.punto(*roc9(u))
            r = Text(txt, color=ROC, weight=BOLD).scale(0.42)
            r.next_to(d, DOWN if u <= 0.5 else RIGHT, buff=0.12)
            self.pts.add(VGroup(d, r))
        self.B = Barrido9(C, P, u=0.0)
        self.add(eje, self.c0, self.c1, P, self.pts, *self.B.todo()[:2])
        self.extremos()
        self.curva()
        self.sin_apriori()
        self.wait(1.0)
        self.B.quieto()
        self.limpiar()

    def lectura(self, fa: str, pd: str) -> VGroup:
        a = MathTex(r"P_{FA} = " + fa, color=FA).scale(0.75)
        b = MathTex(r"P_D = " + pd, color=DET).scale(0.75)
        a.move_to([-5.15, 2.45, 0], aligned_edge=LEFT)
        b.move_to([-5.15, 1.75, 0], aligned_edge=LEFT)
        return VGroup(a, b)

    # ------------------------------------------------------------ b1
    def extremos(self):
        P, B = self.P, self.B
        with self.narrar("b1"):
            # «Los extremos son fáciles»
            self.en("extremos")
            aros = VGroup(Circle(radius=0.28, color=TXT, stroke_width=4).move_to(P.p(0, 0)),
                          Circle(radius=0.28, color=TXT, stroke_width=4).move_to(P.p(1, 1)))
            aros.permitir_encima = True
            self.play(Create(aros), run_time=self.dur(0.4))
            self.play(FadeOut(aros), run_time=self.dur(0.3))

            # «un umbral altísimo»
            self.en("alto")
            self.play(B.u.animate.set_value(6.0), run_time=self.dur(0.8))

            # «ni falsas alarmas ni detección»
            self.en("cero")
            lect = self.lectura("0", "0")
            self.play(FadeIn(lect, shift=DOWN * 0.15), run_time=self.dur(0.4))
            self.lect = lect

            # «abajo a la izquierda»
            self.en("esq0")
            d0 = P.punto(0, 0, radio=0.11)
            t0 = Text("Nunca decir 1", color=TXT).scale(0.42).move_to(P.p(0.33, 0.07))
            self.play(FadeIn(d0, scale=0.4), FadeIn(t0), run_time=self.dur(0.4))

            # «un umbral bajísimo»
            self.en("bajo")
            self.play(B.u.animate.set_value(-4.0), run_time=self.dur(0.8))

            # «todo son detecciones»
            self.en("todo")
            b = MathTex(r"P_D = 1", color=DET).scale(0.75).move_to(lect[1], aligned_edge=LEFT)
            self.play(ReplacementTransform(lect[1], b), run_time=self.dur(0.35))

            # «todo son falsas alarmas»
            self.en("todofa")
            a = MathTex(r"P_{FA} = 1", color=FA).scale(0.75).move_to(lect[0], aligned_edge=LEFT)
            self.play(ReplacementTransform(lect[0], a), run_time=self.dur(0.35))
            self.lect = VGroup(a, b)

            # «arriba a la derecha»
            self.en("esq1")
            d1 = P.punto(1, 1, radio=0.11)
            t1 = Text("Siempre decir 1", color=TXT).scale(0.42).move_to(P.p(0.74, 0.86))
            self.play(FadeIn(d1, scale=0.4), FadeIn(t1), run_time=self.dur(0.4))
            self.esquinas = VGroup(d0, t0, d1, t1)

    # ------------------------------------------------------------ b2
    def curva(self):
        C, P, B = self.C, self.P, self.B
        with self.narrar("b2"):
            # «Al deslizar el umbral»
            self.en("barrido")
            B.u.set_value(6.0)
            B.u_inicio = 6.0
            rastro = B.rastro()
            self.add(rastro, B.pt)
            self.play(FadeOut(self.lect), FadeOut(self.esquinas[1]), FadeOut(self.esquinas[3]),
                      run_time=0.25)
            self.play(B.u.animate.set_value(-4.0), run_time=self.dur(3.4), rate_func=linear)

            # «dibuja una curva»
            self.en("traza")
            curva = P.curva()
            rastro.clear_updaters()
            self.remove(rastro)
            self.add(curva)
            self.play(curva.animate.set_stroke(width=8), run_time=self.dur(0.4))
            self.play(curva.animate.set_stroke(width=5), FadeOut(self.pts), run_time=self.dur(0.3))
            self.curva_roc = curva

            # «curva ROC»
            self.en("roc")
            roc = Text("Curva ROC", color=ROC, weight=BOLD).scale(0.62).move_to(P.p(0.6, 0.42))
            self.pop(roc)

            # «característica operativa del receptor»
            self.en("nombre")
            nom = Text("Receiver Operating Characteristic", color=INK).scale(0.32).next_to(roc, DOWN, buff=0.15)
            self.play(FadeIn(nom, shift=UP * 0.1), run_time=self.dur(0.4))
            self.rotulos = VGroup(roc, nom)

            # «operadores de radar»
            self.en("radar")
            rad = radar13().scale(0.6).move_to([6.35, -3.15, 0])
            self.play(FadeIn(rad), run_time=self.dur(0.35))
            self.play(LaggedStart(*[o.animate(rate_func=there_and_back).set_stroke(ROC, opacity=1)
                                    for o in rad.ondas], lag_ratio=0.3), run_time=self.dur(0.9))

            # «Resume todo»
            self.en("resume")
            self.play(FadeOut(rad), curva.animate.set_stroke(width=8), run_time=self.dur(0.4))
            self.play(curva.animate.set_stroke(width=5), run_time=self.dur(0.3))

            # «Elegir un umbral»
            self.en("umbral")
            self.play(B.u.animate.set_value(CRUCE9), run_time=self.dur(1.0))

            # «elegir un punto»
            self.en("elegir")
            aro = Circle(radius=0.2, color=TXT, stroke_width=4).move_to(P.p(*roc9(CRUCE9)))
            self.play(Create(aro), run_time=self.dur(0.4))
            self.aro = aro

    # ------------------------------------------------------------ b3
    def sin_apriori(self):
        C, P = self.C, self.P
        with self.narrar("b3"):
            # «lo que no aparece»
            self.en("falta")
            a0 = MathTex(r"p_0 = 0{,}7", color=C0).scale(0.75).move_to([-5.15, 2.45, 0], aligned_edge=LEFT)
            a1 = MathTex(r"p_1 = 0{,}3", color=C1).scale(0.75).move_to([-2.85, 2.45, 0], aligned_edge=LEFT)
            self.play(FadeIn(a0, shift=DOWN * 0.15), FadeIn(a1, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «las probabilidades a priori»
            self.en("apriori")
            marco = SurroundingRectangle(VGroup(a0, a1), color=ROC, buff=0.15, stroke_width=4)
            self.play(Create(marco), run_time=self.dur(0.4))

            # «La curva es del detector»
            self.en("del")
            self.play(self.c0.animate.set_stroke(width=7), self.c1.animate.set_stroke(width=7),
                      self.curva_roc.animate.set_stroke(width=8), FadeOut(marco), run_time=self.dur(0.4))
            self.play(self.c0.animate.set_stroke(width=4), self.c1.animate.set_stroke(width=4),
                      self.curva_roc.animate.set_stroke(width=5), run_time=self.dur(0.3))

            # «lo frecuente»
            self.en("tachar")
            tc = VGroup(tachar(a0), tachar(a1))
            self.play(Create(tc), run_time=self.dur(0.4))

            # «lo que busca»
            self.en("busca")
            no = Text("No intervienen", color=ERROR, weight=BOLD).scale(0.5).move_to([-3.75, 1.75, 0])
            self.pop(no)

            # «para elegir el punto»
            self.en("punto")
            fl = CurvedArrow(a1.get_bottom() + DOWN * 0.1, self.aro.get_left() + LEFT * 0.05, color=INK,
                             angle=PI / 4, stroke_width=3.5)
            self.play(Create(fl), run_time=self.dur(0.5))

            # «no cambian la curva»
            self.en("igual")
            for v in ("0{,}5", "0{,}9"):
                n0 = MathTex(r"p_0 = " + v, color=C0).scale(0.75).move_to(a0, aligned_edge=LEFT)
                self.play(ReplacementTransform(a0, n0), run_time=self.dur(0.35))
                a0 = n0
            self.play(self.curva_roc.animate.set_stroke(width=8), run_time=self.dur(0.3))
            self.play(self.curva_roc.animate.set_stroke(width=5), run_time=self.dur(0.3))
