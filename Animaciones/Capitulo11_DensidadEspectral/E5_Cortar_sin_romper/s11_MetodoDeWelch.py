"""Escena 11 — Método de Welch: restar la media, trozos solapados, ventana de Hann, promedio; por qué solapar (8 → 15 trozos)."""
from comun.escena import *


class MetodoDeWelch(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        textos = ["restar la media", "trozos solapados a la mitad", "ventana de Hann", "promediar"]
        fs = fichas(textos, AMBAR, ancho=4.6, alto=0.8, escala=0.5, buff=0.3, encendidas=True).move_to([-4.3, 0.3, 0])
        for f in fs:
            f.save_state()
            f.fade(0.7)
        Lr = Lienzo(ancho=8.0, alto=0.9, t_rango=(0, 7.2), v_max=1.0, centro=(2.2, 2.9))
        L = Lienzo(ancho=8.0, alto=0.9, t_rango=(0, 7.2), v_max=1.0, centro=(2.2, 0.9))
        t = np.linspace(0, 7.2, 300)
        reg = Lr.curva(t, 0.45 * serie(5, 300, 0.7), SENAL, 2.6).shift(UP * 0.35)
        _, marcos, campanas = trozos_solapados(L, n=5, largo=2.4, paso=1.2, alto=0.9)
        welch = self.palabra("método de Welch", AMBAR, 0.75).move_to([-4.3, 3.0, 0])
        # periodogramas de cada trozo y su promedio
        n = 70
        xs = np.linspace(-2.7, 2.7, n)
        cx, cy, alto = 2.4, -2.5, 1.5
        curvas = VGroup(*[espectro_ruidoso((cx, cy), 5.4, alto, semilla=s, color=RUIDO, n=n).set_stroke(opacity=0.6)
                          for s in (1, 2, 3, 4, 5)])
        liso = traza(cx + xs, cy - alto / 2 + 0.2 + 0.85 * alto * np.exp(-(xs / 1.5) ** 2), AMBAR, 4.5)
        base_e = Line([cx - 2.9, cy - alto / 2, 0], [cx + 2.9, cy - alto / 2, 0], color=INK, stroke_width=2)

        with self.narrar("b1"):
            # «todo lo que hemos visto»
            self.en("junta")
            self.play(LaggedStart(*[FadeIn(f, shift=RIGHT * 0.3) for f in fs], lag_ratio=0.25), run_time=self.dur(1.5))

            # «método de Welch»
            self.en("welch")
            self.pop(welch)

            # «Primero, se resta la media»
            self.en("media")
            self.play(Restore(fs[0]), Create(Lr.base()), Create(reg), run_time=self.dur(0.8))
            self.play(reg.animate.shift(DOWN * 0.35), run_time=self.dur(0.8))

            # «se parte la grabación en trozos»
            self.en("trozos")
            self.play(Restore(fs[1]), LaggedStart(*[Create(marcos[i]) for i in (0, 2, 4)], lag_ratio=0.3),
                      run_time=self.dur(1.2))

            # «se solapan por la mitad»
            self.en("solapan")
            self.play(LaggedStart(*[Create(marcos[i]) for i in (1, 3)], lag_ratio=0.3), run_time=self.dur(1.2))

            # «Tercero, a cada trozo»
            self.en("tercero")
            self.play(Restore(fs[2]), run_time=self.dur(0.6))

            # «una ventana de Hann»
            self.en("hann")
            self.play(LaggedStart(*[Create(c) for c in campanas], lag_ratio=0.2), run_time=self.dur(1.5))

            # «se promedian todos los periodogramas»
            self.en("promedia")
            self.play(Restore(fs[3]), Create(base_e), LaggedStart(*[Create(c) for c in curvas], lag_ratio=0.15),
                      run_time=self.dur(1.2))
            self.play(*[Transform(c, liso.copy()) for c in curvas], run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        Lr = Lienzo(ancho=9.0, alto=0.9, t_rango=(0, 3.6), v_max=1.0, centro=(0, 2.9))
        L = Lienzo(ancho=9.0, alto=0.9, t_rango=(0, 3.6), v_max=1.0, centro=(0, 0.9))
        t = np.linspace(0, 3.6, 240)
        reg = Lr.curva(t, 0.45 * serie(9, 240, 0.7), SENAL, 2.6)
        _, marcos, campanas = trozos_solapados(L, n=2, largo=2.4, paso=1.2, alto=0.9)
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.4).move_to([5.6, 1.0, 0])
        zonas = VGroup()
        for i in range(2):
            a = 1.2 * i
            yc = L.cy + (-0.56 if i % 2 else 0.56)
            for lado in (0, 1):
                x = float(L.x(a + (0.0 if lado == 0 else 2.4)))
                r = Rectangle(width=0.7, height=0.9, stroke_width=0, stroke_opacity=0).set_fill(ERROR, 0.3)
                r.move_to([x + (0.35 if lado == 0 else -0.35), yc, 0])
                zonas.add(r)
        ts = 2.3
        x_s = float(L.x(ts))
        yA = L.cy + 0.56 - 0.45 + valores_ventana("hann", 60)[int(60 * ts / 2.4)] * 0.81
        yB = L.cy - 0.56 - 0.45 + valores_ventana("hann", 60)[int(60 * (ts - 1.2) / 2.4)] * 0.81
        guia = DashedLine([x_s, 2.9, 0], [x_s, -0.15, 0], color=INK, stroke_width=2.5)
        dA = Dot([x_s, yA, 0], radius=0.1, color=AMBAR)
        dB = Dot([x_s, yB, 0], radius=0.1, color=VERDE)
        lab1 = etiqueta("sin solapar: 8 trozos", TXT, 0.55)
        lab2 = etiqueta("con solapamiento: 15", TXT, 0.55)
        lab1.move_to([-5.2 + lab1.width / 2 - 0.0, -1.2, 0])
        lab2.move_to([-5.2 + lab2.width / 2 - 0.0, -2.3, 0])
        fila1 = VGroup(*[Rectangle(width=1.2, height=0.4, color=CIAN, stroke_width=2).set_fill(CIAN, 0.18)
                         .move_to([-4.55 + 1.3 * i, -1.65, 0]) for i in range(8)])
        fila2 = VGroup(*[Rectangle(width=1.2, height=0.4, color=AMBAR, stroke_width=2).set_fill(AMBAR, 0.18)
                         .move_to([-4.55 + 0.65 * i, -2.75, 0]) for i in range(15)])
        raiz = formula(r"\sqrt{15/8}", r"\approx", r"1{,}4", escala=0.9, colores={2: AMBAR}).move_to([-1.3, -0.65, 0])
        modesta = etiqueta("mejora modesta", INK, 0.55).move_to([4.2, -0.65, 0])
        ok = tilde().scale(1.0).move_to([6.4, -0.65, 0])

        with self.narrar("b2"):
            # «¿Por qué solapar?»
            self.en("porque")
            self.corte()
            self.play(Create(Lr.base()), Create(reg), FadeIn(marcos), FadeIn(q), run_time=self.dur(0.8))

            # «aplasta los bordes de cada trozo»
            self.en("aplasta")
            self.play(FadeOut(q), LaggedStart(*[Create(c) for c in campanas], lag_ratio=0.3), run_time=self.dur(1.6))

            # «esas muestras casi no cuentan»
            self.en("nocuentan")
            self.play(FadeIn(zonas), run_time=self.dur(0.8))

            # «lo que en un trozo cae en el borde»
            self.en("borde")
            self.play(FadeOut(zonas), Create(guia), FadeIn(dA, scale=0.4), run_time=self.dur(0.7))

            # «en el siguiente cae en el centro»
            self.en("centro")
            self.play(FadeIn(dB, scale=0.4), run_time=self.dur(0.6))

            # «casi el doble de trozos»
            self.en("doble")
            self.play(FadeIn(lab1), LaggedStart(*[FadeIn(r) for r in fila1], lag_ratio=0.1), run_time=0.9)
            self.play(FadeIn(lab2), LaggedStart(*[FadeIn(r) for r in fila2], lag_ratio=0.05), run_time=self.dur(0.9))

            # «de ocho a quince»
            self.en("ocho_quince")
            self.play(Indicate(lab1, scale_factor=1.1, color=CIAN), Indicate(lab2, scale_factor=1.1), run_time=self.dur(0.8))

            # «se divide entre uno coma cuatro»
            self.en("raiz")
            self.play(FadeIn(raiz[0:2]), run_time=0.5)
            self.play(FadeIn(raiz[2]), run_time=self.dur(0.5))

            # «Una mejora modesta»
            self.en("modesta")
            self.play(FadeIn(modesta), run_time=self.dur(0.5))

            # «pero gratis»
            self.en("gratis")
            self.play(FadeIn(ok, scale=0.5), run_time=0.4)
