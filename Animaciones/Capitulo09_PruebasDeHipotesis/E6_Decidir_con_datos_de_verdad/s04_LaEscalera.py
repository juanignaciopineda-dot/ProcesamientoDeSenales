"""Escena 04 — La escalera: bajar el umbral caso a caso dibuja la curva ROC con datos."""
from comun.escena import *
from comun.figuras_c9e6 import *


class LaEscalera(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.col = columna6(centro=(-5.4, 0.0), paso=0.78)
        self.P = PlanoRoc9()
        self.E = Escalera6(self.P)
        self.add(self.col)
        self.reglas()
        self.camino()
        self.avisos()
        self.wait(1.0)
        self.limpiar()

    def linea_umbral(self, i: int) -> Line:
        """Umbral horizontal bajo la ficha i (i = −1: por encima de la primera)."""
        y = self.col.entre(i)
        return Line([-6.4, y, 0], [-3.9, y, 0], color=ESTIMACION, stroke_width=5)

    # ------------------------------------------------------------ b1
    def reglas(self):
        P, E = self.P, self.E
        with self.narrar("b1"):
            # «bajamos el umbral»
            self.en("umbral")
            u = self.linea_umbral(-1)
            self.play(Create(u), run_time=self.dur(0.4))
            self.u = u

            # «caso a caso»
            self.en("plano")
            pt = P.punto(0, 0)
            self.play(FadeIn(P), Create(P.diagonal()), FadeIn(pt, scale=0.5), run_time=self.dur(0.6))
            self.pt = pt

            # «un positivo»
            self.en("pos1")
            self.play(Transform(u, self.linea_umbral(0)), self.col.fichas[0].marco.animate.set_fill(opacity=0.7),
                      run_time=self.dur(0.4))

            # «la detección sube un cuarto»
            self.en("sube")
            cuarto = Text("¼", color=DET).scale(0.45).move_to(P.p(0, 0.25) + LEFT * 0.3)
            self.play(pt.animate.move_to(P.p(0, 0.25)), FadeIn(cuarto), run_time=self.dur(0.5))
            self.cuarto = cuarto

            # «un escalón hacia arriba»
            self.en("arriba")
            t0 = E.tramo(0)
            fl = Text("↑", color=ROC, weight=BOLD).scale(0.6).next_to(t0, RIGHT, buff=0.15)
            self.play(Create(t0), FadeIn(fl), run_time=self.dur(0.4))
            self.tramos = VGroup(t0)
            self.fl = fl

            # «queda un negativo»
            self.en("neg1")
            suelta = ficha6(0, None).move_to([-2.6, self.col.entre(0) - 0.6, 0])
            self.play(FadeIn(suelta, shift=LEFT * 0.2), run_time=self.dur(0.3))
            self.play(suelta.marco.animate.set_fill(NEG, 0.75), run_time=self.dur(0.3))

            # «la falsa alarma sube un cuarto»
            self.en("derecha")
            fl_d = DashedLine(P.p(0, 0.25), P.p(0.25, 0.25), color=FA, stroke_width=4, dash_length=0.1)
            c_d = Text("→ ¼", color=FA).scale(0.42).next_to(fl_d, UP, buff=0.12)
            self.play(Create(fl_d), FadeIn(c_d), run_time=self.dur(0.5))
            self.fl_d = VGroup(fl_d, c_d)

            # «hacia la derecha»
            self.en("regla")
            regla = VGroup(
                VGroup(ficha6(1, None, lado=0.5), Text("→  ↑ ¼", color=DET).scale(0.48)).arrange(RIGHT, buff=0.25),
                VGroup(ficha6(0, None, lado=0.5), Text("→  → ¼", color=FA).scale(0.48)).arrange(RIGHT, buff=0.25),
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([-1.5, -0.4, 0])
            self.play(FadeOut(suelta), FadeIn(regla, shift=UP * 0.15), run_time=self.dur(0.5))
            self.regla = regla

    # ------------------------------------------------------------ b2
    def bajar(self, i: int, t: float):
        """El umbral pasa bajo la ficha i y se dibuja su tramo."""
        tr = self.E.tramo(i)
        self.play(Transform(self.u, self.linea_umbral(i)),
                  self.col.fichas[i].marco.animate.set_fill(opacity=0.7),
                  Create(tr), self.pt.animate.move_to(self.P.p(*self.E.pts[i + 1])), run_time=t)
        self.tramos.add(tr)

    def camino(self):
        P, E = self.P, self.E
        with self.narrar("b2"):
            # «El camino es»
            self.en("p0")
            self.play(FadeOut(self.fl_d), FadeOut(self.fl), run_time=self.dur(0.3))

            # «arriba, arriba,»: el primer tramo ya está; late
            self.en("p1")
            self.play(self.tramos[0].animate(rate_func=there_and_back).set_stroke(width=12), run_time=self.dur(0.35))

            # «arriba, derecha, arriba…»: un tramo por palabra
            for i in range(1, 8):
                self.en(f"p{i + 1}")
                self.bajar(i, self.dur(0.35))

            # «de una esquina a la otra»
            self.en("esquinas")
            aros = VGroup(*[Circle(radius=0.26, color=TXT, stroke_width=4).move_to(P.p(*q)) for q in ((0, 0), (1, 1))])
            aros.permitir_encima = True
            self.play(Create(aros), run_time=self.dur(0.4))
            self.play(FadeOut(aros), run_time=self.dur(0.3))

            # «la curva ROC medida»
            self.en("roc")
            esc = E.todo()
            self.add(esc)
            self.remove(*self.tramos)
            rot = Text("ROC empírica", color=ROC, weight=BOLD).scale(0.55).move_to(P.p(0.66, 0.3))
            self.pop(rot)
            self.esc, self.rot = esc, rot

            # «Con ocho casos»
            self.en("ocho")
            n = Text("8 casos", color=TXT).scale(0.48).next_to(rot, DOWN, buff=0.2)
            self.play(FadeIn(n, shift=UP * 0.1), run_time=self.dur(0.35))
            self.n = n

            # «los escalones son enormes»
            self.en("enormes")
            tr = VGroup(*[E.tramo(i) for i in range(8)])
            self.play(LaggedStart(*[t.animate(rate_func=there_and_back).set_stroke(width=12) for t in tr],
                                  lag_ratio=0.15), run_time=self.dur(1.0))
            self.remove(tr)

            # «con miles»
            self.en("miles")
            for k, txt in ((80, "80 casos"), (8000, "8.000 casos")):
                nueva = escalera_n6(P, k, semilla=5, ancho=5.0)
                nn = Text(txt, color=TXT).scale(0.48).move_to(self.n)
                self.play(Transform(self.esc, nueva), Transform(self.n, nn), run_time=self.dur(0.55))

            # «la curva suave»
            self.en("suave")
            suave = DashedVMobject(P.curva(color=TXT, ancho=3), num_dashes=50)
            self.play(Create(suave), run_time=self.dur(0.8))
            self.suave = suave

    # ------------------------------------------------------------ b3
    def avisos(self):
        P, E = self.P, self.E
        with self.narrar("b3"):
            # «Dos avisos»
            self.en("avisos")
            av = aviso6().move_to([-6.2, 2.7, 0])
            self.play(Transform(self.esc, E.todo()), Transform(self.n, Text("8 casos", color=TXT).scale(0.48).move_to(self.n)),
                      FadeOut(self.suave), FadeOut(self.col), FadeOut(self.u), FadeOut(self.regla),
                      FadeIn(av, scale=0.5), run_time=self.dur(0.6))

            # «pocos casos de un tipo»
            self.en("pocos")
            t1 = tarjeta6("Pocos casos: Dibujo tosco", ESTIMACION, ancho=4.6).move_to([-3.2, 2.7, 0])
            self.pop(t1)

            # «no hay que fiarse de sus detalles»
            self.en("detalles")
            lp = lupa(TXT).scale(0.55).move_to(P.p(0.4, 0.62))
            lp.permitir_encima = True
            q = Text("?", color=ESTIMACION, weight=BOLD).scale(0.6).next_to(lp, UR, buff=0.02)
            q.permitir_encima = True
            self.play(FadeIn(lp, scale=0.6), FadeIn(q), run_time=self.dur(0.45))

            # «Y si la mides»
            self.en("mides")
            regla = VGroup(Line(P.p(1.06, 0), P.p(1.06, 1), color=ESTIMACION, stroke_width=4),
                           *[Line(P.p(1.06, y), P.p(1.1, y), color=ESTIMACION, stroke_width=3)
                             for y in np.linspace(0, 1, 5)])
            self.play(FadeOut(lp), FadeOut(q), Create(regla), run_time=self.dur(0.4))

            # «los mismos datos»
            self.en("mismos")
            def monton(cx, rot):
                m = VGroup(*[ficha6(s, None, lado=0.45) for s in (1, 0, 1, 0)]).arrange(RIGHT, buff=0.1)
                r = Text(rot, color=TXT).scale(0.45).next_to(m, UP, buff=0.18)
                return VGroup(r, m).move_to([cx, 0.6, 0])
            aj, me = monton(-5.2, "Ajustar"), monton(-2.3, "Medir")
            igual = Text("=", color=ERROR, weight=BOLD).scale(0.7).move_to([-3.75, 0.45, 0])
            self.play(FadeIn(aj, shift=UP * 0.15), FadeIn(me, shift=UP * 0.15), FadeIn(igual), run_time=self.dur(0.5))

            # «ajustaste el detector»
            self.en("ajustar")
            det = caja_detector6(ancho=2.2, alto=1.0, escala=0.45).move_to([-5.2, -1.7, 0])
            fl = Arrow(aj.get_bottom(), det.get_top(), buff=0.12, color=INK, stroke_width=3)
            self.play(FadeIn(det), GrowArrow(fl), run_time=self.dur(0.45))

            # «sale mejor de lo que es»
            self.en("optimista")
            inflada = Escalera6(P, [1, 1, 1, 0, 1, 0, 0, 0]).todo()
            t2 = tarjeta6("Optimista", ERROR, ancho=2.6).move_to([-2.3, -1.7, 0])
            self.play(Transform(self.esc, inflada), run_time=self.dur(0.6))
            self.pop(t2)

            # «datos que el detector no haya visto»
            self.en("nuevos")
            nuevo = VGroup(*[ficha6(s, None, lado=0.45) for s in (0, 1, 1, 0)]).arrange(RIGHT, buff=0.1).move_to(me[1])
            for f in nuevo:
                f.marco.set_stroke(VERDE)
            self.play(ReplacementTransform(me[1], nuevo), FadeOut(igual), FadeOut(t2),
                      Transform(self.esc, E.todo()), run_time=self.dur(0.6))
            tic = tilde(VERDE, 0.45).next_to(nuevo, RIGHT, buff=0.2)
            self.pop(tic)
