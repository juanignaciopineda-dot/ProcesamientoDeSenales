"""Escena 15 — La factorización existe si la densidad no se anula en una banda; la señal blanqueada es la innovación."""
from comun.escena import *


class LaInnovacion(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        L = Lienzo(ancho=5.0, alto=1.7, t_rango=(0, 1), v_max=1.0, centro=(-3.4, 1.7))
        g = lambda u: 0.8 * (np.exp(-((u - 0.12) / 0.22) ** 2) + 0.9 * np.exp(-((u - 0.88) / 0.2) ** 2)) + 0.05
        espec = curva_f(L, lambda u: np.where((u > 0.4) & (u < 0.62), 0.0, g(u)), 0.0, 1.0, MEDIDA, 4.0)
        base = L.base()
        lnulo = etiqueta("espectro nulo en una banda", AMBAR, 0.5).move_to([-3.4, 0.3, 0])
        bl_ = caja("blanquear", CIAN, ancho=2.4, alto=0.9, scale=0.5).move_to([3.6, 1.7, 0])
        x_ = cruz(ROJO, 1.5).move_to(bl_)
        bq = BloqueLTI(r"\frac{1}{F}", centro=(-0.4, 1.3), ancho=1.8, alto=1.1, color=CIAN, largo=1.8, escala=0.9)
        lx = MathTex("x", color=MEDIDA).scale(0.9).move_to([-5.4, 1.3, 0])
        leps = MathTex(r"\varepsilon", color=TXT).scale(1.0).move_to([2.9, 1.3, 0])
        tira = tira_blanca((1, -1, -1, 1, -1, 1), lado=0.45).move_to([3.5, 2.6, 0])
        innov = self.palabra("innovación", AMBAR, 0.9).move_to([-2.8, 3.1, 0])
        interr = self.palabra("?", AMBAR, 1.2).move_to([5.6, 1.3, 0])
        ly = MathTex("y", color=SENAL).scale(1.0).move_to([-3.4, -1.0, 0])
        interr2 = self.palabra("?", AMBAR, 1.0).move_to([0, -1.0, 0])
        leps2 = MathTex(r"\varepsilon", color=TXT).scale(1.0).move_to([3.4, -1.0, 0])
        dob = DoubleArrow(ly.get_right() + RIGHT * 0.2, leps2.get_left() + LEFT * 0.2, color=AMBAR, stroke_width=5,
                          buff=0, max_tip_length_to_length_ratio=0.12)
        sel = sello("fórmula del filtro causal", AMBAR).scale(1.0).move_to([0, -2.8, 0])
        with self.narrar("b1"):
            # «la densidad no se anule en toda una banda»
            self.en("banda")
            self.play(Create(base), Create(espec), run_time=self.dur(1.0))
            self.play(FadeIn(lnulo), run_time=self.dur(0.4))

            # «no se puede blanquear lo que no existe»
            self.en("noexiste")
            self.play(FadeIn(bl_), run_time=self.dur(0.4))
            self.play(Create(x_), run_time=0.3)
            self.sfx("error")

            # «La señal blanqueada»
            self.en("blanqueada")
            self.corte()
            self.play(FadeIn(lx), FadeIn(bq.ent), FadeIn(bq.sal), run_time=self.dur(0.6))

            # «uno entre F»
            self.en("unof")
            self.play(FadeIn(bq.caja), FadeIn(bq.rot), run_time=self.dur(0.6))

            # «innovación»
            self.en("innov")
            self.pop(innov)

            # «épsilon»
            self.en("eps")
            self.pop(leps, sonido=None)

            # «es blanca»
            self.en("blanca")
            self.play(FadeIn(tira, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «último ingrediente»
            self.en("ingred")
            self.pop(interr)

            # «relacionar la señal que buscamos»
            self.en("relacionar")
            self.play(FadeIn(ly), FadeIn(interr2), run_time=self.dur(0.6))

            # «con esa innovación»
            self.en("conesa")
            self.play(FadeIn(leps2), FadeOut(interr2), GrowFromCenter(dob), run_time=self.dur(0.7))

            # «la fórmula del filtro causal»
            self.en("formula")
            self.pop(sel, sonido="impacto")

        self.wait(1.0)
        self.limpiar()
