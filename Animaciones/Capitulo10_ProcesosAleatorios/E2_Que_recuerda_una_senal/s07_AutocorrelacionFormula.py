"""Escena 07 — Medio período de separación (R = −½) y la fórmula de la autocorrelación."""
from comun.escena import *


class AutocorrelacionFormula(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.cos = CuatroCosenos(ancho=6.0, paso=1.45, amp=0.5, centro=(3.5, -0.1))
        self.tab = TablaCortes(["0°", "90°", "180°", "270°"])
        self.derecha = []
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def dots(self, t: float) -> VGroup:
        return VGroup(*[Dot(self.cos.punto(i, t), radius=0.09, color=AMBAR) for i in range(4)])

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        cos, tab = self.cos, self.tab
        c1 = cos.corte(0.0, AMBAR)
        c2 = cos.corte(0.0, TXT)
        col0 = [tab.celda(0, i, s) for i, s in enumerate(["1", "0", "−1", "0"])]
        # el plano de partida ya está: la escena empieza donde terminó la anterior
        self.play(Create(VGroup(*cos.bases, *cos.curvas)), FadeIn(cos.rotulos), Create(c1), Create(c2),
                  FadeIn(tab.armazon()), FadeIn(tab.enc(0, "X(t₁)")), *[FadeIn(c) for c in col0], run_time=1.0)
        d1 = self.dots(0.0)
        self.add(d1)
        self.derecha += [VGroup(*cos.bases, *cos.curvas), cos.rotulos, c1, c2, d1]
        with self.narrar("b1"):
            # «medio período más tarde»
            self.en("medio_per")
            d2 = self.dots(0.5)
            self.play(c2.animate.set_x(float(cos.x(0.5))), FadeIn(d2), FadeIn(tab.enc(1, "X(t₂)")),
                      FadeIn(tab.enc(2, "producto")), run_time=self.dur(0.7))
            self.derecha += [d2]

            # «El primer oscilador pasa de uno a menos uno»
            self.en("primero")
            self.play(FadeIn(tab.celda(1, 0, "−1")), FadeIn(tab.celda(2, 0, "−1")), run_time=0.5)

            # «el tercero, de menos uno a uno»
            self.en("tercero")
            self.play(FadeIn(tab.celda(1, 2, "1")), FadeIn(tab.celda(2, 2, "−1")), run_time=0.5)

            # «los otros dos valen cero»
            self.en("otros")
            self.play(*[FadeIn(tab.celda(j, i, "0")) for j in (1, 2) for i in (1, 3)], run_time=0.5)

            # «Los productos son menos uno, cero»
            self.en("prods")
            m = tab.marco(2)
            self.play(Create(m), run_time=0.5)

            # «el promedio es menos un medio»
            self.en("menos_medio")
            self.pop(tab.prom(2, "−½"))

            # «Medio período después»
            self.en("medio_desp")
            fl = DoubleArrow([float(cos.x(0.0)), 3.3, 0], [float(cos.x(0.5)), 3.3, 0], color=AMBAR, stroke_width=4,
                             buff=0, tip_length=0.18)
            et = Text("½ período", color=AMBAR).scale(0.5).move_to([float(cos.x(0.25)), 3.65, 0])
            self.play(GrowFromCenter(fl), FadeIn(et), run_time=self.dur(0.6))
            self.derecha += [fl, et]

            # «la señal está al revés»
            self.en("reves")
            t = np.linspace(cos.t0, cos.t1, 170)
            copia = cos.curvas[0].copy().set_color(AMBAR)
            inversa = traza(cos.x(t), cos.y(0, -np.cos(2 * np.pi * t)), AMBAR, 3.2)
            self.add(copia)
            self.play(Transform(copia, inversa), run_time=self.dur(1.2))
            self.derecha += [copia]

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        tab = self.tab
        F = formula("R_{XX}", "(", "t_1", ",", "t_2", ")", "=", "E", "[", "X", "(", "t_1", ")", "X", "(", "t_2", ")", "]",
                    escala=0.95, colores={0: AMBAR}).move_to([2.9, 1.5, 0])
        auto = self.palabra("auto", AMBAR, 1.1)
        corr = self.palabra("correlación", TXT, 1.1)
        palabra = VGroup(auto, corr).arrange(RIGHT, buff=0.08).move_to([2.9, 3.2, 0])
        with self.narrar("b2"):
            # «Eso es la autocorrelación»
            self.en("autoc")
            self.play(*[FadeOut(m) for m in self.derecha], run_time=0.3)
            self.pop(palabra)

            # «erre sub equis equis de te uno, te dos»
            self.en("r")
            self.play(FadeIn(F[0:6], shift=DOWN * 0.15), run_time=self.dur(0.8))

            # «la esperanza de equis de te uno por equis de te dos»
            self.en("esp")
            self.play(FadeIn(F[6:], shift=DOWN * 0.15), run_time=self.dur(1.6))

            # «El prefijo auto»
            self.en("auto")
            self.play(auto.animate(rate_func=there_and_back).scale(1.3), run_time=0.7)

            # «del mismo proceso»
            self.en("mismo_proc")
            llave = Brace(VGroup(F[9], F[15]), DOWN, color=INK)
            lt = Text("mismo proceso", color=INK).scale(0.5).next_to(llave, DOWN, buff=0.1)
            self.play(GrowFromCenter(llave), FadeIn(lt), run_time=self.dur(0.7))

            # «los dos instantes coinciden»
            self.en("coinciden")
            ig = MathTex(r"t_2=t_1", color=TXT).scale(0.9).move_to([2.9, -0.35, 0])
            G = formula("E", "[", "X", "(", "t", ")", "{}^{2}", "]", escala=1.1).move_to([2.9, -1.3, 0])
            self.play(FadeIn(ig, shift=DOWN * 0.15), run_time=0.5)
            self.play(FadeIn(G, shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «la esperanza del cuadrado»
            self.en("cuadrado")
            self.play(G[6].animate.set_color(AMBAR).scale(1.3), run_time=0.5)

            # «segundo momento»
            self.en("segundo")
            sm = Text("segundo momento", color=INK).scale(0.6).move_to([2.9, -2.3, 0])
            self.pop(sm)

            # «aquí, un medio»
            self.en("un_medio")
            r = MathTex(r"=\tfrac12", color=AMBAR).scale(1.3).next_to(G, RIGHT, buff=0.3)
            self.pop(r)
