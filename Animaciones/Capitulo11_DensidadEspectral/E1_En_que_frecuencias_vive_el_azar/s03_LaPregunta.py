"""Escena 03 — La pregunta: voz, murmullo, filtro; y Fourier con dos senos."""
from comun.escena import *


class LaPregunta(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        L1 = Lienzo(ancho=4.2, alto=1.3, t_rango=(0, 4), v_max=1.0, centro=(-3.6, 2.5))
        L2 = Lienzo(ancho=4.2, alto=1.3, t_rango=(0, 4), v_max=1.0, centro=(-3.6, 0.8))
        L3 = Lienzo(ancho=4.2, alto=1.3, t_rango=(0, 4), v_max=1.0, centro=(-3.6, -1.3))
        voz = voz_t(L1, puntos=200)
        mur = ruido_t(L2, semilla=4, amp=0.3, puntos=200)
        mezcla = L3.curva(np.linspace(0, 4, 200), voz_valores(200) + 0.3 * serie(4, 200, 0.0), MEDIDA, 2.6)
        pers = persona(AZUL).scale(1.1).move_to([-6.45, 2.5, 0])
        with self.narrar("b1"):
            # «alguien habla»
            self.en("voz")
            self.play(FadeIn(pers), Create(L1.base()), Create(voz), run_time=self.dur(1.2), rate_func=linear)

            # «un murmullo constante»
            self.en("murmullo")
            self.play(Create(L2.base()), Create(mur), run_time=self.dur(1.0), rate_func=linear)

            # «Queremos limpiarla»
            self.en("limpiar")
            self.play(Create(L3.base()), Create(mezcla), run_time=self.dur(0.9), rate_func=linear)
            a1 = flecha([-1.3, -1.3, 0], [-0.55, -1.3, 0])
            q = self.palabra("?", AMBAR, 1.4).move_to([2.2, -1.3, 0])
            self.play(GrowArrow(a1), run_time=0.3)
            self.pop(q)

            # «una herramienta de Señales y Sistemas»
            self.en("herramienta")
            ss = etiqueta("Señales y Sistemas", INK, 0.5).move_to([0.3, -0.35, 0])
            self.play(FadeIn(ss), run_time=self.dur(0.4))

            # «el filtro»
            self.en("filtro")
            col = colador(CIAN, 1.2, 0.95).move_to([0.3, -1.3, 0])
            a2 = flecha([0.95, -1.3, 0], [1.6, -1.3, 0])
            self.play(FadeIn(col, scale=0.7), GrowArrow(a2), run_time=self.dur(0.5))
            self.sfx("pop")

            # «un colador que deja pasar unas frecuencias»
            self.en("colador")
            pasan = VGroup(*[Dot([-0.5 - 0.45 * i, -1.3 + 0.18 * (i - 1), 0], radius=0.07, color=AZUL) for i in range(3)])
            rebotan = VGroup(*[Dot([-0.5 - 0.45 * i, -1.3 + 0.35 * (1 - i), 0], radius=0.07, color=MAGENTA) for i in range(3)])
            self.play(FadeIn(pasan), FadeIn(rebotan), run_time=0.25)
            self.play(pasan.animate.shift(RIGHT * 2.4), rebotan.animate(rate_func=there_and_back).shift(RIGHT * 0.5),
                      run_time=self.dur(1.0))

            # «y retiene otras»
            self.en("retiene")
            self.play(rebotan.animate.set_color(ROJO), run_time=0.4)

            # «hay que saber algo antes»
            self.en("saber")
            self.play(FadeOut(pasan), FadeOut(rebotan), q.animate.scale(1.25), run_time=self.dur(0.5))

            # «en qué frecuencias vive la voz»
            self.en("vive_voz")
            eje = Arrow([1.6, 1.2, 0], [6.9, 1.2, 0], color=INK, stroke_width=2.5, buff=0,
                        max_tip_length_to_length_ratio=0.05)
            ef = etiqueta("frecuencia", INK, 0.45).move_to([5.4, 0.8, 0])
            lv = self.palabra("voz  ?", AZUL, 0.7).move_to([3.0, 2.1, 0])
            self.play(Create(eje), FadeIn(ef), run_time=self.dur(0.5))
            self.pop(lv)

            # «y en cuáles vive el ruido»
            self.en("vive_ruido")
            lr = self.palabra("ruido  ?", MAGENTA, 0.7).move_to([5.6, 2.1, 0])
            self.pop(lr)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        L = Lienzo(ancho=5.2, alto=1.2, t_rango=(0, 1), v_max=1.2, centro=(-3.3, 2.6))
        Lr = Lienzo(ancho=5.2, alto=1.2, t_rango=(0, 1), v_max=1.2, centro=(-3.3, 0.9))
        Ls = Lienzo(ancho=5.2, alto=1.6, t_rango=(0, 1), v_max=2.2, centro=(-3.3, -1.4))
        lento = seno_t(L, 2, 1.0, SENAL)
        rapido = seno_t(Lr, 5, 1.0, CIAN)
        t = np.linspace(0, 1, 260)
        suma = Ls.curva(t, np.sin(2 * np.pi * 2 * t) + np.sin(2 * np.pi * 5 * t), AMBAR, 3.2)
        barras = BarrasF([2, 5], [1.0, 1.0], f_max=7, ancho=4.4, alto=1.8, centro=(4.4, -1.4), rotulos=["2 Hz", "5 Hz"])
        cf = caja("Fourier", AZUL, ancho=1.9, alto=0.8).move_to([0.9, -1.4, 0])
        with self.narrar("b2"):
            # «un seno lento»
            self.en("lento")
            self.corte()
            self.play(Create(L.base()), Create(lento), run_time=self.dur(1.0), rate_func=linear)

            # «dos veces por segundo»
            self.en("dos")
            t2 = etiqueta("2 por segundo", SENAL, 0.55).move_to([1.3, 2.6, 0])
            self.pop(t2)

            # «súmale uno rápido»
            self.en("rapido")
            self.play(Create(Lr.base()), Create(rapido), run_time=self.dur(1.0), rate_func=linear)

            # «cinco veces por segundo»
            self.en("cinco")
            t5 = etiqueta("5 por segundo", CIAN, 0.55).move_to([1.3, 0.9, 0])
            self.pop(t5)

            # «La suma tiene una forma rara»
            self.en("suma")
            self.play(Create(Ls.base()), Create(suma), run_time=self.dur(1.2), rate_func=linear)

            # «difícil de leer»
            self.en("dificil")
            q = self.palabra("?", AMBAR, 1.2).move_to([0.0, -1.4, 0])
            self.pop(q)

            # «la transformada de Fourier»
            self.en("fourier")
            self.play(FadeOut(q), FadeIn(cf), run_time=self.dur(0.5))

            # «la desarma»
            self.en("desarma")
            a = flecha([1.9, -1.4, 0], [2.4, -1.4, 0])
            self.play(GrowArrow(a), Create(barras.base), run_time=self.dur(0.5))

            # «un seno de dos hercios»
            self.en("b2hz")
            self.play(Create(barras.barras[0]), FadeIn(barras.puntas[0]), FadeIn(barras.rot[0]), run_time=self.dur(0.6))

            # «y otro de cinco»
            self.en("b5hz")
            self.play(Create(barras.barras[1]), FadeIn(barras.puntas[1]), FadeIn(barras.rot[1]), run_time=self.dur(0.6))

            # «Un hercio es una vez por segundo»
            self.en("hercio")
            h = etiqueta("1 Hz = 1 vez por segundo", TXT, 0.6).move_to([0, -3.4, 0])
            self.pop(h)
