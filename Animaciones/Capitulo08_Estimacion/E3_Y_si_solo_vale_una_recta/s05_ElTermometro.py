"""Escena 05 — El termómetro de la sala: temperatura, ruido, lectura, y la recta que arranca de la media."""
from comun.escena import *


class ElTermometro(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.planteo()
        self.recta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def planteo(self):
        termo = termometro(3.0, ROJO, 0.6).move_to([-5.2, 0.0, 0])
        que = MathTex(r"y=\;?", color=AMBAR).scale(1.4).move_to([-5.2, 2.5, 0])
        n23 = Text("23 °C", color=MEDIDA, weight=BOLD).scale(0.9).move_to([-5.2, -2.3, 0])

        def rotulo(txt, color, y):
            return Text(txt, color=color).scale(0.65).move_to([-3.2, y, 0], aligned_edge=LEFT)

        lbl_a = rotulo("Temperatura", SENAL, 2.4)
        let_y = MathTex("y", color=SENAL).scale(1.1).move_to([-0.2, 2.4, 0])
        mu_y = MathTex(r"\mu=20", color=SENAL).scale(0.95).move_to([1.7, 2.4, 0])
        var_y = MathTex(r"\sigma^2=4", color=SENAL).scale(0.95).move_to([4.3, 2.4, 0])
        lbl_b = rotulo("Ruido", RUIDO, 0.9)
        let_v = MathTex("v", color=RUIDO).scale(1.1).move_to([-0.7, 0.9, 0])
        mu_v = MathTex(r"\mu=0", color=RUIDO).scale(0.95).move_to([1.7, 0.9, 0])
        var_v = MathTex(r"\sigma^2=1", color=RUIDO).scale(0.95).move_to([4.3, 0.9, 0])
        sin_rel = Text("Sin relación con la temperatura", color=INK).scale(0.5).move_to([-3.2, 0.25, 0],
                                                                                          aligned_edge=LEFT)
        lbl_c = rotulo("Lectura", MEDIDA, -0.9)
        f_x = formula("x", "=", "y", "+", "v", escala=1.1, colores={0: MEDIDA, 2: SENAL, 4: RUIDO})
        f_x.move_to([1.9, -0.9, 0])
        R = RectaNum(16, 24, centro=(1.0, -2.9), ancho=8.0, marcas=[16, 18, 20, 22, 24])
        banda = Rectangle(width=abs(R.p(22)[0] - R.p(18)[0]), height=0.3, stroke_width=0).set_fill(SENAL, 0.5)
        banda.move_to(R.p(20))
        ar_d = Arrow(R.p(20) + UP * 0.6, R.p(22) + UP * 0.6, buff=0, color=SENAL, stroke_width=5,
                     max_tip_length_to_length_ratio=0.25)
        ar_i = Arrow(R.p(20) + UP * 0.6, R.p(18) + UP * 0.6, buff=0, color=SENAL, stroke_width=5,
                     max_tip_length_to_length_ratio=0.25)

        with self.narrar("b1"):
            # «un ejemplo que nos acompañará mucho tiempo»
            self.en("ejemplo")
            self.play(FadeIn(termo), run_time=self.dur(0.8))

            # «La temperatura de una sala»
            self.en("sala")
            self.play(FadeIn(lbl_a), run_time=self.dur(0.4))
            self.pop(let_y)

            # «una media de veinte grados»
            self.en("media")
            self.play(FadeIn(mu_y, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «una varianza de cuatro»
            self.en("var")
            self.play(FadeIn(var_y, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «se aparta unos dos grados»
            self.en("dos")
            self.play(Create(R.base), *[Create(R.ticks[v]) for v in R.ticks],
                      *[FadeIn(R.nums[v]) for v in R.nums], run_time=self.dur(0.7))
            self.play(FadeIn(banda), run_time=self.dur(0.6))

            # «arriba o abajo»
            self.en("arriba")
            self.play(GrowArrow(ar_d), GrowArrow(ar_i), run_time=self.dur(0.6))

            # «un termómetro que suma su propio ruido»
            self.en("ruido")
            self.play(FadeIn(lbl_b), run_time=self.dur(0.4))
            self.pop(let_v)

            # «de media cero y varianza uno»
            self.en("r01")
            self.play(FadeIn(mu_v, shift=LEFT * 0.2), FadeIn(var_v, shift=LEFT * 0.2), run_time=self.dur(0.7))

            # «sin ninguna relación con la temperatura»
            self.en("norel")
            self.play(FadeIn(sin_rel), run_time=self.dur(0.6))

            # «El termómetro marca veintitrés»
            self.en("m23")
            self.play(FadeIn(lbl_c), FadeIn(f_x), run_time=self.dur(0.7))
            self.pop(n23)

            # «y buscamos»
            self.en("busca")
            self.resaltar(n23, color=AMBAR, escala=1.15)

            # «¿Qué temperatura hace?»
            self.en("que")
            self.pop(que)
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def recta(self):
        f = formula(r"\hat{y}", "=", "h", r"\cdot", "x", "+", "b", escala=1.5,
                    colores={0: ESTIMACION, 2: ESTIMACION, 4: MEDIDA, 6: ESTIMACION}).move_to([0, 2.5, 0])
        sea = Text("Para cualquier h", color=AMBAR).scale(0.6).move_to([-4.8, 1.3, 0])
        pr1 = MathTex(r"E[\hat{y}]=E[y]", color=TXT).scale(1.1).move_to([0, 1.2, 0])
        pr2 = MathTex(r"20h+b=20", color=TXT).scale(1.1).move_to([0, 0.2, 0])
        b20 = formula("b", "=", "20", "-", "20h", escala=1.3, colores={0: ESTIMACION}).move_to([0, -0.9, 0])
        q = formula(r"\hat{y}", "=", "20", "+", "h", "(", "x", "-", "20", ")", escala=1.5,
                    colores={0: ESTIMACION, 4: ESTIMACION, 6: MEDIDA}).move_to([0, -2.2, 0])
        rect = SurroundingRectangle(VGroup(*[q[i] for i in range(4, 10)]), color=AMBAR, buff=0.12)
        lbl = Text("Lo que se aparta", color=INK).scale(0.5).move_to([rect.get_center()[0], -3.2, 0])
        corr = Text("Corrección", color=ESTIMACION, weight=BOLD).scale(0.55).move_to(lbl.get_center())
        media = Text("Media", color=ESTIMACION, weight=BOLD).scale(0.55).move_to([q[2].get_center()[0], -3.2, 0])

        with self.narrar("b2"):
            # «hache por lo que marca el termómetro»
            self.en("hx")
            self.corte()
            self.play(*[FadeIn(f[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.0))

            # «más un número fijo, be»
            self.en("b")
            self.play(FadeIn(f[5]), FadeIn(f[6], shift=UP * 0.1), run_time=self.dur(0.5))

            # «Empecemos por be»
            self.en("emp")
            self.play(Indicate(f[6], color=AMBAR), run_time=self.dur(0.7))

            # «Sea cual sea hache»
            self.en("sea")
            self.pop(sea)

            # «en promedio no nos desviemos»
            self.en("prom")
            self.play(FadeIn(pr1, shift=UP * 0.1), run_time=self.dur(0.6))
            self.play(FadeIn(pr2, shift=UP * 0.1), run_time=self.dur(0.6))

            # «veinte menos veinte hache»
            self.en("b20")
            self.play(*[FadeIn(b20[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(0.9))

            # «la recta queda veinte»
            self.en("queda")
            self.play(*[FadeIn(q[i], shift=UP * 0.1) for i in range(10)], run_time=self.dur(1.0))

            # «más hache por lo que la lectura se aparta de veinte»
            self.en("aparta")
            self.play(Create(rect), FadeIn(lbl), run_time=self.dur(0.7))

            # «Arrancamos de la media»
            self.en("arranca")
            self.pop(media)

            # «y corregimos»
            self.en("corregimos")
            self.play(ReplacementTransform(lbl, corr), run_time=self.dur(0.5))
