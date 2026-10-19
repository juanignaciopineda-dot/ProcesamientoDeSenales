"""Escena 09 — No hay umbral sin supuestos: el punto más lejos de la diagonal supone a priori y costes iguales."""
from comun.escena import *
from comun.figuras_c9e6 import *

U_NP, U_RIESGO, U_NADA = 1.645, 0.62, 1.0


class UmbralSinSupuestos(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.P = PlanoRoc9()
        self.criterios()
        self.supuestos()
        self.wait(1.0)
        self.limpiar()

    def tarjeta(self, izq: str, der: str, y: float, color=INK) -> VGroup:
        a = Text(izq, color=TXT).scale(0.42)
        f = Text("→", color=INK).scale(0.5)
        b = Text(der, color=ESTIMACION, weight=BOLD).scale(0.42)
        fila = VGroup(a, f, b).arrange(RIGHT, buff=0.2)
        r = RoundedRectangle(corner_radius=0.12, width=6.4, height=0.8, color=color, stroke_width=2.5).set_fill(color, 0.1)
        r.move_to([-3.6, y, 0])
        fila.move_to(r)
        g = VGroup(r, fila)
        g.marco, g.a, g.b = r, a, b
        return g

    # ------------------------------------------------------------ b1
    def criterios(self):
        P = self.P
        with self.narrar("b1"):
            # «con un criterio explícito»
            self.en("criterio")
            cr = Text("Criterio", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([-3.6, 3.1, 0])
            curva = P.curva()
            self.add(P, P.diagonal())
            self.play(Create(curva), run_time=self.dur(0.6))
            self.pop(cr)
            self.curva, self.cr = curva, cr

            # «un tope de falsas alarmas»
            self.en("tope")
            t1 = self.tarjeta("Cota de falsas alarmas", "Neyman-Pearson", 1.9)
            v = DashedLine(P.p(0.05, 0), P.p(0.05, 1), color=FA, stroke_width=3, dash_length=0.1)
            self.play(FadeIn(t1, shift=RIGHT * 0.2), Create(v), run_time=self.dur(0.5))

            # «Neyman-Pearson»
            self.en("np")
            p1 = P.punto(*roc9(U_NP), color=TXT)
            self.play(t1.b.animate(rate_func=there_and_back).scale(1.2), FadeIn(p1, scale=0.4), run_time=self.dur(0.45))

            # «tienes costes»
            self.en("costes")
            t2 = self.tarjeta("Costes", "Riesgo mínimo", 0.9)
            p2 = P.punto(*roc9(U_RIESGO), color=TXT)
            self.play(FadeIn(t2, shift=RIGHT * 0.2), FadeIn(p2, scale=0.4), run_time=self.dur(0.5))

            # «¿Y si no tienes nada?»
            self.en("nada")
            t3 = self.tarjeta("Nada", "?", -0.1)
            self.play(FadeIn(t3, shift=RIGHT * 0.2), run_time=self.dur(0.4))
            self.play(t3.b.animate(rate_func=there_and_back).scale(1.25), run_time=self.dur(0.4))

            # «Se suele tomar»
            self.en("suele")
            u = ValueTracker(3.0)
            pt = always_redraw(lambda: P.punto(*roc9(u.get_value())))

            def distancia():
                fa, pd = roc9(u.get_value())
                m = (fa + pd) / 2
                return DashedLine(P.p(m, m), P.p(fa, pd), color=ESTIMACION, stroke_width=3.5, dash_length=0.08)
            dist = always_redraw(distancia)
            self.add(pt, dist)
            self.play(u.animate.set_value(-0.5), run_time=self.dur(1.6), rate_func=smooth)

            # «más alejado de la diagonal»
            self.en("lejos")
            self.play(u.animate.set_value(U_NADA), run_time=self.dur(0.8))
            pt.clear_updaters()
            dist.clear_updaters()
            nuevo = Text("El punto más lejos de la diagonal", color=ESTIMACION, weight=BOLD).scale(0.38)
            fila = VGroup(t3.a.copy(), t3[1][1].copy(), nuevo).arrange(RIGHT, buff=0.2).move_to(t3.marco)
            self.play(t3.a.animate.move_to(fila[0]), t3[1][1].animate.move_to(fila[1]),
                      Transform(t3.b, nuevo), run_time=self.dur(0.45))
            self.t = VGroup(t1, t2, t3)
            self.t3, self.pt, self.otros = t3, pt, VGroup(v, p1, p2)

    # ------------------------------------------------------------ b2
    def supuestos(self):
        P = self.P
        with self.narrar("b2"):
            # «ese punto ya lo conocemos»
            self.en("conocemos")
            aro = Circle(radius=0.22, color=TXT, stroke_width=4).move_to(self.pt)
            self.play(Create(aro), self.pt.animate.scale(1.4), run_time=self.dur(0.4))

            # «la pendiente vale uno»
            self.en("pendiente")
            tg = P.tangente(U_NADA, largo=0.5, color=TXT)
            rt = Text("Pendiente = 1", color=TXT).scale(0.45).move_to(P.p(0.62, 1) + UP * 0.35)
            self.play(Create(tg), FadeIn(rt), run_time=self.dur(0.5))

            # «Elegirlo es suponer»
            self.en("suponer")
            t3 = self.t3
            self.play(FadeOut(self.t[0]), FadeOut(self.t[1]), FadeOut(self.cr),
                      t3.animate.move_to([-3.5, 2.4, 0]), run_time=self.dur(0.5))

            # «sin decirlo»
            self.en("letra")
            sup = Text("Supone:", color=INK, slant=ITALIC).scale(0.45).move_to([-6.0, 1.5, 0], aligned_edge=LEFT)
            self.play(FadeIn(sup), run_time=self.dur(0.35))

            # «igual de probables»
            self.en("priori")
            pr = MathTex(r"p_0 = p_1", color=TXT).scale(0.8).next_to(sup, RIGHT, buff=0.35)
            self.play(Write(pr), run_time=self.dur(0.5))

            # «cuestan lo mismo»
            self.en("costes_iguales")
            ci = Text("Coste falsa alarma = Coste fallo", color=TXT).scale(0.42).move_to([-6.0, 0.8, 0], aligned_edge=LEFT)
            eta = MathTex(r"\eta = 1", color=ESTIMACION).scale(0.9).move_to([-4.2, 0.05, 0])
            self.play(FadeIn(ci, shift=UP * 0.1), run_time=self.dur(0.4))
            self.pop(eta)

            # «sin supuestos»
            self.en("sin")
            us = tarjeta6("Umbral sin supuestos", INK, ancho=4.4).move_to([-3.6, -1.1, 0])
            self.play(FadeIn(us), run_time=self.dur(0.35))
            self.play(Create(tachar(us)), run_time=self.dur(0.35))

            # «supuestos que se dicen»
            self.en("dicen")
            d = VGroup(tarjeta6("Supuestos dichos", VERDE, ancho=3.2, escala=0.4), tilde(VERDE, 0.35)).arrange(RIGHT, buff=0.15)
            d.move_to([-3.9, -2.2, 0])
            self.pop(d)

            # «supuestos que no»
            self.en("no")
            c = VGroup(tarjeta6("Supuestos callados", INK, ancho=3.2, escala=0.4),
                       Text("?", color=INK, weight=BOLD).scale(0.6)).arrange(RIGHT, buff=0.15).set_opacity(0.55)
            c.move_to([-3.9, -3.2, 0])
            self.play(FadeIn(c, shift=UP * 0.1), run_time=self.dur(0.4))
