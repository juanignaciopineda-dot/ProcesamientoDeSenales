"""Escena 03 — Ocho casos: de las densidades a casos resueltos con una puntuación, y ordenarlos."""
from comun.escena import *
from comun.figuras_c9e6 import *


class OchoCasos(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.casos()
        self.ordenar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def casos(self):
        with self.narrar("b1"):
            # «no conoces las densidades»
            self.en("densidades")
            C = Campanas9(centro=(0.0, -0.6), ancho=8.0, alto=5.0, r_rango=(-3.0, 5.0), v_max=0.45)
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            self.play(Create(c0), Create(c1), run_time=self.dur(0.7))
            camp = VGroup(c0, c1)
            punt = VGroup(DashedVMobject(c0.copy(), num_dashes=40), DashedVMobject(c1.copy(), num_dashes=40))
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(1.2).move_to(C.p(1.0, 0.47))
            self.play(FadeOut(camp), FadeIn(punt), run_time=self.dur(0.4))
            self.pop(q)

            # «Lo que tienes»
            self.en("tienes")
            g = VGroup(punt, q)
            self.play(g.animate.scale(0.55).move_to([-4.6, 2.3, 0]).set_opacity(0.35), run_time=self.dur(0.5))

            # «casos ya resueltos»
            self.en("casos")
            fichas = VGroup(*[ficha6(None, None, lado=0.7) for _ in range(8)]).arrange(RIGHT, buff=0.35)
            fichas.move_to([0, -0.6, 0])
            rng = np.random.default_rng(2)
            gotas = VGroup(*[Dot([x, 2.3 + rng.uniform(-0.3, 0.3), 0], radius=0.07, color=INK)
                             for x in rng.uniform(-5.6, -3.6, 8)])
            self.play(FadeIn(gotas), run_time=0.2)
            self.play(*[ReplacementTransform(gotas[i], fichas[i]) for i in range(8)], run_time=self.dur(0.7))
            self.fichas = fichas

            # «sabes la verdad»
            self.en("verdad")
            signos = [CASOS6[k][1] for k in REVUELTO6]
            marcadas = VGroup(*[ficha6(s, None, lado=0.7).move_to(f) for s, f in zip(signos, fichas)])
            self.play(*[ReplacementTransform(fichas[i], marcadas[i]) for i in range(8)], run_time=self.dur(0.5))
            self.fichas = marcadas

            # «un detector»
            self.en("detector")
            det = caja_detector6().move_to([0, 1.4, 0])
            flechas = VGroup(*[Arrow(det.get_bottom(), f.get_top(), buff=0.1, stroke_width=2, color=INK,
                                     max_tip_length_to_length_ratio=0.12) for f in marcadas])
            self.play(FadeIn(det, shift=DOWN * 0.15), run_time=self.dur(0.4))
            self.play(LaggedStart(*[GrowArrow(a) for a in flechas], lag_ratio=0.08), run_time=self.dur(0.6))
            self.det, self.flechas = det, flechas

            # «una puntuación»
            self.en("punt")
            nums = VGroup(*[Text(num(CASOS6[k][0]), color=TXT).scale(0.4).next_to(f, DOWN, buff=0.18)
                            for k, f in zip(REVUELTO6, marcadas)])
            self.play(LaggedStart(*[FadeIn(n, shift=DOWN * 0.1) for n in nums], lag_ratio=0.1), run_time=self.dur(0.7))
            self.nums = nums

            # «más parece hache uno»
            self.en("h1")
            fl = Arrow([5.9, -2.2, 0], [5.9, 0.4, 0], buff=0, color=C1, stroke_width=5)
            rot = VGroup(Text("Más alta", color=TXT).scale(0.38),
                         Text("Más parece", color=TXT).scale(0.38),
                         MathTex(r"H_1", color=C1).scale(0.6)).arrange(DOWN, buff=0.08)
            rot.next_to(fl, LEFT, buff=0.15).shift(DOWN * 0.1)
            self.play(GrowArrow(fl), FadeIn(rot), run_time=self.dur(0.5))
            self.h1 = VGroup(fl, rot)

            # «un análisis»
            self.en("analisis")
            ic1 = matraz(CIAN).scale(0.55).move_to([-5.7, -2.6, 0])
            self.play(FadeIn(ic1, scale=0.6), run_time=self.dur(0.35))
            # «correo basura»
            self.en("correo")
            ic2 = sobre(TXT).scale(0.5).move_to([-4.4, -2.6, 0])
            x2 = cruz(ERROR, 0.3).move_to(ic2.get_corner(UR))
            self.play(FadeIn(ic2, scale=0.6), FadeIn(x2), run_time=self.dur(0.35))
            # «tumores en radiografías»
            self.en("radio")
            placa = RoundedRectangle(corner_radius=0.06, width=0.8, height=0.95, color=INK, stroke_width=2.5)
            placa.set_fill("#2a3140", 1).move_to([-3.1, -2.6, 0])
            mancha = Dot(placa.get_center() + UR * 0.12, radius=0.09, color=TXT).set_opacity(0.85)
            self.play(FadeIn(placa, scale=0.6), FadeIn(mancha), run_time=self.dur(0.35))
            self.iconos = VGroup(ic1, ic2, x2, placa, mancha)
            self.fondo = g

    # ------------------------------------------------------------ b2
    def ordenar(self):
        with self.narrar("b2"):
            # «ocho casos»
            self.en("ocho")
            self.play(FadeOut(self.iconos), FadeOut(self.fondo), FadeOut(self.flechas), FadeOut(self.det),
                      FadeOut(self.h1), run_time=self.dur(0.4))

            # «cuatro positivos»
            self.en("pos")
            pos = [i for i, k in enumerate(REVUELTO6) if CASOS6[k][1]]
            neg = [i for i, k in enumerate(REVUELTO6) if not CASOS6[k][1]]
            r4p = Text("4 +", color=POS, weight=BOLD).scale(0.6).move_to([-2.0, 1.2, 0])
            self.play(*[self.fichas[i].marco.animate(rate_func=there_and_back).set_fill(POS, 0.7) for i in pos],
                      FadeIn(r4p), run_time=self.dur(0.5))

            # «cuatro negativos»
            self.en("neg")
            r4n = Text("4 −", color=NEG, weight=BOLD).scale(0.6).move_to([2.0, 1.2, 0])
            self.play(*[self.fichas[i].marco.animate(rate_func=there_and_back).set_fill(NEG, 0.7) for i in neg],
                      FadeIn(r4n), run_time=self.dur(0.5))

            # «Los ordenamos»
            self.en("ordenar")
            col = columna6(centro=(-1.6, 0.0), paso=0.82)
            viejas = VGroup(*[VGroup(f, n) for f, n in zip(self.fichas, self.nums)])
            anims = [ReplacementTransform(viejas[i], col.fichas[REVUELTO6[i]]) for i in range(8)]
            self.play(FadeOut(r4p), FadeOut(r4n), *anims, run_time=self.dur(1.2))
            self.col = col

            # «Queda así»
            self.en("queda")
            cursor = Triangle(color=ESTIMACION).scale(0.15).rotate(-PI / 2).set_fill(ESTIMACION, 1)
            cursor.next_to(col.fichas[0].marco, LEFT, buff=0.2)
            self.play(FadeIn(cursor, shift=RIGHT * 0.2), run_time=self.dur(0.3))

            def ilumina(idx, t):
                self.play(cursor.animate.next_to(col.fichas[idx[-1]].marco, LEFT, buff=0.2),
                          *[self.col.fichas[i].marco.animate.set_fill(opacity=0.6) for i in idx],
                          run_time=self.dur(t))

            # «positivo, positivo, negativo…»: una ficha por palabra
            for i in range(8):
                self.en(f"f{i + 1}")
                ilumina([i], 0.3)
            tira = tira6(centro=(3.4, 1.0), lado=0.55)
            self.play(FadeOut(cursor), FadeIn(tira, shift=LEFT * 0.2), run_time=self.dur(0.4))
            self.tira = tira

            # «No está perfecto»
            self.en("imperfecto")
            ideal = tira6([1, 1, 1, 1, 0, 0, 0, 0], centro=(3.4, -0.4), lado=0.55).set_opacity(0.4)
            rot_i = Text("Ideal", color=INK).scale(0.4).next_to(ideal, DOWN, buff=0.15)
            self.play(FadeIn(ideal), FadeIn(rot_i), run_time=self.dur(0.4))

            # «negativos colados»
            self.en("colados")
            aros = VGroup(*[Circle(radius=0.36, color=ERROR, stroke_width=4).move_to(self.col.fichas[i].marco)
                            for i in (2, 4)],
                          *[Circle(radius=0.34, color=ERROR, stroke_width=4).move_to(tira.fichas[i])
                            for i in (2, 4)])
            self.play(Create(aros), run_time=self.dur(0.5))

            # «entre los positivos»
            self.en("entre")
            self.resaltar(*[self.col.fichas[i].marco for i in (3, 5)], color=POS, run_time=self.dur(0.5))
