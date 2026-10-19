"""Escena 04 — Estimar aquí no es lo de Probabilidad y Estadística: la distribución se conoce entera."""
from comun.escena import *


class EstimarEsApostar(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        gris = RoundedRectangle(corner_radius=0.15, width=6.4, height=5.0, color=INK, stroke_width=3,
                                fill_color=INK, fill_opacity=0.07).move_to([-3.6, 0.0, 0])
        tit_g = Text("Probabilidad y Estadística", color=INK, weight=BOLD).scale(0.55).move_to(gris.get_top() + DOWN * 0.45)
        L = Lienzo(ancho=4.8, alto=2.0, t_rango=(-3, 3), v_max=1.0, centro=(-3.6, -0.6))
        t = np.linspace(-3, 3, 120)
        camp = DashedVMobject(L.curva(t, np.exp(-t ** 2 / 2), INK, 3.5), num_dashes=46)
        interr = VGroup(*[Text("?", color=INK, weight=BOLD).scale(0.7).move_to([-3.6 + dx, 1.15 + dy, 0])
                          for dx, dy in [(-1.2, 0.0), (-0.3, 0.3), (0.7, 0.1), (1.3, -0.2)]])
        base = L.base(INK, 1.6)
        pts = VGroup(*[Dot([-3.6 + x, -0.6, 0], radius=0.1, color=MEDIDA) for x in (-1.5, -0.9, -0.4, 0.1, 0.5, 1.1)])
        mu = Text("μ = ?", color=ESTIMACION, weight=BOLD).scale(0.7).move_to([-3.6, -1.75, 0])
        flecha_mu = Arrow([-3.6, -0.85, 0], [-3.6, -1.45, 0], buff=0, color=ESTIMACION, stroke_width=4)
        tach = Line(gris.get_corner(UL) + DR * 0.15, gris.get_corner(DR) + UL * 0.15, color=ROJO, stroke_width=8)

        ambar = RoundedRectangle(corner_radius=0.15, width=6.4, height=5.0, color=ESTIMACION, stroke_width=3,
                                 fill_color=ESTIMACION, fill_opacity=0.07).move_to([3.6, 0.0, 0])
        tit_a = Text("La conocemos entera", color=ESTIMACION, weight=BOLD).scale(0.6).move_to(ambar.get_top() + DOWN * 0.45)
        barras = VGroup(*[Rectangle(width=0.5, height=1.6, color=SENAL, fill_color=SENAL, fill_opacity=0.45,
                                    stroke_width=3).move_to([3.6 + (i - 2.5) * 0.75, -0.9 + 0.8, 0]) for i in range(6)])
        nums = VGroup(*[Text(str(i + 1), color=INK).scale(0.45).move_to([3.6 + (i - 2.5) * 0.75, -1.2, 0])
                        for i in range(6)])
        sextos = VGroup(*[MathTex(r"\tfrac16", color=INK).scale(0.7).move_to([3.6 + (i - 2.5) * 0.75, -1.75, 0])
                          for i in range(6)])
        q = Text("?", color=ESTIMACION, weight=BOLD).scale(1.2).move_to([3.6, 1.35, 0])
        flecha_ap = Arrow([3.975, 1.6, 0], [3.975, 0.85, 0], buff=0, color=ESTIMACION, stroke_width=5)
        ap = Text("Apuesta", color=ESTIMACION, weight=BOLD).scale(0.6).next_to(flecha_ap, RIGHT, buff=0.1)

        with self.narrar("b1"):
            # «Probabilidad y Estadística»
            self.en("pye")
            self.play(FadeIn(gris), FadeIn(tit_g), run_time=self.dur(0.6))

            # «no conocías la distribución»
            self.en("nodist")
            self.play(FadeIn(base), Create(camp), FadeIn(interr, lag_ratio=0.25), run_time=self.dur(1.0))

            # «con una muestra»
            self.en("muestra")
            self.play(FadeIn(pts, shift=DOWN * 0.6, lag_ratio=0.15), run_time=self.dur(0.9))

            # «la media de una población»
            self.en("media")
            self.play(GrowArrow(flecha_mu), FadeIn(mu), run_time=self.dur(0.6))

            # «a partir de unos cuantos datos»
            self.en("pocos")
            self.sfx("error")
            self.play(Create(tach), run_time=self.dur(0.5))

            # «Aquí la distribución la conocemos entera»
            self.en("aqui")
            self.play(FadeIn(ambar), FadeIn(tit_a), run_time=self.dur(0.4))
            self.play(FadeIn(barras, lag_ratio=0.12), FadeIn(nums), run_time=self.dur(0.9))

            # «conocemos entera»
            self.en("entera")
            self.play(FadeIn(sextos, lag_ratio=0.1), run_time=self.dur(0.8))

            # «qué valor saldrá esta vez»
            self.en("valor")
            self.pop(q)

            # «Hay que apostar por uno»
            self.en("apostar")
            self.play(FadeOut(q), GrowArrow(flecha_ap), FadeIn(ap), run_time=self.dur(0.6))
        self.wait(1.0)
        self.limpiar()
