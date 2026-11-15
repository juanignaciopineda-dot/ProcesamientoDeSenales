"""Escena 12 — La respuesta en frecuencia del filtro adaptado es la conjugada de la señal."""
from comun.escena import *


class LaConjugada(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        o_pos = (-2.2, -0.4)
        hom = MathTex(r"H(\Omega)", color=ESTIMACION).scale(1.4).move_to([0, 3.2, 0])
        conj = formula("H", "=", r"S^{*}", escala=1.4, colores={0: ESTIMACION, 2: SENAL}).move_to([0, 3.2, 0])
        pl = plano_c(centro=o_pos, radio=1.6)
        o = pl.o
        s_f = flecha_c(o, 1.5, 50, SENAL, 6)
        h_f = flecha_c(o, 1.5, -50, ESTIMACION, 6)
        guia = DashedLine(o + LEFT * 1.9, o + RIGHT * 1.9, color=INK, stroke_width=2).set_opacity(0.6)
        # tres flechas de la señal
        angs, largos = (35, 100, 160), (1.5, 1.2, 1.0)
        tres = [flecha_c(o, l, a, SENAL, 6) for a, l in zip(angs, largos)]
        girar = [Rotate(f, angle=-np.deg2rad(a), about_point=o) for f, a in zip(tres, angs)]
        resp = MathTex(r"\sum |S|^2", color=AMBAR).scale(1.4).move_to([4.2, 0.6, 0])
        l_mod = etiqueta("mismo módulo", INK, 0.5).move_to([4.2, 1.8, 0])
        with self.narrar("b1"):
            # «Su respuesta en frecuencia»
            self.en("resp")
            self.pop(hom)

            # «la conjugada de la transformada»
            self.en("conj")
            self.play(ReplacementTransform(hom, conj), run_time=self.dur(0.8))

            # «mismo módulo»
            self.en("modulo")
            self.play(FadeIn(pl), run_time=self.dur(0.4))
            self.play(GrowArrow(s_f), run_time=self.dur(0.4))
            self.play(FadeIn(l_mod), run_time=0.3)
            self.resaltar(pl.circ, color=AMBAR, escala=1.04)

            # «el ángulo cambiado de signo»
            self.en("signo")
            self.play(Create(guia), run_time=0.3)
            self.play(TransformFromCopy(s_f, h_f), run_time=self.dur(0.8))

            # «Cada flecha de la señal»
            self.en("cada")
            self.play(FadeOut(s_f), FadeOut(h_f), FadeOut(l_mod), run_time=0.3)
            self.play(LaggedStart(*[GrowArrow(f) for f in tres], lag_ratio=0.3), run_time=self.dur(1.0))

            # «gira justo el ángulo contrario»
            self.en("gira")
            self.sfx("whoosh")
            self.play(*girar, run_time=self.dur(1.2))

            # «apuntando a cero»
            self.en("cero")
            self.resaltar(guia, color=AMBAR, escala=1.0)

            # «Todas alineadas»
            self.en("alin")
            self.play(tres[1].animate.shift(tres[0].get_end() - o),
                      tres[2].animate.shift(tres[0].get_end() - o + tres[1].get_end() - o),
                      run_time=self.dur(0.8))

            # «se suman al máximo»
            self.en("max")
            self.pop(resp)
        self.wait(1.0)
        self.limpiar()
