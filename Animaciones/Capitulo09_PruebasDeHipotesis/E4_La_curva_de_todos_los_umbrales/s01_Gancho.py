"""Escena 01 — Gancho: cada umbral es un detector; juntos dibujan una curva cuya pendiente es el umbral."""
from comun.escena import *
from comun.figuras_c9e4 import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        C = campanas_izq9()
        P = PlanoRoc9()
        eje = eje_izq9(C)
        c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        self.add(eje, c0, c1, P)

        with self.narrar("b1"):
            # «Cada umbral»
            self.en("umbral")
            B = Barrido9(C, P, u=3.0)
            self.play(FadeIn(B.colas), Create(B.linea), run_time=0.4)

            # «un detector distinto»
            self.en("detector")
            puntos = VGroup()
            for u_sig in (2.0, 1.0, None):
                d = P.punto(*roc9(B.u.get_value()))
                puntos.add(d)
                self.sfx("tick")
                self.play(FadeIn(d, scale=0.4), run_time=0.25)
                if u_sig is not None:
                    self.play(B.u.animate.set_value(u_sig), run_time=0.45)

            # «todos a la vez»
            self.en("todos")
            curva = P.curva()
            self.play(B.u.animate.set_value(-3.0), Create(curva), run_time=self.dur(1.6))
            self.play(FadeOut(puntos), run_time=self.dur(0.3))

            # «guarda un secreto»
            self.en("secreto")
            q = Text("?", color=ROC, weight=BOLD).scale(1.0).move_to(P.p(0.6, 0.45))
            self.play(curva.animate.set_stroke(width=8), run_time=self.dur(0.4))
            self.pop(q)

            # «su pendiente»
            self.en("pendiente")
            ut = ValueTracker(2.4)
            tg = always_redraw(lambda: P.tangente(ut.get_value(), largo=0.55, color=TXT, ancho=4))
            pt = always_redraw(lambda: P.punto(*roc9(ut.get_value()), color=TXT))
            self.play(FadeOut(q), FadeIn(tg), FadeIn(pt), run_time=self.dur(0.3))
            self.play(ut.animate.set_value(0.0), run_time=self.dur(1.6))

            # «es el umbral»
            self.en("es")
            msg = Text("Pendiente = Umbral", color=ROC, weight=BOLD).scale(0.6).move_to([0, 3.35, 0])
            self.pop(msg)
            self.play(ut.animate.set_value(1.0), B.u.animate.set_value(1.0), run_time=self.dur(1.0))
        self.wait(0.6)
        tg.clear_updaters()
        pt.clear_updaters()
        B.quieto()
        self.limpiar()
