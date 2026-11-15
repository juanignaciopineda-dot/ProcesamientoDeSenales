"""Escena 07 — En frecuencia: H = conjugada de S dividida entre la densidad del ruido."""
from comun.escena import *


class EnFrecuencia(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        L = lienzo_w(ancho=9.0, alto=3.0, base_y=-2.2)
        eje = eje_w(L)
        # señal (2, 2, 1): |S|² normalizada; ruido con memoria 0,6; filtro |S| / D
        def s2(w):
            return np.abs(2 + 2 * np.exp(-1j * w) + np.exp(-2j * w)) ** 2 / 25.0

        def d(w):
            return d_ruido(w, 0.6)

        def h(w):
            hh = np.sqrt(s2(w)) / (d(w) + 0.05)
            return hh / 3.4

        ws = np.linspace(0, np.pi, 200)
        mejor = ws[np.argmax(np.sqrt(s2(ws)) / (d(ws) + 0.05))]
        c_s = curva_f(L, s2, 0, np.pi, color=SENAL, ancho=4)
        c_d = curva_f(L, d, 0, np.pi, color=RUIDO, ancho=4)
        c_h = curva_f(L, h, 0, np.pi, color=ESTIMACION, ancho=5)
        es = MathTex("|S|^2", color=SENAL).scale(0.7).move_to([L.x(1.4), 1.15, 0])
        ed = MathTex("D_{vv}", color=RUIDO).scale(0.7).move_to([L.x(0.5), 1.15, 0])
        r_fuerte = Rectangle(width=L.x(mejor + 0.45) - L.x(mejor - 0.45), height=3.0,
                             color=SENAL, stroke_width=0).set_fill(SENAL, 0.15).move_to(L.p(mejor, 0.5))
        r_debil = Rectangle(width=L.x(mejor + 0.45) - L.x(mejor - 0.45), height=3.0,
                            color=RUIDO, stroke_width=0).set_fill(RUIDO, 0.15).move_to(L.p(mejor, 0.5))
        H = MathTex("H", "=", "S^*", r"\big/", "D_{vv}", color=TXT).scale(0.9).move_to([-4.2, 3.3, 0])
        H[2].set_color(SENAL); H[4].set_color(RUIDO); H[0].set_color(ESTIMACION)
        rel = MathTex(r"\text{rel}", "=", r"\tfrac{1}{2\pi}\!\int", "|S|^2", r"\big/", "D_{vv}", r"\,d\Omega",
                      color=TXT).scale(0.8).move_to([2.8, 3.3, 0])
        rel[3].set_color(SENAL); rel[5].set_color(RUIDO)
        area = area_f(L, lambda w: s2(w) / (d(w) + 0.05) / 4.0, 0, np.pi, color=AMBAR, opacidad=0.35)
        mat = MathTex(r"\mathbf{g}", "=", r"\mathbf{r}^{T}", r"C^{-1}", r"\mathbf{s}", color=TXT).scale(0.9)
        mat.move_to([-0.6, -3.35, 0])
        doc = documento(INK).scale(0.8).move_to([2.6, -3.35, 0])
        apunte = Text("apunte", color=INK).scale(0.45).next_to(doc, RIGHT, buff=0.15)

        with self.narrar("b1"):
            # «En frecuencia»
            self.en("frec")
            self.play(Create(eje.base), FadeIn(eje.rotulos), Create(c_s), Create(c_d), run_time=self.dur(1.0))
            self.play(FadeIn(es), FadeIn(ed), run_time=self.dur(0.4))

            # «la conjugada de la transformada de la señal»
            self.en("conj")
            self.play(FadeIn(H[0]), FadeIn(H[1]), FadeIn(H[2]), run_time=self.dur(0.8))

            # «dividida entre»
            self.en("div")
            self.play(FadeIn(H[3]), run_time=self.dur(0.4))

            # «la densidad espectral del ruido»
            self.en("dens")
            self.play(FadeIn(H[4]), run_time=self.dur(0.5))

            # «mucha ganancia»
            self.en("ganancia")
            self.play(Create(c_h), run_time=self.dur(1.0))

            # «la señal es fuerte»
            self.en("fuerte")
            self.play(FadeIn(r_fuerte), run_time=self.dur(0.5))

            # «el ruido débil»
            self.en("debil")
            self.play(FadeOut(r_fuerte), FadeIn(r_debil), run_time=self.dur(0.5))

            # «la relación señal-ruido»
            self.en("rel")
            self.play(FadeOut(r_debil), FadeIn(rel[0]), FadeIn(rel[1]), run_time=self.dur(0.5))

            # «la integral, en todas las frecuencias»
            self.en("integral")
            self.play(FadeIn(rel[2]), FadeIn(rel[6]), FadeIn(area), run_time=self.dur(0.9))

            # «del cuadrado de la señal»
            self.en("cuad")
            self.play(FadeIn(rel[3]), run_time=self.dur(0.5))

            # «entre la densidad del ruido»
            self.en("entre")
            self.play(FadeIn(rel[4]), FadeIn(rel[5]), run_time=self.dur(0.6))

            # «La derivación con matrices»
            self.en("deriv")
            self.play(FadeIn(mat, shift=UP * 0.1), run_time=self.dur(0.8))

            # «está en el apunte»
            self.en("apunte")
            self.play(FadeIn(doc), FadeIn(apunte), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
