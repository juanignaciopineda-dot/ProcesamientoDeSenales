"""Escena 04 — La convolución con números (promediador, entrada 2, 4, 6) y su fórmula."""
from comun.escena import *


class Convolucion(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.parte_numeros()
        self.parte_formula()

    # ------------------------------------------------------------------ b1
    def parte_numeros(self):
        xc = -3.4
        ent = Tallos([2, 4, 6], centro=(xc, 1.0), paso=1.6, unidad=0.38, color=SENAL, extra=0.3)
        sal = Tallos([1, 3, 5], centro=(xc, -2.9), paso=1.6, unidad=0.38, color=MEDIDA, extra=0.3)
        rot_e = VGroup(*[MathTex(str(v), color=SENAL).scale(1.0).move_to([ent.x(i), 1.0 + v * 0.38 + 0.35, 0])
                         for i, v in enumerate([2, 4, 6])])
        rot_s = VGroup(*[MathTex(str(v), color=MEDIDA).scale(1.0).move_to([sal.x(i), -2.9 + v * 0.38 + 0.35, 0])
                         for i, v in enumerate([1, 3, 5])])
        lab_e = etiqueta("entrada", SENAL, 0.65).move_to([-5.9, 2.9, 0])
        lab_s = etiqueta("salida", MEDIDA, 0.65).move_to([-5.9, -3.6, 0])
        slots = VGroup(*[Circle(radius=0.12, color=INK, stroke_width=2).move_to([sal.x(i), -2.9, 0]) for i in range(3)])

        # h dada la vuelta: «h[0]» sobre la columna k y «h[1]» sobre la k−1
        hv = Tallos([0.5, 0.5], centro=(0, -0.55), paso=1.6, unidad=2.6, color=ESTIMACION)
        hv.shift(RIGHT * (ent.x(-0.5) - hv.cx))
        c1 = formula(r"\tfrac12\cdot 2", "=", "1", escala=1.2).move_to([3.7, 2.0, 0])
        c2 = formula(r"\tfrac12\cdot 4", "+", r"\tfrac12\cdot 2", "=", "3", escala=1.2).move_to([3.7, 0.6, 0])
        c3 = formula(r"\tfrac12\cdot 6", "+", r"\tfrac12\cdot 4", "=", "5", escala=1.2).move_to([3.7, -0.8, 0])
        marco = SurroundingRectangle(VGroup(sal, rot_s), color=AMBAR, buff=0.2, stroke_width=3)
        conv = self.palabra("convolución", AMBAR, 1.3).move_to([3.7, -2.9, 0])

        with self.narrar("b1"):
            # «Entra la secuencia»
            self.en("entrada")
            self.play(FadeIn(ent), FadeIn(lab_e), run_time=self.dur(0.5))

            # «dos, cuatro, seis»
            self.en("dos_cuatro")
            self.play(LaggedStart(*[FadeIn(r, scale=0.6) for r in rot_e], lag_ratio=0.3), run_time=self.dur(0.9))

            # «La primera salida»
            self.en("primera")
            self.play(Create(sal.base), FadeIn(slots), FadeIn(lab_s), FadeIn(hv), run_time=self.dur(0.6))

            # «un medio por dos»
            self.en("c1")
            self.play(FadeIn(c1[0]), run_time=0.4)

            # «uno, porque antes no había nada»
            self.en("r1")
            self.play(FadeIn(c1[1:]), FadeIn(sal.tallos[0]), FadeIn(sal.puntos[0]), FadeIn(rot_s[0]), run_time=self.dur(0.5))

            # «La segunda»
            self.en("segunda")
            self.play(hv.animate.shift(RIGHT * 1.6), run_time=self.dur(0.6))

            # «un medio por cuatro»
            self.en("c2a")
            self.play(FadeIn(c2[0]), run_time=0.4)

            # «un medio por dos»
            self.en("c2b")
            self.play(FadeIn(c2[1:3]), run_time=0.4)

            # «tres»
            self.en("r2")
            self.play(FadeIn(c2[3:]), FadeIn(sal.tallos[1]), FadeIn(sal.puntos[1]), FadeIn(rot_s[1]), run_time=self.dur(0.5))

            # «un medio por seis»
            self.en("c3a")
            self.play(hv.animate.shift(RIGHT * 1.6), FadeIn(c3[0]), run_time=self.dur(0.5))

            # «un medio por cuatro»
            self.en("c3b")
            self.play(FadeIn(c3[1:3]), run_time=0.4)

            # «cinco»
            self.en("r3")
            self.play(FadeIn(c3[3:]), FadeIn(sal.tallos[2]), FadeIn(sal.puntos[2]), FadeIn(rot_s[2]), run_time=self.dur(0.5))

            # «Cada salida»
            self.en("cada")
            self.play(Create(marco), run_time=self.dur(0.5))

            # «entradas recientes»
            self.en("recientes")
            self.play(ent.animate.set_color(AMBAR), run_time=self.dur(0.4))

            # «pesada por un valor de hache»
            self.en("pesada")
            self.play(hv.animate.set_color(AMBAR), run_time=self.dur(0.4))

            # «un valor de hache»
            self.en("valor_h")
            self.resaltar(hv, color=AMBAR, escala=1.15)

            # «la convolución»
            self.en("conv")
            self.pop(conv)
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def parte_formula(self):
        f = formula(r"y[n]", "=", r"\sum_k", r"h[k]", r"x[n-k]", escala=1.7).move_to([0, 2.6, 0])
        hace = etiqueta("hace k pasos", INK, 0.7).next_to(f[4], DOWN, buff=0.9)
        flecha_k = Arrow(hace.get_left() + LEFT * 0.05, f[3].get_bottom() + DOWN * 0.08, color=AMBAR, buff=0.05, stroke_width=3)
        k1 = MathTex(r"k=1 \;\to\; h[1]=\tfrac12", color=TXT).scale(1.1).move_to([0, 0.6, 0])
        pal = Tallos([0.9, 0.7, 0.5, 0.35, 0.22, 0.12, 0.06], centro=(-3.6, -1.6), paso=0.6, unidad=1.6, color=ESTIMACION)
        t = np.linspace(0, 1, 100)
        curva = traza(-3.6 - 1.8 + 3.6 * t, -1.6 + 1.6 * 0.9 * np.exp(-3.4 * t), ESTIMACION, 4)
        g = formula(r"y(t)", "=", r"\int", r"h(v)", r"x(t-v)\,dv", escala=1.7).move_to([0, -2.8, 0])
        sigma_a_int = MathTex(r"\sum \;\to\; \int", color=AMBAR).scale(1.4).move_to([3.6, -0.6, 0])

        with self.narrar("b2"):
            # «la salida en ene»
            self.en("y_n")
            self.corte()
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.5))

            # «la suma, para cada ka»
            self.en("suma")
            self.play(FadeIn(f[2]), run_time=self.dur(0.4))

            # «hache de ka»
            self.en("h_k")
            self.play(FadeIn(f[3]), run_time=self.dur(0.4))

            # «la entrada en ene menos ka»
            self.en("x_nk")
            self.play(FadeIn(f[4]), run_time=self.dur(0.4))

            # «La entrada de hace»
            self.en("entrada_hace")
            self.play(FadeIn(hace), Create(flecha_k), run_time=self.dur(0.5))

            # «pasos»
            self.en("pasos")
            self.play(FadeIn(k1), run_time=self.dur(0.5))

            # «En tiempo continuo»
            self.en("cont")
            self.play(FadeOut(hace), FadeOut(flecha_k), FadeOut(k1), FadeIn(pal), run_time=self.dur(0.5))
            self.play(ReplacementTransform(pal, curva), run_time=self.dur(1.6))

            # «una integral»
            self.en("integral")
            self.play(FadeIn(sigma_a_int, scale=0.8), run_time=self.dur(0.5))

            # «i griega de te»
            self.en("y_t0")
            self.play(FadeIn(g[0]), FadeIn(g[1]), run_time=self.dur(0.4))

            # «hache de uve»
            self.en("y_t1")
            self.play(FadeIn(g[2]), FadeIn(g[3]), run_time=self.dur(0.4))

            # «equis de te menos uve»
            self.en("x_tv")
            self.play(FadeIn(g[4]), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
