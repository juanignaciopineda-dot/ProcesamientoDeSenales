"""Escena 09 — La covarianza del canal: 0,27 − 0,102 = 0,168."""
from comun.escena import *


class CovarianzaDelCanal(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        T = TablaCanal(centro=(-3.7, 1.2), lado=2.0, esc=0.8)
        f1 = formula(r"\sigma_{SR}", "=", "0{,}27", "-", "0{,}102", escala=1.7,
                     colores={0: AMBAR, 2: AMBAR, 4: INK}).move_to([2.6, 2.3, 0])
        f2 = formula("=", "0{,}168", escala=1.9, colores={1: AMBAR}).move_to([2.6, 0.7, 0])
        f2.align_to(f1[1], LEFT)
        oculta(f1)
        oculta(f2)
        self.add(f1, f2)
        # nube inclinada (el mismo canal visto como nube) y las dos flechas
        a, b = puntos_corr(0.8, 24, 12)
        nube = nube6((-3.2, -2.3), 0.85, 0.6, np.clip(a, -2, 2), np.clip(b, -2, 2))
        with self.narrar("b1"):
            # «Para el canal»
            self.en("canal")
            self.play(FadeIn(T.armazon()), FadeIn(T.probs()), run_time=self.dur(0.6))

            # «cero coma veintisiete»
            self.en("c27")
            self.play(*revelar(f1[0], f1[1], f1[2]), Create(T.marco(1, 1, AMBAR)), run_time=self.dur(0.7))

            # «menos cero coma uno cero dos»
            self.en("c102")
            self.play(*revelar(f1[3], f1[4]), run_time=self.dur(0.7))

            # «La covarianza entre lo enviado»
            self.en("cov_ent")
            self.resaltar(T.enc_f[1], color=AMBAR, escala=1.2)

            # «lo recibido»
            self.en("lo_rec")
            self.resaltar(T.enc_c[1], color=AMBAR, escala=1.2)

            # «cero coma uno seis ocho»
            self.en("c168")
            self.play(*revelar(*f2), run_time=self.dur(0.6))
            self.sfx("exito")

            # «Es positiva»
            self.en("positiva")
            mas = Text("+", color=VERDE, weight=BOLD).scale(3.0).move_to([5.9, 0.7, 0])
            self.pop(mas)

            # «como tenía que ser»
            self.en("como")
            ejesn = VGroup(Arrow([-5.5, -3.6, 0], [-0.8, -3.6, 0], color=INK, stroke_width=2, buff=0),
                           Arrow([-5.5, -3.6, 0], [-5.5, -0.7, 0], color=INK, stroke_width=2, buff=0))
            self.play(FadeIn(ejesn), LaggedStart(*[FadeIn(p, scale=0.4) for p in nube], lag_ratio=0.03),
                      run_time=self.dur(0.9))

            # «tienden a ir en la misma dirección»
            self.en("misma_dir")
            fs = Arrow([1.5, -3.4, 0], [1.5, -1.0, 0], color=SENAL, stroke_width=6, buff=0)
            fr = Arrow([3.3, -3.4, 0], [3.3, -1.0, 0], color=MEDIDA, stroke_width=6, buff=0)
            ts = Text("S", color=SENAL, weight=BOLD).scale(0.7).next_to(fs, UP, buff=0.1)
            tr = Text("R", color=MEDIDA, weight=BOLD).scale(0.7).next_to(fr, UP, buff=0.1)
            self.play(GrowArrow(fs), GrowArrow(fr), FadeIn(ts), FadeIn(tr), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
