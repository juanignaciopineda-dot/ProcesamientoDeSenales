"""Escena 06 — Comprobar con los cuatro osciladores que R(¼, ½) = R(0, ¼) = 0."""
from comun.escena import *


class ComprobarOsciladores(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        cos = CuatroCosenos(ancho=6.0, paso=1.5, amp=0.55, centro=(3.7, -0.1))
        T = TablaCortes(["0°", "90°", "180°", "270°"], x0=-6.6, y0=2.4, n_col=3)
        c1 = Text("1  la media es constante", color=TXT).scale(0.5).move_to([-4.2, -2.3, 0])
        c2 = Text("2  R depende solo de la separación", color=TXT).scale(0.5).move_to([-3.75, -3.0, 0])
        c1.align_to(c2, LEFT)

        def marca_ok(fila):
            return tilde(VERDE, 0.28).next_to(fila, LEFT, buff=0.2)

        def flecha_sep(t0, t1):
            y = -3.55
            f = DoubleArrow([float(cos.x(t0)), y, 0], [float(cos.x(t1)), y, 0], color=AMBAR, buff=0, stroke_width=4,
                            max_tip_length_to_length_ratio=0.25)
            q = etiqueta("¼", AMBAR, 0.6, BOLD).next_to(f, UP, buff=0.05)
            return VGroup(f, q)

        with self.narrar("b1"):
            # «los cuatro osciladores desfasados»
            self.en("cuatro")
            self.play(FadeIn(cos.bases[0]), FadeIn(cos.bases[1]), FadeIn(cos.bases[2]), FadeIn(cos.bases[3]),
                      *[Create(c) for c in cos.curvas], FadeIn(cos.rotulos), run_time=self.dur(1.0))

            # «La media es cero»
            self.en("media0")
            medias = VGroup(*[Line(b.get_start(), b.get_end(), color=AMBAR, stroke_width=4) for b in cos.bases])
            self.play(Create(medias), FadeIn(c1, shift=UP * 0.1), FadeIn(c2, shift=UP * 0.1), run_time=self.dur(0.7))

            # «primera condición»
            self.en("primera")
            t1 = marca_ok(c1)
            self.pop(t1)

            # «entre cero y un cuarto de período»
            self.en("cero_cuarto")
            ca, cb = cos.corte(0.0), cos.corte(0.25)
            fl = flecha_sep(0.0, 0.25)
            self.play(Create(ca), Create(cb), FadeIn(fl), run_time=self.dur(0.7))

            # «era cero»
            self.en("era0")
            r0 = MathTex("R", "=", "0", color=AMBAR).scale(0.9).move_to([-4.6, -1.5, 0])
            self.play(FadeIn(r0), run_time=0.4)

            # «Entre un cuarto y medio período»
            self.en("cuarto_medio")
            d = float(cos.x(0.25) - cos.x(0.0))
            fl2 = flecha_sep(0.25, 0.5)
            self.play(ca.animate.shift(RIGHT * d), cb.animate.shift(RIGHT * d), ReplacementTransform(fl, fl2),
                      run_time=self.dur(0.8))

            # «la separación es la misma»
            self.en("misma")
            self.resaltar(fl2)

            # «debería dar lo mismo»
            self.en("deberia")
            rq = MathTex("R", "=", "?", color=AMBAR).scale(0.9).move_to(r0)
            self.play(ReplacementTransform(r0, rq), run_time=0.4)

            # «cero, menos uno, cero y uno»
            self.en("vals1")
            self.play(FadeIn(T.armazon()), FadeIn(T.enc(0, "¼")), FadeIn(T.enc(1, "½")), FadeIn(T.enc(2, "×")),
                      run_time=self.dur(0.5))
            v1 = [T.celda(0, i, s) for i, s in enumerate(["0", "−1", "0", "1"])]
            self.play(LaggedStart(*[FadeIn(c) for c in v1], lag_ratio=0.25), run_time=self.dur(1.0))

            # «menos uno, cero, uno y cero»
            self.en("vals2")
            v2 = [T.celda(1, i, s) for i, s in enumerate(["−1", "0", "1", "0"])]
            self.play(LaggedStart(*[FadeIn(c) for c in v2], lag_ratio=0.25), run_time=self.dur(1.0))

            # «Todos los productos son cero»
            self.en("prods0")
            v3 = [T.celda(2, i, "0", AMBAR) for i in range(4)]
            self.play(LaggedStart(*[FadeIn(c) for c in v3], lag_ratio=0.15), run_time=self.dur(0.7))
            self.pop(T.prom(2, "0"))

            # «Cumplido»
            self.en("cumplido")
            r_ok = MathTex("R", "=", "0", color=AMBAR).scale(0.9).move_to(rq)
            self.play(ReplacementTransform(rq, r_ok), run_time=0.3)
            t2 = marca_ok(c2)
            self.pop(t2)
        self.wait(1.0)
        self.limpiar()
