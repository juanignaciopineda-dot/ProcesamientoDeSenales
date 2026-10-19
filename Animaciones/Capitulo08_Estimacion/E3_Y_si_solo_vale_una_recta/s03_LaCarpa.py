"""Escena 03 — La carpa: una media condicional que no es una recta."""
from comun.escena import *
from comun.figuras_cap08_e3 import *


class LaCarpa(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.C = CarpaE3()
        self.xs, self.ys = puntos_carpa_e3(60, 5)
        self.pega()
        self.cortes()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pega(self):
        C = self.C
        mc = formula("E[", "y", r"\mid", "x", "]", escala=1.6, color=AMBAR,
                     colores={1: SENAL, 3: MEDIDA}).move_to([-3.6, 1.6, 0])
        etq = Text("Media condicional", color=INK).scale(0.55).move_to([-3.6, 0.7, 0])
        pega = Text("Un problema", color=ROJO, weight=BOLD).scale(0.8).move_to([-3.6, -0.6, 0])
        nube = NubeRhoE3(centro=(3.6, 0.5), sx=0.9, sy=0.75, n=45, rho=0.5)
        conj = Text("Distribución conjunta entera", color=INK).scale(0.5).move_to([3.6, -2.1, 0])
        regla = Text("La regla", color=AMBAR, weight=BOLD).scale(0.6).move_to([3.6, 2.7, 0])
        xs = np.linspace(-2.2, 2.2, 60)
        pts = [nube.p(a, 0.9 * np.sin(1.5 * a)) for a in xs]
        curva = traza([p[0] for p in pts], [p[1] for p in pts], AMBAR, 5)
        dots = [Dot(C.p(x, y), radius=0.07, color=TXT) for x, y in zip(self.xs, self.ys)]
        self.dots = dots
        pico = Dot(C.p(1, 1), radius=0.11, color=AMBAR)
        guia = DashedLine(C.p(0, 1), C.p(1, 1), color=INK, stroke_width=2)

        with self.narrar("b1"):
            # «La media condicional»
            self.en("mc")
            self.play(FadeIn(mc), run_time=self.dur(0.5))
            self.play(FadeIn(etq), run_time=self.dur(0.4))

            # «un problema»
            self.en("pega")
            self.pop(pega)

            # «la distribución conjunta entera»
            self.en("conjunta")
            self.play(FadeIn(nube), FadeIn(conj), run_time=self.dur(0.7))

            # «Y a veces la regla»
            self.en("regla")
            self.pop(regla)

            # «una curva»
            self.en("curva")
            self.play(Create(curva), run_time=self.dur(1.0))

            # «Mira este ejemplo»
            self.en("ejemplo")
            self.corte()
            self.play(Create(C.ax), FadeIn(C.et), run_time=self.dur(0.7))

            # «Un punto cae al azar»
            self.en("punto")
            self.play(LaggedStart(*[FadeIn(d, shift=DOWN * 0.4) for d in dots[:5]], lag_ratio=0.35),
                      run_time=self.dur(1.4))

            # «con la misma probabilidad en cualquier sitio»
            self.en("mismo")
            self.play(LaggedStart(*[FadeIn(d, shift=DOWN * 0.3) for d in dots[5:30]], lag_ratio=0.08),
                      run_time=self.dur(2.0))

            # «un triángulo con forma de carpa»
            self.en("triangulo")
            self.play(Create(C.tri), run_time=self.dur(0.9))
            self.play(LaggedStart(*[FadeIn(d) for d in dots[30:]], lag_ratio=0.05), run_time=self.dur(0.9))

            # «la base va de cero a dos»
            self.en("base")
            self.play(FadeIn(C.nums[0]), FadeIn(C.nums[2]), run_time=self.dur(0.4))
            self.play(Indicate(C.nums[0], color=AMBAR), Indicate(C.nums[2], color=AMBAR), run_time=self.dur(0.8))

            # «el pico, en equis igual a uno»
            self.en("pico")
            self.play(FadeIn(C.nums[1]), run_time=self.dur(0.3))
            self.pop(pico)

            # «tiene altura uno»
            self.en("alto")
            self.play(FadeIn(C.n_y1), Create(guia), run_time=self.dur(0.6))
        self.wait(0.3)
        self.pico_g = VGroup(pico, guia)

    # ------------------------------------------------------------ b2
    def cortes(self):
        C = self.C
        eje_x = Line(C.p(0, 0), C.p(2.35, 0), color=MEDIDA, stroke_width=7)
        txt_x = Text("Lo que observamos", color=MEDIDA).scale(0.5).move_to([2.6, -3.2, 0])
        eje_y = Line(C.p(0, 0), C.p(0, 1.15), color=SENAL, stroke_width=7)
        txt_y = Text("Lo que adivinamos", color=SENAL).scale(0.5).move_to([-3.0, 2.6, 0])
        c05 = C.corte(0.5)
        n05 = Text("0,5", color=MEDIDA).scale(0.42).move_to(C.p(0.5, 0) + DOWN * 0.3)
        reb = C.rebanada(0.5)
        d1 = Dot(C.p(0.5, 0.37), radius=0.08, color=TXT)
        extra = [Dot(C.p(0.5, y), radius=0.08, color=TXT) for y in (0.08, 0.2, 0.46)]
        cen = C.centro(0.5)
        l025 = Text("0,25", color=AMBAR, weight=BOLD).scale(0.5).move_to(C.p(0.5, 0.25) + RIGHT * 0.8)
        c1 = C.corte(1.0)
        reb1 = C.rebanada(1.0)
        cen1 = C.centro(1.0)
        l05 = Text("0,5", color=AMBAR, weight=BOLD).scale(0.5).move_to(C.p(1, 0.5) + RIGHT * 0.7)

        with self.narrar("b2"):
            # «Observamos su posición horizontal»
            self.en("obs")
            self.play(*[FadeOut(d) for d in self.dots], FadeOut(self.pico_g), Create(eje_x), FadeIn(txt_x),
                      run_time=self.dur(0.8))

            # «queremos adivinar la vertical»
            self.en("adivinar")
            self.play(Create(eje_y), FadeIn(txt_y), run_time=self.dur(0.8))

            # «Corta la carpa en equis igual a cero coma cinco»
            self.en("corte")
            self.play(FadeOut(eje_x), FadeOut(eje_y), FadeOut(txt_x), FadeOut(txt_y), Create(c05), FadeIn(n05),
                      run_time=self.dur(0.8))

            # «la rebanada va de cero a cero coma cinco»
            self.en("rebanada")
            self.play(Create(reb), run_time=self.dur(0.7))

            # «y como el punto cae»
            self.en("como")
            self.play(FadeIn(d1, shift=DOWN * 0.4), run_time=self.dur(0.5))

            # «a cualquier altura»
            self.en("altura")
            self.play(LaggedStart(*[FadeIn(d) for d in extra], lag_ratio=0.3), run_time=self.dur(0.8))

            # «la mejor apuesta es el centro»
            self.en("centro")
            self.play(FadeOut(d1), *[FadeOut(d) for d in extra], run_time=self.dur(0.3))
            self.pop(cen)

            # «cero coma veinticinco»
            self.en("c025")
            self.play(FadeIn(l025, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «En equis igual a uno»
            self.en("x1")
            self.play(FadeOut(c05), FadeOut(n05), FadeOut(reb), FadeOut(cen), FadeOut(l025), Create(c1),
                      run_time=self.dur(0.7))

            # «la rebanada llega hasta uno»
            self.en("reb1")
            self.play(Create(reb1), run_time=self.dur(0.7))

            # «apuesta cero coma cinco»
            self.en("a05")
            self.pop(cen1)
            self.play(FadeIn(l05, shift=LEFT * 0.2), run_time=self.dur(0.5))
