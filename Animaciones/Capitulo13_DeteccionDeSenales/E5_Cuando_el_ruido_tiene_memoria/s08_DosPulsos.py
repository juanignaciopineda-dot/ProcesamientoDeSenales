"""Escena 08 — Dos pulsos con la misma energía: (1, 1) lento y (1, −1) rápido, con ruido lento."""
from comun.escena import *


class DosPulsos(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.mismos()
        self.direcciones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def mismos(self):
        tres = [Tallos(v, centro=(x, 1.6), paso=1.1, unidad=0.5, color=SENAL)
                for v, x in (([3, 0, 0], -4.6), ([2, 2, 1], 0.0), ([1, 2, 2], 4.6))]
        e9 = MathTex("E = 9", color=AMBAR).scale(1.3).move_to([0, 0.2, 0])
        si = Text("con memoria: sí", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -1.4, 0])
        A = Tallos([1, 1], centro=(-3.6, 1.6), paso=1.0, unidad=0.8, color=SENAL, indices=True)
        B = Tallos([1, -1], centro=(3.6, 1.6), paso=1.0, unidad=0.8, color=SENAL, indices=True)
        e2 = MathTex("E = 2", color=AMBAR).scale(1.0).move_to([0, 1.6, 0])
        la = MathTex(r"(1,\ 1)", color=SENAL).scale(0.9).move_to([-3.6, 0.2, 0])
        lb = MathTex(r"(1,\ -1)", color=SENAL).scale(0.9).move_to([3.6, -0.3, 0])
        lento = Line(A.pos(0), A.pos(1), color=AMBAR, stroke_width=5)
        rapido = Line(B.pos(0), B.pos(1), color=AMBAR, stroke_width=5)
        t_lento = Text("lento", color=INK).scale(0.55).move_to([-3.6, 3.0, 0])
        t_rapido = Text("rápido", color=INK).scale(0.55).move_to([3.6, 3.0, 0])
        P = PlanoV(centro=(0, -2.4), lado=1.5, esc=0.8)
        nube = P.puntos(0.6, n=30)
        el = P.elipse(0.6)
        rho = MathTex(r"\rho = 0{,}6", color=AMBAR).scale(0.8).move_to([3.4, -2.4, 0])
        eje_largo = DoubleArrow(P.p(-1.55, -1.55), P.p(1.55, 1.55), color=RUIDO, stroke_width=5, buff=0,
                                max_tip_length_to_length_ratio=0.1)

        with self.narrar("b1"):
            # «la forma de la señal no importaba»
            self.en("forma")
            for T in tres:
                self.play(Create(T.base), *[Create(T.palito(i)) for i in range(3)], run_time=self.dur(0.4))

            # «solo la energía»
            self.en("energia")
            self.pop(e9)

            # «Con ruido con memoria, sí»
            self.en("si")
            self.pop(si)

            # «dos pulsos de dos muestras»
            self.en("dospulsos")
            self.corte()
            self.play(Create(A.base), Create(A.palito(0)), Create(A.palito(1)), FadeIn(A.ks),
                      Create(B.base), Create(B.palito(0)), Create(B.palito(1)), FadeIn(B.ks),
                      run_time=self.dur(0.9))

            # «la misma energía, dos»
            self.en("e2")
            self.pop(e2)

            # «Uno, uno»
            self.en("uno1")
            self.play(FadeIn(la, shift=UP * 0.1), run_time=self.dur(0.4))

            # «no cambia de signo, es lento»
            self.en("lento")
            self.play(Create(lento), FadeIn(t_lento), run_time=self.dur(0.6))

            # «Y uno, menos uno»
            self.en("uno_m1")
            self.play(FadeIn(lb, shift=UP * 0.1), run_time=self.dur(0.4))

            # «cambia de signo en cada muestra, es rápido»
            self.en("rapido")
            self.play(Create(rapido), FadeIn(t_rapido), run_time=self.dur(0.6))

            # «El ruido»
            self.en("ruido")
            self.play(Create(P.ejes), FadeIn(P.rot0), FadeIn(P.rot1), FadeIn(nube), Create(el),
                      run_time=self.dur(0.8))

            # «el del eco del cero coma seis»
            self.en("eco")
            self.play(FadeIn(rho), run_time=self.dur(0.5))

            # «es un ruido lento»
            self.en("ruidolento")
            self.play(Create(eje_largo), run_time=self.dur(0.7))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def direcciones(self):
        P = PlanoV(centro=(-3.8, -0.2), lado=2.4, esc=1.0)
        nube = P.puntos(0.6, n=34)
        el = P.elipse(0.6)
        largo = DoubleArrow(P.p(-1.34, -1.34), P.p(1.34, 1.34), color=RUIDO, stroke_width=5, buff=0,
                            max_tip_length_to_length_ratio=0.1)
        corto = DoubleArrow(P.p(-0.67, 0.67), P.p(0.67, -0.67), color=INK, stroke_width=5, buff=0,
                            max_tip_length_to_length_ratio=0.18)
        l_suma = MathTex("v_0+v_1", color=RUIDO).scale(0.7).next_to(P.p(1.34, 1.34), UR, buff=0.05)
        l_resta = MathTex("v_0-v_1", color=INK).scale(0.7).move_to(P.p(1.6, -1.85))
        conex = Line(P.p(0.67, -0.67), l_resta.get_top() + UP * 0.05, color=INK, stroke_width=2)
        f1 = MathTex(r"\mathrm{Var}(v_0+v_1)", "=", r"1+1+2\cdot 0{,}6", "=", num_tex(3.2),
                     color=TXT).scale(0.85).move_to([3.2, 1.6, 0])
        f2 = MathTex(r"\mathrm{Var}(v_0-v_1)", "=", r"1+1-1{,}2", "=", num_tex(0.8),
                     color=TXT).scale(0.85).move_to([3.2, -0.1, 0])
        f1[4].set_color(AMBAR); f2[4].set_color(AMBAR)

        with self.narrar("b2"):
            # «¿Cuánto fluctúa el ruido en cada dirección?»
            self.en("cuanto")
            self.corte(P, nube, el)
            self.play(Create(largo), Create(corto), run_time=self.dur(0.8))

            # «La suma de las dos muestras»
            self.en("suma")
            self.play(FadeIn(l_suma), FadeIn(f1[0]), FadeIn(f1[1]), run_time=self.dur(0.6))

            # «uno más uno, más dos veces cero coma seis»
            self.en("cuenta1")
            self.play(FadeIn(f1[2], shift=UP * 0.1), run_time=self.dur(0.8))

            # «tres coma dos»
            self.en("t32")
            self.play(FadeIn(f1[3]), FadeIn(f1[4]), run_time=self.dur(0.5))

            # «La resta»
            self.en("resta")
            self.play(FadeIn(l_resta), Create(conex), FadeIn(f2[0]), FadeIn(f2[1]), run_time=self.dur(0.6))

            # «uno más uno, menos uno coma dos»
            self.en("cuenta2")
            self.play(FadeIn(f2[2], shift=UP * 0.1), run_time=self.dur(0.8))

            # «cero coma ocho»
            self.en("t08")
            self.play(FadeIn(f2[3]), FadeIn(f2[4]), run_time=self.dur(0.5))

            # «fluctúa mucho a lo largo de la suma»
            self.en("mucho")
            self.resaltar(largo, color=AMBAR, escala=1.1)

            # «poco a lo largo de la resta»
            self.en("poco")
            self.resaltar(corto, color=AMBAR, escala=1.2)
