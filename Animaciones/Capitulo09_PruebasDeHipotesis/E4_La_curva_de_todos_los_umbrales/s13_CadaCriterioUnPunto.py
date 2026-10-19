"""Escena 13 — Cada criterio, un punto de la misma curva: a priori iguales, Neyman-Pearson y un tercero pendiente."""
from comun.escena import *
from comun.figuras_c9e4 import *

PLANO_11 = dict(origen=(-1.6, -3.2), lado=4.6)
XD = 5.0
FA_IG, PD_IG = roc9(1.0)            # (0,16; 0,84)
U_NP = 1.645
FA_NP, PD_NP = roc9(U_NP)           # (0,05; 0,64)
U_R = 0.62                          # el umbral del riesgo (episodio siguiente)


class CadaCriterioUnPunto(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.P = PlanoRoc9(**PLANO_11)
        self.cur = self.P.curva()
        self.dg = self.P.diagonal()
        self.add(self.P, self.dg, self.cur)
        self.dos_puntos()
        self.tercero()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def dos_puntos(self):
        P = self.P
        with self.narrar("b1"):
            # «igual de frecuentes»
            self.en("iguales")
            ig = MathTex(r"p_0 = p_1 = 0{,}5", color=TXT).scale(0.8).move_to([XD, 1.9, 0])
            self.play(FadeIn(ig, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «pendiente uno»
            self.en("pend1")
            c = ValueTracker(-0.4)
            r = always_redraw(lambda: P.recta(1.0, (0, c.get_value()), color=TXT, ancho=4))
            self.play(FadeIn(r), run_time=self.dur(0.3))
            self.play(c.animate.set_value(PD_IG - FA_IG), run_time=self.dur(2.2))
            r.clear_updaters()

            # «El punto de tangencia»
            self.en("tang")
            d_ig = P.punto(FA_IG, PD_IG, color=TXT, radio=0.11)
            self.sfx("tick")
            self.play(FadeIn(d_ig, scale=0.3), run_time=self.dur(0.3))

            # «el más alejado de la diagonal»
            self.en("lejos")
            m = (FA_IG + PD_IG) / 2
            seg = Line(P.p(m, m), P.p(FA_IG, PD_IG), color=ROC, stroke_width=5)
            self.play(Create(seg), run_time=self.dur(0.5))

            # «Neyman-Pearson»
            self.en("np")
            np_t = Text("Neyman-Pearson", color=TXT, weight=BOLD).scale(0.5).move_to([XD, 0.6, 0])
            self.play(FadeOut(r), FadeOut(seg), run_time=0.25)
            self.pop(np_t)

            # «una recta vertical»
            self.en("vertical")
            v = Line(P.p(FA_NP, 0), P.p(FA_NP, 1), color=TXT, stroke_width=3.5)
            cinco = Text("5 %", color=TXT, weight=BOLD).scale(0.42).move_to(P.p(FA_NP, 0) + RIGHT * 0.45 + UP * 0.25)
            self.play(Create(v), FadeIn(cinco), run_time=self.dur(0.6))

            # «donde corta a la curva»
            self.en("corta")
            d_np = P.punto(FA_NP, PD_NP, color=TXT, radio=0.11)
            self.sfx("tick")
            self.play(FadeIn(d_np, scale=0.3), run_time=self.dur(0.3))

            # «ese es el punto»
            self.en("ese")
            par = rotulo_par9("0,05", "0,64", escala=0.45).move_to(P.p(0.27, 0.6))
            self.play(FadeIn(par), run_time=self.dur(0.4))

            # «tres coma seis»
            self.en("pend36")
            tg = P.tangente(U_NP, largo=0.42, color=ROC, ancho=4)
            t36 = Text("Pendiente 3,6", color=ROC).scale(0.42).next_to(par, DOWN, buff=0.15)
            self.play(Create(tg), FadeIn(t36), run_time=self.dur(0.5))
            self.d_ig, self.d_np = d_ig, d_np
            self.quitar = VGroup(v, cinco, par, t36, tg, ig, np_t)

    # ------------------------------------------------------------ b2
    def tercero(self):
        P = self.P
        with self.narrar("b2"):
            # «Dos criterios»
            self.en("dos")
            e1 = Text("Máximo a posteriori", color=TXT).scale(0.42).move_to(P.p(0.48, 0.79))
            e2 = Text("Neyman-Pearson", color=TXT).scale(0.42).move_to(P.p(0.36, 0.6))
            self.play(FadeOut(self.quitar), FadeIn(e1), FadeIn(e2), run_time=self.dur(0.5))

            # «un detector»
            self.en("uno")
            self.play(self.cur.animate.set_stroke(width=8), run_time=self.dur(0.35))
            self.play(self.cur.animate.set_stroke(width=5), run_time=self.dur(0.35))

            # «falta un tercero»
            self.en("tercero")
            vac = Circle(radius=0.2, color=TXT, stroke_width=4).set_fill(FONDO, 1).move_to(P.p(*roc9(U_R)))
            q = Text("?", color=ROC, weight=BOLD).scale(0.45).move_to(vac)
            self.play(FadeIn(vac, scale=0.3), run_time=self.dur(0.3))
            self.pop(q)

            # «el absurdo del test médico»
            self.en("test")
            tj = tarjeta9("Siempre sano → 1 %", ERROR, ancho=3.4).move_to([XD, 0.3, 0])
            fl = Arrow(tj.get_corner(UL) + LEFT * 0.05, vac.get_right(), color=INK, buff=0.08, stroke_width=3,
                       max_tip_length_to_length_ratio=0.08)
            self.play(FadeIn(tj, shift=LEFT * 0.2), run_time=self.dur(0.4))
            self.play(Create(fl), run_time=self.dur(0.4))
