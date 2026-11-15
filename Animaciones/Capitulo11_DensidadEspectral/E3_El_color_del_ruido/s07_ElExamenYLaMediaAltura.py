"""Escena 07 — El examen de la curva 4/(4 + ω²) y su media altura en ω = α."""
from comun.escena import *


class ElExamenYLaMediaAltura(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        esp = Espectro(w_max=8, y_max=1.2, ancho=7.6, alto=3.6, centro=(2.2, -3.0))
        graf = esp.curva(tele_S, AMBAR)
        f = formula(r"S_{xx}(j\omega)", "=", r"\frac{4}{4 + \omega^2}").scale(1.0).move_to([2.2, 3.3, 0])
        f[2].set_color(AMBAR)
        cajas = VGroup(*[caja(t, INK, ancho=3.4, alto=0.75, scale=0.5) for t in ("real", "par", "nunca negativa")])
        cajas.arrange(DOWN, buff=0.35).move_to([-4.9, 1.5, 0])
        tildes = [tilde().scale(0.6).next_to(c, RIGHT, buff=0.15) for c in cajas]
        self.add(f, esp.ejes, graf)
        with self.narrar("b1"):
            # «Pasa el examen»
            self.en("examen")
            self.play(FadeIn(cajas), run_time=self.dur(0.6))
            # «es real»
            self.en("real")
            self.play(FadeIn(tildes[0]), cajas[0][0].animate.set_stroke(VERDE), run_time=self.dur(0.4))
            # «es par»
            self.en("par")
            espejo = DashedLine(esp.p(0, 0), esp.p(0, 1.15), color=INK, stroke_width=3)
            self.play(Create(espejo), FadeIn(tildes[1]), cajas[1][0].animate.set_stroke(VERDE), run_time=self.dur(0.5))
            # «solo aparece omega al cuadrado»
            self.en("omega2")
            self.resaltar(f[2], run_time=self.dur(0.6))
            # «nunca es negativa»
            self.en("nuncaneg")
            self.play(FadeIn(tildes[2]), cajas[2][0].animate.set_stroke(VERDE), run_time=self.dur(0.5))
            # «dos puntos»
            self.en("puntos")
            g0 = DashedLine(esp.p(0, 0), esp.p(0, 1.0), color=AMBAR, stroke_width=3)
            g2 = DashedLine(esp.p(2, 0), esp.p(2, 0.5), color=AMBAR, stroke_width=3)
            self.play(Create(g0), Create(g2), run_time=self.dur(0.5))
            # «En frecuencia cero vale uno»
            self.en("cero")
            p0 = Dot(esp.p(0, 1.0), color=AMBAR, radius=0.11)
            t0 = MathTex("1", color=AMBAR).scale(0.9).next_to(p0, UL, buff=0.1)
            self.play(FadeIn(p0), FadeIn(t0), run_time=self.dur(0.4))
            # «En omega igual a dos»
            self.en("en2")
            w2 = MathTex(r"\omega = 2", color=AMBAR).scale(0.8).move_to(esp.p(2, -0.18))
            self.play(FadeIn(w2), run_time=self.dur(0.4))
            # «cuatro entre ocho»
            self.en("ocho")
            c8 = MathTex(r"\frac{4}{8}", color=AMBAR).scale(0.9).move_to(esp.p(3.5, 0.85))
            self.play(FadeIn(c8), run_time=self.dur(0.5))
            # «un medio»
            self.en("medio")
            p2 = Dot(esp.p(2, 0.5), color=AMBAR, radius=0.11)
            t2 = MathTex(r"\frac{1}{2}", color=AMBAR).scale(0.9).next_to(p2, UR, buff=0.15)
            self.play(FadeIn(p2), FadeOut(c8), FadeIn(t2), run_time=self.dur(0.5))
            # «cae a la mitad»
            self.en("mitad")
            hl = DashedLine(esp.p(-2, 0.5), esp.p(2, 0.5), color=VERDE, stroke_width=3)
            self.play(Create(hl), run_time=self.dur(0.6))
            # «omega igual a alfa»
            self.en("enalfa")
            al = MathTex(r"\alpha", color=VERDE).scale(0.9).move_to(esp.p(2, -0.55))
            self.play(Transform(w2, MathTex(r"\omega = \alpha", color=VERDE).scale(0.8).move_to(esp.p(2, -0.18))),
                      run_time=self.dur(0.6))
            # «un segundo significado»
            self.en("segundo")
            sig = Text("¿qué significa α?", color=AMBAR, weight=BOLD).scale(0.6).move_to([-4.6, -1.8, 0])
            self.pop(sig)
        self.wait(1.0)
        self.limpiar()
