"""Escena 08 — La varianza del promedio de dos muestras seguidas."""
from comun.escena import *


class PromedioDeDos(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        L = Lienzo(ancho=6.4, alto=1.6, t_rango=(0, 1), v_max=3.0, centro=(-3.3, 2.5))
        t = np.linspace(0, 1, 160)
        s = 1.3 * serie(31, 160, 0.6)
        graba = L.curva(t, s, SENAL, 3.5)
        i1, i2 = 70, 76
        d1 = Dot(L.p(t[i1], s[i1]), radius=0.12, color=AMBAR)
        d2 = Dot(L.p(t[i2], s[i2]), radius=0.12, color=AMBAR)
        self.add(L.base(), graba)

        prom = MathTex(r"\frac{x_1+x_2}{2}", color=TXT).scale(1.3).move_to([-3.3, 0.5, 0])
        f = MathTex(r"\mathrm{Var}(x_1+x_2)", "=", r"\sigma^2", "+", r"\sigma^2", "+", "2C[1]", color=TXT).scale(1.0)
        f.move_to([0, -0.9, 0])
        f[2].set_color(AMBAR)
        f[4].set_color(AMBAR)
        f[6].set_color(CIAN)
        f2 = MathTex(r"\mathrm{Var}\!\left(\frac{x_1+x_2}{2}\right)", "=", r"\frac{\sigma^2+\sigma^2+2C[1]}{4}",
                     color=TXT).scale(1.0).move_to([0, -2.6, 0])

        with self.narrar("b1"):
            # «Para responder»
            self.en("resp")
            q = etiqueta("¿qué decide?", AMBAR, 0.7, BOLD).move_to([4.6, 3.4, 0])
            self.play(FadeIn(q), run_time=0.4)

            # «cuánto se dispersa»
            self.en("dispersa")
            cam = campana_mini((4.6, 2.3), 3.0, 1.2, SENAL, 4)
            dl = DoubleArrow([3.1, 1.55, 0], [6.1, 1.55, 0], color=AMBAR, buff=0, stroke_width=4)
            self.play(Create(cam), Create(dl), run_time=self.dur(0.9))

            # «empezando por lo más pequeño»
            self.en("pequeno")
            self.play(cam.animate.scale(0.45).move_to([4.6, 2.0, 0]), FadeOut(dl), run_time=self.dur(0.8))

            # «el promedio de dos muestras»
            self.en("dos")
            self.play(FadeIn(d1, scale=0.5), FadeIn(d2, scale=0.5), run_time=0.4)
            self.play(FadeIn(prom), run_time=0.5)

            # «En el capítulo siete»
            self.en("cap7")
            sl = sello("capítulo 7", AMBAR).scale(0.9).move_to([4.4, 0.5, 0])
            self.pop(sl)

            # «la varianza de una suma»
            self.en("suma")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=0.5)

            # «la varianza de la primera»
            self.en("v1")
            self.play(FadeIn(f[2]), run_time=0.4)

            # «más la de la segunda»
            self.en("v2")
            self.play(FadeIn(f[3]), FadeIn(f[4]), run_time=0.4)

            # «dos veces su covarianza»
            self.en("cov")
            self.play(FadeIn(f[5]), FadeIn(f[6]), run_time=0.5)
            self.resaltar(f[6], color=CIAN)

            # «al dividir entre dos»
            self.en("entre2")
            self.resaltar(prom, escala=1.2)

            # «entre cuatro»
            self.en("entre4")
            self.play(FadeIn(f2), run_time=0.8)
            cu = MathTex(r"\left(\tfrac12\right)^2=\tfrac14", color=AMBAR).scale(0.9).move_to([4.9, -3.6, 0])
            self.play(FadeIn(cu), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
