"""Escena 10 — El precio de la causalidad (1): con la señal blanqueada el error se separa en un término por coeficiente."""
from comun.escena import *


def _mini_parabola(cx: float, R: float, color=TXT):
    """Parábola f(g) = g² − 2Rg (σ² = 1) sobre un lienzo pequeño. Devuelve (lienzo, curva, vértice, punto en g = 0)."""
    L = Lienzo(ancho=3.0, alto=3.0, t_rango=(-0.6, 3.2), v_max=4.0, centro=(cx, -0.4))
    f = lambda g: g * g - 2 * R * g
    cur = curva_f(L, f, -0.55, 3.15, color, 3.5)
    base = L.base(INK, 1.5)
    vert = Dot(L.p(R, f(R)), radius=0.1, color=VERDE)
    cero = Dot(L.p(0, f(0)), radius=0.1, color=ERROR)
    return L, VGroup(base, cur), vert, cero


class ElErrorEnLaSenalBlanca(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        precio = Text("el precio de la causalidad", color=AMBAR, weight=BOLD).scale(0.8).move_to([-1.5, 3.3, 0])
        etq = VGroup(RoundedRectangle(corner_radius=0.1, width=0.7, height=0.5, color=AMBAR, stroke_width=3),
                     Text("€", color=AMBAR, weight=BOLD).scale(0.45)).move_to([3.3, 3.3, 0])
        cad, bl, ent, sal = cadena_bloques("x", "1/F", "ε", centro=(0.0, 1.9), color=CIAN)
        ent.set_color(MEDIDA)
        cad.scale(1.35, about_point=np.array([0.0, 1.9, 0.0]))
        F = formula("error", "=", r"\sigma_y^2", r"-\,2\sum g[m]\,R[m]", r"+\,\sigma^2\sum g[m]^2", escala=1.1,
                    colores={0: ERROR, 2: SENAL})
        F.move_to([0, 0.2, 0])
        F[0].set_color(ERROR)
        oculta(F)
        cols = VGroup()
        for i, m in enumerate([-1, 0, 1, 2]):
            t = formula(r"-2\,g\,R", r"+\sigma^2 g^2", escala=0.95)
            lab = etiqueta(f"m = {m}".replace("-", "−"), INK, 0.5).next_to(t, UP, buff=0.2)
            cols.add(VGroup(lab, t))
        cols.arrange(RIGHT, buff=0.55).move_to([0, -2.1, 0])
        seps = VGroup(*[Line([cols[i].get_right()[0] + 0.28, -3.2, 0], [cols[i].get_right()[0] + 0.28, -1.0, 0],
                             color=INK, stroke_width=2) for i in range(3)])
        with self.narrar("b1"):
            # «Pongamos precio a la causalidad»
            self.en("precio")
            self.play(FadeIn(precio, shift=DOWN * 0.2), FadeIn(etq, scale=0.5), run_time=self.dur(0.8))

            # «la señal blanqueada»
            self.en("blanqueada")
            self.play(Create(cad), run_time=self.dur(1.0))

            # «El error de un estimador»
            self.en("error")
            self.add(F)
            self.play(*revelar(F[0], F[1]), run_time=self.dur(0.7))

            # «la varianza de la señal»
            self.en("varianza")
            self.play(*revelar(F[2]), run_time=self.dur(0.7))

            # «menos dos veces la suma de cada coeficiente por su correlación»
            self.en("menos")
            self.play(*revelar(F[3]), run_time=self.dur(1.1))

            # «más sigma cuadrado por la suma de los coeficientes al cuadrado»
            self.en("mas")
            self.play(*revelar(F[4]), run_time=self.dur(1.1))

            # «Como la innovación es blanca»
            self.en("blanca")
            self.resaltar(ent, color=CIAN, run_time=0.6)

            # «cada posición aporta su propio término»
            self.en("propio")
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in cols], lag_ratio=0.2), run_time=self.dur(1.2))

            # «sin mezclarse con las demás»
            self.en("mezclarse")
            self.play(LaggedStart(*[Create(s) for s in seps], lag_ratio=0.2), run_time=self.dur(0.9))

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        self.corte()
        # una parábola grande
        L = Lienzo(ancho=6.0, alto=4.4, t_rango=(-0.6, 3.2), v_max=4.0, centro=(-1.2, 0.0))
        f = lambda g: g * g - 2 * g
        base = L.base(INK, 2.0)
        cur = curva_f(L, f, -0.55, 3.15, TXT, 4.5)
        l_g = MathTex("g", color=INK).scale(0.7).move_to(L.p(3.2, 0) + RIGHT * 0.3)
        vert = Dot(L.p(1, f(1)), radius=0.13, color=VERDE)
        l_v = formula("g", "=", r"R/\sigma^2", escala=0.9, colores={0: VERDE, 2: VERDE}).move_to(L.p(1, f(1)) + DOWN * 0.7)
        l_a = formula(r"-R^2/\sigma^2", escala=1.0, colores={0: ERROR}).move_to(L.p(1, f(1)) + RIGHT * 3.3 + DOWN * 0.6)
        guia = DashedLine(L.p(1, f(1)), L.p(1, f(1)) + RIGHT * 2.2 + DOWN * 0.4, color=ERROR, stroke_width=2.5)
        # cuatro columnas pequeñas
        minis = []
        for cx, R, m in zip([-5.3, -1.85, 1.85, 5.3], [0.3, 0.6, 1.4, 0.9], [-2, -1, 0, 1]):
            Lm, grp, v, c0 = _mini_parabola(cx, R)
            et = etiqueta(f"m = {m}".replace("-", "−"), INK, 0.55).move_to([cx, 1.5, 0])
            minis.append((Lm, grp, v, c0, et, R))
        negs = [minis[0], minis[1]]
        poss = [minis[2], minis[3]]
        l_pos = formula(r"m\ge 0", escala=1.1, colores={0: VERDE}).move_to([3.6, 2.5, 0])
        marco_pos = Rectangle(width=7.0, height=3.9, color=VERDE, stroke_width=2.5, stroke_opacity=0.7).move_to([3.55, 0.0, 0])
        marco_neg = Rectangle(width=7.0, height=3.9, color=ERROR, stroke_width=2.5, stroke_opacity=0.7).move_to([-3.55, 0.0, 0])
        rojos = []
        for (Lm, grp, v, c0, et, R) in negs:
            seg = Line(c0.get_center(), v.get_center(), color=ERROR, stroke_width=6)
            rojos.append(seg)
        with self.narrar("b2"):
            # «Cada término es una parábola»
            self.en("parabola")
            self.play(Create(base), Create(cur), FadeIn(l_g), run_time=self.dur(1.1))

            # «su punto más bajo»
            self.en("bajo")
            self.play(FadeIn(vert, scale=0.3), run_time=self.dur(0.5))

            # «la correlación dividida entre sigma cuadrado»
            self.en("vertice")
            self.play(FadeIn(l_v), run_time=self.dur(0.8))

            # «aporta menos la correlación al cuadrado, entre sigma cuadrado»
            self.en("aporta")
            self.play(Create(guia), FadeIn(l_a), run_time=self.dur(0.9))

            # «El filtro no causal puede colocar todos los coeficientes»
            self.en("nocausal")
            self.play(*[FadeOut(m) for m in (base, cur, l_g, vert, l_v, guia, l_a)], run_time=0.3)
            self.play(*[FadeIn(g) for (_, g, _, _, et, _) in minis], *[FadeIn(et) for (_, _, _, _, et, _) in minis],
                      *[FadeIn(v, scale=0.3) for (_, _, v, _, _, _) in minis], run_time=self.dur(0.9))

            # «en su punto óptimo»
            self.en("optimo")
            self.play(*[Flash(v, color=VERDE, flash_radius=0.3) for (_, _, v, _, _, _) in minis], run_time=self.dur(0.7))

            # «El causal solo puede hacerlo con los de eme mayor o igual que cero»
            self.en("causal")
            self.play(Create(marco_pos), FadeIn(l_pos), run_time=self.dur(0.7))

            # «los de eme negativo tienen que valer cero»
            self.en("negativo")
            self.play(Create(marco_neg), *[FadeIn(c0, scale=0.3) for (_, _, _, c0, _, _) in negs],
                      *[v.animate.set_opacity(0.3) for (_, _, v, _, _, _) in negs], run_time=self.dur(0.8))

            # «ese término se pierde»
            self.en("pierde")
            self.play(*[Create(s) for s in rojos], run_time=self.dur(0.6))
            self.sfx("error")
