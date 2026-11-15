"""Escena 07 — R_XX(τ) con un solo argumento; el sensor es WSS, los osciladores en fase no."""
from comun.escena import *


class QuienEsEstacionario(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        L = Lienzo(ancho=5.6, alto=1.9, t_rango=(0, 1), v_max=3.0, centro=(-1.1, -1.0))
        t = np.linspace(0, 1, 220)
        serie_s = 0.8 * serie(41, 220, 0.9)
        pal = Palitos(range(0, 6), [4, 2.4, 1.44, 0.86, 0.52, 0.31], ancho=3.4, alto=2.0, v_max=4.0, centro=(4.7, -1.0))

        with self.narrar("b1"):
            # «las dos condiciones»
            self.en("dos_cond")
            ca = VGroup(tilde(VERDE, 0.28), Text("la media es constante", color=TXT).scale(0.5)).arrange(RIGHT, buff=0.2)
            cb = VGroup(tilde(VERDE, 0.28), Text("R solo depende de la separación", color=TXT).scale(0.5)).arrange(RIGHT, buff=0.2)
            cond = VGroup(ca, cb).arrange(RIGHT, buff=0.9).move_to([0, 3.4, 0])
            self.play(FadeIn(cond, shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «un solo argumento»
            self.en("un_arg")
            f1 = formula("R_{XX}", "(", "t_1", ",", "t_2", ")", escala=1.3).move_to([0, 1.9, 0])
            self.play(FadeIn(f1), run_time=0.4)
            self.resaltar(f1[2:5], color=AMBAR)

            # «erre sub equis equis de tau»
            self.en("r_tau")
            f2 = formula("R_{XX}", "(", r"\tau", ")", escala=1.3, colores={2: AMBAR}).move_to([0, 1.9, 0])
            self.play(ReplacementTransform(f1, f2), run_time=self.dur(0.7))

            # «El sensor de temperatura»
            self.en("sensor")
            term = termometro(1.5, ROJO, 0.55).move_to([-6.0, -0.7, 0])
            txt20 = etiqueta("20 °C", TXT, 0.5).next_to(term, DOWN, buff=0.15)
            base = L.base()
            cur = L.curva(t, 1.0 * serie_s, AZUL, 3.2)
            self.play(FadeIn(term), FadeIn(txt20), Create(base), Create(cur), run_time=self.dur(1.2))

            # «estacionario en sentido amplio»
            self.en("wss")
            s = sello("WSS", VERDE).move_to([-5.6, 1.4, 0])
            self.pop(s)

            # «su media es veinte siempre»
            self.en("media20")
            m20 = Line(L.p(0, 0), L.p(1, 0), color=AMBAR, stroke_width=4)
            l20 = etiqueta("20", AMBAR, 0.6, BOLD).move_to([2.05, -1.0, 0])
            self.play(Create(m20), FadeIn(l20), run_time=self.dur(0.6))

            # «su covarianza solo depende»
            self.en("cov")
            self.play(FadeIn(pal.base), *[Create(k) for k in pal.tallos], *[FadeIn(p) for p in pal.puntos], run_time=self.dur(0.8))
            vals = VGroup(*[etiqueta(x, AMBAR, 0.42).next_to(pal.puntos[i], UP, buff=0.1)
                            for i, x in enumerate(["4", "2,4", "1,44"])])
            self.play(FadeIn(vals), run_time=0.3)

            # «cuántos pasos separan las muestras»
            self.en("pasos")
            y0 = -2.55
            a1 = DoubleArrow([pal.pos(0)[0], y0, 0], [pal.pos(1)[0], y0, 0], color=AMBAR, buff=0, stroke_width=3.5,
                             max_tip_length_to_length_ratio=0.3)
            a2 = DoubleArrow([pal.pos(0)[0], y0 - 0.55, 0], [pal.pos(2)[0], y0 - 0.55, 0], color=AMBAR, buff=0, stroke_width=3.5,
                             max_tip_length_to_length_ratio=0.2)
            e1 = etiqueta("1 paso", AMBAR, 0.4).next_to(a1, RIGHT, buff=0.15)
            e2 = etiqueta("2 pasos", AMBAR, 0.4).next_to(a2, RIGHT, buff=0.15)
            self.play(FadeIn(a1), FadeIn(e1), FadeIn(a2), FadeIn(e2), run_time=self.dur(0.9))

            # «los osciladores que arrancan a la vez»
            self.en("arrancan")
            self.play(*[FadeOut(m) for m in (term, txt20, base, cur, m20, l20, pal, vals, a1, a2, e1, e2)], run_time=0.3)
            cf = CuatroEnFase(ancho=8.0, paso=1.3, amp=0.28, centro=(0.6, -0.9))
            self.play(*[Create(c) for c in cf.curvas], *[FadeIn(b) for b in cf.bases], FadeIn(cf.rotulos), run_time=self.dur(1.0))

            # «no lo son»
            self.en("no_son")
            x = cruz(ROJO, 1.4).move_to(s)
            self.play(FadeIn(x, scale=1.4), run_time=0.4)

            # «su media sube y baja»
            self.en("sube")
            self.play(*[c.animate.set_stroke(opacity=0.3) for c in cf.curvas], run_time=0.3)
            L2 = Lienzo(ancho=8.0, alto=2.8, t_rango=(-0.25, 1.75), v_max=2.4, centro=(0.6, -0.9))
            tt = np.linspace(-0.25, 1.75, 200)
            media = L2.curva(tt, 2 * np.cos(2 * np.pi * tt), AMBAR, 5)
            self.play(Create(media), run_time=self.dur(1.2), rate_func=linear)
        self.wait(1.0)
        self.limpiar()
