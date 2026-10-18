"""Escena 13 — Cuando el discriminante es cero: una variable es una recta de la otra (|ρ| = 1)."""
from comun.escena import *


class CuandoEsUno(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        par = parabola_l(centro=(-3.3, 0.4), ancho=5.2, alto=3.4, fondo=0.5, color=VERDE)
        par0 = parabola_l(centro=(-3.3, 0.4), ancho=5.2, alto=3.4, fondo=0.0, color=AMBAR)
        justo = MathTex(r"b^2-4ac=0", color=AMBAR).scale(1.5).move_to([0, 3.4, 0])
        punto = Dot(par0.L.p(0, 0), radius=0.12, color=AMBAR)
        lam0 = MathTex(r"\lambda_0", color=AMBAR).scale(0.9).next_to(punto, DOWN, buff=0.25)
        cero = MathTex(r"U-\lambda_0 V=0", color=TXT).scale(1.1).move_to([-3.3, -2.4, 0])
        rho = ValueTracker(0.3)
        marco = Rectangle(width=4.6, height=4.0, color=INK, stroke_width=2, stroke_opacity=0.6).move_to([3.6, 0.6, 0])
        nube = always_redraw(lambda: nube7((3.6, 0.6), rho.get_value(), n=45, ancho=4.0, semilla=5, color=SENAL))
        recta = MathTex("U", "=", r"\lambda_0 V", color=TXT).scale(1.2).move_to([3.6, -2.4, 0])
        recta[0].set_color(COL_U7)
        recta[2].set_color(COL_V7)
        sin = Text("Sin nada de azar", color=VERDE).scale(0.55).move_to([3.6, 3.0, 0])
        absr = MathTex(r"|\rho|=1", color=AMBAR).scale(1.8).move_to([0, -3.4, 0])
        icono = parabola_l(centro=(-6.0, -3.2), ancho=1.2, alto=0.8, fondo=0.0, color=AMBAR)
        ciclo = Text("Cap. 10 · 11 · 13", color=INK).scale(0.5).move_to([-3.9, -3.2, 0])
        with self.narrar("b1"):
            self.en("justo")
            self.play(Create(par.eje), Create(par.curva), run_time=self.dur(0.6))
            self.pop(justo)
            self.en("toca")
            self.play(Transform(par.curva, par0.curva), run_time=self.dur(1.2))
            self.play(FadeIn(punto), run_time=0.3)
            self.en("lambda")
            self.play(FadeIn(lam0), run_time=self.dur(0.4))
            self.en("cero")
            self.play(FadeIn(cero), run_time=self.dur(0.6))
            self.en("recta")
            self.add(nube)
            self.play(FadeIn(marco), FadeIn(recta), run_time=self.dur(0.5))
            self.play(rho.animate.set_value(1.0), run_time=self.dur(1.6))
            self.en("sinazar")
            self.play(FadeIn(sin), run_time=self.dur(0.4))
            self.en("rho")
            self.pop(absr)
            self.en("truco")
            self.play(FadeOut(par.curva), FadeOut(punto), FadeOut(lam0), FadeOut(par.eje), FadeOut(cero),
                      FadeIn(icono), run_time=self.dur(0.8))
            self.en("volvera")
            self.play(FadeIn(ciclo), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
