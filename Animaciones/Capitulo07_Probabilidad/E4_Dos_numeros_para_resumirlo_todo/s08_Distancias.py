"""Escena 08 — Distancias a la media: sumarlas se cancela; elevarlas al cuadrado da la varianza."""
from comun.escena import *


def campana(cx, cy, sigma, color, ancho=1.0, alto=2.0):
    """Campana sencilla centrada en (cx, cy) (la base está en cy), en coordenadas de pantalla."""
    xs = np.linspace(-4, 4, 160)
    ys = np.exp(-0.5 * (xs / sigma) ** 2)
    return traza(cx + xs * ancho, cy + ys * alto, color, 4)


class Distancias(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        self.R = R = Regla7(centro=(0, 1.2), ancho=10.2, v0=0.4, v1=6.6)
        self.caras = caras7(R, escala=0.8, altura=1.4)
        estrecha = campana(0, -1.4, 0.7, SENAL)
        ancha = campana(0, -1.4, 1.6, ESTIMACION)
        base_c = Line([-4.2, -1.4, 0], [4.2, -1.4, 0], color=INK, stroke_width=2)
        mu_c = DashedLine([0, -1.4, 0], [0, 1.3, 0], color=AMBAR, stroke_width=3)
        mu_t = MathTex(r"\mu", color=AMBAR).scale(1.1).move_to([0.45, 1.4, 0])
        x_p = Dot([1.9, -1.4 + float(np.exp(-0.5 * (1.9 / 1.1) ** 2 / 1.0)) * 0.0, 0], radius=0.1, color=TXT)
        x_p.move_to([1.9, -1.4, 0])
        d_fl = DoubleArrow([0, -1.0, 0], [1.9, -1.0, 0], color=AMBAR, stroke_width=4, buff=0)
        d_t = MathTex("X-", r"\mu", color=AMBAR).scale(0.9).move_to([0.95, -0.6, 0])
        dist = {}
        vals = {1: "-2{,}5", 2: "-1{,}5", 3: "-0{,}5", 4: "0{,}5", 5: "1{,}5", 6: "2{,}5"}
        flechas_d = VGroup()
        for v in range(1, 7):
            k = abs(v - 3.5)
            nivel = {0.5: 0.54, 1.5: 0.72, 2.5: 0.9}[k]
            flechas_d.add(flecha(R.p(3.5) + UP * nivel, R.p(v) + UP * nivel, AMBAR, 3))
        self.flechas_d = flechas_d
        rot = {v: MathTex(vals[v], color=(ROJO if v < 4 else VERDE)).scale(0.7).move_to(R.p(v) + DOWN * 0.8)
               for v in range(1, 7)}
        self.rot = rot
        suma = MathTex("-2{,}5", "-1{,}5", "-0{,}5", "+0{,}5", "+1{,}5", "+2{,}5", color=TXT
                       ).scale(0.95).arrange(RIGHT, buff=0.15).move_to([-1.0, -2.3, 0])
        cero = MathTex("=", "0", color=VERDE).scale(1.3).next_to(suma, RIGHT, buff=0.3)
        self.suma, self.cero = suma, cero
        with self.narrar("b1"):
            # «Queremos medir cuánto se aleja»
            self.en("medir")
            self.play(Create(base_c), Create(estrecha), Create(ancha), run_time=self.dur(1.2))
            # «una variable de su media»
            self.en("variable")
            self.play(Create(mu_c), FadeIn(mu_t), run_time=self.dur(0.7))
            # «promediar las distancias a la media»
            self.en("distancias")
            self.play(FadeIn(x_p), GrowFromCenter(d_fl), FadeIn(d_t), run_time=self.dur(1.0))

            # «Con el dado»
            self.en("con_dado")
            self.corte()
            self.play(FadeIn(R), FadeIn(self.caras), run_time=self.dur(0.7))
            # «tres coma cinco son»
            self.en("a_35")
            filo = DashedLine(R.p(3.5) + UP * 0.4, R.p(3.5) + UP * 1.2, color=AMBAR, stroke_width=3)
            self.play(Create(filo), LaggedStart(*[GrowArrow(a) for a in flechas_d], lag_ratio=0.1),
                      run_time=self.dur(1.3))

            # «menos dos coma cinco»
            self.en("d1")
            self.play(FadeIn(rot[1], shift=UP * 0.1), run_time=0.3)
            # «menos uno coma cinco»
            self.en("d2")
            self.play(FadeIn(rot[2], shift=UP * 0.1), run_time=0.3)
            # «menos cero coma cinco»
            self.en("d3")
            self.play(FadeIn(rot[3], shift=UP * 0.1), run_time=0.3)
            # «las mismas en positivo»
            self.en("positivo")
            self.play(FadeIn(VGroup(rot[4], rot[5], rot[6]), shift=UP * 0.1), run_time=self.dur(0.7))

            # «Súmalas»
            self.en("sumalas")
            self.play(LaggedStart(*[FadeIn(s) for s in suma], lag_ratio=0.12), run_time=self.dur(0.9))
            # «dan cero»
            self.en("cero")
            self.play(FadeIn(cero, shift=LEFT * 0.15), run_time=self.dur(0.5))
            # «cancelan a las del otro»
            self.en("cancelan")
            self.play(*[Indicate(flechas_d[i], color=ROJO) for i in range(3)],
                      *[Indicate(flechas_d[i], color=VERDE) for i in range(3, 6)], run_time=self.dur(1.0))
            # «Así no sirve»
            self.en("no_sirve")
            x = cruz(ROJO, 1.0).move_to(VGroup(suma, cero).get_center())
            self.play(Create(x), run_time=self.dur(0.4))
            self.sfx("error")
            self.x_cruz = x

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        R = self.R
        cuadrados = {}
        lado = lambda v: abs(v - 3.5) * 0.7
        for v in range(1, 7):
            cuadrados[v] = Square(side_length=lado(v), color=ESTIMACION, stroke_width=3
                                  ).set_fill(ESTIMACION, 0.3).move_to(R.p(v) + DOWN * 2.5)
        valores = {1: "6{,}25", 2: "2{,}25", 3: "0{,}25"}
        txt = {v: MathTex(valores[min(v, 7 - v)], color=TXT).scale(0.7).move_to(R.p(v) + DOWN * 3.8)
               for v in range(1, 7)}
        prom = MathTex(r"\frac{6{,}25+2{,}25+0{,}25+0{,}25+2{,}25+6{,}25}{6}", color=TXT).scale(0.8
                      ).move_to([-2.8, -3.6, 0])
        p292 = MathTex(r"\approx", "2{,}92", color=TXT).scale(1.3).next_to(prom, RIGHT, buff=0.3)
        p292[1].set_color(VERDE)
        pal = self.palabra("Varianza", AMBAR, 1.0).move_to([-4.6, 3.4, 0])
        F = MathTex("E[", r"(X-\mu)^2", "]", "=", r"\sigma^2", color=TXT).scale(1.3).move_to([1.8, 3.4, 0])
        F[4].set_color(AMBAR)
        with self.narrar("b2"):
            # «elevar cada distancia al cuadrado»
            self.en("cuadrado")
            self.play(FadeOut(self.suma), FadeOut(self.cero), FadeOut(self.x_cruz), FadeOut(self.flechas_d),
                      run_time=0.4)
            self.play(LaggedStart(*[FadeIn(cuadrados[v], scale=0.3) for v in range(1, 7)], lag_ratio=0.12),
                      run_time=self.dur(1.2))
            # «todas sean positivas»
            self.en("positivas")
            self.play(*[self.rot[v].animate.set_color(VERDE) for v in range(1, 7)],
                      *[cuadrados[v].animate.set_stroke(VERDE).set_fill(VERDE, 0.3) for v in range(1, 7)],
                      run_time=self.dur(0.8))
            # «Seis coma veinticinco»
            self.en("c1")
            self.play(FadeIn(txt[1], shift=UP * 0.1), run_time=0.3)
            # «dos coma veinticinco»
            self.en("c2")
            self.play(FadeIn(txt[2], shift=UP * 0.1), run_time=0.3)
            # «cero coma veinticinco»
            self.en("c3")
            self.play(FadeIn(txt[3], shift=UP * 0.1), run_time=0.3)
            # «el otro lado»
            self.en("otro")
            self.play(FadeIn(VGroup(txt[4], txt[5], txt[6]), shift=UP * 0.1), run_time=self.dur(0.6))

            # «Su promedio»
            self.en("prom")
            self.play(FadeIn(prom, shift=DOWN * 0.15), run_time=self.dur(0.8))
            # «dos coma noventa y dos»
            self.en("p292")
            self.play(FadeIn(p292, shift=LEFT * 0.15), run_time=self.dur(0.6))

            # «Eso es la varianza»
            self.en("varianza")
            self.pop(pal)
            # «la esperanza de la distancia a la media»
            self.en("formula")
            self.play(FadeIn(F[0:4], shift=DOWN * 0.15), run_time=self.dur(1.5))
            # «sigma cuadrado»
            self.en("sigma2")
            self.play(FadeIn(F[4], shift=LEFT * 0.15), run_time=self.dur(0.6))
