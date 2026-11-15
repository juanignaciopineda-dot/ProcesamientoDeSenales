"""Escena 13 — El filtro multiplica la densidad por |H|²; el área sobre una banda es su potencia."""
from comun.escena import *


class PotenciaEnUnaBanda(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        bloque = BloqueLTI("H", centro=(0, 1.7), ancho=2.0, alto=1.2, color=CIAN)
        Li = Lienzo(ancho=2.2, alto=1.6, t_rango=(0, 1), v_max=3.2, centro=(-4.9, 1.7))
        Lo = Lienzo(ancho=2.2, alto=1.6, t_rango=(0, 1), v_max=3.2, centro=(4.9, 1.7))
        s_in = seno_t(Li, 2, 1.0, SENAL)
        s_out = seno_t(Lo, 2, 3.0, SENAL)
        F = formula("S_{yy}", "=", "|H|^2", "S_{xx}", escala=1.3, colores={0: AMBAR}).move_to([0, -2.2, 0])
        with self.narrar("b1"):
            # «¿Qué hace un filtro con la potencia?»
            self.en("pregunta")
            q = etiqueta("¿Qué hace un filtro con la potencia?", TXT, 0.65).move_to([0, 3.5, 0])
            self.play(FadeIn(bloque), FadeIn(q), run_time=self.dur(0.7))

            # «Multiplica la amplitud»
            self.en("amp")
            self.play(Create(Li.base()), Create(s_in), run_time=self.dur(0.8), rate_func=linear)

            # «por su ganancia»
            self.en("suganancia")
            gl = etiqueta("ganancia", CIAN, 0.55).move_to([0, 0.5, 0])
            self.pop(gl)

            # «el cuadrado de la amplitud»
            self.en("cuadamp")
            ca = etiqueta("potencia ~ amplitud²", INK, 0.55).move_to([0, -0.5, 0])
            self.pop(ca)

            # «si la ganancia es tres»
            self.en("g3")
            g3 = etiqueta("ganancia = 3", CIAN, 0.55).move_to(gl)
            self.play(ReplacementTransform(gl, g3), Create(Lo.base()), Create(s_out), run_time=self.dur(1.0),
                      rate_func=linear)

            # «la potencia se multiplica por nueve»
            self.en("p9")
            p9 = etiqueta("potencia × 9", AMBAR, 0.7).move_to([4.9, 0.4, 0])
            self.pop(p9)

            # «Por eso»
            self.en("poreso")
            ar = flecha([0, -0.9, 0], [0, -1.5, 0], INK, 3)
            self.play(GrowArrow(ar), run_time=0.3)

            # «como vimos al final del capítulo anterior»
            self.en("vimos")
            cap = etiqueta("capítulo 10", INK, 0.5).move_to([1.7, -1.2, 0])
            self.play(FadeIn(cap), run_time=self.dur(0.4))

            # «a la salida»
            self.en("salida")
            self.play(FadeIn(F[0:2]), run_time=self.dur(0.5))

            # «la de la entrada»
            self.en("entrada")
            self.play(FadeIn(F[3]), run_time=self.dur(0.5))

            # «el módulo de la ganancia al cuadrado»
            self.en("mod")
            self.play(FadeIn(F[2]), run_time=self.dur(0.7))
            self.resaltar(F, color=AMBAR)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=9.0, alto=3.2, color=AMBAR, x_label=r"\omega") \
            .move_to([0, -0.5, 0])
        ax = c.ejes

        def ventana(a, b):
            x0, x1 = ax.c2p(a, 0)[0], ax.c2p(b, 0)[0]
            r = Rectangle(width=x1 - x0, height=2.9, color=CIAN, stroke_width=2.5).set_fill(CIAN, 0.12)
            r.move_to([(x0 + x1) / 2, ax.c2p(0, 0)[1] + 1.45, 0])
            r.permitir_encima = True
            return r

        vp, vn = ventana(1.1, 2.1), ventana(-2.1, -1.1)
        with self.narrar("b2"):
            # «Dentro de las ventanitas»
            self.en("dentro")
            self.corte()
            self.play(Create(ax), FadeIn(c.etiquetas), Create(c.grafica), FadeIn(vp), FadeIn(vn),
                      run_time=self.dur(1.2))

            # «la ganancia es uno»
            self.en("g1")
            g1 = etiqueta("ganancia 1", VERDE, 0.6).move_to([4.5, 2.7, 0])
            self.pop(g1)

            # «la curva queda intacta»
            self.en("intacta")
            self.resaltar(vp, vn, color=VERDE)

            # «Fuera, es cero»
            self.en("fuera")
            g0 = etiqueta("ganancia 0", ROJO, 0.6).move_to([-4.5, 2.7, 0])
            self.pop(g0)

            # «la curva desaparece»
            self.en("desap")
            self.play(c.grafica.animate.set_stroke(opacity=0.2), run_time=self.dur(0.6))

            # «el área de lo que queda»
            self.en("area")
            a1, a2 = c.area(1.1, 2.1, AMBAR, 0.55), c.area(-2.1, -1.1, AMBAR, 0.55)
            self.play(FadeIn(a1), FadeIn(a2), run_time=self.dur(0.6))
            ar = etiqueta("área", AMBAR, 0.6).move_to([1.6, -3.4, 0])
            self.pop(ar)

            # «dividida entre dos pi»
            self.en("dospi")
            F = MathTex("P", "=", "\\frac{1}{2\\pi}", "\\cdot", color=TXT).scale(1.0).move_to([-0.2, -3.4, 0])
            F[0].set_color(AMBAR)
            self.play(FadeIn(F), run_time=self.dur(0.6))

            # «cualquier banda»
            self.en("banda")
            self.play(FadeOut(a1), FadeOut(a2), vp.animate.shift(RIGHT * 1.6), vn.animate.shift(LEFT * 1.6),
                      run_time=self.dur(0.8))

            # «la potencia que el proceso tiene en ella»
            self.en("potbanda")
            b1, b2 = c.area(2.7, 3.7, AMBAR, 0.55), c.area(-3.7, -2.7, AMBAR, 0.55)
            self.play(FadeIn(b1), FadeIn(b2), run_time=self.dur(0.6))
            pb = etiqueta("potencia en la banda", AMBAR, 0.55).move_to([4.3, -3.4, 0])
            self.pop(pb)

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        c = Curva(psd_tele, x_rango=(-6, 6), y_max=1.2, ancho=9.0, alto=3.2, color=AMBAR, x_label=r"\omega") \
            .move_to([0, -0.5, 0])
        ax = c.ejes
        x0, x1 = ax.c2p(-2, 0)[0], ax.c2p(2, 0)[0]
        rect = Rectangle(width=x1 - x0, height=2.9, color=CIAN, stroke_width=2.5).set_fill(CIAN, 0.12)
        rect.move_to([0, ax.c2p(0, 0)[1] + 1.45, 0])
        rect.permitir_encima = True
        with self.narrar("b3"):
            # «Con la telegráfica»
            self.en("tele")
            self.corte()
            self.play(Create(ax), FadeIn(c.etiquetas), Create(c.grafica), run_time=self.dur(1.0))

            # «de menos dos a dos radianes por segundo»
            self.en("rango")
            self.play(FadeIn(rect), run_time=self.dur(0.5))
            rg = MathTex("-2<\\omega<2\\;\\text{rad/s}", color=CIAN).scale(0.8).move_to([0, 3.4, 0])
            self.pop(rg)

            # «la mitad de la potencia»
            self.en("mitad")
            ai = c.area(-2, 2, AMBAR, 0.5)
            self.play(FadeIn(ai), run_time=self.dur(0.6))
            m1 = MathTex("\\tfrac12", color=TXT).scale(0.9).move_to(ax.c2p(0, 0.3))
            self.pop(m1)

            # «La otra mitad»
            self.en("otra")
            c1, c2 = c.area(-6, -2, INK, 0.45), c.area(2, 6, INK, 0.45)
            self.play(FadeIn(c1), FadeIn(c2), run_time=self.dur(0.6))
            m2 = MathTex("\\tfrac12", color=TXT).scale(0.9).move_to(ax.c2p(4.2, 0.35))
            self.pop(m2)

            # «hasta el infinito»
            self.en("inf")
            fl1 = flecha(ax.c2p(5.4, 0.1), ax.c2p(6.0, 0.1), INK, 3)
            fl2 = flecha(ax.c2p(-5.4, 0.1), ax.c2p(-6.0, 0.1), INK, 3)
            self.play(GrowArrow(fl1), GrowArrow(fl2), run_time=0.4)

            # «la herramienta del capítulo»
            self.en("herr")
            sx = formula("S_{xx}(j\\omega)", escala=1.1, colores={0: AMBAR}).move_to([4.4, 2.6, 0])
            self.pop(sx)

            # «cuánta potencia hay en cada banda»
            self.en("cada")
            self.play(FadeOut(ai), FadeOut(c1), FadeOut(c2), FadeOut(rect), FadeOut(m1), FadeOut(m2),
                      FadeOut(rg), FadeOut(fl1), FadeOut(fl2), run_time=0.4)
            cols = [AZUL, CIAN, VERDE, AMBAR, MAGENTA, ROJO]
            edges = [-6, -4, -2, 0, 2, 4, 6]
            bandas = [c.area(edges[i], edges[i + 1], cols[i], 0.55) for i in range(6)]
            self.play(LaggedStart(*[FadeIn(b) for b in bandas], lag_ratio=0.2), run_time=self.dur(1.4))
