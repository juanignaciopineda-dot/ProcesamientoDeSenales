"""Escena 15 — El máximo está en τ = 0: la parábola del sensor (Cauchy-Schwarz)."""
from comun.escena import *


def g_sensor(x):
    return 4 - 4.8 * x + 4 * x ** 2


class LaParabola(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        La = Lienzo(ancho=5.4, alto=2.2, t_rango=(-2, 2), v_max=1.0, centro=(-3.6, 1.0))
        tau = np.linspace(-2, 2, 200)
        Lb = Lienzo(ancho=5.4, alto=1.5, t_rango=(0, 1), v_max=2.4, centro=(3.6, 2.2))
        t = np.linspace(0, 1, 200)
        s = 0.9 * serie(61, 200, 0.92)
        pa = ejes([-0.3, 1.3, 0.5], [0, 6, 2], ancho=4.6, alto=2.2, x_label=r"\lambda")
        parabola = pa[0].plot(g_sensor, x_range=[-0.3, 1.3, 0.02], color=ESTIMACION, stroke_width=4)
        grupo_p = VGroup(pa[0], pa[1], parabola).move_to([3.6, -1.6, 0])

        with self.narrar("b1"):
            # «La segunda propiedad»
            self.en("segunda")
            n2 = caja("2", AMBAR, ancho=0.8, alto=0.7).move_to([-4.8, 3.45, 0])
            mx = caja("máximo", AZUL, ancho=2.4, alto=0.7).move_to([-3.0, 3.45, 0])
            self.play(FadeIn(n2), FadeIn(mx), run_time=0.4)

            # «el máximo está en tau igual a cero»
            self.en("maximo")
            base, cur = La.base(), La.curva(tau, np.exp(-1.3 * np.abs(tau)), SENAL, 5)
            d0 = Dot(La.p(0, 1.0), radius=0.12, color=AMBAR)
            eje_v = Line(La.p(0, -0.3), La.p(0, 1.15), color=INK, stroke_width=2)
            tm = MathTex(r"\tau = 0", color=AMBAR).scale(0.8).next_to(La.p(0, 0), DOWN, buff=0.15)
            self.play(Create(base), Create(eje_v), Create(cur), FadeIn(d0, scale=0.5), FadeIn(tm), run_time=self.dur(1.0))

            # «Ninguna muestra se parece tanto»
            self.en("ninguna")
            orig = Lb.curva(t, s, SENAL, 3.5)
            copias = [Lb.curva(t + d, s, RUIDO, 3.0, 0.6) for d in (-0.12, -0.25)]
            self.play(Create(Lb.base()), Create(orig), *[Create(c) for c in copias], run_time=self.dur(1.0))

            # «la propia señal en el mismo instante»
            self.en("propia")
            ex = Lb.curva(t, s, AMBAR, 6)
            self.play(*[FadeOut(c) for c in copias], Create(ex), run_time=self.dur(0.7))
            tl = tilde(VERDE, 0.3).move_to([6.4, 2.2, 0])
            self.play(FadeIn(tl), run_time=0.2)

            # «Lo demostramos»
            self.en("demostramos")
            dem = self.palabra("demostración", AMBAR, 0.7).move_to([3.6, 0.55, 0])
            self.pop(dem)

            # «la parábola del capítulo anterior»
            self.en("parabola")
            self.play(Create(grupo_p[0]), FadeIn(grupo_p[1]), Create(grupo_p[2]), run_time=self.dur(1.0))

            # «Con el sensor centrado»
            self.en("centrado")
            c = MathTex(r"\tilde x[n] = x[n] - 20", color=TXT).scale(0.8).move_to([-3.6, -1.0, 0])
            self.play(FadeIn(c), run_time=0.5)

            # «la muestra de ahora menos lambda veces la siguiente»
            self.en("combina")
            f = formula(r"g(\lambda)", "=", r"E\big[\big(", r"\tilde x[n]-\lambda\,\tilde x[n{+}1]", r"\big)^2\big]",
                        escala=0.8).move_to([-3.4, -2.3, 0])
            self.play(FadeIn(f[3]), run_time=0.5)

            # «eleva al cuadrado»
            self.en("cuadrado")
            self.play(FadeIn(f[0]), FadeIn(f[1]), FadeIn(f[2]), FadeIn(f[4]), run_time=self.dur(0.6))

            # «nunca es negativa»
            self.en("no_neg")
            nn = MathTex(r"\ge 0", color=AMBAR).scale(1.2).move_to([-3.4, -3.3, 0])
            self.pop(nn)

            # «la de un cuadrado»
            self.en("un_cuadrado")
            self.resaltar(f[4], color=AMBAR, escala=1.2)
        self.limpiar()

    def parte_b2(self):
        pa = ejes([-0.3, 1.3, 0.5], [0, 6, 2], ancho=6.2, alto=3.4, x_label=r"\lambda", y_label="g")
        parabola = pa[0].plot(g_sensor, x_range=[-0.3, 1.3, 0.02], color=ESTIMACION, stroke_width=5)
        gp = VGroup(pa[0], pa[1], parabola).move_to([2.9, 0.9, 0])
        ax = pa[0]
        pal = Palitos(range(0, 6), [4, 2.4, 1.44, 0.86, 0.52, 0.31], ancho=4.6, alto=1.3, v_max=4.0, centro=(3.3, -2.8))

        with self.narrar("b2"):
            # «los números del sensor»
            self.en("numeros")
            c0 = MathTex(r"C[0] = 4", color=TXT).scale(0.9).move_to([-5.0, 3.1, 0])
            c1 = MathTex(r"C[1] = 2{,}4", color=TXT).scale(0.9).move_to([-4.7, 2.3, 0])
            self.play(FadeIn(c0), FadeIn(c1), run_time=self.dur(0.7))

            # «cuatro menos cuatro coma ocho lambda»
            self.en("t1")
            f = formula(r"g(\lambda)", "=", "4", r"-4{,}8\,\lambda", r"+4\,\lambda^2", escala=0.95).move_to([-3.7, 1.4, 0])
            self.play(FadeIn(f[0]), FadeIn(f[1]), FadeIn(f[2]), FadeIn(f[3]), run_time=self.dur(0.9))

            # «más cuatro lambda al cuadrado»
            self.en("t2")
            self.play(FadeIn(f[4]), run_time=0.4)

            # «una parábola»
            self.en("parab")
            self.play(Create(ax), FadeIn(pa[1]), Create(parabola), run_time=self.dur(1.2))

            # «nunca baja de cero»
            self.en("sobre_eje")
            cero = Line(ax.c2p(-0.3, 0), ax.c2p(1.3, 0), color=VERDE, stroke_width=5)
            self.play(Create(cero), run_time=self.dur(0.6))

            # «su discriminante no puede ser positivo»
            self.en("disc")
            dsc = MathTex(r"b^2 - 4ac \le 0", color=AMBAR).scale(0.95).move_to([-3.9, 0.3, 0])
            self.pop(dsc)

            # «Cuatro coma ocho al cuadrado»
            self.en("b2")
            b2 = MathTex(r"4{,}8^2 = 23{,}04", color=TXT).scale(0.9).move_to([-4.0, -0.6, 0])
            self.play(FadeIn(b2), run_time=0.5)

            # «menos cuatro por cuatro por cuatro»
            self.en("ac")
            ac = MathTex(r"-\,4\cdot 4\cdot 4 = -64", color=TXT).scale(0.9).move_to([-3.85, -1.45, 0])
            self.play(FadeIn(ac), run_time=0.5)

            # «menos cuarenta coma nueve seis»
            self.en("res")
            res = MathTex(r"= -40{,}96 < 0", color=AMBAR).scale(1.0).move_to([-3.9, -2.3, 0])
            self.pop(res)
            tl = tilde(VERDE, 0.3).next_to(res, RIGHT, buff=0.25)
            self.play(FadeIn(tl), run_time=0.2)

            # «Con letras»
            self.en("letras")
            cl = etiqueta("con letras", INK, 0.55).move_to([-4.6, -3.1, 0])
            self.play(FadeIn(cl), run_time=0.3)

            # «el valor absoluto de la autocovarianza en tau»
            self.en("abs")
            ab = MathTex(r"|C(\tau)|", color=TXT).scale(1.0).move_to([-2.9, -3.1, 0])
            self.play(FadeIn(ab), run_time=0.4)

            # «nunca supera su valor en cero»
            self.en("cota")
            cota = MathTex(r"|C(\tau)| \le C(0)", color=AMBAR).scale(1.0).move_to([-2.0, -3.1, 0])
            self.play(ReplacementTransform(ab, cota), run_time=0.4)
            marco = SurroundingRectangle(cota, color=AMBAR, buff=0.12, stroke_width=4)
            tope = DashedLine(pal.pos(0, 4.0) + LEFT * 0.4, pal.pos(5, 4.0) + RIGHT * 0.4, color=AMBAR, stroke_width=3)
            self.play(Create(marco), FadeIn(pal), Create(tope), run_time=self.dur(0.9))
