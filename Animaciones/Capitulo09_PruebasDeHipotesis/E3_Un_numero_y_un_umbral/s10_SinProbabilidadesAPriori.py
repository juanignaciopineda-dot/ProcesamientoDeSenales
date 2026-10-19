"""Escena 10 — Cuando no hay probabilidades a priori: el criterio de Neyman-Pearson."""
from comun.escena import *
from comun.figuras_c9e3 import *


class SinProbabilidadesAPriori(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.sin_eta()
        self.nueva_pregunta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def sin_eta(self):
        with self.narrar("b1"):
            # «las probabilidades a priori»
            self.en("apriori")
            igual = MathTex(r"\eta =", color=ESTIMACION).scale(1.3)
            n = MathTex("p_0", color=C0).scale(1.3)
            d = MathTex("p_1", color=C1).scale(1.3)
            raya = Line(LEFT * 0.4, RIGHT * 0.4, color=TXT, stroke_width=3)
            frac = VGroup(n, raya, d).arrange(DOWN, buff=0.12)
            E = VGroup(igual, frac).arrange(RIGHT, buff=0.25).move_to([0, 2.5, 0])
            self.play(Write(E), run_time=self.dur(0.6))
            self.play(Indicate(n, color=C0, scale_factor=1.3), Indicate(d, color=C1, scale_factor=1.3),
                      run_time=self.dur(0.6))

            # «En el canal las conocemos»
            self.en("canal")
            canal = canal9(centro=(-4.2, -0.6), ancho=4.0, escala=0.8)
            pc = MathTex(r"p_0 = 0{,}7 \quad p_1 = 0{,}3", color=TXT).scale(0.7).next_to(canal, DOWN, buff=0.45)
            ti = tilde(VERDE, 0.4).next_to(pc, RIGHT, buff=0.2)
            self.play(FadeIn(canal, shift=UP * 0.15), FadeIn(pc), run_time=self.dur(0.5))
            self.play(Create(ti), run_time=self.dur(0.3))

            # «vuelve al radar»
            self.en("radar")
            radar = radar13().scale(1.2).move_to([2.4, -0.6, 0])
            self.play(FadeIn(radar, shift=UP * 0.15), run_time=self.dur(0.4))
            self.play(LaggedStart(*[Indicate(o, color=MEDIDA, scale_factor=1.15) for o in radar.ondas],
                                  lag_ratio=0.3), run_time=self.dur(0.8))

            # «haya un avión delante»
            self.en("avion")
            av = avion_arriba(C1).scale(1.1).move_to([5.4, -0.4, 0])
            p1 = MathTex(r"p_1 = \,?", color=C1).scale(0.8).next_to(av, DOWN, buff=0.5)
            self.play(FadeIn(av, shift=LEFT * 0.3), FadeIn(p1), run_time=self.dur(0.5))

            # «Nadie lo sabe»
            self.en("nadie")
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(1.6).move_to([5.4, 1.05, 0])
            self.pop(q)

            # «no hay eta»
            self.en("noeta")
            qe = Text("?", color=ESTIMACION, weight=BOLD).scale(1.1).move_to(frac)
            self.play(FadeOut(n, shift=UP * 0.3), FadeOut(d, shift=DOWN * 0.3), FadeOut(raya),
                      run_time=self.dur(0.4))
            self.play(FadeIn(qe, scale=0.5), run_time=self.dur(0.3))
        self.eta_q = VGroup(igual, qe)
        self.iconos = VGroup(canal, pc, ti, radar, av, p1, q)

    # ------------------------------------------------------------------ b2
    def nueva_pregunta(self):
        with self.narrar("b2"):
            # «Neyman y Pearson»
            self.en("np")
            np_ = Text("Neyman-Pearson", color=TXT, weight=BOLD).scale(0.8).move_to([0, 1.5, 0])
            self.play(FadeOut(self.iconos), run_time=self.dur(0.3))
            self.pop(np_)

            # «cambiar la pregunta»
            self.en("pregunta")
            self.play(self.eta_q.animate.scale(0.6).move_to([5.7, 3.3, 0]), np_.animate.move_to([0, 2.9, 0]),
                      run_time=self.dur(0.6))

            # «minimizar el error total»
            self.en("error")
            err = Text("Mínimo error total", color=ERROR, weight=BOLD).scale(0.6).move_to([0, 1.5, 0])
            self.play(FadeIn(err, shift=UP * 0.1), run_time=self.dur(0.4))
            t = tachar(err)
            self.play(Create(t), run_time=self.dur(0.3))

            # «cuántas falsas alarmas se toleran»
            self.en("fijar")
            fijar = casilla9("Fijar: Falsa alarma ≤ …", ERROR, ancho=5.2, alto=1.0, escala=0.52).move_to([-3.0, -0.8, 0])
            self.play(FadeIn(fijar, shift=UP * 0.15), run_time=self.dur(0.5))

            # «un cinco por ciento»
            self.en("cinco")
            fijar5 = casilla9("Fijar: Falsa alarma ≤ 5 %", ERROR, ancho=5.2, alto=1.0, escala=0.52).move_to(fijar)
            self.play(ReplacementTransform(fijar, fijar5), run_time=self.dur(0.4))
            self.sfx("tick")

            # «con esa condición»
            self.en("condicion")
            m = SurroundingRectangle(fijar5, color=ESTIMACION, buff=0.1, stroke_width=4)
            self.play(Create(m), run_time=self.dur(0.4))

            # «detectar lo máximo posible»
            self.en("max")
            conseguir = casilla9("Conseguir: La mayor detección", VERDE, ancho=5.2, alto=1.0, escala=0.52)
            conseguir.move_to([3.0, -0.8, 0])
            self.play(FadeIn(conseguir, shift=UP * 0.15), run_time=self.dur(0.5))
