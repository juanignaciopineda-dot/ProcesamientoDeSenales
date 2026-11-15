"""Escena 08 — Un periodograma es una sola muestra del ensemble: por qué grabar más no ayuda."""
from comun.escena import *


class UnaSolaMuestra(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.una_medida()
        self.ensemble()
        self.que_promediar()
        self.wait(1.0)
        self.limpiar()

    def una_medida(self):
        L1 = Lienzo(ancho=9.0, alto=1.2, t_rango=(0, 10), v_max=2.6, centro=(-0.8, 3.3))
        t = np.linspace(0, 10, 400)
        v = 0.8 * serie(5, 400, 0.0)
        corta = L1.curva(t[:40], v[:40], RUIDO, 2.6)
        larga = L1.curva(t, v, RUIDO, 2.4)
        P = Lienzo(ancho=11.0, alto=3.0, t_rango=(0, 1), v_max=5.0, centro=(0, -2.8))
        bos = bosque_f(P, periodograma_blanco(8, 320), MEDIDA, 2.2)
        plano = P.curva([0, 1], [1, 1], SENAL, 4)
        pregunta = MathTex("?", color=ROJO).scale(1.6).move_to([5.9, -1.8, 0])
        mas = VGroup(*[Line(P.p(x, 0), P.p(x, 0.18), color=AMBAR, stroke_width=3) for x in np.linspace(0, 1, 90)])
        una = Line(P.p(0.55, 0), P.p(0.55, 5.0), color=AMBAR, stroke_width=4)
        v_una = periodograma_blanco(8, 320)[int(0.55 * 319)]
        punto = Dot(P.p(0.55, v_una), radius=0.13, color=AMBAR)
        et_una = etiqueta("1 medida", AMBAR, 0.55).move_to([2.6, -0.7, 0])
        cap7 = etiqueta("Capítulo 7", INK, 0.55).move_to([-5.6, 1.9, 0])
        R = Lienzo(ancho=3.8, alto=1.7, t_rango=(0, 1), v_max=3.0, centro=(3.6, 1.2))
        media_r = DashedLine(R.p(0, 1), R.p(1, 1), color=SENAL, stroke_width=3)
        d_unica = Dot(R.p(0.5, 2.5), radius=0.12, color=RUIDO)
        lejos_f = DoubleArrow(R.p(0.62, 1), R.p(0.62, 2.5), color=ROJO, buff=0, stroke_width=3.5, max_tip_length_to_length_ratio=0.15)
        rng = np.random.default_rng(3)
        otros = VGroup(*[Dot(R.p(x, y), radius=0.09, color=RUIDO) for x, y in zip(np.linspace(0.08, 0.92, 14), 1 + rng.normal(0, 0.6, 14))])
        prom = Dot(R.p(0.5, 1), radius=0.14, color=ESTIMACION)
        with self.narrar("b1"):
            self.en("porque")
            self.play(Create(P.base()), Create(plano), Create(bos), run_time=self.dur(0.9))
            self.pop(pregunta)
            self.en("larga")
            self.play(Create(L1.base()), Create(corta), run_time=self.dur(0.4))
            self.play(FadeOut(corta), Create(larga), run_time=self.dur(0.9))
            self.en("mas_frec")
            self.play(Create(mas, lag_ratio=0.03), run_time=self.dur(1.0))
            self.en("una_medida")
            self.play(FadeOut(mas), Create(una), FadeIn(punto), FadeIn(et_una), run_time=self.dur(0.6))
            self.en("cap7")
            self.play(FadeIn(cap7), Create(R.base()), Create(media_r), run_time=self.dur(0.6))
            self.en("unica")
            self.play(FadeIn(d_unica), run_time=0.4)
            self.en("lejos")
            self.play(Create(lejos_f), run_time=0.5)
            self.en("promediar")
            self.play(FadeOut(lejos_f), FadeIn(otros, lag_ratio=0.1), run_time=self.dur(0.9))
            self.play(FadeIn(prom), run_time=0.3)

    def ensemble(self):
        L = Lienzo(ancho=10.0, alto=3.2, t_rango=(0, 1), v_max=1.5, centro=(0, -0.5))
        pila = pila_de_curvas(L, 40, semilla=2, a=0.0, puntos=120, color=RUIDO, opacidad=0.35, ancho=1.6, escala=0.6)
        una = L.curva(np.linspace(0, 1, 120), 0.6 * serie(2000, 120, 0.0), AMBAR, 3.5)
        f = formula(r"S_{xx}", "=", r"\mathrm{promedio\ sobre\ el\ ensemble}", escala=0.9,
                    colores={0: AMBAR}).move_to([0, 3.2, 0])
        est = formula(r"\mathrm{promedio}", r"\leftarrow", r"1\ \mathrm{muestra}", "?", escala=0.9,
                      colores={3: ROJO}).move_to([0, -2.9, 0])
        raro = sello("lo raro sería que saliera bien", ROJO).move_to([0, 1.9, 0])
        with self.narrar("b2"):
            self.en("otra")
            self.corte()
            self.play(Create(L.base()), run_time=0.3)
            self.en("ensemble")
            self.play(LaggedStart(*[FadeIn(f[i]) for i in range(3)], lag_ratio=0.5), run_time=self.dur(1.4))
            self.en("mil")
            self.play(FadeIn(pila, lag_ratio=0.03), run_time=self.dur(1.6))
            self.en("una")
            self.play(pila.animate.set_stroke(opacity=0.1), Create(una), run_time=self.dur(0.8))
            self.en("estimar")
            self.play(LaggedStart(*[FadeIn(est[i]) for i in range(4)], lag_ratio=0.35), run_time=self.dur(1.4))
            self.en("raro")
            self.pop(raro)

    def que_promediar(self):
        L = Lienzo(ancho=10.0, alto=1.4, t_rango=(0, 10), v_max=2.6, centro=(0, 1.2))
        t = np.linspace(0, 10, 400)
        P = Lienzo(ancho=3.0, alto=1.3, t_rango=(0, 1), v_max=4.0, centro=(-4.0, 3.4))
        pilas = VGroup(*[bosque_f(P, periodograma_blanco(60 + i, 70), MEDIDA, 1.6, 0.45) for i in range(5)])
        prom = bosque_f(P, periodograma_blanco(77, 70, 25), ESTIMACION, 3.5)
        traza_l = L.curva(t, 0.8 * serie(5, 400, 0.0), RUIDO, 2.6)
        uno = Lienzo(ancho=3.0, alto=1.3, t_rango=(0, 1), v_max=4.0, centro=(0, -1.5))
        un_pg = bosque_f(uno, periodograma_blanco(8, 70), MEDIDA, 2.2)
        pr = MathTex("?", color=AMBAR).scale(3.0).move_to([4.5, -1.3, 0])
        with self.narrar("b3"):
            self.en("muchas")
            self.corte()
            self.play(FadeIn(pilas, lag_ratio=0.15), run_time=self.dur(0.8))
            self.play(ReplacementTransform(pilas, prom), run_time=self.dur(0.8))
            self.en("una_grab")
            self.play(FadeOut(prom), Create(L.base()), Create(traza_l), run_time=self.dur(0.9))
            self.en("uno_por")
            self.play(Create(uno.base()), Create(un_pg), run_time=self.dur(0.8))
            self.en("pregunta")
            self.pop(pr)
