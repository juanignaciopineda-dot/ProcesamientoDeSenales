"""Escena 06 — La innovación: lo nuevo no se puede adivinar. Después, la pausa."""
from comun.escena import *


class LoNuevo(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.parte_innovacion()
        self.wait(0.6)
        self.parte_pausa()
        self.wait(1.0)
        self.limpiar()

    def parte_innovacion(self):
        F = formula("x[n+1]", "=", r"0{,}6\,x[n]", "+", "w[n+1]", escala=1.1,
                    colores={0: MEDIDA, 2: VERDE, 4: ERROR}).move_to([0, 2.8, 0])
        oculta(F)
        l_ya = etiqueta("lo que ya sé", VERDE, 0.55).next_to(F[2], DOWN, buff=0.4)
        l_nuevo = etiqueta("lo nuevo", ERROR, 0.55).next_to(F[4], DOWN, buff=0.4)

        L = Lienzo(ancho=3.2, alto=1.0, t_rango=(0, 1), v_max=1.5, centro=(-4.5, -0.4))
        t = np.linspace(0, 1, 90)
        blanca = L.curva(t, 0.8 * serie(41, 90, 0.0), ERROR, 3)
        l_blanca = etiqueta("ruido blanco", INK, 0.5).move_to([-4.5, -1.5, 0])

        o = np.array([1.2, -1.5, 0.0])
        a_verde = Arrow(o, o + RIGHT * 2.4, buff=0, color=VERDE, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        a_roja = Arrow(o, o + UP * 1.7, buff=0, color=ERROR, stroke_width=6, max_tip_length_to_length_ratio=0.15)
        recto = VMobject(stroke_color=ROJO, stroke_width=3).set_fill(opacity=0)
        recto.set_points_as_corners([o + [0.25, 0, 0], o + [0.25, 0.25, 0], o + [0, 0.25, 0]])
        l_w = MathTex(r"w[n{+}1]", color=ERROR).scale(0.75).next_to(a_roja.get_end(), RIGHT, buff=0.15)
        l_conj = MathTex(r"x[k],\ k\le n", color=MEDIDA).scale(0.75).move_to(o + [1.2, -0.55, 0])
        q = self.palabra("?", ERROR, 1.2).move_to([0.3, -0.4, 0])
        innov = self.palabra("innovación", AMBAR, 1.0).move_to([4.6, 0.2, 0])
        a_trae = Arrow(l_nuevo.get_bottom() + DOWN * 0.1, innov.get_top() + UP * 0.1, color=AMBAR, buff=0,
                       stroke_width=4, max_tip_length_to_length_ratio=0.12)

        with self.narrar("b1"):
            # «la muestra siguiente»
            self.en("sig")
            self.add(F)
            self.play(*revelar(F[0], F[1]), run_time=self.dur(0.6))

            # «lo que ya sé»
            self.en("yase")
            self.play(*revelar(F[2]), FadeIn(l_ya), run_time=self.dur(0.5))

            # «lo genuinamente nuevo»
            self.en("nuevo")
            self.play(*revelar(F[3], F[4]), FadeIn(l_nuevo), run_time=self.dur(0.6))

            # «w de ene más uno»
            self.en("wn1")
            self.resaltar(F[4], color=ERROR)

            # «por ser blanco»
            self.en("blanco")
            self.play(Create(L.base()), Create(blanca), FadeIn(l_blanca), run_time=self.dur(1.0))

            # «no está correlacionado»
            self.en("nocorr")
            self.play(GrowArrow(a_verde), GrowArrow(a_roja), run_time=self.dur(0.6))
            self.play(Create(recto), FadeIn(l_w), run_time=self.dur(0.4))

            # «nada de lo que conozco»
            self.en("conozco")
            self.play(FadeIn(l_conj), run_time=self.dur(0.5))

            # «No hay forma lineal de adivinarlo»
            self.en("noadivina")
            self.pop(q)

            # «innovación»
            self.en("innov")
            self.pop(innov)

            # «lo que la muestra nueva trae»
            self.en("trae")
            self.play(GrowArrow(a_trae), run_time=self.dur(0.6))

    def parte_pausa(self):
        rel = reloj_arena().scale(1.3).move_to([-5.4, 0.6, 0])
        xh = formula(r"\hat{x}[n+1]", "=", "?", escala=1.2, colores={0: ESTIMACION, 2: AMBAR}).move_to([0.5, 2.0, 0])
        er = formula(r"\text{error}", "=", "?", escala=1.2, colores={0: ERROR, 2: ERROR}).move_to([0.5, 0.5, 0])
        lin = Line([-3.0, -0.7, 0], [4.0, -0.7, 0], color=INK, stroke_width=4)
        e2 = etiqueta("E2", INK, 0.6).move_to([6.4, 3.4, 0])
        yw_t = etiqueta("Yule-Walker", AMBAR, 0.6).move_to([0.5, -2.0, 0])
        yw_f = formula(r"\mathbf{R}\,\mathbf{h}", "=", r"\mathbf{r}", escala=0.9, color=INK).move_to([0.5, -2.9, 0])

        with self.narrar("b2"):
            # «Pausa para pensar»
            self.en("pausa")
            self.corte()
            self.play(FadeIn(rel, scale=0.7), run_time=self.dur(0.5))

            # «la mejor predicción posible»
            self.en("mejor")
            self.play(FadeIn(xh, shift=UP * 0.2), run_time=self.dur(0.6))

            # «cuánto error queda»
            self.en("error")
            self.play(FadeIn(er, shift=UP * 0.2), run_time=self.dur(0.6))

            # «cabe en una línea»
            self.en("linea")
            self.play(Create(lin), run_time=self.dur(0.6))

            # «de golpe»
            self.en("golpe")
            self.resaltar(lin, color=AMBAR, escala=1.05)

            # «en el segundo episodio»
            self.en("ep2")
            self.play(FadeIn(e2), run_time=self.dur(0.3))

            # «las ecuaciones de Yule-Walker»
            self.en("yw")
            self.play(FadeIn(yw_t), FadeIn(yw_f), run_time=self.dur(0.6))
