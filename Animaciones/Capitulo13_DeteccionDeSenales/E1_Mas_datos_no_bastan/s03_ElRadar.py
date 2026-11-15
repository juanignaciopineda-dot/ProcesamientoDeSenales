"""Escena 03 — El radar: ¿avión o ruido? Las dos hipótesis y sus probabilidades a priori."""
from comun.escena import *


class ElRadar(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.radar()
        self.hipotesis()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def radar(self):
        ant = antena(TXT).scale(2.0).move_to([-5.4, -0.6, 0])
        punta = ant[1].get_center()
        av = avion(SENAL).scale(1.7).move_to([4.2, 2.0, 0])
        L = Lienzo(ancho=8.2, alto=3.0, t_rango=(0, 1), v_max=2.0, centro=(0.4, 0.0))
        ruido = ruido_t(L, semilla=7, amp=1.0, ancho=3.4)
        etq_ruido = etiqueta("solo ruido", RUIDO, 0.95, BOLD).move_to([1.0, -2.75, 0])
        caja_dec = caja("decidir", AMBAR, ancho=3.2, alto=1.1, scale=0.85).move_to([-2.4, -3.3, 0])
        pregunta = Text("¿avión o ruido?", color=AMBAR, weight=BOLD).scale(1.3).move_to([0.5, 3.2, 0])
        si = Text("sí", color=VERDE, weight=BOLD).scale(1.3).move_to([-3.4, 3.2, 0])
        no = Text("no", color=ROJO, weight=BOLD).scale(1.3).move_to([4.4, 3.2, 0])
        capitulo = etiqueta("Capítulo 13 · Detección de señales", INK, 0.65).move_to([3.6, -3.6, 0])

        with self.narrar("b1"):
            # «lanza un pulso»
            self.en("pulso")
            self.play(FadeIn(VGroup(ant[0], ant[1])), run_time=self.dur(0.4))
            pulso = VGroup(*[Arc(radius=0.35 + 0.25 * i, start_angle=-PI / 5, angle=2 * PI / 5, color=SENAL,
                                 stroke_width=5).move_arc_center_to(punta + LEFT * (0.35 + 0.25 * i))
                             for i in range(3)])
            self.play(FadeIn(pulso, run_time=0.2))
            self.play(pulso.animate.shift(RIGHT * 6.5), run_time=self.dur(1.0))
            self.play(FadeOut(pulso), run_time=0.2)

            # «se queda escuchando»
            self.en("escucha")
            self.play(FadeIn(ant.ondas), run_time=self.dur(0.5))

            # «Si hay un avión»
            self.en("avion")
            self.play(FadeIn(av, shift=LEFT * 0.6), run_time=self.dur(0.6))

            # «vuelve un eco muy débil»
            self.en("eco")
            eco = Arc(radius=0.22, start_angle=PI - PI / 4, angle=PI / 2, color=SENAL, stroke_width=4)
            eco.move_to(av.get_center() + LEFT * 1.2 + DOWN * 0.5)
            self.add(eco)
            self.play(eco.animate.move_to(punta + RIGHT * 1.0), run_time=self.dur(1.4))

            # «escondido en el ruido»
            self.en("escondido")
            self.play(Create(ruido), run_time=self.dur(1.2))

            # «Si no hay nada»
            self.en("nada")
            self.play(FadeOut(av), FadeOut(eco), run_time=self.dur(0.5))

            # «solo se oye el ruido»
            self.en("solo")
            self.pop(etq_ruido)

            # «tiene que decidir»
            self.en("decidir")
            self.play(FadeIn(caja_dec, shift=UP * 0.2), run_time=self.dur(0.5))

            # «¿hay un avión o no?»
            self.en("pregunta")
            self.pop(pregunta)

            # «Ese sí o no»
            self.en("sino")
            self.pop(si, no)

            # «todo este capítulo»
            self.en("capitulo")
            self.play(FadeIn(capitulo), run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def hipotesis(self):
        c0 = RoundedRectangle(corner_radius=0.15, width=6.0, height=3.4, color=RUIDO, stroke_width=3,
                              fill_color=RUIDO, fill_opacity=0.08).move_to([-3.6, 0.9, 0])
        c1 = RoundedRectangle(corner_radius=0.15, width=6.0, height=3.4, color=SENAL, stroke_width=3,
                              fill_color=SENAL, fill_opacity=0.08).move_to([3.6, 0.9, 0])
        h0 = MathTex("H_0", color=RUIDO).scale(1.5).move_to(c0.get_top() + DOWN * 0.45)
        h1 = MathTex("H_1", color=SENAL).scale(1.5).move_to(c1.get_top() + DOWN * 0.45)
        L0 = Lienzo(ancho=5.0, alto=1.2, t_rango=(0, 1), v_max=2.0, centro=(-3.6, 0.9))
        L1 = Lienzo(ancho=5.0, alto=1.2, t_rango=(0, 1), v_max=2.0, centro=(3.6, 0.9))
        ruido0 = ruido_t(L0, semilla=7, amp=0.6, ancho=2.6)
        t = np.linspace(0, 1, 200)
        senal1 = L1.curva(t, 1.2 * np.exp(-((t - 0.5) / 0.12) ** 2), SENAL, 3.2)
        ruido1 = ruido_t(L1, semilla=9, amp=0.6, ancho=2.2, color=RUIDO)
        suma1 = L1.curva(t, 1.2 * np.exp(-((t - 0.5) / 0.12) ** 2) + 0.6 * serie(9, 200, 0.0), MEDIDA, 2.8)
        r0 = etiqueta("solo ruido", RUIDO, 0.7).move_to(c0.get_bottom() + UP * 0.3)
        r1 = etiqueta("señal + ruido", MEDIDA, 0.7).move_to(c1.get_bottom() + UP * 0.3)
        oido = Text("antes de escuchar", color=INK).scale(0.7).move_to([0, 3.4, 0])
        diez = casillas(10, rojas=(), centro=(0, -1.85), lado=0.55, hueco=0.1)
        diez.cas[3].set_color(SENAL).set_fill(SENAL, 0.7)
        p0 = MathTex("p_0", color=RUIDO).scale(1.3).next_to(c0, DOWN, buff=0.25)
        p1 = MathTex("p_1", color=SENAL).scale(1.3).next_to(c1, DOWN, buff=0.25)
        llave = DoubleArrow(c0.get_right(), c1.get_left(), buff=0.05, tip_length=0.2, color=INK, stroke_width=2)
        priori = self.palabra("a priori", AMBAR, 1.5).move_to([0, -2.95, 0])
        medir = etiqueta("antes de medir", INK, 0.7).move_to([0, -3.85, 0])

        with self.narrar("b2"):
            # «Démosle nombres»
            self.en("nombres")
            self.corte()
            self.play(Create(c0), Create(c1), run_time=self.dur(0.6))

            # «hache cero»
            self.en("h0")
            self.pop(h0)

            # «solo hay ruido»
            self.en("h0r")
            self.play(Create(ruido0), FadeIn(r0), run_time=self.dur(0.8))

            # «hache uno»
            self.en("h1")
            self.pop(h1)

            # «hay señal más ruido»
            self.en("h1r")
            self.play(Create(suma1), FadeIn(r1), run_time=self.dur(0.9))

            # «antes de escuchar nada»
            self.en("antes")
            self.play(FadeIn(oido), run_time=self.dur(0.4))

            # «aviones hay pocos»
            self.en("pocos")
            self.play(FadeIn(diez, lag_ratio=0.1), run_time=self.dur(0.9))

            # «Esas dos probabilidades de partida»
            self.en("partida")
            self.play(FadeIn(llave), run_time=self.dur(0.4))

            # «pe cero y pe uno»
            self.en("ps")
            self.pop(p0, p1)

            # «probabilidades a priori»
            self.en("priori")
            self.pop(priori)

            # «antes de medir»
            self.en("medir")
            self.play(FadeIn(medir), run_time=self.dur(0.4))
        self.wait(0.3)
