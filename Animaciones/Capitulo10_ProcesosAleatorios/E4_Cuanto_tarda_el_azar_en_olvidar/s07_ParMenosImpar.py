"""Escena 07 — ParMenosImpar: R = P(par) − P(impar) = 0,368 a medio segundo, y la serie de e^(−λτ)."""
from comun.escena import *
from comun.figuras import BarrasK


def poisson(k: int, m: float) -> float:
    return float(np.exp(-m) * m ** k / np.prod(range(1, k + 1))) if k else float(np.exp(-m))


class ParMenosImpar(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        B = BarrasK([poisson(k, 0.5) for k in range(6)], ancho=6.6, alto=2.6, v_max=0.7, centro=(0, -0.6), color=INK)
        f = formula(r"R=E[x(t)\,x(t+\tau)]=", r"(+1)\cdot P(\text{par})", r"+\,(-1)\cdot P(\text{impar})",
                    colores={1: VERDE, 2: ROJO}, escala=1.05).move_to([0, 3.15, 0])
        t_m = MathTex(r"\tau = 0{,}5", color=AMBAR).scale(1.0).move_to([-5.3, 0.3, 0])
        r_p = etiqueta("0,684", VERDE, 0.7, BOLD).move_to([-2.6, 2.25, 0])
        r_i = etiqueta("0,316", ROJO, 0.7, BOLD).move_to([2.6, 2.25, 0])
        r_a = MathTex(r"R_{XX}(0{,}5)=", color=AMBAR).scale(1.0).move_to([-4.0, -3.0, 0])
        dif = MathTex(r"0{,}684", r"-", r"0{,}316").scale(1.0)
        dif[0].set_color(VERDE)
        dif[2].set_color(ROJO)
        dif.next_to(r_a, RIGHT, buff=0.25)
        res = MathTex(r"=\,0{,}368", color=AMBAR).scale(1.3).next_to(dif, RIGHT, buff=0.3)

        with self.narrar("b1"):
            # «la esperanza del producto»
            self.en("esperanza")
            self.play(Write(f[0]), run_time=self.dur(1.0))

            # «probabilidad de un número par»
            self.en("p_par")
            self.play(Write(f[1]), run_time=self.dur(1.2))

            # «probabilidad de un número impar»
            self.en("p_impar")
            self.play(Write(f[2]), run_time=self.dur(1.4))

            # «A medio segundo»
            self.en("medio")
            self.pop(t_m)
            self.play(Create(B.base), FadeIn(B.ks), *[GrowFromEdge(b, DOWN) for b in B.barras], run_time=self.dur(0.9))

            # «los casos pares»
            self.en("pares")
            self.play(*[B.barras[k].animate.set_color(VERDE) for k in (0, 2, 4)], run_time=0.4)

            # «cero coma seis ocho cuatro»
            self.en("v684")
            self.pop(r_p)

            # «cero coma tres uno seis»
            self.en("v316")
            self.play(*[B.barras[k].animate.set_color(ROJO) for k in (1, 3, 5)], run_time=0.4)
            self.pop(r_i)

            # «La autocorrelación a medio segundo»
            self.en("autoc")
            self.pop(r_a)

            # «es la diferencia»
            self.en("dif")
            self.play(Write(dif), run_time=self.dur(0.9))

            # «cero coma tres seis ocho»
            self.en("v368")
            self.pop(res)
        self.b1 = VGroup(f, B, t_m, r_p, r_i, r_a, dif, res)

    def parte_b2(self):
        A = formula(r"R(\tau)=", r"\sum_k(-1)^k", r"\frac{(\lambda\tau)^k}{k!}", r"e^{-\lambda\tau}",
                    colores={1: ROJO, 2: AZUL, 3: RUIDO}, escala=1.25).move_to([0, 2.7, 0])
        br = Brace(VGroup(A[1], A[2]), DOWN, color=AMBAR)
        t_sa = etiqueta("suma alternada", AMBAR, 0.55).next_to(br, DOWN, buff=0.1)
        t_con = etiqueta("serie conocida", INK, 0.55).next_to(t_sa, DOWN, buff=0.15)
        S = MathTex(r"e^{-x}=\sum_k\frac{(-x)^k}{k!}", color=TXT).scale(1.15).move_to([0, -0.3, 0])
        C = formula("R(\\tau)=", r"e^{-\lambda\tau}", r"\cdot", r"e^{-\lambda\tau}",
                    colores={1: AMBAR, 3: RUIDO}, escala=1.3).move_to([0, -1.5, 0])
        fin = formula(r"R_{XX}(\tau)=", r"e^{-2\lambda|\tau|}", colores={1: AMBAR}, escala=1.6).move_to([0, -2.85, 0])
        cuadro = SurroundingRectangle(fin, color=AMBAR, buff=0.2, stroke_width=4)

        with self.narrar("b2"):
            self.play(FadeOut(self.b1), run_time=0.2)
            # «un tau cualquiera»
            self.en("tau")
            self.play(Write(A[0]), run_time=self.dur(0.9))

            # «términos de Poisson»
            self.en("terminos")
            self.play(Write(A[2]), Write(A[3]), run_time=self.dur(1.0))

            # «signos alternados»
            self.en("alternados")
            self.play(Write(A[1]), run_time=self.dur(1.0))
            self.play(Indicate(A[1], color=ROJO, scale_factor=1.1), run_time=self.dur(3.0))

            # «Esa suma alternada»
            self.en("suma_alt")
            self.play(Create(br), FadeIn(t_sa), run_time=self.dur(0.7))

            # «una serie conocida»
            self.en("conocida")
            self.play(FadeIn(t_con), run_time=0.4)

            # «la de la exponencial»
            self.en("serie")
            self.play(Write(S), run_time=self.dur(1.4))

            # «da e elevado a menos lambda tau»
            self.en("da")
            self.play(Write(C[0]), Write(C[1]), run_time=self.dur(1.0))

            # «Multiplicada por»
            self.en("mult")
            self.play(Write(C[2]), run_time=self.dur(0.5))

            # «que ya llevaba cada término»
            self.en("llevaba")
            self.play(Write(C[3]), run_time=self.dur(0.8))
            self.play(Indicate(A[3], color=AMBAR, scale_factor=1.2), run_time=self.dur(1.0))

            # «menos dos lambda por el valor absoluto de tau»
            self.en("resultado")
            self.play(Write(fin), run_time=self.dur(1.0))
            self.play(Create(cuadro), run_time=0.4)
