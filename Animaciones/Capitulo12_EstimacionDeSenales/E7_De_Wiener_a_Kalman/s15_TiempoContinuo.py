"""Escena 15 — Lo mismo en tiempo continuo: las tres fórmulas, apareadas con las discretas."""
from comun.escena import *


class TiempoContinuo(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        tal = Tallos([0.6, 1.0, 0.7, 0.4, 0.8, 0.5, 0.3], centro=(-4.4, 3.0), paso=0.55, unidad=0.8, color=SENAL)
        Lc = Lienzo(ancho=3.8, alto=1.1, t_rango=(0, 6), v_max=1.2, centro=(4.4, 3.0))
        t = np.linspace(0, 6, 160)
        cont = Lc.curva(t, 0.4 + 0.35 * np.sin(t) + 0.2 * np.sin(2.3 * t), SENAL, 3.0)
        aprox = MathTex("\\approx", color=INK).scale(1.0).move_to([0, 3.0, 0])
        lab = [etiqueta(s, INK, 0.5).move_to([-5.4, y, 0]) for s, y in
               (("no causal", 1.4), ("causal", 0.0), ("con adelanto T", -1.4))]
        for l in lab:
            l.align_to([-6.6, 0, 0], LEFT)
        f1 = formula("H(j\\omega)", "=", "S_{yx}(j\\omega)", "\\Big/", "S_{xx}(j\\omega)", escala=0.85,
                     colores={0: ESTIMACION, 2: AMBAR}).move_to([0.8, 1.4, 0])
        f2 = formula("H", "=", "\\frac{1}{F(j\\omega)}", "\\Big[", "\\frac{S_{yx}}{F(-j\\omega)}", "\\Big]_+",
                     escala=0.85, colores={0: ESTIMACION}).move_to([0.8, 0.0, 0])
        f3 = formula("H(s)", "=", "\\frac{1}{F(s)}", "\\Big[", "e^{sT}F(s)", "\\Big]_+", escala=0.85,
                     colores={0: ESTIMACION}).move_to([0.8, -1.4, 0])
        flat = Line([-1.2, -2.6, 0], [4.2, -2.6, 0], color=RUIDO, stroke_width=4)
        l_inf = Text("∞", color=RUIDO, weight=BOLD).scale(0.7).move_to([5.0, -2.6, 0])
        a_i = DoubleArrow([-1.5, -2.6, 0], [-1.2, -2.6, 0], color=RUIDO, buff=0)
        ideal = etiqueta("idealización", RUIDO, 0.5).move_to([1.5, -3.3, 0])
        with self.narrar("b1"):
            # «tiempo discreto»
            self.en("discreto")
            self.play(Create(tal.base), *[Create(t_) for t_ in tal.tallos], *[FadeIn(p) for p in tal.puntos],
                      run_time=self.dur(1.0))
            # «tiempo continuo»
            self.en("continuo")
            self.play(Create(Lc.base()), Create(cont), run_time=self.dur(0.9))
            # «con demostraciones análogas»
            self.en("analogas")
            self.play(FadeIn(aprox), run_time=self.dur(0.6))
            # «No causal»
            self.en("nc")
            self.play(FadeIn(lab[0]), run_time=0.4)
            # «hache es»
            self.en("hache")
            self.play(FadeIn(f1[0]), FadeIn(f1[1]), run_time=self.dur(0.5))
            # «la densidad cruzada»
            self.en("cruzada")
            self.play(FadeIn(f1[2]), run_time=self.dur(0.7))
            # «entre la densidad de lo medido»
            self.en("entre")
            self.play(FadeIn(f1[3]), FadeIn(f1[4]), run_time=self.dur(0.7))
            # «Causal»
            self.en("c")
            self.play(FadeIn(lab[1]), FadeIn(f2[0]), FadeIn(f2[1]), run_time=self.dur(0.5))
            # «uno entre F»
            self.en("unof")
            self.play(FadeIn(f2[2]), run_time=self.dur(0.6))
            # «la parte causal»
            self.en("parte")
            self.play(FadeIn(f2[3]), FadeIn(f2[5]), run_time=self.dur(0.6))
            # «la cruzada entre F de menos jota omega»
            self.en("cruzadaf")
            self.play(FadeIn(f2[4]), run_time=self.dur(0.9))
            # «predecir con antelación te segundos»
            self.en("pred")
            self.play(FadeIn(lab[2]), FadeIn(f3[0]), FadeIn(f3[1]), FadeIn(f3[2]), run_time=self.dur(0.9))
            # «por la parte causal de»
            self.en("parte2")
            self.play(FadeIn(f3[3]), FadeIn(f3[5]), run_time=self.dur(0.6))
            # «e elevado a ese te»
            self.en("exp")
            self.play(FadeIn(f3[4]), run_time=self.dur(0.8))
            # «La diferencia»
            self.en("diferencia")
            self.play(VGroup(f1, f2, f3, *lab).animate.scale(0.85, about_point=[-6.6, 1.5, 0]), run_time=self.dur(0.6))
            # «el ruido blanco continuo tiene potencia infinita»
            self.en("infinita")
            self.play(Create(flat), FadeIn(l_inf), run_time=self.dur(1.2))
            # «una idealización»
            self.en("ideal")
            self.play(FadeIn(ideal), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
