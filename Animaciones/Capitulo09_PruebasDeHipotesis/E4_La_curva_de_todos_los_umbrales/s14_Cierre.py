"""Escena 14 — Cierre: un detector es una curva; su pendiente es el umbral; anuncia el episodio 5."""
from comun.escena import *
from comun.figuras_c9e4 import *


class Cierre(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        self.resumen()
        self.anuncio()
        self.wait(1.2)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resumen(self):
        C, P = campanas_izq9(), PlanoRoc9()
        eje = eje_izq9(C)
        c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        cur = P.curva()
        B = Barrido9(C, P, u=3.0)
        with self.narrar("b1"):
            # «un detector es una curva entera»
            self.en("curva")
            self.play(FadeIn(VGroup(eje, c0, c1, P)), Create(cur), FadeIn(B.colas), FadeIn(B.linea),
                      run_time=self.dur(0.8))

            # «un punto por cada umbral»
            self.en("barre")
            self.add(B.pt)
            self.play(B.u.animate.set_value(-0.5), run_time=self.dur(1.2))
            self.play(B.u.animate.set_value(CRUCE9), run_time=self.dur(0.8))

            # «Su pendiente»
            self.en("pend")
            tg = P.tangente(CRUCE9, largo=0.55, color=TXT, ancho=4)
            et = MathTex(r"\text{Pendiente} = \eta", color=ROC).scale(0.75).move_to(P.p(0.6, 0.45))
            self.play(Create(tg), FadeIn(et), run_time=self.dur(0.5))

            # «es el umbral que se usa»
            self.en("ahi")
            self.play(et.animate(rate_func=there_and_back).scale(1.2), run_time=self.dur(0.5))

            # «cada criterio no es»
            self.en("criterios")
            B.quieto()
            pts = VGroup()
            for u, txt in ((1.0, "Máximo a posteriori"), (1.645, "Neyman-Pearson")):
                d = P.punto(*roc9(u), color=TXT, radio=0.09)
                pts.add(d)
            r1 = Text("Máximo a posteriori", color=TXT).scale(0.4).move_to(P.p(0.48, 0.78))
            r2 = Text("Neyman-Pearson", color=TXT).scale(0.4).move_to(P.p(0.37, 0.6))
            self.play(FadeOut(tg), FadeOut(et), FadeIn(pts, scale=0.4), FadeIn(r1), FadeIn(r2),
                      run_time=self.dur(0.5))

            # «otro punto de la misma curva»
            self.en("misma")
            vac = Circle(radius=0.2, color=TXT, stroke_width=4).set_fill(FONDO, 1).move_to(P.p(*roc9(0.62)))
            q = Text("?", color=ROC, weight=BOLD).scale(0.42).move_to(vac)
            self.play(FadeIn(vac, scale=0.3), run_time=self.dur(0.3))
            self.pop(q)

    # ------------------------------------------------------------ b2
    def anuncio(self):
        with self.narrar("b2"):
            # «los dos errores pesaban lo mismo»
            self.en("balanza")
            self.corte()
            b = Balanza(centro=(0.0, 1.0), semi=2.8)
            ti = Text("Falsa alarma", color=FA).scale(0.45).next_to(b.izq[1], DOWN, buff=1.05)
            td = Text("Fallo", color=FA).scale(0.45).next_to(b.der[1], DOWN, buff=1.05)
            b.izq.add(ti)
            b.der.add(td)
            self.play(FadeIn(b), run_time=self.dur(0.5))

            # «mandar a casa a un enfermo»
            self.en("enfermo")
            ca = casa(ancho=0.9, alto=0.65).next_to(b.der[1], UP, buff=0.05).shift(RIGHT * 0.25)
            en = persona(ERROR).scale(0.85).next_to(b.der[1], UP, buff=0.05).shift(LEFT * 0.35)
            b.der.add(ca, en)
            self.play(FadeIn(ca), FadeIn(en), run_time=self.dur(0.4))

            # «mucho más grave»
            self.en("inclina")
            self.sfx("impacto", gain=-18)
            self.play(*b.inclinar("der", ang=0.25), run_time=self.dur(0.6))

            # «repetirle la prueba a un sano»
            self.en("sano")
            sa = persona(SENAL).scale(0.85).next_to(b.izq[1], UP, buff=0.05).shift(LEFT * 0.3)
            tt = tira_test07(0.38).next_to(b.izq[1], UP, buff=0.05).shift(RIGHT * 0.3)
            self.play(FadeIn(sa), FadeIn(tt), run_time=self.dur(0.4))

            # «en el próximo episodio»
            self.en("proximo")
            tj = caja("Episodio 5 · ¿Cuánto cuesta equivocarse?", ROC, alto=0.9, scale=0.55).move_to([0, -2.6, 0])
            self.play(FadeIn(tj, shift=UP * 0.2), run_time=self.dur(0.5))

            # «¿cuánto cuesta equivocarse?»
            self.en("titulo5")
            self.resaltar(tj, color=ROC)
            self.play(b.viga.animate(rate_func=there_and_back).set_stroke(ROC, width=9), run_time=self.dur(0.5))
