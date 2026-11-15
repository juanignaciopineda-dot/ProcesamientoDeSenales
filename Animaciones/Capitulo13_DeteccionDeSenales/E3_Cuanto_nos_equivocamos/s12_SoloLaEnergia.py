"""Escena 12 — Con ruido blanco el error solo depende de E/σ²; duplicar E lo baja de 6,7 % a 1,7 %."""
import math

from comun.escena import *


def qf(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


class SoloLaEnergia(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.resultado_central()
        self.mas_energia()
        self.letra_chica()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resultado_central(self):
        central = Text("resultado central", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, 3.3, 0])
        marco = SurroundingRectangle(central, color=AMBAR, buff=0.25, stroke_width=4)
        blanco = Text("ruido blanco", color=RUIDO, weight=BOLD).scale(0.6).move_to([-4.9, 1.7, 0])
        coc = formula("E", "/", r"\sigma^2", escala=2.2).move_to([0, 1.6, 0])
        snr_t = Text("relación señal-ruido", color=TXT).scale(0.6).move_to([0, 0.4, 0])
        barra_fondo = Rectangle(width=5.0, height=0.35, color=INK, stroke_width=3).move_to([0, -0.4, 0])
        barra = Rectangle(width=2.5, height=0.35, color=ESTIMACION, stroke_width=0).set_fill(ESTIMACION, 0.8)
        barra.align_to(barra_fondo, LEFT).move_to(barra_fondo.get_left() + RIGHT * 1.25 + UP * 0)
        iguales = formula("p_0", "=", "p_1", escala=0.85, colores={0: RUIDO, 2: SENAL}).move_to([-5.2, -1.4, 0])
        pe = formula("P_e", "=", "Q", "(", r"\frac{\sqrt{E}}{2\sigma}", ")", escala=1.5,
                     colores={0: ESTIMACION}).move_to([0, -2.4, 0])
        pa = Barras((2, 2, 1), centro=(3.9, 1.7), paso=0.6, unidad=0.28, color=SENAL, ancho=0.4)
        pb = Barras((3, 0, 0), centro=(6.0, 1.7), paso=0.6, unidad=0.28, color=SENAL, ancho=0.4)
        igual = MathTex("=", color=AMBAR).scale(1.4).move_to([5.0, 1.7, 0])
        pin = VGroup(Circle(radius=0.17, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.9),
                     Line(DOWN * 0.17, DOWN * 0.6, color=AMBAR, stroke_width=4)).move_to([3.8, -1.7, 0])
        mat = interrogante13(AMBAR, 0.9).move_to([5.1, -1.7, 0])

        with self.narrar("b1"):
            # «Es el resultado central»
            self.en("central")
            self.pop(central)
            self.play(Create(marco), run_time=0.4)

            # «Con ruido blanco»
            self.en("blanco")
            self.play(FadeIn(blanco), run_time=self.dur(0.5))

            # «depende solo de un cociente»
            self.en("cociente")
            self.play(Write(coc), run_time=self.dur(1.0))

            # «la energía de la señal»
            self.en("e")
            self.play(coc[0].animate.set_color(SENAL), run_time=self.dur(0.5))

            # «la varianza del ruido»
            self.en("s2")
            self.play(coc[2].animate.set_color(RUIDO), run_time=self.dur(0.5))

            # «relación señal-ruido»
            self.en("snr")
            self.play(FadeIn(snr_t), Create(barra_fondo), FadeIn(barra), run_time=self.dur(0.8))

            # «Con probabilidades iguales»
            self.en("iguales")
            self.play(FadeIn(iguales, shift=UP * 0.1), run_time=self.dur(0.7))

            # «la probabilidad de error es cu de»
            self.en("pe")
            self.play(*[FadeIn(pe[i], shift=UP * 0.1) for i in range(4)], run_time=self.dur(0.9))

            # «la raíz de la energía entre dos sigma»
            self.en("raiz")
            self.play(*[FadeIn(pe[i], shift=UP * 0.1) for i in (4, 5)], run_time=self.dur(1.0))

            # «La forma de la señal no importa»
            self.en("forma")
            self.play(FadeIn(pa), FadeIn(pb), FadeIn(igual, scale=0.5), run_time=self.dur(0.9))

            # «Guarda esto»
            self.en("guarda")
            self.pop(pin)

            # «con ruido blanco»
            self.en("blanco2")
            self.play(blanco.animate(rate_func=there_and_back).scale(1.4), run_time=self.dur(0.7))

            # «Más adelante lo vamos a matizar»
            self.en("matizar")
            self.pop(mat)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def mas_energia(self):
        preg = Text("¿Cuánto mejora el error con más energía?", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([0, 3.5, 0])
        fondo = Rectangle(width=6.0, height=0.4, color=INK, stroke_width=3).move_to([0, 2.5, 0])
        b9 = Rectangle(width=3.0, height=0.4, stroke_width=0).set_fill(ESTIMACION, 0.8).move_to(fondo.get_left() + RIGHT * 1.5)
        b18 = Rectangle(width=6.0, height=0.4, stroke_width=0).set_fill(ESTIMACION, 0.8).move_to(fondo.get_left() + RIGHT * 3.0)
        e9 = formula("E", "=", "9", escala=0.9, colores={0: SENAL, 2: AMBAR}).next_to(fondo, LEFT, buff=0.4)
        e18 = formula("E", "=", "18", escala=0.9, colores={0: SENAL, 2: AMBAR}).next_to(fondo, LEFT, buff=0.4)
        raiz = formula(r"\frac{\sqrt{18}}{2}", escala=1.1).move_to([-4.6, 0.7, 0])
        z = formula("=", "2{,}12", escala=1.1, colores={1: AMBAR}).move_to([-2.3, 0.7, 0])
        q = formula("Q(2{,}12)", "=", "0{,}017", escala=1.1, colores={2: VERDE}).move_to([2.6, 0.7, 0])
        g7 = rejilla3(7, centro=(-3.2, -2.0), lado=0.22)
        g2 = rejilla3(2, centro=(3.2, -2.0), lado=0.22)
        t7 = Text("6,7 %", color=ERROR, weight=BOLD).scale(0.6).next_to(g7, DOWN, buff=0.15)
        t2 = Text("1,7 %", color=VERDE, weight=BOLD).scale(0.6).next_to(g2, DOWN, buff=0.15)
        flecha_v = Arrow(g7.get_right() + RIGHT * 0.2, g2.get_left() + LEFT * 0.2, color=VERDE, stroke_width=6, buff=0)

        with self.narrar("b2"):
            # «¿Cuánto mejora el error con más energía?»
            self.en("pregunta")
            self.corte()
            self.play(FadeIn(preg), run_time=self.dur(0.5))

            # «Duplicamos la energía, de nueve a dieciocho»
            self.en("dup")
            self.play(Create(fondo), FadeIn(b9), FadeIn(e9), run_time=self.dur(0.6))
            self.play(ReplacementTransform(b9, b18), ReplacementTransform(e9, e18), run_time=self.dur(1.2))

            # «La raíz de dieciocho entre dos»
            self.en("raiz")
            self.play(FadeIn(raiz, shift=UP * 0.1), run_time=self.dur(0.9))

            # «es dos coma doce»
            self.en("z")
            self.play(FadeIn(z, shift=UP * 0.1), run_time=self.dur(0.5))

            # «cu de dos coma doce vale cero coma cero uno siete»
            self.en("q")
            self.play(FadeIn(q[0], shift=UP * 0.1), FadeIn(q[1]), run_time=self.dur(0.8))

            # «cero coma cero uno siete»
            self.en("v")
            self.play(FadeIn(q[2], shift=UP * 0.1), run_time=self.dur(0.6))

            # «Con el doble de energía»
            self.en("doble")
            self.play(b18.animate(rate_func=there_and_back).set_fill(AMBAR, 1.0), run_time=self.dur(0.6))

            # «casi siete de cada cien»
            self.en("siete")
            self.play(FadeIn(g7), FadeIn(t7), run_time=self.dur(0.7))

            # «menos de dos de cada cien»
            self.en("dos")
            self.play(FadeIn(g2), FadeIn(t2), Create(flecha_v), run_time=self.dur(0.8))
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def letra_chica(self):
        xs1 = np.linspace(0.0, 4.0, 120)
        xs2 = np.linspace(0.0, 16.0, 120)
        # eje vertical logarítmico: v' = 1 + log10(Q)/5 en [0, 1]
        def vlog(q):
            return 1.0 + np.log10(np.maximum(q, 1e-5)) / 5.0
        L1 = Lienzo(ancho=8.0, alto=6.4, t_rango=(0, 4), v_max=1.0, centro=(-1.0, -2.5))
        L2 = Lienzo(ancho=8.0, alto=6.4, t_rango=(0, 16), v_max=1.0, centro=(-1.0, -2.5))
        q1 = np.array([qf(x) for x in xs1])
        q2 = np.array([qf(math.sqrt(u)) for u in xs2])
        ejes_c = VGroup(Arrow(L1.p(0, 0), L1.p(4.1, 0), buff=0, color=INK, stroke_width=3, tip_length=0.2, max_tip_length_to_length_ratio=0.1),
                        Arrow(L1.p(0, 0), L1.p(0, 1.08), buff=0, color=INK, stroke_width=3, tip_length=0.2, max_tip_length_to_length_ratio=0.1))
        y_t = Text("Q (escala logarítmica)", color=INK).scale(0.45).move_to(L1.p(0, 1.0) + UP * 0.45 + RIGHT * 0.9)
        x1_t = MathTex(r"\sqrt{E}\,/\,\sigma", color=INK).scale(0.8).move_to(L1.p(4.0, 0) + DOWN * 0.45)
        x2_t = MathTex(r"E\,/\,\sigma^2", color=INK).scale(0.8).move_to(L1.p(4.0, 0) + DOWN * 0.45)
        curva1 = traza(L1.x(xs1), L1.y(vlog(q1)), ESTIMACION, 5)
        curva2 = traza(L2.x(xs2), L2.y(vlog(q2)), ESTIMACION, 5)
        recta1 = DashedLine(L1.p(0, vlog(0.5)), L1.p(4, vlog(10 ** -3.0)), color=INK, stroke_width=3)
        recta2 = DashedLine(L2.p(0, vlog(0.5)), L2.p(16, vlog(10 ** -4.3)), color=INK, stroke_width=3)
        expo_t = Text("exponencial", color=INK).scale(0.5).move_to(L1.p(4, vlog(10 ** -3.0)) + RIGHT * 1.4)
        rapido = Text("¿más rápido que una exponencial?", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([0, 3.5, 0])
        lup = lupa(TXT).scale(0.9).move_to([5.6, 1.6, 0])
        ast = Text("*", color=AMBAR, weight=BOLD).scale(1.8).move_to([5.1, 2.2, 0])
        misma = Text("la misma curva", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.2, 2.3, 0])

        with self.narrar("b3"):
            # «más rápido que una exponencial»
            self.en("rapido")
            self.corte()
            self.play(FadeIn(rapido), run_time=self.dur(0.5))

            # «tiene letra chica»
            self.en("letra")
            self.play(FadeIn(ast), FadeIn(lup, shift=LEFT * 0.3), run_time=self.dur(0.7))

            # «la raíz de la energía entre sigma»
            self.en("eje1")
            self.play(FadeOut(lup), FadeOut(ast), Create(ejes_c), FadeIn(y_t), FadeIn(x1_t), run_time=self.dur(0.8))

            # «cu cae como una campana»
            self.en("campana")
            self.play(Create(curva1), run_time=self.dur(1.2))

            # «más deprisa que cualquier exponencial»
            self.en("deprisa")
            self.play(Create(recta1), FadeIn(expo_t), run_time=self.dur(0.9))

            # «Como función de la relación señal-ruido»
            self.en("eje2")
            self.play(ReplacementTransform(x1_t, x2_t), FadeOut(expo_t), run_time=self.dur(0.6))
            self.play(ReplacementTransform(curva1, curva2), ReplacementTransform(recta1, recta2), run_time=self.dur(1.0))

            # «la energía entre la varianza»
            self.en("ev")
            self.play(x2_t.animate(rate_func=there_and_back).scale(1.4), run_time=self.dur(0.7))

            # «cae esencialmente como una exponencial»
            self.en("expo")
            self.play(curva2.animate(rate_func=there_and_back).set_stroke(width=9), run_time=self.dur(0.9))

            # «dos formas de mirar la misma curva»
            self.en("misma")
            self.pop(misma)
        self.wait(0.3)
