"""Escena 04 — Poisson: cuántos cambios caben en un intervalo y la fórmula."""
from comun.escena import *


class Poisson(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        L = Lienzo(ancho=9.6, alto=1.6, t_rango=(0, 6), v_max=1.3, centro=(0, 2.1))
        base = L.base()
        marcas = marcas_cambio(L, CAMBIOS, AMBAR, 0.25)
        onda = onda_tel(L, CAMBIOS, 1, SENAL, 3.5)
        ancho_v = float(L.x(0.5) - L.x(0))
        vent = Rectangle(width=ancho_v, height=1.5, color=VERDE, stroke_width=3).set_fill(VERDE, 0.15)
        vent.move_to([float(L.x(0.75)), 2.1, 0])
        f_lam = formula(r"\lambda", "=", "1", colores={0: AMBAR}, escala=1.4).move_to([-4.3, 0.2, 0])
        f_lt = formula(r"\lambda T", "=", r"0{,}5", colores={0: AMBAR}, escala=1.4).move_to([3.6, 0.2, 0])
        cps = etiqueta("cambio por segundo", INK, 0.5).next_to(f_lam, DOWN, buff=0.2)
        t_m = etiqueta("0,5 s", VERDE, 0.5).next_to(vent, DOWN, buff=0.05)
        cajas = VGroup(*[caja(str(k), AZUL, ancho=1.1, alto=0.9, scale=0.7) for k in (0, 1, 2)]).arrange(RIGHT, buff=0.5)
        cajas.move_to([0, -2.5, 0])
        q = MathTex(r"P(k)\ ?", color=AMBAR).scale(1.2).next_to(cajas, UP, buff=0.3)

        with self.narrar("b1"):
            # «cuántos cambios caben»
            self.en("cuantos")
            self.play(Create(base), Create(onda), FadeIn(marcas), run_time=self.dur(1.2))
            self.play(FadeIn(vent), run_time=0.4)

            # «lambda al ritmo medio»
            self.en("lambda")
            self.pop(f_lam)

            # «un cambio por segundo»
            self.en("uno_s")
            self.play(FadeIn(cps), run_time=0.4)
            self.resaltar(f_lam, color=AMBAR, escala=1.1)

            # «medio segundo»
            self.en("medio")
            self.play(FadeIn(t_m), run_time=0.4)

            # «lambda por te»
            self.en("lt")
            self.pop(f_lt)

            # «cero cambios»
            self.en("cero")
            self.play(vent.animate.move_to([float(L.x(5.75)), 2.1, 0]), FadeOut(t_m),
                      run_time=self.dur(3.4), rate_func=linear)

            # «¿Con qué probabilidad cada cosa?»
            self.en("pregunta")
            self.play(FadeIn(cajas), run_time=0.4)
            self.pop(q)

    def parte_b2(self):
        tit = self.palabra("distribución de Poisson", AMBAR, 0.95).move_to([0, 3.2, 0])
        f = formula("P(k)", "=", r"(\lambda T)^k", r"e^{-\lambda T}", "/", "k!",
                    colores={2: AMBAR, 3: RUIDO, 5: AZUL}, escala=1.9).move_to([0, 1.3, 0])
        rng = np.random.default_rng(4)
        linea = Line([-5.5, -0.4, 0], [5.5, -0.4, 0], color=INK, stroke_width=2)
        puntos = VGroup(*[Dot([x, -0.4, 0], radius=0.1, color=AMBAR) for x in np.sort(rng.uniform(-5.4, 5.4, 11))])
        nota_e = MathTex(r"e \approx 2{,}718", color=RUIDO).scale(1.0).move_to([-3.3, -1.5, 0])
        f_fact = MathTex(r"k! = 1\cdot 2\cdot 3\cdots k", color=AZUL).scale(0.95).move_to([-2.6, -2.4, 0])
        f2 = MathTex(r"2! = 2", color=AZUL).scale(0.95).move_to([2.8, -2.0, 0])
        f3 = MathTex(r"3! = 6", color=AZUL).scale(0.95).move_to([2.8, -2.9, 0])

        with self.narrar("b2"):
            self.corte()
            # «distribución de Poisson»
            self.en("poisson")
            self.pop(tit)

            # «sucesos que llegan al azar»
            self.en("sucesos")
            self.play(Create(linea), LaggedStart(*[FadeIn(p, shift=DOWN * 0.4) for p in puntos], lag_ratio=0.15),
                      run_time=self.dur(3.0))

            # «ver ka cambios»
            self.en("p_k")
            self.play(FadeOut(linea), FadeOut(puntos), run_time=0.3)
            self.play(Write(f[0]), Write(f[1]), run_time=self.dur(0.8))

            # «lambda te elevado a ka»
            self.en("num")
            self.play(Write(f[2]), run_time=self.dur(0.8))

            # «e elevado a menos lambda te»
            self.en("exp")
            self.play(Write(f[3]), run_time=self.dur(0.8))

            # «dividido entre ka factorial»
            self.en("fact")
            self.play(Write(f[4]), Write(f[5]), run_time=self.dur(0.8))

            # «dos coma siete uno ocho»
            self.en("e")
            self.pop(nota_e)

            # «uno por dos por tres»
            self.en("fact_ej")
            self.play(Write(f_fact), run_time=self.dur(1.2))

            # «el factorial de dos»
            self.en("f2")
            self.pop(f2)

            # «el de tres, seis»
            self.en("f3")
            self.pop(f3)
