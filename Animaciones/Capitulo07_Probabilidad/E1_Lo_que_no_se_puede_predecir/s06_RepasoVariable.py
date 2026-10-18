"""Escena 06 — Repaso: variable aleatoria, distribución, campana y media."""
from comun.escena import *


class RepasoVariable(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.bloque_variable()
        self.bloque_cimientos()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bloque_variable(self):
        L = Lienzo(ancho=11.0, alto=3.0, t_rango=(0, 7), v_max=1.0, centro=(0.0, -1.2))
        recta = L.base(INK, 3.0)
        marcas = VGroup(*[Text(str(k), color=INK).scale(0.45).move_to([float(L.x(k)), -1.65, 0]) for k in range(1, 7)])

        with self.narrar("b1"):
            # «Una variable aleatoria»
            self.en("va")
            tit = Text("Variable aleatoria", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.3, 0])
            self.pop(tit)
            eje = eje_v7(L, 0, 1.15)
            self.play(Create(recta), Create(eje), FadeIn(marcas), run_time=self.dur(0.6))

            # «un número que depende del resultado»
            self.en("numero")
            d3 = dado_n(3).move_to([float(L.x(3)), 1.3, 0])
            fl = Arrow(d3.get_bottom(), [float(L.x(3)), -1.3, 0], color=INK, stroke_width=4, buff=0.1)
            self.play(FadeIn(d3), GrowArrow(fl), run_time=self.dur(0.6))

            # «lo que marca el dado»
            self.en("marca")
            d5 = dado_n(5).move_to([float(L.x(5)), 1.3, 0])
            fl5 = Arrow(d5.get_bottom(), [float(L.x(5)), -1.3, 0], color=INK, stroke_width=4, buff=0.1)
            self.play(ReplacementTransform(d3, d5), ReplacementTransform(fl, fl5), run_time=self.dur(0.6))

            # «la tensión que se mide»
            self.en("tension")
            volt = caja("3,2 V", CIAN, ancho=1.7, alto=0.8, scale=0.6).move_to([float(L.x(3.2)), 1.3, 0])
            fl3 = Arrow(volt.get_bottom(), [float(L.x(3.2)), -1.3, 0], color=CIAN, stroke_width=4, buff=0.1)
            self.play(FadeIn(volt), GrowArrow(fl3), run_time=self.dur(0.6))

            # «Su distribución»
            self.en("distribucion")
            self.play(*[FadeOut(m) for m in (d5, fl5, volt, fl3)], run_time=0.25)
            barras = VGroup(*[Rectangle(width=0.8, height=1.0, color=SENAL, stroke_width=2).set_fill(SENAL, 0.35)
                              .move_to([float(L.x(k)), -1.2 + 0.5, 0]) for k in range(1, 7)])
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in barras], lag_ratio=0.1), run_time=self.dur(0.9))

            # «con qué probabilidad»
            self.en("con_prob")
            fr = VGroup(*[Text("1/6", color=TXT).scale(0.45).move_to([float(L.x(k)), -0.45, 0]) for k in range(1, 7)])
            self.play(LaggedStart(*[FadeIn(f) for f in fr], lag_ratio=0.08), run_time=self.dur(0.7))

            # «como una curva»
            self.en("curva")
            x = np.linspace(0.3, 6.7, 160)
            campana = L.curva(x, np.exp(-0.5 * ((x - 3.5) / 1.2) ** 2) * 0.95, SENAL, 5.0)
            self.play(FadeOut(barras), FadeOut(fr), Create(campana), run_time=self.dur(1.0))

            # «la campana de Gauss»
            self.en("campana")
            rel = area_bajo(L, x, np.exp(-0.5 * ((x - 3.5) / 1.2) ** 2) * 0.95, SENAL, 0.25)
            gau = Text("Campana de Gauss", color=AMBAR, weight=BOLD).scale(0.65).move_to([3.9, 2.3, 0])
            self.play(FadeIn(rel), run_time=0.4)
            self.pop(gau)

            # «la media es el valor»
            self.en("media")
            tri = Triangle(color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.6).scale(0.22).move_to([float(L.x(3.5)), -1.45, 0])
            med = Text("Media", color=AMBAR, weight=BOLD).scale(0.55).move_to([float(L.x(3.5)), -2.05, 0])
            self.pop(VGroup(tri, med))

            # «se reparten los resultados»
            self.en("reparten")
            rng = np.random.default_rng(6)
            vals = np.clip(rng.normal(3.5, 1.2, 14), 0.4, 6.6)
            pts = VGroup(*[Dot([float(L.x(v)), -1.2 + 0.12 * (i % 3), 0], radius=0.07, color=AMBAR) for i, v in enumerate(vals)])
            self.play(LaggedStart(*[GrowFromCenter(d) for d in pts], lag_ratio=0.06), run_time=self.dur(0.9))

    # ------------------------------------------------------------ b2
    def bloque_cimientos(self):
        with self.narrar("b2"):
            # «Si todo esto te suena»
            self.en("suena")
            self.corte()
            tarjetas = VGroup(*[caja(txt, SENAL, ancho=3.4, alto=0.9, scale=0.5) for txt in
                                ("Experimento", "Variable aleatoria", "Distribución")])
            tarjetas.arrange(RIGHT, buff=0.5).move_to([0, 2.6, 0])
            ticks = VGroup(*[tilde(VERDE, 0.35).next_to(c, DOWN, buff=0.25) for c in tarjetas])
            self.pop(tarjetas)
            self.play(LaggedStart(*[FadeIn(t) for t in ticks], lag_ratio=0.2), run_time=self.dur(0.5))

            # «no pasa nada»
            self.en("nada")
            nn = Text("No pasa nada", color=TXT, weight=BOLD).scale(0.8).move_to([0, 0.8, 0])
            self.pop(nn)

            # «en este capítulo»
            self.en("capitulo")
            cap = Text("Capítulo 7", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -0.3, 0])
            self.pop(cap)

            # «cada una de estas ideas»
            self.en("ideas")
            self.play(LaggedStart(*[t.animate(rate_func=there_and_back).set_stroke(AMBAR, width=5) for t in tarjetas],
                                  lag_ratio=0.3), run_time=self.dur(1.2))

            # «desde cero»
            self.en("cero")
            b1 = caja("Desde cero", AMBAR, ancho=7.5, alto=0.8, scale=0.55).move_to([0, -3.0, 0])
            self.play(GrowFromEdge(b1, DOWN), run_time=self.dur(0.5))

            # «con ejemplos y con números»
            self.en("ejemplos")
            b2 = caja("Con ejemplos y con números", VERDE, ancho=7.5, alto=0.8, scale=0.55).move_to([0, -2.1, 0])
            self.play(GrowFromEdge(b2, DOWN), run_time=self.dur(0.5))

            # «todo el resto de la materia se apoya en ellas»
            self.en("apoya")
            b3 = VGroup(*[caja(str(k), SENAL, ancho=1.0, alto=0.8, scale=0.55) for k in range(8, 14)])
            b3.arrange(RIGHT, buff=0.1).move_to([0, -1.2, 0])
            self.play(LaggedStart(*[GrowFromEdge(c, DOWN) for c in b3], lag_ratio=0.1), run_time=self.dur(0.9))

            # «se apoya en ellas»
            self.en("ellas")
            self.play(b1.animate(rate_func=there_and_back).set_stroke(AMBAR, width=6),
                      b2.animate(rate_func=there_and_back).set_stroke(VERDE, width=6), run_time=self.dur(0.9))

            # «la primera pregunta»
            self.en("primera")
            self.play(*[FadeOut(m) for m in (tarjetas, ticks, nn, cap, b1, b2, b3)], run_time=0.3)
            gq = Text("?", color=AMBAR, weight=BOLD).scale(3.0).move_to([0, 0.3, 0])
            self.pop(gq)

            # «es la más importante»
            self.en("importante")
            self.play(gq.animate(rate_func=there_and_back).scale(1.3), run_time=self.dur(0.7))

            # «¿por qué una materia de señales necesita tanta probabilidad?»
            self.en("porque")
            pregunta = self.texto_centrado("¿Por qué una materia de señales", "necesita tanta probabilidad?", escala=0.85)
            self.play(FadeOut(gq), run_time=0.2)
            self.play(FadeIn(pregunta, shift=UP * 0.2), run_time=self.dur(0.5))
