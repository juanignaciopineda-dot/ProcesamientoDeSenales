"""Escena 17 — Cierre: repaso del episodio y anuncio del E7, «De Wiener a Kalman»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        contorno = Rectangle(width=3.0, height=0.9, color=MEDIDA, stroke_width=4).move_to([-4.6, 2.3, 0])
        verde = Rectangle(width=2.7, height=0.9, stroke_width=0).set_fill(VERDE, 0.7).move_to([-4.75, 2.3, 0])
        roja = Rectangle(width=0.3, height=0.9, stroke_width=0).set_fill(ERROR, 0.9).move_to([-3.25, 2.3, 0])
        innov = self.palabra("innovación", AMBAR, 0.6).move_to([-3.0, 3.4, 0])
        tj = tijeras().scale(0.4).move_to([-3.25, 3.0, 0])
        sabias = Text("ya sabías", color=VERDE, weight=BOLD).scale(0.55).move_to([-4.75, 1.4, 0])

        bal = Balanza(centro=(4.6, 2.0), semi=1.5)
        sq_i = Square(side_length=0.5, color=MEDIDA, stroke_width=3).set_fill(MEDIDA, 0.35).move_to([3.1, 1.55, 0])
        sqs_d = VGroup(*[Square(side_length=0.26, color=INK, stroke_width=2).set_fill(INK, 0.3)
                         .move_to([6.1 + (i - 2.5) * 0.31, 1.45, 0]) for i in range(6)])

        fr = fraccion(MathTex(r"0{,}7386", color=TXT).scale(0.9),
                      MathTex(r"1-0{,}157\,z^{-1}", color=TXT).scale(0.9)).move_to([-4.4, -0.6, 0])
        pz = plano_c(centro=(-4.4, -2.7), radio=0.6)
        eq = MathTex(r"\times", color=ESTIMACION).scale(0.7).move_to([-4.4 + 0.1, -2.7, 0])
        cer = Circle(radius=0.09, color=AMBAR, stroke_width=4).move_to([-4.4 + 0.45, -2.7, 0])
        est = caja("estado", AZUL, ancho=2.2, alto=0.8, scale=0.55).move_to([4.0, -0.9, 0])
        obs = caja("observador", ESTIMACION, ancho=2.8, alto=0.8, scale=0.55).move_to([4.0, -2.4, 0])
        a_eo = flecha([4.0, -1.35, 0], [4.0, -1.95, 0], INK)
        igual = MathTex(r"=", color=VERDE).scale(2.0).move_to([0.0, -1.7, 0])
        sig = etiqueta("Episodio 7", INK, 0.6).move_to([5.9, -3.5, 0])
        tit = self.palabra("De Wiener a Kalman", AMBAR, 0.8).move_to([0, -3.5, 0])

        with self.narrar("b1"):
            # «cada muestra trae algo nuevo»
            self.en("nuevo")
            self.play(Create(contorno), FadeIn(verde), FadeIn(roja), run_time=self.dur(0.7))

            # «la innovación»
            self.en("innov")
            self.pop(innov)

            # «predecir es tirarlo»
            self.en("tirar")
            self.play(FadeIn(tj, scale=0.7), run_time=self.dur(0.3))
            self.play(FadeOut(roja), FadeOut(tj), run_time=self.dur(0.4))

            # «lo que ya sabías»
            self.en("sabias")
            self.play(FadeIn(sabias), run_time=self.dur(0.4))

            # «la muestra de ahora vale más»
            self.en("ahora")
            self.play(FadeIn(bal), FadeIn(sq_i), run_time=self.dur(0.5))

            # «que todo el futuro junto»
            self.en("futuro")
            self.play(FadeIn(sqs_d), run_time=self.dur(0.3))
            dy = bal.semi * np.sin(0.22)
            self.play(*bal.inclinar("izq"), sq_i.animate.shift(DOWN * dy), sqs_d.animate.shift(UP * dy),
                      run_time=self.dur(0.7))

            # «Pero la fórmula del filtro causal»
            self.en("formula")
            self.play(FadeIn(fr), run_time=self.dur(0.6))

            # «con sus polos y sus ceros»
            self.en("polos")
            self.play(FadeIn(pz), FadeIn(eq), Create(cer), run_time=self.dur(0.6))

            # «un sistema de control con un observador»
            self.en("obs")
            self.play(FadeIn(est), FadeIn(obs), GrowArrow(a_eo), run_time=self.dur(0.8))

            # «esa casualidad no lo es»
            self.en("nolo")
            self.pop(igual)

            # «En el siguiente episodio»
            self.en("sig")
            self.play(FadeIn(sig, shift=LEFT * 0.3), run_time=self.dur(0.4))

            # «De Wiener a Kalman»
            self.en("titulo")
            self.pop(tit)

        self.wait(1.0)
        self.limpiar()
