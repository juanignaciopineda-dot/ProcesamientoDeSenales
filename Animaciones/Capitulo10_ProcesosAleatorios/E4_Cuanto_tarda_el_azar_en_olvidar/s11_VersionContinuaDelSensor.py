"""Escena 11 — VersionContinuaDelSensor: el sensor es la versión discreta de la exponencial; y la pregunta de la grabación única."""
from comun.escena import *


class VersionContinuaDelSensor(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        ks = list(range(7))
        centro = (-1.0, -0.4)
        Lm = Lienzo(ancho=8.0, alto=2.6, t_rango=(-0.5, 6.5), v_max=1.1, centro=centro)
        pal = Palitos(ks, [0.6 ** k for k in ks], ancho=8.0, alto=2.6, v_max=1.1, color=AMBAR, centro=centro,
                      rotulo="pasos")
        t = np.linspace(-0.5, 6.5, 200)
        curva = Lm.curva(t, np.exp(-0.5108 * t), SENAL, 5)
        term = termometro().scale(0.9).move_to([-6.0, 2.3, 0])
        x06 = MathTex(r"\times\,0{,}6\ \text{por paso}", color=AMBAR).scale(1.0).move_to([-2.8, 2.6, 0])
        pasos = VGroup(*[etiqueta("× 0,6", AMBAR, 0.42).move_to(Lm.p(k + 0.5, 0.6 ** k * 0.92 + 0.22)) for k in (0, 1, 2)])
        mismo_t = etiqueta("mismo tiempo, mismo factor", INK, 0.5).move_to([-1.0, -2.85, 0])
        f2l = MathTex(r"2\lambda", color=AMBAR).scale(1.5).move_to([4.6, 2.3, 0])
        ancho = nota("2λ → capítulo 11: ancho de banda", 0.5).move_to([4.2, 1.35, 0])
        Lo = Lienzo(ancho=3.4, alto=1.6, t_rango=(0, 2), v_max=1.2, centro=(4.6, -0.1))
        tt = np.linspace(0, 2, 120)
        osc = Lo.curva(tt, np.cos(2 * np.pi * tt), VERDE, 4)
        t_osc = etiqueta("osciladores: no se apaga", VERDE, 0.5).move_to([4.6, -1.35, 0])
        base_m, base_o = Lm.base(), Lo.base()
        self.b1 = VGroup(pal, curva, term, x06, pasos, mismo_t, f2l, ancho, osc, t_osc, base_m, base_o)

        with self.narrar("b1"):
            # «la versión continua»
            self.en("continua")
            self.play(Create(base_m), Create(curva), run_time=self.dur(1.0))

            # «sensor de temperatura»
            self.en("sensor")
            self.pop(term)

            # «la correlación se multiplicaba»
            self.en("correl")
            self.play(Create(pal.base), LaggedStart(*[Create(s) for s in pal.tallos], lag_ratio=0.2),
                      FadeIn(VGroup(*pal.puntos)), run_time=self.dur(1.6))

            # «cero coma seis en cada paso»
            self.en("x06")
            self.pop(x06)

            # «un mismo factor»
            self.en("factor")
            self.play(LaggedStart(*[FadeIn(p) for p in pasos], lag_ratio=0.3), run_time=self.dur(1.6))

            # «un mismo tiempo»
            self.en("tiempo")
            self.play(FadeIn(mismo_t), run_time=0.4)

            # «Las dos son memorias»
            self.en("dos_mem")
            self.resaltar(curva, color=AMBAR, escala=1.02)

            # «se borran poco a poco»
            self.en("borran")
            self.play(curva.animate.set_stroke(opacity=0.5), run_time=self.dur(1.6))

            # «los osciladores»
            self.en("osc")
            self.play(Create(base_o), Create(osc), FadeIn(t_osc), run_time=self.dur(1.2))

            # «ese dos lambda»
            self.en("dos_lambda")
            self.pop(f2l)

            # «ancho de banda»
            self.en("ancho")
            self.play(FadeIn(ancho), run_time=0.5)

    def parte_b2(self):
        L = Lienzo(ancho=9.6, alto=3.0, t_rango=(0, 6), v_max=2.0, centro=(0, 1.2))
        pila = pila_de_curvas(L, 14, semilla=5, a=0.93, puntos=180, opacidad=0.5, ancho=2.4, escala=0.6)
        corte = L.vertical(3.0, AMBAR, 3.5, 1.5)
        flecha_v = DoubleArrow(L.p(3.0, -1.35) + RIGHT * 0.35, L.p(3.0, 1.35) + RIGHT * 0.35, color=AMBAR, buff=0,
                               stroke_width=4, max_tip_length_to_length_ratio=0.1)
        t_prom = etiqueta("promedio del ensemble", AMBAR, 0.5).move_to([-2.0, 3.35, 0])
        mat = matraz().scale(0.9).move_to([-6.2, -2.5, 0])
        sws = VGroup(*[interruptor().scale(0.32) for _ in range(9)]).arrange(RIGHT, buff=0.12).move_to([-2.6, -2.5, 0])
        ter = VGroup(*[termometro().scale(0.42) for _ in range(6)]).arrange(RIGHT, buff=0.22).move_to([3.4, -2.5, 0])
        lo_que = etiqueta("lo que tienes", AMBAR, 0.6, BOLD).move_to([-2.0, 3.35, 0])
        sol_i = sol().scale(0.9).move_to([6.0, 3.3, 0])
        interrog = MathTex(r"\text{¿basta?}", color=AMBAR).scale(1.5).move_to([4.6, 3.3, 0])

        with self.narrar("b2"):
            self.play(FadeOut(self.b1), run_time=0.2)
            # «promedios sobre el ensemble»
            self.en("ensemble")
            self.play(Create(L.base()), LaggedStart(*[Create(c) for c in pila], lag_ratio=0.08), run_time=self.dur(1.6))

            # «en cada corte»
            self.en("corte")
            self.play(Create(corte), run_time=self.dur(0.6))

            # «a través de todas las realizaciones»
            self.en("traves")
            self.play(Create(flecha_v), FadeIn(t_prom), run_time=self.dur(0.8))

            # «en un laboratorio»
            self.en("lab")
            self.pop(mat)

            # «mil interruptores»
            self.en("mil")
            self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in sws], lag_ratio=0.1), run_time=self.dur(1.0))

            # «mil sensores»
            self.en("sensores")
            self.play(LaggedStart(*[FadeIn(s, scale=0.5) for s in ter], lag_ratio=0.1), run_time=self.dur(1.0))

            # «una grabación»
            self.en("una")
            self.play(*[c.animate.set_stroke(opacity=0.08) for c in pila[1:]],
                      pila[0].animate.set_stroke(opacity=1, width=5),
                      FadeOut(corte), FadeOut(flecha_v), FadeOut(t_prom),
                      FadeOut(sws), FadeOut(ter), FadeOut(mat), run_time=self.dur(1.0))
            self.play(FadeIn(lo_que), run_time=0.4)

            # «una tarde de datos»
            self.en("tarde")
            self.pop(sol_i)

            # «¿basta con eso?»
            self.en("basta")
            self.pop(interrog)
