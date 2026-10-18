"""Escena 10 — Las tres reglas de la probabilidad y el complementario."""
from comun.escena import *


class TresReglas(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.bloque_reglas()
        self.bloque_complementario()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bloque_reglas(self):
        cols = (-4.6, 0.0, 4.6)

        with self.narrar("b1"):
            # «No vale cualquier número»
            self.en("cualquiera")
            a = Text("P = −3", color=TXT, weight=BOLD).scale(0.8).move_to([-2.0, 2.0, 0])
            b = Text("P = 7", color=TXT, weight=BOLD).scale(0.8).move_to([2.0, 2.0, 0])
            self.play(FadeIn(a), FadeIn(b), run_time=0.3)
            self.play(FadeIn(tachar(a)), FadeIn(tachar(b)), run_time=self.dur(0.4))
            self.malos = VGroup(a, b)

            # «tres reglas»
            self.en("reglas")
            fichas = VGroup()
            for i, x in enumerate(cols):
                c = Circle(radius=0.32, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.25)
                n = Text(str(i + 1), color=AMBAR, weight=BOLD).scale(0.6).move_to(c)
                fichas.add(VGroup(c, n).move_to([x, 3.2, 0]))
            self.corte()
            self.play(LaggedStart(*[GrowFromCenter(f) for f in fichas], lag_ratio=0.2), run_time=self.dur(0.6))

            # «Primera: está entre cero y uno»
            self.en("r1")
            x0, x1 = cols[0] - 1.5, cols[0] + 1.5
            barra = Line([x0, 1.3, 0], [x1, 1.3, 0], color=INK, stroke_width=4)
            l0 = Text("0", color=TXT, weight=BOLD).scale(0.6).next_to(barra.get_start(), UP, buff=0.2)
            l1 = Text("1", color=TXT, weight=BOLD).scale(0.6).next_to(barra.get_end(), UP, buff=0.2)
            punto = Dot([x0 + 0.35 * 3.0, 1.3, 0], radius=0.12, color=AMBAR)
            t1 = Text("Entre 0 y 1", color=AMBAR).scale(0.5).move_to([cols[0], -0.5, 0])
            self.play(Create(barra), FadeIn(l0), FadeIn(l1), run_time=0.4)
            self.play(FadeIn(punto), FadeIn(t1), run_time=self.dur(0.4))

            # «Cero es imposible»
            self.en("cero")
            im = Text("Imposible", color=ROJO).scale(0.5).next_to(barra.get_start(), DOWN, buff=0.25)
            self.pop(im)

            # «uno es seguro»
            self.en("uno")
            se = Text("Seguro", color=VERDE).scale(0.5).next_to(barra.get_end(), DOWN, buff=0.25)
            self.pop(se)

            # «Segunda: el espacio muestral entero vale uno»
            self.en("r2")
            rect = RoundedRectangle(corner_radius=0.15, width=2.8, height=1.7, color=INK, stroke_width=3).move_to([cols[1], 1.3, 0])
            uno = Text("P = 1", color=VERDE, weight=BOLD).scale(0.65).move_to([cols[1], 0.05, 0])
            t2 = Text("El total vale 1", color=AMBAR).scale(0.5).move_to([cols[1], -0.5, 0])
            self.play(Create(rect), run_time=0.3)
            self.play(FadeIn(uno), FadeIn(t2), run_time=self.dur(0.4))

            # «algo tiene que pasar»
            self.en("algo")
            d = dado_n(3).scale(0.6).move_to([cols[1], 2.6, 0])
            self.play(FadeIn(d), run_time=0.2)
            self.play(d.animate.move_to([cols[1], 1.3, 0]), run_time=self.dur(0.5))

            # «Tercera: si dos eventos»
            self.en("r3")
            ea = Ellipse(width=1.6, height=1.2, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.15).move_to([cols[2] - 1.0, 1.3, 0])
            eb = Ellipse(width=1.6, height=1.2, color=CIAN, stroke_width=4).set_fill(CIAN, 0.15).move_to([cols[2] + 1.0, 1.3, 0])
            la = Text("A", color=AMBAR, weight=BOLD).scale(0.6).move_to(ea)
            lb = Text("B", color=CIAN, weight=BOLD).scale(0.6).move_to(eb)
            t3 = Text("Si no se solapan, se suman", color=AMBAR).scale(0.5).move_to([cols[2], -0.5, 0])
            self.play(FadeIn(ea), FadeIn(la), run_time=self.dur(0.5))

            # «no pueden ocurrir a la vez»
            self.en("no_vez")
            self.play(FadeIn(eb), FadeIn(lb), run_time=self.dur(0.5))

            # «ocurra uno u otro»
            self.en("uno_u_otro")
            self.play(ea.animate(rate_func=there_and_back).set_stroke(width=9),
                      eb.animate(rate_func=there_and_back).set_stroke(width=9), FadeIn(t3), run_time=self.dur(0.8))

            # «la suma de sus probabilidades»
            self.en("suma")
            f = formula("P", "(A", r"\text{ o }", "B)", "=", "P(A)", "+", "P(B)", escala=0.8,
                        colores={1: AMBAR, 3: CIAN, 5: AMBAR, 7: CIAN}).move_to([3.7, -1.8, 0])
            self.play(LaggedStart(*[FadeIn(f[i]) for i in range(8)], lag_ratio=0.1), run_time=self.dur(1.2))

    # ------------------------------------------------------------ b2
    def bloque_complementario(self):
        E = EspacioDado(centro=(-3.0, -0.4))

        with self.narrar("b2"):
            # «una muy útil»
            self.en("util")
            self.corte()
            tit = Text("El complementario", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.3, 0])
            self.pop(tit)

            # «algo no pase»
            self.en("no_pase")
            self.play(FadeIn(E), run_time=self.dur(0.4))
            self.resaltar(E.caras[6], color=AMBAR, run_time=0.5)
            self.play(*[E.caras[n].animate.set_stroke(CIAN) for n in (1, 2, 3, 4, 5)], run_time=self.dur(0.4))

            # «uno menos la probabilidad de que pase»
            self.en("formula")
            f = formula(r"P(\text{no }A)", "=", "1", "-", "P(A)", escala=0.95, colores={0: CIAN, 4: AMBAR}).move_to([3.4, 1.8, 0])
            self.play(LaggedStart(*[FadeIn(f[i]) for i in range(5)], lag_ratio=0.25), run_time=self.dur(1.4))

            # «¿Qué probabilidad hay»
            self.en("que_prob")
            self.resaltar(E.caras[6], color=AMBAR, run_time=0.6)

            # «no sacar un seis»
            self.en("no_seis")
            tz = tachar(E.caras[6])
            nos = Text("No sacar un 6", color=CIAN, weight=BOLD).scale(0.6).move_to([3.4, 0.4, 0])
            self.play(FadeIn(tz), run_time=0.3)
            self.pop(nos)

            # «Uno menos un sexto»
            self.en("cuenta")
            c = formula("1", "-", r"\tfrac{1}{6}", escala=1.2).move_to([3.4, -0.9, 0])
            self.play(LaggedStart(*[FadeIn(c[i]) for i in range(3)], lag_ratio=0.3), run_time=self.dur(0.9))

            # «cinco sextos»
            self.en("cinco_sextos")
            r = formula("=", r"\tfrac{5}{6}", escala=1.2, colores={1: VERDE}).next_to(c, DOWN, buff=0.35)
            self.play(FadeIn(r), run_time=self.dur(0.4))
            self.resaltar(r[1], color=VERDE, run_time=0.5)
