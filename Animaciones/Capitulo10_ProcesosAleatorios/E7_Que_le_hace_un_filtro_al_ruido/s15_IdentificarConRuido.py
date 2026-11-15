"""Escena 15 — Identificar un sistema desconocido con ruido blanco: R_yx = h."""
from comun.escena import *


class IdentificarConRuido(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        bl = BloqueLTI(r"h = ?", centro=(0.6, 1.2), ancho=2.4, alto=1.5, largo=1.5, color=INK)
        rng = np.random.default_rng(7)
        tira = tira_pm1([1 if v > 0 else -1 for v in rng.normal(size=6)], lado=0.52).move_to([-5.0, 1.2, 0])
        Ls = Lienzo(ancho=2.8, alto=1.4, t_rango=(0, 1), v_max=1.5, centro=(5.4, 1.2))
        sal = Ls.curva(np.linspace(0, 1, 120), 0.6 * serie(5, 120, 0.93), MEDIDA, 4)
        f1 = formula(r"R_{yx}", "=", "h", "*", r"R_{xx}", escala=1.3).move_to([-3.4, -0.9, 0])
        f2 = formula(r"R_{xx}", "=", r"\text{impulso}", escala=1.2).move_to([-3.4, -2.1, 0])
        f3 = formula(r"R_{yx}", "=", "h", escala=1.5, colores={2: ESTIMACION}).move_to([-3.4, -3.3, 0])
        caja_f3 = SurroundingRectangle(f3, color=AMBAR, buff=0.18, stroke_width=3)
        correlador = caja("correlación", AMBAR, ancho=3.0, alto=0.8, scale=0.5).move_to([0.6, 3.1, 0])
        l1 = Line(tira.get_top() + UP * 0.05, correlador.get_left(), color=AMBAR, stroke_width=3)
        l2 = Line(Ls.p(0.5, 0.0) + UP * 0.75, correlador.get_right(), color=AMBAR, stroke_width=3)
        est = Tallos([0.5, 0.5, 0.0], centro=(3.7, -2.2), paso=1.0, unidad=2.2, color=ESTIMACION, extra=1)
        rots = VGroup(*[MathTex(s, color=TXT).scale(0.9).move_to([est.x(i), -3.25, 0])
                        for i, s in enumerate([r"\tfrac12", r"\tfrac12", "0"])])
        prom = caja("promediador", AZUL, ancho=3.2, alto=0.7, scale=0.5).move_to([3.7, -0.4, 0])
        ok = tilde().scale(0.9).next_to(prom, RIGHT, buff=0.3)
        h_fin = Tallos([0.5, 0.5, 0.0], centro=(0.6, 1.2), paso=0.5, unidad=1.0, color=ESTIMACION)

        with self.narrar("b1"):
            # «una aplicación»
            self.en("aplicacion")
            self.play(FadeIn(bl), run_time=self.dur(0.7))

            # «La correlación cruzada»
            self.en("cruzada")
            self.play(FadeIn(f1[:2]), run_time=self.dur(0.6))

            # «hache convolucionada»
            self.en("conv")
            self.play(FadeIn(f1[2:]), run_time=self.dur(0.8))

            # «la autocorrelación de la entrada»
            self.en("de_entrada")
            self.play(f1[4].animate(rate_func=there_and_back).scale(1.3).set_color(SENAL), run_time=0.6)

            # «Si la entrada»
            self.en("si_entrada")
            self.play(FadeIn(tira, shift=RIGHT * 0.4), Create(bl.ent), Create(bl.sal), run_time=self.dur(0.7))

            # «la moneda»
            self.en("moneda")
            self.resaltar(tira, color=AMBAR, escala=1.08)

            # «un impulso»
            self.en("impulso")
            self.play(FadeIn(f2), run_time=self.dur(0.7))

            # «directamente hache»
            self.en("directo")
            self.play(FadeIn(f3), Create(caja_f3), run_time=self.dur(0.8))

            # «un medio, un medio y cero»
            self.en("tres")
            self.play(Create(est.base), *[Create(p) for p in est.tallos], *[FadeIn(p) for p in est.puntos],
                      FadeIn(rots), run_time=self.dur(1.0))

            # «justo el promediador»
            self.en("justo")
            self.play(FadeIn(prom), FadeIn(ok, scale=0.6), run_time=self.dur(0.6))

            # «un sistema desconocido»
            self.en("desconocido")
            self.resaltar(bl.caja, color=AMBAR, escala=1.1)

            # «mides la correlación»
            self.en("mides")
            self.play(FadeIn(correlador), Create(sal), Create(l1), Create(l2), run_time=self.dur(1.0))

            # «su respuesta al impulso»
            self.en("respuesta")
            self.play(FadeOut(bl.rot), FadeIn(h_fin), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
