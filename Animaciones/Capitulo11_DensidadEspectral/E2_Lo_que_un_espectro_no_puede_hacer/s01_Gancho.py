"""Escena 01 — Gancho: un rectángulo que parece una autocorrelación y no puede serlo."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        A = Lienzo(ancho=5.6, alto=3.0, t_rango=(-3, 3), v_max=1.5, centro=(-3.7, 0.0))
        B = Lienzo(ancho=5.6, alto=3.4, t_rango=(-12, 12), v_max=2.5, centro=(3.7, 0.0))
        C = Lienzo(ancho=5.6, alto=3.4, t_rango=(-12, 12), v_max=1.3, centro=(3.7, 0.0))
        ej_a = ejes_L(A, -0.3, 1.4)
        ej_b = ejes_L(B, -1.0, 2.3)
        rect = A.curva([-3, -1, -1, 1, 1, 3], [0, 0, 1, 1, 0, 0], SENAL, 5)
        r_lbl = MathTex(r"R_{xx}(\tau)", color=TXT).scale(0.9).move_to([-3.7, 2.4, 0])
        tl = tilde(VERDE, 0.4).move_to([-3.7, -2.3, 0])
        cr = cruz(ROJO, 0.55).move_to([-3.7, -2.3, 0])
        sinc = curva_f(B, sinc2x, -12, 12, MEDIDA, 4)
        lobulos = VGroup(area_f(B, sinc2x, np.pi, 2 * np.pi, ROJO, 0.55),
                         area_f(B, sinc2x, 3 * np.pi, 4 * np.pi, ROJO, 0.55),
                         area_f(B, sinc2x, -2 * np.pi, -np.pi, ROJO, 0.55),
                         area_f(B, sinc2x, -4 * np.pi, -3 * np.pi, ROJO, 0.55))
        f_lbl = MathTex(r"2\,\frac{\sin\omega}{\omega}", color=TXT).scale(0.9).move_to([3.7, 2.55, 0])
        esp = etiqueta("espectro", INK, 0.6).move_to([3.7, -2.4, 0])
        psd = curva_f(C, psd_tele, -12, 12, AMBAR, 5)
        psd_lbl = MathTex(r"\frac{4}{4+\omega^2}", color=TXT).scale(0.9).move_to([3.7, 2.55, 0])
        tl2 = tilde(VERDE, 0.4).move_to([3.7, -2.3, 0])

        with self.narrar("b1"):
            # «Un rectángulo»
            self.en("rect")
            self.play(Create(ej_a), Create(rect), run_time=self.dur(0.9))

            # «la autocorrelación más razonable»
            self.en("razonable")
            self.play(FadeIn(r_lbl), FadeIn(tl), run_time=0.4)

            # «ningún proceso puede tenerla»
            self.en("nopuede")
            self.play(ReplacementTransform(tl, cr), run_time=0.4)
            self.sfx("error")

            # «una sola cuenta»
            self.en("cuenta")
            self.play(Create(ej_b), Create(sinc), FadeIn(f_lbl), run_time=self.dur(1.0))
            self.play(FadeIn(lobulos), run_time=0.4)

            # «Hoy vemos»
            self.en("hoy")
            self.play(FadeIn(esp), run_time=0.4)

            # «cuáles no»
            self.en("cuales")
            self.play(FadeOut(sinc), FadeOut(lobulos), FadeOut(f_lbl), FadeOut(esp),
                      Create(psd), FadeIn(psd_lbl), run_time=self.dur(0.8))
            self.play(FadeIn(tl2), run_time=0.3)
        self.wait(1.0)
        self.limpiar()
