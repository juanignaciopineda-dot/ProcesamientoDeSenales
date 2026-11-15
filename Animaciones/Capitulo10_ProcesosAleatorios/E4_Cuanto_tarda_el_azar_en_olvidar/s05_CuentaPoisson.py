"""Escena 05 — CuentaPoisson: P(0), P(1), P(2) con λT = 0,5, hechas a mano."""
from comun.escena import *


def poisson(k: int, m: float) -> float:
    return float(np.exp(-m) * m ** k / np.prod(range(1, k + 1))) if k else float(np.exp(-m))


class CuentaPoisson(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        self.B = BarrasK([poisson(k, 0.5) for k in range(6)], ancho=6.0, alto=3.0, v_max=0.7, centro=(3.4, -1.3))
        B = self.B
        f_base = formula(r"P(k)=\frac{(\lambda T)^k\,e^{-\lambda T}}{k!}", r"\qquad \lambda T = 0{,}5",
                         colores={1: AMBAR}, escala=0.85).move_to([-2.7, 3.15, 0])
        l0 = formula(r"P(0)=e^{-0{,}5}", r"=0{,}61", colores={1: AMBAR}, escala=0.95).move_to([-3.4, 1.55, 0])
        l1 = formula(r"P(1)=0{,}5\cdot 0{,}61", r"=0{,}30", colores={1: AMBAR}, escala=0.95).move_to([-3.4, 0.45, 0])
        l2 = formula("P(2)=", r"\frac{0{,}5^2}{2}", r"\cdot 0{,}61", r"=0{,}08", colores={3: AMBAR},
                     escala=0.95).move_to([-3.4, -0.75, 0])
        for l in (l0, l1, l2):
            l.align_to([-6.6, 0, 0], LEFT)
        rot = lambda k, txt: etiqueta(txt, AMBAR, 0.6, BOLD).next_to(B.pos(k), UP, buff=0.08)
        r0, r1, r2 = rot(0, "0,61"), rot(1, "0,30"), rot(2, "0,08")
        r3 = etiqueta("0,01", AMBAR, 0.5, BOLD).next_to(B.pos(3), UP, buff=0.08)
        uno_pc = etiqueta("≈ 1 % entre 3 o más", INK, 0.5).move_to([4.6, 1.2, 0])
        suma = MathTex(r"\Sigma = 1", color=VERDE).scale(1.3).move_to([-3.4, -2.2, 0])
        ok = tilde(VERDE, 0.5).next_to(suma, RIGHT, buff=0.3)

        with self.narrar("b1"):
            # «Hagamos la cuenta»
            self.en("cuenta")
            self.play(Write(f_base), Create(B.base), FadeIn(B.ks), run_time=self.dur(1.2))

            # «Cero cambios»
            self.en("p0")
            self.play(Write(l0[0]), B.crecer(0), run_time=self.dur(0.9))

            # «cero coma seis uno»
            self.en("v61")
            self.play(Write(l0[1]), FadeIn(r0), run_time=self.dur(0.6))

            # «Un cambio»
            self.en("p1")
            self.play(Write(l1[0]), B.crecer(1), run_time=self.dur(0.9))

            # «cero coma tres cero»
            self.en("v30")
            self.play(Write(l1[1]), FadeIn(r1), run_time=self.dur(0.6))

            # «Dos cambios»
            self.en("p2")
            self.play(Write(l2[0]), B.crecer(2), run_time=self.dur(0.7))

            # «cero coma cinco al cuadrado»
            self.en("cuad")
            self.play(Write(l2[1]), run_time=self.dur(0.9))

            # «cero coma cero ocho»
            self.en("v08")
            self.play(Write(l2[2]), run_time=self.dur(1.0))
            self.play(Write(l2[3]), FadeIn(r2), run_time=self.dur(0.6))

            # «Tres o más»
            self.en("p3")
            self.play(*[B.crecer(k) for k in (3, 4, 5)], FadeIn(r3), run_time=self.dur(0.7))

            # «uno por ciento»
            self.en("uno_pc")
            self.play(FadeIn(uno_pc), run_time=0.4)

            # «suma uno»
            self.en("suma")
            self.pop(suma)
            self.play(FadeIn(ok, scale=0.5), run_time=0.3)
        self.B_rots = (r0, r1, r2, r3, uno_pc)
        self.izq = VGroup(f_base, l0, l1, l2, suma, ok)

    def parte_b2(self):
        B = self.B
        B2 = BarrasK([poisson(k, 2.0) for k in range(6)], ancho=6.0, alto=3.0, v_max=0.7, centro=(3.4, -1.3), color=RUIDO)
        f_aut = MathTex(r"R_{XX}(\tau)", color=AMBAR).scale(1.5).move_to([-3.6, 1.6, 0])
        Lw = Lienzo(ancho=6.0, alto=1.3, t_rango=(0, 6), v_max=1.3, centro=(-3.4, -1.0))
        onda = onda_tel(Lw, CAMBIOS, 1, SENAL, 3.5)
        copia = onda_tel(Lw, [t + 0.5 for t in CAMBIOS], 1, AMBAR, 3.0)
        flecha_d = DoubleArrow(Lw.p(1.0, -1.45), Lw.p(1.5, -1.45), color=AMBAR, buff=0, stroke_width=4,
                               max_tip_length_to_length_ratio=0.3)
        t_05 = etiqueta("0,5 s", AMBAR, 0.5).next_to(flecha_d, DOWN, buff=0.05)
        l_mas = etiqueta("n.º de cambios más probable", RUIDO, 0.5).move_to([3.4, 2.2, 0])

        with self.narrar("b2"):
            self.play(FadeOut(self.izq), FadeOut(VGroup(*self.B_rots)), run_time=0.4)
            # «lo más probable»
            self.en("probable")
            self.resaltar(B.barras[0], color=AMBAR, escala=1.1)

            # «dos o más son raros»
            self.en("raros")
            self.resaltar(*B.barras[2:4], color=ROJO, escala=1.2)

            # «intervalo es más largo»
            self.en("largo")
            self.play(Transform(VGroup(*B.barras), VGroup(*B2.barras)), run_time=self.dur(1.4))

            # «muchos cambios»
            self.en("muchos")
            self.play(FadeIn(l_mas), run_time=0.4)
            self.resaltar(B.barras[1], B.barras[2], color=AMBAR, escala=1.1)

            # «la autocorrelación de la onda»
            self.en("autocorr")
            self.pop(f_aut)

            # «cuánto se parece la señal»
            self.en("parece")
            self.play(Create(Lw.base()), Create(onda), run_time=self.dur(0.9))
            self.play(Create(copia), run_time=self.dur(0.9))

            # «medio segundo después»
            self.en("despues")
            self.play(Create(flecha_d), FadeIn(t_05), run_time=self.dur(0.6))
