"""Escena 11 — El filtro de dos muestras del sensor: h₀ ≈ 0,74, h₁ ≈ 0,12, error 0,74."""
from comun.escena import *


class DosMuestras(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        css = Palitos([0, 1], [4, 2.4], ancho=2.8, alto=1.7, v_max=5.0, color=SENAL, centro=(-4.7, 1.9))
        cdd = Palitos([0, 1], [1, 0.0], ancho=2.8, alto=1.7, v_max=5.0, color=RUIDO, centro=(-0.4, 1.9))
        crr = Palitos([0, 1], [5, 2.4], ancho=2.8, alto=1.7, v_max=5.0, color=MEDIDA, centro=(3.9, 1.9))
        for p_ in (css, cdd, crr):
            p_.remove(p_.eje)
        tss = MathTex(r"R_{ss}", color=SENAL).scale(1.1).move_to([-4.7, 3.65, 0])
        tdd = MathTex(r"R_{dd}", color=RUIDO).scale(1.1).move_to([-0.4, 3.65, 0])
        trr = MathTex(r"R_{rr}", color=MEDIDA).scale(1.1).move_to([3.9, 3.65, 0])
        lds = MathTex("L=2", color=AMBAR).scale(1.0).move_to([6.4, 3.65, 0])
        cs0 = Text("4", color=SENAL).scale(0.45).next_to(css.pos(0), UP, buff=0.12)
        cs1 = Text("2,4", color=SENAL).scale(0.45).next_to(css.pos(1), UP, buff=0.12)
        cd0 = Text("1", color=RUIDO).scale(0.45).next_to(cdd.pos(0), UP, buff=0.12)
        cr0 = Text("5", color=MEDIDA).scale(0.45).next_to(crr.pos(0), UP, buff=0.12)
        cr1 = Text("2,4", color=MEDIDA).scale(0.45).next_to(crr.pos(1), UP, buff=0.12)

        e1 = MathTex("5h_0", "+", "2{,}4h_1", "=", "4", color=TXT).scale(1.45).move_to([0, -0.75, 0])
        e2 = MathTex("2{,}4h_0", "+", "5h_1", "=", "2{,}4", color=TXT).scale(1.45).move_to([0, -2.0, 0])
        self.e1, self.e2 = e1, e2

        with self.narrar("b1"):
            # «Con dos muestras»
            self.en("dos")
            self.play(FadeIn(lds), run_time=0.4)

            # «la señal vale cuatro en cero»
            self.en("s4")
            self.play(FadeIn(tss), FadeIn(css.base), Create(css.tallos[0]), FadeIn(css.puntos[0]), FadeIn(cs0),
                      run_time=0.7)

            # «dos coma cuatro a un paso»
            self.en("s24")
            self.play(Create(css.tallos[1]), FadeIn(css.puntos[1]), FadeIn(cs1), run_time=0.6)

            # «uno en cero y nada más»
            self.en("d1")
            self.play(FadeIn(tdd), FadeIn(cdd.base), Create(cdd.tallos[0]), FadeIn(cdd.puntos[0]), FadeIn(cd0),
                      run_time=0.7)

            # «cinco y dos coma cuatro»
            self.en("r5")
            self.play(FadeIn(trr), FadeIn(crr.base), Create(crr.tallos[0]), FadeIn(crr.puntos[0]), FadeIn(cr0),
                      Create(crr.tallos[1]), FadeIn(crr.puntos[1]), FadeIn(cr1), run_time=self.dur(1.0))

            # «Primera ecuación»
            self.en("e1")
            self.play(FadeIn(e1[:4]), run_time=0.7)

            # «igual a cuatro»
            self.en("igual4")
            self.pop(e1[4])

            # «Segunda»
            self.en("e2")
            self.play(FadeIn(e2[:2]), run_time=0.6)

            # «cinco por hache uno»
            self.en("c5h1")
            self.play(FadeIn(e2[2:]), run_time=0.7)
        self.arriba = VGroup(css, cdd, crr, tss, tdd, trr, lds, cs0, cs1, cd0, cr0, cr1)

    def parte_b2(self):
        e1, e2 = self.e1, self.e2
        u = 3.0
        b0 = Rectangle(width=1.1, height=0.74 * u, stroke_width=2, color=AMBAR).set_fill(AMBAR, 0.5)
        b0.move_to([-2.4, -3.0 + 0.74 * u / 2 + 0.0, 0]).shift(UP * 0.0)
        b1_ = Rectangle(width=1.1, height=0.12 * u, stroke_width=2, color=AMBAR).set_fill(AMBAR, 0.5)
        b1_.move_to([0.4, -3.0 + 0.12 * u / 2, 0])
        piso = Line([-4.0, -3.0, 0], [2.0, -3.0, 0], color=INK, stroke_width=2.5)
        h0 = MathTex("h_0", r"\approx", num_tex(0.74), color=ESTIMACION).scale(1.1).next_to(b0, UP, buff=0.15)
        h1 = MathTex("h_1", r"\approx", num_tex(0.12), color=ESTIMACION).scale(1.1).next_to(b1_, UP, buff=0.15)
        r0 = MathTex("r[n]", color=MEDIDA).scale(0.7).next_to(b0, DOWN, buff=0.12)
        r1 = MathTex("r[n-1]", color=MEDIDA).scale(0.7).next_to(b1_, DOWN, buff=0.12)
        mem = Palitos(range(4), [1, .6, .36, .22], ancho=2.2, alto=1.0, v_max=1.0, color=SENAL, centro=(5.2, -0.4))
        rui = Palitos(range(4), [1, 0, 0, 0], ancho=2.2, alto=1.0, v_max=1.0, color=RUIDO, centro=(5.2, -2.4))
        mem.remove(mem.eje)
        rui.remove(rui.eje)
        tmem = Text("temperatura", color=SENAL).scale(0.4).move_to([5.2, 0.6, 0])
        trui = Text("ruido", color=RUIDO).scale(0.4).move_to([5.2, -1.4, 0])
        baja = MathTex(num_tex(0.8), r"\to", num_tex(0.74), color=ERROR).scale(1.2).move_to([-5.2, -1.6, 0])
        ax, _ = ejes([0, 6, 1], [0, 1, 0.25], ancho=3.0, alto=1.7, tip=False)
        ax.move_to([5.2, -1.4, 0])
        curva_e = ax.plot(lambda x: 0.74 + 0.06 * np.exp(-0.9 * x) , x_range=[0, 6, 0.05], color=ERROR, stroke_width=4)

        with self.narrar("b2"):
            # «Resolviendo el sistema»
            self.en("resuelve")
            self.play(FadeOut(self.arriba), e1.animate.move_to([0, 3.3, 0]).scale(0.85),
                      e2.animate.move_to([0, 2.4, 0]).scale(0.85), run_time=0.7)

            # «hache cero vale cero coma siete cuatro»
            self.en("h0")
            self.play(Create(piso), FadeIn(b0), FadeIn(h0), FadeIn(r0), run_time=0.7)

            # «hache uno, cero coma uno dos»
            self.en("h1")
            self.play(FadeIn(b1_), FadeIn(h1), FadeIn(r1), run_time=0.7)

            # «sobre todo la muestra de ahora»
            self.en("ahora")
            self.resaltar(b0, color=AMBAR, escala=1.06)

            # «la temperatura recuerda y el ruido no»
            self.en("recuerda")
            self.play(FadeIn(mem), FadeIn(rui), FadeIn(tmem), FadeIn(trui), run_time=self.dur(0.9))

            # «de cero coma ocho a cero coma siete cuatro»
            self.en("baja")
            self.pop(baja)

            # «Con más muestras»
            self.en("mas")
            self.play(FadeOut(mem), FadeOut(rui), FadeOut(tmem), FadeOut(trui), run_time=0.3)
            self.play(Create(ax), run_time=0.4)

            # «cada vez menos»
            self.en("menos")
            self.play(Create(curva_e), run_time=self.dur(1.2))
        self.restos = VGroup(e1, e2, b0, b1_, piso, h0, h1, r0, r1, baja, ax, curva_e)

    def parte_b3(self):
        css = Palitos([0, 1], [4, 2.4], ancho=2.8, alto=1.7, v_max=5.0, color=SENAL, centro=(-3.6, 0.9))
        cdd = Palitos([0, 1], [1, 0.0], ancho=2.8, alto=1.7, v_max=5.0, color=RUIDO, centro=(0.0, 0.9))
        for p_ in (css, cdd):
            p_.remove(p_.eje)
        tss = MathTex(r"R_{ss}", color=SENAL).scale(0.9).move_to([-3.6, 2.65, 0])
        tdd = MathTex(r"R_{dd}", color=RUIDO).scale(0.9).move_to([0.0, 2.65, 0])
        camp = campana_mini(centro=(3.9, 0.9), ancho=2.0, alto=1.3, color=INK)
        tach = Line([2.9, 0.2, 0], [4.9, 1.6, 0], color=ROJO, stroke_width=7)
        sw = sello("Wiener", AMBAR).move_to([-2.6, -2.2, 0])
        cap = Text("capítulo 12", color=INK).scale(0.6).move_to([0.6, -2.2, 0])

        with self.narrar("b3"):
            # «solo la memoria de la señal y la del ruido»
            self.en("memorias")
            self.play(FadeOut(self.restos), run_time=0.3)
            self.play(FadeIn(css), FadeIn(tss), FadeIn(cdd), FadeIn(tdd), run_time=0.8)

            # «Ninguna densidad»
            self.en("nada")
            self.play(Create(camp), run_time=0.5)
            self.play(Create(tach), run_time=0.4)

            # «el filtro de Wiener»
            self.en("wiener")
            self.pop(sw)

            # «capítulo doce»
            self.en("cap12")
            self.play(FadeIn(cap), run_time=0.4)
