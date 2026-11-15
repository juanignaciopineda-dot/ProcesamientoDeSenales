"""Escena 08 — Un trozo lo dice todo (el seno); la moneda, nada. Los dos extremos."""
from comun.escena import *


class TrozoBasta(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.seno()
        self.moneda()
        self.extremos()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1: el seno
    def seno(self):
        L = Lienzo(ancho=10.2, alto=3.0, t_rango=(0, 3), v_max=1.5, centro=(0, -0.5))
        th = -0.9
        ta = np.linspace(0, 2, 200)
        tb = np.linspace(2, 3, 100)
        base = L.base()
        c_a = L.curva(ta, np.sin(2 * np.pi * ta + th), SENAL, 4.5)
        c_b = L.curva(tb, np.sin(2 * np.pi * tb + th), SENAL, 4.5)
        t_pico = (np.pi / 2 - th) / (2 * np.pi)
        t_cero = -th / (2 * np.pi)
        with self.narrar("b1"):
            self.play(Create(base), Create(c_a), Create(c_b), run_time=self.dur(1.6), rate_func=linear)

            # «un trozo pequeño»
            self.en("trozo")
            marco = Rectangle(width=float(L.x(2) - L.x(0)) + 0.2, height=2.7, color=AMBAR, stroke_width=4)
            marco.move_to([float((L.x(0) + L.x(2)) / 2), -0.5, 0])
            self.play(Create(marco), FadeOut(c_b), run_time=self.dur(0.7))

            # «un par de oscilaciones»
            self.en("par")
            self.play(c_a.animate.set_stroke(AMBAR, width=6), run_time=self.dur(0.5))

            # «medir la amplitud»
            self.en("med_a")
            fa = DoubleArrow(L.p(t_pico, 0), L.p(t_pico, 1.0), color=TXT, stroke_width=4, buff=0)
            self.play(GrowFromCenter(fa), run_time=self.dur(0.6))

            # «la frecuencia»
            self.en("med_f")
            ff = DoubleArrow(L.p(t_pico, 1.3), L.p(t_pico + 1, 1.3), color=TXT, stroke_width=4, buff=0)
            self.play(GrowFromCenter(ff), run_time=self.dur(0.6))

            # «la fase»
            self.en("med_p")
            fp = DoubleArrow(L.p(0, -0.3), L.p(t_cero, -0.3), color=TXT, stroke_width=4, buff=0)
            self.play(GrowFromCenter(fp), run_time=self.dur(0.6))

            # «qué oscilador es»
            self.en("cual")
            par = formula("A", ",", r"\Phi", ",", r"\Theta", color=AMBAR, escala=1.5).move_to([0, 2.7, 0])
            self.pop(par)

            # «dibujar todo lo que viene después»
            self.en("futuro")
            self.play(FadeOut(fa), FadeOut(ff), FadeOut(fp), marco.animate.set_stroke(opacity=0.35), run_time=0.3)
            resto = DashedVMobject(L.curva(tb, np.sin(2 * np.pi * tb + th), AMBAR, 4.5), num_dashes=36)
            self.play(Create(resto), run_time=self.dur(2.2), rate_func=linear)

            # «Un trozo basta»
            self.en("basta")
            ok = tilde(VERDE, 1.2).move_to([5.9, 2.5, 0])
            self.pop(ok)

    # ---------------------------------------------------------------- b2: la moneda
    def moneda(self):
        with self.narrar("b2"):
            # «otro experimento»
            self.en("otro")
            self.corte()
            c = moneda("", AMBAR).scale(1.5).move_to([-4.6, 2.2, 0])
            self.pop(c)

            # «tiras una moneda»
            self.en("moneda")
            self.play(Rotate(c, angle=PI, axis=UP), run_time=0.5)
            self.play(Rotate(c, angle=PI, axis=UP), run_time=0.5)

            # «más uno si sale cara»
            self.en("cara")
            t_cara = Text("cara → +1", color=TXT, weight=BOLD).scale(0.7).move_to([-0.9, 2.7, 0])
            self.pop(t_cara)

            # «menos uno si sale cruz»
            self.en("cruz")
            t_cruz = Text("cruz → −1", color=TXT, weight=BOLD).scale(0.7).move_to([-0.9, 1.7, 0])
            self.pop(t_cruz)

            # «una fila de más unos y menos unos»
            self.en("fila")
            rng = np.random.default_rng(3)
            valores = [1, -1, -1, 1, 1, -1, 1, -1, -1, 1]
            tira = tira_pm1(valores, lado=0.8, escala_txt=0.5).move_to([-0.55, -0.6, 0])
            slot = Square(0.8, color=AMBAR, stroke_width=3).next_to(tira, RIGHT, buff=0.06)
            slot_dash = DashedVMobject(slot, num_dashes=24)
            self.play(LaggedStart(*[FadeIn(cl, shift=DOWN * 0.2) for cl in tira.celdas], lag_ratio=0.3),
                      run_time=self.dur(3.3))

            # «por muchas tiradas que hayas visto»
            self.en("muchas")
            self.play(LaggedStart(*[cl.animate(rate_func=there_and_back).scale(1.25) for cl in tira.celdas],
                                  lag_ratio=0.12), run_time=self.dur(2.0))

            # «la siguiente»
            self.en("siguiente")
            interr = Text("?", color=AMBAR, weight=BOLD).scale(0.9).move_to(slot)
            self.play(Create(slot_dash), FadeIn(interr), run_time=self.dur(0.7))

            # «mitad y mitad»
            self.en("mitad")
            mm = Text("½ | ½", color=AMBAR, weight=BOLD).scale(0.8).next_to(slot, UP, buff=0.3)
            self.pop(mm)

            # «Las diez primeras tiradas»
            self.en("diez")
            llave = Brace(VGroup(*tira.celdas), DOWN, buff=0.15, color=INK)
            self.play(GrowFromCenter(llave), run_time=self.dur(0.6))

            # «no dicen nada de la undécima»
            self.en("nada")
            desde = llave.get_bottom() + DOWN * 0.05
            flecha_ = CurvedArrow(desde, slot.get_bottom() + DOWN * 0.1, angle=PI / 3, color=INK)
            self.play(Create(flecha_), run_time=self.dur(0.6))
            x_ = cruz(ROJO, 0.9).move_to(flecha_.point_from_proportion(0.5))
            self.pop(x_)

    # ---------------------------------------------------------------- b3: los dos extremos
    def extremos(self):
        with self.narrar("b3"):
            # «dos procesos en los extremos»
            self.en("barra")
            self.corte()
            barra = Line([-4.6, 1.2, 0], [4.6, 1.2, 0], color=INK, stroke_width=5)
            e_i = Dot([-4.6, 1.2, 0], radius=0.14, color=SENAL)
            e_d = Dot([4.6, 1.2, 0], radius=0.14, color=AMBAR)
            tt = np.linspace(0, 1, 80)
            seno = traza(-5.3 + tt * 1.4, 2.4 + 0.4 * np.sin(2 * np.pi * 2 * tt), SENAL, 4.0)
            mon = moneda("", AMBAR).scale(0.9).move_to([4.6, 2.4, 0])
            self.play(Create(barra), FadeIn(e_i), FadeIn(e_d), Create(seno), FadeIn(mon), run_time=self.dur(0.8))

            # «un trozo lo dice todo»
            self.en("todo")
            t_i = Text("un trozo lo dice todo", color=SENAL).scale(0.55).move_to([-3.3, 0.55, 0])
            self.play(FadeIn(t_i, shift=UP * 0.15), run_time=self.dur(0.5))

            # «no dice nada»
            self.en("nada")
            t_d = Text("un trozo no dice nada", color=AMBAR).scale(0.55).move_to([3.3, 0.55, 0])
            self.play(FadeIn(t_d, shift=UP * 0.15), run_time=self.dur(0.5))

            # «suelen estar en medio»
            self.en("medio")
            centro = Dot([0, 1.2, 0], radius=0.2, color=TXT)
            t_r = Text("señales reales", color=TXT, weight=BOLD).scale(0.6).move_to([0, 1.95, 0])
            self.play(FadeIn(centro, scale=0.4), FadeIn(t_r, shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «dice algo de lo que valdrán»
            self.en("algo")
            L = Lienzo(ancho=9.0, alto=2.0, t_rango=(0, 1), v_max=2.4, centro=(0, -1.6))
            tl = np.linspace(0, 1, 200)
            sv = serie(77, 200, 0.96) * 0.85
            curva = L.curva(tl, sv, MEDIDA, 3.5)
            b = L.base()
            t1, t2 = 0.3, 0.62
            p1 = L.p(t1, float(np.interp(t1, tl, sv)))
            p2 = L.p(t2, float(np.interp(t2, tl, sv)))
            d1, d2 = Dot(p1, radius=0.12, color=AMBAR), Dot(p2, radius=0.12, color=AMBAR)
            arco = ArcBetweenPoints(p1 + UP * 0.35, p2 + UP * 0.35, angle=-PI / 2, color=AMBAR, stroke_width=4)
            l1 = Text("ahora", color=INK).scale(0.5).move_to([float(L.x(t1)), -3.15, 0])
            l2 = Text("un momento después", color=INK).scale(0.5).move_to([float(L.x(t2)), -3.15, 0])
            self.play(Create(b), Create(curva), run_time=self.dur(1.2), rate_func=linear)
            self.play(FadeIn(d1), FadeIn(d2), Create(arco), FadeIn(l1), FadeIn(l2), run_time=self.dur(0.9))

            # «pero no todo»
            self.en("no_todo")
            self.play(arco.animate.set_stroke(opacity=0.35), run_time=self.dur(0.6))

            # «mirar el ensemble de otra manera»
            self.en("ensemble")
            self.play(*[FadeOut(m) for m in (curva, d1, d2, arco, l1, l2)], run_time=0.3)
            pila = pila_de_curvas(L, 36, semilla=4, a=0.96, color=MEDIDA, opacidad=0.5, ancho=2.2, escala=0.4)
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.04), run_time=self.dur(2.2))

            # «los osciladores y la moneda»
            self.en("osc_moneda")
            self.play(seno.animate(rate_func=there_and_back).scale(1.3), mon.animate(rate_func=there_and_back).scale(1.3),
                      run_time=self.dur(0.9))

            # «nos van a acompañar todo el capítulo»
            self.en("acompanan")
            resto = [m for m in self.mobjects if m is not self.camera.frame and m not in (seno, mon)]
            self.play(*[FadeOut(m) for m in resto],
                      seno.animate.scale(0.6).move_to([-6.2, 3.45, 0]), mon.animate.scale(0.6).move_to([6.4, 3.45, 0]),
                      run_time=self.dur(1.0))
