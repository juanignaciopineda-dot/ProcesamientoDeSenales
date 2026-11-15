"""Escena 12 — La autocorrelación del oscilador: identidad del producto de cosenos."""
from comun.escena import *


class ProductoDeCosenos(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        L = Lienzo(ancho=8.0, alto=1.8, t_rango=(0, 2), v_max=1.25, centro=(0, 2.5))
        curvas = [coseno(L, k * 45, 1.0, SENAL, 2.4) for k in range(8)]
        c1, c2 = L.vertical(0.3, AMBAR, 3.5, mitad=1.1), L.vertical(0.85, AMBAR, 3.5, mitad=1.1)

        with self.narrar("b1"):
            # «la autocorrelación»
            self.en("autoc")
            self.play(Create(L.base()), *[Create(c) for c in curvas], Create(c1), Create(c2), run_time=self.dur(0.9))
            xx = MathTex(r"X(t)\,X(t+\tau)", color=AMBAR).scale(0.9).move_to([0, 3.75, 0])
            self.play(FadeIn(xx), run_time=0.3)

            # «multiplicar dos cosenos»
            self.en("multiplicar")
            m = MathTex(r"\cos\alpha", r"\cdot", r"\cos\beta", color=TXT).scale(1.2).move_to([0, 0.7, 0])
            self.play(FadeIn(m), run_time=self.dur(0.5))

            # «una identidad del colegio»
            self.en("identidad")
            pal = self.palabra("identidad", AMBAR, 0.8).move_to([5.2, 0.7, 0])
            self.pop(pal)

            # «el producto de dos cosenos»
            self.en("producto")
            f = formula(r"\cos\alpha\,\cos\beta", "=", r"\tfrac{1}{2}\cos(\alpha-\beta)", "+", r"\tfrac{1}{2}\cos(\alpha+\beta)",
                        escala=1.0).move_to([0, -0.6, 0])
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.5))

            # «la mitad del coseno de la diferencia»
            self.en("mitad_dif")
            self.play(FadeIn(f[2], shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «la mitad del coseno de la suma»
            self.en("mitad_suma")
            self.play(FadeIn(f[3]), FadeIn(f[4], shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «los dos ángulos a cero»
            self.en("cero")
            z = MathTex(r"\alpha = \beta = 0", color=AMBAR).scale(1.0).move_to([0, -1.9, 0])
            self.pop(z)

            # «uno por uno es uno»
            self.en("uno_uno")
            u = MathTex(r"1 \cdot 1 = 1", color=TXT).scale(1.0).move_to([-2.4, -3.0, 0])
            self.play(FadeIn(u), run_time=0.4)

            # «un medio más un medio también es uno»
            self.en("medio_medio")
            mm = MathTex(r"\tfrac12 + \tfrac12 = 1", color=TXT).scale(1.0).move_to([2.4, -3.0, 0])
            self.play(FadeIn(mm), run_time=0.4)
            t = tilde(VERDE, 0.4).move_to([4.4, -3.0, 0])
            self.pop(t)
        self.limpiar()

    def parte_b2(self):
        ab = MathTex(r"\alpha = \omega_0 t + \Theta", r",\qquad", r"\beta = \omega_0 (t+\tau) + \Theta", color=INK).scale(0.8)
        ab.move_to([0, 3.35, 0])
        f = formula(r"\tfrac{1}{2}\cos(\alpha-\beta)", "+", r"\tfrac{1}{2}\cos(\alpha+\beta)", escala=1.1).move_to([0, 2.2, 0])
        Lp = Lienzo(ancho=5.0, alto=1.4, t_rango=(0, 2), v_max=1.25, centro=(-2.2, -1.1))
        circ = Circle(radius=0.85, color=INK, stroke_width=3).move_to([4.6, -1.1, 0])
        pts = VGroup(*[Dot(circ.point_at_angle(k * TAU / 16), radius=0.07, color=AMBAR) for k in range(16)])

        with self.narrar("b2"):
            # «El término de la suma»
            self.en("suma")
            self.play(FadeIn(ab), FadeIn(f), run_time=self.dur(0.5))
            self.resaltar(f[2], escala=1.12)

            # «la fase dentro dos veces»
            self.en("dos_veces")
            dv = MathTex(r"\Theta + \Theta = 2\Theta", color=AMBAR).scale(1.0).move_to([3.4, 0.8, 0])
            self.pop(dv)

            # «al promediar sobre todas las fases»
            self.en("promediar")
            self.play(Create(circ), FadeIn(pts), run_time=self.dur(0.7))

            # «vueltas completas»
            self.en("vueltas")
            dc = traza(Lp.x(np.linspace(0, 2, 160)), Lp.y(np.cos(2 * np.pi * 2 * np.linspace(0, 2, 160))), AMBAR, 4)
            self.play(Create(Lp.base()), Create(dc), run_time=self.dur(1.0), rate_func=linear)

            # «da cero»
            self.en("da0")
            tachon = Line(f[2].get_corner(DL) + DL * 0.05, f[2].get_corner(UR) + UR * 0.05, color=ROJO, stroke_width=6)
            cero = MathTex("0", color=ROJO).scale(1.1).next_to(f[2], DOWN, buff=0.15)
            self.play(Create(tachon), FadeIn(cero), run_time=self.dur(0.5))

            # «El de la diferencia»
            self.en("dif")
            self.resaltar(f[0], escala=1.12)

            # «no tiene fase»
            self.en("sin_fase")
            sf = MathTex(r"\Theta", "-", r"\Theta", "=0", color=AMBAR).scale(1.0).move_to([-3.4, 0.8, 0])
            self.pop(sf)

            # «se cancela al restar»
            self.en("cancela")
            t1 = Line(sf[0].get_corner(DL) + DL * 0.04, sf[0].get_corner(UR) + UR * 0.04, color=ROJO, stroke_width=5)
            t2 = Line(sf[2].get_corner(DL) + DL * 0.04, sf[2].get_corner(UR) + UR * 0.04, color=ROJO, stroke_width=5)
            self.play(Create(t1), Create(t2), run_time=self.dur(0.4))

            # «la esperanza de A al cuadrado»
            self.en("ea2")
            r = formula(r"R_{XX}(\tau)", "=", r"E[A^2]", r"\,/\,2", r"\cdot", r"\cos(\omega_0\tau)", escala=1.2).move_to([0, -3.05, 0])
            self.play(FadeIn(r[0]), FadeIn(r[1]), FadeIn(r[2]), run_time=self.dur(0.6))

            # «dividida entre dos»
            self.en("entre2")
            self.play(FadeIn(r[3]), run_time=0.4)

            # «el coseno de omega cero por tau»
            self.en("cos_tau")
            self.play(FadeIn(r[4]), FadeIn(r[5]), run_time=self.dur(0.6))
            self.resaltar(r, color=AMBAR, escala=1.05)
