"""Escena 03 — La memoria del ruido: dos muestras con correlación 0,6 y un pulso (2, 0)."""
from comun.escena import *


class LaMemoriaDelRuido(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.memoria()
        self.pulso()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def memoria(self):
        rng = np.random.default_rng(4)
        sueltas = Tallos(list(np.clip(rng.normal(0, 1, 10), -1.6, 1.6)), centro=(0, 1.2), paso=0.95,
                         unidad=0.7, color=RUIDO)
        con_mem = Tallos(list(np.clip(ruido_ar(10, 0.85, 6), -1.6, 1.6)), centro=(0, 1.2), paso=0.95,
                         unidad=0.7, color=RUIDO)
        a, b = 4, 5
        arco = CurvedArrow(con_mem.pos(a) + UP * 0.1, con_mem.pos(b) + UP * 0.1, angle=-PI / 2.4,
                           color=AMBAR, stroke_width=5)
        por = MathTex(r"\times\, 0{,}6", color=AMBAR).scale(0.8).next_to(arco, UP, buff=0.1)
        fantasma = Line(con_mem.x(b) * RIGHT + UP * 1.2, con_mem.x(b) * RIGHT + UP * (1.2 + con_mem.valores[a] * 0.6 * 0.7),
                        color=AMBAR, stroke_width=5, stroke_opacity=0.9)
        P = PlanoV(centro=(0, -0.9), lado=2.2, esc=1.0)
        s1 = MathTex(r"\sigma^2 = 1", color=INK).scale(0.65).next_to(P.ejes[0].get_end(), DOWN, buff=0.35)
        s2 = MathTex(r"\sigma^2 = 1", color=INK).scale(0.65).next_to(P.ejes[1].get_end(), LEFT, buff=0.35)
        nube = P.puntos(0.6, n=34)
        el = P.elipse(0.6)
        rho = MathTex(r"\rho = 0{,}6", color=AMBAR).scale(0.9).move_to([4.9, -0.9, 0])

        with self.narrar("b1"):
            # «independiente del de las demás»
            self.en("indep")
            self.play(Create(sueltas.base), *[Create(sueltas.palito(i)) for i in range(10)], run_time=self.dur(0.9))

            # «muchos ruidos tienen memoria»
            self.en("memoria")
            self.play(ReplacementTransform(sueltas, con_mem), run_time=self.dur(1.0))

            # «el eco del cero coma seis»
            self.en("eco")
            self.play(Create(arco), FadeIn(por), run_time=self.dur(0.7))

            # «se parece un sesenta por ciento a la anterior»
            self.en("sesenta")
            self.play(Create(fantasma), run_time=self.dur(0.6))

            # «dos muestras seguidas»
            self.en("dos")
            self.corte()
            self.play(Create(P.ejes), FadeIn(P.rot0), FadeIn(P.rot1), run_time=self.dur(0.6))
            self.play(FadeIn(Dot(P.p(0.8, 0.3), radius=0.09, color=RUIDO)), run_time=0.3)

            # «varianza uno cada una»
            self.en("var1")
            self.play(FadeIn(s1), FadeIn(s2), run_time=self.dur(0.5))

            # «una correlación de cero coma seis»
            self.en("corr")
            self.play(FadeIn(nube), Create(el), run_time=self.dur(0.8))
            self.play(FadeIn(rho), run_time=self.dur(0.4))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def pulso(self):
        S = Tallos([2, 0], centro=(-5.0, 1.2), paso=1.2, unidad=0.8, color=SENAL, indices=True)
        rs = MathTex(r"s = (2,\ 0)", color=SENAL).scale(1.0).next_to(S, DOWN, buff=0.5).shift(RIGHT * 0.1)
        h1 = MathTex("H_1", color=AMBAR).scale(1.1).move_to([-5.0, 3.5, 0])
        r0 = MathTex("r_0", "=", "2", "+", "v_0", color=TXT).scale(1.2).move_to([0.2, 2.6, 0])
        r0[0].set_color(MEDIDA); r0[2].set_color(SENAL); r0[4].set_color(RUIDO)
        r1 = MathTex("r_1", "=", "v_1", color=TXT).scale(1.2).move_to([-0.5, 1.3, 0])
        r1[0].set_color(MEDIDA); r1[2].set_color(RUIDO)
        ver = ojo(INK).scale(1.0).move_to([4.2, 2.6, 0])
        tach = Line(r1.get_corner(DL) + DL * 0.08, r1.get_corner(UR) + UR * 0.08, color=ERROR, stroke_width=6)
        # campanas bajo cada hipótesis
        L = Lienzo(ancho=5.5, alto=2.4, t_rango=(-2.5, 4.5), v_max=0.45, centro=(-3.4, -2.8))
        base = L.base()
        h0 = curva_f(L, lambda x: gaussiana(x, 0, 1), -2.5, 4.5, color=RUIDO, ancho=3.5)
        h1c = curva_f(L, lambda x: gaussiana(x, 2, 1), -2.5, 4.5, color=SENAL, ancho=4)
        l2 = DashedLine(L.p(2, 0), L.p(2, 0.42), color=SENAL, stroke_width=2.5)
        t2 = MathTex("2", color=SENAL).scale(0.6).next_to(L.p(2, 0), DOWN, buff=0.12)
        umbral = DashedLine(L.p(1, 0), L.p(1, 0.42), color=AMBAR, stroke_width=3)
        cola = area_f(L, lambda x: gaussiana(x, 2, 1), -2.5, 1, color=ERROR, opacidad=0.55)
        var = MathTex(r"\sigma^2 = 1", color=INK).scale(0.65).move_to(L.p(4.3, 0.62))
        d2 = MathTex(r"d^2 = \frac{4}{1} = 4", color=TXT).scale(1.1).move_to([3.4, -1.6, 0])
        pe = formula("P_e", "=", "Q(1)", "=", num_tex(0.1587, 4), escala=1.1,
                     colores={0: ERROR, 2: ERROR, 4: ERROR}).move_to([3.4, -2.9, 0])

        with self.narrar("b2"):
            # «un pulso de una sola muestra»
            self.en("pulso")
            self.corte()
            self.play(Create(S.base), Create(S.palito(0)), FadeIn(S.ks), run_time=self.dur(0.6))

            # «dos, cero»
            self.en("dos0")
            self.play(Create(S.palito(1)), FadeIn(rs), run_time=self.dur(0.5))

            # «Bajo la hipótesis uno»
            self.en("h1")
            self.pop(h1)

            # «dos más el ruido de la primera muestra»
            self.en("r0")
            self.play(FadeIn(r0, shift=UP * 0.1), run_time=self.dur(0.7))

            # «y el ruido de la segunda»
            self.en("r1")
            self.play(FadeIn(r1, shift=UP * 0.1), run_time=self.dur(0.6))

            # «El detector ingenuo»
            self.en("ingenuo")
            self.play(FadeIn(ver), Create(tach), run_time=self.dur(0.6))

            # «media dos»
            self.en("media")
            self.play(Create(base), Create(h1c), run_time=self.dur(0.7))
            self.play(Create(l2), FadeIn(t2), run_time=self.dur(0.4))

            # «varianza uno»
            self.en("var")
            self.play(FadeIn(var), run_time=self.dur(0.4))

            # «relación cuatro»
            self.en("rel4")
            self.play(FadeIn(d2, shift=UP * 0.1), run_time=self.dur(0.6))

            # «cu de uno»
            self.en("qu")
            self.play(Create(h0), Create(umbral), FadeIn(cola), run_time=self.dur(0.7))
            self.play(*[FadeIn(pe[i]) for i in range(3)], run_time=self.dur(0.4))

            # «cero coma uno cinco ocho siete»
            self.en("pe")
            self.play(FadeIn(pe[3]), FadeIn(pe[4]), run_time=self.dur(0.5))
