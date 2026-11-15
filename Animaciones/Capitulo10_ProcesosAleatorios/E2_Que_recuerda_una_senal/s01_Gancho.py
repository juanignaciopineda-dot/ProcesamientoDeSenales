"""Escena 01 — Gancho: los cuatro osciladores y la moneda tienen la misma media (cero); ¿en qué se distinguen?"""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        cos = CuatroCosenos(ancho=8.0, paso=0.8, amp=0.3, centro=(0.8, 1.7))
        rng = np.random.default_rng(4)
        tira = tira_pm1(rng.choice([-1, 1], 11), lado=0.66).move_to([0.8, -1.5, 0])

        with self.narrar("b1"):
            # «Cuatro señales»
            self.en("cuatro")
            self.play(Create(VGroup(*cos.bases)), FadeIn(cos.rotulos), run_time=self.dur(0.5))

            # «suben y bajan sin parar»
            self.en("suben")
            self.play(LaggedStart(*[Create(c) for c in cos.curvas], lag_ratio=0.15),
                      run_time=self.dur(1.5), rate_func=linear)

            # «su media es cero»
            self.en("media0")
            planas = [Line(b.get_start(), b.get_end(), color=AMBAR, stroke_width=5) for b in cos.bases]
            mu = formula(r"\mu", "=", "0", colores={0: AMBAR}, escala=1.0).move_to([6.0, 1.7, 0])
            self.play(LaggedStart(*[Create(p) for p in planas], lag_ratio=0.1), run_time=self.dur(0.7))
            self.pop(mu)

            # «Una moneda»
            self.en("moneda")
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in tira.celdas], lag_ratio=0.12),
                      run_time=self.dur(2.0))

            # «su media también es cero»
            self.en("media0b")
            plana2 = Line(tira.get_left() + LEFT * 0.1, tira.get_right() + RIGHT * 0.1, color=AMBAR, stroke_width=5)
            mu2 = formula(r"\mu", "=", "0", colores={0: AMBAR}, escala=1.0).move_to([6.0, -1.5, 0])
            self.play(Create(plana2), run_time=self.dur(0.6))
            self.pop(mu2)

            # «¿Cómo distinguirlas?»
            self.en("pregunta")
            q = Text("=  ?", color=TXT, weight=BOLD).scale(1.3).move_to([0.8, -0.3, 0])
            self.pop(q)

            # «lo que recuerdan»
            self.en("recuerdan")
            self.play(Create(tachar(q)), run_time=0.3)
            rec = self.palabra("recuerdan", AMBAR, 1.3).move_to([0.8, -3.2, 0])
            self.pop(rec)

        self.wait(1.0)
        self.limpiar()
