"""Escena 09 — Comprobar la desigualdad con el micrófono sin ruido: igualdad, la parábola toca el eje."""
from comun.escena import *


class LaComprobacionConElMicrofono(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        par = parabola_l(centro=(-3.6, 0.3), ancho=4.2, alto=2.6, fondo=0.3, color=AMBAR)
        l_cs = etiqueta("Cauchy-Schwarz", AMBAR, 0.6).move_to([-3.6, 2.6, 0])
        c10 = caja("Cap. 10", INK, ancho=1.6, alto=0.5, scale=0.4).move_to([2.2, 3.3, 0])
        f10 = formula(r"|R(\tau)|\le R(0)", escala=0.8).move_to([5.0, 3.3, 0])
        c13 = caja("Cap. 13", INK, ancho=1.6, alto=0.5, scale=0.4).move_to([2.2, 2.2, 0])
        l13 = etiqueta("una vez más", INK, 0.5).move_to([4.6, 2.2, 0])
        # el micrófono tardío
        pers = persona(AZUL).scale(0.9).move_to([-6.0, 2.7, 0])
        mic = microfono(CIAN).scale(1.0).move_to([-4.5, 2.7, 0])
        F1 = oculta(formula(r"|S_{yx}|^2", "=", r"S_{xx}^2", escala=1.0, colores={0: MEDIDA}).move_to([-3.2, 0.9, 0]))
        F2 = oculta(formula(r"S_{yy}", "=", r"S_{xx}", escala=1.0, colores={0: MEDIDA, 2: SENAL}
                            ).move_to([-3.2, -0.5, 0]))
        t = np.linspace(0, 4, 200)
        v = 0.8 * voz_valores(200)
        d = 24
        ret = np.concatenate([np.zeros(d), v[:-d]])
        La = Lienzo(ancho=5.0, alto=1.4, t_rango=(0, 4), v_max=1.0, centro=(4.1, 1.3))
        Lb = Lienzo(ancho=5.0, alto=1.4, t_rango=(0, 4), v_max=1.0, centro=(4.1, -1.0))
        ca, cb = La.curva(t, v, SENAL, 2.4), Lb.curva(t, ret, MEDIDA, 2.4)
        aa, ab = area_bajo(La, t, v ** 2, SENAL, 0.45), area_bajo(Lb, t, ret ** 2, MEDIDA, 0.45)
        with self.narrar("b1"):
            # «la parábola de Cauchy-Schwarz del capítulo siete»
            self.en("cs7")
            self.corte()
            self.play(Create(par.eje), Create(par.curva), FadeIn(l_cs), run_time=self.dur(1.0))

            # «el capítulo anterior»
            self.en("anterior")
            self.play(FadeIn(c10), run_time=self.dur(0.4))

            # «acotó la autocovarianza»
            self.en("autocov")
            self.play(FadeIn(f10), run_time=self.dur(0.6))

            # «una vez más, en el capítulo trece»
            self.en("cap13")
            self.play(FadeIn(c13), FadeIn(l13), run_time=self.dur(0.6))

            # «Comprobémoslo con el micrófono»
            self.en("comprobar")
            self.corte()
            self.add(F1, F2)
            self.play(FadeIn(pers), FadeIn(mic), run_time=self.dur(0.6))

            # «El módulo de la cruzada»
            self.en("modulo")
            self.play(*revelar(F1), run_time=self.dur(0.8))

            # «la densidad de la voz al cuadrado»
            self.en("sxx2")
            self.play(F1[2].animate.set_color(SENAL), run_time=0.5)

            # «La densidad del micrófono es la misma»
            self.en("syy")
            self.play(*revelar(F2), run_time=self.dur(0.8))

            # «retrasar no cambia la potencia»
            self.en("retrasar")
            self.play(Create(La.base()), Create(ca), Create(Lb.base()), Create(cb), run_time=self.dur(1.0),
                      rate_func=linear)
            self.play(FadeIn(aa), FadeIn(ab), run_time=self.dur(0.6))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        p1 = MathTex(r"S_{xx}\cdot S_{xx}", color=TXT).scale(1.0)
        eq = MathTex("=", color=VERDE).scale(1.2)
        p2 = MathTex(r"S_{xx}\cdot S_{xx}", color=TXT).scale(1.0)
        fila = VGroup(p1, eq, p2).arrange(RIGHT, buff=0.35).move_to([-3.0, 3.1, 0])
        par = parabola_l(centro=(-3.0, 0.4), ancho=4.2, alto=2.6, fondo=0.0, color=VERDE)
        c7 = caja("Cap. 7", INK, ancho=1.4, alto=0.5, scale=0.4).move_to([-5.9, -1.7, 0])
        rho = formula(r"\rho=1", escala=1.0, colores={0: AMBAR}).move_to([-3.0, -1.7, 0])
        # recta: puntos alineados
        pts = VGroup(*[Dot([3.0 + 0.55 * k, 1.5 + 0.4 * k, 0], radius=0.07, color=SENAL) for k in range(-3, 4)])
        recta = Line([1.2, 0.1, 0], [5.4, 2.9, 0], color=AMBAR, stroke_width=3)
        l_rec = etiqueta("una recta", AMBAR, 0.5).move_to([5.8, 0.6, 0])
        t = np.linspace(0, 4, 200)
        v = 0.8 * voz_valores(200)
        Lv = Lienzo(ancho=5.0, alto=1.3, t_rango=(0, 4), v_max=1.0, centro=(4.1, -0.5))
        cv = Lv.curva(t, v, SENAL, 3.0)
        cm = Lv.curva(t, v, MEDIDA, 2.0)
        l_sin = etiqueta("sin azar añadido", INK, 0.5).move_to([4.1, -1.5, 0])
        Lr = Lienzo(ancho=5.0, alto=0.9, t_rango=(0, 4), v_max=1.0, centro=(4.1, -2.7))
        cr = ruido_t(Lr, semilla=5, amp=0.2, color=RUIDO)
        mayor = MathTex("<", color=ROJO).scale(1.2)
        interr = self.palabra("?", AMBAR, 1.4).move_to([1.0, 3.1, 0])
        with self.narrar("b2"):
            # «los dos lados son iguales»
            self.en("iguales")
            self.corte()
            self.play(FadeIn(p1), FadeIn(eq), FadeIn(p2), run_time=self.dur(0.6))

            # «la parábola toca el eje»
            self.en("toca")
            self.play(Create(par.eje), Create(par.curva), run_time=self.dur(1.0))

            # «En el capítulo siete»
            self.en("cap7")
            self.play(FadeIn(c7), run_time=self.dur(0.4))

            # «rho igual a uno»
            self.en("rho1")
            self.pop(rho)

            # «una recta de la otra»
            self.en("recta")
            self.play(FadeIn(pts), Create(recta), FadeIn(l_rec), run_time=self.dur(1.0))

            # «Aquí es lo mismo»
            self.en("mismo")
            self.play(FadeOut(pts), FadeOut(recta), FadeOut(l_rec), run_time=0.4)

            # «una copia exacta de la voz»
            self.en("copia")
            self.play(Create(Lv.base()), Create(cv), Create(cm), run_time=self.dur(1.0), rate_func=linear)

            # «sin nada de azar añadido»
            self.en("sinazar")
            self.play(FadeIn(l_sin), run_time=self.dur(0.4))

            # «Cuanto más ruido añada la sala»
            self.en("ruido")
            self.play(Create(Lr.base()), Create(cr), run_time=self.dur(0.9), rate_func=linear)

            # «más se separarán los dos lados»
            self.en("separan")
            mayor.move_to(eq)
            self.play(ReplacementTransform(eq, mayor), par.curva.animate.shift(UP * 0.5), run_time=self.dur(0.9))

            # «Y eso tiene una medida»
            self.en("medida")
            self.pop(interr)
