"""Escena 05 — Leer una condicional en la tabla; de la conjunta salen las marginales, pero no al revés."""
from comun.escena import *

VALORES = [[r"0{,}63", r"0{,}07"], [r"0{,}03", r"0{,}27"]]


class LeerCondicional(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.t = Tabla2x2(centro=(-3.0, 0.0), lado=2.0)
        self.vals = [[self.t.valor(i, j, VALORES[i][j], VERDE, 1.2) for j in range(2)] for i in range(2)]
        self.add(self.t, *[v for f in self.vals for v in f])
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def columna(self, j, color=AMBAR):
        t = self.t
        return Rectangle(width=t.lado, height=2 * t.lado, color=color, stroke_width=5).move_to(
            (t.c(0, j) + t.c(1, j)) / 2)

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        t = self.t
        mundo = SurroundingRectangle(VGroup(*[c for f in t.cel for c in f]), color=INK, buff=0.05, stroke_width=4)
        col1 = self.columna(1)
        vela = Rectangle(width=t.lado, height=2 * t.lado, stroke_width=0).set_fill(FONDO, 0.72).move_to(
            (t.c(0, 0) + t.c(1, 0)) / 2)
        cond = formula(r"P(S{=}1\mid R{=}1)", "=", escala=1.0, colores={0: AMBAR}).move_to([3.6, 2.6, 0])
        frac = MathTex(r"\dfrac{0{,}27}{0{,}34}", color=TXT).scale(1.3).move_to([3.0, 0.5, 0])
        r79 = MathTex(r"\approx 0{,}79", color=VERDE).scale(1.3).next_to(frac, RIGHT, buff=0.25)
        with self.narrar("b1"):
            # «las condicionales»
            self.en("condicionales")
            pal = self.palabra("condicionales", AMBAR, 1.0).move_to([3.6, 3.4, 0])
            self.pop(pal)

            # «se recibió un uno»
            self.en("uno")
            self.play(Create(mundo), run_time=self.dur(0.4))
            self.resaltar(t.rot_c[1], color=MEDIDA, run_time=0.5)
            self.play(FadeIn(cond, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «solo con esa columna»
            self.en("columna")
            self.play(FadeIn(vela), run_time=self.dur(0.5))

            # «el mundo se achica»
            self.en("achica")
            self.play(ReplacementTransform(mundo, col1), run_time=self.dur(0.9))

            # «como con el dado»
            self.en("dado")
            cara = dado_n(4).scale(0.9).move_to([5.6, 1.4, 0])
            self.pop(cara)

            # «el uno enviado pesa»
            self.en("pesa")
            m = t.marco(1, 1, VERDE)
            self.play(FadeOut(cara), run_time=0.2)
            self.play(Create(m), run_time=self.dur(0.4))

            # «cero coma veintisiete de un total de»
            self.en("total")
            self.play(FadeIn(frac, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «cero coma treinta y cuatro»
            self.en("t34")
            self.play(Indicate(frac, color=AMBAR, scale_factor=1.15), run_time=self.dur(0.6))

            # «cero coma setenta y nueve»
            self.en("r79")
            self.play(FadeIn(r79, shift=LEFT * 0.2), run_time=self.dur(0.5))
            self.play(FadeIn(formula(r"0{,}79", escala=1.0, color=VERDE).next_to(cond, RIGHT, buff=0.2)),
                      run_time=self.dur(0.4))

            # «el mismo número que nos dio Bayes»
            self.en("bayes")
            bayes = Text("el mismo de Bayes", color=VERDE).scale(0.6).next_to(frac, DOWN, buff=0.7)
            self.pop(bayes)

            # «leído directamente de la tabla»
            self.en("leido")
            self.resaltar(m, color=VERDE, escala=1.15, run_time=0.7)
        self.col1, self.vela, self.m = col1, vela, m
        self.resto = VGroup(pal, cond, frac, r79, bayes)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        t = self.t
        with self.narrar("b2"):
            # «siempre puedes sacar las marginales»
            self.en("sacar")
            self.play(FadeOut(self.resto), FadeOut(self.col1), FadeOut(self.vela), FadeOut(self.m), run_time=0.4)
            marg = VGroup(MathTex(r"0{,}7\ \ 0{,}3", color=SENAL), MathTex(r"0{,}66\ \ 0{,}34", color=MEDIDA)
                          ).arrange(DOWN, buff=0.6).scale(1.0).move_to([4.3, 0.0, 0])
            etiq = Text("marginales", color=AMBAR).scale(0.65).next_to(marg, UP, buff=0.4)
            suma = Arrow([-1.2, 0.0, 0], [2.0, 0.0, 0], color=VERDE, buff=0, stroke_width=6,
                         max_tip_length_to_length_ratio=0.2)
            sumando = Text("sumando", color=VERDE).scale(0.55).next_to(suma, UP, buff=0.1)
            self.play(GrowArrow(suma), FadeIn(sumando), run_time=self.dur(0.6))
            self.play(FadeIn(marg), FadeIn(etiq), run_time=self.dur(0.5))

            # «Pero al revés, no»
            self.en("alreves")
            atras = Arrow([2.0, -1.3, 0], [-1.2, -1.3, 0], color=ERROR, buff=0, stroke_width=6,
                          max_tip_length_to_length_ratio=0.2)
            x = cruz(ERROR, 0.9).move_to([0.4, -1.3, 0])
            self.play(GrowArrow(atras), run_time=self.dur(0.5))
            self.pop(x)

            # «cuánto se envía y cuánto se recibe»
            self.en("solo_m")
            self.corte()
            t2 = Tabla2x2(centro=(-3.0, 0.0), lado=2.0)
            sf = [MathTex(s, color=SENAL).scale(1.0).move_to(t2.p_fila(i) + RIGHT * 0.2) for i, s in enumerate((r"0{,}7", r"0{,}3"))]
            sc = [MathTex(s, color=MEDIDA).scale(1.0).move_to(t2.p_col(j)) for j, s in enumerate((r"0{,}66", r"0{,}34"))]
            self.play(Create(VGroup(*[c for f in t2.cel for c in f])), FadeIn(VGroup(*t2.rot_f, *t2.rot_c)),
                      FadeIn(VGroup(*sf, *sc)), run_time=self.dur(0.8))

            # «cómo se relacionan»
            self.en("relacionan")
            qs = VGroup(*[Text("?", color=AMBAR, weight=BOLD).scale(1.3).move_to(t2.c(i, j))
                          for i in range(2) for j in range(2)])
            self.play(LaggedStart(*[FadeIn(q, scale=0.4) for q in qs], lag_ratio=0.2), run_time=self.dur(0.9))

            # «lo que nos interesa»
            self.en("interesa")
            marco = SurroundingRectangle(VGroup(*[c for f in t2.cel for c in f]), color=AMBAR, buff=0.06, stroke_width=5)
            rel = self.palabra("la relación", AMBAR, 1.1).move_to([3.8, 0.4, 0])
            self.play(Create(marco), run_time=self.dur(0.4))
            self.pop(rel)

            # «las variables son continuas»
            self.en("continuas")
            self.play(FadeOut(VGroup(t2, qs, marco, rel, *sf, *sc)), run_time=0.4)
            x_, y_ = nube_xy7(40, 5)
            puntos = VGroup(*[Dot([1.7 * a, 1.1 * b, 0], radius=0.09, color=SENAL) for a, b in zip(x_, y_)])
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in puntos], lag_ratio=0.03), run_time=self.dur(1.2))

            # «se convierte en otra cosa»
            self.en("otra")
            self.play(LaggedStart(*[p.animate.set_color(AMBAR) for p in puntos], lag_ratio=0.05), run_time=self.dur(1.2))
