"""Escena 08 — El problema del filtro: r[n] = s[n] + d[n], un filtro FIR para recuperar la señal."""
from comun.escena import *


class ElProblemaDelFiltro(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        titulo_ = self.palabra("el problema del curso", AMBAR, 0.6).move_to([0, 3.6, 0])
        term = termometro(alto=1.3, color=ROJO, nivel=0.6).scale(0.9).move_to([-6.2, 0.6, 0])
        suma = VGroup(Circle(radius=0.42, color=TXT, stroke_width=3).set_fill(FONDO, 1),
                      Text("+", color=TXT, weight=BOLD).scale(0.7)).move_to([-2.2, 0.7, 0])
        cable = Arrow([-5.6, 0.7, 0], [-2.65, 0.7, 0], buff=0, color=SENAL, stroke_width=4)
        salida = Arrow([-1.75, 0.7, 0], [0.9, 0.7, 0], buff=0, color=MEDIDA, stroke_width=4)
        lr = MathTex("r[n]", color=MEDIDA).scale(0.85).move_to([-0.4, 1.3, 0])
        ls = MathTex("s[n]", color=SENAL).scale(0.85).move_to([-4.2, 1.3, 0])
        mon = moneda("±1", RUIDO).scale(0.55).move_to([-2.2, 3.0, 0])
        ent_d = Arrow([-2.2, 2.45, 0], [-2.2, 1.15, 0], buff=0, color=RUIDO, stroke_width=4)
        ld = MathTex("d[n]", color=RUIDO).scale(0.85).move_to([-1.2, 1.95, 0])
        var1 = Text("media 0 · varianza 1", color=RUIDO).scale(0.45).move_to([2.4, 2.6, 0])
        indep = Text("no correlacionados", color=INK).scale(0.45).move_to([2.4, 1.9, 0])
        caja_h = caja("h", AMBAR, ancho=1.1, alto=0.9, scale=0.7).move_to([3.0, 0.7, 0])
        e1 = Arrow([0.95, 0.7, 0], [2.4, 0.7, 0], buff=0, color=MEDIDA, stroke_width=4)
        e2 = Arrow([3.55, 0.7, 0], [5.3, 0.7, 0], buff=0, color=ESTIMACION, stroke_width=4)
        lsh = MathTex(r"\hat s[n]", color=ESTIMACION).scale(0.85).move_to([6.1, 0.7, 0])

        t = np.linspace(0, 1, 200)
        s_ = 1.0 * serie(14, 200, 0.97)
        d_ = 0.6 * np.random.default_rng(7).normal(0, 1, 200)
        Ls = Lienzo(ancho=3.8, alto=1.4, t_rango=(0, 1), v_max=2.4, centro=(-4.6, -2.3))
        Ld = Lienzo(ancho=3.8, alto=1.4, t_rango=(0, 1), v_max=2.4, centro=(-0.3, -2.3))
        Lr = Lienzo(ancho=3.8, alto=1.4, t_rango=(0, 1), v_max=2.4, centro=(4.0, -2.3))
        cs, cd, cr = Ls.curva(t, s_, SENAL, 3), Ld.curva(t, d_, RUIDO, 2.5), Lr.curva(t, s_ + d_, MEDIDA, 2.5)

        with self.narrar("b1"):
            # «el problema que da sentido»
            self.en("problema")
            self.pop(titulo_)

            # «El sensor mide la temperatura»
            self.en("mide")
            self.play(FadeIn(term), run_time=0.5)

            # «el cable le suma un ruido»
            self.en("cable")
            self.play(Create(cable), run_time=0.6)

            # «Lo que recibimos, erre de ene»
            self.en("recibido")
            self.play(FadeIn(suma), Create(salida), FadeIn(lr), run_time=self.dur(0.8))

            # «la señal, ese de ene»
            self.en("senal")
            self.play(FadeIn(ls), Create(cs), run_time=self.dur(0.9))

            # «el ruido, de de ene»
            self.en("ruido")
            self.play(Create(ent_d), FadeIn(ld), Create(cd), run_time=self.dur(0.9))

            # «es como la moneda»
            self.en("moneda")
            self.play(FadeIn(mon), run_time=0.5)

            # «varianza uno»
            self.en("var1")
            self.play(FadeIn(var1), run_time=0.5)

            # «sin relación con la temperatura»
            self.en("indep")
            self.play(FadeIn(indep), run_time=0.5)

            # «recuperar la señal»
            self.en("recuperar")
            self.play(Create(e1), FadeIn(caja_h), Create(e2), FadeIn(lsh), Create(cr), run_time=self.dur(1.2))

    def parte_b2(self):
        self.limpiar()
        t = np.linspace(0, 1, 44)
        y = sensor_datos(44, 30)
        L = Lienzo(ancho=8.0, alto=3.0, t_rango=(0, 1), v_max=6.5, centro=(-1.5, 0.4))
        desfase = 1.7
        base = L.base()
        curva = L.curva(t, y, SENAL, 3.5).shift(UP * desfase)
        media_ = DashedLine(L.p(0, 0) + UP * desfase, L.p(1, 0) + UP * desfase, color=INK, stroke_width=2.2)
        lab20 = Text("20 °C", color=INK).scale(0.5).next_to(L.p(0, 0) + UP * desfase, LEFT, buff=0.15)
        lab0 = Text("0", color=INK).scale(0.5).next_to(L.p(0, 0), LEFT, buff=0.15)
        resta = Text("−20", color=AMBAR, weight=BOLD).scale(0.8).move_to([-6.3, 1.4, 0])
        m0v4 = Text("media 0 · varianza 4", color=SENAL).scale(0.55).move_to([5.0, 0.4, 0])
        fir = caja("filtro FIR", AMBAR, alto=0.85, scale=0.6).move_to([5.3, -0.9, 0])

        paso = float(L.x(t[1]) - L.x(t[0]))
        centro_v = float(L.x(t[25])) - paso / 2 + 3 * paso
        ventana = Rectangle(width=paso * 6, height=3.1, stroke_width=3, color=AMBAR).set_fill(AMBAR, 0.12)
        ventana.move_to([centro_v, L.cy, 0])
        coefs = VGroup(*[Rectangle(width=paso * 0.8, height=h, stroke_width=1.5, color=AMBAR).set_fill(AMBAR, 0.5)
                         .move_to([centro_v + (2.5 - i) * paso, L.cy + 1.65 + h / 2, 0])
                         for i, h in enumerate((0.55, 0.4, 0.3, 0.22, 0.16, 0.1))])
        suma = MathTex(r"\hat s[n]", "=", r"\sum_{k=0}^{L-1}", "h[k]", "r[n-k]", color=TXT).scale(0.95).move_to([0, -2.0, 0])
        suma[0].set_color(ESTIMACION)
        suma[3].set_color(ESTIMACION)
        suma[4].set_color(MEDIDA)
        una = MathTex(r"\hat s", "=", "h", r"\cdot", "r", color=TXT).scale(1.2).move_to([0, -3.2, 0])
        una[0].set_color(ESTIMACION)
        una[2].set_color(ESTIMACION)
        una[4].set_color(MEDIDA)

        with self.narrar("b2"):
            # «la temperatura centrada»
            self.en("centrada")
            self.play(Create(base), Create(media_), FadeIn(lab20), Create(curva), run_time=self.dur(1.2))

            # «restándole sus veinte grados»
            self.en("resta")
            self.play(curva.animate.shift(DOWN * desfase), media_.animate.shift(DOWN * desfase),
                      ReplacementTransform(lab20, lab0), FadeIn(resta), run_time=self.dur(1.0))

            # «media cero y varianza cuatro»
            self.en("m0v4")
            self.play(FadeIn(m0v4), run_time=0.5)

            # «un filtro FIR»
            self.en("fir")
            self.pop(fir)

            # «las últimas ele muestras»
            self.en("ventana")
            self.play(FadeIn(ventana), FadeIn(suma[:3]), FadeIn(suma[4]), run_time=self.dur(0.9))

            # «multiplicada por un coeficiente»
            self.en("mult")
            self.play(FadeIn(coefs, lag_ratio=0.15), run_time=self.dur(0.9))

            # «hache de ka»
            self.en("hk")
            self.play(FadeIn(suma[3]), run_time=0.5)

            # «Empecemos por el filtro más pequeño»
            self.en("empecemos")
            self.play(FadeOut(coefs), ventana.animate.stretch_to_fit_width(paso * 1.2).shift(RIGHT * paso * 2.5),
                      run_time=self.dur(0.8))

            # «una sola muestra»
            self.en("una")
            self.play(FadeOut(suma), run_time=0.3)
            self.pop(una)
