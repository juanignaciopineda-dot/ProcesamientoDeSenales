"""Escena 09 — Desviación estándar: la raíz de la varianza vuelve a las unidades de la variable."""
from comun.escena import *


class DesviacionEstandar(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        s2 = MathTex(r"\sigma^2", color=AMBAR).scale(1.4).move_to([-4.8, 3.0, 0])
        unid = Text("Unidades²", color=INK).scale(0.6).next_to(s2, RIGHT, buff=0.4)
        x = MathTex("X", color=SENAL).scale(1.4).move_to([-4.8, 1.7, 0])
        volt = Text("Voltios [V]", color=AMBAR).scale(0.6).next_to(x, RIGHT, buff=0.4)
        v2 = Text("Voltios² [V²]", color=ROJO).scale(0.6).next_to(s2, RIGHT, buff=0.4)
        raiz = MathTex(r"\sqrt{\sigma^2}", "=", r"\sigma", color=TXT).scale(1.5).move_to([2.2, 2.4, 0])
        raiz[2].set_color(AMBAR)
        desv = self.palabra("Desviación estándar", AMBAR, 0.9).move_to([3.0, 3.5, 0])
        vuelve = Text("[V]", color=VERDE, weight=BOLD).scale(0.8).next_to(raiz, RIGHT, buff=0.4)
        d171 = MathTex(r"\sigma", r"\approx", "1{,}71", color=TXT).scale(1.4).move_to([-4.0, 0.3, 0])
        R = Regla7(centro=(0, -2.6), ancho=9.0, v0=0.4, v1=6.6)
        media = DashedLine(R.p(3.5) + UP * 1.3, R.p(3.5) + DOWN * 0.1, color=AMBAR, stroke_width=3)
        fl = VGroup(flecha(R.p(3.5) + UP * 0.9, R.p(3.5 - 1.71) + UP * 0.9, AMBAR, 4),
                    flecha(R.p(3.5) + UP * 0.9, R.p(3.5 + 1.71) + UP * 0.9, AMBAR, 4))
        sig_t = VGroup(MathTex(r"\sigma", color=AMBAR).scale(0.8).move_to(R.p(3.5 - 0.85) + UP * 1.3),
                       MathTex(r"\sigma", color=AMBAR).scale(0.8).move_to(R.p(3.5 + 0.85) + UP * 1.3))
        banda = Rectangle(width=R.p(5.21)[0] - R.p(1.79)[0], height=0.4, stroke_width=0).set_fill(AMBAR, 0.25
                         ).move_to((R.p(1.79) + R.p(5.21)) / 2 + UP * 0.45)
        with self.narrar("b1"):
            # «unidades al cuadrado»
            self.en("unidades")
            self.play(FadeIn(s2, shift=DOWN * 0.15), FadeIn(unid, shift=LEFT * 0.15), run_time=self.dur(0.8))
            # «la variable son voltios»
            self.en("voltios")
            self.play(FadeIn(x), FadeIn(volt, shift=LEFT * 0.15), run_time=self.dur(0.8))
            # «voltios al cuadrado»
            self.en("v2")
            self.play(Transform(unid, v2), run_time=self.dur(0.7))
            self.sfx("error")
            # «su raíz»
            self.en("raiz")
            self.play(FadeIn(raiz[0:2], shift=DOWN * 0.15), run_time=self.dur(0.8))
            self.play(FadeIn(raiz[2], shift=LEFT * 0.15), run_time=0.4)
            # «desviación estándar»
            self.en("desv")
            self.pop(desv)
            # «unidades de la variable»
            self.en("vuelve")
            self.play(FadeIn(vuelve, shift=LEFT * 0.15), run_time=self.dur(0.6))
            self.sfx("exito")
            # «uno coma siete uno»
            self.en("d171")
            self.play(FadeIn(d171, shift=DOWN * 0.15), run_time=self.dur(0.8))
            # «se alejan de tres coma cinco»
            self.en("alejan")
            self.play(FadeIn(R), Create(media), run_time=self.dur(0.7))
            self.play(LaggedStart(*[GrowArrow(a) for a in fl], lag_ratio=0.2), FadeIn(sig_t), run_time=self.dur(0.8))
            # «algo menos de dos puntos»
            self.en("menos2")
            self.play(FadeIn(banda), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
