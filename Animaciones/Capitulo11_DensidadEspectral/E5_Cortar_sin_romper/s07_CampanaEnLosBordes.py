"""Escena 07 — La ventana de Hann: multiplicar el trozo por una campana que baja a cero en los bordes; −13, −31 y −58 dB."""
from comun.escena import *


class CampanaEnLosBordes(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        cx = -0.8
        L1 = Lienzo(ancho=8.0, alto=1.6, t_rango=(0, 1), v_max=1.2, centro=(cx, 2.6))
        L2 = Lienzo(ancho=8.0, alto=1.6, t_rango=(0, 1), v_max=1.2, centro=(cx, 0.5))
        L3 = Lienzo(ancho=8.0, alto=1.6, t_rango=(0, 1), v_max=1.2, centro=(cx, -1.8))
        t = np.linspace(0, 1, 300, endpoint=False)
        osc = np.cos(2 * np.pi * 10.5 * t)
        h = valores_ventana("hann", 300)
        trozo = L1.curva(t, osc, SENAL, 3.0)
        corte_i = Line(L1.p(0, 0), L1.p(0, 1), color=ERROR, stroke_width=6)
        corte_d = Line(L1.p(1, 0), L1.p(1, -1), color=ERROR, stroke_width=6)
        campana = L2.curva(t, h, VERDE, 4.0)
        prod = L3.curva(t, osc * h, SENAL, 3.0)
        por = Text("×", color=TXT, weight=BOLD).scale(0.9).move_to([-5.7, 1.55, 0])
        igual = Text("=", color=TXT, weight=BOLD).scale(0.9).move_to([-5.7, -0.65, 0])
        d_i = Dot(L2.p(0, 0), radius=0.1, color=VERDE)
        d_d = Dot(L2.p(1, 0), radius=0.1, color=VERDE)
        p_i = Dot(L3.p(0, 0), radius=0.1, color=VERDE)
        p_d = Dot(L3.p(1, 0), radius=0.1, color=VERDE)

        L4 = Lienzo(ancho=12.0, alto=1.8, t_rango=(-1, 2), v_max=1.2, centro=(0, 0.4))
        tt = np.linspace(0, 1, 300, endpoint=False)
        copias = VGroup(*[L4.curva(tt + i, np.cos(2 * np.pi * 10.5 * tt) * h, SENAL, 2.6, 1.0 if i == 0 else 0.6)
                          for i in (-1, 0, 1)])
        ok1 = tilde().scale(1.1).move_to(L4.p(0, 0) + UP * 1.4)
        ok2 = tilde().scale(1.1).move_to(L4.p(1, 0) + UP * 1.4)
        vent = self.palabra("ventana", AMBAR, 1.3).move_to([0, 3.1, 0])
        hann = self.palabra("Hann", VERDE, 1.3).move_to([0, 2.15, 0])
        L5 = Lienzo(ancho=5.0, alto=1.3, t_rango=(0, 1), v_max=1.2, centro=(-2.8, -2.6))
        t5 = np.linspace(0, 1, 200)
        cos_ = L5.curva(t5, -np.cos(2 * np.pi * t5), INK, 3.5)
        lev = L5.curva(t5, 0.5 - 0.5 * np.cos(2 * np.pi * t5), VERDE, 4.0)
        lab_cos = etiqueta("coseno levantado", VERDE, 0.6).move_to([2.4, -2.6, 0])

        with self.narrar("b1"):
            # «En lugar de cortar de golpe»
            self.en("lugar")
            self.play(Create(L1.base()), Create(trozo), run_time=self.dur(0.9), rate_func=linear)
            self.play(Create(corte_i), Create(corte_d), run_time=self.dur(0.4))

            # «multiplicamos el trozo por una campana»
            self.en("mult")
            self.play(Create(L2.base()), FadeIn(por), run_time=self.dur(0.7))

            # «empieza en cero»
            self.en("cero_ini")
            self.play(FadeIn(d_i, scale=0.4), run_time=0.4)

            # «sube suave»
            self.en("sube")
            self.play(Create(campana), run_time=self.dur(1.0), rate_func=linear)

            # «vuelve a cero en los bordes»
            self.en("cero_fin")
            self.play(FadeIn(d_d, scale=0.4), run_time=0.4)

            # «el final y el principio del trozo valen los dos cero»
            self.en("ambos")
            self.play(FadeIn(igual), Create(L3.base()), Create(prod), FadeOut(corte_i), FadeOut(corte_d),
                      run_time=self.dur(1.0))
            self.play(FadeIn(p_i, scale=0.4), FadeIn(p_d, scale=0.4), run_time=0.4)

            # «al pegarlos no hay salto»
            self.en("pegar")
            self.corte()
            self.play(Create(L4.base()), Create(copias[1]), run_time=0.5)
            self.play(FadeIn(copias[0]), FadeIn(copias[2]), run_time=0.5)
            self.play(FadeIn(ok1, scale=0.5), FadeIn(ok2, scale=0.5), run_time=self.dur(0.5))

            # «se la llama ventana»
            self.en("ventana")
            self.pop(vent)

            # «la de Hann»
            self.en("hann")
            self.pop(hann)

            # «coseno levantado»
            self.en("coseno")
            self.play(Create(L5.base()), Create(cos_), FadeIn(lab_cos), run_time=self.dur(0.7))
            self.play(Transform(cos_, lev), run_time=self.dur(1.2))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        X = 16
        L = lienzo_db(ancho=10.6, alto=5.0, x_max=X, top=2.4, cx=0.5)
        regla = regla_db(L, (0, -20, -40, -60, -80))
        curvas = {tp: curva_f(L, lambda x, tp=tp: nucleo_db(tp, x), 0, X, COLOR_VENTANA[tp], 3.0, n=1400)
                  for tp in ("rect", "hann", "blackman")}
        curvas["rect"].set_stroke(opacity=0.4)
        leyenda = {tp: etiqueta(NOMBRE_VENTANA[tp], COLOR_VENTANA[tp], 0.55).move_to([-1.8 + 3.0 * i, 3.5, 0])
                   for i, tp in enumerate(("rect", "hann", "blackman"))}
        picos = {tp: picos_laterales(tp, X)[0] for tp in ("rect", "hann", "blackman")}
        puntos = {tp: Dot(L.p(*picos[tp]), radius=0.09, color=COLOR_VENTANA[tp]) for tp in picos}
        etiq = {"rect": ("−13 dB", 1.2), "hann": ("−31 dB", 1.3), "blackman": ("−58 dB", 1.3)}
        rotulos = {tp: etiqueta(etiq[tp][0], COLOR_VENTANA[tp], 0.55).move_to(L.p(picos[tp][0], picos[tp][1]) + RIGHT * etiq[tp][1] + UP * 0.05)
                   for tp in picos}
        xd = 8.0
        debil = Line(L.p(xd, -80), L.p(xd, -60), color=CIAN, stroke_width=9)
        g60 = DashedLine(L.p(0, -60), L.p(X, -60), color=CIAN, stroke_width=3)
        t60 = etiqueta("−60 dB", CIAN, 0.55).move_to(L.p(13.0, -60) + UP * 0.3)
        ok = tilde().scale(1.0).move_to(L.p(xd, -50))
        lab_x = etiqueta("distancia al pico (bines)", INK, 0.45).move_to(L.p(X * 0.55, -80) + DOWN * 0.4)

        with self.narrar("b2"):
            # «El efecto en la fuga es enorme»
            self.en("enorme")
            self.corte()
            self.play(Create(regla), Create(curvas["rect"]), FadeIn(lab_x), run_time=self.dur(0.9))

            # «la ventana rectangular»
            self.en("rect")
            self.play(FadeIn(leyenda["rect"]), curvas["rect"].animate.set_stroke(opacity=1.0), FadeIn(puntos["rect"]),
                      run_time=self.dur(0.8))

            # «a menos trece decibelios»
            self.en("m13")
            self.play(FadeIn(rotulos["rect"]), run_time=self.dur(0.5))

            # «Con la de Hann»
            self.en("hann")
            self.play(Create(curvas["hann"]), FadeIn(leyenda["hann"]), run_time=self.dur(1.0))

            # «a menos treinta y uno»
            self.en("m31")
            self.play(FadeIn(puntos["hann"], scale=0.4), FadeIn(rotulos["hann"]), run_time=self.dur(0.6))

            # «la de Blackman»
            self.en("blackman")
            self.play(Create(curvas["blackman"]), FadeIn(leyenda["blackman"]), run_time=self.dur(1.0))

            # «a menos cincuenta y ocho»
            self.en("m58")
            self.play(FadeIn(puntos["blackman"], scale=0.4), FadeIn(rotulos["blackman"]), run_time=self.dur(0.6))

            # «el tono débil de antes»
            self.en("debil")
            self.play(Create(debil), run_time=self.dur(0.6))

            # «sesenta decibelios por debajo»
            self.en("m60")
            self.play(Create(g60), FadeIn(t60), run_time=self.dur(0.8))

            # «por fin tiene una oportunidad de asomar»
            self.en("asoma")
            self.play(FadeIn(ok, scale=0.5), run_time=self.dur(0.6))
