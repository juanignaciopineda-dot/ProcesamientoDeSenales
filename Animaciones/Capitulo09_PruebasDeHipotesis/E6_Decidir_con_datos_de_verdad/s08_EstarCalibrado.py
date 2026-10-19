"""Escena 08 — Estar calibrado: cortar en 0,5 solo es el máximo a posteriori si el número es una probabilidad."""
from comun.escena import *
from comun.figuras_c9e6 import *


def rejilla_cien(centro, lado: float = 0.27, buff: float = 0.04) -> VGroup:
    """Cien casillas grises en 10 × 10."""
    g = VGroup(*[Square(side_length=lado, stroke_width=1, color=INK).set_fill(INK, 0.25) for _ in range(100)])
    g.arrange_in_grid(10, 10, buff=buff).move_to([centro[0], centro[1], 0])
    return g


def pintar(rej: VGroup, positivos: int):
    """Las primeras `positivos` casillas en azul, el resto en magenta (por filas, mezcladas un poco)."""
    rng = np.random.default_rng(positivos)
    orden = rng.permutation(100)
    pos = set(orden[:positivos].tolist())
    return [c.animate.set_fill(POS if i in pos else NEG, 0.85).set_stroke(POS if i in pos else NEG)
            for i, c in enumerate(rej)]


