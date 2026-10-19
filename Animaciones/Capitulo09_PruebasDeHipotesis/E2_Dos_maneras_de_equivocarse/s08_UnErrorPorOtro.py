"""Escena 08 — Comparar los tres errores; mover el umbral solo reparte el error entre las dos colas."""
from comun.escena import *
from comun.figuras_c9e2 import *


class UnErrorPorOtro(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.comparar()
        self.repartir()
        self.engano()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def comparar(self):
        B = Barras9([0.159, 0.30, 0.139], ["Umbral en 1", "Siempre 0", "Umbral en 1,42"], [ERROR, ERROR, ERROR],
                    xs=[-2.8, 0.0, 2.8], base_y=-2.6, esc=16.0, ancho=1.6, escala=0.45,
                    textos=["0,159", "0,30", "0,139"])
        eje_v = Line([-4.4, -2.6, 0], [-4.4, 2.9, 0], color=INK, stroke_width=2.4)
        tit = Text("Error", color=ERROR).scale(0.5).move_to([-4.4, 3.3, 0])
        top = B.barras[0].get_top()[1]
        pfa = MathTex(r"P_{FA} = 0{,}159", color=ERROR).scale(0.7).move_to([-2.8, top + 1.1, 0])
        pm = MathTex(r"P_M = 0{,}159", color=ERROR).scale(0.7).move_to([-2.8, top + 0.55, 0])

        with self.narrar("b1"):
            # «Comparemos»
            self.en("ejes")
            self.corte()
            self.play(Create(B.base), Create(eje_v), FadeIn(tit), run_time=self.dur(0.6))

            # «Con el umbral en uno»
            self.en("u1")
            self.play(GrowFromEdge(B.barras[0], DOWN), FadeIn(B.rots[0]), run_time=self.dur(0.6))

            # «las dos colas valen»
            self.en("colas")
            self.play(FadeIn(pfa, shift=DOWN * 0.15), FadeIn(pm, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «y el error también»
            self.en("tambien")
            self.play(ReplacementTransform(VGroup(pfa, pm), B.vals[0]), run_time=self.dur(0.6))

            # «Diciendo siempre cero»
            self.en("s0")
            self.play(GrowFromEdge(B.barras[1], DOWN), FadeIn(B.rots[1]), run_time=self.dur(0.7))

            # «el error es cero coma treinta»
            self.en("v030")
            self.pop(B.vals[1])

            # «Con el umbral en uno coma cuarenta y dos»
            self.en("u142")
            self.play(GrowFromEdge(B.barras[2], DOWN), FadeIn(B.rots[2]), run_time=self.dur(0.6))

            # «cero coma ciento treinta y nueve»
            self.en("v139")
            self.pop(B.vals[2])

            # «Es el menor»
            self.en("menor")
            self.play(B.barras[2].animate.set_fill(VERDE, 0.6).set_stroke(VERDE), B.vals[2].animate.set_color(VERDE),
                      run_time=self.dur(0.4))
            self.resaltar(B.barras[2], color=VERDE, escala=1.06)
            self.sfx("exito", gain=-20)

    # ------------------------------------------------------------ b2
    def repartir(self):
        C = Campanas9(centro=(0.0, -2.3), ancho=12.0, alto=7.2, r_rango=(-3.0, 7.0))
        u = ValueTracker(CRUCE9)
        d = ValueTracker(2.0)
        base = Line(C.p(-3), C.p(7), color=INK, stroke_width=2.4)
        c0 = C.campana(0, 1, C0)

        def c1_viva():
            return C.campana(d.get_value(), 1, C1)

        def colas_vivas():
            g = VGroup(C.area(0, 1, u.get_value(), 7), C.area(d.get_value(), 1, -3, u.get_value()))
            return g

        def umbral_vivo():
            return Line(C.p(u.get_value()), C.p(u.get_value()) + UP * 3.4, color=ESTIMACION, stroke_width=4)

        c1, colas, umb = always_redraw(c1_viva), always_redraw(colas_vivas), always_redraw(umbral_vivo)
        f_fa = Arrow(UP * 0.35, DOWN * 0.35, color=ERROR, stroke_width=5, buff=0).move_to(C.p(3.0, 0.16))
        f_m = Arrow(UP * 0.35, DOWN * 0.35, color=ERROR, stroke_width=5, buff=0).move_to(C.p(0.0, 0.2))
        tachas = VGroup(*[Line(f.get_corner(DL), f.get_corner(UR), color=ERROR, stroke_width=6) for f in (f_fa, f_m)])
        crece = Arrow(DOWN * 0.3, UP * 0.3, color=ERROR, stroke_width=5, buff=0).move_to(C.p(-1.6, 0.2))
        amp = Text("Más señal o menos ruido", color=ESTIMACION, weight=BOLD).scale(0.6).move_to([0, 3.3, 0])
        menos = MathTex(r"p_1 = 0{,}3", color=C1).scale(0.85).move_to(C.p(2.0) + UP * 3.75 + RIGHT * 1.6)
        self.vivos = (c1, colas, umb)

        with self.narrar("b2"):
            # «al mover el umbral»
            self.en("mover")
            self.corte()
            self.play(Create(base), Create(c0), FadeIn(c1), FadeIn(colas), FadeIn(umb), run_time=self.dur(0.5))

            # «una cola encoge»
            self.en("encoge")
            self.play(u.animate.set_value(1.9), run_time=self.dur(0.9))

            # «la otra crece»
            self.en("crece")
            self.play(u.animate.set_value(2.3), GrowArrow(crece), run_time=self.dur(0.8))

            # «No hay manera de bajar las dos»
            self.en("nohay")
            self.play(FadeOut(crece), u.animate.set_value(CRUCE9), run_time=self.dur(0.5))
            self.play(GrowArrow(f_fa), GrowArrow(f_m), run_time=self.dur(0.4))
            self.play(Create(tachas), run_time=self.dur(0.3))

            # «moviendo el umbral»
            self.en("vaiven")
            self.play(u.animate(rate_func=there_and_back).set_value(0.6), run_time=self.dur(1.2))

            # «separar las campanas»
            self.en("separar")
            self.play(FadeOut(f_fa), FadeOut(f_m), FadeOut(tachas), run_time=0.25)
            self.play(d.animate.set_value(4.6), u.animate.set_value(2.3), run_time=self.dur(1.2))

            # «más amplitud o menos ruido»
            self.en("amp")
            self.pop(amp)

            # «solo reparte el error»
            self.en("reparte")
            self.play(FadeOut(amp), d.animate.set_value(2.0), u.animate.set_value(CRUCE9), run_time=self.dur(1.0))

            # «lo carga sobre los unos»
            self.en("carga")
            borde = C.area(2, 1, -3, CRUCE9, opacidad=0.0).set_stroke(ESTIMACION, 5, opacity=1)
            self.play(Create(borde), run_time=self.dur(0.5))
            self.play(FadeOut(borde), run_time=self.dur(0.4))

            # «porque son menos»
            self.en("menos")
            self.pop(menos)

    # ------------------------------------------------------------ b3
    def engano(self):
        for m in self.vivos:
            m.clear_updaters()
        tot = MathTex(r"P_e\ \text{m\'inima}", color=TXT).scale(1.1).move_to([0, 1.0, 0])
        ok = tilde(VERDE, 1.0).move_to([0, -0.5, 0])
        duda = Text("?", color=ESTIMACION, weight=BOLD).scale(1.8).move_to([1.1, 0.1, 0])
        tira = tira_test07(0.8).move_to([8.5, -0.3, 0])

        with self.narrar("b3"):
            # «Minimizar el total»
            self.en("total")
            self.corte()
            self.play(Write(tot), Create(ok), run_time=self.dur(0.7))

            # «¿es siempre lo que queremos?»
            self.en("pregunta")
            self.pop(duda)

            # «un ejemplo que ya conoces»
            self.en("ejemplo")
            self.play(tira.animate.move_to([4.8, -0.3, 0]), run_time=self.dur(0.6))

            # «el total engaña»
            self.en("engana")
            self.play(Create(tachar(ok)), run_time=self.dur(0.4))
            self.sfx("error", gain=-20)
