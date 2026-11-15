"""Escena 15 — La parábola de Cauchy-Schwarz, por cuarta vez: la relación de salida no supera E/σ²."""
from comun.escena import *


class LaParabola(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        q9 = MathTex(r"\mathrm{SNR}>9\;?", color=AMBAR).scale(1.3).move_to([-4.0, 3.0, 0])
        peq = parabola_l(centro=(5.0, 2.5), ancho=2.4, alto=1.4, fondo=0.25, color=INK)
        l_caps = etiqueta("capítulos 7 · 10 · 11", INK, 0.45).move_to([5.0, 1.55, 0])
        cuarta = self.palabra("cuarta vez", AMBAR, 0.6).move_to([5.0, 0.7, 0])
        par = parabola_l(centro=(0.2, -1.4), ancho=5.2, alto=2.8, fondo=0.35, color=AMBAR)
        lx = MathTex(r"x_1,\ x_2,\ x_3", color=SENAL).scale(0.9).move_to([-4.6, 1.5, 0])
        ly = MathTex(r"y_1,\ y_2,\ y_3", color=ESTIMACION).scale(0.9).move_to([-4.6, 0.6, 0])
        lam = MathTex(r"\lambda", color=AMBAR).scale(1.2).move_to([-4.6, -0.6, 0])
        punto = Dot(par.L.p(-1.2, 0), radius=0.1, color=AMBAR)
        f_s = formula(r"\sum", r"(x-\lambda y)^2", escala=1.0, colores={1: TXT}).move_to([4.6, -0.8, 0])
        pos = MathTex(r"\geq 0", color=VERDE).scale(1.2).move_to([4.6, -1.9, 0])
        # segundo bloque
        f_d = MathTex(r"\left(\sum x^2\right)\lambda^2", "-", r"2\left(\sum xy\right)\lambda", "+", r"\sum y^2", r"\geq 0"
                      ).scale(0.85).move_to([0, 3.2, 0])
        par2 = parabola_l(centro=(-3.0, -0.4), ancho=4.6, alto=2.6, fondo=0.35, color=AMBAR)
        malo = parabola_l(centro=(-3.0, -0.4), ancho=4.6, alto=2.6, fondo=-0.6, color=ROJO)
        x_malo = cruz(ROJO, 1.0).move_to([-3.0, 0.9, 0])
        f_disc = MathTex(r"\Delta\leq 0", color=VERDE).scale(1.4).move_to([3.8, 1.5, 0])
        f_cs = MathTex(r"\left(\sum xy\right)^2", r"\leq", r"\left(\sum x^2\right)", r"\left(\sum y^2\right)"
                       ).scale(0.9).move_to([3.4, 0.0, 0])
        f_ap = MathTex(r"x=s,\ y=h", color=INK).scale(0.9).move_to([3.4, -1.1, 0])
        f_cota = MathTex(r"\mathrm{SNR}", r"\leq", r"E/\sigma^2", color=AMBAR).scale(1.3).move_to([3.4, -2.4, 0])

        with self.narrar("b1"):
            # «supere nueve»
            self.en("supere")
            self.pop(q9)

            # «un viejo conocido»
            self.en("conocido")
            self.play(Create(peq), FadeIn(l_caps), run_time=self.dur(0.8))

            # «por cuarta vez»
            self.en("cuarta")
            self.pop(cuarta)

            # «la parábola de Cauchy-Schwarz»
            self.en("parabola")
            self.play(Create(par.eje), Create(par.curva), run_time=self.dur(1.2))

            # «dos listas de números, equis e i griega»
            self.en("listas")
            self.play(FadeIn(lx), FadeIn(ly), run_time=self.dur(0.7))

            # «un número lambda cualquiera»
            self.en("lambda")
            self.play(FadeIn(lam, scale=1.4), FadeIn(punto), run_time=self.dur(0.4))
            self.play(punto.animate.move_to(par.L.p(1.2, 0)), run_time=self.dur(1.2))

            # «equis menos lambda por i griega, al cuadrado»
            self.en("suma")
            self.play(Write(f_s), run_time=self.dur(1.2))

            # «una suma de cuadrados»
            self.en("cuadrados")
            self.resaltar(f_s[1], color=AMBAR, escala=1.2)

            # «nunca es negativa»
            self.en("nuncaneg")
            self.pop(pos)

        with self.narrar("b2"):
            # «La desarrollamos»
            self.en("desarrolla")
            self.corte()
            self.play(Write(f_d), run_time=self.dur(2.2))

            # «una parábola en lambda»
            self.en("parab")
            self.play(Create(par2.eje), Create(par2.curva), run_time=self.dur(1.0))

            # «Nunca baja de cero»
            self.en("nunca")
            self.resaltar(par2.curva, color=VERDE, escala=1.0)

            # «cortar el eje dos veces»
            self.en("corta")
            self.play(Create(malo.curva), run_time=self.dur(0.8))
            self.play(Create(x_malo), run_time=0.3)

            # «su discriminante no es positivo»
            self.en("discr")
            self.play(FadeOut(malo.curva), FadeOut(x_malo), run_time=0.3)
            self.pop(f_disc)

            # «la suma de equis por i griega, al cuadrado»
            self.en("cs")
            self.play(Write(f_cs[0]), run_time=self.dur(1.2))

            # «no supera la suma de los cuadrados de equis»
            self.en("nosupera")
            self.play(Write(f_cs[1]), Write(f_cs[2]), run_time=self.dur(1.2))

            # «por la de i griega»
            self.en("porlade")
            self.play(Write(f_cs[3]), run_time=self.dur(0.8))

            # «Aplicada al filtro»
            self.en("aplic")
            self.play(FadeIn(f_ap), run_time=self.dur(0.6))

            # «la energía entre sigma cuadrado»
            self.en("cota")
            self.play(Write(f_cota), run_time=self.dur(1.2))
            self.sfx("exito", gain=-18)
        self.wait(1.0)
        self.limpiar()
