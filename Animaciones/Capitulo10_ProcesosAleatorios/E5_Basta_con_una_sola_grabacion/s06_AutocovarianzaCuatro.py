"""Escena 06 — La autocovarianza de la pila vale 4 para cualquier separación."""
from comun.escena import *


class AutocovarianzaCuatro(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        L = Lienzo(ancho=5.2, alto=1.6, t_rango=(0, 1), v_max=3.0, centro=(-3.6, 2.5))
        Lc = Lienzo(ancho=6.2, alto=2.6, t_rango=(-2, 2), v_max=5.0, centro=(3.2, -0.4))
        tau = np.linspace(-2, 2, 200)
        Lo = Lienzo(ancho=5.2, alto=1.3, t_rango=(0, 2), v_max=1.25, centro=(-3.6, -2.6))

        with self.narrar("b1"):
            # «La autocovarianza»
            self.en("autocov")
            ejes_c = Line(Lc.p(-2, 0), Lc.p(2, 0), color=INK, stroke_width=2)
            eje_v = Line(Lc.p(0, -0.3), Lc.p(0, 5.0), color=INK, stroke_width=2)
            ct = MathTex(r"C(\tau)", color=INK).scale(0.8).move_to(Lc.p(0.45, 5.0))
            self.play(Create(ejes_c), Create(eje_v), FadeIn(ct), run_time=self.dur(0.7))

            # «La muestra de ahora»
            self.en("ahora")
            rec = Line(L.p(0, 2), L.p(1, 2), color=AMBAR, stroke_width=6)
            base = L.base()
            m1 = Dot(L.p(0.2, 2), radius=0.14, color=TXT)
            self.play(Create(base), Create(rec), FadeIn(m1, scale=0.5), run_time=self.dur(0.7))

            # «de dentro de una hora»
            self.en("hora")
            m2 = Dot(L.p(0.8, 2), radius=0.14, color=TXT)
            hr = etiqueta("1 hora", INK, 0.5).next_to(L.p(0.5, 2), UP, buff=0.25)
            self.play(FadeIn(m2, scale=0.5), FadeIn(hr), run_time=0.4)

            # «son el mismo número»
            self.en("mismo")
            ig = MathTex("=", color=AMBAR).scale(1.4).move_to(L.p(0.5, 0.7))
            self.pop(ig)

            # «es la varianza»
            self.en("esvar")
            f = MathTex(r"C(\tau)", "=", r"\sigma^2", color=TXT).scale(1.3).move_to([3.2, 2.9, 0])
            f[2].set_color(AMBAR)
            self.play(FadeIn(f), run_time=0.5)

            # «cuatro»
            self.en("cuatro")
            f4 = MathTex("=", "4", color=AMBAR).scale(1.3).next_to(f, RIGHT, buff=0.15)
            self.pop(f4)

            # «cualquier separación»
            self.en("sep")
            recta4 = Line(Lc.p(-2, 4), Lc.p(2, 4), color=AMBAR, stroke_width=6)
            self.play(Create(recta4), run_time=self.dur(1.0))

            # «cuatro a un segundo»
            self.en("seg")
            p1 = Dot(Lc.p(1.0, 4), radius=0.13, color=TXT)
            t1 = etiqueta("1 s", TXT, 0.5).move_to(Lc.p(1.0, -0.9))
            self.play(FadeIn(p1, scale=0.5), FadeIn(t1), run_time=0.4)

            # «cuatro a un año»
            self.en("ano")
            p2 = Dot(Lc.p(1.8, 4), radius=0.13, color=TXT)
            t2 = etiqueta("1 año", TXT, 0.5).move_to(Lc.p(1.8, -0.9))
            self.play(FadeIn(p2, scale=0.5), FadeIn(t2), run_time=0.4)

            # «Los osciladores tampoco olvidaban»
            self.en("osc")
            t = np.linspace(0, 2, 160)
            base_o = Lo.base()
            cos = Lo.curva(t, np.cos(2 * PI * 0.8 * t), SENAL, 4)
            self.play(Create(base_o), Create(cos), run_time=self.dur(1.2))

            # «recorría todos sus valores»
            self.en("recorre")
            d = Dot(Lo.p(0, 1.0), radius=0.12, color=AMBAR)
            self.add(d)
            self.play(MoveAlongPath(d, cos), run_time=self.dur(2.0), rate_func=linear)

            # «Cada pila se queda quieta»
            self.en("quieta")
            ench = VGroup(*[Line(a, b, color=ROJO, stroke_width=3) for a, b in (
                (L.p(0, 2) + UP * 0.2, L.p(1, 2) + UP * 0.2), (L.p(1, 2) + UP * 0.2, L.p(1, 2) + DOWN * 0.2),
                (L.p(1, 2) + DOWN * 0.2, L.p(0, 2) + DOWN * 0.2), (L.p(0, 2) + DOWN * 0.2, L.p(0, 2) + UP * 0.2))])
            self.play(Create(ench), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
