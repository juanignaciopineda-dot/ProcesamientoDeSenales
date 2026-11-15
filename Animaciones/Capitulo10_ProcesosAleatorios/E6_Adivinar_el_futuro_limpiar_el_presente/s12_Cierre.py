"""Escena 12 — Cierre: un filtro ya diseñado, ¿qué le hace a un proceso que pasa por él? (anuncia el E7)."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        css = Palitos([0, 1], [4, 2.4], ancho=2.2, alto=1.2, v_max=5.0, color=SENAL, centro=(-4.7, 2.5))
        cdd = Palitos([0, 1], [1, 0.0], ancho=2.2, alto=1.2, v_max=5.0, color=RUIDO, centro=(-1.9, 2.5))
        for p_ in (css, cdd):
            p_.remove(p_.eje)
        caja_h = caja("h", AMBAR, ancho=1.6, alto=1.2, scale=0.9).move_to([0, -0.4, 0])
        Lin = Lienzo(ancho=4.0, alto=1.6, t_rango=(0, 1), v_max=2.6, centro=(-4.6, -0.4))
        Lout = Lienzo(ancho=4.0, alto=1.6, t_rango=(0, 1), v_max=2.6, centro=(4.6, -0.4))
        t = np.linspace(0, 1, 200)
        ruido = np.random.default_rng(11).normal(0, 1, 200)
        suave = np.convolve(ruido, np.ones(6) / 6, mode="same") * 1.6
        c_in = Lin.curva(t, ruido, RUIDO, 2.5)
        c_out = Lout.curva(t, suave, MEDIDA, 3.2)
        e_in = Arrow([-2.4, -0.4, 0], [-0.95, -0.4, 0], buff=0, color=INK, stroke_width=4)
        e_out = Arrow([0.95, -0.4, 0], [2.4, -0.4, 0], buff=0, color=INK, stroke_width=4)
        chips = VGroup(*[caja(txt, AMBAR, alto=0.65, scale=0.5) for txt in ("media", "memoria", "varianza")])
        chips.arrange(RIGHT, buff=0.25).move_to([3.4, 1.5, 0])
        fin_ = Text("7 / 7", color=INK).scale(0.5).move_to([6.3, 3.6, 0])
        titulo_ = self.texto_centrado("¿Qué le hace un", "filtro al ruido?", color=AMBAR, escala=1.4).move_to([0, 0, 0])

        with self.narrar("b1"):
            # «solo las autocorrelaciones»
            self.en("auto")
            self.play(FadeIn(css), FadeIn(cdd), run_time=0.7)

            # «una vez que existe»
            self.en("existe")
            self.pop(caja_h)

            # «un proceso aleatorio que pasa por él»
            self.en("pasa")
            self.play(Create(c_in), Create(e_in), run_time=0.8)
            self.play(Create(e_out), Create(c_out), run_time=self.dur(1.0))

            # «su media, con su memoria, con su varianza»
            self.en("tres")
            self.play(FadeIn(chips, lag_ratio=0.3), run_time=self.dur(1.2))

            # «el último episodio»
            self.en("ultimo")
            self.play(FadeIn(fin_), run_time=0.4)

            # «¿Qué le hace un filtro al ruido?»
            self.en("titulo")
            self.play(*[FadeOut(m) for m in list(self.mobjects) if m is not self.camera.frame], run_time=0.3)
            self.pop(titulo_)
        self.wait(1.0)
        self.limpiar()
