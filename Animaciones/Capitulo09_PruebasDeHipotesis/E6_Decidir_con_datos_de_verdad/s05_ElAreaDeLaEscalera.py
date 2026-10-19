"""Escena 05 — El área bajo la curva: sus dos referencias y la cuenta en la escalera (13/16)."""
from comun.escena import *
from comun.figuras_c9e6 import *


class ElAreaDeLaEscalera(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.P = PlanoRoc9(origen=(-5.6, -2.5), lado=4.9)
        self.referencias()
        self.cuenta()
        self.wait(1.0)
        self.limpiar()

    def regla(self) -> VGroup:
        """Regla de 0,5 a 1 a la derecha, donde se marcan las áreas. `.p(v)`."""
        x0, x1, y = 1.2, 6.2, -2.3
        base = Line([x0, y, 0], [x1, y, 0], color=INK, stroke_width=3)
        g = VGroup(base)
        g.p = lambda v: np.array([x0 + (v - 0.5) / 0.5 * (x1 - x0), y, 0])
        return g

    def marca(self, R, v: float, txt: str, color) -> VGroup:
        t = Line(R.p(v) + DOWN * 0.15, R.p(v) + UP * 0.15, color=color, stroke_width=4)
        r = Text(txt, color=color).scale(0.42).next_to(t, DOWN, buff=0.12)
        return VGroup(t, r)

    # ------------------------------------------------------------ b1
    def referencias(self):
        P = self.P
        with self.narrar("b1"):
            # «resumir toda la curva»
            self.en("curva")
            curva = P.curva()
            diag = P.diagonal()
            self.play(FadeIn(P), Create(diag), Create(curva), run_time=self.dur(0.8))
            self.curva, self.diag = curva, diag

            # «en un solo número»
            self.en("numero")
            q = MathTex(r"= \ ?", color=TXT).scale(1.1).move_to([3.6, 1.6, 0])
            self.pop(q)

            # «el área que queda debajo»
            self.en("area")
            area = area_curva6(P)
            auc = Text("AUC", color=ROC, weight=BOLD).scale(0.6).next_to(q, LEFT, buff=0.3)
            self.play(FadeIn(area), FadeIn(auc), run_time=self.dur(0.6))
            self.area, self.q, self.auc = area, q, auc

            # «Para la diagonal»
            self.en("diagonal")
            tri = Polygon(P.p(0, 0), P.p(1, 1), P.p(1, 0), stroke_width=0).set_fill(INK, 0.3)
            self.play(FadeOut(area), curva.animate.set_stroke(opacity=0.25),
                      diag.animate.set_stroke(TXT, width=4), FadeIn(tri), run_time=self.dur(0.5))
            self.tri = tri

            # «tira una moneda»
            self.en("moneda")
            mon = moneda("", AMBAR).scale(0.45).move_to(P.p(0.3, 0.55))
            self.play(FadeIn(mon), Rotate(mon, PI, axis=UP), run_time=self.dur(0.6))
            self.mon = mon

            # «el área es un medio»
            self.en("medio")
            R = self.regla()
            m05 = self.marca(R, 0.5, "0,5", INK)
            t05 = Text("Área = 0,5", color=TXT).scale(0.55).move_to([3.6, 0.4, 0])
            self.play(FadeIn(t05, shift=UP * 0.1), Create(R), FadeIn(m05), run_time=self.dur(0.5))
            self.R = R

            # «el detector perfecto»
            self.en("perfecto")
            perf = VMobject(stroke_color=VERDE, stroke_width=6)
            perf.set_points_as_corners([P.p(0, 0), P.p(0, 1), P.p(1, 1)])
            cuad = Square(side_length=P.lado, stroke_width=0).set_fill(VERDE, 0.18).move_to(P.p(0.5, 0.5))
            self.play(FadeOut(mon), FadeOut(tri), Create(perf), FadeIn(cuad), run_time=self.dur(0.6))

            # «uno.»
            self.en("uno")
            t1 = Text("Área = 1", color=VERDE).scale(0.55).next_to(t05, DOWN, buff=0.3)
            m1 = self.marca(R, 1.0, "1", VERDE)
            self.play(FadeIn(t1, shift=UP * 0.1), FadeIn(m1), run_time=self.dur(0.4))
            self.ref = VGroup(perf, cuad, t05, t1)

    # ------------------------------------------------------------ b2
    def cuenta(self):
        P = self.P
        E = Escalera6(P)
        with self.narrar("b2"):
            # «nuestra escalera»
            self.en("escalera")
            esc = E.todo()
            self.play(FadeOut(self.ref), FadeOut(self.curva), FadeOut(self.q), FadeOut(self.auc),
                      self.diag.animate.set_stroke(INK, width=3), Create(esc), run_time=self.dur(0.6))

            # «cuatro columnas»
            self.en("columnas")
            cols = E.columnas(opacidad=0.0)
            self.play(Create(cols), run_time=self.dur(0.6))

            # «un cuarto de ancho»
            self.en("ancho")
            ll = Brace(cols[0], DOWN, buff=0.45, color=TXT)
            lt = Text("¼", color=TXT).scale(0.5).next_to(ll, DOWN, buff=0.08)
            self.play(FadeIn(ll), FadeIn(lt), run_time=self.dur(0.4))

            alturas = ["2/4", "3/4", "1", "1"]
            rots = VGroup()

            def col(i):
                r = Text(alturas[i], color=TXT, weight=BOLD).scale(0.55).move_to(cols[i].get_center())
                rots.add(r)
                return [cols[i].animate.set_fill(ROC, 0.4), FadeIn(r)]

            # «dos cuartos»
            self.en("c1")
            self.play(*col(0), run_time=self.dur(0.4))
            # «tres cuartos»
            self.en("c2")
            self.play(*col(1), run_time=self.dur(0.4))
            # «uno y uno»
            self.en("c34")
            self.play(*col(2), *col(3), run_time=self.dur(0.4))

            # «Sumamos y dividimos»
            self.en("suma")
            f = MathTex(r"\left(\frac24 + \frac34 + 1 + 1\right)", r"\,/\,4", color=TXT).scale(1.0)
            f.move_to([3.5, 1.6, 0])
            self.play(Write(f[0]), run_time=self.dur(0.7))
            self.play(Write(f[1]), run_time=self.dur(0.3))

            # «trece dieciseisavos»
            self.en("trece")
            g = MathTex(r"= \frac{13}{16}", color=ROC).scale(1.1).next_to(f, DOWN, buff=0.35)
            self.pop(g)

            # «Cero coma ochenta y uno»
            self.en("ochentayuno")
            h = MathTex(r"= 0{,}81", color=ROC).scale(1.0).next_to(g, DOWN, buff=0.3)
            m = self.marca(self.R, 0.8125, "0,81", ROC)
            self.play(FadeIn(h, shift=UP * 0.1), run_time=self.dur(0.35))
            self.play(FadeIn(m, shift=DOWN * 0.3), run_time=self.dur(0.35))
