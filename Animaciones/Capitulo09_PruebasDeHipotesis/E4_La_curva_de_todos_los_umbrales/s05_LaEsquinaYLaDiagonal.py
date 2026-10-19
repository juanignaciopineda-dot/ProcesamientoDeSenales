"""Escena 05 — La esquina ideal y la diagonal del azar."""
from comun.escena import *
from comun.figuras_c9e4 import *


class LaEsquinaYLaDiagonal(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.P = PlanoRoc9(**PLANO_C)
        self.curva = self.P.curva()
        self.esquina()
        self.diagonal()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def esquina(self):
        P = self.P
        with self.narrar("b1"):
            # «¿Cómo se lee esta curva?»
            self.en("leer")
            self.play(FadeIn(P), Create(self.curva), run_time=self.dur(0.9))

            # «arriba a la izquierda»
            self.en("esquina")
            brillo = Circle(radius=0.22, color=DET, stroke_width=5).move_to(P.p(0, 1))
            brillo.permitir_encima = True
            self.play(Create(brillo), run_time=self.dur(0.4))

            # «la detección vale uno»
            self.en("uno")
            t1 = Text("Detección 1", color=DET).scale(0.45).move_to(P.p(0, 1) + LEFT * 1.75)
            self.play(FadeIn(t1, shift=RIGHT * 0.15), run_time=self.dur(0.35))

            # «la falsa alarma, cero»
            self.en("cero")
            t0 = Text("Falsa alarma 0", color=FA).scale(0.45).move_to(P.p(0, 1) + LEFT * 1.85 + DOWN * 0.5)
            self.play(FadeIn(t0, shift=RIGHT * 0.15), run_time=self.dur(0.35))

            # «el detector perfecto»
            self.en("ideal")
            est = estrella9(radio=0.2).move_to(P.p(0, 1))
            est.permitir_encima = True
            ideal = Text("Ideal", color=DET, weight=BOLD).scale(0.5).move_to(P.p(0.26, 0.965))
            self.play(FadeOut(brillo), run_time=0.15)
            self.pop(est, ideal)

            # «Cuanto más se acerque»
            self.en("acerca")
            mejor = P.curva(3.2)
            self.play(Transform(self.curva, mejor), run_time=self.dur(0.7))
            self.play(Transform(self.curva, P.curva()), run_time=self.dur(0.6))

            # «esa esquina, mejor»
            self.en("mejor")
            tl = tilde(tam=0.45).move_to(P.p(0.44, 0.965))
            self.play(Create(tl), run_time=self.dur(0.35))
            self.extra = VGroup(t1, t0, tl)

    # ------------------------------------------------------------ b2
    def diagonal(self):
        P = self.P
        with self.narrar("b2"):
            # «Segundo, la diagonal»
            self.en("diagonal")
            dg = P.diagonal()
            self.play(FadeOut(self.extra), Create(dg), self.curva.animate.set_stroke(opacity=0.35),
                      run_time=self.dur(0.6))

            # «Imagina un detector»
            self.en("imagina")
            det = caja("Detector", INK, ancho=2.4, alto=0.8, scale=0.5).move_to([4.7, 1.9, 0])
            self.play(FadeIn(det, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «no mira nada»
            self.en("ciego")
            o = ojo().scale(0.6).move_to([4.7, 0.75, 0])
            tc = tachar(o)
            self.play(FadeIn(o), run_time=self.dur(0.25))
            self.play(Create(tc), run_time=self.dur(0.3))

            # «una moneda cargada»
            self.en("moneda")
            mon = moneda("1").scale(0.95).move_to([4.7, -0.65, 0])
            qt = MathTex("q", color=ROC).scale(0.8).next_to(mon, DOWN, buff=0.15)
            self.play(FadeIn(mon, scale=0.6), FadeIn(qt), run_time=self.dur(0.4))

            # «con cierta probabilidad»
            self.en("prob")
            self.sfx("tick")
            self.play(mon.animate(rate_func=there_and_back).stretch(0.08, 0), run_time=self.dur(0.4))
            self.play(mon.animate(rate_func=there_and_back).stretch(0.08, 0), run_time=self.dur(0.4))

            # «Dirá uno esa fracción»
            self.en("q")
            q = ValueTracker(0.3)
            qv = MathTex(r"q = 0{,}3", color=ROC).scale(0.8).move_to(qt)
            pt = always_redraw(lambda: P.punto(q.get_value(), q.get_value(), radio=0.11))
            self.play(ReplacementTransform(qt, qv), FadeIn(pt, scale=0.4), run_time=self.dur(0.45))

            # «haya avión o no»
            self.en("avion")
            ca = casilla9("Con avión · 0,3", DET, ancho=3.0, alto=0.7, escala=0.42).move_to([-5.2, 1.0, 0])
            sa = casilla9("Sin avión · 0,3", FA, ancho=3.0, alto=0.7, escala=0.42).move_to([-5.2, 0.0, 0])
            self.play(FadeIn(ca, shift=RIGHT * 0.2), FadeIn(sa, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «son iguales»
            self.en("iguales")
            ig = Text("Falsa alarma = Detección = q", color=TXT).scale(0.4).move_to([-4.85, -1.0, 0])
            self.play(FadeIn(ig), run_time=self.dur(0.35))
            self.play(q.animate.set_value(0.8), run_time=self.dur(1.0))
            self.play(q.animate.set_value(0.3), run_time=self.dur(0.8))

            # «decidir al azar»
            self.en("azar")
            az = Text("Decidir al azar", color=INK, weight=BOLD).scale(0.5)
            az.rotate(PI / 4).move_to(P.p(0.66, 0.5))
            self.pop(az)
        pt.clear_updaters()
