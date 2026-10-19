"""Escena 08 — La pendiente: cómo se encuentra el fondo de la parábola (derivada = pendiente)."""
from comun.escena import *


class LaPendiente(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.pendiente()
        self.derivada()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pendiente(self):
        P = ParabolaJ(centro=(-0.8, -0.4), ancho=8.0, alto=4.2)
        h = ValueTracker(0.2)
        punto = Dot(radius=0.11, color=AMBAR)
        punto.add_updater(lambda m: m.move_to(P.p(h.get_value())))
        tang = P.pendiente(0.2, 2.6, AMBAR)
        tang.add_updater(lambda m: m.become(P.pendiente(h.get_value(), 2.6, AMBAR)))
        saltos = Dot(radius=0.11, color=TXT)
        prob = Text("Probar valores", color=INK).scale(0.6).move_to([5.1, 2.6, 0])
        tach = tachar(prob)
        pie = Text("Pendiente = derivada", color=AMBAR, weight=BOLD).scale(0.65).move_to([0, 3.3, 0])
        # el escalón: un paso a la derecha y lo que sube
        h0 = 1.4
        s0 = P.p(h0)
        ancho_px = 0.8
        pend_px = (-8 + 10 * h0) * (4.2 / 6.0) / (8.0 / 2.0)
        corre = Line(s0, s0 + RIGHT * ancho_px, color=TXT, stroke_width=4)
        sube = Line(s0 + RIGHT * ancho_px, s0 + RIGHT * ancho_px + UP * pend_px * ancho_px, color=VERDE,
                    stroke_width=5)
        t_corre = Text("Un paso", color=TXT).scale(0.45).move_to(s0 + RIGHT * ancho_px / 2 + DOWN * 0.3)
        t_sube = Text("Sube", color=VERDE).scale(0.4).move_to(s0 + RIGHT * (ancho_px + 0.5) + UP * pend_px * ancho_px / 2)
        sg_neg = MathTex("-", color=ERROR).scale(1.8).move_to(P.p(0.2) + UP * 1.0 + RIGHT * 0.9)
        sg_pos = MathTex("+", color=VERDE).scale(1.8).move_to(P.p(1.4) + UP * 1.0 + LEFT * 0.9)
        cero = MathTex("0", color=AMBAR).scale(1.4).move_to(P.p(0.8) + UP * 0.9)

        with self.narrar("b1"):
            # «el punto más bajo de una parábola»
            self.en("bajo")
            self.play(Create(P.eje), Create(P.curva), run_time=self.dur(1.0))
            self.pop(P.vertice)

            # «sin probar valores»
            self.en("probar")
            self.add(saltos)
            for hv in (0.1, 0.5, 1.4):
                self.play(saltos.animate.move_to(P.p(hv)), run_time=0.25)
            self.play(FadeIn(prob), run_time=0.3)
            self.play(Create(tach), FadeOut(saltos), run_time=self.dur(0.4))

            # «Con la pendiente»
            self.en("pend")
            self.play(FadeOut(prob), FadeOut(tach), run_time=0.2)
            self.add(tang, punto)

            # «En cada punto de una curva»
            self.en("cadapunto")
            self.play(h.animate.set_value(1.5), run_time=self.dur(2.0), rate_func=linear)

            # «cuánto sube por cada paso hacia la derecha»
            self.en("paso")
            self.play(h.animate.set_value(h0), run_time=self.dur(0.5))
            self.play(Create(corre), run_time=self.dur(0.4))
            self.play(Create(sube), FadeIn(t_corre), FadeIn(t_sube), run_time=self.dur(0.7))

            # «la derivada»
            self.en("deriv")
            self.pop(pie)

            # «la pendiente es negativa»
            self.en("neg")
            self.play(FadeOut(corre), FadeOut(sube), FadeOut(t_corre), FadeOut(t_sube), run_time=0.2)
            self.play(h.animate.set_value(0.2), run_time=self.dur(0.6))
            self.pop(sg_neg)

            # «positiva»
            self.en("pos")
            self.play(h.animate.set_value(1.4), run_time=self.dur(0.8))
            self.pop(sg_pos)

            # «en el fondo»
            self.en("fondo")
            self.play(h.animate.set_value(0.8), run_time=self.dur(1.2))

            # «es cero»
            self.en("cero")
            self.pop(cero)
            tang.clear_updaters()
            punto.clear_updaters()
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def derivada(self):
        J = formula("J(h)", "=", "4", "-8h", "+5h^2", escala=1.4, colores={0: ERROR}).move_to([0, 3.0, 0])
        d = formula("J'(h)", "=", "-8", "+10h", escala=1.4, colores={0: ERROR}).move_to([0, 1.7, 0])
        cero = MathTex("=", "0", color=TXT).scale(1.4)
        cero.next_to(d, RIGHT, buff=0.15)
        h810 = MathTex("h", "=", r"\frac{8}{10}", color=TXT).scale(1.4).move_to([0, 0.3, 0])
        h810[0].set_color(AMBAR)
        eahi = formula(r"J(0{,}8)", "=", "4", "-", r"6{,}4", "+", r"3{,}2", "=", r"0{,}8", escala=1.4,
                       colores={0: ERROR, 8: ERROR}).move_to([0, -1.4, 0])
        letras = Text("Ahora, con letras", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -3.0, 0])

        with self.narrar("b2"):
            # «La derivada de»
            self.en("dd")
            self.corte()
            self.play(*[FadeIn(J[i]) for i in range(5)], run_time=self.dur(0.9))

            # «menos ocho más diez hache»
            self.en("d")
            self.play(*[FadeIn(d[i], shift=UP * 0.1) for i in range(4)], run_time=self.dur(0.9))

            # «Igualada a cero»
            self.en("igual0")
            self.play(FadeIn(cero, shift=LEFT * 0.1), run_time=self.dur(0.5))

            # «ocho décimos»
            self.en("h810")
            self.play(FadeIn(h810, shift=UP * 0.1), run_time=self.dur(0.7))

            # «Y el error ahí»
            self.en("eahi")
            self.play(*[FadeIn(eahi[i]) for i in range(3)], run_time=self.dur(0.6))

            # «menos seis coma cuatro»
            self.en("c64")
            self.play(FadeIn(eahi[3]), FadeIn(eahi[4], shift=UP * 0.1), run_time=self.dur(0.5))

            # «más tres coma dos»
            self.en("c32")
            self.play(FadeIn(eahi[5]), FadeIn(eahi[6], shift=UP * 0.1), run_time=self.dur(0.5))

            # «cero coma ocho. Ahora»
            self.en("r08")
            self.play(FadeIn(eahi[7]), FadeIn(eahi[8], shift=UP * 0.1), run_time=self.dur(0.5))

            # «lo mismo con letras»
            self.en("letras")
            self.pop(letras)
