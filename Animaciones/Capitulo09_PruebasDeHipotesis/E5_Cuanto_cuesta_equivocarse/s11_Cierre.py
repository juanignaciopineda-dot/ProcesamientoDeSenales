"""Escena 11 — Cierre: con costes distintos se minimiza el coste; el umbral baja; anuncia el episodio 6."""
from comun.escena import *
from comun.figuras_c9e5 import *

XT = 2.6


class Cierre(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.resumen()
        self.anuncio()
        self.wait(1.2)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resumen(self):
        with self.narrar("b1"):
            # «cuando un error cuesta más que el otro»
            self.en("balanza")
            b = Balanza(centro=(-4.2, 2.4), semi=1.5)
            x5 = Text("× 5", color=ERROR, weight=BOLD).scale(0.6).move_to([-4.2, 0.65, 0])
            self.play(FadeIn(b), run_time=self.dur(0.35))
            self.play(*b.inclinar("der", ang=0.3), FadeIn(x5), run_time=self.dur(0.5))

            # «no se minimiza la probabilidad de error»
            self.en("tacha")
            t1 = Text("Mínimo error", color=INK).scale(0.55).move_to([XT, 3.1, 0])
            self.play(FadeIn(t1), run_time=self.dur(0.3))
            self.play(Create(tachar(t1)), run_time=self.dur(0.3))

            # «el coste esperado»
            self.en("coste")
            t2 = Text("Mínimo coste esperado", color=VERDE, weight=BOLD).scale(0.6).move_to([XT, 2.3, 0])
            self.pop(t2)

            # «la razón de verosimilitud»
            self.en("lambda")
            lrt = MathTex(r"\Lambda(r)", r"\gtrless", r"\eta", color=TXT).scale(0.95).move_to([XT, 1.35, 0])
            lrt[2].set_color(AMBAR)
            self.play(FadeIn(lrt, shift=DOWN * 0.15), run_time=self.dur(0.4))

            # «solo que más bajo»
            self.en("bajo")
            C = campanas_e5(centro=(-1.8, -3.3), ancho=7.6, alto=3.6)
            eje = C.eje((0, 1, 2), rotulo=False, escala=0.4)
            c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
            u = ValueTracker(U_MAP)
            linea = always_redraw(lambda: umbral9_e5(C, u.get_value(), alto=2.0))
            self.play(FadeIn(VGroup(eje, c0, c1)), FadeIn(linea), run_time=self.dur(0.4))
            self.play(u.animate.set_value(U_R), run_time=self.dur(0.9))
            linea.clear_updaters()

            # «cero coma sesenta y dos»
            self.en("u062")
            n062 = Text("0,62", color=AMBAR, weight=BOLD).scale(0.45).next_to(linea, UP, buff=0.1)
            self.pop(n062)

            # «uno coma cuarenta y dos»
            self.en("u142")
            n142 = Text("1,42", color=INK).scale(0.45).next_to(n062, RIGHT, buff=0.5)
            self.play(FadeIn(n142), run_time=self.dur(0.25))
            self.play(Create(tachar(n142)), run_time=self.dur(0.3))

            # «Con el cuadrado del error»
            self.en("cuadrado")
            ax = Line([3.6, -2.6, 0], [5.6, -2.6, 0], color=INK, stroke_width=2)
            par = FunctionGraph(lambda x: -2.6 + 0.9 * (x - 4.6) ** 2, x_range=[3.75, 5.45], color=ERROR,
                                stroke_width=4)
            e2 = MathTex(r"\text{Error}^2", color=ERROR).scale(0.65).move_to([4.6, -0.6, 0])
            self.play(Create(ax), Create(par), FadeIn(e2), run_time=self.dur(0.5))

            # «sirve para estimar»
            self.en("estimar")
            mc = Text("→ Media condicional", color=VERDE).scale(0.48).move_to([4.6, -3.25, 0])
            self.play(FadeIn(mc, shift=RIGHT * 0.2), run_time=self.dur(0.4))
            self.campanas = VGroup(eje, c0, c1, linea, n062, n142)

    # ------------------------------------------------------------ b2
    def anuncio(self):
        with self.narrar("b2"):
            # «sin campanas»
            self.en("sin")
            self.corte(self.campanas)
            self.play(FadeOut(self.campanas), run_time=self.dur(0.5))

            # «ni curva, ni umbral»
            self.en("ni")
            fichas = VGroup(MathTex(r"\Lambda(r)", color=TXT).scale(1.0), Text("Curva", color=TXT).scale(0.6),
                            Text("Umbral", color=TXT).scale(0.6)).arrange(RIGHT, buff=1.4).move_to([0, 2.2, 0])
            self.play(FadeIn(fichas), run_time=self.dur(0.3))
            for f in fichas:
                self.play(Create(tachar(f)), run_time=self.dur(0.25))

            # «una lista de casos»
            self.en("lista")
            L = lista_casos9(centro=(0.0, 0.3), lado=0.85)
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.2) for c in L], lag_ratio=0.12), run_time=self.dur(0.8))

            # «en el próximo episodio»
            self.en("proximo")
            tj = caja("Episodio 6 · Decidir con datos de verdad", ROC, alto=0.9, scale=0.55).move_to([0, -2.2, 0])
            self.play(FadeIn(tj, shift=UP * 0.2), run_time=self.dur(0.5))
            self.resaltar(tj, color=ROC)
