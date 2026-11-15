"""Escena 03 — La media de un proceso, corte a corte, con los cuatro osciladores desfasados."""
from comun.escena import *


class MediaPorCortes(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.cos = CuatroCosenos(ancho=6.0, paso=1.45, amp=0.5, centro=(3.5, -0.1))
        self.tab = TablaCortes(["0°", "90°", "180°", "270°"])
        self.corte_l = None
        self.puntos = None
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def dots(self, t: float) -> VGroup:
        return VGroup(*[Dot(self.cos.punto(i, t), radius=0.09, color=AMBAR) for i in range(4)])

    def mover_corte(self, t: float, dur: float = 0.4) -> list:
        """Animaciones: el corte pasa a `t` y los puntos se renuevan."""
        nuevos = self.dots(t)
        anims = [self.corte_l.animate.set_x(float(self.cos.x(t)))]
        if self.puntos is not None:
            anims.append(FadeOut(self.puntos))
        anims.append(FadeIn(nuevos))
        self.puntos = nuevos
        return anims

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        cos, tab = self.cos, self.tab
        campana = Curva(lambda x: gaussiana(x, 0, 1), x_rango=(-3, 3), y_max=0.5, ancho=3.4, alto=1.5,
                        color=SENAL).move_to([-3.9, 0.7, 0])
        with self.narrar("b1"):
            # «la media»
            self.en("media")
            w = self.palabra("media", AMBAR, 1.4).move_to([-3.9, 3.4, 0])
            self.pop(w)

            # «En el capítulo anterior»
            self.en("anterior")
            cap7 = etiqueta("capítulo 7", INK, 0.55).move_to([-3.9, 2.1, 0])
            self.play(FadeIn(cap7), Create(campana.ejes), Create(campana.grafica), run_time=self.dur(0.9))

            # «punto de equilibrio»
            self.en("equilibrio")
            bal = balancin().scale(0.9).move_to([-3.9, -1.5, 0])
            self.play(FadeIn(bal, shift=UP * 0.2), run_time=self.dur(0.6))

            # «en cada instante hay una variable»
            self.en("variable")
            self.play(FadeOut(cap7), FadeOut(campana), FadeOut(bal), run_time=0.3)
            self.play(Create(VGroup(*cos.bases, *cos.curvas)), run_time=self.dur(0.9))
            self.corte_l = cos.corte(-0.25)
            self.play(Create(self.corte_l), run_time=0.2)
            self.play(self.corte_l.animate.set_x(float(cos.x(1.75))), run_time=self.dur(1.5), rate_func=linear)

            # «en cada instante hay una media»
            self.en("media_t")
            mus = [Text("μ", color=TXT, weight=BOLD).scale(0.7).move_to([float(cos.x(t)), 3.35, 0])
                   for t in (0.0, 0.5, 1.0, 1.5)]
            self.pop(*mus)

            # «Calculémosla»
            self.en("calcula")
            self.play(*[m.animate.set_color(AMBAR) for m in mus], run_time=0.4)

            # «los cuatro osciladores»
            self.en("cuatro")
            self.play(*[FadeOut(m) for m in mus], FadeIn(cos.rotulos), FadeOut(w), run_time=0.5)

            # «En te igual a cero»
            self.en("t0")
            self.play(self.corte_l.animate.set_x(float(cos.x(0.0))), FadeIn(tab.armazon()),
                      FadeIn(tab.enc(0, "t = 0")),
                      FadeIn(etiqueta("t en períodos", INK, 0.45).move_to([-4.2, 3.15, 0])), run_time=self.dur(0.7))

            # «uno, cero, menos uno y cero»
            self.en("valores")
            self.puntos = self.dots(0.0)
            self.col0 = [tab.celda(0, i, txt) for i, txt in enumerate(["1", "0", "−1", "0"])]
            self.play(FadeIn(self.puntos), LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in self.col0], lag_ratio=0.25),
                      run_time=self.dur(1.4))

            # «Su promedio es cero»
            self.en("promedio")
            self.pop(tab.prom(0, "0"))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        cos, tab = self.cos, self.tab
        with self.narrar("b2"):
            # «un cuarto de período más tarde»
            self.en("cuarto")
            self.play(*self.mover_corte(0.25), FadeIn(tab.enc(1, "t = ¼")), run_time=self.dur(0.6))

            # «cero, menos uno, cero y uno»
            self.en("vals4")
            col1 = [tab.celda(1, i, txt) for i, txt in enumerate(["0", "−1", "0", "1"])]
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in col1], lag_ratio=0.2), run_time=self.dur(1.0))

            # «Otra vez cero»
            self.en("otra_vez")
            self.pop(tab.prom(1, "0"))

            # «un instante cualquiera»
            self.en("cualquiera")
            self.play(*self.mover_corte(0.125), run_time=self.dur(0.6))

            # «un octavo de período»
            self.en("octavo")
            self.play(FadeIn(tab.enc(2, "t = ⅛")), run_time=0.4)

            # «valen cero coma siete uno»
            self.en("valores8")
            self.play(FadeIn(tab.celda(2, 0, "0,71")), run_time=0.4)

            # «menos cero coma siete uno, menos cero»
            self.en("dos_negativos")
            self.play(FadeIn(tab.celda(2, 1, "−0,71")), FadeIn(tab.celda(2, 2, "−0,71")), run_time=0.5)

            # «y cero coma siete uno»
            self.en("cierra8")
            self.play(FadeIn(tab.celda(2, 3, "0,71")), run_time=0.4)

            # «De nuevo, cero»
            self.en("denuevo")
            self.pop(tab.prom(2, "0"))

            # «la media vale cero en todos los instantes»
            self.en("plana")
            planas = [Line(b.get_start(), b.get_end(), color=AMBAR, stroke_width=5) for b in cos.bases]
            self.play(LaggedStart(*[Create(p) for p in planas], lag_ratio=0.1), run_time=self.dur(0.9))
