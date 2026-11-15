"""Escena 11 — La moneda: potencia 1, vecinas sin relación, autocovarianza δ[m] y espectro plano."""
from comun.escena import *


class LaMonedaSinMemoria(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.tira = tira_pm1([1, -1, -1, 1, -1, 1, 1, -1], lado=0.8, escala_txt=0.5).move_to([0.8, 2.9, 0])
        self.potencia_y_vecinas()
        self.autocovarianza()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def potencia_y_vecinas(self):
        tira = self.tira
        mon = moneda("", AMBAR).scale(0.9).move_to([-5.6, 2.9, 0])
        pot = Text("potencia", color=AMBAR, weight=BOLD).scale(0.6).move_to([-4.6, 1.2, 0])
        cuad = MathTex(r"x^2 = 1", r"\Rightarrow", r"E[x^2] = 1", color=TXT).scale(0.9).move_to([-4.6, 0.3, 0])
        cuad[2].set_color(AMBAR)
        marco = SurroundingRectangle(VGroup(tira.celdas[2], tira.celdas[3]), color=AMBAR, buff=0.06, stroke_width=4)
        marco.permitir_encima = True
        filas = [(r"(+1)(+1) = +1", VERDE), (r"(+1)(-1) = -1", ROJO), (r"(-1)(+1) = -1", ROJO), (r"(-1)(-1) = +1", VERDE)]
        tabla = VGroup(*[MathTex(t, color=c).scale(0.85) for t, c in filas]).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        tabla.move_to([3.6, 0.1, 0])
        prom = MathTex(r"\text{promedio} = \tfrac{1 - 1 - 1 + 1}{4} = 0", color=AMBAR).scale(0.8).move_to([2.6, -2.8, 0])
        with self.narrar("b1"):
            # «Vuelve a la moneda»
            self.en("moneda")
            self.play(FadeIn(mon), run_time=self.dur(0.4))
            # «más uno o menos uno»
            self.en("pm")
            self.play(LaggedStart(*[FadeIn(c) for c in tira.celdas], lag_ratio=0.12), run_time=self.dur(1.0))
            # «cada tirada independiente»
            self.en("indep")
            ind = Text("independientes", color=INK).scale(0.5).move_to([0.8, 2.2, 0])
            self.play(FadeIn(ind), run_time=self.dur(0.4))
            # «Su potencia es fácil»
            self.en("pot")
            self.play(FadeIn(pot), run_time=self.dur(0.4))
            # «al cuadrado, dan siempre uno»
            self.en("cuad")
            self.play(FadeIn(cuad[0]), run_time=self.dur(0.5))
            self.play(FadeIn(cuad[1]), FadeIn(cuad[2]), run_time=self.dur(0.5))
            # «dos tiradas vecinas»
            self.en("vecinas")
            self.play(FadeOut(ind), Create(marco), run_time=self.dur(0.6))
            # «cuatro combinaciones»
            self.en("cuatro")
            self.play(LaggedStart(*[FadeIn(f.set_opacity(0.5)) for f in tabla], lag_ratio=0.25), run_time=self.dur(1.2))
            # «Si coinciden»
            self.en("coinciden")
            self.play(tabla[0].animate.set_opacity(1), tabla[3].animate.set_opacity(1), run_time=self.dur(0.5))
            # «si no, menos uno»
            self.en("difieren")
            self.play(tabla[1].animate.set_opacity(1), tabla[2].animate.set_opacity(1), run_time=self.dur(0.5))
            # «el promedio es cero»
            self.en("cero")
            self.play(FadeIn(prom), run_time=self.dur(0.6))
        self.play(*[FadeOut(m) for m in self.mobjects if m not in tira.celdas and m is not self.camera.frame
                    and m is not tira], run_time=0.3)

    # ------------------------------------------------------------ b2
    def autocovarianza(self):
        tira = self.tira
        ks = list(range(-4, 5))
        pal = Palitos(ks, [1.0 if k == 0 else 0.0 for k in ks], ancho=5.4, alto=2.2, v_max=1.2, color=SENAL,
                      centro=(-3.7, -1.6), rotulo="m")
        i0 = ks.index(0)
        oculta(pal)
        self.add(pal)
        cov = MathTex(r"C_{xx}[m]", color=SENAL).scale(0.9).move_to([-3.7, 0.9, 0])
        delta = MathTex(r"\delta[m]", color=AMBAR).scale(1.1).move_to([-5.4, -0.15, 0])
        v1 = Text("1 en m = 0", color=AMBAR).scale(0.5).move_to([-2.0, 0.05, 0])
        v0 = Text("0 en otro caso", color=INK).scale(0.5).move_to([-2.0, -0.45, 0])
        arcos = VGroup(*[ArcBetweenPoints(tira.celdas[0].get_bottom(), tira.celdas[j].get_bottom(), angle=-0.8, color=INK, stroke_width=3)
                         for j in (2, 4, 6)])
        for a_ in arcos:
            a_.permitir_encima = True
        esp = Espectro(w_max=3.4, y_max=1.5, ancho=5.0, alto=1.8, centro=(3.7, -3.2), x_label=None)
        plano = esp.curva(lambda w: 1.0, AMBAR, a=-np.pi, b=np.pi)
        marcas = VGroup(MathTex(r"-\pi", color=INK).scale(0.6).move_to(esp.p(-np.pi, -0.35)),
                        MathTex(r"\pi", color=INK).scale(0.6).move_to(esp.p(np.pi, -0.35)))
        suma = oculta(MathTex(r"D_{xx}(\Omega) = \sum_m", r"C_{xx}[m]", r"e^{-j\Omega m}", color=TXT).scale(0.85)).move_to([3.7, 0.9, 0])
        solo = oculta(MathTex(r"1 \cdot e^{0}", "=", "1", color=AMBAR).scale(1.0)).move_to([3.7, -0.4, 0])
        self.add(suma, solo)
        with self.narrar("b2"):
            # «a cualquier distancia»
            self.en("dist")
            self.play(Create(arcos), run_time=self.dur(1.0))
            # «la autocovarianza»
            self.en("cov")
            self.play(FadeIn(cov), FadeOut(arcos), run_time=self.dur(0.5))
            # «una única barra de altura uno en el origen»
            self.en("barra")
            self.play(*revelar(pal.base, pal.eje, pal.tallos[i0], pal.puntos[i0]), run_time=self.dur(0.8))
            # «cero en todo lo demás»
            self.en("resto")
            self.play(*revelar(*[p for i, p in enumerate(pal.puntos) if i != i0],
                               *[t for i, t in enumerate(pal.tallos) if i != i0]), run_time=self.dur(0.8))
            # «delta de eme»
            self.en("delta")
            self.play(FadeIn(delta), run_time=self.dur(0.5))
            # «vale uno cuando eme es cero»
            self.en("vale1")
            self.play(FadeIn(v1), run_time=self.dur(0.5))
            # «cero en otro caso»
            self.en("vale0")
            self.play(FadeIn(v0), run_time=self.dur(0.5))
            # «Su transformada»
            self.en("transf")
            self.play(*revelar(suma[0], suma[1], suma[2]), run_time=self.dur(0.7))
            # «un solo término»
            self.en("solo")
            self.play(suma[1].animate.set_color(AMBAR), run_time=self.dur(0.5))
            # «uno por e elevado a cero»
            self.en("unoxe")
            self.play(*revelar(*solo), run_time=self.dur(0.8))
            # «para todas las frecuencias»
            self.en("todas")
            self.play(Create(esp.ejes), Create(plano), FadeIn(marcas), run_time=self.dur(1.0))
