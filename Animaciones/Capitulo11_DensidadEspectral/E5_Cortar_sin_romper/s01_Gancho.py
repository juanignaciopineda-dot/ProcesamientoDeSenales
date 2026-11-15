"""Escena 01 — Gancho: un tono cortado mal abre faldas que tapan a otro tono un millón de veces más débil."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        Lt = Lienzo(ancho=9.0, alto=1.7, t_rango=(0, 1), v_max=1.2, centro=(-0.8, 2.5))
        t = np.linspace(0, 1, 400)
        tono = Lt.curva(t, np.cos(2 * np.pi * 8.5 * t), SENAL, 3.5)
        Lf = lienzo_f(4, 15, 2.0, ancho=9.0, cx=-0.8, base_y=-1.9)
        base_f = Lf.base()
        raya = Line(Lf.p(8.5, 0), Lf.p(8.5, 1.0), color=SENAL, stroke_width=7)
        sinc = curva_f(Lf, lambda f: sinc_abs(f, 8.5), 4, 15, RUIDO, 3.5, n=400)
        faldas = area_f(Lf, lambda f: sinc_abs(f, 8.5), 4, 15, RUIDO, 0.5, n=400).set_z_index(2)
        debil = Line(Lf.p(12, 0), Lf.p(12, 0.06), color=CIAN, stroke_width=7).set_z_index(1)
        tij = tijeras().scale(0.8).move_to([5.6, 2.5, 0])
        salto = Line(Lt.p(1, -1), Lt.p(1, 1), color=ERROR, stroke_width=6)
        lab_millon = etiqueta("1/1.000.000", CIAN, 0.55).move_to(Lf.p(12.6, 0.62))
        fl_millon = flecha(Lf.p(12.4, 0.5), Lf.p(12.05, 0.1), CIAN, 3)
        pregunta = self.palabra("¿Cómo se corta sin romper?", AMBAR, 0.8).move_to([-0.8, 0.55, 0])

        with self.narrar("b1"):
            # «Un tono puro»
            self.en("tono")
            self.play(Create(Lt.base()), Create(tono), run_time=self.dur(1.2), rate_func=linear)

            # «una raya fina»
            self.en("raya")
            self.play(Create(base_f), Create(raya), run_time=self.dur(0.8))

            # «si lo cortas mal»
            self.en("cortas")
            self.sfx("whoosh")
            self.play(FadeIn(tij, shift=LEFT * 0.4), Create(salto), run_time=self.dur(0.6))

            # «sus faldas»
            self.en("faldas")
            self.play(Create(sinc), FadeIn(faldas), run_time=self.dur(0.5))

            # «pueden tapar a otro tono»
            self.en("tapa")
            self.play(FadeIn(debil), run_time=0.3)
            self.play(faldas.animate.set_fill(RUIDO, 0.9), run_time=self.dur(0.5))

            # «un millón de veces más débil»
            self.en("millon")
            self.play(FadeIn(lab_millon), GrowArrow(fl_millon), run_time=self.dur(0.6))

            # «¿Cómo se corta sin romper?»
            self.en("pregunta")
            self.pop(pregunta)

        self.wait(1.0)
        self.limpiar()
