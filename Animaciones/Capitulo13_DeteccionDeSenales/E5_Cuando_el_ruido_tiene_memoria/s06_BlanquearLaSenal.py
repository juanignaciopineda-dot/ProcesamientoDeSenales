"""Escena 06 — Blanquear la señal: el pulso (2, 0) pasa a (2, −1,5), con energía 6,25."""
from comun.escena import *


class BlanquearLaSenal(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.pulso()
        self.energia()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def pulso(self):
        S = Tallos([2, 0], centro=(-5.2, 1.2), paso=1.0, unidad=0.7, color=SENAL)
        blanq = caja("blanqueador", ESTIMACION, ancho=2.8, alto=0.9, scale=0.5).move_to([-1.2, 1.4, 0])
        a_ent = flecha([-4.0, 1.4, 0], blanq.get_left(), INK)
        P = Tallos([2, -1.5], centro=(4.0, 1.4), paso=1.0, unidad=0.7, color=SENAL)
        a_sal = flecha(blanq.get_right(), [2.9, 1.4, 0], INK)
        c1 = MathTex("p_1", "=", r"\frac{0-0{,}6\cdot 2}{0{,}8}", color=TXT).scale(0.95).move_to([-1.2, -1.0, 0])
        c1[2].set_color(TXT)
        res = MathTex("= -1{,}5", color=SENAL).scale(1.0).next_to(c1, RIGHT, buff=0.3)
        etiq = MathTex(r"(2,\ -1{,}5)", color=SENAL).scale(1.0).move_to([4.0, 3.2, 0])
        circ = Circle(radius=1.0, color=RUIDO, stroke_width=4).set_fill(RUIDO, 0.12).move_to([-4.0, -2.0, 0])
        circ_l = Text("ruido blanco", color=RUIDO).scale(0.45).next_to(circ, DOWN, buff=0.15)
        filt = caja("filtro adaptado", SENAL, ancho=3.2, alto=0.9, scale=0.5).move_to([3.0, -2.0, 0])
        inv = Tallos([-1.5, 2], centro=(6.0, -2.0), paso=0.7, unidad=0.35, color=ESTIMACION)

        with self.narrar("b1"):
            # «el mismo blanqueador»
            self.en("mismo")
            self.play(Create(S.base), Create(S.palito(0)), Create(S.palito(1)), FadeIn(blanq), Create(a_ent),
                      run_time=self.dur(0.9))

            # «sigue valiendo dos»
            self.en("dos")
            self.play(Create(a_sal), Create(P.base), Create(P.palito(0)), run_time=self.dur(0.7))

            # «cero menos cero coma seis por dos»
            self.en("cuenta")
            self.play(FadeIn(c1, shift=UP * 0.1), run_time=self.dur(0.8))

            # «entre cero coma ocho»
            self.en("entre")
            self.resaltar(c1[2], color=AMBAR, escala=1.1)

            # «menos uno coma cinco»
            self.en("m15")
            self.play(FadeIn(res, shift=UP * 0.1), Create(P.palito(1)), run_time=self.dur(0.6))

            # «El pulso blanqueado»
            self.en("pulsob")
            self.play(P.palito(0).animate(rate_func=there_and_back).scale(1.15), run_time=self.dur(0.5))

            # «dos, menos uno coma cinco»
            self.en("valores")
            self.play(FadeIn(etiq, shift=UP * 0.1), run_time=self.dur(0.6))

            # «sobre ruido blanco»
            self.en("sobre")
            self.play(FadeIn(circ), FadeIn(circ_l), run_time=self.dur(0.5))

            # «el filtro adaptado a ese pulso»
            self.en("adaptado")
            self.play(FadeIn(filt), Create(inv.base), Create(inv.palito(0)), Create(inv.palito(1)),
                      run_time=self.dur(0.8))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def energia(self):
        T = Tallos([2, -1.5], centro=(-4.8, 1.8), paso=1.2, unidad=0.8, color=SENAL)
        E = MathTex("E", "=", "p_0^2", "+", "p_1^2", color=TXT).scale(1.2).move_to([0.4, 2.7, 0])
        suma = MathTex("=", "4", "+", num_tex(2.25), color=TXT).scale(1.2).move_to([0.4, 1.5, 0]).align_to(E, LEFT)
        s625 = MathTex("=", num_tex(6.25), color=AMBAR).scale(1.4).move_to([0.4, 0.3, 0]).align_to(E, LEFT)
        antes = MathTex("d^2", "=", num_tex(6.25), color=INK).scale(0.95).move_to([-4.2, -1.6, 0])
        a1 = Arrow([-3.0, -1.2, 0], [-1.5, 0.0, 0], color=ESTIMACION, stroke_width=4, buff=0.05,
                   max_tip_length_to_length_ratio=0.12)
        a2 = Arrow([-3.9, 1.3, 0], [-1.5, 0.7, 0], color=CIAN, stroke_width=4, buff=0.05,
                   max_tip_length_to_length_ratio=0.12)
        igual = MathTex("=", color=VERDE).scale(1.4).move_to([-2.9, 0.1, 0])
        sin = Text("sin pérdida", color=VERDE, weight=BOLD).scale(0.6).move_to([4.2, -0.4, 0])
        ruido = Text("ruido blanco", color=RUIDO).scale(0.5)
        mem = Text("ruido con memoria", color=RUIDO).scale(0.5)
        flecha_vuelta = Arrow([4.9, -1.6, 0], [2.6, -1.6, 0], color=VERDE, stroke_width=4, buff=0.05,
                              max_tip_length_to_length_ratio=0.12)
        mem.move_to([0.9, -1.6, 0])
        ruido.move_to([5.8, -1.6, 0])
        prom = Text("promedio", color=INK).scale(0.5).move_to([1.2, -2.8, 0])
        flecha_prom = Arrow([4.8, -2.8, 0], [2.4, -2.8, 0], color=INK, stroke_width=4, buff=0.05,
                            max_tip_length_to_length_ratio=0.12)
        tach = Line([3.1, -2.5, 0], [4.3, -3.1, 0], color=ERROR, stroke_width=6)
        irrec = Text("irrecuperable", color=ERROR).scale(0.45).move_to([5.6, -2.8, 0])

        with self.narrar("b2"):
            # «Su energía»
            self.en("energia")
            self.corte()
            self.play(Create(T.base), Create(T.palito(0)), Create(T.palito(1)), FadeIn(E), run_time=self.dur(0.7))

            # «cuatro más dos coma veinticinco»
            self.en("suma")
            self.play(FadeIn(suma, shift=UP * 0.1), run_time=self.dur(0.8))

            # «seis coma veinticinco»
            self.en("s625")
            self.play(FadeIn(s625, shift=UP * 0.1), run_time=self.dur(0.5))

            # «la relación de antes»
            self.en("antes")
            self.play(FadeIn(antes, shift=UP * 0.1), run_time=self.dur(0.6))

            # «Por los dos caminos»
            self.en("caminos")
            self.play(GrowArrow(a1), GrowArrow(a2), run_time=self.dur(0.8))

            # «el mismo número»
            self.en("mismo2")
            self.pop(igual)

            # «no se pierde información»
            self.en("nopierde")
            self.pop(sin)

            # «se puede deshacer»
            self.en("deshacer")
            self.play(FadeIn(mem), FadeIn(ruido), GrowArrow(flecha_vuelta), run_time=self.dur(0.9))

            # «recuperar las originales»
            self.en("orig")
            self.resaltar(mem, color=VERDE, escala=1.15)

            # «No es como el promedio»
            self.en("promedio")
            self.play(FadeIn(prom), GrowArrow(flecha_prom), Create(tach), run_time=self.dur(0.8))

            # «lo que no se puede recuperar»
            self.en("norecup")
            self.pop(irrec)
