"""Escena 15 — Cuando las mediciones son muestras de una señal: las mismas ecuaciones normales (caps. 10 y 12)."""
from comun.escena import *
from comun.figuras_c8e5 import *


def senal(t):
    t = np.asarray(t, dtype=float)
    return 1.0 * np.sin(0.85 * t + 0.4) + 0.55 * np.sin(2.1 * t + 1.0) + 0.25 * np.sin(3.4 * t)


class MuestrasDeUnaSenal(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        L = Lienzo(ancho=10.0, alto=2.4, t_rango=(0, 10), v_max=2.0, centro=(-0.8, 0.95))
        tt = np.linspace(0, 8, 240)
        curva = L.curva(tt, senal(tt), color=SENAL, ancho=3.5)
        base = L.base(color=INK, ancho=1.6)
        tallos = VGroup(*[Line(L.p(k, 0), L.p(k, float(senal(k))), color=MEDIDA, stroke_width=4) for k in range(9)])
        puntas = VGroup(*[Dot(L.p(k, float(senal(k))), radius=0.08, color=MEDIDA) for k in range(9)])
        alturas = {8: 2.75, 7: 3.35, 6: 2.75}
        rot = {k: MathTex(t, color=MEDIDA).scale(0.85).move_to([L.x(k), alturas[k], 0])
               for k, t in ((8, r"x[n-1]"), (7, r"x[n-2]"), (6, r"x[n-3]"))}
        lin = formula(r"C_{xx}", r"\,\mathbf{h}", "=", r"\mathbf{c}_{xy}", escala=1.3,
                      colores={1: ESTIMACION, 3: SENAL}).move_to([0, -1.05, 0])
        arcos = VGroup(*[ArcBetweenPoints(L.p(a, float(senal(a))), L.p(b, float(senal(b))), angle=TAU / 4,
                                          color=AMBAR, stroke_width=3) for a, b in ((6, 7), (7, 8), (6, 8))])
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.1).move_to(L.p(9, 0.9))
        pred = Dot(L.p(9, float(senal(9))), radius=0.14, color=ESTIMACION)
        lbl_p = Text("Capítulo 10 · Predecir", color=AMBAR).scale(0.5).move_to([-3.4, -3.5, 0])
        L2 = Lienzo(ancho=4.2, alto=1.2, t_rango=(0, 1), v_max=1.0, centro=(3.4, -2.55))
        rng = np.random.default_rng(13)
        t2 = np.linspace(0, 1, 70)
        limpia = 0.7 * np.sin(2 * PI * 1.3 * t2 + 0.5)
        sucia = L2.curva(t2, limpia + rng.normal(0, 0.22, 70), color=MEDIDA, ancho=2.2)
        buena = L2.curva(t2, limpia, color=SENAL, ancho=4)
        lbl_l = Text("Capítulo 12 · Limpiar", color=AMBAR).scale(0.5).move_to([3.4, -3.5, 0])
        mini_p = VGroup(*[Line([-4.6 + 0.5 * i, -2.55, 0], [-4.6 + 0.5 * i, -2.55 + v, 0], color=MEDIDA, stroke_width=4)
                          for i, v in enumerate([0.4, 0.7, 0.55, 0.85])])
        mini_q = Dot([-2.6, -2.55 + 0.75, 0], radius=0.11, color=ESTIMACION)

        with self.narrar("b1"):
            # «un adelanto»
            self.en("adelanto")
            self.play(Create(base), run_time=0.3)
            self.play(Create(curva), run_time=self.dur(1.5), rate_func=linear)

            # «muestras de una misma señal»
            self.en("muestras")
            self.play(LaggedStart(*[AnimationGroup(Create(l), FadeIn(p)) for l, p in zip(tallos, puntas)],
                                  lag_ratio=0.15), run_time=self.dur(1.2))

            # «hace un segundo»
            self.en("m1")
            self.play(tallos[8].animate.set_stroke(width=8), FadeIn(rot[8], shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «hace dos»
            self.en("m2")
            self.play(tallos[7].animate.set_stroke(width=8), FadeIn(rot[7], shift=DOWN * 0.1), run_time=self.dur(0.35))

            # «hace tres»
            self.en("m3")
            self.play(tallos[6].animate.set_stroke(width=8), FadeIn(rot[6], shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «exactamente las mismas»
            self.en("mismas")
            self.play(FadeIn(lin, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Covarianzas entre las muestras»
            self.en("cxx")
            self.play(lin[0].animate.set_color(AMBAR), Create(arcos), run_time=self.dur(0.8))

            # «por los pesos»
            self.en("h")
            self.resaltar(lin[1], color=AMBAR, escala=1.3)

            # «lo que se quiere adivinar»
            self.en("cxy")
            self.resaltar(lin[3], color=AMBAR, escala=1.3)
            self.pop(q)

            # «predeciremos el futuro de una señal»
            self.en("pred")
            self.play(ReplacementTransform(q, pred), run_time=self.dur(0.5))
            self.play(Create(mini_p), FadeIn(mini_q), FadeIn(lbl_p), run_time=self.dur(0.6))

            # «limpiaremos el ruido de una grabación»
            self.en("limpia")
            self.play(Create(sucia), run_time=self.dur(0.6))
            self.play(Create(buena), FadeIn(lbl_l), run_time=self.dur(0.6))

            # «en los capítulos diez y doce»
            self.en("caps")
            self.resaltar(lbl_p, lbl_l, color=AMBAR, escala=1.12, run_time=0.7)
        self.wait(1.0)
        self.limpiar()
