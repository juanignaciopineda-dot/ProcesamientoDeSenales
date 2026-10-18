"""Escena 17 — Cierre: una curva lo describe todo; anuncia «Dos números para resumirlo todo»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "17"

    def construir(self, x):
        """Las tres distribuciones, pequeñas, centradas en x."""
        ax = Axes(x_range=[-0.7, 1.7, 1], y_range=[0, 1.0, 1], x_length=3.6, y_length=2.1,
                  axis_config={"color": INK, "stroke_width": 2, "include_ticks": False, "include_tip": False}
                  ).move_to([x[0], 1.3, 0])
        barras = VGroup(Rectangle(width=0.6, height=0.7, stroke_color=AZUL, fill_color=AZUL, fill_opacity=0.5)
                        .move_to(ax.c2p(0, 0) + UP * 0.35),
                        Rectangle(width=0.6, height=1.4, stroke_color=VERDE, fill_color=VERDE, fill_opacity=0.5)
                        .move_to(ax.c2p(1, 0) + UP * 0.7))
        b = VGroup(ax, barras)
        ax2 = Axes(x_range=[0, 5, 1], y_range=[0, 1.0, 1], x_length=3.6, y_length=2.1,
                   axis_config={"color": INK, "stroke_width": 2, "include_ticks": False, "include_tip": False}
                   ).move_to([x[1], 1.3, 0])
        rect = Rectangle(width=2.0, height=1.0, stroke_color=SENAL, fill_color=SENAL, fill_opacity=0.35)
        rect.move_to(ax2.c2p(2.5, 0) + UP * 0.5)
        u = VGroup(ax2, rect)
        ax3 = Axes(x_range=[-3, 3, 1], y_range=[0, 0.5, 1], x_length=3.6, y_length=2.1,
                   axis_config={"color": INK, "stroke_width": 2, "include_ticks": False, "include_tip": False}
                   ).move_to([x[2], 1.3, 0])
        camp = ax3.plot(lambda t: float(gaussiana(t)), x_range=[-3, 3, 0.05], color=AMBAR, stroke_width=4)
        gcc = VGroup(ax3, camp)
        return VGroup(b, u, gcc)

    def construct(self):
        xs = (-4.4, 0.0, 4.4)
        figs = self.construir(xs)
        marcos = VGroup(*[SurroundingRectangle(f, color=VERDE, buff=0.25, corner_radius=0.12, stroke_width=3)
                          for f in figs])
        rng = np.random.default_rng(2)
        nums = VGroup(*[Text(f"{rng.uniform(0, 9):.2f}".replace(".", ","), color=INK).scale(0.5)
                        .move_to([-6.0 + 1.0 * (i % 13), -1.3 - 0.8 * (i // 13), 0]) for i in range(26)])
        q = VGroup(*[Text("?", color=AMBAR, weight=BOLD).scale(0.9).move_to([x, 2.4, 0]) for x in xs])
        badges = VGroup()
        for x in xs:
            b1 = VGroup(Circle(radius=0.4, color=AMBAR, stroke_width=3), Text("1", color=AMBAR, weight=BOLD).scale(0.65))
            b2 = VGroup(Circle(radius=0.4, color=VERDE, stroke_width=3), Text("2", color=VERDE, weight=BOLD).scale(0.65))
            badges.add(VGroup(b1, b2).arrange(RIGHT, buff=0.35).move_to([x, -0.9, 0]))

        with self.narrar("b1"):
            self.en("curva")                                  # «Una curva describe una variable»
            self.play(LaggedStart(*[FadeIn(f, scale=0.8) for f in figs], lag_ratio=0.25), run_time=self.dur(1.2))
            self.en("completo")                               # «por completo»
            self.play(Create(marcos), run_time=self.dur(0.8))
            self.en("no_conocemos")                           # «no conocemos la curva entera»
            self.play(figs.animate.fade(0.6), FadeIn(q), FadeOut(marcos), run_time=self.dur(0.7))
            self.en("demasiada")                              # «demasiada información»
            self.play(LaggedStart(*[FadeIn(n, scale=0.6) for n in nums], lag_ratio=0.04), run_time=self.dur(1.6))
            self.en("trabajar")                               # «trabajar con ella»
            self.play(LaggedStart(*[n.animate(rate_func=there_and_back).scale(1.5) for n in nums[::2]],
                                  lag_ratio=0.05), run_time=self.dur(1.4))
            self.en("resumirla")                              # «¿Y si pudiéramos resumirla»
            self.play(FadeOut(nums), FadeOut(q), figs.animate.scale(0.8).shift(UP * 0.45), run_time=self.dur(0.9))
            self.en("dos_numeros")                            # «solo dos números»
            self.play(LaggedStart(*[FadeIn(b, scale=0.6) for b in badges], lag_ratio=0.2), run_time=self.dur(0.9))
            self.en("alcanzan")                               # «alcanzan para mucho»
            self.play(*[b.animate(rate_func=there_and_back).scale(1.35) for b in badges], run_time=self.dur(0.8))
            self.en("veremos")                                # «Lo veremos en el próximo episodio»
            fl = Arrow([-1.4, -2.1, 0], [1.4, -2.1, 0], color=INK, stroke_width=5, buff=0)
            self.play(Create(fl), run_time=self.dur(0.6))
            self.en("titulo")                                 # «Dos números para resumirlo todo»
            tit = self.palabra("Dos números para resumirlo todo", AMBAR, 0.8).move_to([0, -3.1, 0])
            self.pop(tit)
        self.wait(1.2)
        self.limpiar()
