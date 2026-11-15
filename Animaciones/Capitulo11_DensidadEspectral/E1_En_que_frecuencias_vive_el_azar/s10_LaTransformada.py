"""Escena 10 — La transformada de Fourier recordada, la exponencial compleja y la definición de la densidad."""
from comun.escena import *


class LaTransformada(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        t = np.linspace(-3, 3, 240)
        r = autocorr_tele(t)
        L1 = Lienzo(ancho=8.0, alto=1.4, t_rango=(-3, 3), v_max=1.2, centro=(-0.8, 2.4))
        L2 = Lienzo(ancho=8.0, alto=1.4, t_rango=(-3, 3), v_max=1.2, centro=(-0.8, 0.6))
        L3 = Lienzo(ancho=8.0, alto=1.4, t_rango=(-3, 3), v_max=1.2, centro=(-0.8, -1.2))
        w = ValueTracker(0.8)
        curva_r = L1.curva(t, r, AZUL, 3.5)
        osc = always_redraw(lambda: L2.curva(t, np.cos(w.get_value() * t), CIAN, 3))
        prod = always_redraw(lambda: L3.curva(t, r * np.cos(w.get_value() * t), AMBAR, 3))
        area = always_redraw(lambda: area_bajo(L3, t, r * np.cos(w.get_value() * t), AMBAR, 0.35))
        rl = formula("R_{xx}(\\tau)", escala=0.9, colores={0: AZUL}).move_to([5.3, 2.4, 0])
        wl = formula(r"\omega", escala=1.1, colores={0: CIAN}).move_to([5.3, 0.6, 0])
        with self.narrar("b1"):
            # «Para cada frecuencia omega»
            self.en("omega")
            self.play(Create(L1.base()), Create(curva_r), FadeIn(rl), run_time=self.dur(1.0), rate_func=linear)
            self.pop(wl)

            # «por una oscilación de esa frecuencia»
            self.en("oscila")
            self.play(Create(L2.base()), FadeIn(osc), run_time=self.dur(0.9))

            # «el área del producto»
            self.en("producto")
            self.play(Create(L3.base()), FadeIn(prod), FadeIn(area), run_time=self.dur(0.9))

            # «mucho de esa frecuencia»
            self.en("mucho")
            g = etiqueta("área grande", VERDE, 0.6).move_to([5.3, -1.2, 0])
            self.pop(g)

            # «si no tiene nada»
            self.en("nada")
            self.play(w.animate.set_value(9.0), run_time=self.dur(1.2), rate_func=smooth)

            # «el área es cero»
            self.en("cero")
            z = etiqueta("área ≈ 0", ROJO, 0.6).move_to(g)
            self.play(ReplacementTransform(g, z), run_time=self.dur(0.4))

            # «frecuencia por frecuencia»
            self.en("freq")
            self.play(w.animate.set_value(1.5), run_time=self.dur(1.2), rate_func=linear)
            self.play(w.animate.set_value(5.0), run_time=self.dur(1.2), rate_func=linear)

            # «cuánto hay»
            self.en("cuanto")
            q = self.palabra("¿cuánto hay?", AMBAR, 0.8).move_to([0, -3.4, 0])
            self.pop(q)
        prod.clear_updaters()
        area.clear_updaters()
        osc.clear_updaters()

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        f = formula(r"e^{j\theta}", "=", r"\cos\theta", "+", r"j\sin\theta", escala=1.1,
                    colores={0: AMBAR}).move_to([-2.6, 1.6, 0])
        jj = MathTex("j", "=", r"\sqrt{-1}", color=TXT).scale(1.1).move_to([-4.4, -0.1, 0])
        jj[0].set_color(AMBAR)
        Lc = Lienzo(ancho=4.0, alto=1.2, t_rango=(0, 1), v_max=1.2, centro=(4.4, 1.8))
        Ls = Lienzo(ancho=4.0, alto=1.2, t_rango=(0, 1), v_max=1.2, centro=(4.4, -0.3))
        cf = caja("Fourier", AZUL, ancho=1.9, alto=0.9).move_to([-4.2, -2.2, 0])
        with self.narrar("b2"):
            # «una exponencial compleja»
            self.en("expo")
            self.corte()
            pal = self.palabra("exponencial compleja", AMBAR, 0.8).move_to([-2.6, 3.2, 0])
            self.pop(pal)

            # «e elevado a jota por un ángulo»
            self.en("ejt")
            self.play(FadeIn(f[0], shift=DOWN * 0.15), run_time=self.dur(0.7))

            # «la unidad imaginaria»
            self.en("imag")
            self.pop(jj[0])

            # «la raíz de menos uno»
            self.en("raiz")
            self.play(FadeIn(jj[1:]), run_time=self.dur(0.6))

            # «una forma compacta»
            self.en("compacta")
            self.play(FadeIn(f[1:], shift=DOWN * 0.15), run_time=self.dur(1.0))
            br = Brace(f[1:], DOWN, color=INK)
            br.permitir_encima = True
            self.play(Create(br), run_time=0.4)

            # «un coseno y un seno a la vez»
            self.en("cosen")
            self.resaltar(f[2], f[4], color=AMBAR)

            # «Así la transformada mide»
            self.en("mide")
            a = flecha([-3.2, -2.2, 0], [-2.3, -2.2, 0])
            self.play(FadeIn(cf), GrowArrow(a), run_time=self.dur(0.6))

            # «las dos oscilaciones»
            self.en("dos")
            self.play(Create(Lc.base()), Create(coseno(Lc, 0, 1.0, CIAN)), run_time=self.dur(0.8), rate_func=linear)
            self.play(Create(Ls.base()), Create(seno_t(Ls, 1, 1.0, AMBAR)), run_time=self.dur(0.8), rate_func=linear)
            lc = etiqueta("coseno", CIAN, 0.5).move_to([4.4, 2.8, 0])
            ls = etiqueta("seno", AMBAR, 0.5).move_to([4.4, 0.75, 0])
            self.play(FadeIn(lc), FadeIn(ls), run_time=0.3)

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        R = formula("R_{xx}(\\tau)", escala=1.1, colores={0: AZUL}).move_to([-5.0, 1.7, 0])
        rect = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.0, color=AMBAR, stroke_width=3).move_to([0.4, 1.7, 0])
        a1 = flecha([-4.1, 1.7, 0], [-2.5, 1.7, 0])
        S = MathTex("S_{xx}(j\\omega)", "=", "\\int", "R_{xx}(\\tau)", "e^{-j\\omega\\tau}", "\\,d\\tau",
                    color=TXT).scale(1.0).move_to([0, -0.2, 0])
        S[0].set_color(AMBAR)
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=6.5, alto=1.7, color=AMBAR, x_label=r"\omega") \
            .move_to([-0.8, -2.65, 0])
        with self.narrar("b3"):
            # «le pusimos nombre»
            self.en("nombre")
            self.corte()
            self.play(FadeIn(R), GrowArrow(a1), Create(rect), run_time=self.dur(0.8))

            # «densidad espectral de potencia»
            self.en("dep")
            nm = etiqueta("densidad espectral de potencia", TXT, 0.55).move_to(rect)
            self.pop(nm)

            # «ese sub equis equis de jota omega»
            self.en("s")
            self.play(FadeIn(S[0:2]), run_time=self.dur(0.6))

            # «la integral de la autocorrelación»
            self.en("integral")
            self.play(FadeIn(S[2:4]), run_time=self.dur(0.6))

            # «e elevado a menos jota omega tau»
            self.en("exp")
            self.play(FadeIn(S[4:]), run_time=self.dur(0.8))

            # «Una curva sobre el eje de frecuencias»
            self.en("curva")
            self.play(Create(c.ejes), FadeIn(c.etiquetas), Create(c.grafica), run_time=self.dur(1.2))

            # «Ahora vamos a ver»
            self.en("ahora")
            ar = flecha([5.0, -1.2, 0], [3.0, -2.2, 0], AMBAR, 3)
            self.play(GrowArrow(ar), run_time=0.4)

            # «por qué se merece ese nombre»
            self.en("merece")
            q = self.palabra("¿densidad?", AMBAR, 0.8).move_to([5.4, -0.8, 0])
            self.pop(q)
