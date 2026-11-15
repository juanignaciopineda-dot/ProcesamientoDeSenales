"""Escena 15 — Cierre: media y autocorrelación resumen el proceso; ¿y si solo importara la separación?"""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        Li = Lienzo(ancho=5.4, alto=2.6, t_rango=(0, 1), v_max=2.4, centro=(-3.7, 0.9))
        Ld = Lienzo(ancho=5.4, alto=2.6, t_rango=(0, 4), v_max=1.2, centro=(3.7, 0.9))
        t = np.linspace(0, 1, 200)
        tk = np.linspace(0, 4, 100)
        pila = pila_de_curvas(Li, 12, semilla=23, a=0.93, color=SENAL, opacidad=0.45, ancho=2.0, escala=0.4)
        with self.narrar("b1"):
            # «las dos funciones»
            self.en("dos_func")
            self.play(Create(Li.base()), Create(Ld.base()), run_time=self.dur(0.7))

            # «la media»
            self.en("media")
            media = Li.curva(t, 0.9 * np.cos(2 * np.pi * t), AMBAR, 5)
            self.play(Create(media), run_time=self.dur(0.9), rate_func=linear)

            # «alrededor de qué valor»
            self.en("alrededor")
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.05), run_time=self.dur(1.2))

            # «la autocorrelación»
            self.en("autoc")
            ac = Ld.curva(tk, 1.0 * np.exp(-tk), ESTIMACION, 5)
            self.play(Create(ac), run_time=self.dur(1.2), rate_func=linear)

            # «cuánto recuerda»
            self.en("recuerda")
            mem = Text("memoria", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([4.8, 2.6, 0])
            fl = flecha([4.2, 2.3, 0], [3.0, 1.6, 0], ESTIMACION, 3)
            self.pop(mem)
            self.play(GrowArrow(fl), run_time=0.4)

            # «dependen de dos instantes»
            self.en("dos_inst")
            self.corte()
            F = formula("R", "(", "t_1", ",", "t_2", ")", escala=1.3, colores={0: AMBAR}).move_to([0, 3.0, 0])
            self.pop(F)

            # «cada pareja»
            self.en("parejas")
            ejes_ = Axes(x_range=[0, 8, 1], y_range=[0, 8, 1], x_length=5.6, y_length=4.2,
                         axis_config={"color": INK, "stroke_width": 2, "include_ticks": False, "tip_width": 0.16,
                                      "tip_height": 0.16}).move_to([0, -0.4, 0])
            lx = formula("t_1", escala=0.7, color=INK).next_to(ejes_.x_axis.get_end(), DR, buff=0.1)
            ly = formula("t_2", escala=0.7, color=INK).next_to(ejes_.y_axis.get_end(), UR, buff=0.1)
            puntos = VGroup(*[Dot(ejes_.c2p(a + 0.5, b + 0.5), radius=0.07, color=SENAL)
                              for a in range(8) for b in range(8)])
            self.play(Create(ejes_), FadeIn(lx), FadeIn(ly), run_time=0.5)
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in puntos], lag_ratio=0.02), run_time=self.dur(2.4))

            # «sería interminable»
            self.en("interminable")
            self.play(puntos.animate.set_color(ERROR), run_time=0.4)
            inter = etiqueta("una cuenta por cada pareja", ERROR, 0.65).move_to([0, -3.3, 0])
            self.pop(inter)

            # «no importara cuándo miras»
            self.en("cuando")
            self.corte()
            L = Lienzo(ancho=9.0, alto=2.6, t_rango=(0, 1), v_max=3.0, centro=(0, 0.3))
            curva = L.curva(np.linspace(0, 1, 240), 1.3 * serie(24, 240, 0.93), SENAL, 3.5)
            c1 = L.vertical(0.2, AMBAR, 3.5)
            c2 = L.vertical(0.45, TXT, 3.5)
            base_l = L.base()
            self.play(Create(base_l), Create(curva), run_time=self.dur(0.6), rate_func=linear)
            self.play(Create(c1), Create(c2), run_time=0.3)
            self.play(c1.animate.shift(RIGHT * float(L.x(0.4) - L.x(0.2))),
                      c2.animate.shift(RIGHT * float(L.x(0.4) - L.x(0.2))), run_time=self.dur(1.2))

            # «cuánto separas»
            self.en("separas")
            llave = Brace(VGroup(c1, c2), DOWN, color=AMBAR)
            tau = formula(r"\tau", escala=1.0, colores={0: AMBAR}).next_to(llave, DOWN, buff=0.1)
            self.play(GrowFromCenter(llave), FadeIn(tau), run_time=self.dur(0.7))

            # «En el próximo episodio»
            self.en("proximo")
            prox = etiqueta("próximo episodio", INK, 0.6).move_to([0, 2.9, 0])
            self.play(FadeIn(prox, shift=DOWN * 0.15), run_time=0.4)

            # «da igual cuándo mires»
            self.en("titulo_e3")
            self.play(*[FadeOut(m) for m in (base_l, curva, c1, c2, llave, tau)], run_time=0.3)
            tit = self.palabra("Da igual cuándo mires", AMBAR, 1.3).move_to([0, -0.2, 0])
            self.pop(tit)
        self.wait(1.0)
        self.limpiar()
