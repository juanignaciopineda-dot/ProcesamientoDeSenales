"""Escena 05 — Primer paso: se recuerdan los tres pasos de la fórmula causal y se blanquea la cruzada del sensor."""
from comun.escena import *


class PrimerPaso(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        colores = [CIAN, AMBAR, VERDE]
        marcos, numeros = [], []
        for i, c in enumerate(colores):
            r = RoundedRectangle(corner_radius=0.18, width=4.1, height=3.6, color=c, fill_color=c,
                                 fill_opacity=0.08, stroke_width=3.5).move_to([-4.5 + 4.5 * i, 0.4, 0])
            n = Text(str(i + 1), color=c, weight=BOLD).scale(0.8).move_to(r.get_corner(UL) + DR * 0.45)
            marcos.append(r), numeros.append(n)
        # contenido de cada casilla
        t1 = Text("blanquear", color=CIAN, weight=BOLD).scale(0.7).move_to([-4.5, 1.7, 0])
        x_ = MathTex("x", color=MEDIDA).scale(0.9)
        b_ = caja("1/F", CIAN, ancho=1.1, alto=0.7, scale=0.5)
        e_ = MathTex(r"\varepsilon", color=TXT).scale(0.9)
        cad1 = VGroup(x_, flecha([0, 0, 0], [0.6, 0, 0]), b_, flecha([0, 0, 0], [0.6, 0, 0]), e_).arrange(RIGHT, buff=0.12)
        cad1.move_to([-4.5, 0.5, 0])
        div = formula(r"\div F", escala=1.5, colores={0: CIAN}).move_to([-4.5, -0.8, 0])
        t2 = Text("parte causal", color=AMBAR, weight=BOLD).scale(0.7).move_to([0, 1.7, 0])
        tj = tijeras().scale(0.7).move_to([0, 0.6, 0])
        sec = dos_colas(centro=(0.0, -0.9), paso=0.26, unidad=0.2, m_min=-5, m_max=6, indices=False)
        # las posiciones m ≥ 0 resaltadas
        t3 = Text("deshacer", color=VERDE, weight=BOLD).scale(0.7).move_to([4.5, 1.7, 0])
        por = formula(r"\times\ 1/F", escala=1.5, colores={0: VERDE}).move_to([4.5, 0.2, 0])
        mini = recuadro_mini()
        term = termometro(alto=1.1).move_to([-6.4, 3.1, 0])
        grande = VGroup(*marcos, *numeros)
        with self.narrar("b1"):
            # «los tres pasos»
            self.en("tres")
            self.play(LaggedStart(*[FadeIn(VGroup(m, n)) for m, n in zip(marcos, numeros)], lag_ratio=0.25),
                      run_time=self.dur(1.2))

            # «Primero, blanquear»
            self.en("uno")
            self.play(FadeIn(t1), FadeIn(cad1, shift=RIGHT * 0.2), run_time=self.dur(0.9))

            # «dividiendo entre el factor de fase mínima»
            self.en("divide")
            self.pop(div)

            # «Segundo, quedarnos con la parte causal»
            self.en("dos")
            self.play(FadeIn(t2), FadeIn(tj, scale=0.6), run_time=self.dur(0.7))

            # «las posiciones cero y positivas»
            self.en("cero")
            self.play(FadeIn(sec.base), *[FadeIn(sec.palito(i)) for i in range(len(sec.valores))], run_time=0.5)
            self.play(*[sec.palito(sec.m(m)).animate.set_opacity(0.25) for m in range(-5, 0)],
                      Flash(sec.puntos[sec.m(0)], color=AMBAR, flash_radius=0.3), run_time=0.6)

            # «Tercero, deshacer el blanqueo»
            self.en("tres3")
            self.play(FadeIn(t3), FadeIn(por, shift=UP * 0.2), run_time=self.dur(0.7))

            # «Hagámoslos con el sensor»
            self.en("sensor")
            contenido = VGroup(t1, cad1, div, t2, tj, sec, t3, por)
            self.play(FadeOut(contenido), run_time=0.3)
            self.play(ReplacementTransform(grande, mini), FadeIn(term), run_time=self.dur(0.8))
        self.mini = mini

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        mini = self.mini
        r1 = oculta(formula("S_{yx}", "=", "S_{yy}", "=", escala=1.1, colores={0: AMBAR, 2: SENAL}).move_to([-4.6, 2.2, 0]))
        den1 = formula(r"(1-0{,}6\,z^{-1})", r"(1-0{,}6\,z)", escala=1.0)
        f1 = oculta(fraccion(MathTex(r"2{,}56", color=SENAL).scale(1.0), den1))
        f1.move_to([-0.6, 2.2, 0])
        L = Lienzo(ancho=2.2, alto=0.9, t_rango=(0, 1), v_max=1.0, centro=(4.4, 2.1))
        tr = ruido_t(L, semilla=5, amp=0.35, color=RUIDO)
        l_r = etiqueta("ruido", RUIDO, 0.45).move_to([4.4, 3.0, 0])
        d2a = formula(r"\div", r"F(z^{-1})", "=", escala=1.0, colores={1: AMBAR}).move_to([-4.0, -0.1, 0])
        f2 = fraccion(formula(r"1-0{,}157\,z", escala=1.0, colores={0: RUIDO}), formula(r"1-0{,}6\,z", escala=1.0))
        f2.move_to([-1.3, -0.1, 0])
        res = oculta(formula("=", escala=1.1).move_to([-5.3, -2.2, 0]))
        den3 = formula(r"(1-0{,}6\,z^{-1})", r"(1-0{,}157\,z)", escala=1.0)
        f3 = fraccion(MathTex(r"2{,}56", color=SENAL).scale(1.0), den3).move_to([-2.2, -2.2, 0])
        oculta(f3.num), oculta(f3.den), f3.barra.set_stroke(opacity=0)
        t1 = tachar(den1[1]).set_stroke(width=5)
        t2 = tachar(f2.den).set_stroke(width=5)
        llave1 = Brace(den3[0], DOWN, color=AMBAR, buff=0.1)
        llave2 = Brace(den3[1], DOWN, color=AMBAR, buff=0.1)
        sec = dos_colas(centro=(0.0, -1.2), paso=0.7, unidad=0.6, m_min=-5, m_max=6, indices=False)
        with self.narrar("b2"):
            # «Primer paso»
            self.en("paso1")
            self.resaltar(mini.c1, color=CIAN, run_time=0.6)

            # «la cruzada entre i griega y lo medido»
            self.en("cruzada")
            self.add(r1)
            self.play(*revelar(r1[0], r1[1]), run_time=self.dur(0.6))

            # «es la densidad de la temperatura»
            self.en("igual")
            self.add(f1)
            self.play(*revelar(r1[2], r1[3]), run_time=0.4)
            self.play(*revelar(f1), run_time=self.dur(1.0))

            # «porque el ruido no aporta»
            self.en("noaporta")
            self.play(Create(tr), FadeIn(l_r), run_time=0.6)
            self.play(FadeOut(tr), FadeOut(l_r), run_time=0.5)

            # «Dividida entre F de zeta a la menos uno»
            self.en("divide2")
            self.play(FadeIn(d2a), Create(f2.barra), FadeIn(f2.num), FadeIn(f2.den), run_time=self.dur(1.1))

            # «sale dos coma cinco seis»
            self.en("sale256")
            self.add(f3, res)
            self.play(*revelar(res), *revelar(f3.num), f3.barra.animate.set_stroke(opacity=1), run_time=self.dur(0.8))

            # «entre uno menos cero coma seis zeta a la menos uno»
            self.en("fr1")
            self.play(*revelar(f3.den[0]), run_time=self.dur(0.7))

            # «por uno menos cero coma uno cinco siete zeta»
            self.en("fr2")
            self.play(*revelar(f3.den[1]), Create(t1), Create(t2), run_time=self.dur(0.9))

            # «un producto de dos fracciones»
            self.en("producto")
            self.play(GrowFromCenter(llave1), GrowFromCenter(llave2), run_time=self.dur(0.6))

            # «una secuencia con dos colas»
            self.en("colas")
            fila3 = VGroup(res, f3, llave1, llave2)
            self.play(FadeOut(r1), FadeOut(f1), FadeOut(d2a), FadeOut(f2), FadeOut(t1), FadeOut(t2),
                      fila3.animate.move_to([-0.8, 2.3, 0]), run_time=self.dur(0.8))
            self.play(Create(sec.base), LaggedStart(*[AnimationGroup(GrowFromEdge(sec.tallos[i], DOWN),
                                                                     FadeIn(sec.puntos[i], scale=0.3))
                                                      for i in range(len(sec.valores))], lag_ratio=0.08),
                      run_time=self.dur(1.2))