class EstarCalibrado(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.calibrado()
        self.mal_calibrado()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def calibrado(self):
        with self.narrar("b1"):
            # «muchos detectores modernos»
            self.en("detector")
            det = caja_detector6().move_to([-5.2, 2.2, 0])
            sal = Arrow(det.get_right(), [-3.1, 2.2, 0], buff=0.1, color=INK, stroke_width=3)
            self.play(FadeIn(det, shift=RIGHT * 0.2), GrowArrow(sal), run_time=self.dur(0.5))

            # «entre cero y uno»
            self.en("regla")
            x0, x1, y = -2.6, 4.4, 2.2
            p = lambda v: np.array([x0 + v * (x1 - x0), y, 0])
            base = Line(p(0), p(1), color=INK, stroke_width=3)
            nums = VGroup(Text("0", color=INK).scale(0.42).next_to(p(0), DOWN, buff=0.15),
                          Text("1", color=INK).scale(0.42).next_to(p(1), DOWN, buff=0.15))
            m7 = Line(p(0.7) + DOWN * 0.18, p(0.7) + UP * 0.18, color=MEDIDA, stroke_width=5)
            t7 = Text("0,7", color=MEDIDA).scale(0.42).next_to(m7, DOWN, buff=0.12)
            self.play(Create(base), FadeIn(nums), run_time=self.dur(0.4))
            self.play(Create(m7), FadeIn(t7), run_time=self.dur(0.3))

            # «lo llaman probabilidad»
            self.en("prob")
            prob = Text("«Probabilidad»", color=MEDIDA).scale(0.45).next_to(m7, UP, buff=0.18)
            self.play(FadeIn(prob, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «corta en cero coma cinco»
            self.en("corte")
            m5 = Line(p(0.5) + DOWN * 0.35, p(0.5) + UP * 0.35, color=ESTIMACION, stroke_width=5)
            t5 = Text("Por defecto: 0,5", color=ESTIMACION).scale(0.42).next_to(m5, DOWN, buff=0.12).shift(LEFT * 0.5)
            self.play(Create(m5), FadeIn(t5), run_time=self.dur(0.4))

            # «la regla del máximo a posteriori»
            self.en("map")
            mp = MathTex(r"\text{MAP:}\ \ P(H_1 \mid r) > 0{,}5", color=TXT).scale(0.75).move_to([1.0, 1.05, 0])
            self.play(Write(mp), run_time=self.dur(0.7))

            # «de verdad la probabilidad a posteriori»
            self.en("deverdad")
            prob2 = Text("Probabilidad", color=MEDIDA).scale(0.45).move_to(prob)
            sub = Underline(prob2, color=MEDIDA, buff=0.05)
            self.play(ReplacementTransform(prob, prob2), Create(sub), run_time=self.dur(0.5))

            # «de todos los casos»
            self.en("todos")
            rej = rejilla_cien((-4.0, -1.9))
            self.play(LaggedStart(*[FadeIn(c) for c in rej], lag_ratio=0.01), run_time=self.dur(0.6))

            # «reciben un cero coma siete»
            self.en("cien")
            pu = Text("Puntuación 0,7", color=MEDIDA).scale(0.42).next_to(rej, UP, buff=0.15)
            self.play(FadeIn(pu, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «el setenta por ciento son positivos»
            self.en("setenta")
            c70 = Text("70 de 100", color=POS, weight=BOLD).scale(0.5).next_to(rej, DOWN, buff=0.15)
            self.play(*pintar(rej, 70), FadeIn(c70), run_time=self.dur(0.8))

            # «A eso se le llama»
            self.en("llama")
            ll = Brace(rej, LEFT, color=VERDE, buff=0.1)
            self.play(FadeIn(ll), run_time=self.dur(0.4))

            # «estar calibrado»
            self.en("calibrado")
            cal = tarjeta6("Calibrado", VERDE, ancho=2.6).move_to([-1.1, -1.1, 0])
            self.pop(cal)
            self.r1 = VGroup(rej, pu, c70, ll, cal)

    # ------------------------------------------------------------ b2
    def mal_calibrado(self):
        with self.narrar("b2"):
            # «ordenar perfectamente»
            self.en("ordena")
            rej = rejilla_cien((2.6, -1.9))
            pu = Text("Puntuación 0,7", color=MEDIDA).scale(0.42).next_to(rej, UP, buff=0.15)
            ok = VGroup(tilde(VERDE, 0.35), Text("Ordena bien", color=VERDE).scale(0.42)).arrange(RIGHT, buff=0.15)
            ok.move_to([5.75, -0.6, 0])
            self.play(FadeIn(rej), FadeIn(pu), FadeIn(ok), run_time=self.dur(0.5))

            # «mal calibrado»
            self.en("mal")
            c40 = Text("40 de 100", color=POS, weight=BOLD).scale(0.5).next_to(rej, DOWN, buff=0.15)
            mal = tarjeta6("Mal calibrado", ERROR, ancho=2.4, escala=0.4).move_to([5.75, -1.5, 0])
            self.play(*pintar(rej, 40), FadeIn(c40), run_time=self.dur(0.7))
            self.pop(mal)

            # «su cero coma cinco»
            self.en("punto")
            self.corte()
            P = PlanoRoc9(origen=(-5.4, -2.5), lado=4.9)
            curva = P.curva()
            u0, u1 = 1.0, 0.25
            pt = P.punto(*roc9(u0), color=ESTIMACION, radio=0.12)
            rp = Text("0,5", color=ESTIMACION, weight=BOLD).scale(0.45)
            rp.add_updater(lambda m: m.next_to(pt, DR, buff=0.08))
            self.add(P, P.diagonal(), curva)
            self.play(FadeIn(pt, scale=0.4), FadeIn(rp), run_time=self.dur(0.4))

            # «un punto cualquiera»
            self.en("cualquiera")
            u = ValueTracker(u0)
            pt.add_updater(lambda m: m.move_to(P.p(*roc9(u.get_value()))))
            self.play(u.animate.set_value(-0.6), run_time=self.dur(0.6))
            self.play(u.animate.set_value(u1), run_time=self.dur(0.4))
            pt.clear_updaters()

            # «Un área alta»
            self.en("area")
            area = area_curva6(P)
            aa = VGroup(Text("Área alta", color=ROC).scale(0.5), tilde(INK, 0.35)).arrange(RIGHT, buff=0.15)
            aa.move_to([3.4, 1.4, 0])
            self.play(FadeIn(area), FadeIn(aa), run_time=self.dur(0.5))

            # «ordena bien»
            self.en("bien")
            self.play(aa[1].animate.set_color(VERDE), run_time=self.dur(0.3))

            # «No dice que»
            self.en("nodice")
            self.play(pt.animate(rate_func=there_and_back).scale(1.8), run_time=self.dur(0.4))

            # «el sitio donde cortar»
            self.en("cortar")
            rp.clear_updaters()
            q = Text("?", color=ERROR, weight=BOLD).scale(0.8).move_to(P.p(*roc9(u1)) + UP * 0.45 + LEFT * 0.1)
            t = tarjeta6("Área alta ≠ Buen corte", ERROR, ancho=4.2).move_to([3.4, 0.2, 0])
            self.pop(q, t)
