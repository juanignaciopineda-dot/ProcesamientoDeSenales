"""Escena 12 — El permiso de la ergodicidad: la densidad espectral es un promedio sobre el ensemble y Welch promedia en el tiempo."""
from comun.escena import *


class ElPermisoDeLaErgodicidad(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        losa_i = Rectangle(width=4.8, height=0.2, color=INK, stroke_width=2).set_fill(INK, 0.5).move_to([-4.4, -2.5, 0])
        losa_d = Rectangle(width=4.8, height=0.2, color=INK, stroke_width=2).set_fill(INK, 0.5).move_to([4.4, -2.5, 0])
        t_ens = self.palabra("ensemble", AZUL, 0.9).move_to([-4.4, 3.5, 0])
        t_tie = self.palabra("tiempo", AMBAR, 0.9).move_to([4.4, 3.5, 0])
        abismo = DashedVMobject(CurvedArrow([-1.7, -2.3, 0], [1.7, -2.3, 0], angle=-1.1, color=INK, stroke_width=4))
        l_dens = etiqueta("densidad espectral", AZUL, 0.55).move_to([-4.4, 2.65, 0])
        xs = np.linspace(-1.0, 1.0, 60)
        mini = traza(-4.4 + xs, 2.0 + 0.45 * np.exp(-(xs / 0.5) ** 2), AZUL, 4.0)
        Li = Lienzo(ancho=4.8, alto=2.0, t_rango=(0, 1), v_max=1.3, centro=(-4.4, 0.0))
        pila1 = pila_de_curvas(Li, 10, semilla=3, a=0.9, color=SENAL, opacidad=0.5, ancho=2.0, escala=0.45)
        pila2 = pila_de_curvas(Li, 12, semilla=4, a=0.9, color=SENAL, opacidad=0.5, ancho=2.0, escala=0.45)
        corte_v = Li.vertical(0.5, AMBAR, 3.0)
        lupa_ = lupa().scale(1.2).move_to([0.0, 0.8, 0])
        Ld = Lienzo(ancho=4.8, alto=1.0, t_rango=(0, 1), v_max=1.0, centro=(4.4, 0.0))
        rd = Ld.curva(np.linspace(0, 1, 240), 0.9 * serie(31, 240, 0.9), SENAL, 2.8)
        seps = VGroup(*[DashedLine(Ld.p(k / 4, -1.0), Ld.p(k / 4, 1.0), color=AMBAR, stroke_width=2.5) for k in (1, 2, 3)])
        f_t = Arrow([2.1, 1.0, 0], [6.7, 1.0, 0], color=AMBAR, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.1)
        sel = sello("¿permiso?", AMBAR).scale(1.3).move_to([0, -1.0, 0])

        with self.narrar("b1"):
            # «un salto que conviene mirar de frente»
            self.en("salto")
            self.play(FadeIn(losa_i), FadeIn(losa_d), Create(abismo), run_time=self.dur(1.2))
            self.pop(t_ens, t_tie)

            # «La densidad espectral»
            self.en("densidad")
            self.play(FadeIn(l_dens), Create(mini), run_time=self.dur(0.9))

            # «un promedio sobre el ensemble»
            self.en("ensemble")
            self.play(LaggedStart(*[Create(c) for c in pila1], lag_ratio=0.1), Create(corte_v), run_time=self.dur(1.7))

            # «todas las grabaciones posibles»
            self.en("todas")
            self.play(LaggedStart(*[Create(c) for c in pila2], lag_ratio=0.08), run_time=self.dur(1.4))

            # «Y nosotros estamos promediando»
            self.en("nosotros")
            self.pop(lupa_)

            # «trozos de una sola grabación»
            self.en("una")
            self.play(lupa_.animate.move_to([4.4, 1.1, 0]), Create(rd), run_time=self.dur(1.5))
            self.play(Create(seps), run_time=0.5)

            # «a lo largo del tiempo»
            self.en("tiempo")
            self.play(GrowArrow(f_t), run_time=self.dur(0.8))

            # «¿Con qué permiso?»
            self.en("permiso")
            self.pop(sel)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        L = Lienzo(ancho=8.4, alto=3.6, t_rango=(0, 1), v_max=2.4, centro=(1.0, -0.2))
        def yv(v):
            return float(L.y(v))
        sel = sello("ergodicidad = permiso", VERDE).scale(1.1).move_to([0, 3.3, 0])
        cap = etiqueta("capítulo 10", INK, 0.55).move_to([-5.6, 3.3, 0])
        volt = (1, -2, 2, 0)
        pilas = VGroup(*[pila(f"{v}", AMBAR).scale(0.6).move_to([-4.6, yv(v), 0]) for v in volt])
        rectas = rectas_pilas(L, volt, SENAL, 3.5)
        prom = Arrow(L.p(0.05, 2), L.p(0.93, 2), color=AMBAR, stroke_width=6, buff=0, max_tip_length_to_length_ratio=0.1)
        et2 = etiqueta("2 V", AMBAR, 0.6).move_to(L.p(1.0, 2) + RIGHT * 0.6)
        todas_l = DashedLine(L.p(0, 0.25), L.p(1, 0.25), color=TXT, stroke_width=3.5)
        et_t = etiqueta("todas", TXT, 0.55).move_to(L.p(1.0, 0.25) + RIGHT * 0.6)
        x_ = cruz().scale(1.0).move_to([4.8, 3.3, 0])
        no_e = etiqueta("no ergódico", ERROR, 0.55).move_to([6.0, 3.3, 0])
        mas_t = Arrow(L.p(0, -2.8), L.p(1, -2.8), color=AMBAR, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.06)
        l_mas = etiqueta("más tiempo", AMBAR, 0.5).move_to(L.p(0.5, -2.8) + DOWN * 0.3)
        no_llega = Arrow(L.p(0.9, 2), L.p(0.9, 1.1), color=ERROR, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.2)
        marco = SurroundingRectangle(pilas[2], color=AMBAR, buff=0.12, stroke_width=4)

        with self.narrar("b2"):
            # «la ergodicidad»
            self.en("ergo")
            self.corte()
            self.pop(sel)

            # «del capítulo anterior»
            self.en("cap10")
            self.play(FadeIn(cap), run_time=self.dur(0.5))

            # «Recuerda las pilas»
            self.en("pilas")
            self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in pilas], lag_ratio=0.2), run_time=self.dur(1.5))

            # «una tensión constante»
            self.en("constante")
            self.play(LaggedStart(*[Create(r) for r in rectas], lag_ratio=0.2), run_time=self.dur(1.6))

            # «promediar en el tiempo»
            self.en("prom_t")
            self.play(GrowArrow(prom), run_time=self.dur(1.0))

            # «el voltaje de esa pila»
            self.en("esa_pila")
            self.play(rectas[2].animate.set_stroke(AMBAR, 6), FadeIn(et2), run_time=self.dur(0.7))

            # «no el de todas»
            self.en("todas")
            self.play(Create(todas_l), FadeIn(et_t), run_time=self.dur(0.7))

            # «no es ergódico»
            self.en("noerg")
            self.play(FadeIn(x_, scale=0.5), FadeIn(no_e), run_time=self.dur(0.6))

            # «promediar más tiempo»
            self.en("mas_t")
            self.play(GrowArrow(mas_t), FadeIn(l_mas), run_time=self.dur(0.9))

            # «no te acerca a la densidad espectral del ensemble»
            self.en("noacerca")
            self.play(GrowArrow(no_llega), run_time=self.dur(1.2))

            # «el trozo de ensemble que te ha tocado»
            self.en("tocado")
            self.play(Create(marco), run_time=self.dur(0.8))
