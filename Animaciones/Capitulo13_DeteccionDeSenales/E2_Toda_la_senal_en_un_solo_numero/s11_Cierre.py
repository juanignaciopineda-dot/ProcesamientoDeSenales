"""Escena 11 — Cierre: resumen del episodio y pregunta del siguiente (E3, «¿Cuánto nos equivocamos?»)."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        rng = np.random.default_rng(21)
        n = 160
        t = np.arange(n)
        ruido = rng.normal(0, 1.2, n)
        pulso = np.zeros(n)
        pulso[70:90] = [0.8, 1.4, 1.9, 2.3, 2.5, 2.5, 2.3, 1.9, 1.9, 2.3, 2.5, 2.3, 1.9, 1.4, 0.8, 0.4, 0.2, 0.1, 0.0, 0.0]
        La = Lienzo(ancho=5.4, alto=2.2, t_rango=(0, n - 1), v_max=6, centro=(2.8, 2.5))
        tr_ruido = La.curva(t, ruido, RUIDO, 2.6)
        tr_pulso = La.curva(t, pulso, SENAL, 4.5)
        s = Barras((2, 2, 1), centro=(-5.0, 2.5), paso=0.8, unidad=0.38, color=SENAL, ancho=0.5)
        r = Barras((3, 1, 2), centro=(-5.0, 1.0), paso=0.8, unidad=0.38, color=MEDIDA, ancho=0.5)
        F = formula("g", "=", r"\sum r[n]\,s[n]", escala=1.7, colores={0: AMBAR, 2: MEDIDA}).move_to([-1.2, 0.2, 0])
        parecida = Text("lo parecida que es r a s", color=MEDIDA).scale(0.7).move_to([-1.2, -0.9, 0])
        gam = formula(r"\gtrless", r"\gamma", escala=1.7, colores={0: AMBAR, 1: AMBAR}).next_to(F, RIGHT, buff=0.3)
        suf = Text("no tira nada", color=VERDE, weight=BOLD).scale(0.8).move_to([4.2, -0.9, 0])
        marco = SurroundingRectangle(VGroup(F, gam), color=ESTIMACION, buff=0.25)
        # las dos campanas del próximo episodio, con sus colas
        Lb = Lienzo(ancho=9.6, alto=1.7, t_rango=(-6, 15), v_max=1.1, centro=(0.0, -2.9))
        b0 = campana_curva(Lb, 0, 3.0, RUIDO, 4)
        b1 = campana_curva(Lb, 9, 3.0, SENAL, 4)
        base = Lb.base()
        um = DashedLine(Lb.p(4.5, 0), Lb.p(4.5, 1.15), color=AMBAR, stroke_width=4)
        xs0 = np.linspace(4.5, 15, 60)
        cola0 = Polygon(*[Lb.p(x, np.exp(-0.5 * (x / 3.0) ** 2)) for x in xs0], Lb.p(15, 0), Lb.p(4.5, 0),
                        color=ERROR, stroke_width=0).set_fill(ERROR, 0.7)
        xs1 = np.linspace(-6, 4.5, 60)
        cola1 = Polygon(Lb.p(-6, 0), *[Lb.p(x, np.exp(-0.5 * ((x - 9) / 3.0) ** 2)) for x in xs1], Lb.p(4.5, 0),
                        color=ERROR, stroke_width=0).set_fill(ERROR, 0.7)
        titulo_e3 = Text("¿Cuánto nos equivocamos?", color=AMBAR, weight=BOLD).scale(1.1).move_to([0, 3.0, 0])

        with self.narrar("b1"):
            # «Resumamos»
            self.en("resumamos")
            self.play(Create(s.base), *[GrowFromEdge(b, DOWN) for b in s.barras], run_time=self.dur(0.6))
            self.play(Create(r.base), *[GrowFromEdge(b, DOWN) for b in r.barras], run_time=self.dur(0.5))

            # «Una señal conocida enterrada en ruido gaussiano»
            self.en("conocida")
            self.play(Create(tr_pulso), run_time=self.dur(0.8))
            self.play(Create(tr_ruido), tr_pulso.animate.set_stroke(opacity=0.5), run_time=self.dur(1.2))

            # «un solo número»
            self.en("numero")
            self.play(*[FadeIn(F[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(1.0))

            # «lo parecida que es lo recibido a la señal»
            self.en("parecida")
            self.play(FadeIn(parecida, shift=UP * 0.1), run_time=self.dur(0.7))

            # «comparada con un umbral»
            self.en("umbral")
            self.play(FadeIn(gam, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «Ese número no tira nada»
            self.en("nada")
            self.pop(suf)

            # «el mismo detector»
            self.en("mismo")
            self.play(Create(marco), run_time=self.dur(0.7))

            # «qué calcular»
            self.en("calcular")
            self.play(Indicate(F[2], color=AMBAR, scale_factor=1.1), run_time=self.dur(0.6))

            # «dónde cortar»
            self.en("cortar")
            self.play(Indicate(gam[1], color=AMBAR, scale_factor=1.5), run_time=self.dur(0.6))

            # «cuánto vamos a equivocarnos»
            self.en("equivocar")
            self.play(*[FadeOut(m) for m in (s, r, tr_ruido, tr_pulso, parecida, suf)], run_time=self.dur(0.4))
            self.play(Create(base), Create(b0), Create(b1), Create(um), run_time=self.dur(1.0))
            self.play(FadeIn(cola0), FadeIn(cola1), run_time=self.dur(0.6))

            # «y de qué depende»
            self.en("depende")
            self.play(Indicate(cola0, color=ERROR, scale_factor=1.15), Indicate(cola1, color=ERROR, scale_factor=1.15),
                      run_time=self.dur(0.8))

            # «¿cuánto nos equivocamos?»
            self.en("titulo")
            self.pop(titulo_e3)
        self.wait(1.2)
        self.limpiar()
