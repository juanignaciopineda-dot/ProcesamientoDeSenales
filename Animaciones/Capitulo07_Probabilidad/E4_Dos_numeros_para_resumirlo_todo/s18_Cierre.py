"""Escena 18 — Cierre: la media, la varianza y la pregunta de las dos variables."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        y0 = 0.2
        base = Line([-6.2, y0, 0], [-0.8, y0, 0], color=INK, stroke_width=2)
        estrecha = campana7(-3.5, y0, 0.8, SENAL, ancho=0.9, alto=2.2, x_max=3)
        ancha = campana7(-3.5, y0, 1.6, ESTIMACION, ancho=0.9, alto=2.2, x_max=3)
        mu = MathTex(r"\mu", color=AMBAR).scale(1.4).move_to([-3.5, y0 - 0.6, 0])
        s2 = MathTex(r"\sigma^2", color=AMBAR).scale(1.4).move_to([-5.8, 3.3, 0])
        cheb = MathTex(r"P(|X-\mu|\ge\alpha\sigma)\le\frac{1}{\alpha^2}", color=TXT).scale(1.0).move_to([3.6, 2.1, 0])
        prom = MathTex(r"\mathrm{Var}(\bar X_n)=\frac{\sigma^2}{n}", color=TXT).scale(1.0).move_to([3.6, 0.3, 0])
        caja_x = RoundedRectangle(corner_radius=0.12, width=1.6, height=1.6, color=SENAL, fill_color=SENAL, fill_opacity=0.12, stroke_width=2.5)
        x_t = MathTex("X", color=SENAL).scale(1.6).move_to(caja_x)
        env = sobre(TXT).scale(1.0)
        rec = sobre(TXT).scale(1.0)
        y_t = MathTex("Y", color=MEDIDA).scale(1.6)
        caja_y = RoundedRectangle(corner_radius=0.12, width=1.6, height=1.6, color=MEDIDA, fill_color=MEDIDA, fill_opacity=0.12, stroke_width=2.5)
        grupo_x = VGroup(caja_x, x_t).move_to([-3.6, -0.3, 0])
        grupo_y = VGroup(caja_y, y_t).move_to([3.6, -0.3, 0])
        env.next_to(grupo_x, UP, buff=0.35)
        rec.next_to(grupo_y, UP, buff=0.35)
        t_env = Text("Lo que se envió", color=INK).scale(0.55).next_to(grupo_x, DOWN, buff=0.3)
        t_rec = Text("Lo que se recibió", color=INK).scale(0.55).next_to(grupo_y, DOWN, buff=0.3)
        doble = DoubleArrow(grupo_x.get_right() + RIGHT * 0.2, grupo_y.get_left() + LEFT * 0.2, color=AMBAR,
                            stroke_width=5, buff=0)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.3).move_to([0, 0.5, 0])
        titulo_ = self.palabra("Dos variables a la vez", AMBAR, 1.3).move_to([0, -3.0, 0])
        with self.narrar("b1"):
            self.play(Create(base), run_time=1.0)
            # «la media dice dónde está»
            self.en("media")
            self.play(Create(estrecha), FadeIn(mu), run_time=self.dur(1.0))
            # «la varianza, cuánto se aleja»
            self.en("varianza")
            self.play(Transform(estrecha, ancha), FadeIn(s2, shift=DOWN * 0.15), run_time=self.dur(1.2))
            # «acotamos lo imposible con Chebyshev»
            self.en("cheb")
            self.play(FadeIn(cheb, shift=LEFT * 0.15), run_time=self.dur(1.2))
            # «por qué promediar funciona»
            self.en("prom")
            self.play(FadeIn(prom, shift=LEFT * 0.15), run_time=self.dur(1.2))
            # «nunca hay una sola variable»
            self.en("una")
            self.corte()
            self.play(FadeIn(grupo_x), run_time=self.dur(0.6))
            # «lo que se envió»
            self.en("envio")
            self.play(FadeIn(env, shift=RIGHT * 0.2), FadeIn(t_env), run_time=self.dur(0.7))
            # «lo que se recibió»
            self.en("recibio")
            self.play(FadeIn(grupo_y, shift=LEFT * 0.2), FadeIn(rec, shift=LEFT * 0.2), FadeIn(t_rec),
                      run_time=self.dur(0.8))
            # «¿Qué podemos saber de una»
            self.en("saber")
            self.play(GrowFromCenter(doble), run_time=0.5)
            self.pop(interr)
            # «En el próximo episodio»
            self.en("proximo")
            self.play(Indicate(doble, color=AMBAR), run_time=self.dur(0.9))
            # «Dos variables a la vez»
            self.en("titulo")
            self.pop(titulo_)
        self.wait(1.2)
        self.limpiar()
