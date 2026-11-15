"""Escena 17 — Con memoria, promediar funciona pero más despacio."""
from comun.escena import *


class LaSorpresa(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        with self.narrar("b1"):
            # «una sorpresa»
            self.en("sorpresa")
            ex = self.palabra("!", AMBAR, 3.0).move_to([0, 0.2, 0])
            self.pop(ex)
            self.play(FadeOut(ex), run_time=0.3)

            # «veinte muestras independientes»
            self.en("indep20")
            fila = fila_puntos(20, 8.0, (-1.0, 2.9), SENAL, 0.11)
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in fila], lag_ratio=0.05), run_time=self.dur(1.2))

            # «de varianza cuatro»
            self.en("v4")
            sg = MathTex(r"\sigma^2=4", color=AMBAR).scale(0.9).move_to([4.6, 2.9, 0])
            self.play(FadeIn(sg), run_time=0.4)

            # «cuatro entre veinte»
            self.en("cuenta")
            cu = MathTex(r"\frac{4}{20}", color=TXT).scale(1.5).move_to([-3.5, 1.0, 0])
            self.play(Write(cu), run_time=0.8)

            # «cero coma dos»
            self.en("v02")
            r = MathTex(r"=0{,}2", color=VERDE).scale(1.5).next_to(cu, RIGHT, buff=0.2)
            self.pop(r)

            # «cero coma siete dos»
            self.en("v725")
            sen = VGroup(etiqueta("sensor", SENAL, 0.7, BOLD), MathTex(r"=0{,}725", color=AMBAR).scale(1.5))
            sen.arrange(RIGHT, buff=0.25).move_to([3.6, 1.0, 0])
            self.pop(sen)

            # «más de tres veces más»
            self.en("tres")
            fl = Arrow([-0.6, -0.1, 0], [3.0, -0.1, 0], color=ROJO, buff=0, stroke_width=5)
            x36 = MathTex(r"\times3{,}6", color=ROJO).scale(1.1).next_to(fl, DOWN, buff=0.15)
            self.play(Create(fl), FadeIn(x36), run_time=self.dur(0.8))

            # «Promediar funciona»
            self.en("funciona")
            tl = tilde(VERDE, 0.6).move_to([0, -1.6, 0])
            tx = etiqueta("promediar funciona", VERDE, 0.7, BOLD).next_to(tl, RIGHT, buff=0.2)
            self.play(FadeIn(tl, scale=0.5), FadeIn(tx), run_time=0.5)

            # «más despacio»
            self.en("despacio")
            ax = VGroup(Line([-5.0, -3.6, 0], [-5.0, -1.9, 0], color=INK, stroke_width=2),
                        Line([-5.0, -3.6, 0], [-0.6, -3.6, 0], color=INK, stroke_width=2))
            xs = np.linspace(0.0, 1.0, 50)
            c_ind = traza(-5.0 + xs * 4.4, -3.6 + 1.6 * np.exp(-3.2 * xs), AMBAR, 4)
            c_sen = traza(-5.0 + xs * 4.4, -3.6 + 1.7 * np.exp(-1.8 * xs), SENAL, 4)
            self.play(Create(ax), Create(c_ind), Create(c_sen), run_time=self.dur(1.6))

            # «Veinte muestras con memoria»
            self.en("memoria")
            self.play(FadeOut(VGroup(ax, c_ind, c_sen)), run_time=0.3)
            fm = fila_puntos(20, 8.0, (1.6, -2.3), SENAL, 0.11)
            hm = hilos_entre(fm, AMBAR, 3)
            self.play(FadeIn(fm), Create(hm), run_time=0.6)

            # «no valen lo que veinte independientes»
            self.en("novalen")
            ne = MathTex(r"\neq", color=ROJO).scale(1.6).move_to([-3.6, -2.3, 0])
            self.pop(ne)

            # «¿Cuánto valen, entonces?»
            self.en("cuanto")
            q = MathTex(r"20\ \text{del sensor}=\ ?\ \text{independientes}", color=AMBAR).scale(0.9).move_to([0, -3.4, 0])
            self.play(FadeIn(q), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
