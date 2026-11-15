"""Escena 08 — Menos fuga a cambio de peor resolución: lóbulos de ancho 1, 2 y 3; los tonos de 50 y 50,5 Hz; fichas de uso."""
from comun.escena import *


class AnchoContraFuga(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        L = lienzo_db(ancho=7.2, alto=4.2, x_max=4, top=2.0, cx=1.9, db=60)
        regla = regla_db(L, (0, -20, -40, -60))
        tipos = ("rect", "hann", "blackman")
        curvas = {tp: curva_f(L, lambda x, tp=tp: nucleo_db(tp, x, piso=60), 0, 4, COLOR_VENTANA[tp], 3.5, n=900)
                  for tp in tipos}
        # ventanitas del lado izquierdo
        minis, nombres = VGroup(), VGroup()
        for i, tp in enumerate(tipos):
            y = 1.7 - 1.5 * i
            Lw = Lienzo(ancho=2.4, alto=0.9, t_rango=(0, 1), v_max=1.2, centro=(-5.4, y))
            t = np.linspace(0, 1, 160, endpoint=False)
            v = valores_ventana(tp, 160)
            m = VGroup(Lw.base(), Lw.curva(t, v, COLOR_VENTANA[tp], 4.0))
            if tp == "rect":
                m.add(Line(Lw.p(0, 0), Lw.p(0, 1), color=COLOR_VENTANA[tp], stroke_width=4),
                      Line(Lw.p(1, 0), Lw.p(1, 1), color=COLOR_VENTANA[tp], stroke_width=4))
            minis.add(m)
            nombres.add(etiqueta(NOMBRE_VENTANA[tp], COLOR_VENTANA[tp], 0.5).move_to([-5.4, y - 0.62, 0]))
        gratis = self.palabra("nada gratis", AMBAR, 1.0).move_to([1.9, 3.35, 0])
        bordes = {"rect": 1, "hann": 2, "blackman": 3}
        marcas = {tp: DashedLine(L.p(bordes[tp], 0), L.p(bordes[tp], -60), color=COLOR_VENTANA[tp], stroke_width=3)
                  for tp in tipos}
        anchos = {tp: etiqueta(f"ancho {bordes[tp]}", COLOR_VENTANA[tp], 0.55).move_to(L.p(bordes[tp], -60) + DOWN * 0.4)
                  for tp in tipos}
        desenf = self.palabra("más desenfoque", ERROR, 0.6).move_to([5.2, 2.6, 0])
        menos = etiqueta("menos fuga", VERDE, 0.7)
        peor = etiqueta("peor resolución", ERROR, 0.7)
        comp = VGroup(menos, DoubleArrow(LEFT * 0.7, RIGHT * 0.7, color=INK, stroke_width=4, buff=0), peor).arrange(RIGHT, buff=0.3)
        comp.move_to([1.9, 3.35, 0])

        with self.narrar("b1"):
            # «no hay nada gratis»
            self.en("gratis")
            self.pop(gratis)

            # «Cuanto más suave es la ventana»
            self.en("suave")
            self.play(LaggedStart(*[FadeIn(m) for m in minis], lag_ratio=0.3), FadeIn(nombres), run_time=self.dur(1.5))

            # «más ancho es su lóbulo principal»
            self.en("ancho")
            self.play(Create(regla), LaggedStart(*[Create(curvas[tp]) for tp in tipos], lag_ratio=0.3),
                      run_time=self.dur(1.7))

            # «el de Hann mide el doble»
            self.en("doble")
            self.play(Create(marcas["hann"]), FadeIn(anchos["hann"]), run_time=self.dur(0.6))

            # «que el de la rectangular»
            self.en("rectangular")
            self.play(Create(marcas["rect"]), FadeIn(anchos["rect"]), run_time=self.dur(0.6))

            # «el de Blackman»
            self.en("blackman")
            self.play(curvas["blackman"].animate.set_stroke(width=6), run_time=self.dur(0.5))

            # «el triple»
            self.en("triple")
            self.play(Create(marcas["blackman"]), FadeIn(anchos["blackman"]), run_time=self.dur(0.5))

            # «más desenfoque»
            self.en("desenfoque")
            self.pop(desenf)

            # «Menos fuga a cambio de peor resolución»
            self.en("compromiso")
            self.play(FadeOut(gratis), FadeIn(comp), run_time=self.dur(0.7))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        Lf = lienzo_f(48.5, 52.0, 2.2, ancho=9.0, cx=0.0, base_y=0.2, v_max=1.5)
        base = Lf.base()
        tonos = VGroup(*[Line(Lf.p(f, 0), Lf.p(f, 1.0), color=SENAL, stroke_width=5, stroke_opacity=0.6) for f in (50, 50.5)])
        l50 = etiqueta("50 Hz", SENAL, 0.5).move_to(Lf.p(49.75, 0) + DOWN * 0.35)
        l505 = etiqueta("50,5 Hz", SENAL, 0.5).move_to(Lf.p(50.75, 0) + DOWN * 0.35)

        def espec(tipo, T, color):
            def f(fr):
                fr = np.asarray(fr, dtype=float)
                return nucleo_lin(tipo, T * (fr - 50)) + nucleo_lin(tipo, T * (fr - 50.5))
            return curva_f(Lf, f, 48.5, 52.0, color, 4.0, n=700)

        c_rect = espec("rect", 2, AMBAR)
        c_hann2 = espec("hann", 2, VERDE)
        c_hann4 = espec("hann", 4, VERDE)
        barra_t = etiqueta("2 s de grabación", INK, 0.6).move_to([-5.0, 3.2, 0])
        barra_t4 = etiqueta("4 s de grabación", INK, 0.6).move_to([-5.0, 3.2, 0])
        ok1 = tilde().scale(1.1).move_to([4.6, 1.8, 0])
        x1 = cruz().scale(1.1).move_to([4.6, 1.8, 0])
        ok2 = tilde().scale(1.1).move_to([4.6, 1.8, 0])
        lab_doble = etiqueta("el doble de ancha", VERDE, 0.55).move_to([4.6, 2.55, 0])
        # fichas de uso
        xs = (-4.8, 0.0, 4.8)
        marcos = [RoundedRectangle(corner_radius=0.12, width=4.3, height=1.3, color=COLOR_VENTANA[tp], stroke_width=2.5)
                  .move_to([x, -2.7, 0]) for x, tp in zip(xs, ("hann", "blackman", "rect"))]
        def contenido(x, nombre, tp, l1, l2=None):
            g = VGroup(Text(nombre, color=COLOR_VENTANA[tp], weight=BOLD).scale(0.5),
                       Text(l1, color=TXT).scale(0.42))
            if l2:
                g.add(Text(l2, color=TXT).scale(0.42))
            return g.arrange(DOWN, buff=0.1).move_to([x, -2.7, 0])
        f_hann = contenido(xs[0], "Hann", "hann", "por defecto")
        f_bl = contenido(xs[1], "Blackman", "blackman", "algo pequeño junto", "a algo enorme")
        f_rect = contenido(xs[2], "rectangular", "rect", "máxima resolución")
        f_rect2 = contenido(xs[2], "rectangular", "rect", "máxima resolución", "amplitudes parecidas")
        par = VGroup(*[Line(Lf.p(f, 0), Lf.p(f, 0.55), color=AMBAR, stroke_width=6) for f in (49.7, 50.3)])
        par.move_to([4.8, -1.35, 0])

        with self.narrar("b2"):
            # «los tonos de cincuenta y cincuenta y medio»
            self.en("tonos")
            self.corte()
            self.play(Create(base), Create(tonos), FadeIn(l50), FadeIn(l505), run_time=self.dur(1.0))

            # «dos segundos de grabación»
            self.en("dos_s")
            self.play(FadeIn(barra_t, shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «la rectangular los separa justo»
            self.en("rectsep")
            self.play(Create(c_rect), FadeIn(ok1, scale=0.5), run_time=self.dur(1.0))

            # «Con la de Hann»
            self.en("hannf")
            self.play(FadeOut(ok1), Transform(c_rect, c_hann2), run_time=self.dur(0.9))

            # «el doble de ancha»
            self.en("dobleancha")
            self.play(FadeIn(lab_doble), run_time=self.dur(0.5))

            # «se funden»
            self.en("funden")
            self.play(FadeIn(x1, scale=0.5), run_time=0.4)

            # «hacen falta cuatro segundos»
            self.en("cuatro_s")
            self.play(FadeOut(x1), FadeOut(lab_doble), FadeOut(barra_t), FadeIn(barra_t4), Transform(c_rect, c_hann4),
                      run_time=self.dur(1.0))
            self.play(FadeIn(ok2, scale=0.5), run_time=0.3)

            # «cada ventana tiene su uso»
            self.en("uso")
            self.play(LaggedStart(*[Create(m) for m in marcos], lag_ratio=0.2), run_time=self.dur(0.9))

            # «La de Hann, por defecto»
            self.en("ficha_hann")
            self.play(FadeIn(f_hann, shift=UP * 0.1), run_time=self.dur(0.5))

            # «cuando hay algo pequeño junto a algo enorme»
            self.en("ficha_bl")
            self.play(FadeIn(f_bl, shift=UP * 0.1), run_time=self.dur(0.5))

            # «La rectangular, cuando manda la resolución»
            self.en("ficha_rect")
            self.play(FadeIn(f_rect, shift=UP * 0.1), run_time=self.dur(0.5))

            # «las amplitudes se parecen»
            self.en("parecen")
            self.play(FadeOut(f_rect), FadeIn(f_rect2), FadeIn(par), run_time=self.dur(0.6))

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        Lw = Lienzo(ancho=2.6, alto=1.0, t_rango=(0, 1), v_max=1.2, centro=(-4.6, 2.5))
        t = np.linspace(0, 1, 160, endpoint=False)
        ventana_ = VGroup(Lw.base(), Lw.curva(t, valores_ventana("hann", 160), VERDE, 4.0))
        Lf = lienzo_f(-3, 3, 1.8, ancho=5.6, cx=2.6, base_y=0.4)
        raya = Line(Lf.p(0, 0), Lf.p(0, 1.0), color=SENAL, stroke_width=8)
        lobulo = curva_f(Lf, lambda f: nucleo_lin("hann", 2.2 * f), -3, 3, VERDE, 4.0, n=500)
        fl = flecha([-3.0, 2.5, 0], [-0.3, 1.8, 0], INK, 4)
        # fila del reloj
        reloj_ = reloj().scale(1.0).move_to([-4.6, 0.3, 0])
        cartel = caja("resolución", AMBAR, ancho=3.2, alto=1.0, scale=0.65).move_to([2.2, 0.3, 0])
        flecha_h = flecha([-3.8, 0.3, 0], [0.4, 0.3, 0], INK, 5)
        atajo = CurvedArrow([-4.4, -0.5, 0], [2.0, -0.5, 0], angle=1.0, color=AMBAR, stroke_width=5)
        atajo_d = DashedVMobject(atajo)
        gente = VGroup(*[persona(AZUL).scale(0.55).move_to([x, -2.3, 0]) for x in (-3.3, -2.0, -0.7)])
        pregunta = Text("?", color=AMBAR, weight=BOLD).scale(2.2).move_to([2.2, 0.3, 0])

        with self.narrar("b3"):
            # «cómo se deforma el espectro»
            self.en("deforma")
            self.corte()
            self.play(FadeIn(ventana_), Create(Lf.base()), Create(raya), run_time=self.dur(0.9))
            self.play(GrowArrow(fl), Transform(raya, lobulo), run_time=self.dur(1.1))

            # «la resolución la sigue dando»
            self.en("sigue")
            self.corte()
            self.play(FadeIn(cartel, scale=0.8), GrowArrow(flecha_h), run_time=self.dur(0.9))

            # «el tiempo grabado»
            self.en("tiempo")
            self.play(FadeIn(reloj_, scale=0.7), run_time=self.dur(0.7))

            # «un atajo muy tentador»
            self.en("atajo")
            self.play(Create(atajo_d), run_time=self.dur(1.2))

            # «muy extendido»
            self.en("extendido")
            self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in gente], lag_ratio=0.3), run_time=self.dur(1.2))

            # «sin grabar más»
            self.en("sin_grabar")
            self.play(Create(tachar(reloj_)), run_time=self.dur(0.5))

            # «Veamos si funciona»
            self.en("funciona")
            self.play(FadeOut(cartel), FadeOut(flecha_h), run_time=0.3)
            self.pop(pregunta)
