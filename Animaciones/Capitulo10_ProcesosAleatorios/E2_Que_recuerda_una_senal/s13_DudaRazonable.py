"""Escena 13 — ¿Basta con la media y la autocorrelación? Primera razón: el proceso gaussiano."""
from comun.escena import *


class DudaRazonable(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        d1 = formula("f_{X(t_1)}(x_1)", escala=0.8).move_to([-3.6, 2.4, 0])
        d2 = formula("f_{X(t_1)X(t_2)}(x_1,x_2)", escala=0.8).move_to([-3.6, 1.4, 0])
        d3 = formula("f_{X(t_1)X(t_2)X(t_3)}(x_1,x_2,x_3)", escala=0.8).move_to([-3.6, 0.4, 0])
        d4 = formula(r"\vdots", escala=0.9).move_to([-3.6, -0.5, 0])
        mu = caja_tex(r"\mu(t)", AMBAR, 1.9, 1.0, 0.95).move_to([3.4, 1.7, 0])
        rr = caja_tex(r"R(t_1,t_2)", AMBAR, 3.1, 1.0, 0.95).move_to([3.4, 0.4, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(2.0).move_to([0, 1.3, 0])
        b1 = caja_tex("1", AZUL, 1.0, 1.0, 1.0).move_to([-1.3, -2.4, 0])
        b2 = caja_tex("2", AZUL, 1.0, 1.0, 1.0).move_to([1.3, -2.4, 0])
        with self.narrar("b1"):
            # «Queda una duda razonable»
            self.en("duda")
            big = Text("?", color=AMBAR, weight=BOLD).scale(3.0).move_to([0, 1.3, 0])
            self.pop(big)

            # «la descripción completa del proceso»
            self.en("completa")
            self.play(FadeOut(big), FadeIn(d1, shift=RIGHT * 0.2), run_time=self.dur(0.6))

            # «la conjunta de todos los instantes»
            self.en("conjunta")
            self.play(LaggedStart(FadeIn(d2, shift=RIGHT * 0.2), FadeIn(d3, shift=RIGHT * 0.2), FadeIn(d4),
                                  lag_ratio=0.35), run_time=self.dur(1.3))

            # «dos funciones»
            self.en("dos_f")
            self.play(Create(mu.caja), Create(rr.caja), run_time=self.dur(0.6))

            # «la media y la autocorrelación»
            self.en("mu_r")
            self.play(FadeIn(mu.tex), FadeIn(rr.tex), run_time=self.dur(0.6))

            # «¿No estamos tirando demasiada información?»
            self.en("tirando")
            self.pop(q)

            # «Hay dos razones»
            self.en("razones")
            self.play(FadeOut(q), FadeIn(b1, shift=UP * 0.2), FadeIn(b2, shift=UP * 0.2), run_time=self.dur(0.7))

            # «conviene tenerlas presentes»
            self.en("presentes")
            self.play(b1.caja.animate(rate_func=there_and_back).scale(1.25).set_stroke(AMBAR),
                      b2.caja.animate(rate_func=there_and_back).scale(1.25).set_stroke(AMBAR), run_time=0.8)

            # «sostienen todo lo que queda de asignatura»
            self.en("sostienen")
            pilar = VGroup(*[Line([x, -2.9, 0], [x, -3.7, 0], color=AMBAR, stroke_width=8) for x in (-1.3, 1.3)])
            base = Line([-2.2, -3.7, 0], [2.2, -3.7, 0], color=AMBAR, stroke_width=8)
            self.play(Create(pilar), Create(base), run_time=self.dur(0.8))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        campana = Curva(lambda x: gaussiana(x, 0, 1), x_rango=(-3, 3), y_max=0.5, ancho=4.4, alto=2.2,
                        color=SENAL).move_to([-3.8, 0.5, 0])
        L = Lienzo(ancho=5.6, alto=3.0, t_rango=(0, 1), v_max=2.0, centro=(3.7, 0.5))
        pila = pila_de_curvas(L, 12, semilla=17, a=0.93, color=SENAL, opacidad=0.5, ancho=2.0, escala=0.45)
        t = np.linspace(0, 1, 160)
        with self.narrar("b2"):
            # «La primera es la gaussiana»
            self.en("primera")
            self.corte()
            uno = caja_tex("1", AZUL, 0.9, 0.9, 0.9).move_to([-6.2, 3.3, 0])
            w = self.palabra("gaussiana", AMBAR, 1.2).move_to([-3.6, 3.3, 0])
            self.play(FadeIn(uno), run_time=0.3)
            self.pop(w)

            # «una campana queda dibujada entera»
            self.en("campana")
            cap7 = etiqueta("capítulo 7", INK, 0.5).move_to([-3.8, 2.3, 0])
            self.play(FadeIn(cap7), Create(campana.ejes), Create(campana.grafica), run_time=self.dur(1.0))

            # «su media y su varianza»
            self.en("mu_sigma")
            lm = formula(r"\mu", escala=0.9, colores={0: AMBAR}).move_to(campana.ejes.c2p(0, 0) + DOWN * 0.45)
            ls = formula(r"\sigma", escala=0.9, colores={0: AMBAR}).move_to(campana.ejes.c2p(1.2, 0.3) + RIGHT * 0.3)
            self.pop(lm)
            self.pop(ls)

            # «Con los procesos pasa lo mismo»
            self.en("igual")
            self.play(Create(L.base()), LaggedStart(*[Create(c) for c in pila], lag_ratio=0.05), run_time=self.dur(1.3))

            # «cualquier grupo de muestras»
            self.en("grupo")
            cortes = [L.vertical(tt, AMBAR, 3) for tt in (0.2, 0.5, 0.8)]
            self.play(*[Create(c) for c in cortes], run_time=self.dur(0.6))

            # «conjuntamente gaussiano»
            self.en("gauss")
            xs = np.linspace(-1.2, 1.2, 40)
            bells = VGroup(*[traza(float(L.x(tt)) + 0.55 * gaussiana(xs, 0, 0.5), L.cy + xs * 0.9, AMBAR, 3)
                             for tt in (0.2, 0.5, 0.8)])
            self.play(LaggedStart(*[Create(b) for b in bells], lag_ratio=0.25), run_time=self.dur(1.0))

            # «determinan el proceso por completo»
            self.en("determinan")
            marco = SurroundingRectangle(pila, color=AMBAR, buff=0.2, stroke_width=3)
            et = formula(r"\mu(t)", ",", "C", escala=0.9, colores={0: AMBAR, 2: AMBAR}).next_to(marco, DOWN, buff=0.25)
            self.play(Create(marco), FadeIn(et), run_time=self.dur(0.8))

            # «No falta nada»
            self.en("nofalta")
            ok = tilde(VERDE, 1.0).move_to([-3.8, -2.2, 0])
            self.pop(ok)

            # «el ruido de los aparatos»
            self.en("aparatos")
            ap = chip(INK, "").scale(0.9).move_to([-5.2, -3.3, 0])
            ruido = traza(np.linspace(-4.2, -1.6, 90), -3.3 + 0.25 * serie(9, 90, 0.3), RUIDO, 3)
            self.play(FadeIn(ap), Create(ruido), run_time=self.dur(0.8))
