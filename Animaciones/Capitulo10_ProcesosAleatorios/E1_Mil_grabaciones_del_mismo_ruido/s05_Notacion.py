"""Escena 05 — Notación: X(t) en tiempo continuo, X[n] en tiempo discreto."""
from comun.escena import *


class Notacion(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        with self.narrar("b1"):
            # «equis mayúscula de te»
            self.en("xt")
            fx = formula("X", "(", "t", ")", colores={0: AMBAR}, escala=1.6).move_to([-3.6, 2.6, 0])
            self.pop(fx)

            # «el tiempo es continuo»
            self.en("cont")
            L = Lienzo(ancho=5.8, alto=2.4, t_rango=(0, 1), v_max=2.0, centro=(-3.6, -0.3))
            t = np.linspace(0, 1, 200)
            cont = L.curva(t, np.sin(2 * np.pi * 1.6 * t) * 0.8 + 0.35 * np.sin(2 * np.pi * 4.3 * t + 1), SENAL, 3.5)
            base_c = L.base()
            self.play(Create(base_c), Create(cont), run_time=self.dur(1.3), rate_func=linear)

            # «equis mayúscula de ene»
            self.en("xn")
            fn = formula("X", "[", "n", "]", colores={0: AMBAR}, escala=1.6).move_to([3.6, 2.6, 0])
            self.pop(fn)

            # «una muestra en cada instante entero»
            self.en("muestras")
            R = Lienzo(ancho=5.8, alto=2.4, t_rango=(0, 1), v_max=2.0, centro=(3.6, -0.3))
            ns = np.arange(0, 12)
            tn = ns / 11
            vn = np.sin(2 * np.pi * 1.6 * tn) * 0.8 + 0.35 * np.sin(2 * np.pi * 4.3 * tn + 1)
            base_n = R.base()
            palitos = VGroup(*[Line(R.p(a, 0), R.p(a, v), color=SENAL, stroke_width=3) for a, v in zip(tn, vn)])
            bolas = VGroup(*[Dot(R.p(a, v), radius=0.09, color=SENAL) for a, v in zip(tn, vn)])
            self.play(Create(base_n), run_time=0.3)
            self.play(LaggedStart(*[AnimationGroup(Create(p), FadeIn(b, scale=0.4)) for p, b in zip(palitos, bolas)],
                                  lag_ratio=0.12), run_time=self.dur(1.8))

            # «La mayúscula recuerda»
            self.en("mayus")
            self.play(fx[0].animate.scale(1.35), fn[0].animate.scale(1.35), run_time=self.dur(0.4))
            self.play(fx[0].animate.scale(1 / 1.35), fn[0].animate.scale(1 / 1.35), run_time=0.3)

            # «todavía no ha salido nada»
            self.en("nada")
            aun = etiqueta("aún sin resultado", INK, 0.6).move_to([0, -2.9, 0])
            self.play(FadeIn(aun, shift=UP * 0.15), run_time=0.5)

            # «con algo concreto»
            self.en("concreto")
            self.play(*[FadeOut(m) for m in (cont, palitos, bolas, base_n, base_c)], FadeOut(aun), run_time=0.4)

            # «una nave llena de osciladores»
            self.en("nave")
            gens = VGroup(*[generador(1.0, 1.0 + 0.4 * k, 0.6 * k, 1.5, 1.0) for k in range(5)])
            gens.arrange(RIGHT, buff=0.35).move_to([0, -1.2, 0])
            self.play(LaggedStart(*[FadeIn(g, shift=LEFT * 0.4) for g in gens], lag_ratio=0.15), run_time=self.dur(1.3))
        self.wait(1.0)
        self.limpiar()
