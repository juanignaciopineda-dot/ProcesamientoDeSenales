"""Escena 03 — Qué es un estado: Wiener parte de espectros, Kalman de un modelo de cómo nace la señal."""
from comun.escena import *


def recuadro(color, x, y):
    return RoundedRectangle(corner_radius=0.12, width=3.4, height=2.4, color=color, stroke_width=2.5
                            ).set_fill(color, 0.08).move_to([x, y, 0])


class EstadoDeUnSistema(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        q = Text("?", color=AMBAR, weight=BOLD).scale(2.2)
        qc = Text("?", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.3, 0])
        rw = recuadro(AZUL, -3.6, 1.6)
        lw = etiqueta("Wiener", AZUL, 0.55, BOLD).move_to([-3.6, 2.45, 0])
        L = Lienzo(ancho=2.6, alto=0.9, t_rango=(0, 1), v_max=1.0, centro=(-3.6, 1.2))
        e1 = curva_f(L, lambda u: 0.15 + 0.8 * np.exp(-((u - 0.3) / 0.2) ** 2), 0, 1, AZUL, 3.5)
        e2 = curva_f(L, lambda u: 0.9 - 0.7 * np.exp(-((u - 0.6) / 0.2) ** 2), 0, 1, CIAN, 3.5)
        rk = recuadro(AMBAR, 3.6, 1.6)
        da = DoubleArrow([-1.7, 1.6, 0], [1.7, 1.6, 0], color=INK, stroke_width=3, buff=0,
                         max_tip_length_to_length_ratio=0.15)
        mp = etiqueta("mismo problema", INK, 0.42).move_to([0, 2.1, 0])
        w = MathTex("w", color=RUIDO).scale(0.8).move_to([2.35, 1.2, 0])
        sis = caja("sistema", AZUL, ancho=1.3, alto=0.6, scale=0.4).move_to([3.6, 1.2, 0])
        y = MathTex("y", color=SENAL).scale(0.8).move_to([4.85, 1.2, 0])
        ar1 = flecha([2.6, 1.2, 0], [2.95, 1.2, 0])
        ar2 = flecha([4.25, 1.2, 0], [4.6, 1.2, 0])
        est = etiqueta("espacio de estados", AMBAR, 0.5, BOLD).move_to([3.6, 2.45, 0])
        conj = MathTex("q_1,\\ q_2,\\ \\dots", color=AMBAR).scale(0.95).move_to([0, -0.4, 0])
        rec = etiqueta("lo que el sistema recuerda", INK, 0.45).move_to([0, -1.1, 0])
        coh = cohete().scale(1.0).move_to([-3.6, -2.4, 0])
        pos = etiqueta("posición", TXT, 0.5).move_to([-1.6, -2.1, 0])
        vel = etiqueta("velocidad", TXT, 0.5).move_to([-1.6, -2.75, 0])
        term = termometro(1.2).move_to([2.4, -2.4, 0])
        qq = MathTex("q", color=AMBAR).scale(1.0).move_to([3.5, -2.4, 0])
        uno = etiqueta("un solo número", INK, 0.45).move_to([5.0, -2.4, 0])
        with self.narrar("b1"):
            # «la sorpresa»
            self.en("sorpresa")
            self.pop(q)
            # «El filtro de Wiener»
            self.en("wiener")
            self.play(Transform(q, qc), FadeIn(rw), FadeIn(lw), run_time=self.dur(0.7))
            # «parte de espectros»
            self.en("espectros")
            self.play(Create(e1), Create(e2), run_time=self.dur(0.9))
            # «La otra forma de ver el mismo problema»
            self.en("otra")
            self.play(FadeIn(rk), GrowArrow(da), FadeIn(mp), run_time=self.dur(0.8))
            # «un modelo de cómo nace la señal»
            self.en("modelo")
            self.play(FadeIn(w), FadeIn(sis), FadeIn(y), GrowArrow(ar1), GrowArrow(ar2), run_time=self.dur(1.0))
            # «espacio de estados»
            self.en("estados")
            self.pop(est)
            # «el conjunto de números»
            self.en("conjunto")
            self.play(FadeIn(conj, shift=UP * 0.3), run_time=self.dur(0.6))
            # «lo que el sistema recuerda»
            self.en("recuerda")
            self.play(FadeIn(rec), run_time=self.dur(0.5))
            # «un cohete»
            self.en("cohete")
            self.play(FadeIn(coh, shift=UP * 0.3), run_time=self.dur(0.6))
            # «la posición y la velocidad»
            self.en("posvel")
            self.play(FadeIn(pos), FadeIn(vel), run_time=self.dur(0.6))
            # «solo un número»
            self.en("uno")
            self.play(FadeIn(term), FadeIn(qq), run_time=self.dur(0.6))
            self.play(FadeIn(uno), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
