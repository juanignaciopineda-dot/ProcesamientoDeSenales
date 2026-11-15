"""Escena 07 — La regla: curvas escaladas por su a priori; con una medición siempre se decide lo mismo."""
from comun.escena import *

ESC = 3.0


class LaReglaDeDecision(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        R = self.R = RectaR(centro=(0.0, -1.5), ancho=9.5, x_rango=(-1.5, 1.5))
        self.r0 = rect_dens(R, -1, 1, 0.5, ESC, RUIDO)
        self.r1 = rect_dens(R, -0.5, 0.5, 1.0, ESC, SENAL)
        self.punto = Dot(R.p(0.2), radius=0.18, color=MEDIDA)
        self.r_et = MathTex("r", color=MEDIDA).scale(1.1).next_to(self.punto, DOWN, buff=0.2)
        self.regla()
        self.cuenta()
        self.error()
        self.wait(1.0)
        self.limpiar()

    def parpadeo(self, m, color=AMBAR):
        self.play(m.animate(rate_func=there_and_back).set_stroke(color, 7), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b1
    def regla(self):
        R = self.R
        F = formula(r"P(H_i\mid r)", r"\propto", "p_i", r"\cdot", r"f(r\mid H_i)", escala=1.4,
                    colores={2: AMBAR}).move_to([0, 3.3, 0])
        r0s = rect_dens(R, -1, 1, 0.375, ESC, RUIDO)
        r1s = rect_dens(R, -0.5, 0.5, 0.25, ESC, SENAL)
        self.r0s, self.r1s, self.F = r0s, r1s, F
        flecha_a = Arrow([R.p(0.2)[0], 1.3, 0], [R.p(0.2)[0], -0.3, 0], buff=0, color=AMBAR, stroke_width=6)
        guia = DashedLine(R.p(0.2), R.p(0.2) + UP * 1.125, color=AMBAR, stroke_width=3)
        err = VGroup(Text("error", color=ROJO, weight=BOLD), Text("mínimo", color=TXT, weight=BOLD)).arrange(
            RIGHT, buff=0.2).scale(1.1).move_to([0, 2.3, 0])
        self.err_lbl = err

        with self.narrar("b1"):
            # «Ahora, la regla»
            self.en("regla")
            self.corte()
            self.play(FadeIn(R), FadeIn(self.r0), FadeIn(self.r1), run_time=self.dur(0.6))

            # «Midiendo un valor»
            self.en("valor")
            self.play(FadeIn(self.punto, shift=DOWN * 0.8), FadeIn(self.r_et), run_time=self.dur(0.5))

            # «la probabilidad de cada hipótesis»
            self.en("probh")
            self.play(FadeIn(F[0], shift=UP * 0.1), run_time=self.dur(0.6))

            # «ya con el dato en la mano»
            self.en("dato")
            self.resaltar(self.punto, color=AMBAR)

            # «proporcional a su curva»
            self.en("prop")
            self.play(FadeIn(F[1]), FadeIn(F[4]), run_time=self.dur(0.6))

            # «su probabilidad a priori»
            self.en("pi")
            self.play(FadeIn(F[2]), FadeIn(F[3]), run_time=self.dur(0.6))

            # «dibujamos cada curva multiplicada»
            self.en("escalar")
            self.play(Transform(self.r0, r0s), Transform(self.r1, r1s), run_time=self.dur(1.0))

            # «decidimos por la más alta»
            self.en("alta")
            self.play(GrowArrow(flecha_a), run_time=self.dur(0.6))

            # «en el valor medido»
            self.en("medido")
            self.play(Create(guia), run_time=self.dur(0.5))

            # «minimiza la probabilidad de error»
            self.en("minimiza")
            self.pop(err)
        self.wait(0.3)
        self.quitar1 = VGroup(flecha_a, guia)

    # ------------------------------------------------------------ b2
    def cuenta(self):
        R = self.R
        c0 = MathTex(r"\tfrac34", r"\cdot", r"\tfrac12", color=RUIDO).scale(1.4).move_to([-5.4, 0.6, 0])
        o3 = MathTex(r"=\tfrac38", color=RUIDO).scale(1.4).next_to(c0, DOWN, buff=0.25)
        c1 = MathTex(r"\tfrac14", r"\cdot", "1", color=SENAL).scale(1.4).move_to([5.4, 0.6, 0])
        o2 = MathTex(r"=\tfrac14=\tfrac28", color=SENAL).scale(1.3).next_to(c1, DOWN, buff=0.25)
        barrido = Dot(R.p(-0.45), radius=0.12, color=MEDIDA)
        gana = self.gana = rect_dens(R, -0.5, 0.5, 0.375, ESC, RUIDO, 0.5)
        h1 = MathTex("H_1", color=SENAL).scale(1.6).move_to([0, 2.6, 0])
        x_h1 = cruz(ROJO, 1.6).move_to(h1.get_center())

        with self.narrar("b2"):
            # «Hagamos la cuenta»
            self.en("cuenta")
            self.play(FadeOut(self.F), FadeOut(self.err_lbl), FadeOut(self.quitar1), run_time=self.dur(0.4))

            # «La hipótesis cero escalada»
            self.en("h0esc")
            self.parpadeo(self.r0)

            # «tres cuartos por un medio»
            self.en("c0")
            self.play(FadeIn(c0, shift=UP * 0.1), run_time=self.dur(0.7))

            # «tres octavos»
            self.en("o3")
            self.play(FadeIn(o3), run_time=self.dur(0.5))

            # «un cuarto por uno»
            self.en("c1")
            self.play(FadeIn(c1, shift=UP * 0.1), run_time=self.dur(0.6))

            # «o dos octavos»
            self.en("o2")
            self.play(FadeIn(o2), run_time=self.dur(0.5))
            self.parpadeo(self.r1, SENAL)

            # «En todos los puntos donde las dos existen»
            self.en("puntos")
            self.play(FadeOut(self.punto), FadeOut(self.r_et), FadeIn(barrido), run_time=0.25)
            self.play(barrido.animate.move_to(R.p(0.45)), run_time=self.dur(1.2))

            # «gana la cero»
            self.en("gana")
            self.play(FadeIn(gana), run_time=self.dur(0.5))

            # «Nunca conviene decir hache uno»
            self.en("nunca")
            self.play(FadeIn(h1), run_time=0.2)
            self.pop(x_h1)
        self.wait(0.3)
        self.quitar2 = VGroup(c0, o3, c1, o2, barrido, h1, x_h1)

    # ------------------------------------------------------------ b3
    def error(self):
        R = self.R
        siempre = VGroup(Text("siempre", color=AMBAR, weight=BOLD).scale(1.2),
                         MathTex("H_0", color=RUIDO).scale(1.6)).arrange(RIGHT, buff=0.3).move_to([0, 2.9, 0])
        cas = casillas(4, rojas=(0,), centro=(5.0, 2.0), lado=0.6)
        pe = MathTex(r"P_e=\tfrac14", color=ROJO).scale(1.5).move_to([5.0, 0.9, 0])
        veamos = Text("¿y con dos?", color=AMBAR, weight=BOLD).scale(1.1).move_to([-4.8, 1.8, 0])
        eje2 = Arrow(R.p(0), R.p(0) + UP * 3.8, buff=0, color=INK, stroke_width=3, tip_length=0.2,
                     max_tip_length_to_length_ratio=0.1)
        r2 = MathTex("r_2", color=INK).scale(0.7).next_to(eje2, RIGHT, buff=0.1).shift(UP * 1.5)

        with self.narrar("b3"):
            # «decir siempre»
            self.en("siempre")
            self.play(FadeOut(self.quitar2), FadeOut(self.gana), run_time=0.25)
            self.play(FadeIn(siempre, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «nos equivocamos»
            self.en("equivocamos")
            self.play(self.r1.animate.set_color(ROJO).set_fill(ROJO, 0.55), run_time=self.dur(0.5))

            # «una de cada cuatro veces»
            self.en("cuatro")
            self.play(FadeIn(cas), run_time=self.dur(0.5))

            # «la probabilidad de error es un cuarto»
            self.en("pe")
            self.pop(pe)

            # «Parece triste»
            self.en("triste")
            self.play(Wiggle(pe, scale_value=1.15, rotation_angle=0.03 * TAU), run_time=self.dur(0.7))

            # «Veamos qué pasa»
            self.en("veamos")
            self.pop(veamos)

            # «hacemos dos»
            self.en("dos")
            self.play(FadeOut(self.r0), FadeOut(self.r1), FadeOut(siempre), FadeOut(veamos), run_time=0.3)
            self.play(Create(eje2), FadeIn(r2), run_time=self.dur(0.6))
        self.wait(0.3)
