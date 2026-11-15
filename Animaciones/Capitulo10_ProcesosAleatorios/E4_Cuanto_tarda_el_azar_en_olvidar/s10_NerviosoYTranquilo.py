"""Escena 10 — NerviosoYTranquilo: la velocidad de olvido es 2λ."""
from comun.escena import *


class NerviosoYTranquilo(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        Lm = Lienzo(ancho=8.4, alto=2.6, t_rango=(0, 2.5), v_max=1.1, centro=(0.6, -1.3))
        tau = np.linspace(0, 2.5, 200)
        mem = lambda lam: np.exp(-2 * lam * tau)
        rng = np.random.default_rng(3)
        t_n = list(np.cumsum(rng.exponential(1 / 5, 40)))
        Lw1 = Lienzo(ancho=6.0, alto=0.95, t_rango=(0, 6), v_max=1.3, centro=(-2.3, 3.15))
        Lw2 = Lienzo(ancho=6.0, alto=0.95, t_rango=(0, 6), v_max=1.3, centro=(-2.3, 1.75))
        nerv = onda_tel(Lw1, t_n, 1, ROJO, 2.5)
        tranq = onda_tel(Lw2, [2.6, 5.1], 1, VERDE, 3.0)
        l_n = MathTex(r"\lambda=5", color=ROJO).scale(0.9).move_to([3.2, 3.15, 0])
        l_t = MathTex(r"\lambda=\tfrac14", color=VERDE).scale(0.9).move_to([3.2, 1.75, 0])
        base_m = Lm.base()
        eje_m = Line(Lm.p(0, -0.05), Lm.p(0, 1.08), color=INK, stroke_width=2)
        rot_tau = MathTex(r"\tau", color=INK).scale(0.6).next_to(Lm.p(2.5, 0), DR, buff=0.1)
        c1 = Lm.curva(tau, mem(1), SENAL, 4.5)
        c5 = Lm.curva(tau, mem(5), ROJO, 5)
        c25 = Lm.curva(tau, mem(0.25), VERDE, 5)
        t_c1 = MathTex(r"\lambda=1", color=SENAL).scale(0.8).move_to(Lm.p(1.0, 0.44) + RIGHT * 0.5)
        x5 = etiqueta("5 veces más deprisa", ROJO, 0.5).move_to([4.6, 0.25, 0])
        d7 = Dot(Lm.p(0.5, float(np.exp(-5))), radius=0.11, color=ROJO)
        r7 = etiqueta("0,007", ROJO, 0.6, BOLD).next_to(d7, UR, buff=0.25)
        d78 = Dot(Lm.p(0.5, float(np.exp(-0.25))), radius=0.11, color=VERDE)
        r78 = etiqueta("0,78", VERDE, 0.6, BOLD).next_to(d78, UR, buff=0.15)
        vel = MathTex(r"\text{velocidad de olvido}=2\lambda", color=AMBAR).scale(1.0).move_to([3.4, -3.35, 0])
        baja = Arrow(Lm.p(0.12, 1.0) + UP * 0.25, Lm.p(0.4, 0.85) + UP * 0.25, color=AMBAR, buff=0, stroke_width=5)
        t_olv = etiqueta("olvida", AMBAR, 0.55, BOLD).next_to(baja, UP, buff=0.05)

        with self.narrar("b1"):
            # «más nervioso»
            self.en("nervioso")
            self.play(Create(Lw1.base()), Create(nerv), FadeIn(l_n), run_time=self.dur(1.6))
            self.play(Create(base_m), Create(eje_m), FadeIn(rot_tau), run_time=0.4)
            self.play(Create(c1), FadeIn(t_c1), run_time=0.6)

            # «cinco cambios por segundo»
            self.en("cinco")
            self.play(Create(c5), run_time=self.dur(1.0))

            # «cae cinco veces más deprisa»
            self.en("cae5")
            self.play(FadeIn(x5), run_time=0.4)
            self.resaltar(c5, color=AMBAR, escala=1.03)

            # «siete milésimas»
            self.en("v007")
            self.play(FadeIn(d7, scale=0.5), FadeIn(r7), run_time=0.4)

            # «un cambio cada cuatro segundos»
            self.en("tranquilo")
            self.play(Create(Lw2.base()), Create(tranq), FadeIn(l_t), run_time=self.dur(1.0))
            self.play(Create(c25), run_time=self.dur(1.0))

            # «cero coma siete ocho»
            self.en("v078")
            self.play(FadeIn(d78, scale=0.5), FadeIn(r78), run_time=0.4)

            # «Dos lambda es la velocidad»
            self.en("velocidad")
            self.pop(vel)

            # «a la que el proceso olvida»
            self.en("olvida")
            self.play(Create(baja), FadeIn(t_olv), run_time=self.dur(0.7))

            # «olvida deprisa»
            self.en("deprisa")
            self.resaltar(c5, color=AMBAR, escala=1.03)

            # «uno tranquilo, despacio»
            self.en("despacio")
            self.resaltar(c25, color=AMBAR, escala=1.03)
        self.wait(1.0)
        self.limpiar()
