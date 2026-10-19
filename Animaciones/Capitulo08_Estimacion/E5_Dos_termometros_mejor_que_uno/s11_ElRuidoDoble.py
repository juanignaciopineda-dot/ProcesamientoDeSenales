"""Escena 11 — El ruido doble: pesos 2 y −1, error cero; con números, 20 + 2 · 3 − 1 · 4 = 22."""
from comun.escena import *
from comun.figuras_c8e5 import *


class ElRuidoDoble(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.resolver()
        self.con_numeros()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resolver(self):
        carta = tarjeta8(r"B_3", centro=(0, 0)).scale(0.3).move_to([6.1, 3.3, 0])
        self.add(carta)
        A = Termo8("A", centro=(-5.2, 0.9), alto=2.4, escala_letra=0.9)
        B3 = Termo8("B_3", centro=(-2.2, 0.9), alto=2.4, escala_letra=0.9)
        excl = Text("!", color=AMBAR, weight=BOLD).scale(1.6).move_to([-1.2, 2.6, 0])
        ra = A.debajo(ruido8(ancho=2.0, amp=0.1, semilla=7, grosor=4), 0.35)
        rb = B3.debajo(ruido8(ancho=2.0, amp=0.2, semilla=7, grosor=4), 0.35)
        rb.set_y(ra.get_y())
        m05 = MathTex(r"+0{,}5", color=RUIDO).scale(0.85).next_to(A.t.tubo, RIGHT, buff=0.2)
        m1 = MathTex(r"+1", color=RUIDO).scale(0.85).next_to(B3.t.tubo, RIGHT, buff=0.2)
        M, H, igual, C, sis = sistema8([["5", "6"], ["6", "8"]], centro=(3.7, 1.7), escala=0.85)
        h = formula(r"\mathbf{h}=(2\,;\,", "-1", ")", escala=1.1).move_to([3.4, 0.2, 0])
        e0 = MathTex(r"\text{Error}=0", color=VERDE).scale(1.1).move_to([3.4, -0.9, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.8).move_to([0, 2.8, 0])
        r = formula(r"x_{B_3}-x_A", "=", r"(y+2v_A)-(y+v_A)", "=", "v_A", escala=1.05,
                    colores={0: MEDIDA, 4: RUIDO}).move_to([0, 1.0, 0])
        quita = formula("y", "=", "x_A", "-", "v_A", escala=1.2, colores={0: SENAL, 2: MEDIDA, 4: RUIDO})
        quita.move_to([0, -0.6, 0])

        with self.narrar("b1"):
            # «El tercero»
            self.en("b3")
            self.play(carta.animate.scale(1 / 0.3).move_to([-2.2, 0.6, 0]), run_time=self.dur(0.4))
            self.play(carta.animate.stretch(0.03, 0), run_time=0.2)
            self.remove(carta)
            self.play(FadeIn(A), FadeIn(B3), run_time=self.dur(0.4))

            # «el más curioso»
            self.en("curioso")
            self.pop(excl)

            # «el doble que el de A»
            self.en("doble")
            self.play(Create(ra), run_time=0.4)
            self.play(TransformFromCopy(ra, rb), run_time=self.dur(0.7))

            # «Si A se pasa medio grado»
            self.en("medio")
            self.play(FadeIn(m05, shift=UP * 0.1), run_time=self.dur(0.4))

            # «este se pasa un grado»
            self.en("uno")
            self.play(FadeIn(m1, shift=UP * 0.1), run_time=self.dur(0.4))

            # «Al resolver»
            self.en("res")
            self.play(FadeIn(sis), run_time=self.dur(0.6))

            # «dos y menos uno»
            self.en("pesos")
            self.play(FadeIn(h, shift=UP * 0.1), run_time=self.dur(0.5))

            # «¡Un peso negativo!»
            self.en("neg")
            self.play(h[1].animate.set_color(AMBAR).scale(1.3), run_time=0.4)
            self.sfx("pop")

            # «Y el error, cero»
            self.en("e0")
            self.pop(e0, sonido="exito")

            # «¿Por qué?»
            self.en("porque")
            self.corte()
            self.pop(q)

            # «menos la de A»
            self.en("resta")
            self.play(*[FadeIn(r[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.7))

            # «justo el ruido de A»
            self.en("va")
            self.play(FadeIn(r[3]), FadeIn(r[4], shift=LEFT * 0.1), run_time=self.dur(0.5))

            # «sabes cuánto se equivocó A»
            self.en("sabes")
            self.resaltar(r[4], color=AMBAR, escala=1.3)

            # «y lo quitas»
            self.en("quita")
            self.play(FadeIn(quita, shift=UP * 0.1), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b2
    def con_numeros(self):
        xa = MathTex("x_A=23", color=MEDIDA).scale(1.1).move_to([-3.0, 2.7, 0])
        xb = MathTex("x_{B_3}=24", color=MEDIDA).scale(1.1).move_to([2.0, 2.7, 0])
        dif = formula("24-23=1", "=", "v_A", escala=1.1, colores={2: RUIDO}).move_to([-0.5, 1.45, 0])
        y22 = MathTex("y=23-1=22", color=VERDE).scale(1.1).move_to([-0.5, 0.25, 0])
        ap = formula(r"\hat{y}", "=", "20", r"+2\cdot 3", r"-1\cdot 4", "=22", escala=1.1,
                     colores={0: ESTIMACION, 5: VERDE}).move_to([-0.5, -1.15, 0])
        ok = tilde(VERDE, 0.55).next_to(ap, RIGHT, buff=0.35)
        parece = Text("Parecerse a la señal", color=INK).scale(0.8).move_to([0, 1.3, 0])
        tache = tachar(parece)
        nuevo = Text("Vale lo que trae de nuevo", color=AMBAR, weight=BOLD).scale(0.85).move_to([0, -0.1, 0])
        lin = formula(r"C_{xx}", r"\,\mathbf{h}", "=", r"\mathbf{c}_{xy}", escala=1.2,
                      colores={1: ESTIMACION, 3: SENAL}).move_to([0, -1.7, 0])

        with self.narrar("b2"):
            # «A marca veintitrés»
            self.en("a23")
            self.corte()
            self.play(FadeIn(xa, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «el tercero, veinticuatro»
            self.en("b24")
            self.play(FadeIn(xb, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «La diferencia, uno»
            self.en("dif")
            self.play(FadeIn(dif[0], shift=UP * 0.1), run_time=self.dur(0.5))

            # «es el ruido de A»
            self.en("esva")
            self.play(FadeIn(dif[1]), FadeIn(dif[2], shift=LEFT * 0.1), run_time=self.dur(0.4))

            # «veintitrés menos uno, veintidós»
            self.en("t22")
            self.play(FadeIn(y22, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Y eso dan los pesos»
            self.en("pesos2")
            self.play(*[FadeIn(ap[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(0.5))

            # «más dos por tres»
            self.en("p2")
            self.play(FadeIn(ap[3], shift=UP * 0.1), run_time=self.dur(0.4))

            # «menos uno por cuatro»
            self.en("p1")
            self.play(FadeIn(ap[4], shift=UP * 0.1), run_time=self.dur(0.4))

            # «cuatro. Veintidós»
            self.en("ok22")
            self.play(FadeIn(ap[5], shift=LEFT * 0.1), run_time=0.4)
            self.play(Create(ok), run_time=0.5)
            self.sfx("exito")
            self.play(Circumscribe(ap, color=VERDE, buff=0.15), run_time=1.2)

            # «no vale por lo que se parece a la señal»
            self.en("parece")
            self.corte()
            self.play(FadeIn(parece), run_time=0.3)
            self.play(Create(tache), run_time=self.dur(0.4))

            # «lo que trae de nuevo»
            self.en("nuevo")
            self.pop(nuevo)

            # «lo calculan solas»
            self.en("solas")
            self.play(FadeIn(lin, shift=UP * 0.1), run_time=self.dur(0.5))
