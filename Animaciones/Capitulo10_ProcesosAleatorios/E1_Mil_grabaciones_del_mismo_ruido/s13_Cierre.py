"""Escena 13 — Cierre: del proceso como familia de variables a la pregunta del siguiente episodio."""
from comun.escena import *

CONJUNTA = r"f_{X(t_1),X(t_2),X(t_3),\ldots,X(t_n)}(x_1,x_2,x_3,\ldots,x_n)"


class Cierre(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        L = Lienzo(ancho=10.4, alto=2.6, t_rango=(0, 1), v_max=2.4, centro=(0, 1.9))
        xs = [-4.5, -2.5, -0.5, 3.9]
        tcs = [float((x + 5.2) / 10.4) for x in xs]
        with self.narrar("b1"):
            # «una familia de variables»
            self.en("familia")
            pila = pila_de_curvas(L, 12, semilla=8, a=0.96, color=SENAL, opacidad=0.4, ancho=2.2, escala=0.5)
            cuts = VGroup(*[L.vertical(t, AMBAR, 3.0) for t in tcs])
            nombres = ["X(t_{1})", "X(t_{2})", "X(t_{3})", "X(t_{n})"]
            cajas = VGroup(*[caja_tex(n, AZUL, 1.6, 0.85, 0.9).move_to([x, -0.35, 0]) for n, x in zip(nombres, xs)])
            puntos = Text("⋯", color=TXT, weight=BOLD).scale(1.4).move_to([1.7, -0.35, 0])
            self.play(LaggedStart(*[Create(c) for c in pila], lag_ratio=0.04), run_time=0.9)
            self.play(LaggedStart(*[Create(c) for c in cuts], lag_ratio=0.15),
                      LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cajas], lag_ratio=0.15), FadeIn(puntos),
                      run_time=self.dur(1.0))

            # «una por cada instante»
            self.en("instante")
            enlaces = VGroup(*[DashedLine([x, 0.6, 0], [x, 0.05, 0], color=INK, dash_length=0.08, stroke_width=2.5)
                               for x in xs])
            eje = Line([-5.2, -1.6, 0], [5.2, -1.6, 0], color=INK, stroke_width=2.5)
            tiempos = VGroup(*[formula(n, color=AMBAR, escala=0.9).move_to([x, -2.05, 0])
                               for n, x in zip(["t_{1}", "t_{2}", "t_{3}", "t_{n}"], xs)])
            self.play(LaggedStart(*[Create(e) for e in enlaces], lag_ratio=0.15), Create(eje),
                      LaggedStart(*[FadeIn(t) for t in tiempos], lag_ratio=0.15), run_time=self.dur(1.4))

            # «inmanejable»
            self.en("imposible")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
            f = formula(CONJUNTA, color=TXT, escala=1.1).move_to([0, 0.3, 0])
            self.play(FadeIn(f), run_time=0.3)
            tach = tachar(f)
            self.play(Create(tach), run_time=self.dur(0.5))

            # «dos muestras separadas»
            self.en("dos_marcas")
            self.play(FadeOut(f), FadeOut(tach), run_time=0.25)
            M = Lienzo(ancho=10.4, alto=3.2, t_rango=(0, 1), v_max=2.6, centro=(0, 0.6))
            t = np.linspace(0, 1, 260)
            v = serie(71, 260, 0.96) * 0.9
            base = M.base()
            curva = M.curva(t, v, SENAL, 3.5)
            self.play(Create(base), Create(curva), run_time=0.9, rate_func=linear)
            t1 = 0.28
            tr = ValueTracker(0.55)
            d1 = Dot(M.p(t1, float(np.interp(t1, t, v))), radius=0.13, color=AMBAR)
            l1 = Line([float(M.x(t1)), M.cy - 1.6, 0], [float(M.x(t1)), M.cy + 1.6, 0], color=AMBAR, stroke_width=2.5)
            d2 = always_redraw(lambda: Dot(M.p(tr.get_value(), float(np.interp(tr.get_value(), t, v))), radius=0.13, color=AMBAR))
            l2 = always_redraw(lambda: Line([float(M.x(tr.get_value())), M.cy - 1.6, 0],
                                            [float(M.x(tr.get_value())), M.cy + 1.6, 0], color=AMBAR, stroke_width=2.5))
            ar = always_redraw(lambda: DoubleArrow([float(M.x(t1)), -1.55, 0], [float(M.x(tr.get_value())), -1.55, 0],
                                                   color=AMBAR, stroke_width=4, buff=0))
            tau = always_redraw(lambda: formula(r"\tau", color=AMBAR, escala=1.1).move_to(
                [float((M.x(t1) + M.x(tr.get_value())) / 2), -2.05, 0]))
            self.play(FadeIn(d1), Create(l1), FadeIn(d2), Create(l2), GrowFromCenter(ar), FadeIn(tau), run_time=self.dur(0.7))

            # «qué recuerda la señal»
            self.en("recuerda")
            self.play(tr.animate.set_value(0.85), run_time=1.2, rate_func=smooth)
            self.play(tr.animate.set_value(0.38), run_time=1.4, rate_func=smooth)
            self.play(tr.animate.set_value(0.6), run_time=self.dur(0.8), rate_func=smooth)
            for m in (d2, l2, ar, tau):
                m.clear_updaters()

            # «la media»
            self.en("media")
            self.play(*[FadeOut(m) for m in (base, curva, d1, d2, l1, l2, ar, tau)], run_time=0.2)
            A = Lienzo(ancho=4.6, alto=2.2, t_rango=(0, 1), v_max=2.0, centro=(-3.2, 0.4))
            Bx = Lienzo(ancho=4.6, alto=2.2, t_rango=(-1, 1), v_max=2.0, centro=(3.2, 0.4))
            plana = A.curva([0, 1], [0.6, 0.6], AMBAR, 5)
            t_m = etiqueta("media", TXT, 0.8, BOLD).move_to([-3.2, -1.3, 0])
            self.play(Create(A.base()), Create(plana), FadeIn(t_m), run_time=self.dur(0.5))

            # «la autocorrelación»
            self.en("autoc")
            tt = np.linspace(-1, 1, 160)
            deca = Bx.curva(tt, 1.6 * np.exp(-3.0 * np.abs(tt)) - 0.2, AMBAR, 5)
            t_a = etiqueta("autocorrelación", TXT, 0.8, BOLD).move_to([3.2, -1.3, 0])
            self.play(Create(Bx.base()), Create(deca), FadeIn(t_a), run_time=self.dur(0.6))

            # «resumiremos el proceso entero»
            self.en("resumen")
            marco = SurroundingRectangle(VGroup(plana, t_m, deca, t_a), color=AMBAR, buff=0.35, corner_radius=0.2,
                                         stroke_width=3)
            self.play(Create(marco), run_time=self.dur(0.7))

            # «¿qué recuerda una señal?»
            self.en("titulo_e2")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
            prox = etiqueta("Próximo episodio", INK, 0.8).move_to([0, 1.3, 0])
            tit = Text("¿Qué recuerda una señal?", color=AMBAR, weight=BOLD).scale(1.3).move_to([0, 0.2, 0])
            self.play(FadeIn(prox), run_time=0.3)
            self.pop(tit)
        self.wait(1.0)
        self.limpiar()
