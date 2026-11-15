"""Escena 06 — La fuga en decibelios: faldas de la ventana rectangular a −13 dB, tono débil a −60 dB enterrado."""
from comun.escena import *


class LaFugaEnDecibelios(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.bloque1y2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1 y b2: el mismo gráfico
    def bloque1y2(self):
        X = 16
        L = lienzo_db(ancho=10.6, alto=5.0, x_max=X, top=2.4, cx=0.5)
        regla = regla_db(L, (0, -20, -40, -60, -80))
        curva = curva_f(L, lambda x: nucleo_db("rect", x), 0, X, AMBAR, 3.0, n=1400)
        lab_x = etiqueta("distancia al pico (bines)", INK, 0.45).move_to(L.p(X * 0.55, -80) + DOWN * 0.4)
        Lw = Lienzo(ancho=2.2, alto=0.7, t_rango=(-0.1, 1.1), v_max=1.0, centro=(4.4, 3.35))
        v_rect = Line(Lw.p(0, 0.45), Lw.p(1, 0.45), color=AMBAR, stroke_width=4)
        lados = VGroup(Line(Lw.p(0, 0.45), Lw.p(0, -0.45), color=AMBAR, stroke_width=4),
                       Line(Lw.p(1, 0.45), Lw.p(1, -0.45), color=AMBAR, stroke_width=4))
        v_base = Lw.base()
        lab_rect = etiqueta("rectangular", AMBAR, 0.5).move_to([5.0, 2.85, 0])
        pks = picos_laterales("rect", X)
        x1, d1 = pks[0]
        punto1 = Dot(L.p(x1, d1), radius=0.09, color=AMBAR)
        llave = DashedLine(L.p(x1, 0), L.p(x1, d1), color=TXT, stroke_width=3)
        l13 = etiqueta("−13 dB", AMBAR, 0.6).move_to(L.p(x1, -6.5) + RIGHT * 0.95)
        l20 = formula(r"\approx", r"\tfrac{1}{20}", escala=0.7).move_to(L.p(5.2, -9))
        siguientes = VGroup(*[Dot(L.p(x, d), radius=0.07, color=AMBAR) for x, d in pks[1:9]])
        envol = DashedVMobject(curva_f(L, lambda x: -20 * np.log10(np.pi * x), 1.2, X, TXT, 2.5, n=100))
        lejos = flecha(L.p(8.0, -52), L.p(14.5, -52), INK, 4)
        lab_lejos = etiqueta("lejos del pico", INK, 0.5).move_to(L.p(11.2, -58))
        g30 = DashedLine(L.p(0, -30), L.p(X, -30), color=CIAN, stroke_width=3)
        g40 = DashedLine(L.p(0, -40), L.p(X, -40), color=CIAN, stroke_width=3)
        t30 = etiqueta("−30 dB", CIAN, 0.45).move_to(L.p(X, -30) + RIGHT * 0.6)
        t40 = etiqueta("−40 dB", CIAN, 0.45).move_to(L.p(X, -40) + RIGHT * 0.6)

        xd = 10
        debil = Line(L.p(xd, -80), L.p(xd, -60), color=CIAN, stroke_width=9)
        g60 = DashedLine(L.p(0, -60), L.p(X, -60), color=CIAN, stroke_width=3)
        t60 = etiqueta("−60 dB", CIAN, 0.55).move_to(L.p(2.2, -60) + UP * 0.3)
        mill = etiqueta("1/1.000.000", CIAN, 0.5).move_to(L.p(xd, -68) + RIGHT * 1.5)
        p30 = Dot(L.p(xd, -30), radius=0.1, color=RUIDO)
        mil = DoubleArrow(L.p(xd + 0.6, -30), L.p(xd + 0.6, -60), color=RUIDO, stroke_width=4, buff=0, tip_length=0.18)
        t_mil = formula(r"\times 1.000", escala=0.65, color=RUIDO).move_to(L.p(xd + 0.6, -45) + RIGHT * 1.15)
        enterr = area_f(L, lambda x: nucleo_db("rect", x), xd - 1.0, xd + 1.0, RUIDO, 0.45, n=120, piso=-80)
        lab_arm = etiqueta("armónico", CIAN, 0.5).move_to(L.p(xd - 2.5, -63))
        ojo_ = ojo().scale(0.8).move_to([5.9, 1.4, 0])

        with self.narrar("b1"):
            # «miremos la fuga con esta regla»
            self.en("regla")
            self.play(Create(regla), Create(curva), FadeIn(lab_x), run_time=self.dur(1.6))

            # «la ventana rectangular»
            self.en("rect")
            self.play(Create(v_base), Create(v_rect), Create(lados), FadeIn(lab_rect), run_time=self.dur(0.9))

            # «el primer lóbulo lateral»
            self.en("primero")
            self.play(FadeIn(punto1, scale=0.4), run_time=0.4)

            # «a menos trece decibelios del pico»
            self.en("m13")
            self.play(Create(llave), FadeIn(l13), run_time=self.dur(0.9))

            # «una vigésima parte»
            self.en("veinte")
            self.play(FadeIn(l20), run_time=self.dur(0.6))

            # «los siguientes bajan»
            self.en("bajan")
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in siguientes], lag_ratio=0.2), run_time=self.dur(1.6))

            # «pero despacio»
            self.en("lento")
            self.play(Create(envol), run_time=self.dur(0.9))

            # «bastante lejos del pico»
            self.en("lejos")
            self.play(GrowArrow(lejos), FadeIn(lab_lejos), run_time=self.dur(0.8))

            # «treinta o cuarenta decibelios por debajo»
            self.en("tres_cuatro")
            self.play(Create(g30), Create(g40), FadeIn(t30), FadeIn(t40), run_time=self.dur(1.0))

        with self.narrar("b2"):
            # «un tono débil»
            self.en("debil")
            self.play(FadeOut(lejos), FadeOut(lab_lejos), FadeOut(g30), FadeOut(g40), FadeOut(t30), FadeOut(t40),
                      FadeOut(l20), FadeOut(llave), FadeOut(l13), FadeOut(punto1), FadeOut(siguientes),
                      FadeOut(envol), run_time=0.4)
            self.play(Create(debil), run_time=self.dur(0.4))

            # «sesenta decibelios por debajo del fuerte»
            self.en("m60")
            self.play(Create(g60), FadeIn(t60), run_time=self.dur(0.7))

            # «una millonésima de su potencia»
            self.en("millon")
            self.play(FadeIn(mill), run_time=self.dur(0.5))

            # «las faldas del fuerte están a menos treinta»
            self.en("faldas30")
            self.play(FadeIn(p30, scale=0.4), run_time=0.4)

            # «mil veces por encima del débil»
            self.en("mil")
            self.play(GrowFromCenter(mil), FadeIn(t_mil), run_time=self.dur(0.8))

            # «El tono débil queda enterrado»
            self.en("enterrado")
            self.play(FadeIn(enterr), run_time=self.dur(0.7))

            # «un armónico pequeño»
            self.en("armonico")
            self.play(FadeIn(lab_arm), run_time=self.dur(0.5))

            # «cortar con una ventana rectangular te lo esconde»
            self.en("esconde")
            self.play(FadeIn(ojo_), Create(tachar(ojo_)), run_time=self.dur(0.7))

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        L = Lienzo(ancho=8.0, alto=2.4, t_rango=(-0.3, 1.3), v_max=1.3, centro=(0, -0.2))
        t = np.linspace(0, 1, 300, endpoint=False)
        trozo = L.curva(t, np.cos(2 * np.pi * 10.5 * t), SENAL, 3.0)
        suave = L.curva(t, np.cos(2 * np.pi * 10.5 * t) * valores_ventana("hann", 300), SENAL, 3.0)
        salto_i = Line(L.p(0, 0), L.p(0, 1), color=ERROR, stroke_width=6)
        salto_d = Line(L.p(1, 0), L.p(1, -1), color=ERROR, stroke_width=6)
        tij = tijeras().scale(0.9).move_to([-3.0, 2.9, 0])
        gota = Dot([-2.4, 2.4, 0], radius=0.1, color=RUIDO)
        bomb = bombilla().scale(0.9).move_to([3.0, 2.8, 0])
        ok_i = tilde().scale(1.1).move_to(L.p(0, 0) + UP * 1.6)
        ok_d = tilde().scale(1.1).move_to(L.p(1, 0) + UP * 1.6)

        with self.narrar("b3"):
            # «una forma de cortar que derrame menos»
            self.en("derrame")
            self.corte()
            self.pop(tij)
            self.play(FadeIn(gota), run_time=0.2)
            self.play(gota.animate.shift(DOWN * 1.2), run_time=self.dur(1.0), rate_func=rush_into)

            # «Y la idea es sencilla»
            self.en("idea")
            self.play(FadeOut(gota), FadeOut(tij), run_time=0.3)
            self.pop(bomb)

            # «el problema era el salto en los bordes»
            self.en("salto_bordes")
            self.play(Create(L.base()), Create(trozo), run_time=self.dur(0.8), rate_func=linear)
            self.play(Create(salto_i), Create(salto_d), run_time=self.dur(0.5))

            # «Si no cortamos de golpe»
            self.en("nogolpe")
            self.play(Transform(trozo, suave), FadeOut(salto_i), FadeOut(salto_d), FadeOut(bomb), run_time=self.dur(1.2))

            # «no hay salto»
            self.en("sinsalto")
            self.play(FadeIn(ok_i, scale=0.5), FadeIn(ok_d, scale=0.5), run_time=0.5)
