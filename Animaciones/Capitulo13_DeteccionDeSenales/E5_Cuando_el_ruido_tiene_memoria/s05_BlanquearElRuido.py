"""Escena 05 — Blanquear el ruido: la segunda muestra menos 0,6 veces la primera, dividida entre 0,8."""
from comun.escena import *


class BlanquearElRuido(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.receta()
        self.blanquear()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def receta(self):
        blanq = caja("blanqueador", ESTIMACION, ancho=2.8, alto=0.9, scale=0.5).move_to([-1.2, 2.4, 0])
        adapt = caja("filtro adaptado", SENAL, ancho=3.2, alto=0.9, scale=0.5).move_to([5.0, 2.4, 0])
        mem = Text("ruido con memoria", color=RUIDO).scale(0.5).move_to([-5.3, 2.4, 0])
        blanco = Text("ruido blanco", color=RUIDO).scale(0.5).move_to([2.0, 2.4, 0])
        a1 = flecha(mem.get_right() + RIGHT * 0.05, blanq.get_left() + LEFT * 0.02, INK)
        a2 = flecha(blanq.get_right() + RIGHT * 0.02, blanco.get_left() + LEFT * 0.05, INK)
        a3 = flecha(blanco.get_right() + RIGHT * 0.05, adapt.get_left() + LEFT * 0.02, INK)
        resta = MathTex("x[n]", "-", "0{,}6", "x[n-1]", color=TXT).scale(0.9).move_to([-1.2, 1.1, 0])
        resta[2].set_color(AMBAR)
        monedas = tira_pm1([1, -1, -1, 1, 1], lado=0.5, color=RUIDO, escala_txt=0.3).move_to([2.0, 1.1, 0])
        P = PlanoV(centro=(0, -1.5), lado=2.1, esc=0.95)
        nube = P.puntos(0.6, n=26)
        el = P.elipse(0.6)

        with self.narrar("b1"):
            # «blanquear primero»
            self.en("blanquear")
            self.pop(blanq)

            # «aplicar lo que ya sabemos»
            self.en("aplicar")
            self.pop(adapt)

            # «Recuerda el blanqueador»
            self.en("recuerda")
            self.play(FadeIn(mem), Create(a1), run_time=self.dur(0.7))

            # «restar cero coma seis veces la muestra anterior»
            self.en("restar")
            self.play(FadeIn(resta, shift=UP * 0.1), run_time=self.dur(0.7))

            # «devolvía una moneda»
            self.en("moneda")
            self.play(Create(a2), FadeIn(monedas), run_time=self.dur(0.7))

            # «ruido blanco»
            self.en("blanco")
            self.play(FadeIn(blanco), Create(a3), run_time=self.dur(0.5))

            # «Hagámoslo con las dos muestras»
            self.en("hagamos")
            self.corte()
            self.play(Create(P.ejes), FadeIn(P.rot0), FadeIn(P.rot1), FadeIn(nube), Create(el),
                      run_time=self.dur(0.7))
        self.wait(0.1)

    # ------------------------------------------------------------ b2
    def blanquear(self):
        P = PlanoV(centro=(-3.6, -0.3), lado=2.4, esc=1.0, rot0="u_0", rot1="u_1")
        nube = P.puntos(0.6, n=34)
        el = P.elipse(0.6)
        el_raro = P.elipse(0, k=1.5, sx=1.0, sy=0.8)
        el_blanco = P.elipse(0, k=1.5)
        u0 = MathTex("u_0", "=", "v_0", color=TXT).scale(0.95).move_to([3.0, 2.8, 0])
        u0[0].set_color(RUIDO); u0[2].set_color(RUIDO)
        s1 = MathTex(r"\sigma^2 = 1", color=INK).scale(0.7).next_to(u0, RIGHT, buff=0.4)
        resta = MathTex("v_1", "-", "0{,}6", "v_0", color=TXT).scale(0.95).move_to([3.0, 1.7, 0])
        resta[0].set_color(RUIDO); resta[3].set_color(RUIDO); resta[2].set_color(AMBAR)
        r_seis = SurroundingRectangle(VGroup(resta[2], resta[3]), color=AMBAR, buff=0.08, stroke_width=3)
        v64 = MathTex(r"\sigma^2 = 0{,}64", color=AMBAR).scale(0.8).next_to(resta, RIGHT, buff=0.4)
        u1 = MathTex("u_1", "=", r"\frac{v_1-0{,}6\,v_0}{0{,}8}", color=TXT).scale(0.95).move_to([3.0, 0.1, 0])
        u1[0].set_color(RUIDO); u1[2].set_color(RUIDO)
        valga = MathTex(r"\sigma^2 = 1\ ?", color=AMBAR).scale(0.8).move_to([3.0, 0.9, 0])
        raiz = MathTex(r"0{,}8 = \sqrt{0{,}64}", color=TXT).scale(0.9).move_to([3.0, -1.4, 0])
        blanco = Text("ruido blanco", color=RUIDO).scale(0.5).next_to(P, DOWN, buff=0.35)

        with self.narrar("b2"):
            # «La primera queda igual»
            self.en("igual")
            self.corte(P, nube, el)
            self.play(FadeIn(u0, shift=UP * 0.1), FadeIn(s1), run_time=self.dur(0.6))

            # «A la segunda le restamos»
            self.en("resta")
            self.play(FadeIn(resta[0]), FadeIn(resta[1]), run_time=self.dur(0.5))

            # «cero coma seis veces la primera»
            self.en("seis")
            self.play(FadeIn(resta[2]), FadeIn(resta[3]), Create(r_seis), run_time=self.dur(0.6))

            # «varianza cero coma seis cuatro»
            self.en("v64")
            self.play(FadeIn(v64, shift=UP * 0.1), run_time=self.dur(0.6))

            # «no está correlacionada con la primera»
            self.en("nocorr")
            self.play(ReplacementTransform(el, el_raro), run_time=self.dur(0.9))

            # «Para que valga uno»
            self.en("valga")
            self.play(FadeOut(r_seis), FadeIn(valga), run_time=self.dur(0.5))

            # «dividimos entre cero coma ocho»
            self.en("div")
            self.play(FadeOut(valga), FadeIn(u1, shift=UP * 0.1), run_time=self.dur(0.7))

            # «la raíz de cero coma seis cuatro»
            self.en("raiz")
            self.play(FadeIn(raiz, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Ahora las dos muestras son independientes»
            self.en("indep")
            self.play(ReplacementTransform(el_raro, el_blanco), run_time=self.dur(0.9))

            # «ruido blanco»
            self.en("blanco2")
            self.pop(blanco)
