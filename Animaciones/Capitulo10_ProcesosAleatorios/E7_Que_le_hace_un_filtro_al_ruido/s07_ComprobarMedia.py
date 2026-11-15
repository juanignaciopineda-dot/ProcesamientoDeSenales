"""Escena 07 — Comprobar la media con el sensor (media 20): promediador y filtro que resta."""
from comun.escena import *


class ComprobarMedia(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.comprobar()
        self.letra_pequena()

    # ------------------------------------------------------------------ b1
    def comprobar(self):
        t = np.linspace(0, 1, 120)
        x = serie(21, 120, 0.9)
        y_prom = np.convolve(x, [0.5, 0.5])[:120]
        y_res = np.convolve(x, [1, -1])[:120]
        # arriba: promediador; abajo: el filtro que resta
        Le = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=3.0, centro=(-4.7, 1.6))
        Ls = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=3.0, centro=(4.7, 1.6))
        Le2 = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=3.0, centro=(-4.7, -2.0))
        Ls2 = Lienzo(ancho=2.6, alto=1.4, t_rango=(0, 1), v_max=3.0, centro=(4.7, -2.0))
        ce = Le.curva(t, x, SENAL, 3.5)
        m_e = Le.curva([0, 1], [0, 0], AMBAR, 2.5)
        cs = Ls.curva(t, y_prom, MEDIDA, 3.5)
        m_s = Ls.curva([0, 1], [0, 0], AMBAR, 2.5)
        ce2 = Le2.curva(t, x, SENAL, 3.5)
        cs2 = Ls2.curva(t, y_res, MEDIDA, 3.5)
        m_s2 = Ls2.curva([0, 1], [0, 0], AMBAR, 2.5)
        term = termometro(alto=1.3).scale(0.8).move_to([-6.45, 1.6, 0])
        bl = BloqueLTI(r"\tfrac12,\tfrac12", centro=(0, 1.6), ancho=1.8, alto=1.1, largo=2.2, escala=0.75)
        bl2 = BloqueLTI(r"1,\,-1", centro=(0, -2.0), ancho=1.8, alto=1.1, largo=2.2, escala=0.75)
        mu_x = formula(r"\mu_x", "=", "20", escala=0.85, colores={0: AMBAR}).move_to([-4.7, 0.35, 0])
        g1 = formula("H(0)", "=", "1", escala=0.85).move_to([0, 0.45, 0])
        mu_y = formula(r"\mu_y", "=", "20", escala=0.85, colores={0: AMBAR}).move_to([4.7, 0.35, 0])
        par = VGroup(Dot(Le.p(0.4, 0.3), radius=0.08, color=AMBAR), Dot(Le.p(0.6, 0.3), radius=0.08, color=AMBAR))
        ok = tilde().scale(0.9).move_to([6.6, 0.4, 0])
        h2 = Tallos([1, -1], centro=(-2.2, -0.75), paso=0.5, unidad=0.35, color=ESTIMACION)
        h_cero = formula("H(0)", "=", "1-1", "=", "0", escala=0.85).move_to([0, -0.85, 0])
        mu_0 = formula(r"\mu_y", "=", "0", escala=0.85, colores={0: AMBAR}).move_to([4.7, -3.4, 0])
        otras = VGroup(*[Le2.curva(t, serie(30 + i, 120, 0.9), SENAL, 2.2, 0.55) for i in range(3)])
        otras_s = VGroup(*[Ls2.curva(t, np.convolve(serie(30 + i, 120, 0.9), [1, -1])[:120], MEDIDA, 2.2, 0.55) for i in range(3)])

        with self.narrar("b1"):
            # «el sensor»
            self.en("sensor")
            self.play(FadeIn(term), Create(ce), Create(m_e), FadeIn(bl), run_time=self.dur(0.8))

            # «La temperatura»
            self.en("temp")
            self.resaltar(ce, color=AMBAR, escala=1.05)

            # «media veinte»
            self.en("m20")
            self.play(FadeIn(mu_x), run_time=self.dur(0.5))

            # «ganancia uno»
            self.en("g1")
            self.play(FadeIn(g1), run_time=self.dur(0.5))

            # «la salida tiene media veinte»
            self.en("sale20")
            self.play(Create(cs), Create(m_s), FadeIn(mu_y), run_time=self.dur(0.8))

            # «Promediar dos temperaturas»
            self.en("promedio")
            self.play(FadeIn(par), run_time=self.dur(0.3))
            self.play(par[0].animate.move_to(Le.p(0.5, 0.3)), par[1].animate.move_to(Le.p(0.5, 0.3)), run_time=self.dur(0.6))

            # «no cambia la temperatura media»
            self.en("igual")
            self.play(FadeOut(par), FadeIn(ok, scale=0.6), run_time=self.dur(0.4))

            # «Y con el filtro»
            self.en("filtro")
            self.play(FadeIn(bl2), Create(ce2), run_time=self.dur(0.7))

            # «resta la muestra anterior»
            self.en("resta")
            self.resaltar(bl2.caja, color=AMBAR, escala=1.1)

            # «uno y menos uno»
            self.en("uno_menos")
            self.play(FadeIn(h2), run_time=self.dur(0.5))

            # «la ganancia en continua es cero»
            self.en("h_cero")
            self.play(FadeIn(h_cero), run_time=self.dur(0.8))

            # «la salida tiene media cero»
            self.en("m0")
            self.play(Create(cs2), Create(m_s2), FadeIn(mu_0), run_time=self.dur(0.8))

            # «sea cual sea la entrada»
            self.en("cual_sea")
            self.play(*[Create(c) for c in otras], run_time=self.dur(0.6))
            self.play(*[Create(c) for c in otras_s], run_time=self.dur(0.6))
        self.wait(1.0)

    # ------------------------------------------------------------------ b2
    def letra_pequena(self):
        bl = BloqueLTI(r"h", centro=(0, 2.4), ancho=1.6, alto=1.1, largo=2.4)
        Le = Lienzo(ancho=2.2, alto=0.6, t_rango=(0, 1), v_max=1.0, centro=(-4.0, 2.4))
        Ls = Lienzo(ancho=2.2, alto=0.6, t_rango=(0, 1), v_max=1.0, centro=(4.0, 2.4))
        rec_e = Le.curva([0, 1], [0, 0], AMBAR, 5)
        rec_s = Ls.curva([0, 1], [0, 0], AMBAR, 5)
        etq_e = formula(r"\mu_x", escala=0.8, colores={0: AMBAR}).next_to(rec_e, UP, buff=0.25)
        etq_s = formula(r"\mu_y", escala=0.8, colores={0: AMBAR}).next_to(rec_s, UP, buff=0.25)
        f_suma = formula(r"\sum_k h[k]", escala=1.0).move_to([-2.3, 0.7, 0])
        f_int = formula(r"\int h(v)\,dv", escala=1.0).move_to([2.3, 0.7, 0])
        fl = Arrow(f_suma.get_right() + RIGHT * 0.2, f_int.get_left() + LEFT * 0.2, color=AMBAR, buff=0, stroke_width=4)
        filas = VGroup(*[Line(LEFT * 0.9, RIGHT * 0.9, color=INK, stroke_width=4) for _ in range(4)]).arrange(DOWN, buff=0.15).move_to([0, -0.3, 0])
        nota_prof = nota("apunte en profundidad", 0.62).move_to([0, -1.2, 0])
        c_est = caja("sistema estable", VERDE, ancho=3.6, alto=0.8, scale=0.6).move_to([-4.2, -1.3, 0])
        c_fin = caja("varianza finita", VERDE, ancho=3.6, alto=0.8, scale=0.6).move_to([4.2, -1.3, 0])
        excl = Text("!", color=AMBAR, weight=BOLD).scale(1.3).move_to([0, -2.15, 0])
        c_cruz = caja("correlación cruzada", AZUL, ancho=3.6, alto=0.75, scale=0.6).move_to([-4.3, -2.9, 0])
        r_yx = formula(r"R_{yx}(\tau)", escala=0.95).move_to([-0.3, -2.9, 0])
        wss = caja("¿conjuntamente WSS? → ahora", AMBAR, ancho=5.8, alto=0.8, scale=0.6).move_to([4.0, -2.9, 0])
        sig = Arrow(wss.get_bottom() + DOWN * 0.05, wss.get_bottom() + DOWN * 0.75, color=AMBAR, buff=0, stroke_width=4)

        with self.narrar("b2"):
            # «atraviesa el sistema»
            self.en("atraviesa")
            self.corte()
            self.play(FadeIn(bl), Create(rec_e), FadeIn(etq_e), run_time=self.dur(0.6))
            self.play(Create(rec_s), FadeIn(etq_s), run_time=self.dur(0.5))

            # «como si fuera»
            self.en("como")
            self.play(rec_e.animate.set_stroke(width=8), run_time=self.dur(0.4))

            # «la parte que no cambia»
            self.en("constante")
            self.play(Indicate(etq_e, color=AMBAR), run_time=0.6)

            # «En tiempo continuo»
            self.en("continuo")
            self.play(FadeIn(f_suma), run_time=self.dur(0.4))

            # «la deducción es idéntica»
            self.en("identica")
            self.play(FadeIn(filas), run_time=self.dur(0.6))

            # «con una integral»
            self.en("integral")
            self.play(Create(fl), FadeIn(f_int), run_time=self.dur(0.6))

            # «la letra pequeña»
            self.en("pequena")
            self.play(FadeIn(nota_prof), run_time=self.dur(0.4))

            # «sea estable»
            self.en("estable")
            self.play(FadeIn(c_est), run_time=self.dur(0.4))

            # «varianza finita»
            self.en("finita")
            self.play(FadeIn(c_fin), run_time=self.dur(0.4))

            # «Y hay algo más»
            self.en("algo_mas")
            self.pop(excl)

            # «la correlación cruzada»
            self.en("cruzada")
            self.play(FadeIn(c_cruz), run_time=self.dur(0.4))

            # «solo depende de la separación»
            self.en("separacion")
            self.play(FadeIn(r_yx), FadeIn(wss), run_time=self.dur(0.6))

            # «Lo veremos»
            self.en("veremos")
            self.play(GrowArrow(sig), run_time=self.dur(0.4))

            # «la cuenta siguiente»
            self.en("siguiente")
            self.resaltar(wss, color=AMBAR, escala=1.06)

            # «que es la importante»
            self.en("importante")
            self.resaltar(sig, color=AMBAR, escala=1.3)
        self.wait(1.0)
        self.limpiar()
