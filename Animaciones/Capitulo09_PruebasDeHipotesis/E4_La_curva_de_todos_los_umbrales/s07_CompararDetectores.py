"""Escena 07 — Comparar dos detectores con sus curvas, y la pregunta por la forma."""
from comun.escena import *
from comun.figuras_c9e4 import *

DA = 2.2                  # separación del detector A
DB = 1.3                  # separación del detector B (siempre peor)
MB, SB = 3.5, 2.5         # el B que se cruza con A: campana del uno en 3,5 con desvío 2,5


def fa_cruce() -> float:
    xs = np.linspace(0.005, 0.995, 2000)
    dif = np.array([pd_de_fa9(x, DA) - pd_de_fa9(x, MB, SB) for x in xs])
    i = int(np.argmax(np.sign(dif) != np.sign(dif[0])))
    return float(xs[i])


class CompararDetectores(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.P = PlanoRoc9(**PLANO_C)
        self.comparar()
        self.forma()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def comparar(self):
        P = self.P
        fA = lambda x: pd_de_fa9(x, DA)
        fB = lambda x: pd_de_fa9(x, DB)
        with self.narrar("b1"):
            # «sirve también para comparar»
            self.en("comparar")
            a, b = P.curva(DA, ROC, 5), P.curva(DB, CIAN, 5)
            ta = Text("A", color=ROC, weight=BOLD).scale(0.6).move_to(P.p(0.05, 0.93))
            tb = Text("B", color=CIAN, weight=BOLD).scale(0.6).move_to(P.p(0.4, 0.66))
            self.play(FadeIn(P), FadeIn(P.diagonal()), run_time=self.dur(0.4))
            self.play(Create(a), Create(b), FadeIn(ta), FadeIn(tb), run_time=self.dur(0.9))

            # «por encima de la de otro»
            self.en("encima")
            zona = P.entre(fA, fB, 0.002, 0.998, VERDE, 0.28)
            zona.permitir_encima = True
            self.play(FadeIn(zona), run_time=self.dur(0.5))

            # «con cualquier criterio»
            self.en("mejor")
            mejor = Text("A mejor siempre", color=ROC, weight=BOLD).scale(0.5).move_to([4.9, 1.2, 0])
            self.pop(mejor)

            # «Si se cruzan»
            self.en("cruzan")
            b2 = P.curva_bin(MB, SB, CIAN, 5)
            self.play(FadeOut(zona), Transform(b, b2), tb.animate.move_to(P.p(0.5, 0.8)),
                      mejor.animate.set_opacity(0.3), run_time=self.dur(0.7))

            # «depende de la zona»
            self.en("zona")
            fB2 = lambda x: pd_de_fa9(x, MB, SB)
            xc = fa_cruce()
            zb = P.entre(fB2, fA, 0.002, xc, CIAN, 0.3)       # a la izquierda gana B
            za = P.entre(fA, fB2, xc, 0.998, ROC, 0.3)        # a la derecha gana A
            za.permitir_encima = zb.permitir_encima = True
            dep = Text("Depende de la zona", color=TXT, weight=BOLD).scale(0.5).move_to([4.9, 0.2, 0])
            self.play(FadeIn(za), FadeIn(zb), FadeOut(mejor), run_time=self.dur(0.5))
            self.pop(dep)

    # ------------------------------------------------------------ b2
    def forma(self):
        P = self.P
        with self.narrar("b2"):
            # «un detalle de la forma»
            self.en("forma")
            self.corte()
            cur = P.curva()
            self.add(P, cur)
            self.play(cur.animate.set_stroke(width=7), run_time=self.dur(0.3))
            self.play(cur.animate.set_stroke(width=5), run_time=self.dur(0.3))

            # «la panza hacia arriba»
            self.en("panza")
            arco = CurvedArrow(P.p(0.1, 0.5), P.p(0.55, 0.88), color=TXT, angle=PI / 3, stroke_width=4)
            self.play(Create(arco), run_time=self.dur(0.6))

            # «Muy empinadas al principio»
            self.en("empinada")
            ini = P.curva(2, DET, 9, u0=6.0, u1=1.4, n=60)
            self.play(Create(ini), run_time=self.dur(0.5))

            # «casi planas al final»
            self.en("plana")
            fin = P.curva(2, DET, 9, u0=0.3, u1=-4.0, n=60)
            self.play(Create(fin), run_time=self.dur(0.5))

            # «No es casualidad»
            self.en("casualidad")
            q = Text("?", color=ROC, weight=BOLD).scale(1.6).move_to(P.p(0.66, 0.42))
            self.play(FadeOut(ini), FadeOut(fin), run_time=self.dur(0.25))
            self.pop(q)

            # «el resultado más bonito»
            self.en("bonito")
            self.play(q.animate(rate_func=there_and_back).scale(1.3).set_color(TXT), run_time=self.dur(0.7))
