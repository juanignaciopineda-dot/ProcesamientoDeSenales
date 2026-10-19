"""Escena 09 — La media condicional nunca pierde contra la recta; empatan con dos valores (el canal de bits)."""
from comun.escena import *
from comun.figuras_c8e4 import *


class ElCanalEsUnaRecta(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.quien_gana()
        self.canal()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def quien_gana(self):
        b_rec = caja("Error: mejor recta", AMBAR, ancho=5.4, alto=1.0).move_to([3.9, 1.3, 0])
        b_con = caja("Error: media condicional", VERDE, ancho=5.4, alto=1.0).move_to([-3.9, 1.3, 0])
        t_entre = Text("Entre todas las rectas", color=INK).scale(0.5).next_to(b_rec, DOWN, buff=0.25)
        t_sin = Text("Sin restricciones", color=INK).scale(0.5).next_to(b_con, DOWN, buff=0.25)
        menor = MathTex(r"\leq", color=TXT).scale(2.0).move_to([0, 1.3, 0])
        igual = MathTex("=", color=AMBAR).scale(2.0).move_to([0, 1.3, 0])
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.3).move_to([0, 2.3, 0])
        carpa_t = Text("Carpa", color=INK).scale(0.55)
        carpa_f = MathTex(r"\frac{1}{24}", "<", r"\frac{1}{18}", color=TXT).scale(1.1)
        carpa = VGroup(carpa_t, carpa_f).arrange(RIGHT, buff=0.4).move_to([0, -0.9, 0])
        f1 = caja("1 · Solo dos valores", AMBAR, ancho=4.8, alto=0.9).move_to([-3.6, -2.9, 0])
        f2 = caja("2 · Gaussianas", AMBAR, ancho=4.8, alto=0.9).move_to([3.6, -2.9, 0])

        with self.narrar("b1"):
            # «La recta es lo mejor»
            self.en("recta")
            self.play(FadeIn(b_rec, shift=LEFT * 0.3), run_time=self.dur(0.6))

            # «entre las rectas»
            self.en("entre")
            self.play(FadeIn(t_entre), run_time=self.dur(0.4))

            # «La media condicional»
            self.en("cond")
            self.play(FadeIn(b_con, shift=RIGHT * 0.3), run_time=self.dur(0.6))

            # «sin restricciones»
            self.en("sin")
            self.play(FadeIn(t_sin), run_time=self.dur(0.4))

            # «nunca pierde»
            self.en("nunca")
            self.pop(menor)

            # «como en la carpa»
            self.en("carpa")
            self.play(FadeIn(carpa, shift=UP * 0.2), run_time=self.dur(0.8))

            # «cuándo empatan»
            self.en("empatan")
            self.play(FadeOut(carpa), ReplacementTransform(menor, igual), run_time=self.dur(0.6))
            self.pop(interr)

            # «Hay dos casos»
            self.en("dos")
            self.play(FadeIn(f1, shift=UP * 0.2), FadeIn(f2, shift=UP * 0.2), run_time=self.dur(0.8))

    # ------------------------------------------------------------ b2
    def canal(self):
        ax, etq = ejes([-0.5, 1.5, 0.5], [0, 1.0, 0.5], ancho=5.6, alto=3.8, x_label=r"\text{Recibido}", y_label=r"\hat{S}")
        g = VGroup(ax, etq).move_to([-3.2, -0.3, 0])
        g1 = DashedLine(ax.c2p(0, 0), ax.c2p(0, 1.0), color=INK, dash_length=0.15, stroke_width=2.5)
        g2 = DashedLine(ax.c2p(1, 0), ax.c2p(1, 1.0), color=INK, dash_length=0.15, stroke_width=2.5)
        n0 = MathTex("0", color=INK).scale(0.7).next_to(ax.c2p(0, 0), DOWN, buff=0.2)
        n1 = MathTex("1", color=INK).scale(0.7).next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        d0 = Dot(ax.c2p(0, 0.045), radius=0.11, color=ESTIMACION)
        d1 = Dot(ax.c2p(1, 0.79), radius=0.11, color=ESTIMACION)
        t0 = MathTex(num_tex(0.045), color=ESTIMACION).scale(0.8).next_to(d0, UP, buff=0.2).shift(RIGHT * 0.45)
        t1 = MathTex(num_tex(0.79), color=ESTIMACION).scale(0.8).next_to(d1, UP, buff=0.2)
        recta = Line(ax.c2p(-0.4, 0.045 - 0.745 * 0.4), ax.c2p(1.35, 0.045 + 0.745 * 1.35), color=ESTIMACION, stroke_width=5)
        h1 = formula(r"\text{Error}", "=", r"\sigma^2", r"(1-\rho^2)", escala=1.2, colores={0: ERROR}).move_to([3.7, 2.4, 0])
        h2 = formula(r"\sigma^2", "=", num_tex(0.21), escala=1.2).move_to([3.7, 1.3, 0])
        h3 = formula(num_tex(0.21), r"\cdot", r"(1-\rho^2)", escala=1.2).move_to([3.7, 0.2, 0])
        h4 = formula(r"\approx", num_tex(0.084), escala=1.2, colores={1: ERROR}).next_to(h3, RIGHT, buff=0.2)
        ok = tilde(VERDE, 0.5).move_to([2.1, -1.0, 0])
        antes = Text("Como en el episodio 2", color=VERDE).scale(0.55).move_to([4.7, -1.0, 0])

        with self.narrar("b2"):
            # «el canal de bits»
            self.en("canal")
            self.corte()
            self.play(Create(ax), FadeIn(etq), run_time=self.dur(1.0))

            # «solo vale cero o uno»
            self.en("cerouno")
            self.play(Create(g1), Create(g2), FadeIn(n0), FadeIn(n1), run_time=self.dur(0.8))

            # «dos puntos»
            self.en("puntos")
            self.play(FadeIn(d0, scale=0.3), FadeIn(d1, scale=0.3), run_time=self.dur(0.6))

            # «cero coma cero cuatro cinco»
            self.en("p045")
            self.play(FadeIn(t0), run_time=self.dur(0.5))

            # «cero coma setenta y nueve»
            self.en("p79")
            self.play(FadeIn(t1), run_time=self.dur(0.5))

            # «Por dos puntos siempre pasa una recta»
            self.en("pasa")
            self.play(Create(recta), run_time=self.dur(1.0))

            # «La mejor regla ya es una recta»
            self.en("regla")
            self.resaltar(recta, color=AMBAR, escala=1.03)

            # «la fórmula lo confirma»
            self.en("formula")
            self.play(*[FadeIn(h1[i]) for i in range(len(h1))], run_time=self.dur(0.9))

            # «cero coma dos uno»
            self.en("c021")
            self.play(*[FadeIn(h2[i]) for i in range(len(h2))], run_time=self.dur(0.6))

            # «uno menos rho al cuadrado da»
            self.en("unomenos")
            self.play(*[FadeIn(h3[i]) for i in range(len(h3))], run_time=self.dur(0.7))

            # «cero coma cero ocho cuatro»
            self.en("e084")
            self.play(*[FadeIn(h4[i]) for i in range(len(h4))], run_time=self.dur(0.6))

            # «el mismo error de antes»
            self.en("antes")
            self.play(FadeIn(ok, scale=0.4), FadeIn(antes), run_time=self.dur(0.6))
