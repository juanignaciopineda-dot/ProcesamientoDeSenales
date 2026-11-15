"""Escena 08 — El peso del ruido en el umbral, y por qué todos los criterios dan el mismo detector."""
from comun.escena import *

Y = -1.2                      # altura de la recta de g


def gamma_de(sg, p1):
    return sg * np.log((1 - p1) / p1) + 4.5


class ElPesoDelRuido(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.varianza()
        self.criterios()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def varianza(self):
        G = formula(r"\gamma", "=", r"\sigma^2", r"\ln\frac{p_0}{p_1}", "+", r"\frac{E}{2}", escala=1.5,
                    colores={0: AMBAR, 2: RUIDO}).move_to([0, 3.0, 0])
        recta = recta_g(Y)
        m0, m9 = marca_g(0, Y, INK, escala=0.7), marca_g(9, Y, SENAL, escala=0.7)
        um = umbral_g(4.5, Y)
        L = Lienzo(ancho=4.4, alto=1.8, t_rango=(-5, 5), v_max=1.15, centro=(-3.4, 1.3))
        ejeb = L.base()
        peq = campana_curva(L, 0, 0.5, RUIDO, 4.5)
        gra = campana_curva(L, 0, 2.0, RUIDO, 4.5)
        s_peq = MathTex(r"\sigma^2=0{,}25", color=RUIDO).scale(1.3).move_to([0.9, 1.3, 0])
        s_gra = MathTex(r"\sigma^2=4", color=RUIDO).scale(1.3).move_to([0.9, 1.3, 0])
        ap = Text("a priori", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.8, 1.3, 0])
        oido_ok = tilde(VERDE, 0.5).move_to([3.4, 1.3, 0])
        oido_no = cruz(ROJO, 0.5).move_to([3.4, 1.3, 0])
        u = subrayado(G[2], RUIDO)

        with self.narrar("b1"):
            # «La varianza del ruido»
            self.en("varianza")
            self.play(*[FadeIn(G[i], shift=UP * 0.1) for i in range(6)], run_time=self.dur(0.7))
            self.play(Create(u), run_time=self.dur(0.3))

            # «Multiplica al logaritmo»
            self.en("mult")
            self.play(Create(recta), FadeIn(m0), FadeIn(m9), Create(um[0]), FadeIn(um[1]), run_time=self.dur(0.8))
            self.play(Indicate(G[3], color=AMBAR, scale_factor=1.2), run_time=self.dur(0.5))

            # «muy pequeño»
            self.en("pequeno")
            self.play(Create(ejeb), Create(peq), FadeIn(s_peq), run_time=self.dur(0.8))

            # «se fía de lo que oye»
            self.en("fia")
            self.play(FadeIn(oido_ok), run_time=self.dur(0.4))

            # «casi no importan»
            self.en("casino")
            self.play(um.animate.shift(RIGHT * (gamma_de(0.25, 0.2) - 4.5)), run_time=self.dur(0.9))

            # «el ruido es grande»
            self.en("grande")
            self.play(um.animate.shift(LEFT * (gamma_de(0.25, 0.2) - 4.5)), FadeOut(oido_ok),
                      Transform(peq, gra), Transform(s_peq, s_gra), run_time=self.dur(0.9))

            # «vale poco»
            self.en("poco")
            self.play(FadeIn(oido_no), run_time=self.dur(0.4))

            # «lo que sabía de antemano»
            self.en("antemano")
            self.play(FadeOut(oido_no), FadeIn(ap, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «El umbral se mueve más»
            self.en("mueve")
            self.play(um.animate.shift(RIGHT * (gamma_de(4, 0.2) - 4.5)), run_time=self.dur(1.2))
        self.Gf = G
        self.fuera = [G, recta, m0, m9, um, ejeb, peq, s_peq, ap, u]
        self.wait(0.2)

    # ------------------------------------------------------------ b2
    def criterios(self):
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
        caja_g = caja("g ≷ γ", AMBAR, ancho=3.4, alto=1.3, scale=0.9).move_to([3.4, 1.6, 0])
        e = Text("error mínimo", color=TXT).scale(0.85).move_to([-4.0, 2.7, 0])
        n = Text("Neyman-Pearson", color=TXT).scale(0.85).move_to([-4.0, 1.6, 0])
        r = Text("riesgo mínimo", color=TXT).scale(0.85).move_to([-4.0, 0.2, 0])
        excl = Text("!", color=AMBAR, weight=BOLD).scale(2.0).move_to([0, 0.6, 0])
        cap9 = Text("Capítulo 9", color=INK).scale(0.6).move_to([-4.0, 3.65, 0])
        aw = [Arrow([-1.9, y, 0], [1.4, 1.6, 0], buff=0.05, color=INK, stroke_width=3,
                    max_tip_length_to_length_ratio=0.15) for y in (2.7, 1.6, 0.2)]
        calc = MathTex(r"g=\sum r[n]\,s[n]", color=MEDIDA).scale(1.3).move_to([3.4, 0.0, 0])
        ruido = campana_curva(Lienzo(ancho=2.2, alto=1.0, t_rango=(-4, 4), v_max=1.15, centro=(5.4, 3.0)), 0, 1.2, RUIDO, 4)
        recta = recta_g(-2.4)
        marcas = [(3.4, "NP", CIAN), (4.5, "MAP", AMBAR), (5.3, "riesgo", VERDE)]
        trio = VGroup()
        for gv, t, c in marcas:
            v = Line([gx(gv), -2.4 - 0.22, 0], [gx(gv), -2.4 + 0.5, 0], color=c, stroke_width=5)
            tx = Text(t, color=c).scale(0.7).next_to(v, DOWN, buff=0.12) if t != "MAP" else \
                Text(t, color=c).scale(0.7).next_to(v, UP, buff=0.12)
            trio.add(v, tx)

        with self.narrar("b2"):
            # «Una advertencia importante»
            self.en("aviso")
            self.pop(excl)

            # «la regla de error mínimo»
            self.en("map")
            self.play(FadeOut(excl), FadeIn(e, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «pruebas de hipótesis»
            self.en("cap9")
            self.play(FadeIn(cap9), run_time=self.dur(0.4))

            # «Neyman-Pearson»
            self.en("np")
            self.play(FadeIn(n, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «riesgo mínimo»
            self.en("riesgo")
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «Con un ruido como este»
            self.en("ruido")
            self.play(Create(ruido), run_time=self.dur(0.6))

            # «mismo detector»
            self.en("mismo")
            self.play(FadeIn(caja_g), *[GrowArrow(a) for a in aw], run_time=self.dur(0.9))

            # «calcular ge y compararlo»
            self.en("calcular")
            self.play(FadeIn(calc, shift=UP * 0.1), run_time=self.dur(0.7))

            # «dónde se pone el umbral»
            self.en("donde")
            self.play(Create(recta), *[FadeIn(m) for m in trio], run_time=self.dur(1.0))

            # «Veamos por qué»
            self.en("veamos")
            self.play(Create(SurroundingRectangle(caja_g, color=ESTIMACION, buff=0.15)), run_time=self.dur(0.6))
        self.wait(0.2)
