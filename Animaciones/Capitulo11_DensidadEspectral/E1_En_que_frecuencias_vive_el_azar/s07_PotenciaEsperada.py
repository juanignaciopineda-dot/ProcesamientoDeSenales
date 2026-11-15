"""Escena 07 — De la energía a la potencia, y a la potencia esperada sobre el ensemble."""
from comun.escena import *


class PotenciaEsperada(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        Lm = Lienzo(ancho=2.6, alto=0.9, t_rango=(0, 3), v_max=1.3, centro=(-5.2, 1.9))
        mini = onda_tel(Lm, tiempos=[0.5, 1.4, 2.1], color=SENAL, ancho=3)
        f1 = MathTex(r"\frac{10}{10}", "=", "1", color=TXT).scale(1.0).move_to([-2.2, 1.9, 0])
        f2 = MathTex(r"\frac{1000}{1000}", "=", "1", color=TXT).scale(1.0).move_to([1.9, 1.9, 0])
        ax1, _ = ejes([0, 10, 1], [0, 10, 1], ancho=4.0, alto=2.0, x_label="t")
        ax1.move_to([-3.6, -1.7, 0])
        l1 = ax1.plot(lambda x: x, x_range=[0, 10], color=AMBAR, stroke_width=4)
        ax2, _ = ejes([0, 10, 1], [0, 2, 1], ancho=4.0, alto=2.0, x_label="t")
        ax2.move_to([3.6, -1.7, 0])
        l2 = ax2.plot(lambda x: 1.0, x_range=[0, 10], color=VERDE, stroke_width=4)
        with self.narrar("b1"):
            # «energía por unidad de tiempo»
            self.en("def")
            d = etiqueta("potencia = energía ÷ tiempo", TXT, 0.75).move_to([0, 3.3, 0])
            self.pop(d)

            # «Con la onda telegráfica»
            self.en("tele")
            self.play(Create(mini), run_time=self.dur(0.7), rate_func=linear)

            # «diez de energía en diez segundos»
            self.en("diez")
            self.play(FadeIn(f1[0]), run_time=self.dur(0.6))

            # «da potencia uno»
            self.en("p1")
            self.play(FadeIn(f1[1:]), run_time=self.dur(0.4))

            # «Mil en mil segundos»
            self.en("mil")
            self.play(FadeIn(f2), run_time=self.dur(0.8))

            # «La energía crece sin parar»
            self.en("crece")
            et = etiqueta("energía", AMBAR, 0.55).move_to([-3.6, -0.35, 0])
            self.play(Create(ax1), FadeIn(et), run_time=self.dur(0.5))
            self.play(Create(l1), run_time=self.dur(1.2), rate_func=linear)

            # «la potencia se queda quieta»
            self.en("quieta")
            pt = etiqueta("potencia", VERDE, 0.55).move_to([3.6, -0.35, 0])
            self.play(Create(ax2), FadeIn(pt), run_time=self.dur(0.5))
            self.play(Create(l2), run_time=self.dur(0.8), rate_func=linear)

            # «Es finita»
            self.en("finita")
            ti = tilde(VERDE, 0.6).move_to([5.9, -0.35, 0])
            self.play(Create(ti), run_time=0.4)

            # «Primer problema resuelto»
            self.en("resuelto")
            sl = sello("resuelto", VERDE).move_to([0.0, -1.8, 0])
            self.pop(sl, sonido="exito")

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        L = Lienzo(ancho=8.0, alto=2.4, t_rango=(0, 1), v_max=1.5, centro=(-1.8, -1.4))
        pila = pila_de_curvas(L, 6, semilla=5, a=0.8, color=SENAL, opacidad=0.65, ancho=2.4, escala=0.5)
        idx = int(0.6 * 199)
        vals = [0.5 * serie(5 * 1000 + i, 200, 0.8)[idx] for i in range(6)]
        with self.narrar("b2"):
            # «una resistencia de un ohmio»
            self.en("resist")
            self.corte()
            r = Rectangle(width=1.1, height=0.5, color=TXT, stroke_width=3).move_to([-5.4, 2.4, 0])
            w1 = Line([-6.5, 2.4, 0], [-5.95, 2.4, 0], color=TXT, stroke_width=3)
            w2 = Line([-4.85, 2.4, 0], [-4.3, 2.4, 0], color=TXT, stroke_width=3)
            ohm = etiqueta("1 Ω", TXT, 0.45).move_to(r)
            self.play(Create(w1), Create(r), Create(w2), FadeIn(ohm), run_time=self.dur(0.9))

            # «su cuadrado»
            self.en("cuad")
            x2 = formula("x^2(t)", escala=1.1).move_to([-1.6, 2.4, 0])
            self.pop(x2)

            # «la potencia instantánea»
            self.en("inst")
            ins = etiqueta("potencia instantánea", AMBAR, 0.55).move_to([2.7, 2.4, 0])
            ar = flecha([0.8, 2.4, 0], [-0.6, 2.4, 0], AMBAR, 3)
            self.play(GrowArrow(ar), FadeIn(ins), run_time=self.dur(0.7))

            # «el segundo cambio»
            self.en("segundo")
            sc = etiqueta("segundo cambio: el ensemble", INK, 0.55).move_to([0, 1.3, 0])
            self.pop(sc)

            # «en un instante cualquiera»
            self.en("corte")
            cut = L.vertical(0.6, AMBAR, 3.5)
            self.play(Create(L.base()), LaggedStart(*[Create(c) for c in pila], lag_ratio=0.1),
                      run_time=self.dur(1.2), rate_func=linear)
            self.play(Create(cut), run_time=0.4)

            # «todas las grabaciones del ensemble»
            self.en("todas")
            puntos = VGroup(*[Dot(L.p(0.6, v), radius=0.09, color=AMBAR) for v in vals])
            self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in puntos], lag_ratio=0.1), run_time=self.dur(0.8))

            # «la esperanza de equis al cuadrado»
            self.en("esperanza")
            F = formula("E", "[", "x^2(t)", "]", escala=1.2, colores={0: AMBAR}).move_to([5.0, -1.4, 0])
            self.play(FadeIn(F[0:2]), run_time=0.3)
            self.play(FadeIn(F[2:]), run_time=self.dur(0.5))
