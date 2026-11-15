"""Escena 01 — Gancho: el interruptor que olvida (0,37 a medio segundo, 0,02 a dos)."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        Lo = Lienzo(ancho=9.0, alto=1.5, t_rango=(0, 6), v_max=1.3, centro=(1.3, 2.4))
        Lm = Lienzo(ancho=8.0, alto=2.6, t_rango=(0, 2.5), v_max=1.1, centro=(1.3, -1.2))
        tau = np.linspace(0, 2.5, 160)
        memoria = lambda t: np.exp(-2 * t)
        sw = interruptor().scale(1.1).move_to([-5.5, 2.4, 0])
        onda = onda_tel(Lo, CAMBIOS, 1, AMBAR, 4)
        base_o = Lo.base()
        eje_m = Line(Lm.p(0, -0.08), Lm.p(0, 1.05), color=INK, stroke_width=2)
        base_m = Lm.base()
        rot_tau = MathTex(r"\tau", color=INK).scale(0.6).next_to(Lm.p(2.5, 0), DR, buff=0.1)
        m1 = Lo.vertical(1.0, AMBAR, 3, mitad=0.75)
        m2 = Lo.vertical(1.5, AMBAR, 3, mitad=0.75)
        llave = BraceBetweenPoints(Lo.p(1.5, -0.75), Lo.p(1.0, -0.75), color=AMBAR)
        r05 = etiqueta("0,5 s", AMBAR, 0.5).next_to(llave, DOWN, buff=0.05)
        d1 = Dot(Lm.p(0.5, memoria(0.5)), radius=0.12, color=AMBAR)
        v1 = etiqueta("0,37", AMBAR, 0.7, BOLD).next_to(d1, UR, buff=0.15)
        d2 = Dot(Lm.p(2.0, memoria(2.0)), radius=0.12, color=AMBAR)
        v2 = etiqueta("0,02", AMBAR, 0.7, BOLD).next_to(d2, UP, buff=0.5)

        with self.narrar("b1"):
            # «Un interruptor»
            self.en("interruptor")
            self.pop(sw)

            # «salta al azar»
            self.en("salta")
            self.play(Create(base_o), Create(onda), run_time=self.dur(1.6), rate_func=linear)

            # «Medio segundo después»
            self.en("medio")
            self.play(Create(m1), Create(m2), FadeIn(llave), FadeIn(r05), run_time=self.dur(0.7))
            self.play(Create(base_m), Create(eje_m), FadeIn(rot_tau), run_time=0.4)

            # «treinta y siete por ciento»
            self.en("p37")
            parte = Lm.curva(tau[tau <= 0.5], memoria(tau[tau <= 0.5]), SENAL, 5)
            self.play(Create(parte), run_time=0.6)
            self.play(FadeIn(d1, scale=0.5), FadeIn(v1), run_time=0.4)

            # «Dos segundos después»
            self.en("dos")
            self.play(m2.animate.shift(RIGHT * float(Lo.x(3.0) - Lo.x(1.5))),
                      llave.animate.stretch_to_fit_width(float(Lo.x(3.0) - Lo.x(1.0)), about_point=Lo.p(1.0, -0.75)),
                      FadeOut(r05), run_time=self.dur(0.8))

            # «un dos por ciento»
            self.en("p2")
            seguir = Lm.curva(tau[(tau >= 0.5) & (tau <= 2.0)], memoria(tau[(tau >= 0.5) & (tau <= 2.0)]), SENAL, 5)
            self.play(Create(seguir), run_time=self.dur(0.9))
            self.play(FadeIn(d2, scale=0.5), FadeIn(v2), run_time=0.4)

            # «olvida el azar»
            self.en("olvida")
            resto = Lm.curva(tau[tau >= 2.0], memoria(tau[tau >= 2.0]), SENAL, 5)
            self.play(Create(resto), run_time=self.dur(0.6))
            self.resaltar(seguir, color=AMBAR, escala=1.03)
        self.wait(0.6)
        self.limpiar()
