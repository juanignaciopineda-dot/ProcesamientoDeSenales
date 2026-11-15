"""Escena 07 — Deshacer el blanqueo: H(z) = 0,7386 / (1 − 0,157 z⁻¹) y sus coeficientes, que son los del filtro finito."""
from comun.escena import *


class DeshacerElBlanqueo(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        mini = recuadro_mini()
        Hz = oculta(formula("H(z)", "=", escala=1.05, colores={0: AMBAR}))
        f_a = oculta(fraccion(MathTex("1", color=VERDE).scale(1.0), MathTex(r"3{,}826", color=VERDE).scale(1.0)))
        f_b = oculta(fraccion(formula(r"1-0{,}6\,z^{-1}", escala=1.0), formula(r"1-0{,}157\,z^{-1}", escala=1.0, colores={0: RUIDO})))
        f_c = oculta(fraccion(MathTex(r"2{,}826", color=AMBAR).scale(1.0), formula(r"1-0{,}6\,z^{-1}", escala=1.0)))
        fila = VGroup(Hz, f_a, f_b, f_c).arrange(RIGHT, buff=0.35).move_to([-0.4, 1.7, 0])
        t_arriba = SurroundingRectangle(f_b.num, color=ERROR, buff=0.08, stroke_width=3)
        t_abajo = SurroundingRectangle(f_c.den, color=ERROR, buff=0.08, stroke_width=3)
        x1 = tachar(f_b.num).set_stroke(width=5)
        x2 = tachar(f_c.den).set_stroke(width=5)
        res_H = formula("H(z)", "=", escala=1.15, colores={0: AMBAR}).move_to([-5.3, -1.5, 0])
        num_r = MathTex(r"0{,}7386", color=AMBAR).scale(1.1)
        den_r = formula("1-0{,}157", r"\,z^{-1}", escala=1.1, colores={0: RUIDO})
        fr_r = fraccion(num_r, den_r).move_to([-2.5, -1.5, 0])
        oculta(num_r), oculta(den_r[0]), oculta(den_r[1]), fr_r.barra.set_stroke(opacity=0)
        marco = SurroundingRectangle(fr_r, color=AMBAR, buff=0.12, corner_radius=0.1, stroke_width=3)
        pz = PlanoZ(centro=(4.2, -1.6), radio=1.3)
        polo = marca_x(pz.p(0.157), AMBAR)
        l_polo = etiqueta("un solo polo", AMBAR, 0.5).move_to([4.2, -3.5, 0])
        self.add(mini)
        with self.narrar("b1"):
            # «Tercer paso»
            self.en("paso3")
            self.resaltar(mini.c3, color=VERDE, run_time=0.6)

            # «multiplicando por uno entre tres coma ocho dos seis F»
            self.en("multiplica")
            self.add(fila)
            self.play(*revelar(Hz), run_time=0.4)
            self.play(*revelar(f_a), run_time=0.6)
            self.play(*revelar(f_b), run_time=self.dur(0.8))
            self.play(*revelar(f_c), run_time=self.dur(0.8))

            # «Uno menos cero coma seis zeta a la menos uno, arriba»
            self.en("arriba")
            self.play(Create(t_arriba), run_time=self.dur(0.5))

            # «se cancela con el mismo factor del segundo paso»
            self.en("cancela")
            self.play(Create(t_abajo), run_time=0.4)
            self.play(Create(x1), Create(x2), run_time=self.dur(0.6))
            self.sfx("tick")

            # «Queda cero coma siete tres ocho seis»
            self.en("q07386")
            self.add(fr_r, res_H)
            self.play(FadeIn(res_H), *revelar(num_r), fr_r.barra.animate.set_stroke(opacity=1), run_time=self.dur(0.8))

            # «entre uno menos cero coma uno cinco siete»
            self.en("deno157")
            self.play(*revelar(den_r[0]), run_time=self.dur(0.7))

            # «zeta a la menos uno.»
            self.en("zinv")
            self.play(*revelar(den_r[1]), Create(marco), run_time=self.dur(0.5))

            # «Un filtro de un solo polo»
            self.en("unpolo")
            self.play(Create(pz), FadeIn(l_polo), run_time=self.dur(0.6))
            self.play(Create(polo), run_time=0.4)
        self.mini = mini

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        mini = self.mini
        self.corte(mini)
        unidad = 2.4
        t = Tallos(list(H_CAUSAL_5), centro=(-2.2, -1.6), paso=1.5, unidad=unidad, color=ESTIMACION)
        puntos = Text("…", color=INK).scale(0.9).move_to([1.2, -1.45, 0])
        l_h = MathTex("h[n]", color=ESTIMACION).scale(0.8).move_to([-5.9, -0.2, 0])
        vals = VGroup(*[etiqueta(s, TXT, 0.5).move_to([t.x(i), -1.6 - 0.35, 0])
                        for i, s in enumerate(["0,7386", "0,1158", "0,0182", "0,0028"])])
        fir = Tallos(list(H_CAUSAL_5), centro=(-2.2, 1.4), paso=1.5, unidad=unidad, color=VERDE)
        l_fir = etiqueta("filtro finito", VERDE, 0.5).move_to([-5.9, 2.9, 0])
        l_fir2 = etiqueta("(segundo episodio)", VERDE, 0.4).move_to([-5.9, 2.45, 0])
        saltos = VGroup(*[ArcBetweenPoints(t.pos(i) + UP * 0.3 + RIGHT * 0.2, t.pos(i + 1) + UP * 0.3 + LEFT * 0.2,
                                           angle=-PI / 2.5, color=AMBAR, stroke_width=3).add_tip(tip_length=0.15)
                          for i in range(0, 2)])
        l_veces = VGroup(*[formula(r"\times 0{,}157", escala=0.7, colores={0: AMBAR}).move_to(a.get_center() + UP * 0.45)
                           for a in saltos])
        l_pq = etiqueta("¿por qué?", AMBAR, 0.6, BOLD).move_to([-1.0, 2.3, 0])
        pz = PlanoZ(centro=(5.4, -0.5), radio=1.0)
        cero = marca_o(pz.p(0.157), AMBAR)
        l_cero = formula(r"0{,}157", escala=0.8, colores={0: AMBAR}).next_to(pz, DOWN, buff=0.2)
        sello = caja("filtro de Wiener causal", AMBAR, ancho=4.4, alto=0.8, scale=0.5).move_to([-0.8, 3.2, 0])
        chips = VGroup(*[caja(f"L = {n}", VERDE, ancho=1.3, alto=0.55, scale=0.4) for n in (1, 2, 3)]).arrange(RIGHT, buff=0.2)
        chips.move_to([-4.3, -3.6, 0])
        flecha_inf = MathTex(r"\to\ \infty", color=AMBAR).scale(0.8).next_to(chips, RIGHT, buff=0.25)
        sello2 = caja("Wiener causal = límite del FIR", AMBAR, ancho=5.2, alto=0.8, scale=0.5).move_to([2.6, -3.6, 0])
        with self.narrar("b2"):
            # «Su respuesta al impulso»
            self.en("impulso")
            self.play(Create(t.base), FadeIn(l_h), run_time=self.dur(0.5))

            # «cero coma siete tres ocho seis»
            self.en("b1")
            self.play(GrowFromEdge(t.tallos[0], DOWN), FadeIn(t.puntos[0], scale=0.3), FadeIn(vals[0]), run_time=self.dur(0.6))

            # «cero coma uno uno cinco ocho»
            self.en("b2")
            self.play(GrowFromEdge(t.tallos[1], DOWN), FadeIn(t.puntos[1], scale=0.3), FadeIn(vals[1]), run_time=self.dur(0.6))

            # «cero coma cero uno ocho dos»
            self.en("b3")
            self.play(GrowFromEdge(t.tallos[2], DOWN), FadeIn(t.puntos[2], scale=0.3), FadeIn(vals[2]), run_time=self.dur(0.6))

            # «cero coma cero cero dos ocho»
            self.en("b4")
            self.play(GrowFromEdge(t.tallos[3], DOWN), FadeIn(t.puntos[3], scale=0.3), FadeIn(vals[3]), FadeIn(puntos),
                      run_time=self.dur(0.6))

            # «¡Son los coeficientes»
            self.en("coinciden")
            self.play(Create(fir), FadeIn(l_fir), FadeIn(l_fir2), run_time=self.dur(1.0))

            # «del filtro finito del segundo episodio»
            self.en("finito")
            self.play(fir.animate.shift(DOWN * 3.0), FadeOut(l_fir2), l_fir.animate.move_to([-5.9, 0.5, 0]),
                      run_time=self.dur(1.2))
            self.sfx("exito")

            # «cero coma uno cinco siete veces el anterior»
            self.en("veces")
            self.play(*[Create(a) for a in saltos], *[FadeIn(l) for l in l_veces], run_time=self.dur(1.0))

            # «ahora sabemos por qué»
            self.en("sabemos")
            self.pop(l_pq)

            # «es el cero de la factorización»
            self.en("cerofact")
            self.play(FadeOut(l_pq), Create(pz), run_time=0.4)
            self.play(Create(cero), FadeIn(l_cero), run_time=self.dur(0.5))
            self.resaltar(cero, color=AMBAR, escala=1.6, run_time=0.5)

            # «El filtro de Wiener causal»
            self.en("wiener")
            self.pop(sello)

            # «exactamente el límite del filtro finito»
            self.en("limite")
            self.play(FadeIn(chips, shift=UP * 0.2), FadeIn(flecha_inf), run_time=self.dur(0.6))
            self.play(FadeIn(sello2, scale=0.8), run_time=self.dur(0.6))
            self.sfx("exito")
