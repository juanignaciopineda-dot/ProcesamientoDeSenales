"""Escena 12 — Por qué ninguna regla le gana: una columna por cada r y el error como área."""
from comun.escena import *
from comun.figuras_c9e1 import *

RS = np.linspace(-2.2, 4.4, 23)      # las rebanadas


def campanas_grandes():
    """Lienzo de las campanas ya escaladas (0,7 y 0,3), con la altura aprovechada."""
    return Campanas9(centro=(0.0, -2.6), alto=8.0, v_max=0.3)


class InfinitasColumnas(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.columnas()
        self.promedio()
        self.ninguna()
        self.wait(1.0)
        self.limpiar()

    def bajo_alto(self, r):
        a, b = self.C.f(0, r, P0), self.C.f(2, r, P1)
        return min(a, b), max(a, b)

    def columnas(self):
        C = campanas_grandes()
        self.C = C
        with self.narrar("b1"):
            # «¿Es la mejor regla posible»
            self.en("pregunta")
            p = Text("¿La mejor?", color=ESTIMACION, weight=BOLD).scale(0.75).move_to([0, 3.35, 0])
            self.pop(p)

            # «o solo una regla razonable»
            self.en("razonable")
            q = Text("¿O solo razonable?", color=INK).scale(0.6).move_to([0, 2.65, 0])
            self.play(FadeIn(q, shift=UP * 0.15), run_time=self.dur(0.4))
            self.preg = VGroup(p, q)

            # «las columnas de la tabla»
            self.en("tabla")
            T = TablaCanal(centro=(0, -0.3), lado=1.4, esc=0.55)
            T.prob[0][1].set_color(ERROR)
            T.prob[1][0].set_color(ERROR)
            tabla = VGroup(T.armazon(), T.probs())
            self.play(FadeIn(tabla), run_time=self.dur(0.5))

            # «infinitas columnas»
            self.en("rebanadas")
            eje = C.eje((0, 1, 2))
            c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
            reb = VGroup(*[Line(C.p(r), C.p(r, self.bajo_alto(r)[1]), color=INK, stroke_width=3, stroke_opacity=0.7)
                           for r in RS])
            self.play(FadeOut(tabla, scale=0.6), FadeOut(self.preg), run_time=self.dur(0.4))
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.6))
            self.play(LaggedStart(*[Create(l) for l in reb], lag_ratio=0.05), run_time=self.dur(0.8))
            self.eje, self.c0, self.c1, self.reb = eje, c0, c1, reb

            # «una por cada»
            self.en("cada")
            cada = VGroup(Text("Una columna por cada", color=TXT).scale(0.55), MathTex("r", color=MEDIDA).scale(0.8))
            cada.arrange(RIGHT, buff=0.15).move_to([0, 2.7, 0])
            self.cada = cada
            self.play(FadeIn(cada), run_time=self.dur(0.4))

            # «si dices uno»
            self.en("di1")
            r1 = 2.2
            s1 = Line(C.p(r1), C.p(r1, C.f(0, r1, P0)), color=ERROR, stroke_width=9)
            self.play(Create(s1), run_time=self.dur(0.4))

            # «si dices cero»
            self.en("di0")
            r0 = 0.6
            s0 = Line(C.p(r0), C.p(r0, C.f(2, r0, P1)), color=ERROR, stroke_width=9)
            self.play(Create(s0), run_time=self.dur(0.4))

            # «Quedarte con la mayor»
            self.en("mayor")
            rojos = VGroup(*[Line(C.p(r), C.p(r, self.bajo_alto(r)[0]), color=ERROR, stroke_width=4) for r in RS])
            verdes = VGroup(*[Line(C.p(r, self.bajo_alto(r)[0]), C.p(r, self.bajo_alto(r)[1]), color=VERDE,
                                   stroke_width=4) for r in RS])
            self.play(FadeOut(s1), FadeOut(s0), FadeOut(reb), FadeIn(rojos), FadeIn(verdes), run_time=self.dur(0.6))
            self.rojos, self.verdes = rojos, verdes

            # «fallar lo menos posible ahí»
            self.en("menos")
            self.play(rojos.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.7))

    def promedio(self):
        C = self.C
        with self.narrar("b2"):
            # «La probabilidad de error total»
            self.en("pe")
            pe = MathTex(r"P(\text{error})", color=ERROR).scale(0.9).move_to([0, 2.7, 0])
            self.play(FadeOut(self.cada), FadeIn(pe), run_time=self.dur(0.4))

            # «el promedio de esos fallos»
            self.en("promedio")
            copias = VGroup(*[self.rojos[i].copy() for i in range(4, 20, 3)])
            self.add(copias)
            self.play(*[c.animate.move_to(pe.get_bottom() + DOWN * 0.3).scale(0.2).set_opacity(0) for c in copias],
                      run_time=self.dur(0.8))
            self.remove(copias)

            # «sobre todos los valores de erre»
            self.en("todos")
            cur = Line(C.p(C.r0), C.p(C.r0) + UP * 4.0, color=MEDIDA, stroke_width=3)
            self.play(FadeIn(cur), run_time=0.2)
            self.play(cur.animate.shift(C.p(C.r1) - C.p(C.r0)), run_time=self.dur(2.4), rate_func=linear)
            self.play(FadeOut(cur), run_time=0.2)

            # «lo a menudo que aparece»
            self.en("peso")
            t = np.linspace(C.r0, C.r1, 200)
            mezcla = DashedVMobject(C.L.curva(t, C.f(0, t, P0) + C.f(2, t, P1), TXT, 3), num_dashes=70)
            peso = Text("Peso", color=TXT).scale(0.5).move_to(C.p(-1.9, 0.2))
            self.play(Create(mezcla), FadeIn(peso), run_time=self.dur(0.8))
            self.mezcla = mezcla

            # «Ese peso es una densidad»
            self.en("densidad")
            dens = MathTex(r"f(r)", color=TXT).scale(0.75).move_to(peso)
            self.play(ReplacementTransform(peso, dens), run_time=self.dur(0.5))
            self.dens = dens

            # «nunca es negativa»
            self.en("positiva")
            pos = MathTex(r"f(r) \ge 0", color=ESTIMACION).scale(0.8).move_to([4.6, 2.0, 0])
            self.pop(pos)
            self.pos = pos

            # «El promedio es una integral»
            self.en("integral")
            integ = MathTex(r"P(\text{error})", "=", r"\int \ldots \, dr", color=ERROR).scale(0.9).move_to([0, 2.7, 0])
            self.play(ReplacementTransform(pe, integ[0]), FadeIn(integ[1:]), run_time=self.dur(0.6))
            self.integ = integ

            # «rebanadas muy finas»
            self.en("finas")
            a1 = C.area(2, P1, C.r0, CRUCE9, ERROR, 0.5)
            a0 = C.area(0, P0, CRUCE9, C.r1, ERROR, 0.5)
            self.play(FadeOut(self.verdes), ReplacementTransform(self.rojos, VGroup(a1, a0)),
                      FadeOut(self.mezcla), FadeOut(dens), FadeOut(pos), run_time=self.dur(1.0))
            self.areas = VGroup(a1, a0)

    def ninguna(self):
        C = self.C
        with self.narrar("b3"):
            # «Cualquier otra regla»
            self.en("otra")
            r = 1.15
            otra = Line(C.p(r), C.p(r, C.f(0, r, P0)), color=ERROR, stroke_width=10)
            rot = Text("Otra regla", color=INK).scale(0.45).move_to(C.p(r, 0.3) + UP * 0.2 + LEFT * 0.6)
            self.play(Create(otra), FadeIn(rot), run_time=self.dur(0.5))

            # «lo mismo o más»
            self.en("mayor")
            ge = MathTex(r"\ge", color=ESTIMACION).scale(0.9).next_to(rot, RIGHT, buff=0.25)
            self.pop(ge)

            # «Y sumar cosas»
            self.en("sumar")
            ges = VGroup(*[MathTex(r"\ge", color=ESTIMACION).scale(0.7).move_to([x, 1.9, 0]) for x in (-3.0, -1.6, 1.6)])
            self.play(LaggedStart(*[FadeIn(g) for g in ges], lag_ratio=0.3), run_time=self.dur(0.6))
            self.play(*[g.animate.move_to([4.6, 1.9, 0]) for g in ges], run_time=self.dur(0.6))

            # «con pesos que nunca son negativos»
            self.en("pesos")
            pos = MathTex(r"f(r) \ge 0", color=ESTIMACION).scale(0.75).move_to([4.6, 1.45, 0])
            self.play(FadeIn(pos), run_time=self.dur(0.4))

            # «da un total igual o»
            self.en("total")
            tot = MathTex(r"P(\text{error, otra})", r"\ge", r"P(\text{error, MAP})", color=TXT).scale(0.85)
            tot[0].set_color(ERROR)
            tot[2].set_color(VERDE)
            tot.move_to([-0.4, 2.7, 0])
            self.play(FadeOut(self.integ), FadeOut(ges), FadeOut(pos), FadeIn(tot), run_time=self.dur(0.6))

            # «Ninguna regla puede ganarle»
            self.en("gana")
            ok = tilde(VERDE, 0.6).next_to(tot, RIGHT, buff=0.35)
            self.play(Create(ok), run_time=self.dur(0.4))
            self.sfx("exito", gain=-18)

            # «En el dibujo»
            self.en("dibujo")
            self.play(FadeOut(otra), FadeOut(rot), FadeOut(ge), run_time=self.dur(0.4))

            # «el área bajo la»
            self.en("area")
            et = Text("Error = área roja", color=ERROR, weight=BOLD).scale(0.55).move_to([3.4, 0.4, 0])
            self.play(self.areas.animate(rate_func=there_and_back).set_fill(opacity=0.85), FadeIn(et),
                      run_time=self.dur(0.7))

            # «Si mueves el umbral»
            self.en("mueve")
            u = Line(C.p(CRUCE9) + DOWN * 0.15, C.p(CRUCE9) + UP * 2.6, color=ESTIMACION, stroke_width=4)
            self.play(Create(u), run_time=self.dur(0.3))
            self.play(u.animate.shift(C.p(1) - C.p(CRUCE9)), run_time=self.dur(0.8))

            # «un trozo»
            self.en("trozo")
            t = np.linspace(1, CRUCE9, 30)
            arr = [C.p(a, C.f(0, a, P0)) for a in t]
            aba = [C.p(a, C.f(2, a, P1)) for a in t[::-1]]
            trozo = Polygon(*arr, *aba, stroke_width=0, stroke_opacity=0).set_fill(ERROR, 0.95)
            dm = Text("De más", color=ERROR, weight=BOLD).scale(0.5).move_to(C.p(1.2, 0.27) + UP * 0.5)
            self.play(FadeIn(trozo), FadeIn(dm), run_time=self.dur(0.5))
            self.play(trozo.animate(rate_func=there_and_back).scale(1.15), run_time=self.dur(0.6))
