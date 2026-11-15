"""Escena 03 — Del dado al receptor: lo aleatorio deja de ser un número y pasa a ser una curva."""
from comun.escena import *


class DelDadoAlReceptor(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.numeros()
        self.curvas()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1: de números a señales
    def numeros(self):
        with self.narrar("b1"):
            # «todo lo aleatorio eran números»
            self.en("numeros")
            xs = [-3.75 + 1.5 * k for k in range(6)]
            recta = Line([-4.6, -0.6, 0], [4.6, -0.6, 0], color=INK, stroke_width=2.5)
            marcas = VGroup(*[Line([x, -0.72, 0], [x, -0.48, 0], color=INK, stroke_width=2.5) for x in xs])
            nums = VGroup(*[Text(str(k + 1), color=INK).scale(0.6).move_to([x, -1.15, 0]) for k, x in enumerate(xs)])
            self.play(Create(recta), FadeIn(marcas), FadeIn(nums), run_time=0.6)
            punto = Dot([xs[1], -0.6, 0], radius=0.16, color=AMBAR)
            self.play(FadeIn(punto, scale=0.5), run_time=0.2)
            for k in (4, 2):
                self.play(punto.animate.move_to([xs[k], -0.6, 0]), run_time=self.dur(0.4))

            # «Tiras un dado»
            self.en("dado")
            d = dado_n(3).move_to([0, 2.0, 0])
            self.pop(d)
            fl = flecha(d.get_bottom() + DOWN * 0.1, [xs[2], -0.35, 0], AMBAR)
            self.play(GrowArrow(fl), run_time=self.dur(0.5))

            # «Envías un bit»
            self.en("bit")
            self.corte()
            uno = caja("1", SENAL, 1.0, 1.0, 0.8).move_to([-4.2, 0.3, 0])
            canal = caja("canal", INK, 2.4, 1.0, 0.6).move_to([0, 0.3, 0])
            cero = caja("0", MEDIDA, 1.0, 1.0, 0.8).move_to([4.2, 0.3, 0])
            enviado = etiqueta("enviado", INK, 0.6).next_to(uno, DOWN, buff=0.3)
            recibido = etiqueta("recibido", INK, 0.6).next_to(cero, DOWN, buff=0.3)
            self.pop(uno)
            self.play(GrowArrow(flecha(uno.get_right(), canal.get_left(), INK)), FadeIn(enviado), run_time=0.4)
            self.pop(canal, sonido=None)
            self.play(GrowArrow(flecha(canal.get_right(), cero.get_left(), INK)), FadeIn(recibido), run_time=0.4)
            self.pop(cero, sonido=None)

            # «dos variables a la vez»
            self.en("dos_var")
            self.corte()
            celdas = VGroup(*[Square(1.3, color=SENAL, stroke_width=2.5).set_fill(SENAL, 0.1) for _ in range(4)])
            celdas.arrange_in_grid(2, 2, buff=0.0).move_to([-3.4, -0.1, 0])
            cab_x = VGroup(*[etiqueta(s, INK, 0.5).next_to(celdas[i], UP, buff=0.15) for i, s in enumerate(("0", "1"))])
            cab_y = VGroup(*[etiqueta(s, INK, 0.5).next_to(celdas[2 * i], LEFT, buff=0.2) for i, s in enumerate(("0", "1"))])
            t_rec = etiqueta("recibido", INK, 0.45).next_to(celdas, UP, buff=0.65)
            t_env = etiqueta("enviado", INK, 0.45).rotate(PI / 2).next_to(celdas, LEFT, buff=0.7)
            self.play(Create(celdas), FadeIn(cab_x), FadeIn(cab_y), FadeIn(t_rec), FadeIn(t_env), run_time=self.dur(1.0))

            # «su tabla»
            self.en("tabla")
            valores = VGroup(*[etiqueta(v, TXT, 0.6).move_to(celdas[i]) for i, v in enumerate(("0,63", "0,07", "0,03", "0,27"))])
            self.play(LaggedStart(*[FadeIn(v, scale=0.6) for v in valores], lag_ratio=0.2), run_time=self.dur(0.9))

            # «su nube de puntos»
            self.en("nube")
            rng = np.random.default_rng(4)
            base = rng.normal(0, 1, 70)
            ruido = rng.normal(0, 0.7, 70)
            px, py = base * 0.55, (0.7 * base + ruido) * 0.55
            centro = np.array([3.6, -0.1, 0])
            ejes_x = Line(centro + LEFT * 2.2, centro + RIGHT * 2.2, color=INK, stroke_width=2)
            ejes_y = Line(centro + DOWN * 2.0, centro + UP * 2.0, color=INK, stroke_width=2)
            puntos = VGroup(*[Dot(centro + [x, y, 0], radius=0.07, color=MEDIDA) for x, y in zip(px, py)])
            self.play(Create(ejes_x), Create(ejes_y), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in puntos], lag_ratio=0.02), run_time=self.dur(1.2))

            # «llega de verdad a un receptor»
            self.en("receptor")
            self.corte()
            rx = caja("receptor", CIAN, 2.8, 1.3, 0.7).move_to([-4.4, 0.3, 0])
            t = np.linspace(0, 1, 60)
            onda = traza(-7.0 + t * 1.3, 0.3 + 0.28 * np.sin(2 * np.pi * 3 * t), SENAL, 3.5)
            self.play(Create(onda), FadeIn(rx), run_time=0.7)
            self.play(GrowArrow(flecha([-5.6, 0.3, 0], rx.get_left(), SENAL)), run_time=0.3)

            # «no es un número»
            self.en("no_num")
            siete = Text("7", color=TXT, weight=BOLD).scale(2.6).move_to([1.2, 0.3, 0])
            self.play(GrowArrow(flecha(rx.get_right(), [0.4, 0.3, 0], INK)), FadeIn(siete), run_time=0.5)
            tach = tachar(siete)
            self.play(Create(tach), run_time=self.dur(0.4))

            # «dura segundos, minutos u horas»
            self.en("dura")
            self.play(FadeOut(siete), FadeOut(tach), run_time=0.3)
            L = Lienzo(ancho=8.8, alto=1.8, t_rango=(0, 1), v_max=2.2, centro=(2.2, 0.3))
            tt = np.linspace(0, 1, 300)
            senal = L.curva(tt, serie(21, 300, 0.97) * 0.7, SENAL, 3.5)
            eje_t = Line([-2.2, -1.5, 0], [6.6, -1.5, 0], color=INK, stroke_width=2)
            puntas = VGroup(*[etiqueta(s, INK, 0.6).move_to([x, -1.95, 0])
                              for s, x in (("segundos", -1.1), ("minutos", 2.4), ("horas", 5.9))])
            self.play(Create(senal), Create(eje_t), run_time=self.dur(2.0), rate_func=linear)
            self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.15) for p in puntas], lag_ratio=0.35),
                      run_time=self.dur(1.0))

    # ---------------------------------------------------------------- b2: curvas enteras
    def curvas(self):
        Lc = Lienzo(ancho=9.6, alto=1.5, t_rango=(0, 1), v_max=2.4, centro=(0.9, 2.1))
        Ls = Lienzo(ancho=9.6, alto=1.5, t_rango=(0, 1), v_max=2.4, centro=(0.9, 0.3))
        Lv = Lienzo(ancho=9.6, alto=1.5, t_rango=(0, 1), v_max=2.4, centro=(0.9, -1.5))
        t = np.linspace(0, 1, 280)
        env = sum(np.exp(-((t - c) / w) ** 2) for c, w in ((0.15, 0.06), (0.4, 0.08), (0.62, 0.05), (0.85, 0.09)))
        with self.narrar("b2"):
            self.corte()
            # «El ruido de un canal»
            self.en("canal")
            e1 = etiqueta("canal", RUIDO, 0.7).move_to([-5.9, 2.1, 0])
            b1 = Lc.base()
            v1 = serie(31, 280, 0.5) * 0.75
            c1 = Lc.curva(t, v1, RUIDO, 3.2)
            self.play(FadeIn(e1), Create(b1), run_time=0.25)
            self.play(Create(c1), run_time=self.dur(1.1), rate_func=linear)

            # «la tensión que mide un sensor»
            self.en("sensor")
            e2 = etiqueta("sensor", MEDIDA, 0.7).move_to([-5.9, 0.3, 0])
            b2 = Ls.base()
            c2 = Ls.curva(t, serie(32, 280, 0.985) * 0.9, MEDIDA, 3.2)
            self.play(FadeIn(e2), Create(b2), run_time=0.25)
            self.play(Create(c2), run_time=self.dur(2.0), rate_func=linear)

            # «una grabación de voz»
            self.en("voz")
            e3 = etiqueta("voz", SENAL, 0.7).move_to([-5.9, -1.5, 0])
            b3 = Lv.base()
            c3 = Lv.curva(t, np.sin(2 * np.pi * 38 * t) * env * 1.1, SENAL, 2.6)
            self.play(FadeIn(e3), Create(b3), run_time=0.25)
            self.play(Create(c3), run_time=self.dur(2.0), rate_func=linear)

            # «una curva entera»
            self.en("entera")
            marco = DoubleArrow(Lc.p(0, 1.25), Lc.p(1, 1.25), color=AMBAR, stroke_width=4, buff=0)
            txt = etiqueta("una curva entera", AMBAR, 0.55).next_to(marco, UP, buff=0.12)
            self.play(GrowFromCenter(marco), FadeIn(txt), run_time=self.dur(0.6))

            # «un valor en cada instante»
            self.en("instante")
            self.play(FadeOut(marco), FadeOut(txt), run_time=0.25)
            tr = ValueTracker(0.02)
            linea = always_redraw(lambda: Lc.vertical(tr.get_value(), AMBAR, 2.5, mitad=0.85))
            punto = always_redraw(lambda: Dot(Lc.p(tr.get_value(), float(np.interp(tr.get_value(), t, v1))),
                                              radius=0.11, color=AMBAR))
            self.add(linea, punto)
            self.play(tr.animate.set_value(0.98), run_time=self.dur(3.6), rate_func=linear)
            linea.clear_updaters()
            punto.clear_updaters()

            # «qué curva nos va a tocar»
            self.en("tocar")
            self.play(FadeOut(linea), FadeOut(punto), *[FadeOut(m) for m in (e2, b2, c2, e3, b3, c3)], run_time=0.3)
            fantasmas = pila_de_curvas(Lc, 5, semilla=9, a=0.5, color=RUIDO, opacidad=0.35, ancho=2.2, escala=0.75)
            q = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to([6.4, 2.1, 0])
            self.play(LaggedStart(*[Create(f) for f in fantasmas], lag_ratio=0.15), run_time=self.dur(1.3))
            self.pop(q)

            # «dos veces»
            self.en("dos")
            self.play(FadeOut(fantasmas), FadeOut(q), run_time=0.3)
            e4 = etiqueta("otra vez", RUIDO, 0.7).move_to([-5.9, 0.3, 0])
            b4 = Ls.base()
            c4 = Ls.curva(t, serie(33, 280, 0.5) * 0.75, RUIDO, 3.2)
            self.play(FadeIn(e4), Create(b4), Create(c4), run_time=self.dur(1.2), rate_func=linear)
            distinto = Text("≠", color=ROJO, weight=BOLD).scale(2.2).move_to([6.4, 1.2, 0])
            self.pop(distinto)

            # «Necesitamos una forma»
            self.en("necesitamos")
            q2 = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to([6.4, 1.2, 0])
            self.play(FadeOut(distinto), run_time=0.2)
            self.pop(q2)

            # «describir el azar de una curva completa»
            self.en("azar")
            cartel = Text("el azar de una curva entera", color=AMBAR, weight=BOLD).scale(0.85).move_to([0, -2.4, 0])
            self.play(FadeIn(cartel, shift=UP * 0.2), run_time=0.5)
