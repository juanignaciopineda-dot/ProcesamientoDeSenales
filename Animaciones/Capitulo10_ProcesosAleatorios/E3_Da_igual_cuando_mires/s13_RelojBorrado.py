"""Escena 13 — Con amplitud 1 sale lo mismo que a mano; la fase aleatoria borra el origen de tiempos."""
from comun.escena import *


class RelojBorrado(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        L = Lienzo(ancho=6.0, alto=2.4, t_rango=(-1, 1), v_max=0.7, centro=(-2.6, 0.5))
        tau = np.linspace(-1, 1, 200)

        with self.narrar("b1"):
            # «Con amplitud uno»
            self.en("amp1")
            f = formula(r"R_{XX}(\tau)", "=", r"\tfrac{1}{2}", r"\cos(\omega_0\tau)", escala=1.2).move_to([0, 3.2, 0])
            a1 = MathTex("A=1", color=AMBAR).scale(0.9).move_to([-5.2, 3.2, 0])
            self.play(FadeIn(a1), FadeIn(f), run_time=self.dur(0.6))

            # «un medio por el coseno»
            self.en("medio_cos")
            self.resaltar(f[2], f[3], escala=1.15)
            base = L.base()
            cur = L.curva(tau, 0.5 * np.cos(2 * np.pi * tau), SENAL, 4)
            self.play(Create(base), Create(cur), run_time=self.dur(0.9))

            # «un medio en cero»
            self.en("en0")
            d0 = Dot(L.p(0, 0.5), radius=0.11, color=AMBAR)
            l0 = MathTex(r"\tfrac12", color=AMBAR).scale(0.8).next_to(d0, UP, buff=0.12)
            self.play(FadeIn(d0, scale=0.5), FadeIn(l0), run_time=0.4)

            # «cero a un cuarto de período»
            self.en("cuarto")
            d1 = Dot(L.p(0.25, 0), radius=0.11, color=AMBAR)
            l1 = MathTex("0", color=AMBAR).scale(0.8).next_to(d1, UP, buff=0.15)
            self.play(FadeIn(d1, scale=0.5), FadeIn(l1), run_time=0.4)

            # «menos un medio a medio período»
            self.en("medio")
            d2 = Dot(L.p(0.5, -0.5), radius=0.11, color=AMBAR)
            l2 = MathTex(r"-\tfrac12", color=AMBAR).scale(0.8).next_to(d2, DOWN, buff=0.12)
            self.play(FadeIn(d2, scale=0.5), FadeIn(l2), run_time=0.4)

            # «lo mismo que calculamos a mano»
            self.en("mano")
            filas = VGroup(*[MathTex(a, b, c, color=TXT).scale(0.8) for a, b, c in
                             ((r"\tau = 0", r"\to", r"\tfrac12"), (r"\tau = \tfrac14", r"\to", "0"),
                              (r"\tau = \tfrac12", r"\to", r"-\tfrac12"))])
            filas.arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to([4.6, 0.6, 0])
            cab = etiqueta("a mano", INK, 0.5).next_to(filas, UP, buff=0.3)
            self.play(FadeIn(cab), LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in filas], lag_ratio=0.25), run_time=self.dur(1.2))

            # «Es estacionario en sentido amplio»
            self.en("wss")
            s = sello("WSS", VERDE).move_to([5.5, 3.25, 0])
            self.pop(s)

            # «La moraleja»
            self.en("moraleja")
            mor = self.palabra("moraleja", AMBAR, 0.7).move_to([-5.5, -1.9, 0])
            self.pop(mor)

            # «si todos los osciladores arrancan a la vez»
            self.en("arrancan")
            gens = VGroup(*[generador(1.0, 1.0, np.pi / 2, 1.3, 0.9).move_to([x, -3.0, 0]) for x in (-4.6, -3.2, -1.8, -0.4)])
            self.play(LaggedStart(*[FadeIn(g, scale=0.7) for g in gens], lag_ratio=0.12), run_time=self.dur(0.8))

            # «el reloj tiene un instante especial»
            self.en("especial")
            r = reloj().scale(1.15).move_to([2.2, -2.9, 0])
            cero = Text("0", color=AMBAR, weight=BOLD).scale(0.6).move_to(r.get_top() + UP * 0.3)
            marca = Dot(r.get_top() + DOWN * 0.03, radius=0.09, color=AMBAR)
            self.play(FadeIn(r), FadeIn(cero), FadeIn(marca), run_time=0.5)

            # «el de la salida»
            self.en("salida")
            b = bandera(AMBAR).scale(0.9).move_to([3.7, -2.9, 0])
            self.play(FadeIn(b, shift=UP * 0.2), run_time=0.4)

            # «La fase aleatoria lo borra»
            self.en("borra")
            self.play(FadeOut(cero), FadeOut(marca), FadeOut(b), *[FadeOut(g) for g in gens], run_time=self.dur(0.6))

            # «la estadística»
            self.en("estadistica")
            banda = Rectangle(width=2.2, height=0.75, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.15).move_to([5.3, -2.9, 0])
            ondas = traza(np.linspace(4.3, 6.3, 80), -2.9 + 0.28 * serie(77, 80, 0.7), RUIDO, 3)
            self.play(FadeIn(banda), Create(ondas), run_time=self.dur(0.7))

            # «la hora»
            self.en("hora")
            dep = Text("depende solo de τ", color=INK).scale(0.5).move_to([5.3, -3.65, 0])
            self.play(FadeIn(dep, shift=UP * 0.1), Rotate(r.minutero, angle=-2 * PI, about_point=r.aro.get_center()),
                      run_time=self.dur(1.2))
        self.wait(1.0)
        self.limpiar()
