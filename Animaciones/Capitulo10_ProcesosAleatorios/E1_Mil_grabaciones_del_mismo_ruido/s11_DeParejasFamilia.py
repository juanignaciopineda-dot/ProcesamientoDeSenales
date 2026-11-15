"""Escena 11 — Dos cortes dan una conjunta (el rombo); muchos cortes, una familia de variables."""
from comun.escena import *


class DeParejasFamilia(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.pareja()
        self.plano()
        self.familia()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1: dos cortes, cuatro parejas
    def pareja(self):
        cos = CuatroCosenos(ancho=6.4, centro=(-2.9, 0.0))
        self.cos = cos
        pares = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        with self.narrar("b1"):
            self.play(FadeIn(cos), run_time=0.5)

            # «dos cortes»
            self.en("cortes")
            c0 = cos.corte(0.0)
            self.play(Create(c0), run_time=self.dur(0.9))

            # «un cuarto de período»
            self.en("cuarto_t")
            c1 = cos.corte(0.25)
            puntos = VGroup(*[Dot(cos.punto(i, t), radius=0.1, color=AMBAR) for i in range(4) for t in (0.0, 0.25)])
            self.play(Create(c1), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in puntos], lag_ratio=0.1), run_time=self.dur(1.3))
            self.cortes = VGroup(c0, c1, puntos)

            # «una pareja de números»
            self.en("pareja")
            cab = formula(r"\big(X(0),\ X(T/4)\big)", color=AMBAR, escala=0.95).move_to([3.7, 3.45, 0])
            self.pop(cab)

            # «da uno y cero» … «cero y uno»
            self.filas = []
            for marca, i, par in (("p1", 0, pares[0]), ("p2", 1, pares[1]), ("p3", 2, pares[2]), ("p4", 3, pares[3])):
                self.en(marca)
                txt = "(" + ", ".join(("−1" if v < 0 else str(v)) for v in par) + ")"
                fila = Text(txt, color=TXT, weight=BOLD).scale(0.85).move_to([3.4, cos.yc(i), 0])
                self.filas.append(fila)
                self.play(puntos[2 * i].animate(rate_func=there_and_back).scale(2.0),
                          puntos[2 * i + 1].animate(rate_func=there_and_back).scale(2.0), run_time=0.5)
                self.pop(fila, sonido=None)

            # «Cuatro parejas»
            self.en("cuatro")
            self.cuartos = VGroup(*[Text("¼", color=AMBAR, weight=BOLD).scale(0.8).move_to([5.7, cos.yc(i), 0])
                                    for i in range(4)])
            self.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in self.cuartos], lag_ratio=0.15), run_time=self.dur(1.0))
            self.cab = cab

    # ---------------------------------------------------------------- b2: conjunta, rombo y más cortes
    def plano(self):
        cos = self.cos
        with self.narrar("b2"):
            # «una distribución conjunta»
            self.en("conjunta")
            tabla = SurroundingRectangle(VGroup(self.cab, *self.filas, self.cuartos), color=AMBAR, buff=0.2,
                                         corner_radius=0.15, stroke_width=3)
            conj = Text("conjunta", color=AMBAR, weight=BOLD).scale(0.6).next_to(tabla, DOWN, buff=0.15)
            self.play(Create(tabla), FadeIn(conj), run_time=self.dur(0.8))

            # «lo enviado y lo recibido»
            self.en("enviado")
            self.play(FadeOut(cos), FadeOut(self.cortes), run_time=0.3)
            celdas = VGroup(*[Square(1.2, color=SENAL, stroke_width=2.5).set_fill(SENAL, 0.1) for _ in range(4)])
            celdas.arrange_in_grid(2, 2, buff=0.0).move_to([-3.2, 0.1, 0])
            vals = VGroup(*[Text(v, color=TXT, weight=BOLD).scale(0.6).move_to(celdas[i])
                            for i, v in enumerate(("0,63", "0,07", "0,03", "0,27"))])
            env = Text("enviado", color=INK).scale(0.55).rotate(PI / 2).next_to(celdas, LEFT, buff=0.25)
            rec = Text("recibido", color=INK).scale(0.55).next_to(celdas, UP, buff=0.25)
            self.play(Create(celdas), FadeIn(vals), FadeIn(env), FadeIn(rec), run_time=self.dur(1.0))

            # «puntos en el plano»
            self.en("plano")
            self.play(FadeOut(celdas), FadeOut(vals), FadeOut(env), FadeOut(rec), run_time=0.3)
            centro = np.array([-3.2, 0.1, 0])
            ex = Arrow(centro + LEFT * 2.6, centro + RIGHT * 2.6, color=INK, stroke_width=3, buff=0)
            ey = Arrow(centro + DOWN * 2.6, centro + UP * 2.6, color=INK, stroke_width=3, buff=0)
            lx = formula("X(0)", color=INK, escala=0.9).next_to(ex, RIGHT, buff=0.1)
            ly = formula(r"X(T/4)", color=INK, escala=0.9).next_to(ey, UP, buff=0.1)
            esc = 1.8
            dest = [centro + np.array([a * esc, b * esc, 0]) for a, b in ((1, 0), (0, -1), (-1, 0), (0, 1))]
            pts = VGroup(*[Dot([4.8, self.cos.yc(i), 0], radius=0.16, color=AMBAR) for i in range(4)])
            self.play(Create(ex), Create(ey), FadeIn(lx), FadeIn(ly), FadeIn(pts), run_time=0.5)
            self.play(*[p.animate.move_to(d) for p, d in zip(pts, dest)], run_time=self.dur(1.6))

            # «un rombo»
            self.en("rombo")
            romb = Polygon(*dest, color=AMBAR, stroke_width=4)
            self.play(Create(romb), run_time=self.dur(1.0))

            # «Con dos cortes»
            self.en("dos")
            self.play(*[FadeOut(m) for m in (tabla, conj, self.cab, *self.filas, self.cuartos, ex, ey, lx, ly, pts, romb)],
                      run_time=0.3)
            L = Lienzo(ancho=10.5, alto=3.0, t_rango=(0, 1), v_max=2.4, centro=(0, 0.6))
            t = np.linspace(0, 1, 260)
            curva = L.curva(t, serie(55, 260, 0.96) * 0.85, SENAL, 3.5)
            base = L.base()
            self.play(Create(base), Create(curva), run_time=0.6)
            cortes = [L.vertical(x, AMBAR, 3.0, mitad=1.7) for x in (0.3, 0.66)]
            self.play(*[Create(c) for c in cortes], run_time=0.4)
            txt = Text("2 cortes → 2 variables", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, -2.1, 0])
            self.pop(txt)

            # «Con tres cortes»
            self.en("tres")
            c3 = L.vertical(0.48, AMBAR, 3.0, mitad=1.7)
            txt3 = Text("3 cortes → 3 variables", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, -2.1, 0])
            self.play(Create(c3), run_time=0.3)
            self.play(Transform(txt, txt3), run_time=0.3)

            # «Con mil cortes»
            self.en("mil")
            masa = VGroup(*[L.vertical(x, AMBAR, 1.6, mitad=1.7).set_stroke(opacity=0.6)
                            for x in np.linspace(0.02, 0.98, 70)])
            txtm = Text("1000 cortes → 1000 variables", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, -2.1, 0])
            self.play(LaggedStart(*[FadeIn(m) for m in masa], lag_ratio=0.02), Transform(txt, txtm),
                      run_time=self.dur(1.8))

    # ---------------------------------------------------------------- b3: la familia de variables
    def familia(self):
        L = Lienzo(ancho=10.4, alto=2.6, t_rango=(0, 1), v_max=2.4, centro=(0, 1.9))
        xs = [-4.5, -2.5, -0.5, 3.9]
        tcs = [float((x + 5.2) / 10.4) for x in xs]
        with self.narrar("b3"):
            self.corte()
            pila = pila_de_curvas(L, 14, semilla=8, a=0.96, color=SENAL, opacidad=0.4, ancho=2.2, escala=0.5)
            cuts = VGroup(*[L.vertical(t, AMBAR, 3.0) for t in tcs])
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.05), run_time=1.5)
            self.play(LaggedStart(*[Create(c) for c in cuts], lag_ratio=0.2), run_time=1.0)

            # «una familia de variables aleatorias»
            self.en("familia")
            nombres = ["X(t_{1})", "X(t_{2})", "X(t_{3})", "X(t_{n})"]
            cajas = VGroup(*[caja_tex(n, AZUL, 1.6, 0.85, 0.9).move_to([x, -0.35, 0]) for n, x in zip(nombres, xs)])
            puntos = Text("⋯", color=TXT, weight=BOLD).scale(1.4).move_to([1.7, -0.35, 0])
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cajas], lag_ratio=0.2), FadeIn(puntos),
                      run_time=self.dur(1.4))

            # «una por cada instante»
            self.en("instante")
            enlaces = VGroup(*[DashedLine([x, 0.6, 0], [x, 0.05, 0], color=INK, dash_length=0.08, stroke_width=2.5)
                               for x in xs])
            self.play(LaggedStart(*[Create(e) for e in enlaces], lag_ratio=0.15), run_time=self.dur(1.0))

            # «El tiempo hace de etiqueta»
            self.en("etiqueta")
            eje = Line([-5.2, -1.6, 0], [5.2, -1.6, 0], color=INK, stroke_width=2.5)
            marcas = VGroup(*[Line([x, -1.7, 0], [x, -1.5, 0], color=INK, stroke_width=2.5) for x in xs])
            tiempos = VGroup(*[formula(n, color=AMBAR, escala=0.9).move_to([x, -2.05, 0])
                               for n, x in zip(["t_{1}", "t_{2}", "t_{3}", "t_{n}"], xs)])
            self.play(Create(eje), FadeIn(marcas), LaggedStart(*[FadeIn(t, shift=UP * 0.15) for t in tiempos],
                                                                 lag_ratio=0.15), run_time=self.dur(1.3))

            # «de qué variable de la familia»
            self.en("que_var")
            self.play(cajas[1].animate(rate_func=there_and_back).scale(1.25),
                      tiempos[1].animate(rate_func=there_and_back).scale(1.3), run_time=self.dur(0.9))

            # «conocer el proceso del todo»
            self.en("todo")
            todo = SurroundingRectangle(VGroup(cajas, puntos), color=AMBAR, buff=0.2, corner_radius=0.15,
                                        stroke_width=4)
            self.play(Create(todo), run_time=self.dur(0.8))

            # «cualquier grupo de instantes»
            self.en("grupo")
            self.play(FadeOut(todo), run_time=0.2)
            g1 = SurroundingRectangle(VGroup(cajas[0], cajas[1]), color=VERDE, buff=0.15, corner_radius=0.12, stroke_width=4)
            g2 = SurroundingRectangle(VGroup(cajas[1], cajas[2]), color=VERDE, buff=0.15, corner_radius=0.12, stroke_width=4)
            self.play(Create(g1), run_time=0.5)
            self.play(ReplacementTransform(g1, g2), run_time=0.5)

            # «de cualquier tamaño»
            self.en("tamano")
            g3 = SurroundingRectangle(VGroup(cajas, puntos), color=VERDE, buff=0.2, corner_radius=0.15, stroke_width=4)
            self.play(ReplacementTransform(g2, g3), run_time=self.dur(0.9))
