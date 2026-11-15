"""Escena 14 — La moneda (espectro plano) por el promediador (|H|² = cos²(Ω/2)): el filtro le da forma al ruido."""
from comun.escena import *


class MonedaEnFrecuencia(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        ex = dict(ancho=3.9, alto=2.2)
        a1, l1 = ejes((0, PI), (0, 1.3), x_label=r"\Omega", **ex)
        a2, l2 = ejes((0, PI), (0, 1.3), x_label=r"\Omega", **ex)
        a3, l3 = ejes((0, PI), (0, 1.3), x_label=r"\Omega", **ex)
        p1 = VGroup(a1, l1).move_to([-4.6, -0.2, 0])
        p2 = VGroup(a2, l2).move_to([0.0, -0.2, 0])
        p3 = VGroup(a3, l3).move_to([4.6, -0.2, 0])
        t1 = formula(r"S_{xx}", escala=0.9, colores={0: SENAL}).move_to([-4.6, 1.5, 0])
        t2 = formula(r"|H|^2", escala=0.9, colores={0: ESTIMACION}).move_to([0.0, 1.5, 0])
        t3 = formula(r"S_{yy}", escala=0.9, colores={0: MEDIDA}).move_to([4.6, 1.5, 0])
        mult = formula(r"\times", escala=1.3).move_to([-2.3, 0.2, 0])
        igual = formula(r"=", escala=1.3).move_to([2.3, 0.2, 0])
        moneda = tira_pm1([1, -1, -1, 1, -1, 1, 1], lado=0.46).move_to([-4.8, 3.3, 0])
        sin_mem = etiqueta("sin memoria", INK, 0.5).move_to([-1.3, 3.3, 0])
        imp = Tallos([1.0], centro=(1.2, 3.3), paso=0.6, unidad=0.5, color=AMBAR, extra=2)
        r_xx = formula(r"R_{xx}", "=", r"\text{impulso}", escala=0.7).move_to([3.3, 3.3, 0])
        f_fl = Arrow([-4.6, 2.6, 0], [-4.6, 1.9, 0], color=AMBAR, buff=0, stroke_width=4)
        f_tx = etiqueta("F", AMBAR, 0.55, BOLD).next_to(f_fl, RIGHT, buff=0.1)
        plana = a1.plot(lambda w: 1.0, x_range=[0, PI], color=SENAL, stroke_width=5)
        pts = VGroup(*[Dot(a1.c2p(w, 1.0), radius=0.08, color=AMBAR) for w in np.linspace(0.3, 2.9, 5)])
        h2 = lambda w: np.cos(w / 2) ** 2
        c_h = a2.plot(h2, x_range=[0, PI], color=ESTIMACION, stroke_width=5)
        d0 = Dot(a2.c2p(0, 1.0), radius=0.12, color=VERDE)
        dp = Dot(a2.c2p(PI, 0.0), radius=0.12, color=ROJO)
        v_cont = MathTex("1", color=VERDE).scale(0.8).next_to(d0, RIGHT, buff=0.2).shift(UP * 0.2)
        v_rap = MathTex("0", color=ROJO).scale(0.8).next_to(dp, UR, buff=0.1)
        alterna = tira_pm1([1, -1, 1, -1, 1, -1, 1], lado=0.46).move_to([0.0, -2.6, 0])
        alterna_y = Tallos([0, 0, 0, 0, 0, 0, 0], centro=(0.0, -3.4), paso=0.52, unidad=1.0, color=MEDIDA)
        c_y = a3.plot(h2, x_range=[0, PI], color=MEDIDA, stroke_width=5)
        alta = Arrow(a3.c2p(1.3, 0.95), a3.c2p(2.9, 0.12), color=ROJO, buff=0.05, stroke_width=4)
        forma = self.texto_centrado("el filtro le da forma", "al ruido", color=AMBAR, escala=0.6).move_to([4.6, -3.2, 0])

        with self.narrar("b1"):
            # «la moneda»
            self.en("moneda")
            self.play(FadeIn(moneda), FadeIn(p1), FadeIn(t1), run_time=self.dur(0.7))

            # «no tiene memoria»
            self.en("sin_mem")
            self.play(FadeIn(sin_mem), run_time=self.dur(0.4))

            # «un impulso»
            self.en("impulso")
            self.play(FadeIn(imp), FadeIn(r_xx), run_time=self.dur(0.6))

            # «cuya transformada»
            self.en("transf")
            self.play(GrowArrow(f_fl), FadeIn(f_tx), run_time=self.dur(0.5))

            # «plana»
            self.en("plana")
            self.play(Create(plana), run_time=self.dur(0.7))

            # «igual en todas las frecuencias»
            self.en("todas")
            self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in pts], lag_ratio=0.2), run_time=self.dur(1.0))

            # «El promediador»
            self.en("prom")
            self.play(FadeIn(p2), FadeIn(t2), FadeIn(mult), Create(c_h), run_time=self.dur(1.0))

            # «deja pasar la continua»
            self.en("continua")
            self.play(FadeIn(d0), FadeIn(v_cont), run_time=self.dur(0.5))

            # «anula la frecuencia más rápida»
            self.en("rapida")
            self.play(FadeIn(dp), FadeIn(v_rap), run_time=self.dur(0.5))

            # «alterna más uno y menos uno»
            self.en("alterna")
            self.play(FadeIn(alterna), run_time=self.dur(0.6))
            self.play(ReplacementTransform(alterna.copy(), alterna_y), run_time=self.dur(0.8))

            # «la curva plana cae»
            self.en("cae")
            self.play(FadeIn(p3), FadeIn(t3), FadeIn(igual), Create(c_y), run_time=self.dur(1.0))

            # «hacia las frecuencias altas»
            self.en("altas")
            self.play(GrowArrow(alta), run_time=self.dur(0.6))

            # «dado forma al ruido»
            self.en("forma")
            self.pop(forma)
        self.wait(1.0)
        self.limpiar()
