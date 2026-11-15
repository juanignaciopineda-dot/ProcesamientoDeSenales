"""Escena 06 — Dos colas y una tijera: la secuencia K·0,6^m / K·0,157^|m|, su valor central y el corte de la cola de m < 0."""
from comun.escena import *


class DosColasYUnaTijera(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        mini = recuadro_mini()
        t = dos_colas(centro=(0.0, -1.4), paso=0.7, unidad=0.6, m_min=-5, m_max=6, indices=True)
        self.t = t
        der = [t.palito(t.m(m)) for m in range(1, 7)]
        izq = [t.palito(t.m(m)) for m in range(-5, 0)]
        cen = t.palito(t.m(0))
        l_mpos = formula(r"m\ge 0", escala=1.0, colores={0: SENAL}).move_to([2.6, -3.35, 0])
        l_06 = formula(r"K\cdot 0{,}6^{m}", escala=1.1, colores={0: SENAL}).move_to([3.6, 0.9, 0])
        l_157 = oculta(formula(r"K\cdot 0{,}157", r"^{|m|}", escala=1.1).move_to([-3.6, 0.9, 0]))
        l_157.set_color(RUIDO)
        suma = formula(r"2{,}56", r"\cdot", r"(1+0{,}094+0{,}094^2+\cdots)", escala=1.05,
                       colores={0: SENAL}).move_to([-1.2, 3.1, 0])
        llave = Brace(suma[2], DOWN, color=AMBAR, buff=0.1)
        l_razon = formula(r"0{,}6\cdot 0{,}157=0{,}094", escala=0.85, colores={0: AMBAR}).next_to(llave, DOWN, buff=0.12)
        l_razon.set_color(AMBAR)
        coc = formula(r"\frac{2{,}56}{0{,}906}", escala=1.1, colores={0: SENAL}).move_to([-1.2, 3.1, 0])
        k_val = formula("K", "=", r"2{,}826", escala=1.1, colores={0: AMBAR, 2: AMBAR}).move_to([-0.35, 0.95, 0])
        self.add(mini)
        with self.narrar("b1"):
            # «A la derecha»
            self.en("derecha")
            self.play(Create(t.base), FadeIn(t.ks), run_time=0.4)
            self.play(LaggedStart(*[AnimationGroup(GrowFromEdge(p[0], DOWN), FadeIn(p[1], scale=0.3)) for p in der],
                                  lag_ratio=0.15), run_time=self.dur(1.0))

            # «para eme mayor o igual que cero»
            self.en("mpos")
            self.play(FadeIn(l_mpos), run_time=self.dur(0.4))

            # «cae como cero coma seis elevado a eme»
            self.en("cae06")
            self.play(FadeIn(l_06, shift=DOWN * 0.2), run_time=self.dur(0.7))

            # «A la izquierda»
            self.en("izquierda")
            self.play(LaggedStart(*[AnimationGroup(GrowFromEdge(p[0], DOWN), FadeIn(p[1], scale=0.3)) for p in izq],
                                  lag_ratio=0.12), run_time=self.dur(0.9))

            # «cae como cero coma uno cinco siete»
            self.en("cae157")
            self.add(l_157)
            self.play(*revelar(l_157[0]), run_time=self.dur(0.7))

            # «al valor absoluto de eme»
            self.en("abs")
            self.play(*revelar(l_157[1]), run_time=self.dur(0.5))

            # «Y en el centro, el valor común»
            self.en("centro")
            self.play(GrowFromEdge(cen[0], DOWN), FadeIn(cen[1], scale=0.3), run_time=self.dur(0.6))
            self.resaltar(cen[1], color=AMBAR, escala=2.0, run_time=0.5)

            # «dos coma cinco seis por la suma de una progresión geométrica»
            self.en("suma")
            self.play(FadeIn(suma, shift=DOWN * 0.2), run_time=self.dur(1.2))

            # «de razón cero coma cero nueve cuatro»
            self.en("razon")
            self.play(GrowFromCenter(llave), FadeIn(l_razon), run_time=self.dur(0.7))

            # «dos coma cinco seis entre cero coma nueve cero seis»
            self.en("cociente")
            self.play(FadeOut(llave), FadeOut(l_razon), ReplacementTransform(suma, coc), run_time=self.dur(0.9))

            # «dos coma ocho dos seis»
            self.en("k2826")
            self.pop(k_val)
        self.coc = coc
        self.partes = (der, izq, cen, l_mpos, l_06, l_157, k_val, mini)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        t = self.t
        der, izq, cen, l_mpos, l_06, l_157, k_val, mini = self.partes
        tj = tijeras().scale(0.9).move_to([-1.0, 2.0, 0])
        tj.permitir_encima = True
        nuevo_06 = formula(r"2{,}826", r"\cdot", r"0{,}6^{m}", escala=1.1, colores={0: AMBAR, 2: SENAL}).move_to([-1.2, 0.95, 0])
        a_z = flecha([1.0, 0.1, 0], [2.0, 0.1, 0], AMBAR)
        num_z = MathTex(r"2{,}826", color=AMBAR).scale(1.0)
        den_z = formula("1-0{,}6", r"\,z^{-1}", escala=1.0)
        fr_z = oculta(fraccion(num_z, den_z))
        fr_z.move_to([4.6, 0.1, 0])
        marco = SurroundingRectangle(fr_z, color=AMBAR, buff=0.2, corner_radius=0.1, stroke_width=3)
        movibles = VGroup(*[m for m in (t.base, t.ks)], *der, cen)
        with self.narrar("b2"):
            # «Segundo paso»
            self.en("paso2")
            self.resaltar(mini.c2, color=AMBAR, run_time=0.6)

            # «La cola de la izquierda, la de eme negativo»
            self.en("colaizq")
            self.play(*[p.animate(rate_func=there_and_back).set_color(ERROR) for g in izq for p in g],
                      run_time=self.dur(1.2))

            # «se corta»
            self.en("corta")
            self.play(FadeIn(tj, scale=0.6), run_time=0.3)
            self.play(tj.animate.move_to([-0.95, -1.3, 0]), run_time=0.5)
            self.sfx("whoosh")
            self.play(*[FadeOut(g, shift=DOWN * 0.6) for g in izq], FadeOut(l_157), run_time=self.dur(0.7))
            self.play(FadeOut(tj), run_time=0.3)

            # «Queda la de la derecha»
            self.en("queda")
            self.play(movibles.animate.shift(LEFT * 2.6), l_mpos.animate.shift(LEFT * 2.6),
                      FadeOut(k_val), FadeOut(l_06), FadeOut(self.coc), run_time=self.dur(0.8))

            # «dos coma ocho dos seis por cero coma seis elevado a eme»
            self.en("kpor06")
            nuevo_06.move_to([-1.5, 1.0, 0])
            self.play(FadeIn(nuevo_06, shift=DOWN * 0.2), run_time=self.dur(0.8))

            # «que en zeta es»
            self.en("enz")
            self.play(GrowArrow(a_z), run_time=self.dur(0.5))

            # «dos coma ocho dos seis entre uno menos cero coma seis»
            self.en("fraccion")
            self.add(fr_z)
            self.play(*revelar(fr_z.num, fr_z.barra), *revelar(den_z[0]), run_time=self.dur(0.9))

            # «zeta a la menos uno.»
            self.en("finalz")
            self.play(*revelar(den_z[1]), Create(marco), run_time=self.dur(0.6))
