"""Escena 04 — La progresión de 0,157, el candado hasta el episodio 5 y la regla práctica."""
from comun.escena import *


class LaProgresion(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.progresion()
        self.candado_wiener()
        self.regla()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def progresion(self):
        vals = [0.7386, 0.1158, 0.0182, 0.0028]
        T = Tallos(vals, centro=(-1.5, -1.6), paso=1.9, unidad=3.4, color=ESTIMACION)
        base_y = T.cy
        hk = [MathTex(f"h_{i}", color=TXT).scale(1.04).move_to([T.x(i), base_y - 0.35, 0]) for i in range(4)]
        txt = [Text(num(v, 4), color=TXT).scale(0.65).move_to([T.x(i), base_y - 0.85, 0]) for i, v in enumerate(vals)]
        flechas = [Arrow([T.x(i) + 0.45, base_y + 0.55, 0], [T.x(i + 1) - 0.45, base_y + 0.55, 0], color=INK,
                         stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.25) for i in range(3)]
        rat = [MathTex(r"\times 0{,}157", color=AMBAR).scale(0.78).move_to([(T.x(i) + T.x(i + 1)) / 2, base_y + 0.95, 0])
               for i in range(3)]
        curva = VMobject(color=INK, stroke_width=3)
        curva.set_points_smoothly([T.pos(i) for i in range(4)])
        prog = Text("progresión geométrica", color=INK).scale(0.65).move_to([4.6, 0.6, 0])
        q157 = MathTex(r"0{,}157", color=AMBAR).scale(1.56).move_to([-1.8, 3.0, 0])
        interr1 = Text("?", color=AMBAR, weight=BOLD).scale(1.17).next_to(q157, RIGHT, buff=0.15)
        q06 = MathTex(r"0{,}6", color=TXT).scale(1.56).move_to([1.7, 3.0, 0])
        tach = tachar(q06)
        reloj = reloj_arena().scale(0.9).move_to([5.8, 2.8, 0])
        self.q157, self.interr1, self.tach, self.q06, self.reloj = q157, interr1, tach, q06, reloj
        self.escena_prog = [T, *hk, *txt, *flechas, *rat, curva, prog]

        with self.narrar("b1"):
            # «Mira ahora los coeficientes»
            self.en("coefs")
            self.corte()
            self.play(FadeIn(T.base), *[FadeIn(h) for h in hk], run_time=self.dur(0.5))
            # los cuatro valores
            for i, m in enumerate(("h0", "h1", "h2", "h3")):
                self.en(m)
                self.play(FadeIn(T.palito(i)), FadeIn(txt[i]), run_time=self.dur(0.4))
            # «Divide cada uno entre el anterior»
            self.en("divide")
            self.play(*[Create(f) for f in flechas], run_time=self.dur(0.7))
            self.en("r1")
            self.play(FadeIn(rat[0]), run_time=0.3)
            self.en("r2")
            self.play(FadeIn(rat[1]), run_time=0.3)
            self.en("r3")
            self.play(FadeIn(rat[2]), run_time=0.3)
            # «Una progresión geométrica perfecta»
            self.en("prog")
            self.play(Create(curva), FadeIn(prog), run_time=self.dur(0.8))
            # «la sorpresa»
            self.en("sorpresa")
            self.resaltar(curva, color=AMBAR, run_time=0.6)
            # «¿por qué cero coma uno cinco siete»
            self.en("porque")
            self.play(FadeIn(q157), FadeIn(interr1), run_time=0.4)
            # «y no cero coma seis?»
            self.en("noseis")
            self.play(FadeIn(q06), run_time=0.3)
            self.play(Create(tach), run_time=0.3)
            # «Piénsalo.»
            self.en("pausa")
            self.play(FadeIn(reloj), run_time=0.4)

    # ------------------------------------------------------------------ b2
    def candado_wiener(self):
        cand = candado(AMBAR).scale(1.0)
        ep5 = Text("episodio 5", color=AMBAR).scale(0.65)
        ec = MathTex(r"a x^2 + b x + c = 0", color=TXT).scale(1.17).move_to([4.2, 2.6, 0])
        B = barras_error([0.8, 0.74, 0.7387, 0.7386, 0.7386], ["1", "2", "3", "5", "10"], centro=(-1.0, -0.6),
                         ancho=7.0, alto=2.6, v_max=1.0)
        y_lin = B.base.get_center()[1] + 0.7386 / 1.0 * 2.6
        linea = DashedLine([-4.5, y_lin, 0], [2.5, y_lin, 0], color=AMBAR, stroke_width=3)
        casual = Text("¡no es casual!", color=AMBAR, weight=BOLD).scale(0.78).move_to([4.2, 0.9, 0])
        mejor = sello("el mejor filtro", VERDE).move_to([4.4, -0.8, 0])
        flecha_p = Arrow([3.0, 1.5, 0], [-6.2, 1.5, 0], color=INK, stroke_width=4, buff=0)
        todo = Text("todo el pasado", color=INK).scale(0.65).move_to([1.2, 1.9, 0])
        cartel = RoundedRectangle(corner_radius=0.15, width=4.8, height=0.9, color=AMBAR, stroke_width=3
                                  ).move_to([-1.0, -3.3, 0])
        wiener = Text("filtro de Wiener causal", color=AMBAR, weight=BOLD).scale(0.72).move_to(cartel)

        with self.narrar("b2"):
            # «No lo vamos a contar todavía»
            self.en("candado")
            self.play(*[FadeOut(m) for m in (*self.escena_prog, self.q06, self.tach, self.interr1, self.reloj)],
                      self.q157.animate.move_to([-0.5, 3.0, 0]), run_time=0.4)
            cand.next_to(self.q157, LEFT, buff=0.3)
            ep5.next_to(cand, DOWN, buff=0.1)
            self.play(FadeIn(cand, scale=0.6), run_time=0.4)
            # «el episodio cinco»
            self.en("ep5")
            self.play(FadeIn(ep5), run_time=0.3)
            # «una ecuación de segundo grado»
            self.en("seg")
            self.play(FadeIn(ec), run_time=self.dur(0.6))
            # «el número al que se acerca el error»
            self.en("acerca")
            self.play(FadeIn(B), run_time=self.dur(0.6))
            self.play(Create(linea), run_time=0.5)
            # «tampoco es casual»
            self.en("casual")
            self.play(FadeIn(casual), run_time=0.4)
            self.resaltar(linea, color=VERDE, run_time=0.5)
            # «el error del mejor filtro»
            self.en("mejor")
            self.pop(mejor)
            # «que puede usar todo el pasado»
            self.en("pasado")
            self.play(Create(flecha_p), FadeIn(todo), run_time=self.dur(0.8))
            # «Ese filtro tiene nombre»
            self.en("nombre")
            self.play(Create(cartel), run_time=self.dur(0.5))
            # «filtro de Wiener causal»
            self.en("wiener")
            self.play(FadeIn(wiener), run_time=0.4)

    # ------------------------------------------------------------------ b3
    def regla(self):
        sel = sello("regla práctica", AMBAR).move_to([0, 3.2, 0])
        F = FilaMuestras([r"h_0", r"h_1", r"h_2", r"h_3", r"h_4"], centro=(-2.2, 1.4), lado=1.25,
                         color=ESTIMACION, escala=0.98)
        mas = MathTex(r"L\ \uparrow", color=AMBAR).scale(1.17).move_to([1.6, 1.4, 0])
        L = Lienzo(ancho=4.2, alto=1.8, t_rango=(0, 6), v_max=2.0, centro=(4.4, 1.4))
        curva_e = curva_f(L, lambda x: 0.1 + 0.9 * np.exp(-1.2 * x), 0, 6, ERROR, 4)
        base_e = L.base()
        casi0 = MathTex(r"\approx 0", color=AMBAR).scale(0.91).next_to(F.cas[4], DOWN, buff=0.3)
        sensor = FilaMuestras([r"x[n-2]", r"x[n-1]", r"x[n]"], centro=(-3.3, -1.0), lado=1.50, color=MEDIDA, escala=0.72)
        fl_a = Arrow([-1.2, -1.0, 0], [0.0, -1.0, 0], color=INK, stroke_width=4, buff=0)
        yh = caja("", ESTIMACION, ancho=1.2, alto=1.0).move_to([0.9, -1.0, 0])
        yht = MathTex(r"\hat y[n]", color=ESTIMACION).scale(1.04).move_to(yh)
        term = termometro(1.4).move_to([3.0, -1.0, 0])
        ecs = MathTex(r"C_{xx}\,h = c", color=TXT).scale(1.17).move_to([-1.0, -2.8, 0])
        fut = FilaMuestras([r"x[n+1]"], centro=(5.4, -1.0), lado=1.50, color=INK, escala=0.72)
        fut_q = Text("?", color=AMBAR, weight=BOLD).scale(1.04).next_to(fut.cas[0], UP, buff=0.15)
        salto = CurvedArrow([-3.3, -0.3, 0], [5.4, -0.3, 0], angle=-PI / 2.4, color=AMBAR, stroke_width=5)
        salto.permitir_encima = True

        with self.narrar("b3"):
            # «Regla práctica»
            self.en("regla")
            self.corte()
            self.pop(sel)
            # «aumentar ele»
            self.en("aumentar")
            self.play(FadeIn(VGroup(*F.cas[:3], *F.rots[:3])), FadeIn(mas), run_time=0.4)
            self.play(FadeIn(VGroup(F.cas[3], F.rots[3])), run_time=0.3)
            self.play(FadeIn(VGroup(F.cas[4], F.rots[4])), run_time=0.3)
            # «el error deje de bajar»
            self.en("baja")
            self.play(Create(base_e), Create(curva_e), run_time=self.dur(1.0))
            # «el último coeficiente sea despreciable»
            self.en("ultimo")
            self.play(VGroup(F.cas[4], F.rots[4]).animate.fade(0.7), FadeIn(casi0), run_time=0.5)
            # «Pero hemos estado estimando»
            self.en("estimando")
            self.corte()
            self.play(FadeIn(sensor), Create(fl_a), FadeIn(yh), FadeIn(yht), run_time=self.dur(0.8))
            # «la temperatura de ahora»
            self.en("ahora")
            self.play(FadeIn(term), run_time=0.4)
            self.resaltar(yh, color=AMBAR, run_time=0.5)
            # «Estas mismas ecuaciones sirven»
            self.en("sirven")
            self.play(FadeIn(ecs), run_time=0.5)
            # «más tentador»
            self.en("tentador")
            self.play(FadeIn(fut), FadeIn(fut_q), run_time=0.5)
            # «adivinar lo que todavía no ha ocurrido»
            self.en("futuro")
            self.play(Create(salto), run_time=self.dur(0.8))
