"""Escena 10 — La pendiente no para de bajar: por eso la curva tiene la panza hacia arriba."""
from comun.escena import *
from comun.figuras_c9e4 import *


class LaPanzaHaciaArriba(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        P = PlanoRoc9(origen=(-5.0, -2.7), lado=5.2)
        cur = P.curva()
        X = 3.6                     # columna de la derecha
        with self.narrar("b1"):
            # «De ahí sale la forma»
            self.en("forma")
            ut = ValueTracker(2.6)
            tg = always_redraw(lambda: P.tangente(ut.get_value(), largo=0.5, color=TXT, ancho=4))
            pt = always_redraw(lambda: P.punto(*roc9(ut.get_value()), color=TXT))
            self.add(P, cur)
            self.play(FadeIn(tg), FadeIn(pt), run_time=self.dur(0.4))

            # «Al bajar el umbral»
            self.en("barre")
            self.play(ut.animate.set_value(1.2), run_time=self.dur(1.8))

            # «y la pendiente con él»
            self.en("tumba")
            rot = Text("Pendiente", color=INK).scale(0.45).move_to([X - 0.7, 2.7, 0])
            val = always_redraw(lambda: Text(num(lam9(ut.get_value()), 2), color=TXT, weight=BOLD)
                                .scale(0.6).next_to(rot, RIGHT, buff=0.3))
            self.play(FadeIn(rot), FadeIn(val), run_time=0.3)
            self.play(ut.animate.set_value(-1.0), run_time=self.dur(1.8))

            # «Una curva cuya pendiente»
            self.en("cuya")
            arco = CurvedArrow(P.p(0.1, 0.5), P.p(0.55, 0.88), color=TXT, angle=PI / 3, stroke_width=4)
            self.play(Create(arco), run_time=self.dur(0.6))

            # «la panza hacia arriba»
            self.en("panza")
            t1 = Text("Pendiente que baja", color=TXT, weight=BOLD).scale(0.48)
            t2 = Text("= Panza hacia arriba", color=ROC, weight=BOLD).scale(0.48)
            frase = VGroup(t1, t2).arrange(DOWN, buff=0.15).move_to([X, 1.65, 0])
            self.pop(frase)

            # «Es el presupuesto otra vez»
            self.en("mochila")
            moch = mochila9(centro=(X, -0.7), lado=0.85, escala=0.46)
            self.play(FadeIn(moch, shift=UP * 0.2), run_time=self.dur(0.45))

            # «las primeras falsas alarmas»
            self.en("primeras")
            m5 = moch.cas[4].copy().set_stroke(DET, 5)
            ini = P.curva(2, DET, 9, u0=6.0, u1=1.4, n=60)
            self.play(Create(m5), Create(ini), ut.animate.set_value(2.0), run_time=self.dur(0.6))

            # «compran mucha detección»
            self.en("compran")
            fuerte = P.tangente(2.0, largo=0.6, color=DET, ancho=8)
            self.play(Create(fuerte), run_time=self.dur(0.3))
            self.play(FadeOut(fuerte), run_time=self.dur(0.3))

            # «casi nada»
            self.en("ultimas")
            m1 = moch.cas[0].copy().set_stroke(FA, 5)
            fin = P.curva(2, FA, 9, u0=0.0, u1=-4.0, n=60)
            self.play(Create(m1), FadeOut(ini), Create(fin), ut.animate.set_value(-0.6), run_time=self.dur(0.7))

            # «sirve para algo más»
            self.en("mas")
            tg.clear_updaters()
            pt.clear_updaters()
            val.clear_updaters()
            self.play(FadeOut(VGroup(moch, m5, m1)), FadeOut(fin), FadeOut(tg), FadeOut(pt), FadeOut(arco),
                      run_time=self.dur(0.4))

            # «cada criterio»
            self.en("criterio")
            vacios = VGroup()
            for u in (CRUCE9, 1.0, 1.645):
                c = Circle(radius=0.12, color=TXT, stroke_width=4).set_fill(FONDO, 1).move_to(P.p(*roc9(u)))
                vacios.add(c)
            q = Text("?", color=ROC, weight=BOLD).scale(0.6).move_to(P.p(0.32, 0.72))
            self.play(LaggedStart(*[FadeIn(c, scale=0.4) for c in vacios], lag_ratio=0.3), run_time=self.dur(0.6))
            self.pop(q)
        self.wait(1.0)
        self.limpiar()
