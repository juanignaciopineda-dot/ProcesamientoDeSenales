"""Escena 09 — Una regla, no un número: la estimación ya calculada es un número; el estimador es una variable aleatoria."""
from comun.escena import *


class ReglaYNumero(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.numero()
        self.regla()
        self.wait(1.0)
        self.limpiar()

    def numero(self):
        fdef = MathTex(r"f(x)=x^2", color=TXT).scale(1.3).move_to([0, 3.2, 0])
        f3 = MathTex(r"f(3)=9", color=TXT).scale(1.7).move_to([-3.6, 1.7, 0])
        fx = MathTex(r"f(x)", color=TXT).scale(1.7).move_to([3.6, 1.7, 0])
        num_ = caja("Un número", SENAL, ancho=3.6, alto=1.0, scale=0.8).move_to([-3.6, 0.2, 0])
        reg_ = caja("Una regla", AMBAR, ancho=3.6, alto=1.0, scale=0.8).move_to([3.6, 0.2, 0])
        hueco = Square(0.5, color=INK, stroke_width=3)
        with self.narrar("b1"):
            # «dos cosas que se escriben casi igual»
            self.en("dos")
            self.play(FadeIn(f3), FadeIn(fx), run_time=self.dur(0.5))

            # «Una función evaluada en tres»
            self.en("evaluada")
            self.play(FadeIn(fdef, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «efe de tres»
            self.en("f3")
            self.resaltar(f3, color=AMBAR)

            # «es un número»
            self.en("numero")
            self.pop(num_)

            # «Una función sin evaluar»
            self.en("sin_evaluar")
            fh = MathTex(r"f(\,\cdot\,)", color=TXT).scale(1.7).move_to(fx)
            self.play(Transform(fx, fh), run_time=self.dur(0.5))

            # «es una regla»
            self.en("regla")
            self.pop(reg_)

            # «Con la estimación pasa lo mismo»
            self.en("igual")
            ig = Text("Con la estimación, igual", color=INK).scale(0.8).move_to([0, -1.1, 0])
            self.play(FadeIn(ig), run_time=self.dur(0.4))

            # «Si ya recibiste un uno»
            self.en("recibido")
            r1 = MathTex(r"R=1", color=MEDIDA).scale(1.4).move_to([-5.4, -2.5, 0])
            casilla = caja(" ", SENAL, ancho=2.6, alto=1.2, scale=0.5).move_to([-1.9, -2.5, 0])
            fl = flecha(r1.get_right() + RIGHT * 0.1, casilla.get_left() + LEFT * 0.1, AMBAR, 4)
            self.play(FadeIn(r1), Create(fl), FadeIn(casilla), run_time=self.dur(0.6))

            # «cero coma setenta y nueve»
            self.en("n79")
            self.pop(MathTex(r"0{,}79", color=VERDE).scale(1.5).move_to(casilla))

    def regla(self):
        caja_r = caja("Regla", AMBAR, ancho=3.0, alto=1.3, scale=0.9).move_to([0, 2.9, 0])
        ent = flecha([-3.4, 2.9, 0], [-1.6, 2.9, 0], MEDIDA, 5)
        sal = flecha([1.6, 2.9, 0], [3.4, 2.9, 0], AMBAR, 5)
        rr = MathTex("R", color=MEDIDA).scale(1.4).move_to([-4.6, 2.9, 0])
        l1 = MathTex(r"R=1\ \longrightarrow\ 0{,}79", color=TXT).scale(1.4).move_to([0, 1.2, 0])
        l0 = MathTex(r"R=0\ \longrightarrow\ 0{,}045", color=TXT).scale(1.4).move_to([0, 0.1, 0])
        base = Line([-3.6, -3.4, 0], [3.6, -3.4, 0], color=INK, stroke_width=3)
        x45, x79 = -2.2, 2.2
        e45 = MathTex(r"0{,}045", color=INK).scale(0.7).move_to([x45, -3.8, 0])
        e79 = MathTex(r"0{,}79", color=INK).scale(0.7).move_to([x79, -3.8, 0])
        with self.narrar("b2"):
            # «antes de recibir nada»
            self.en("antes")
            self.corte()
            self.play(FadeIn(caja_r), Create(ent), FadeIn(rr), run_time=self.dur(0.6))

            # «si llega un uno»
            self.en("llega1")
            self.play(FadeIn(l1, shift=UP * 0.2), run_time=self.dur(0.5))

            # «si llega un cero»
            self.en("llega0")
            self.play(FadeIn(l0, shift=UP * 0.2), run_time=self.dur(0.5))

            # «cero coma cero cuatro cinco»
            self.en("n045")
            self.resaltar(l0, color=AMBAR)

            # «lo que llega es aleatorio»
            self.en("aleatorio")
            for v in ("1", "0", "1"):
                n = MathTex("R", "=", v, color=MEDIDA).scale(1.4).move_to(rr)
                self.play(Transform(rr, n), run_time=0.3)

            # «la apuesta también lo es»
            self.en("tambien")
            self.play(Create(sal), run_time=self.dur(0.3))
            sh = MathTex(r"\hat{S}", color=ESTIMACION).scale(1.8).move_to([4.4, 2.9, 0])
            self.pop(sh)

            # «variable aleatoria»
            self.en("va")
            va = Text("Variable aleatoria", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, -0.6, 0])
            self.pop(va)

            # «con su propia distribución»
            self.en("distrib")
            self.play(Create(base), FadeIn(e45), FadeIn(e79), run_time=self.dur(0.5))

            # «vale cero coma setenta y nueve»
            self.en("vale79")
            h = 2.3
            b79 = Rectangle(width=1.0, height=0.34 * h, color=VERDE, stroke_width=2.5).set_fill(VERDE, 0.5)
            b79.move_to([x79, -3.4 + 0.34 * h / 2, 0])
            self.play(GrowFromEdge(b79, DOWN), run_time=self.dur(0.6))

            # «cero coma treinta y cuatro»
            self.en("p34")
            self.pop(MathTex(r"0{,}34", color=VERDE).scale(0.9).next_to(b79, UP, buff=0.15))

            # «cero coma sesenta y seis»
            self.en("p66")
            b45 = Rectangle(width=1.0, height=0.66 * h, color=VERDE, stroke_width=2.5).set_fill(VERDE, 0.5)
            b45.move_to([x45, -3.4 + 0.66 * h / 2, 0])
            self.play(GrowFromEdge(b45, DOWN), run_time=self.dur(0.5))
            self.pop(MathTex(r"0{,}66", color=VERDE).scale(0.9).next_to(b45, UP, buff=0.15))
