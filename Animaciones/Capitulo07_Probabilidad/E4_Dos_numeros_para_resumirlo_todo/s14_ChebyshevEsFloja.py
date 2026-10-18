"""Escena 14 — Chebyshev vale para todo, y por eso es flojo (uniforme con α = 1,5)."""
from comun.escena import *


class ChebyshevEsFloja(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        todo = self.palabra("Vale para todo", VERDE, 1.0).move_to([-3.6, 3.3, 0])
        corta = self.palabra("Y se queda corta", ERROR, 1.0).move_to([3.4, 3.3, 0])
        # uniforme entre 0 y 1: 4 unidades de ancho en pantalla
        x0, y0, W = -6.6, -1.8, 5.2
        base = Line([x0 - 0.3, y0, 0], [x0 + W + 0.3, y0, 0], color=INK, stroke_width=2)
        rect = Rectangle(width=W, height=1.9, stroke_width=3, color=SENAL).set_fill(SENAL, 0.3
                        ).move_to([x0 + W / 2, y0 + 0.95, 0])
        mu_l = DashedLine([x0 + W / 2, y0 - 0.1, 0], [x0 + W / 2, y0 + 2.4, 0], color=AMBAR, stroke_width=3)
        mu_t = MathTex("0{,}5", color=AMBAR).scale(0.7).move_to([x0 + W / 2, y0 - 0.45, 0])
        d = 0.433 * W
        colas = VGroup(Rectangle(width=W / 2 - d, height=1.9, stroke_width=0).set_fill(ERROR, 0.6
                                 ).move_to([x0 + (W / 2 - d) / 2, y0 + 0.95, 0]),
                       Rectangle(width=W / 2 - d, height=1.9, stroke_width=0).set_fill(ERROR, 0.6
                                 ).move_to([x0 + W - (W / 2 - d) / 2, y0 + 0.95, 0]))
        lim = VGroup(DashedLine([x0 + W / 2 - d, y0 - 0.1, 0], [x0 + W / 2 - d, y0 + 2.4, 0], color=AMBAR, stroke_width=2),
                     DashedLine([x0 + W / 2 + d, y0 - 0.1, 0], [x0 + W / 2 + d, y0 + 2.4, 0], color=AMBAR, stroke_width=2))
        a15 = MathTex(r"\alpha=1{,}5", color=AMBAR).scale(1.0).move_to([x0 + W / 2, y0 + 3.0, 0])
        # barras: cota y real
        bx = 0.6
        b_cota = Rectangle(width=0.44 * 12, height=0.8, stroke_width=0).set_fill(AMBAR, 0.7)
        b_cota.move_to([bx + 0.44 * 12 / 2, 0.5, 0])
        b_real = Rectangle(width=0.134 * 12, height=0.8, stroke_width=0).set_fill(ERROR, 0.8)
        b_real.move_to([bx + 0.134 * 12 / 2, -0.8, 0])
        t_cota = Text("Cota: 0,44", color=AMBAR).scale(0.8).next_to(b_cota, UP, buff=0.12).align_to(b_cota, LEFT)
        t_real = Text("Real: 0,13", color=ERROR).scale(0.8).next_to(b_real, DOWN, buff=0.12).align_to(b_real, LEFT)
        veces = MathTex(r"\times 3", color=VERDE).scale(1.1).move_to([bx + 0.134 * 12 + 1.0, -0.8, 0])
        interr = Text("¿Para qué sirve?", color=TXT, weight=BOLD).scale(0.8).move_to([3.5, 2.0, 0])
        rel = reloj().scale(1.2).move_to([3.5, 2.0, 0])
        prom = self.palabra("Promediar funciona", AMBAR, 1.2).move_to([0, -3.4, 0])
        with self.narrar("b1"):
            # «El precio de valer para todo»
            self.en("precio")
            self.pop(todo)
            # «quedarse corta»
            self.en("corta")
            self.pop(corta)
            # «una uniforme entre cero y uno»
            self.en("unif")
            self.play(Create(base), FadeIn(rect), FadeIn(mu_l), FadeIn(mu_t), run_time=self.dur(1.2))
            # «alfa igual a uno coma cinco»
            self.en("a15")
            self.play(Create(lim), FadeIn(a15), FadeIn(colas), run_time=self.dur(1.5))
            # «cero coma cuatro cuatro»
            self.en("c044")
            self.play(FadeIn(b_cota), FadeIn(t_cota), run_time=self.dur(0.9))
            # «cero coma uno tres»
            self.en("r013")
            self.play(FadeIn(b_real), FadeIn(t_real), run_time=self.dur(0.9))
            # «más de tres veces menos»
            self.en("tres_veces")
            self.play(FadeIn(veces, shift=LEFT * 0.15), run_time=self.dur(0.8))
            # «no necesita conocer la curva»
            self.en("sin_curva")
            self.play(rect.animate.set_fill(SENAL, 0.05).set_stroke(opacity=0.2), run_time=self.dur(1.0))
            # «sirve para demostrar algo»
            self.en("sirve")
            self.pop(interr)
            # «todos los días»
            self.en("dias")
            self.play(ReplacementTransform(interr, rel), run_time=self.dur(0.8))
            # «que promediar funciona»
            self.en("promediar")
            self.pop(prom)
        self.wait(1.0)
        self.limpiar()
