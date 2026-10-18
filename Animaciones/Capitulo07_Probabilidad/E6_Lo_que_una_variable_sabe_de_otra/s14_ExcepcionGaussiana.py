"""Escena 14 — La excepción: si las dos son gaussianas, covarianza cero sí es independencia."""
from comun.escena import *


class ExcepcionGaussiana(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        a, b = puntos_corr(0.0, 60, 3)
        nube = nube6((-3.0, -0.4), 0.9, 0.7, np.clip(a, -2.2, 2.2), np.clip(b, -2.2, 2.2))
        arriba = campana_mini(centro=(-3.0, 2.1), ancho=3.8, alto=1.0, color=SENAL)
        derecha = campana_mini(centro=(0.2, -0.4), ancho=3.0, alto=0.9, color=MEDIDA).rotate(-PI / 2)
        L = Lienzo(ancho=4.0, alto=1.3, t_rango=(0, 1), v_max=1.0, centro=(3.0, -2.5))
        ruido = ruido_t(L, semilla=5, amp=0.6)
        c_ruido = campana_mini(centro=(6.0, -2.5), ancho=1.0, alto=0.9, color=RUIDO)
        with self.narrar("b1"):
            # «Hay una excepción»
            self.en("excepcion")
            w = self.palabra("Excepción", AMBAR, 0.95).move_to([1.0, 3.4, 0])
            self.pop(w)

            # «muy importante para nosotros»
            self.en("importante")
            self.resaltar(w, color=TXT, escala=1.1)

            # «Si las dos variables»
            self.en("si_dos")
            self.play(Create(arriba), Create(derecha), run_time=self.dur(0.8))

            # «gaussianas a la vez»
            self.en("gauss")
            self.play(LaggedStart(*[FadeIn(p, scale=0.4) for p in nube], lag_ratio=0.02),
                      run_time=self.dur(1.2))

            # «covarianza cero»
            self.en("cov_cero2")
            c0 = formula(r"\sigma_{XY}", "=", "0", escala=1.7, colores={0: AMBAR, 2: AMBAR}).move_to([4.2, 1.8, 0])
            self.pop(c0)

            # «independencia»
            self.en("indep2")
            fl = MathTex(r"\Rightarrow", color=VERDE).scale(1.6)
            txt = Text("Independientes", color=TXT, weight=BOLD).scale(0.75)
            fila = VGroup(fl, txt).arrange(RIGHT, buff=0.3).move_to([3.7, 0.4, 0])
            ok = tilde(VERDE, 0.5).next_to(fila, RIGHT, buff=0.15)
            self.play(FadeIn(fila, shift=RIGHT * 0.2), Create(ok), run_time=self.dur(0.7))
            self.sfx("exito")

            # «el ruido suele ser gaussiano»
            self.en("ruido")
            self.play(Create(L.base()), Create(ruido), Create(c_ruido), run_time=self.dur(1.0))

            # «la vamos a usar muchísimo»
            self.en("usar")
            estrella = Star(n=5, outer_radius=0.32, color=AMBAR, fill_opacity=1, stroke_width=0).move_to([-1.9, 3.4, 0])
            self.pop(estrella)

            # «es una excepción»
            self.en("solo_gauss")
            nota_g = Text("Solo si ambas son gaussianas", color=AMBAR).scale(0.7).move_to([0, -3.7, 0])
            self.play(FadeIn(nota_g, shift=UP * 0.2), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
