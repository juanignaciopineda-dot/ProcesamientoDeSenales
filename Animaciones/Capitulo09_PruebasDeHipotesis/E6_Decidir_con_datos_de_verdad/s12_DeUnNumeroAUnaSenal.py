"""Escena 12 — De un número a una señal: las tres ideas del capítulo y la pregunta que abre el siguiente."""
from comun.escena import *
from comun.figuras_c9e6 import *

U_NP, U_MAP, U_RIESGO = 1.645, 1.42, 0.62


class DeUnNumeroAUnaSenal(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.tres_ideas()
        self.una_senal()
        self.la_regla()
        self.el_ruido()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def tres_ideas(self):
        with self.narrar("b1"):
            # «tres ideas»
            self.en("tres")
            cards = VGroup()
            for i, x in enumerate((-4.5, 0.0, 4.5)):
                r = RoundedRectangle(corner_radius=0.2, width=4.1, height=3.6, color=INK, stroke_width=3)
                r.set_fill(INK, 0.08).move_to([x, 0.4, 0])
                n = Text(str(i + 1), color=ESTIMACION, weight=BOLD).scale(0.6).move_to(r.get_corner(UL) + DR * 0.38)
                cards.add(VGroup(r, n))
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cards], lag_ratio=0.2), run_time=self.dur(0.7))
            self.cards = cards

            # «comparar un número»
            self.en("uno")
            lam = MathTex(r"\Lambda(r)", color=MEDIDA).scale(1.2).move_to(cards[0][0].get_center() + UP * 0.1)
            self.play(Write(lam), run_time=self.dur(0.5))
            # «con un umbral»
            self.en("umbral")
            lrt = MathTex(r"\Lambda(r)", r"\gtrless", r"\eta", color=MEDIDA).scale(1.2).move_to(lam)
            lrt[2].set_color(ESTIMACION)
            self.play(ReplacementTransform(lam, lrt[0]), FadeIn(lrt[1:]), run_time=self.dur(0.45))

            # «Dos: el umbral sale»
            self.en("dos")
            c2 = cards[1][0]
            eta = MathTex(r"\eta :", color=ESTIMACION).scale(1.0).move_to(c2.get_top() + DOWN * 0.75)
            self.play(Write(eta), run_time=self.dur(0.4))
            lineas = VGroup()
            for k, (marca, txt) in enumerate((("priori", "A priori"), ("presupuesto", "Presupuesto"), ("costes", "Costes"))):
                # «las probabilidades a priori» · «un presupuesto de falsas» · «o los costes»
                self.en(marca)
                t = Text(txt, color=TXT).scale(0.48).move_to(c2.get_center() + DOWN * (0.15 + 0.55 * k))
                self.play(FadeIn(t, shift=RIGHT * 0.15), run_time=self.dur(0.35))
                lineas.add(t)

            # «Tres: la curva ROC»
            self.en("roc")
            c3 = cards[2][0]
            P = PlanoRoc9(origen=(c3.get_center()[0] - 1.25, c3.get_center()[1] - 1.4), lado=2.5, escala=0.32,
                          rotulos=False)
            curva = P.curva(ancho=4)
            pts = VGroup(*[P.punto(*roc9(u), color=TXT, radio=0.07) for u in (U_NP, U_MAP, U_RIESGO)])
            self.play(FadeIn(P), Create(curva), run_time=self.dur(0.5))
            self.play(FadeIn(pts), run_time=self.dur(0.3))

            # «todos los umbrales a la vez»
            self.en("todos")
            pt = P.punto(0, 0, radio=0.08)
            self.add(pt)
            self.play(MoveAlongPath(pt, curva), run_time=self.dur(1.2), rate_func=linear)
            self.remove(pt)

            # «su pendiente es el propio umbral»
            self.en("pendiente")
            tg = P.tangente(U_MAP, largo=0.5, color=ESTIMACION)
            rp = MathTex(r"\text{Pendiente} = \eta", color=ESTIMACION).scale(0.6).next_to(c3, DOWN, buff=0.2)
            self.play(Create(tg), Write(rp), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b2
    def una_senal(self):
        with self.narrar("b2"):
            # «un solo número»
            self.en("r")
            self.corte()
            base = Line([-3.0, 0, 0], [5.5, 0, 0], color=INK, stroke_width=2)
            d = Dot([1.0, 0.45, 0], radius=0.12, color=MEDIDA)
            rr = MathTex("r", color=MEDIDA).scale(0.8).next_to(d, UP, buff=0.15)
            self.play(Create(base), FadeIn(d, scale=0.4), FadeIn(rr), run_time=self.dur(0.5))

            # «Un voltaje»
            self.en("voltaje")
            v = Text("1,3 V", color=MEDIDA).scale(0.5).next_to(d, RIGHT, buff=0.25)
            self.play(FadeIn(v, shift=LEFT * 0.1), run_time=self.dur(0.35))

            # «Un receptor de verdad»
            self.en("receptor")
            rad = radar13().scale(0.9).move_to([-5.4, 0.4, 0])
            self.play(FadeIn(rad, shift=RIGHT * 0.2), run_time=self.dur(0.45))

            # «una señal entera»
            self.en("senal")
            fila = fila_barras6(n=24, centro=(1.5, 0.0), ancho=8.0, alto=1.3)
            self.play(FadeOut(rr), FadeOut(v), FadeOut(base), run_time=0.2)
            self.play(ReplacementTransform(VGroup(*[d.copy() for _ in range(24)]), fila.barras), FadeIn(fila.base),
                      run_time=self.dur(0.7))
            self.remove(d)

            # «miles de muestras»
            self.en("miles")
            larga = fila_barras6(n=60, centro=(5.1, 0.0), ancho=15.2, alto=1.3)
            self.play(ReplacementTransform(fila, larga), run_time=self.dur(0.8))
            self.fila, self.rad = larga, rad

            # «cada una con su ruido»
            self.en("ruido")
            rng = np.random.default_rng(9)
            trozos = VGroup(*[Rectangle(width=b.width, height=0.12 + 0.12 * rng.random(), stroke_width=0)
                              .set_fill(RUIDO, 0.9).next_to(b, UP, buff=0) for b in larga.barras])
            self.play(FadeIn(trozos), run_time=self.dur(0.3))
            self.play(LaggedStart(*[VGroup(b, t).animate(rate_func=there_and_back).shift(UP * 0.15 * (1 if i % 2 else -1))
                                    for i, (b, t) in enumerate(zip(larga.barras, trozos))], lag_ratio=0.02),
                      run_time=self.dur(0.9))
            self.trozos = trozos

    # ------------------------------------------------------------ b3
    def la_regla(self):
        with self.narrar("b3"):
            # «La regla no cambia»
            self.en("regla")
            fila = VGroup(self.fila, self.trozos)
            self.play(FadeOut(self.rad), fila.animate.shift(DOWN * 2.2 + LEFT * 3.6), run_time=self.dur(0.4))
            f = MathTex(r"\Lambda(r)", r"\gtrless", r"\eta", color=MEDIDA).scale(1.1).move_to([0, 2.6, 0])
            f[2].set_color(ESTIMACION)
            self.play(Write(f), run_time=self.dur(0.5))

            # «todas las muestras juntas»
            self.en("muchas")
            g = MathTex(r"\Lambda(r[0], r[1], r[2], \ldots)", r"\gtrless", r"\eta", color=MEDIDA).scale(1.1).move_to(f)
            g[2].set_color(ESTIMACION)
            self.play(TransformMatchingTex(f, g), run_time=self.dur(0.6))
            self.f = g

            # «contra un umbral. Al»
            self.en("contra")
            self.play(g[2].animate(rate_func=there_and_back).scale(1.5), run_time=self.dur(0.4))

            # «Al final del curso»
            self.en("cap13")
            c13 = etiqueta("Capítulo 13", INK, 0.5).move_to([5.8, -3.55, 0])
            self.play(FadeIn(c13), run_time=self.dur(0.35))

            # «toda esa señal»
            self.en("toda")
            self.play(self.fila.barras.animate.set_fill(TXT, 1), run_time=self.dur(0.4))

            # «en un solo número»
            self.en("numero")
            punto = Dot([0, -2.0, 0], radius=0.14, color=MEDIDA)
            t1 = tarjeta6("Toda la señal en un solo número", MEDIDA, ancho=5.4).move_to([-3.4, 0.9, 0])
            self.play(ReplacementTransform(fila, punto), run_time=self.dur(0.6))
            self.pop(t1)

            # «sin perder nada»
            self.en("nada")
            tic = tilde(VERDE, 0.4).next_to(t1, DOWN, buff=0.15)
            self.pop(tic)

            # «más datos no basta»
            self.en("masdatos")
            t2 = tarjeta6("Más datos no bastan", ESTIMACION, ancho=4.2).move_to([3.4, 0.9, 0])
            self.pop(t2)

            # «saber combinarlos»
            self.en("combinar")
            sig = RoundedRectangle(corner_radius=0.12, width=0.9, height=0.9, color=ESTIMACION, stroke_width=3)
            sig.set_fill(ESTIMACION, 0.15).move_to([0, -1.5, 0])
            sl = MathTex(r"\Sigma", color=ESTIMACION).scale(0.9).move_to(sig)
            barras = fila_barras6(n=10, centro=(0, -3.3), ancho=6.0, alto=0.6)
            flechas = VGroup(*[Arrow(b.get_top(), sig.get_bottom(), buff=0.08, color=INK, stroke_width=2,
                                     max_tip_length_to_length_ratio=0.08) for b in barras.barras])
            self.play(ReplacementTransform(punto, sig), FadeIn(sl), FadeIn(barras), run_time=self.dur(0.4))
            self.play(LaggedStart(*[GrowArrow(a) for a in flechas], lag_ratio=0.06), run_time=self.dur(0.6))
            self.resto = VGroup(t1, tic, t2, sig, sl, barras, flechas, c13)

    # ------------------------------------------------------------ b4
    def el_ruido(self):
        with self.narrar("b4"):
            # «algo que todavía no tenemos»
            self.en("falta")
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(1.6).move_to([0, 0.2, 0])
            self.play(FadeOut(self.resto, shift=DOWN * 0.3), FadeOut(self.f), run_time=self.dur(0.4))
            self.pop(q)

            # «Para escribir esa razón»
            self.en("escribir")
            g = MathTex(r"\Lambda(r[0], r[1], \ldots) = \ ?", color=MEDIDA).scale(1.0).move_to([0, 2.8, 0])
            self.play(FadeOut(q), Write(g), run_time=self.dur(0.6))

            # «describir el ruido a lo largo del tiempo»
            self.en("ruido")
            n = 80
            ruido = ruido6(centro=(0, 0.7), ancho=11.0, alto=1.4, n=n, semilla=3)
            self.play(Create(ruido), run_time=self.dur(1.4), rate_func=linear)

            # «a lo largo del tiempo»
            self.en("tiempo")
            eje = Arrow([-5.6, -0.4, 0], [5.9, -0.4, 0], buff=0, color=INK, stroke_width=3,
                        max_tip_length_to_length_ratio=0.03)
            rt = Text("Tiempo", color=INK).scale(0.42).next_to(eje.get_end(), DOWN, buff=0.15).shift(LEFT * 0.9)
            self.play(GrowArrow(eje), FadeIn(rt), run_time=self.dur(0.5))

            # «de este instante»
            self.en("ahora")
            k = 30
            pa = ruido.point_from_proportion(k / (n - 1))
            pb = ruido.point_from_proportion((k + 1) / (n - 1))
            da = Dot(pa, radius=0.1, color=TXT)
            self.play(FadeIn(da, scale=0.4), run_time=self.dur(0.3))

            # «dentro de un milisegundo»
            self.en("despues")
            db = Dot(pb, radius=0.1, color=TXT)
            arco = ArcBetweenPoints(pa + UP * 0.25, pb + UP * 0.25, angle=-PI / 1.5, color=ESTIMACION, stroke_width=3)
            pre = Text("¿Tienen algo que ver?", color=ESTIMACION).scale(0.45).move_to([(pa[0] + pb[0]) / 2 + 2.2, 1.95, 0])
            self.play(FadeIn(db, scale=0.4), Create(arco), run_time=self.dur(0.4))
            self.play(FadeIn(pre, shift=DOWN * 0.1), run_time=self.dur(0.35))

            # «¿Cómo se describe»
            self.en("como")
            como = Text("¿Cómo se describe?", color=ESTIMACION, weight=BOLD).scale(0.65).move_to([0, 2.8, 0])
            self.play(FadeOut(g), FadeOut(pre), FadeOut(arco), FadeOut(da), FadeOut(db), FadeIn(como), run_time=self.dur(0.45))

            # «una señal entera que»
            self.en("entera")
            self.play(ruido.animate(rate_func=there_and_back).set_stroke(width=6), run_time=self.dur(0.6))

            # «nunca se repite»
            self.en("repite")
            otro = ruido6(centro=(0, 0.7), ancho=11.0, alto=1.4, n=n, semilla=8)
            self.play(FadeOut(ruido), run_time=self.dur(0.3))
            self.play(Create(otro), run_time=self.dur(1.0), rate_func=linear)

            # «una grabación del ruido»
            self.en("una")
            uno = Text("1", color=TXT, weight=BOLD).scale(0.5).move_to([-6.2, 0.7, 0])
            self.play(FadeIn(uno), run_time=self.dur(0.35))

            # «imaginar muchas a la vez»
            self.en("muchas")
            pila = VGroup(*[ruido6(centro=(0, -1.0 - 0.55 * i), ancho=11.0, alto=0.5, n=n, semilla=20 + i,
                                   ancho_trazo=2.0, opacidad=0.75) for i in range(5)])
            self.play(FadeOut(eje), FadeOut(rt), run_time=0.2)
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in pila], lag_ratio=0.2), run_time=self.dur(1.0))
