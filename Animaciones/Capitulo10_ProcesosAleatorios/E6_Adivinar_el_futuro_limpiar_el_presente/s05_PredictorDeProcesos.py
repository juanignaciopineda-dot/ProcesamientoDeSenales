"""Escena 05 — El predictor lineal de un proceso: la fórmula del capítulo 8 traducida a procesos."""
from comun.escena import *


class PredictorDeProcesos(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        # la fórmula del capítulo 8, arriba y pequeña
        yh = MathTex(r"\hat y", color=ESTIMACION)
        eq = MathTex("=", color=TXT)
        mu = MathTex(r"\mu_Y", color=TXT)
        mas = MathTex("+", color=TXT)
        fr = fraccion(MathTex(r"\sigma_{XY}", color=TXT), MathTex(r"\sigma_X^2", color=TXT))
        par = MathTex(r"(x-\mu_X)", color=TXT)
        vieja = VGroup(yh, eq, mu, mas, fr, par).arrange(RIGHT, buff=0.16).scale(1.0).move_to([0, 3.1, 0])

        self.P = PanelSensor(centro=(0, -2.25), ancho=9.0, alto=2.1, n=44, n0=30)
        P = self.P
        n0 = P.n0
        dahora = P.punto(n0, 3.0, AMBAR)
        y_arco = P.L.cy + 1.4
        arco = DoubleArrow([float(P.L.x(n0)), y_arco, 0], [float(P.L.x(n0 + 6)), y_arco, 0], buff=0, color=AMBAR,
                           stroke_width=4, max_tip_length_to_length_ratio=0.12)
        lm = MathTex("m", color=AMBAR).scale(0.8).next_to(arco, UP, buff=0.08)
        dfut = Circle(radius=0.1, color=INK, stroke_width=3).move_to(P.p(n0 + 6, 1.0))
        est = caja("estacionario", VERDE, alto=0.8, scale=0.6).move_to([5.5, -2.2, 0])

        igual = MathTex(r"\mu_Y=\mu_X=\mu_x", r"\qquad", r"\sigma_Y^2=\sigma_X^2=C_{xx}[0]", color=TXT).scale(1.0)
        igual.move_to([0, 1.7, 0])
        cm = MathTex(r"\sigma_{XY}=C_{xx}[m]", color=TXT).scale(1.0).move_to([0, 0.9, 0])

        yh2 = MathTex(r"\hat x[n_0+m]", color=ESTIMACION)
        eq2 = MathTex("=", color=TXT)
        mu2 = MathTex(r"\mu_x", color=TXT)
        mas2 = MathTex("+", color=TXT)
        self.fr2 = fraccion(MathTex(r"C_{xx}[m]", color=TXT), MathTex(r"C_{xx}[0]", color=TXT))
        par2 = MathTex(r"(x[n_0]-\mu_x)", color=TXT)
        nueva = VGroup(yh2, eq2, mu2, mas2, self.fr2, par2).arrange(RIGHT, buff=0.18).scale(1.2).move_to([0, 1.2, 0])
        self.nueva = nueva
        self.extras = [arco, lm, dfut, dahora, est]
        self.par2 = par2

        with self.narrar("b1"):
            # «Traducido a procesos»
            self.en("traduce")
            self.play(FadeIn(vieja), run_time=0.6)

            # «eme pasos más adelante»
            self.en("m")
            self.play(Create(P.media), FadeIn(P.rotulo_media), Create(P.pasado), Create(arco), FadeIn(lm),
                      FadeIn(dfut), run_time=self.dur(1.2))

            # «la de ahora»
            self.en("ahora")
            self.play(FadeIn(dahora, scale=2.0), run_time=0.4)

            # «es estacionario»
            self.en("estac")
            self.pop(est)

            # «la misma media y la misma varianza»
            self.en("igual")
            self.play(FadeIn(igual), run_time=0.7)

            # «su covarianza es la autocovarianza en eme»
            self.en("cm")
            self.play(FadeIn(cm), run_time=0.6)

            # «La predicción queda así»
            self.en("queda")
            self.play(FadeOut(igual), FadeOut(cm), run_time=0.3)
            self.play(FadeIn(yh2), FadeIn(eq2), FadeIn(mu2), run_time=0.6)

            # «más la autocovarianza en eme»
            self.en("num")
            self.play(FadeIn(mas2), FadeIn(self.fr2.num), Create(self.fr2.barra), run_time=0.6)

            # «dividida entre la autocovarianza en cero»
            self.en("c0")
            self.play(FadeIn(self.fr2.den), run_time=0.5)
            self.play(FadeIn(par2), run_time=0.5)

            # «se aparta de la media»
            self.en("aparta")
            self.resaltar(par2, color=AMBAR, escala=1.1)

    def parte_b2(self):
        P, n0 = self.P, self.P.n0
        fr2 = self.fr2
        caja_fr = SurroundingRectangle(fr2, color=AMBAR, buff=0.12, stroke_width=3.5)
        rho = MathTex(r"=\rho", color=AMBAR).scale(1.1).next_to(fr2, DOWN, buff=0.35)

        # dial de rho (0 a 1) y dos barras: el dato y la predicción
        rt = ValueTracker(0.6)
        dial = Line([-4.6, -2.3, 0], [-0.6, -2.3, 0], color=INK, stroke_width=4)
        t0 = MathTex("0", color=INK).scale(0.6).move_to([-4.6, -2.75, 0])
        t1 = MathTex("1", color=INK).scale(0.6).move_to([-0.6, -2.75, 0])
        lr = MathTex(r"\rho", color=AMBAR).scale(0.8).move_to([-2.6, -3.3, 0])
        marca = always_redraw(lambda: Dot([-4.6 + 4.0 * rt.get_value(), -2.3, 0], radius=0.17, color=AMBAR))
        base_y = -3.05
        piso = Line([2.3, base_y, 0], [6.3, base_y, 0], color=INK, stroke_width=2.5)
        b_dato = Rectangle(width=0.9, height=1.6, stroke_width=2, color=SENAL).set_fill(SENAL, 0.5)
        b_dato.move_to([3.3, base_y + 0.8, 0])
        b_pred = always_redraw(lambda: Rectangle(width=0.9, height=max(0.02, 1.6 * rt.get_value()), stroke_width=2,
                                                 color=AMBAR).set_fill(AMBAR, 0.5)
                               .move_to([5.3, base_y + max(0.02, 1.6 * rt.get_value()) / 2, 0]))
        ld = Text("dato", color=SENAL).scale(0.4).move_to([3.3, base_y - 0.3, 0])
        lp_ = Text("predicción", color=AMBAR).scale(0.4).move_to([5.3, base_y - 0.3, 0])

        with self.narrar("b2"):
            # «Ese cociente»
            self.en("cociente")
            self.play(Create(caja_fr), run_time=0.4)

            # «coeficiente de correlación»
            self.en("rho")
            self.play(FadeIn(rho), run_time=0.4)

            # «entre el presente y el futuro»
            self.en("entre")
            self.play(FadeOut(P.pasado), FadeOut(P.media), FadeOut(P.rotulo_media),
                      *[FadeOut(m) for m in self.extras], run_time=0.5)

            # «algo muy razonable»
            self.en("razonable")
            self.play(Create(dial), FadeIn(t0), FadeIn(t1), FadeIn(lr), FadeIn(marca), run_time=0.7)
            self.play(Create(piso), FadeIn(b_dato), FadeIn(b_pred), FadeIn(ld), FadeIn(lp_), run_time=0.7)

            # «muy correlacionados»
            self.en("alto")
            self.play(rt.animate.set_value(1.0), run_time=self.dur(1.2))

            # «le hacemos caso al dato»
            self.en("sigue")
            self.resaltar(b_pred, color=VERDE, escala=1.05)

            # «Si casi no lo están»
            self.en("bajo")
            self.play(rt.animate.set_value(0.05), run_time=self.dur(1.2))

            # «nos quedamos con la media»
            self.en("media0")
            self.resaltar(piso, color=INK, escala=1.05)

            # «Veamos cuánto caso le hacemos»
            self.en("veamos")
            marca.clear_updaters()
            b_pred.clear_updaters()
            self.play(FadeOut(dial), FadeOut(t0), FadeOut(t1), FadeOut(lr), FadeOut(marca), FadeOut(piso),
                      FadeOut(b_dato), FadeOut(b_pred), FadeOut(ld), FadeOut(lp_), run_time=0.4)

            # «en el sensor»
            self.en("sensor")
            self.play(Create(P.media), FadeIn(P.rotulo_media), Create(P.pasado), FadeIn(P.punto(n0, 3.0, AMBAR)),
                      run_time=self.dur(1.0))
