"""Escena 06 — Contar parejas: el área es la probabilidad de que un positivo puntúe más que un negativo."""
from comun.escena import *
from comun.figuras_c9e6 import *

# dos detectores con la misma área (0,85) y muy distintos con poca falsa alarma
AZ_M, AZ_S = 2.317, 2.0      # azul: con 1 % de falsas alarmas detecta 0,50
CI_M, CI_S = 1.158, 0.5      # cian: con 1 % detecta 0,01

POS_I = [0, 1, 3, 5]         # posiciones de los «+» en la columna
NEG_I = [2, 4, 6, 7]         # posiciones de los «−»


class ContarParejas(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.parejas()
        self.ordena()
        self.lo_que_no_dice()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def parejas(self):
        with self.narrar("b1"):
            # «Ese número»
            self.en("numero")
            v = Text("0,81", color=ROC, weight=BOLD).scale(1.4)
            self.add(v)
            self.play(v.animate.scale(0.55).move_to([5.6, 3.2, 0]), run_time=self.dur(0.5))
            self.v = v

            # «algo muy concreto»
            self.en("concreto")
            mp = VGroup(*[ficha6(1, None, lado=0.5) for _ in range(4)]).arrange_in_grid(2, 2, buff=0.1).move_to([-4.6, 1.6, 0])
            mn = VGroup(*[ficha6(0, None, lado=0.5) for _ in range(4)]).arrange_in_grid(2, 2, buff=0.1).move_to([-1.6, 1.6, 0])
            self.play(v.animate(rate_func=there_and_back).scale(1.3), FadeIn(mp), FadeIn(mn), run_time=self.dur(0.5))

            # «un positivo al azar»
            self.en("pos")
            fp = mp[2]
            self.play(fp.animate.scale(1.4).move_to([-4.0, -0.6, 0]), run_time=self.dur(0.45))
            # «un negativo al azar»
            self.en("neg")
            fn = mn[1]
            self.play(fn.animate.scale(1.4).move_to([-2.2, -0.6, 0]), run_time=self.dur(0.45))

            # «el positivo tenga más puntuación»
            self.en("compara")
            mayor = MathTex(">", color=TXT).scale(1.2).move_to([-3.1, -0.6, 0])
            prob = MathTex(r"P(\text{Positivo} > \text{Negativo})", color=TXT).scale(0.8).move_to([-3.1, -1.8, 0])
            self.pop(mayor)
            self.play(Write(prob), run_time=self.dur(0.6))

            # «Comprobémoslo»
            self.en("tira")
            col = columna6(centro=(-5.0, 0.0), paso=0.78)
            self.play(FadeOut(VGroup(mp, mn, fp, fn, mayor)), prob.animate.scale(0.7).move_to([2.6, 3.2, 0]),
                      FadeIn(col), run_time=self.dur(0.6))
            self.col, self.prob = col, prob

            # «dieciséis parejas»
            self.en("parejas")
            lado = 0.7
            celdas = VGroup()
            for i in range(4):
                for j in range(4):
                    c = Square(side_length=lado, color=INK, stroke_width=2).set_fill(INK, 0.08)
                    c.move_to([0.9 + j * lado, 1.4 - i * lado, 0])
                    celdas.add(c)
            filas = VGroup(*[ficha6(1, None, lado=0.45).next_to(celdas[4 * i], LEFT, buff=0.15) for i in range(4)])
            cols = VGroup(*[ficha6(0, None, lado=0.45).next_to(celdas[j], UP, buff=0.15) for j in range(4)])
            self.play(FadeIn(celdas), FadeIn(filas), FadeIn(cols), run_time=self.dur(0.6))
            self.celdas = celdas

            cuentas = VGroup()

            def negativo(j, t):
                n = NEG_I[j]
                arcos = VGroup(*[ArcBetweenPoints(col.fichas[n].marco.get_left(), col.fichas[p].marco.get_left(),
                                                  angle=-PI / 2, color=VERDE, stroke_width=3)
                                 for p in POS_I if p < n])
                arcos.permitir_encima = True
                verdes = [celdas[4 * i + j].animate.set_fill(VERDE, 0.55) for i, p in enumerate(POS_I) if p < n]
                k = Text(str(len(arcos)), color=VERDE, weight=BOLD).scale(0.5).next_to(celdas[12 + j], DOWN, buff=0.18)
                cuentas.add(k)
                self.play(col.fichas[n].marco.animate.set_fill(NEG, 0.8), Create(arcos), *verdes, FadeIn(k),
                          run_time=t)
                return arcos

            # «El primer negativo»
            self.en("n1")
            a1 = negativo(0, self.dur(0.6))
            # «dos positivos»
            self.en("dos")
            self.resaltar(cuentas[0], color=VERDE, run_time=self.dur(0.4))
            # «El segundo, tres»
            self.en("n2")
            self.play(FadeOut(a1), run_time=0.2)
            a2 = negativo(1, self.dur(0.6))
            # «Los otros dos»
            self.en("otros")
            self.play(FadeOut(a2), col.fichas[6].marco.animate.set_fill(NEG, 0.8),
                      col.fichas[7].marco.animate.set_fill(NEG, 0.8), run_time=self.dur(0.4))
            # «cuatro cada uno»
            self.en("n34")
            a3 = negativo(2, self.dur(0.4))
            self.play(FadeOut(a3), run_time=0.2)
            a4 = negativo(3, self.dur(0.4))

            # «Trece de»
            self.en("trece")
            rojas = [celdas[4 * i + j] for j in range(4) for i, p in enumerate(POS_I) if p > NEG_I[j]]
            suma = MathTex(r"2 + 3 + 4 + 4 = 13", color=VERDE).scale(0.8).move_to([2.0, -2.3, 0])
            self.play(FadeOut(a4), *[c.animate.set_fill(ERROR, 0.5) for c in rojas], Write(suma),
                      run_time=self.dur(0.7))
            self.suma = suma

            # «El mismo número»
            self.en("mismo")
            fr = MathTex(r"\frac{13}{16}", color=VERDE).scale(0.85).next_to(v, LEFT, buff=0.7)
            ig = MathTex("=", color=VERDE).scale(0.9).move_to((fr.get_right() + v.get_left()) / 2)
            self.play(FadeOut(self.prob), FadeIn(fr, shift=UP * 0.1), FadeIn(ig), run_time=self.dur(0.45))
            self.parejas_g = VGroup(celdas, filas, cols, cuentas, suma)
            self.arriba = VGroup(fr, ig, v)

    # ------------------------------------------------------------ b2
    def ordena(self):
        with self.narrar("b2"):
            # «el área mide»
            self.en("mide")
            t = tarjeta6("Área = Lo bien que ordena", ROC, ancho=5.0).move_to([2.4, 0.4, 0])
            self.play(FadeOut(self.parejas_g), run_time=0.25)
            self.pop(t)

            # «los positivos por delante»
            self.en("delante")
            ideal = tira6([1, 1, 1, 1, 0, 0, 0, 0], centro=(2.4, -1.0), lado=0.55)
            self.play(FadeIn(ideal, shift=UP * 0.15), run_time=self.dur(0.4))

            # «de los negativos»
            self.en("detras")
            self.play(*[ideal[i].animate.shift(RIGHT * 0.35).set_opacity(0.45) for i in range(4, 8)],
                      run_time=self.dur(0.45))

            # «nuestras dos campanas»
            self.en("campanas")
            self.corte()
            C, P = campanas_izq9(), PlanoRoc9()
            eje = eje_izq9(C)
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            curva = P.curva()
            self.add(eje, c0, c1, P, P.diagonal())
            self.play(Create(curva), run_time=self.dur(0.7))
            self.C, self.P, self.curva = C, P, curva

            # «separadas dos desvíos»
            self.en("desvios")
            ll = BraceBetweenPoints(C.p(0, 0.47), C.p(2, 0.47), UP, color=TXT)
            lt = Text("2 desvíos", color=TXT).scale(0.45).next_to(ll, UP, buff=0.1)
            self.play(FadeIn(ll), FadeIn(lt), run_time=self.dur(0.4))

            # «cero coma noventa y dos»
            self.en("noventaydos")
            area = area_curva6(P)
            t92 = Text("Área = 0,92", color=TXT, weight=BOLD).scale(0.55).move_to(P.p(0.27, 0.3))
            self.play(FadeIn(area), run_time=self.dur(0.4))
            self.pop(t92)
            self.area, self.t92 = area, t92

    # ------------------------------------------------------------ b3
    def lo_que_no_dice(self):
        P = self.P
        with self.narrar("b3"):
            # «cuidado con lo que no dice»
            self.en("cuidado")
            av = aviso6().move_to([-6.2, 2.9, 0])
            self.pop(av)

            # «Es un promedio»
            self.en("promedio")
            pr = Text("Promedio", color=TXT).scale(0.48).next_to(self.t92, DOWN, buff=0.18)
            self.play(FadeIn(pr, shift=UP * 0.1), run_time=self.dur(0.4))

            # «todos los umbrales»
            self.en("todos")
            pt = P.punto(0, 0)
            self.add(pt)
            self.play(MoveAlongPath(pt, self.curva), run_time=self.dur(1.3), rate_func=linear)

            # «los que nunca vas a usar»
            self.en("nunca")
            velo = Rectangle(width=P.lado * 0.5, height=P.lado, stroke_width=0).set_fill(FONDO, 0.7)
            velo.move_to(P.p(0.75, 0.5))
            velo.permitir_encima = True
            self.play(FadeOut(pt), FadeIn(velo), run_time=self.dur(0.4))

            # «Dos detectores»
            self.en("dos")
            self.corte()
            P2 = PlanoRoc9(origen=(-5.4, -2.5), lado=4.9)
            az = P2.curva_bin(AZ_M, AZ_S, color=AZUL)
            ci = P2.curva_bin(CI_M, CI_S, color=CIAN)
            self.add(P2, P2.diagonal())
            self.play(Create(az), Create(ci), run_time=self.dur(0.8))

            # «la misma área»
            self.en("misma")
            ma = VGroup(Text("Área = 0,85", color=AZUL).scale(0.45), Text("Área = 0,85", color=CIAN).scale(0.45))
            ma.arrange(DOWN, buff=0.15).move_to(P2.p(0.7, 0.25))
            self.play(FadeIn(ma, shift=UP * 0.1), run_time=self.dur(0.4))

            # «muy distintos»
            self.en("distintos")
            self.play(az.animate(rate_func=there_and_back).set_stroke(width=10), run_time=self.dur(0.4))
            self.play(ci.animate(rate_func=there_and_back).set_stroke(width=10), run_time=self.dur(0.4))

            # «un uno por ciento»
            self.en("uno")
            franja = Rectangle(width=0.08, height=P2.lado, color=ESTIMACION, stroke_width=3).move_to(P2.p(0.008, 0.5))
            # recuadro ampliado: falsa alarma de 0 a 0,01
            o = np.array([1.6, -2.3, 0])
            an, al = 4.4, 4.4
            def q(fa, pd):
                return o + RIGHT * fa / 0.01 * an + UP * pd * al
            marco = Rectangle(width=an, height=al, color=INK, stroke_width=2.5).move_to(o + RIGHT * an / 2 + UP * al / 2)
            xs = np.geomspace(1e-5, 0.01, 60)
            def trazo(m, s, color):
                c = VMobject(stroke_color=color, stroke_width=5)
                c.set_points_as_corners([q(x, pd_de_fa9(x, m, s)) for x in xs])
                return c
            iaz, ici = trazo(AZ_M, AZ_S, AZUL), trazo(CI_M, CI_S, CIAN)
            ejx = Text("Falsa alarma: 0 a 1 %", color=FA).scale(0.4).next_to(marco, DOWN, buff=0.15)
            union = DashedLine(franja.get_right(), marco.get_left(), color=ESTIMACION, stroke_width=2)
            fl = DoubleArrow(q(0.01, pd_de_fa9(0.01, CI_M, CI_S)) + LEFT * 0.3, q(0.01, pd_de_fa9(0.01, AZ_M, AZ_S)) + LEFT * 0.3,
                             buff=0.05, color=TXT, stroke_width=3)
            self.play(Create(franja), Create(union), Create(marco), FadeIn(ejx), run_time=self.dur(0.5))
            self.play(Create(iaz), Create(ici), GrowFromCenter(fl), run_time=self.dur(0.6))
            self.recuadro = VGroup(marco, iaz, ici, ejx, union, franja, fl)

            # «la única que te importa»
            self.en("importa")
            self.play(marco.animate.set_stroke(ESTIMACION, width=5), run_time=self.dur(0.4))

            # «Y el área tampoco»
            self.en("tampoco")
            area = area_curva6(P2, lambda x: pd_de_fa9(x, AZ_M, AZ_S), color=AZUL, opacidad=0.25)
            self.play(FadeOut(self.recuadro), FadeIn(area), run_time=self.dur(0.5))

            # «dónde poner el umbral»
            self.en("donde")
            qm = Text("?", color=ESTIMACION, weight=BOLD).scale(0.9).move_to(P2.p(0.35, 1) + UP * 0.5)
            t = tarjeta6("Área ≠ Umbral", ESTIMACION, ancho=3.4).move_to([3.6, 0.4, 0])
            self.pop(qm, t)
