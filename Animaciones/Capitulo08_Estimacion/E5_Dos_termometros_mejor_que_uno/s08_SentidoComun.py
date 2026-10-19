"""Escena 08 — Sentido común: cada termómetro pesa según su ruido, los pesos suman menos de uno y más
mediciones nunca empeoran."""
from comun.escena import *
from comun.figuras_c8e5 import *


def casilla_num(n: int, centro) -> VGroup:
    r = RoundedRectangle(corner_radius=0.12, width=0.75, height=0.75, color=INK, stroke_width=3)
    r.set_fill(INK, 0.1).move_to([centro[0], centro[1], 0])
    t = Text(str(n), color=TXT, weight=BOLD).scale(0.6).move_to(r)
    g = VGroup(r, t)
    g.r = r
    return g


class SentidoComun(EscenaCurso):
    ESCENA = "08"

    def barra(self, x, base_y, alto, color, ancho=1.1):
        b = Rectangle(width=ancho, height=alto, color=color, stroke_width=0).set_fill(color, 0.85)
        return b.move_to([x, base_y + alto / 2, 0])

    def construct(self):
        c1 = casilla_num(1, (-6.2, 3.25))
        c2 = casilla_num(2, (-5.25, 3.25))
        by = -1.6
        # los pesos (ámbar) a la izquierda
        ba = self.barra(-4.4, by, 2.6, ESTIMACION)
        bb = self.barra(-2.6, by, 0.65, ESTIMACION)
        suelo_p = Line([-5.4, by, 0], [-1.6, by, 0], color=INK, stroke_width=2)
        la = MathTex("h_A", color=ESTIMACION).scale(0.8).move_to([-4.4, by - 0.4, 0])
        lb = MathTex("h_B", color=ESTIMACION).scale(0.8).move_to([-2.6, by - 0.4, 0])
        va = MathTex(r"\frac{2}{3}", color=TXT).scale(0.8).next_to(ba, UP, buff=0.15)
        vb = MathTex(r"\frac{1}{6}", color=TXT).scale(0.8).next_to(bb, UP, buff=0.15)
        x4 = MathTex(r"\times 4", color=AMBAR).scale(1.0).move_to([-2.6, 1.6, 0])
        # los ruidos (magenta) a la derecha
        ra = self.barra(2.0, by, 0.65, RUIDO)
        rb = self.barra(3.8, by, 2.6, RUIDO)
        suelo_r = Line([1.0, by, 0], [4.8, by, 0], color=INK, stroke_width=2)
        lra = MathTex("A", color=MEDIDA).scale(0.8).move_to([2.0, by - 0.4, 0])
        lrb = MathTex("B", color=MEDIDA).scale(0.8).move_to([3.8, by - 0.4, 0])
        vra = MathTex(r"\sigma^2=1", color=TXT).scale(0.7).next_to(ra, UP, buff=0.15)
        vrb = MathTex(r"\sigma^2=4", color=TXT).scale(0.7).next_to(rb, UP, buff=0.15)
        d4 = MathTex(r"\div 4", color=RUIDO).scale(1.0).move_to([2.0, 1.6, 0])
        regla = MathTex(r"\frac{2}{3}:\frac{1}{6}=4:1", color=VERDE).scale(1.0).move_to([-0.3, -3.0, 0])
        # comprobación 2
        suma = formula(r"\frac{2}{3}+\frac{1}{6}", "=", r"\frac{5}{6}", escala=1.2,
                       colores={2: ESTIMACION}).move_to([-1.2, 1.7, 0])
        menos1 = MathTex("<1", color=AMBAR).scale(1.2).next_to(suma, RIGHT, buff=0.3)
        R = RectaNum(19.5, 24.5, centro=(0.0, -1.3), ancho=10.0, marcas=[20, 21, 22, 23, 24])
        p = Dot(R.p(22.33), radius=0.13, color=ESTIMACION)
        pl = MathTex(r"22{,}33", color=ESTIMACION).scale(0.8).next_to(p, UP, buff=0.95)
        tira = Arrow(R.p(22.33) + UP * 0.5, R.p(21.2) + UP * 0.5, buff=0, color=AMBAR, stroke_width=5,
                     max_tip_length_to_length_ratio=0.25)
        media = Text("Media", color=SENAL).scale(0.5).move_to(R.p(20) + DOWN * 0.95)
        # la regla general
        d = barras8([4, 0.8, 0.67], ["Sin dato", "A", "A y B"], centro=(0.0, -0.5), ancho=7.0, alto=4.0, v_max=4.0,
                    textos=["4", "0,8", "0,67"])

        with self.narrar("b1"):
            # «Dos comprobaciones»
            self.en("dos")
            self.play(FadeIn(c1, shift=DOWN * 0.1), FadeIn(c2, shift=DOWN * 0.1), run_time=self.dur(0.4))
            self.play(c1.r.animate.set_stroke(AMBAR, 4), run_time=0.3)

            # «A pesa dos tercios»
            self.en("pa")
            self.play(Create(suelo_p), GrowFromEdge(ba, DOWN), FadeIn(la), FadeIn(va), run_time=self.dur(0.6))

            # «y B un sexto»
            self.en("pb")
            self.play(GrowFromEdge(bb, DOWN), FadeIn(lb), FadeIn(vb), run_time=self.dur(0.5))

            # «cuatro veces más»
            self.en("x4")
            self.pop(x4)

            # «Y el ruido de A»
            self.en("ra")
            self.play(Create(suelo_r), GrowFromEdge(ra, DOWN), FadeIn(lra), FadeIn(vra), run_time=self.dur(0.5))

            # «cuatro veces más pequeño»
            self.en("r4")
            self.play(GrowFromEdge(rb, DOWN), FadeIn(lrb), FadeIn(vrb), run_time=self.dur(0.5))
            self.pop(d4)

            # «Cada termómetro pesa según lo poco que se equivoca»
            self.en("regla")
            self.play(FadeIn(regla, shift=UP * 0.15), run_time=self.dur(0.6))
            self.sfx("exito")

            # «Además»
            self.en("ademas")
            self.corte(c1, c2)
            self.play(c1.r.animate.set_stroke(INK, 3), c2.r.animate.set_stroke(AMBAR, 4), run_time=self.dur(0.4))

            # «los pesos suman cinco sextos»
            self.en("suma")
            self.play(FadeIn(suma, shift=UP * 0.1), run_time=self.dur(0.6))

            # «menos de uno»
            self.en("menos1")
            self.pop(menos1)

            # «tirando un poco hacia la media»
            self.en("media")
            self.play(Create(R.base), *[Create(R.ticks[v]) for v in R.ticks], *[FadeIn(R.nums[v]) for v in R.nums],
                      FadeIn(media), run_time=self.dur(0.6))
            self.play(FadeIn(p, scale=0.5), FadeIn(pl), run_time=0.3)
            self.play(GrowArrow(tira), run_time=self.dur(0.6))

            # «una regla general»
            self.en("general")
            self.corte()
            self.play(Create(d["base"]), *[FadeIn(r) for r in d["rots"]], run_time=self.dur(0.5))

            # «nunca empeora el error»
            self.en("nunca")
            for i in range(3):
                self.play(GrowFromEdge(d["barras"][i], DOWN), FadeIn(d["vals"][i]), run_time=0.45)
        self.wait(1.0)
        self.limpiar()
