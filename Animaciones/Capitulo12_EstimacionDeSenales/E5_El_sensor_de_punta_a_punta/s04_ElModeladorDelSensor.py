"""Escena 04 — El modelador del sensor: ecuación de segundo grado, raíz de dentro, F(z) y comprobación de potencia."""
from comun.escena import *


class ElModeladorDelSensor(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        e1 = formula(r"\kappa\rho", "=", r"0{,}6", escala=0.95, colores={0: VERDE, 2: VERDE}).move_to([-3.6, 3.1, 0])
        e2 = formula(r"\kappa(1+\rho^2)", "=", r"3{,}92", escala=0.95, colores={0: CIAN, 2: CIAN}).move_to([-3.6, 2.2, 0])
        num_d = formula(r"\kappa", r"(1+\rho^2)", escala=0.9, colores={0: AMBAR})
        den_d = formula(r"\kappa", r"\rho", escala=0.9, colores={0: AMBAR})
        fr_d = fraccion(num_d, den_d)
        igual1 = MathTex("=", color=TXT).scale(0.9)
        fr_n = fraccion(MathTex(r"3{,}92", color=CIAN).scale(0.9), MathTex(r"0{,}6", color=VERDE).scale(0.9))
        fila_d = VGroup(fr_d, igual1, fr_n).arrange(RIGHT, buff=0.3).move_to([-3.6, 0.5, 0])
        tk1 = tachar(num_d[0]).set_stroke(width=5)
        tk2 = tachar(den_d[0]).set_stroke(width=5)
        fr_r = fraccion(MathTex(r"1+\rho^2", color=TXT).scale(0.9), MathTex(r"\rho", color=TXT).scale(0.9))
        r_seis = oculta(MathTex(r"=6{,}53", color=AMBAR).scale(0.9))
        fila_r = VGroup(fr_r, r_seis).arrange(RIGHT, buff=0.25).move_to([-4.3, -1.2, 0])
        cuad = formula(r"\rho^2", "-", r"6{,}53\,\rho", "+", "1", "=", "0", escala=0.95,
                       colores={0: AMBAR, 2: AMBAR, 4: AMBAR}).move_to([-3.6, -2.7, 0])
        l_seg = etiqueta("segundo grado", AMBAR, 0.5).next_to(cuad, DOWN, buff=0.2)
        # el plano z con la recta real
        pl = PlanoZ(centro=(0.5, -0.5), radio=0.95, ver_unos=True, ext_der=6.0)
        eje_real = Line(pl.c + LEFT * 1.4, pl.c + RIGHT * 6.0, color=INK, stroke_width=2)
        l_dossol = etiqueta("dos soluciones", INK, 0.5).move_to([4.2, 0.9, 0])
        d_6377 = Dot(pl.p(6.377), radius=0.11, color=AMBAR)
        t_6377 = etiqueta("6,377", AMBAR, 0.5).next_to(d_6377, DOWN, buff=0.15)
        d_0157 = Dot(pl.p(0.157), radius=0.11, color=AMBAR)
        t_0157 = etiqueta("0,157", AMBAR, 0.5).next_to(d_0157, DOWN, buff=0.2).shift(RIGHT * 0.25)
        arco = ArcBetweenPoints(pl.p(0.157) + UP * 0.12, pl.p(6.377) + UP * 0.12, angle=-PI / 2.5, color=INK, stroke_width=3)
        t_prod = formula(r"0{,}157", r"\cdot", r"6{,}377", "=", "1", escala=0.8).move_to([3.6, 1.55, 0])
        t_prod.set_color(AMBAR)
        l_fm = etiqueta("fase mínima", VERDE, 0.5).move_to([1.0, -2.1, 0])
        k_val = formula(r"\kappa", "=", r"3{,}826", escala=1.0, colores={0: AMBAR, 2: AMBAR}).move_to([3.9, -2.9, 0])
        with self.narrar("b1"):
            # «Dividimos una entre la otra»
            self.en("divide")
            self.add(e1, e2)
            self.play(Create(fr_d.barra), FadeIn(num_d), FadeIn(den_d), FadeIn(igual1), Create(fr_n.barra),
                      FadeIn(fr_n.num), FadeIn(fr_n.den), run_time=self.dur(1.0))

            # «desaparece kappa»
            self.en("desaparece")
            self.play(Create(tk1), Create(tk2), run_time=self.dur(0.5))
            self.sfx("tick")

            # «uno más ro al cuadrado, entre ro»
            self.en("razon")
            self.add(r_seis)
            self.play(FadeIn(fr_r.num, shift=DOWN * 0.2), Create(fr_r.barra), FadeIn(fr_r.den, shift=UP * 0.2),
                      run_time=self.dur(0.7))

            # «seis coma cinco tres»
            self.en("seis53")
            self.play(*revelar(r_seis), run_time=self.dur(0.6))

            # «Una ecuación de segundo grado»
            self.en("segundo")
            self.play(FadeIn(cuad, shift=UP * 0.2), FadeIn(l_seg), run_time=self.dur(0.8))

            # «Tiene dos soluciones»
            self.en("dossol")
            self.play(Create(eje_real), FadeIn(l_dossol), run_time=self.dur(0.7))

            # «seis coma tres siete siete»
            self.en("r6377")
            self.play(FadeIn(d_6377, scale=0.3), FadeIn(t_6377), run_time=self.dur(0.5))
            self.sfx("pop")

            # «cero coma uno cinco siete»
            self.en("r0157")
            self.play(FadeIn(d_0157, scale=0.3), FadeIn(t_0157), run_time=self.dur(0.5))
            self.sfx("pop")

            # «Su producto es uno»
            self.en("producto")
            self.play(Create(arco), FadeIn(t_prod), FadeOut(l_dossol), run_time=self.dur(0.8))

            # «una dentro y otra fuera del círculo»
            self.en("circulo")
            self.play(Create(pl.circ), Create(pl.v), run_time=self.dur(1.0))

            # «Nos quedamos con la de dentro»
            self.en("dentro")
            self.play(d_6377.animate.set_opacity(0.25), t_6377.animate.set_opacity(0.25),
                      d_0157.animate.set_color(VERDE), t_0157.animate.set_color(VERDE), run_time=self.dur(0.6))

            # «la de fase mínima»
            self.en("faseminima")
            self.play(FadeIn(l_fm), run_time=self.dur(0.4))

            # «Kappa vale tres coma ocho dos seis»
            self.en("k3826")
            self.pop(k_val)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        F_ = formula("F(z)", "=", escala=1.1, colores={0: AMBAR}).move_to([-5.4, 0.2, 0])
        num_f = formula("1", r"-0{,}157\,z^{-1}", escala=0.95, colores={1: RUIDO})
        den_f = formula("1", r"-0{,}6\,z^{-1}", escala=0.95, colores={1: SENAL})
        fr_f = fraccion(num_f, den_f).move_to([-3.1, 0.2, 0])
        pz = PlanoZ(centro=(3.4, 0.2), radio=1.7)
        polo = marca_x(pz.p(0.6), AMBAR)
        cero = marca_o(pz.p(0.157), AMBAR)
        l_mem = etiqueta("memoria", SENAL, 0.5).move_to([5.6, -2.3, 0])
        r_mem = Line(pz.p(0.6) + DOWN * 0.25, l_mem.get_top() + UP * 0.05, color=SENAL, stroke_width=2.5)
        l_rui = etiqueta("ruido", RUIDO, 0.5).move_to([1.6, 2.7, 0])
        r_rui = Line(pz.p(0.157) + UP * 0.2, l_rui.get_bottom() + DOWN * 0.05, color=RUIDO, stroke_width=2.5)
        sig = formula(r"\sigma^2", "=", r"3{,}826", escala=1.0, colores={0: AMBAR, 2: AMBAR}).move_to([-3.1, -2.0, 0])
        with self.narrar("b2"):
            # «El filtro de fase mínima»
            self.en("filtro")
            self.corte()
            self.play(FadeIn(F_), Create(pz), run_time=self.dur(0.8))

            # «uno menos cero coma uno cinco siete zeta a la menos uno»
            self.en("numf")
            self.play(FadeIn(num_f), Create(fr_f.barra), run_time=self.dur(0.8))

            # «entre uno menos cero coma seis zeta a la menos uno»
            self.en("denf")
            self.play(FadeIn(den_f), run_time=self.dur(0.8))

            # «Tiene un polo en cero coma seis»
            self.en("polo")
            self.play(Create(polo), run_time=self.dur(0.5))
            self.sfx("pop")

            # «la memoria de la temperatura»
            self.en("memoria")
            self.play(FadeIn(l_mem), Create(r_mem), run_time=self.dur(0.4))

            # «un cero en cero coma uno cinco siete»
            self.en("cero")
            self.play(Create(cero), run_time=self.dur(0.5))
            self.sfx("pop")

            # «que pone el ruido»
            self.en("poneruido")
            self.play(FadeIn(l_rui), Create(r_rui), run_time=self.dur(0.4))

            # «Los dos, dentro»
            self.en("dentro2")
            self.play(pz.circ.animate.set_stroke(VERDE, width=6), run_time=self.dur(0.6))

            # «Y sigma cuadrado vale tres coma ocho dos seis»
            self.en("sigma")
            self.pop(sig)

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        h_f = [1.0] + [0.443 * 0.6 ** i for i in range(6)]
        barras = Tallos(h_f, centro=(-3.3, -0.9), paso=0.72, unidad=1.5, color=SENAL)
        t_vals = VGroup(*[etiqueta(s, TXT, 0.42).next_to(barras.pos(i), UP, buff=0.1)
                          for i, s in enumerate(["1", "0,443", "0,266"])])
        bl = BloqueLTI("F", centro=(-3.3, 2.9), ancho=1.2, alto=0.8, color=AMBAR, largo=1.3, escala=0.8)
        l_d = MathTex(r"\delta", color=TXT).scale(0.8).next_to(bl.p_ent(), LEFT, buff=0.15)
        l_h = MathTex("h", color=SENAL).scale(0.8).next_to(bl.p_sal(), RIGHT, buff=0.15)
        cuadr = Tallos([v * v for v in h_f], centro=(3.4, -0.9), paso=0.72, unidad=1.5, color=ERROR)
        a_cuad = flecha([-0.2, -0.3, 0], [1.2, -0.3, 0], INK)
        l_cuad = MathTex(r"(\ )^2", color=INK).scale(0.7).next_to(a_cuad, UP, buff=0.1)
        sigma = formula(r"\sum", "=", r"1{,}307", escala=0.9, colores={2: AMBAR}).move_to([3.4, 1.0, 0])
        cuenta = oculta(formula(r"3{,}826", r"\cdot", r"1{,}307", "=", "5", escala=0.95,
                                colores={0: AMBAR, 4: VERDE}).move_to([3.4, 2.3, 0]))
        suma_ = formula("4", "+", "1", escala=0.95, colores={0: SENAL, 2: RUIDO}).move_to([3.4, -3.1, 0])
        ok = tilde(VERDE, 0.5).next_to(suma_, RIGHT, buff=0.3)
        mon = moneda("").scale(0.45)
        cad = BloqueLTI("F", centro=(-3.3, -3.2), ancho=1.1, alto=0.7, color=AMBAR, largo=1.0, escala=0.7)
        mon.next_to(cad.p_ent(), LEFT, buff=0.1)
        l_x = MathTex("x", color=MEDIDA).scale(0.8).next_to(cad.p_sal(), RIGHT, buff=0.15)
        tj = tijeras().scale(0.6).move_to([0.1, -3.2, 0])
        with self.narrar("b3"):
            # «Comprobémoslo con la potencia»
            self.en("compro")
            self.corte()
            self.play(Create(barras.base), run_time=self.dur(0.5))

            # «La respuesta de F al impulso»
            self.en("respf")
            self.play(Create(bl), FadeIn(l_d), FadeIn(l_h), run_time=self.dur(0.8))

            # «uno, cero coma cuatro cuatro tres, cero coma dos seis seis, y así»
            self.en("impulso")
            for i in range(3):
                self.play(GrowFromEdge(barras.tallos[i], DOWN), FadeIn(barras.puntos[i], scale=0.3),
                          FadeIn(t_vals[i]), run_time=self.dur(0.5))

            # «y así»
            self.en("yasi")
            self.play(LaggedStart(*[AnimationGroup(GrowFromEdge(barras.tallos[i], DOWN),
                                                   FadeIn(barras.puntos[i], scale=0.3)) for i in range(3, 7)],
                                  lag_ratio=0.3), run_time=self.dur(0.9))

            # «la suma de sus cuadrados»
            self.en("cuadrados")
            self.play(GrowArrow(a_cuad), FadeIn(l_cuad), Create(cuadr.base), run_time=0.4)
            self.play(LaggedStart(*[AnimationGroup(GrowFromEdge(cuadr.tallos[i], DOWN),
                                                   FadeIn(cuadr.puntos[i], scale=0.3)) for i in range(7)],
                                  lag_ratio=0.12), run_time=self.dur(1.0))

            # «uno coma tres cero siete»
            self.en("s1307")
            self.pop(sigma)

            # «Multiplicada por tres coma ocho dos seis»
            self.en("multiplica2")
            self.add(cuenta)
            self.play(*revelar(cuenta[0], cuenta[1], cuenta[2]), run_time=self.dur(0.8))

            # «da cinco»
            self.en("cinco")
            self.play(*revelar(cuenta[3], cuenta[4]), run_time=self.dur(0.5))
            self.sfx("exito")

            # «cuatro más uno»
            self.en("cuatromasuno")
            self.play(FadeIn(suma_), run_time=self.dur(0.5))
            self.play(Create(ok), run_time=0.4)

            # «una moneda pasada por este filtro»
            self.en("moneda")
            self.play(Create(cad), FadeIn(mon), FadeIn(l_x), run_time=self.dur(0.9))

            # «Ahora falta la parte causal»
            self.en("falta")
            self.play(FadeIn(tj, scale=0.5), run_time=self.dur(0.5))
