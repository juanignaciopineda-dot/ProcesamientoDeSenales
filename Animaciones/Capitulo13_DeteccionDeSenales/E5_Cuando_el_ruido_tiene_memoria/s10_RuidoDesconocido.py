"""Escena 10 — Ruido desconocido: aprenderlo de un tramo sin señal (Welch o un modelo pequeño)."""
from comun.escena import *


class RuidoDesconocido(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.pregunta()
        self.welch()
        self.modelo()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pregunta(self):
        P = PlanoV(centro=(-4.0, 0.5), lado=2.0, esc=1.0)
        el = DashedVMobject(P.elipse(0.6), num_dashes=24)
        q1 = Text("?", color=AMBAR, weight=BOLD).scale(0.9).move_to(P.c)
        L = lienzo_w(ancho=5.5, alto=1.8, base_y=-0.5, cx=3.5)
        eje = eje_w(L)
        curva = DashedVMobject(curva_f(L, lambda w: d_ruido(w, 0.6), 0, np.pi, color=RUIDO, ancho=4), num_dashes=40)
        q2 = Text("?", color=AMBAR, weight=BOLD).scale(0.9).move_to([L.x(1.7), L.y(1.0) + 0.6, 0])
        varianza = MathTex(r"\sigma^2 = ?", color=AMBAR).scale(1.0).move_to([0.0, -2.2, 0])
        quehace = Text("¿qué se hace?", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -3.3, 0])
        reg = traza(np.linspace(-6.0, 6.0, 140), 1.2 + 0.35 * ruido_ar(140, 0.6, 9), color=RUIDO, ancho=3)
        base = Line([-6.2, 1.2, 0], [6.2, 1.2, 0], color=INK, stroke_width=1.5)
        marco = Rectangle(width=3.0, height=1.5, color=INK, stroke_width=3).set_fill(INK, 0.18).move_to([0.0, 1.2, 0])
        solo = Text("solo ruido", color=RUIDO).scale(0.6).move_to([0.0, 2.5, 0])
        caja_r = caja("ruido", RUIDO, ancho=2.0, alto=0.8, scale=0.55).move_to([0.0, -1.0, 0])
        baja = flecha([0.0, 0.4, 0], [0.0, -0.5, 0], INK)
        c1 = Circle(radius=0.42, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.12).move_to([-3.2, -3.0, 0])
        n1 = Text("1", color=AMBAR, weight=BOLD).scale(0.6).move_to(c1)
        c2 = Circle(radius=0.42, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.12).move_to([3.2, -3.0, 0])
        n2 = Text("2", color=AMBAR, weight=BOLD).scale(0.6).move_to(c2)
        d1 = flecha([-0.5, -1.45, 0], [-2.7, -2.7, 0], INK)
        d2 = flecha([0.5, -1.45, 0], [2.7, -2.7, 0], INK)

        with self.narrar("b1"):
            # «no conocemos el ruido»
            self.en("noconoce")
            self.play(Create(P.ejes), FadeIn(P.rot0), FadeIn(P.rot1), Create(el), FadeIn(q1), run_time=self.dur(0.9))

            # «cómo se reparte en frecuencias»
            self.en("reparte")
            self.play(Create(eje.base), FadeIn(eje.rotulos), Create(curva), FadeIn(q2), run_time=self.dur(0.9))

            # «cuánto vale su varianza»
            self.en("varianza")
            self.play(FadeIn(varianza, shift=UP * 0.1), run_time=self.dur(0.6))

            # «¿Qué se hace?»
            self.en("quehace")
            self.pop(quehace)

            # «Se graba un tramo»
            self.en("graba")
            self.corte()
            self.play(Create(base), Create(reg), FadeIn(marco), run_time=self.dur(0.9))

            # «solo ruido»
            self.en("solo")
            self.play(FadeIn(solo, shift=DOWN * 0.1), run_time=self.dur(0.5))

            # «se aprende de él»
            self.en("aprende")
            self.play(GrowArrow(baja), FadeIn(caja_r), run_time=self.dur(0.7))

            # «dos cosas»
            self.en("dos")
            self.play(GrowArrow(d1), GrowArrow(d2), FadeIn(c1), FadeIn(n1), FadeIn(c2), FadeIn(n2),
                      run_time=self.dur(0.7))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def welch(self):
        c1 = Circle(radius=0.38, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.12).move_to([-6.2, 3.5, 0])
        n1 = Text("1", color=AMBAR, weight=BOLD).scale(0.55).move_to(c1)
        estimar = MathTex(r"D_{vv}\ ?", color=RUIDO).scale(0.9).move_to([-4.2, 3.5, 0])
        reg = traza(np.linspace(-6.0, 6.0, 140), 2.2 + 0.35 * ruido_ar(140, 0.6, 9), color=RUIDO, ancho=3)
        base = Line([-6.2, 2.2, 0], [6.2, 2.2, 0], color=INK, stroke_width=1.5)
        centros = [-4.2, -1.4, 1.4, 4.2]
        marcos = [Rectangle(width=3.4, height=1.3, stroke_width=3, color=AMBAR).set_fill(AMBAR, 0.1)
                  .move_to([cx, 2.2, 0]) for cx in centros]
        rng = np.random.default_rng(12)
        ws = np.linspace(0, np.pi, 40)
        ruidosas = []
        crudos = []
        for cx in centros:
            Lm = Lienzo(ancho=2.6, alto=0.9, t_rango=(0, np.pi), v_max=1.0, centro=(cx, 0.55))
            v = d_ruido(ws, 0.6) * rng.exponential(1.0, len(ws)) * 0.9
            crudos.append(v)
            ruidosas.append(Lm.curva(ws, np.clip(v, 0, 2.4), RUIDO, 2.5))
        K = 16
        medio = d_ruido(ws, 0.6)
        La = Lienzo(ancho=6.5, alto=1.0, t_rango=(0, np.pi), v_max=1.0, centro=(1.2, -2.5))
        var4 = np.mean(crudos, axis=0)
        var16 = 0.55 * medio + 0.45 * var4 * 0.4 + 0.0
        c_avg4 = La.curva(ws, np.clip(var4, 0, 1.6), RUIDO, 4)
        c_avg16 = La.curva(ws, np.clip(0.2 * var4 + 0.8 * medio, 0, 1.6), RUIDO, 4)
        medio_ancho = np.convolve(medio, np.ones(15) / 15, mode="same")
        c_borrosa = La.curva(ws, medio_ancho, RUIDO, 4)
        ejea = La.base(INK, 2.0)
        flechas_ = [Arrow([cx, 0.0, 0], [1.2 + 0.3 * (cx - 1.4) / 4.2, -1.6, 0], color=INK, stroke_width=3,
                          buff=0.05, max_tip_length_to_length_ratio=0.1) for cx in centros]
        wel = Text("Welch", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([5.9, -1.8, 0])
        H = MathTex("H", "=", "S^*", r"\big/", "D_{vv}", color=TXT).scale(0.9).move_to([-4.6, -2.3, 0])
        H[2].set_color(SENAL); H[4].set_color(RUIDO); H[0].set_color(ESTIMACION)
        mas = MathTex(r"\uparrow\ \text{trozos}", color=INK).scale(0.7).move_to([-4.6, -3.4, 0])
        res = Text("resolución", color=INK).scale(0.5).move_to([5.0, -3.4, 0])

        with self.narrar("b2"):
            # «La primera»
            self.en("primera")
            self.corte()
            self.pop(c1, n1)

            # «estimar la densidad espectral del ruido»
            self.en("estimar")
            self.play(FadeIn(estimar, shift=UP * 0.1), run_time=self.dur(0.6))

            # «se parte el registro en trozos»
            self.en("trozos")
            self.play(Create(base), Create(reg), run_time=self.dur(0.5))
            self.play(LaggedStart(*[FadeIn(m) for m in marcos], lag_ratio=0.3), run_time=self.dur(1.0))

            # «el periodograma de cada uno»
            self.en("periodo")
            self.play(LaggedStart(*[Create(c) for c in ruidosas], lag_ratio=0.25), run_time=self.dur(1.4))

            # «se promedian»
            self.en("promedian")
            self.play(*[GrowArrow(f) for f in flechas_], Create(ejea), Create(c_avg4), run_time=self.dur(1.2))

            # «el método de Welch»
            self.en("welch")
            self.pop(wel)

            # «Con eso se construye el filtro»
            self.en("filtro")
            self.play(FadeIn(H, shift=UP * 0.1), run_time=self.dur(0.8))

            # «más trozos, menos varianza»
            self.en("masmenos")
            self.play(FadeIn(mas), ReplacementTransform(c_avg4, c_avg16), run_time=self.dur(1.2))

            # «menos resolución»
            self.en("resol")
            self.play(FadeIn(res), ReplacementTransform(c_avg16, c_borrosa), run_time=self.dur(1.2))
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def modelo(self):
        c2 = Circle(radius=0.38, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.12).move_to([-6.2, 3.5, 0])
        n2 = Text("2", color=AMBAR, weight=BOLD).scale(0.55).move_to(c2)
        cm = caja("modelo", AZUL, ancho=2.0, alto=0.7, scale=0.5).move_to([-4.6, 3.5, 0])
        f = MathTex("x[n]", "=", "a", r"\,x[n-1]", "+", "w[n]", color=TXT).scale(1.1).move_to([0.6, 2.4, 0])
        f[2].set_color(AMBAR); f[3].set_color(TXT); f[5].set_color(RUIDO)
        coin = tira_pm1([1, -1, 1, -1, -1], lado=0.46, color=RUIDO, escala_txt=0.28).move_to([3.4, 1.1, 0])
        eco = MathTex("a = 0{,}6", color=AMBAR).scale(0.9).move_to([-4.6, 1.0, 0])
        coef = MathTex(r"\hat{a}\ =\ ?", color=AMBAR).scale(0.9).move_to([-4.9, -0.4, 0])
        lup = lupa(TXT).scale(0.9).move_to([-2.7, -0.4, 0])
        blq = MathTex("x[n]", "-", r"\hat{a}", r"\,x[n-1]", color=TXT).scale(1.0).move_to([1.0, -1.7, 0])
        blq[2].set_color(AMBAR)
        marco_b = SurroundingRectangle(blq, color=ESTIMACION, buff=0.28, stroke_width=3).set_fill(ESTIMACION, 0.08)
        r_term = SurroundingRectangle(VGroup(blq[2], blq[3]), color=AMBAR, buff=0.1, stroke_width=3)
        r_term.permitir_encima = True
        corto = traza(np.linspace(-5.8, -3.4, 30), -3.1 + 0.3 * ruido_ar(30, 0.6, 4), color=RUIDO, ancho=3)
        t_ok = tilde(VERDE, 1.0).move_to([5.8, 2.4, 0])

        with self.narrar("b3"):
            # «La segunda»
            self.en("segunda")
            self.corte()
            self.pop(c2, n2)

            # «un modelo con pocos coeficientes»
            self.en("modelo")
            self.play(FadeIn(cm), run_time=self.dur(0.5))

            # «Por ejemplo»
            self.en("ejemplo")
            self.play(FadeIn(f[0]), FadeIn(f[1]), run_time=self.dur(0.4))

            # «un cierto número por la anterior»
            self.en("a")
            self.play(FadeIn(f[2]), FadeIn(f[3]), run_time=self.dur(0.6))
            self.resaltar(f[2], color=AMBAR, escala=1.4)

            # «más una moneda»
            self.en("moneda")
            self.play(FadeIn(f[4]), FadeIn(f[5]), FadeIn(coin), run_time=self.dur(0.7))

            # «como en el eco del cero coma seis»
            self.en("eco")
            self.play(FadeIn(eco, shift=UP * 0.1), run_time=self.dur(0.6))

            # «estimar un coeficiente»
            self.en("coef")
            self.play(FadeIn(coef), FadeIn(lup), run_time=self.dur(0.7))

            # «el blanqueador sale directamente»
            self.en("blanq")
            self.play(FadeIn(blq, shift=UP * 0.1), Create(marco_b), run_time=self.dur(0.8))

            # «restar ese coeficiente por la muestra anterior»
            self.en("restar")
            self.play(Create(r_term), run_time=self.dur(0.6))

            # «Con registros cortos»
            self.en("cortos")
            self.play(Create(corto), run_time=self.dur(0.7))

            # «un modelo pequeño casi siempre gana»
            self.en("gana")
            self.play(Create(t_ok), run_time=self.dur(0.5))
