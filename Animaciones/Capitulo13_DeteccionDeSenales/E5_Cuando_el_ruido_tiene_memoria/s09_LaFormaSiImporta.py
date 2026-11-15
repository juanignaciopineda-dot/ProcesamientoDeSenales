"""Escena 09 — La forma sí importa: el pulso rápido gana cuatro veces al lento; la letra pequeña."""
from comun.escena import *


class LaFormaSiImporta(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.tabla()
        self.espectro()
        self.diseno()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def tabla(self):
        A = Tallos([1, 1], centro=(-5.3, 1.45), paso=0.9, unidad=0.6, color=SENAL)
        B = Tallos([1, -1], centro=(-5.3, 0.3), paso=0.9, unidad=0.6, color=SENAL)
        la = MathTex(r"(1,\ 1)", color=SENAL).scale(0.9).move_to([-3.4, 1.7, 0])
        lb = MathTex(r"(1,\ -1)", color=SENAL).scale(0.9).move_to([-3.4, 0.3, 0])
        lc = Text("ruido blanco", color=RUIDO).scale(0.5).move_to([-4.6, -1.1, 0])
        hd = MathTex("d^2", color=AMBAR).scale(0.9).move_to([1.9, 2.7, 0])
        ra = MathTex("2^2=4", "/", num_tex(3.2), "=", num_tex(1.25), color=TXT).scale(1.0).move_to([1.9, 1.7, 0])
        rb = MathTex("4", "/", num_tex(0.8), "=", "5", color=TXT).scale(1.0).move_to([1.9, 0.3, 0])
        rc = MathTex("2", color=TXT).scale(0.9).move_to([1.9, -1.1, 0])
        he = MathTex("P_e", color=ERROR).scale(0.9).move_to([5.9, 2.7, 0])
        pa = MathTex(num_tex(0.29), color=ERROR).scale(0.9).move_to([5.9, 1.7, 0])
        pb = MathTex(num_tex(0.13), color=ERROR).scale(0.9).move_to([5.9, 0.3, 0])
        pc = MathTex(num_tex(0.24), color=ERROR).scale(0.9).move_to([5.9, -1.1, 0])
        self.fila1 = [A.base, A.palito(0), A.palito(1), la, ra[0], ra[1], ra[2], ra[3], ra[4], pa]
        self.fila2 = VGroup(B, lb, rb, pb)
        self.res_rect = None

        with self.narrar("b1"):
            # «Para el pulso uno, uno»
            self.en("p11")
            self.play(Create(A.base), Create(A.palito(0)), Create(A.palito(1)), FadeIn(la), FadeIn(hd),
                      run_time=self.dur(0.7))

            # «al cuadrado cuatro»
            self.en("cuad")
            self.play(FadeIn(ra[0], shift=UP * 0.1), run_time=self.dur(0.5))

            # «entre tres coma dos»
            self.en("entre32")
            self.play(FadeIn(ra[1]), FadeIn(ra[2]), run_time=self.dur(0.5))

            # «uno coma veinticinco»
            self.en("r125")
            self.play(FadeIn(ra[3]), FadeIn(ra[4]), run_time=self.dur(0.5))

            # «Para el pulso uno, menos uno»
            self.en("p1m1")
            self.play(Create(B.base), Create(B.palito(0)), Create(B.palito(1)), FadeIn(lb), run_time=self.dur(0.7))

            # «cuatro entre cero coma ocho»
            self.en("entre08")
            self.play(*[FadeIn(rb[i]) for i in range(3)], run_time=self.dur(0.7))

            # «cinco»
            self.en("r5")
            self.play(FadeIn(rb[3]), FadeIn(rb[4]), run_time=self.dur(0.4))

            # «Con ruido blanco, los dos habrían dado dos»
            self.en("blanco")
            self.play(FadeIn(lc), FadeIn(rc), run_time=self.dur(0.6))

            # «Uno coma veinticinco, dos, cinco»
            self.en("lista")
            self.play(ra[4].animate(rate_func=there_and_back).scale(1.4),
                      rc.animate(rate_func=there_and_back).scale(1.4),
                      rb[4].animate(rate_func=there_and_back).scale(1.4), run_time=self.dur(1.2))

            # «los errores son»
            self.en("errores")
            self.play(FadeIn(he), run_time=self.dur(0.4))

            # «cero coma veintinueve»
            self.en("q29")
            self.play(FadeIn(pa, shift=UP * 0.1), run_time=self.dur(0.4))

            # «cero coma veinticuatro»
            self.en("q24")
            self.play(FadeIn(pc, shift=UP * 0.1), run_time=self.dur(0.4))

            # «cero coma trece»
            self.en("q13")
            self.play(FadeIn(pb, shift=UP * 0.1), run_time=self.dur(0.4))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def espectro(self):
        # la tabla sigue en pantalla para los cuatro primeros momentos
        marco = SurroundingRectangle(self.fila2, color=VERDE, buff=0.15, stroke_width=3)
        e2 = MathTex("E = 2", color=AMBAR).scale(0.9).move_to([-0.3, 2.7, 0])
        cuatro = MathTex(r"5\,/\,1{,}25 = 4", color=AMBAR).scale(0.95).move_to([1.9, -2.4, 0])
        L = lienzo_w(ancho=9.0, alto=3.0, base_y=-2.2)
        eje = eje_w(L)
        c_d = curva_f(L, lambda w: d_ruido(w, 0.6), 0, np.pi, color=RUIDO, ancho=4)
        c_r = curva_f(L, s2_rapido, 0, np.pi, color=SENAL, ancho=4)
        c_l = curva_f(L, s2_lento, 0, np.pi, color=AZUL, ancho=3)
        c_l.set_stroke(opacity=0.5)
        r_debil = Rectangle(width=L.x(np.pi) - L.x(2.3), height=3.0, stroke_width=0).set_fill(SENAL, 0.14)
        r_debil.move_to([(L.x(np.pi) + L.x(2.3)) / 2, L.y(0.0) + 1.5, 0])
        r_fuerte = Rectangle(width=L.x(0.9) - L.x(0), height=3.0, stroke_width=0).set_fill(RUIDO, 0.14)
        r_fuerte.move_to([(L.x(0.9) + L.x(0)) / 2, L.y(0.0) + 1.5, 0])
        # el cociente |S|² / D reescala cada curva
        piso = 0.12

        def rap(w):
            return s2_rapido(w) / (d_ruido(w, 0.6) + piso) / 5.6

        def len_(w):
            return s2_lento(w) / (d_ruido(w, 0.6) + piso) / 5.6

        a_r0 = area_f(L, s2_rapido, 0, np.pi, color=SENAL, opacidad=0.3)
        a_l0 = area_f(L, s2_lento, 0, np.pi, color=AZUL, opacidad=0.2)
        a_r1 = area_f(L, rap, 0, np.pi, color=SENAL, opacidad=0.45)
        a_l1 = area_f(L, len_, 0, np.pi, color=AZUL, opacidad=0.3)
        f_int = MathTex(r"\int", "|S|^2", r"\big/", "D_{vv}", color=TXT).scale(0.95).move_to([-2.0, 3.0, 0])
        f_int[1].set_color(SENAL); f_int[3].set_color(RUIDO)

        with self.narrar("b2"):
            # «el pulso rápido»
            self.en("rapido")
            self.play(Create(marco), run_time=self.dur(0.5))

            # «el mismo gasto de energía»
            self.en("gasto")
            self.play(FadeIn(e2), run_time=self.dur(0.5))

            # «cuatro veces mayor»
            self.en("cuatro")
            self.play(FadeIn(cuatro, shift=UP * 0.1), run_time=self.dur(0.6))

            # «que el lento»
            self.en("lento")
            self.play(*[m.animate.fade(0.7) for m in self.fila1], run_time=self.dur(0.5))

            # «donde el ruido es débil»
            self.en("debil")
            self.corte()
            self.play(Create(eje.base), FadeIn(eje.rotulos), Create(c_d), Create(c_r), run_time=self.dur(0.9))
            self.play(FadeIn(r_debil), run_time=self.dur(0.4))

            # «En frecuencia»
            self.en("frec")
            self.play(FadeOut(r_debil), Create(c_l), run_time=self.dur(0.8))

            # «la integral del cuadrado de la señal»
            self.en("integral")
            self.play(FadeIn(a_r0), FadeIn(a_l0), FadeIn(f_int[0]), FadeIn(f_int[1]), run_time=self.dur(0.9))

            # «dividido entre la densidad del ruido»
            self.en("dens")
            self.play(FadeIn(f_int[2]), FadeIn(f_int[3]), ReplacementTransform(a_r0, a_r1),
                      ReplacementTransform(a_l0, a_l1), run_time=self.dur(1.2))

            # «Cada frecuencia de la señal cuenta menos»
            self.en("cuenta")
            self.resaltar(a_l1, color=AMBAR, escala=1.05)

            # «donde el ruido es fuerte»
            self.en("fuerte")
            self.play(FadeIn(r_fuerte), run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def diseno(self):
        L = lienzo_w(ancho=9.0, alto=3.0, base_y=-2.2)
        eje = eje_w(L)
        c_d = curva_f(L, lambda w: d_ruido(w, 0.6), 0, np.pi, color=RUIDO, ancho=4)
        c_d2 = curva_f(L, lambda w: d_ruido(w, -0.6), 0, np.pi, color=RUIDO, ancho=4)
        c_r = curva_f(L, s2_rapido, 0, np.pi, color=SENAL, ancho=4)
        c_l = curva_f(L, s2_lento, 0, np.pi, color=VERDE, ancho=5)
        neg = MathTex("a = -0{,}6", color=AMBAR).scale(0.95).move_to([-5.0, 3.3, 0])
        zig = traza(np.linspace(3.0, 6.4, 40), 2.75 + 0.3 * ruido_ar(40, -0.85, 5), color=RUIDO, ancho=3)
        chica = Text("la forma no importa*", color=TXT, weight=BOLD).scale(0.6).move_to([0.2, 3.3, 0])
        solo = Text("*solo con ruido blanco", color=AMBAR).scale(0.5).move_to([0.2, 2.65, 0])
        lap = lapiz(AMBAR).scale(0.9).move_to([-4.8, -3.3, 0])
        av = avion_arriba(AZUL).scale(1.2).move_to([-1.8, -3.3, 0])
        an = antena(TXT).scale(0.7).move_to([0.5, -3.3, 0])
        area = area_f(L, s2_lento, 0, np.pi, color=AMBAR, opacidad=0.4)
        r_valle = Rectangle(width=L.x(1.0) - L.x(0), height=3.0, stroke_width=0).set_fill(VERDE, 0.14)
        r_valle.move_to([(L.x(1.0) + L.x(0)) / 2, L.y(0.0) + 1.5, 0])

        with self.narrar("b3"):
            # «memoria negativa»
            self.en("neg")
            self.corte()
            self.add(eje.base, eje.rotulos, c_d, c_r)
            self.play(FadeIn(neg, shift=UP * 0.1), run_time=self.dur(0.5))

            # «al revés»
            self.en("reves")
            self.play(ReplacementTransform(c_d, c_d2), run_time=self.dur(0.9))

            # «el ruido alterna»
            self.en("alterna")
            self.play(Create(zig), run_time=self.dur(0.8))

            # «una señal que no alterne»
            self.en("noalterne")
            self.play(c_r.animate.set_stroke(opacity=0.25), Create(c_l), run_time=self.dur(0.9))

            # «la letra pequeña»
            self.en("chica")
            self.pop(chica)

            # «solo con ruido blanco»
            self.en("blanco")
            self.play(FadeIn(solo, shift=UP * 0.1), run_time=self.dur(0.5))

            # «Cuando puedes diseñar la señal»
            self.en("disenar")
            self.play(FadeIn(lap, shift=UP * 0.2), run_time=self.dur(0.5))

            # «en un radar o en una comunicación»
            self.en("radar")
            self.play(FadeIn(av), FadeIn(an), run_time=self.dur(0.7))

            # «dónde poner la energía»
            self.en("energia")
            self.play(FadeIn(area), run_time=self.dur(0.7))

            # «donde el ruido es más débil»
            self.en("debil")
            self.play(FadeIn(r_valle), run_time=self.dur(0.5))
