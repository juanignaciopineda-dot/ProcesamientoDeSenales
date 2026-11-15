"""Escena 07 — Con aviones raros (p1 = 0,2) el umbral sube a 5,886: menos falsas alarmas, más fallos."""
from comun.escena import *


class UmbralMasAlto(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.L = lienzo_g3(centro=(0.0, -1.3))
        L = self.L
        self.base = eje_g3(L, marcas=(0, 9))
        self.cam0 = dens3(L, 0, 3, RUIDO)
        self.cam1 = dens3(L, 9, 3, SENAL)
        self.umb = umbral3(L, 4.5, alto=2.1)
        self.cola_d = cola3(L, 0, 3, 5.886, 17)
        self.cola_i = cola3(L, 9, 3, -8, 5.886)
        self.nuevo_umbral()
        self.falsa_alarma()
        self.fallo()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def nuevo_umbral(self):
        L = self.L
        ant = antena(TXT).scale(1.3).move_to([-5.4, 0.8, 0])
        cielo = casillas(10, rojas=(6,), centro=(0.8, 1.0), lado=0.55, color=INK, color_rojo=SENAL)
        avion_i = avion(AZUL).scale(0.5).move_to(cielo.cas[6].get_center())
        raros = Text("aviones raros", color=TXT).scale(0.6).move_to([0.8, 2.1, 0])
        p1 = formula("p_1", "=", "0{,}2", escala=1.2, colores={0: SENAL, 2: AMBAR}).move_to([-1.2, -1.0, 0])
        p0 = formula("p_0", "=", "0{,}8", escala=1.2, colores={0: RUIDO, 2: AMBAR}).move_to([3.0, -1.0, 0])
        sube = formula(r"\gamma:", "4{,}5", r"\to", "5{,}886", escala=1.3,
                       colores={0: ESTIMACION, 3: AMBAR}).move_to([0.8, -2.8, 0])
        pfa = MathTex("P_{FA}", color=ERROR).scale(0.85).move_to(L.p(8.0, 0) + DOWN * 0.9)
        pm = MathTex("P_M", color=ERROR).scale(0.85).move_to(L.p(2.2, 0) + DOWN * 0.9)

        with self.narrar("b1"):
            # «Volvamos al radar»
            self.en("radar")
            self.play(FadeIn(ant), run_time=self.dur(0.4))
            self.play(Create(ant.ondas.set_color(TXT)), run_time=self.dur(0.3))

            # «los aviones son raros»
            self.en("raros")
            self.play(FadeIn(cielo), FadeIn(raros), run_time=self.dur(0.6))
            self.play(FadeIn(avion_i, scale=0.5), run_time=self.dur(0.4))

            # «pe uno igual a cero coma dos»
            self.en("p1")
            self.play(FadeIn(p1, shift=UP * 0.1), FadeIn(p0, shift=UP * 0.1), run_time=self.dur(0.8))

            # «el umbral sube a cinco coma ocho ocho seis»
            self.en("sube")
            self.play(*[FadeIn(sube[i], shift=UP * 0.1) for i in range(4)], run_time=self.dur(1.2))

            # «En las dos campanas»
            self.en("campanas")
            self.corte()
            self.play(FadeIn(self.base), Create(self.cam0), Create(self.cam1), FadeIn(self.umb), run_time=self.dur(0.8))

            # «la marca se desplaza hacia la derecha»
            self.en("marca")
            self.play(self.umb.animate.shift(RIGHT * (L.x(5.886) - L.x(4.5))), run_time=self.dur(1.4))

            # «qué le pasa a cada error»
            self.en("cada")
            self.play(FadeIn(self.cola_d), FadeIn(self.cola_i), FadeIn(pfa), FadeIn(pm), run_time=self.dur(0.8))
        self.pfa, self.pm = pfa, pm
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def falsa_alarma(self):
        L = self.L
        cuenta = formula(r"\frac{5{,}886}{3}", "=", "1{,}962", escala=1.0, colores={2: AMBAR}).move_to([-3.0, 3.1, 0])
        q = formula("P_{FA}", "=", "Q(1{,}962)", "=", "0{,}0249", escala=1.0,
                    colores={0: ERROR, 4: AMBAR}).move_to([2.6, 3.1, 0])
        vieja = cola3(L, 0, 3, 4.5, 17, opacidad=0.22)
        v67 = Text("6,7 %", color=ERROR).scale(0.6).move_to([-5.3, 1.4, 0])
        tacha = Line(v67.get_corner(DL), v67.get_corner(UR), color=ERROR, stroke_width=5)
        v25 = Text("2,5 %", color=VERDE, weight=BOLD).scale(0.7).move_to([-5.3, 0.5, 0])
        intento = Dot(L.p(1.0, 0), radius=0.1, color=RUIDO)

        with self.narrar("b2"):
            # «La falsa alarma»
            self.en("fa")
            self.play(self.cola_d.animate(rate_func=there_and_back).set_fill(ERROR, 0.95), run_time=self.dur(0.7))

            # «cinco coma ocho ocho seis entre tres»
            self.en("cuenta")
            self.play(FadeIn(cuenta[0], shift=UP * 0.1), run_time=self.dur(0.8))

            # «uno coma nueve seis dos»
            self.en("z")
            self.play(FadeIn(cuenta[1]), FadeIn(cuenta[2], shift=UP * 0.1), run_time=self.dur(0.6))

            # «Cu de eso vale cero coma cero dos cuatro nueve»
            self.en("q")
            self.play(*[FadeIn(q[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(1.0))

            # «cero coma cero dos cuatro nueve»
            self.en("v")
            self.play(*[FadeIn(q[i], shift=UP * 0.1) for i in (3, 4)], run_time=self.dur(0.8))

            # «Bajó de casi siete por ciento»
            self.en("bajo")
            self.play(FadeIn(vieja), FadeIn(v67), run_time=self.dur(0.6))
            self.play(Create(tacha), run_time=self.dur(0.3))

            # «a poco más de dos y medio»
            self.en("dosmedio")
            self.pop(v25)

            # «es más difícil que el ruido solo lo cruce»
            self.en("dificil")
            self.play(FadeIn(intento), run_time=0.2)
            self.play(intento.animate.move_to(L.p(5.0, 0)), run_time=self.dur(0.8))
            self.play(intento.animate.move_to(L.p(1.0, 0)), run_time=self.dur(0.5))
        self.wait(0.3)
        self.limpia_b2 = [cuenta, q, vieja, v67, tacha, v25, intento]

    # ------------------------------------------------------------ b3
    def fallo(self):
        L = self.L
        cuenta = formula(r"\frac{9-5{,}886}{3}", "=", "1{,}038", escala=1.0, colores={2: AMBAR}).move_to([-3.0, 3.1, 0])
        q = formula("P_M", "=", "Q(1{,}038)", "=", "0{,}1497", escala=1.0,
                    colores={0: ERROR, 4: AMBAR}).move_to([2.6, 3.1, 0])
        v15 = Text("15 %", color=ERROR, weight=BOLD).scale(0.7).move_to([-5.5, 1.3, 0])
        gs = [7.0, 8.4, 9.6, 11.0, 5.2, 4.6]
        puntos = VGroup(*[Dot(L.p(g, 0), radius=0.1, color=SENAL) for g in gs])
        cons = Text("más conservador", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([-4.0, 2.1, 0])
        pierde = VGroup(Text("falsas alarmas ↓", color=VERDE).scale(0.5),
                        Text("misses ↑", color=ERROR).scale(0.5)).arrange(DOWN, buff=0.2).move_to([-3.3, 0.6, 0])

        with self.narrar("b3"):
            # «El fallo»
            self.en("fallo")
            self.play(*[FadeOut(m) for m in self.limpia_b2], run_time=self.dur(0.4))
            self.play(self.cola_i.animate(rate_func=there_and_back).set_fill(ERROR, 0.95), run_time=self.dur(0.6))

            # «nueve menos cinco coma ocho ocho seis»
            self.en("cuenta")
            self.play(FadeIn(cuenta[0], shift=UP * 0.1), run_time=self.dur(1.0))

            # «uno coma cero tres ocho»
            self.en("z")
            self.play(FadeIn(cuenta[1]), FadeIn(cuenta[2], shift=UP * 0.1), run_time=self.dur(0.6))

            # «Cu de eso vale cero coma uno cuatro nueve siete»
            self.en("q")
            self.play(*[FadeIn(q[i], shift=UP * 0.1) for i in range(3)], run_time=self.dur(1.0))

            # «cero coma uno cuatro nueve siete»
            self.en("v")
            self.play(*[FadeIn(q[i], shift=UP * 0.1) for i in (3, 4)], run_time=self.dur(0.8))

            # «Subió a un quince por ciento»
            self.en("subio")
            self.pop(v15)

            # «la señal, que sí estaba»
            self.en("estaba")
            self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in puntos], lag_ratio=0.1), run_time=self.dur(0.8))

            # «se queda a veces por debajo»
            self.en("debajo")
            self.play(puntos[4].animate.set_color(ERROR), puntos[5].animate.set_color(ERROR), run_time=self.dur(0.6))

            # «Un detector más conservador»
            self.en("conserv")
            self.pop(cons)

            # «da menos falsas alarmas y pierde más aviones»
            self.en("pierde")
            self.play(FadeIn(pierde, shift=UP * 0.1), run_time=self.dur(0.8))
        self.wait(0.3)
