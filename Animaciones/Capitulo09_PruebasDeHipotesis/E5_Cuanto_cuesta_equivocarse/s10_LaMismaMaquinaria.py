"""Escena 10 — La misma maquinaria: detectar y estimar solo cambian el coste; y todo supone conocer las campanas."""
from comun.escena import *
from comun.figuras_c9e5 import *


class LaMismaMaquinaria(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.maquina()
        self.datos()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def maquina(self):
        with self.narrar("b1"):
            # «Es la misma maquinaria»
            self.en("maquina")
            a = bloque9("A posteriori", INK, ancho=3.0, alto=1.1, escala=0.58).move_to([-4.3, 0.9, 0])
            b = bloque9("Menor coste esperado", INK, ancho=4.2, alto=1.1, escala=0.58).move_to([0.3, 0.9, 0])
            f_ab = Arrow(a.get_right(), b.get_left(), color=INK, buff=0.1, stroke_width=3,
                         max_tip_length_to_length_ratio=0.2)
            self.play(FadeIn(a), FadeIn(b), Create(f_ab), run_time=self.dur(0.6))

            # «probabilidades a posteriori»
            self.en("post")
            self.play(a.marco.animate.set_stroke(MEDIDA, 5), run_time=self.dur(0.4))

            # «el menor coste esperado»
            self.en("menor")
            self.play(b.marco.animate.set_stroke(AMBAR, 5), run_time=self.dur(0.4))

            # «Solo cambia el coste»
            self.en("coste")
            cc = bloque9("Coste: 0–1", ERROR, ancho=3.0, alto=0.9, escala=0.55).move_to([0.3, 2.9, 0])
            f_c = Arrow(cc.get_bottom(), b.get_top(), color=ERROR, buff=0.08, stroke_width=3,
                        max_tip_length_to_length_ratio=0.25)
            self.play(FadeIn(cc, shift=DOWN * 0.2), Create(f_c), run_time=self.dur(0.4))
            c2 = bloque9("Coste: Error²", ERROR, ancho=3.0, alto=0.9, escala=0.55).move_to(cc)
            self.play(Transform(cc, c2), run_time=self.dur(0.5))

            # «el tipo de respuesta»
            self.en("salida")
            f_s = Arrow(b.get_right(), b.get_right() + RIGHT * 1.0, color=INK, buff=0.1, stroke_width=3,
                        max_tip_length_to_length_ratio=0.25)
            s1 = MathTex(r"H_0 \,/\, H_1", color=TXT).scale(1.0).next_to(f_s, RIGHT, buff=0.15)
            s2 = Text("Un número", color=TXT).scale(0.58).move_to(s1, aligned_edge=LEFT)
            self.play(Create(f_s), FadeIn(s1), Transform(cc, bloque9("Coste: 0–1", ERROR, ancho=3.0, alto=0.9,
                                                                      escala=0.55).move_to(cc)),
                      run_time=self.dur(0.4))
            self.play(ReplacementTransform(s1, s2), Transform(cc, c2.copy()), run_time=self.dur(0.5))

            # «Detectar responde»
            self.en("detectar")
            dt = Text("Detectar: ¿Cuál de estas?", color=TXT).scale(0.72).move_to([-5.0, -1.3, 0], aligned_edge=LEFT)
            self.play(FadeIn(dt, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «Estimar responde a cuánto»
            self.en("estimar")
            es = Text("Estimar: ¿Cuánto?", color=TXT).scale(0.72).next_to(dt, DOWN, buff=0.4, aligned_edge=LEFT)
            self.play(FadeIn(es, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «en el canal»
            self.en("canal")
            self.corte()
            K = canal9(centro=(0.0, 2.4), ancho=7.0)
            self.play(FadeIn(K), run_time=self.dur(0.5))

            # «setenta y nueve»
            self.en("v079")
            le = Text("Estimar", color=MEDIDA, weight=BOLD).scale(0.55).move_to([-2.6, -0.5, 0])
            ve = Text("0,79", color=MEDIDA, weight=BOLD).scale(1.2).move_to([-2.6, -1.6, 0])
            self.play(FadeIn(le), run_time=0.25)
            self.pop(ve)

            # «y el uno»
            self.en("v1")
            ld = Text("Decidir", color=AMBAR, weight=BOLD).scale(0.55).move_to([2.6, -0.5, 0])
            vd = Text("1", color=AMBAR, weight=BOLD).scale(1.2).move_to([2.6, -1.6, 0])
            self.play(FadeIn(ld), run_time=0.25)
            self.pop(vd)

            # «a dos preguntas»
            self.en("preguntas")
            qe = Text("¿Cuánto?", color=TXT).scale(0.5).move_to([-2.6, 0.55, 0])
            qd = Text("¿Cuál?", color=TXT).scale(0.5).move_to([2.6, 0.55, 0])
            self.play(FadeIn(qe, shift=DOWN * 0.15), FadeIn(qd, shift=DOWN * 0.15), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b2
    def datos(self):
        C = campanas_e5(centro=(0.0, -2.2), ancho=10.0, alto=5.0)
        with self.narrar("b2"):
            # «algo muy cómodo»
            self.en("comodo")
            self.corte()
            eje = C.eje((0, 1, 2), rotulo=False)
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.6))

            # «conocemos las dos campanas»
            self.en("conocidas")
            k = Text("Conocidas", color=VERDE, weight=BOLD).scale(0.6).move_to([0, 2.4, 0])
            self.pop(k)

            # «nadie te las da»
            self.en("borra")
            self.play(Uncreate(c0), Uncreate(c1), FadeOut(k), run_time=self.dur(0.6))

            # «Lo que tienes son datos»
            self.en("datos")
            rng = np.random.default_rng(9)
            marcas = VGroup()
            for mu, col, n in ((0, C0, 9), (2, C1, 5)):
                for r in rng.normal(mu, 1, n):
                    marcas.add(Line(C.p(r), C.p(r) + UP * 0.9, color=col, stroke_width=7))
            self.play(LaggedStart(*[GrowFromEdge(m, DOWN) for m in marcas], lag_ratio=0.12), run_time=self.dur(1.0))
