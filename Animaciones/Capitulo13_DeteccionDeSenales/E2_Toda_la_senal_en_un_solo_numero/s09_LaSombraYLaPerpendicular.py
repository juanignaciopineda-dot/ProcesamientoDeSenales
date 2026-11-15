"""Escena 09 — g es la sombra de r sobre s; la parte perpendicular es ruido puro y no informa (suficiencia)."""
from comun.escena import *

O = np.array([-5.0, -1.6, 0.0])


def dirv(grados: float) -> np.ndarray:
    a = np.radians(grados)
    return np.array([np.cos(a), np.sin(a), 0.0])


class LaSombraYLaPerpendicular(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.sombra()
        self.nubes()
        self.suficiente()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def sombra(self):
        S = O + 3.8 * dirv(20)
        R = O + 4.6 * dirv(62)
        P = O + 3.42 * dirv(20)
        a_s = Arrow(O, S, buff=0, color=SENAL, stroke_width=7, max_tip_length_to_length_ratio=0.12)
        a_r = Arrow(O, R, buff=0, color=MEDIDA, stroke_width=7, max_tip_length_to_length_ratio=0.1)
        l_s = MathTex(r"s=(2,2,1)", color=SENAL).scale(0.95).move_to(S + LEFT * 0.2 + DOWN * 0.8)
        l_r = MathTex(r"r=(3,1,2)", color=MEDIDA).scale(0.95).move_to(R + UP * 0.45 + RIGHT * 0.25)
        basta = Text("¿por qué g basta?", color=AMBAR, weight=BOLD).scale(0.8).move_to([3.0, 3.4, 0])
        cap7 = Text("Capítulo 7", color=INK).scale(0.6).move_to([-5.9, 3.5, 0])
        escalar = formula("r", r"\cdot", "s", escala=1.4, colores={0: MEDIDA, 2: SENAL}).move_to([3.0, 1.9, 0])
        esge = MathTex("=g", color=AMBAR).scale(1.4).next_to(escalar, RIGHT, buff=0.15)
        proy = DashedLine(R, P, color=INK, stroke_width=3)
        som = Line(O, P, color=MEDIDA, stroke_width=12)
        som_t = Text("la sombra", color=MEDIDA).scale(0.6).move_to([-3.6, -2.35, 0])
        largo = formula("g", "=", r"|\text{sombra}|", r"\cdot", "|s|", escala=1.2,
                        colores={0: AMBAR, 2: MEDIDA, 4: SENAL}).move_to([3.0, 0.4, 0])
        self.geo = dict(O=O, S=S, R=R, P=P, a_s=a_s, a_r=a_r, l_s=l_s, l_r=l_r, proy=proy, som=som)

        with self.narrar("b1"):
            # «¿Por qué ge basta?»
            self.en("basta")
            self.pop(basta)

            # «lo recibido como una flecha con tres números»
            self.en("flecha_r")
            self.play(GrowArrow(a_r), FadeIn(l_r), run_time=self.dur(0.9))

            # «la señal como otra flecha fija»
            self.en("flecha_s")
            self.play(GrowArrow(a_s), FadeIn(l_s), run_time=self.dur(0.9))

            # «el capítulo siete»
            self.en("cap7")
            self.play(FadeIn(cap7), run_time=self.dur(0.4))

            # «el producto escalar de las dos»
            self.en("escalar")
            self.play(*[FadeIn(escalar[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.9))

            # «que es justo ge»
            self.en("esge")
            self.play(FadeIn(esge), run_time=self.dur(0.5))

            # «cuánto de una flecha cae en la dirección de la otra»
            self.en("cuanto")
            self.play(Create(proy), run_time=self.dur(0.9))

            # «la longitud de su sombra»
            self.en("sombra")
            self.play(Create(som), FadeIn(som_t), run_time=self.dur(0.8))

            # «multiplicada por la longitud de la señal»
            self.en("largo")
            self.play(*[FadeIn(largo[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.2))
        self.b1 = [basta, cap7, escalar, esge, largo, som_t, som]
        self.wait(0.2)

    # ------------------------------------------------------------ b2
    def nubes(self):
        g = self.geo
        P, R = g["P"], g["R"]
        self.play(*[FadeOut(m) for m in self.b1], run_time=0.3)
        par = Arrow(O, P, buff=0, color=MEDIDA, stroke_width=9, max_tip_length_to_length_ratio=0.12)
        per = Arrow(P, R, buff=0, color=RUIDO, stroke_width=9, max_tip_length_to_length_ratio=0.12)
        ang = Polygon(P, P + 0.35 * dirv(20), P + 0.35 * dirv(20) + 0.35 * dirv(110), P + 0.35 * dirv(110),
                      color=INK, stroke_width=3)
        gpar = MathTex("g", color=AMBAR).scale(1.5).move_to([-3.3, -2.2, 0])
        solo = Text("solo ruido", color=RUIDO, weight=BOLD).scale(0.65).move_to([-0.9, 1.5, 0])
        c0 = np.array([2.2, -0.5, 0.0])
        c1 = c0 + 3.4 * dirv(20)
        flechitas = VGroup(*[Arrow(c0, c0 + 0.9 * dirv(a), buff=0, color=RUIDO, stroke_width=3,
                                   max_tip_length_to_length_ratio=0.3) for a in range(0, 360, 45)])
        nube0 = nube_de_puntos(c0[:2], 1.25, 90, 5, RUIDO)
        nube1 = nube_de_puntos(c1[:2], 1.25, 90, 5, SENAL)
        h0 = MathTex("H_0", color=RUIDO).scale(1.2).move_to(c0 + UP * 1.6)
        h1 = MathTex("H_1", color=SENAL).scale(1.2).move_to(c1 + UP * 1.6)
        desp = Arrow(c0 + DOWN * 1.6, c1 + DOWN * 1.6, buff=0, color=AMBAR, stroke_width=5)
        desp_l = MathTex("s", color=SENAL).scale(1.1).move_to((c0 + c1) / 2 + DOWN * 2.1)
        centro = (c0 + c1) / 2
        plano = DashedLine(centro - 1.8 * dirv(110), centro + 1.8 * dirv(110), color=ESTIMACION, stroke_width=3)
        corte0 = Circle(radius=0.55, color=RUIDO, stroke_width=5).move_to([3.0, -3.2, 0])
        corte1 = Circle(radius=0.55, color=SENAL, stroke_width=5).move_to([4.6, -3.2, 0])
        self.g2 = [par, per, ang, gpar, solo, nube0, nube1, h0, h1, desp, desp_l, plano, corte0, corte1, flechitas]

        with self.narrar("b2"):
            # «se descompone en dos partes»
            self.en("dos")
            self.play(FadeOut(g["a_r"]), FadeOut(g["proy"]), FadeIn(par), FadeIn(per), run_time=self.dur(0.9))

            # «la que va en la dirección de la señal»
            self.en("paralela")
            self.play(Indicate(par, color=AMBAR, scale_factor=1.0), run_time=self.dur(0.8))

            # «perpendicular a ella»
            self.en("perp")
            self.play(Create(ang), Indicate(per, color=AMBAR, scale_factor=1.0), run_time=self.dur(0.8))

            # «Ge es la parte paralela»
            self.en("gpar")
            self.play(FadeIn(gpar), run_time=self.dur(0.5))

            # «¿Qué pasa con la perpendicular?»
            self.en("quepasa")
            self.play(Indicate(per, color=AMBAR, scale_factor=1.0), run_time=self.dur(0.8))

            # «Sale solo del ruido»
            self.en("solo")
            self.play(FadeIn(solo, shift=UP * 0.1), run_time=self.dur(0.6))

            # «no distingue direcciones»
            self.en("direcciones")
            self.play(LaggedStart(*[GrowArrow(a) for a in flechitas], lag_ratio=0.08), run_time=self.dur(1.2))

            # «una nube esférica»
            self.en("nube")
            self.play(FadeOut(flechitas), FadeIn(nube0), FadeIn(h0), run_time=self.dur(1.0))

            # «La señal la desplaza»
            self.en("desplaza")
            self.play(TransformFromCopy(nube0, nube1), FadeIn(h1), run_time=self.dur(1.2))

            # «en la dirección de la señal»
            self.en("direccion")
            self.play(GrowArrow(desp), FadeIn(desp_l), run_time=self.dur(0.7))

            # «las dos nubes son idénticas»
            self.en("identicas")
            self.play(Create(plano), run_time=self.dur(0.6))
            self.play(FadeIn(corte0), FadeIn(corte1), run_time=self.dur(0.4))
            self.play(corte0.animate.move_to([3.8, -3.2, 0]), corte1.animate.move_to([3.8, -3.2, 0]),
                      run_time=self.dur(0.8))
        self.wait(0.2)

    # ------------------------------------------------------------ b3
    def suficiente(self):
        g = self.geo
        par, per, ang, gpar, solo, nube0, nube1, h0, h1, desp, desp_l, plano, corte0, corte1, flechitas = self.g2
        aviones = VGroup(avion(AZUL).scale(0.45), avion(INK).scale(0.45)).arrange(RIGHT, buff=0.5).move_to([3.8, -2.2, 0])
        tachado_av = tachado(aviones[1], ROJO)
        no_info = Text("no informa", color=ERROR, weight=BOLD).scale(0.65).move_to([-0.9, 1.5, 0])
        suf = Text("estadístico suficiente", color=AMBAR, weight=BOLD).scale(0.85).move_to([2.8, 3.3, 0])
        info = Text("toda la información", color=VERDE, weight=BOLD).scale(0.75).move_to([2.8, 2.3, 0])
        bal = Balanza(centro=(2.3, 0.4), semi=1.1)
        sumcuad = formula(r"\sum r^2", escala=1.3, colores={0: MEDIDA}).move_to([5.3, 0.4, 0])
        vimos = Text("ya lo vimos", color=INK).scale(0.6).move_to([5.3, -0.6, 0])

        with self.narrar("b3"):
            # «la misma distribución»
            self.en("misma")
            self.play(FadeOut(nube0), FadeOut(nube1), FadeOut(h0), FadeOut(h1), FadeOut(desp), FadeOut(desp_l),
                      FadeOut(plano), run_time=self.dur(0.5))

            # «si hay avión o no»
            self.en("avion")
            self.play(FadeIn(aviones), run_time=self.dur(0.5))
            self.play(Create(tachado_av), run_time=self.dur(0.4))

            # «No aporta nada para decidir»
            self.en("nada")
            self.play(FadeOut(solo), FadeIn(no_info), run_time=self.dur(0.5))

            # «Tirarla no cuesta nada»
            self.en("tirar")
            self.play(FadeOut(per), FadeOut(ang), FadeOut(no_info), run_time=self.dur(0.8))

            # «Todo lo que sirve está en ge»
            self.en("todo")
            self.play(Indicate(par, color=AMBAR, scale_factor=1.0), Indicate(gpar, color=AMBAR, scale_factor=1.3),
                      run_time=self.dur(0.9))

            # «Eso es lo que significa»
            self.en("significa")
            self.play(FadeOut(corte0), FadeOut(corte1), FadeOut(aviones), FadeOut(tachado_av), run_time=0.3)
            self.play(FadeIn(suf, shift=DOWN * 0.1), run_time=self.dur(0.6))

            # «toda la información relevante»
            self.en("info")
            self.play(FadeIn(info, shift=DOWN * 0.1), run_time=self.dur(0.6))

            # «ni más ni menos»
            self.en("nimas")
            self.play(FadeIn(bal), run_time=self.dur(0.7))

            # «Y ya vimos la señal de esto»
            self.en("vimos")
            self.play(FadeIn(sumcuad), FadeIn(vimos), run_time=self.dur(0.7))

            # «la suma de cuadrados se canceló»
            self.en("cancelo")
            self.play(Create(tachado(sumcuad)), run_time=self.dur(0.6))
        self.wait(0.2)
