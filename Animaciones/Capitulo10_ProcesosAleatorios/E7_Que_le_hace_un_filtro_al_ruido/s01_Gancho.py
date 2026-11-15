"""Escena 01 — Gancho: ruido en una caja desconocida; una correlación revela su respuesta al impulso."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        bl = BloqueLTI(r"h = ?", centro=(0.6, 0.3), ancho=2.4, alto=1.5, largo=1.5)
        rng = np.random.default_rng(7)
        tira = tira_pm1([1 if v > 0 else -1 for v in rng.normal(size=6)], lado=0.52).move_to([-5.0, 0.3, 0])
        Ls = Lienzo(ancho=2.8, alto=1.4, t_rango=(0, 1), v_max=1.5, centro=(5.4, 0.3))
        t = np.linspace(0, 1, 120)
        sal = Ls.curva(t, 0.6 * serie(5, 120, 0.93), MEDIDA, 4)
        correlador = caja("correlación", AMBAR, ancho=3.0, alto=0.8, scale=0.5).move_to([0.6, 2.9, 0])
        l1 = Line(tira.get_top() + UP * 0.05, correlador.get_left(), color=AMBAR, stroke_width=3)
        l2 = Line(Ls.p(0.5, 0.0) + UP * 0.75, correlador.get_right(), color=AMBAR, stroke_width=3)
        eje = Tallos([0.5, 0.5, 0.0], centro=(0.6, -2.5), paso=0.9, unidad=1.6, color=ESTIMACION, extra=1)
        rots = VGroup(*[MathTex(s, color=TXT).scale(0.7).move_to([eje.x(i), -3.45, 0])
                        for i, s in enumerate([r"\tfrac12", r"\tfrac12", "0"])])
        h_fin = Tallos([0.5, 0.5, 0.0], centro=(0.6, 0.3), paso=0.45, unidad=0.9, color=ESTIMACION)

        with self.narrar("b1"):
            # «Metes ruido puro»
            self.en("ruido")
            self.play(FadeIn(tira, shift=RIGHT * 0.4), run_time=self.dur(0.5))
            self.play(Create(bl.ent), run_time=self.dur(0.4))

            # «una caja que no conoces»
            self.en("caja")
            self.play(FadeIn(bl.caja), FadeIn(bl.rot), Create(bl.sal), run_time=self.dur(0.6))

            # «que no conoces»
            self.en("desconocida")
            self.resaltar(bl.caja, color=AMBAR, escala=1.1)

            # «una sola correlación»
            self.en("correl")
            self.pop(correlador)

            # «entre lo que entra y lo que sale»
            self.en("entra_sale")
            self.play(Create(sal), Create(l1), Create(l2), run_time=self.dur(0.9))

            # «aparece, entera»
            self.en("aparece")
            self.play(Create(eje.base), *[Create(p) for p in eje.tallos], *[FadeIn(p) for p in eje.puntos],
                      FadeIn(rots), run_time=self.dur(0.8))

            # «la respuesta al impulso de la caja»
            self.en("impulso")
            self.play(FadeOut(bl.rot), FadeIn(h_fin), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
