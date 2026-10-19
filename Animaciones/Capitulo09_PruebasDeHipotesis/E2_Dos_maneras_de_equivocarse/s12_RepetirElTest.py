"""Escena 12 — Repetir el test encadena Bayes: 1 % → 17 % → 80 % → 99 %."""
from comun.escena import *
from comun.figuras_c9e2 import *


class RepetirElTest(EscenaCurso):
    ESCENA = "12"

    Y_CADENA = 3.0

    def construct(self):
        self.segunda_prueba()
        self.tercera()
        self.leccion()
        self.wait(1.0)
        self.limpiar()

    def _test(self, x: float) -> VGroup:
        return casilla9("Test +", MEDIDA, ancho=1.5, alto=0.7, escala=0.45).move_to([x, self.Y_CADENA, 0])

    def _flecha(self, x0: float, x1: float) -> Arrow:
        return Arrow([x0, self.Y_CADENA, 0], [x1, self.Y_CADENA, 0], buff=0, color=INK, stroke_width=3,
                     max_tip_length_to_length_ratio=0.3)

    def _valor(self, txt: str, x: float, color=TXT) -> Text:
        return Text(txt, color=color, weight=BOLD).scale(0.55).move_to([x, self.Y_CADENA, 0])

    # ------------------------------------------------------------ b1
    def segunda_prueba(self):
        # cadena: 1 % → [Test +] → 17 % → [Test +] → ? → [Test +] → ?
        xs = dict(v0=-6.3, t1=-4.65, v1=-3.0, t2=-1.35, v2=0.3, t3=1.95, v3=3.6)
        self.xs = xs
        tira = tira_test07(0.8).move_to([0, 0.3, 0])
        duda = Text("?", color=ESTIMACION, weight=BOLD).scale(1.6).move_to([1.2, 1.1, 0])
        v0 = self._valor("1 %", xs["v0"])
        t1 = self._test(xs["t1"])
        v1 = self._valor("17 %", xs["v1"], ESTIMACION)
        f01 = self._flecha(xs["v0"] + 0.35, xs["t1"] - 0.8)
        f11 = self._flecha(xs["t1"] + 0.8, xs["v1"] - 0.5)
        paso = CurvedArrow([xs["v0"], self.Y_CADENA - 0.4, 0], [xs["v1"], self.Y_CADENA - 0.4, 0], angle=PI / 3,
                           color=VERDE, stroke_width=4)
        apriori = Text("Nueva a priori", color=ESTIMACION).scale(0.4).move_to([xs["v1"], self.Y_CADENA - 0.65, 0])
        t2 = self._test(xs["t2"])
        f12 = self._flecha(xs["v1"] + 0.5, xs["t2"] - 0.8)
        f22 = self._flecha(xs["t2"] + 0.8, xs["v2"] - 0.4)
        self.q2 = self._valor("?", xs["v2"], ESTIMACION)
        perp = MathTex(r"\perp", color=INK).scale(0.9).move_to([(xs["t1"] + xs["t2"]) / 2, self.Y_CADENA + 0.7, 0])
        raiz = casilla9("1.000 personas", INK, ancho=2.8, alto=0.7, escala=0.45).move_to([-4.6, -0.5, 0])
        enf = casilla9("167 enfermas", C1, ancho=2.6, alto=0.7, escala=0.45).move_to([-0.6, 0.5, 0])
        san = casilla9("833 sanas", C0, ancho=2.6, alto=0.7, escala=0.45).move_to([-0.6, -1.5, 0])
        p165 = Text("→ 165 positivos", color=C1).scale(0.48).move_to([3.3, 0.5, 0])
        p42 = Text("→ 42 positivos", color=ERROR).scale(0.48).move_to([3.3, -1.5, 0])
        l_e = Line(raiz.get_right(), enf.get_left(), color=INK, stroke_width=3)
        l_s = Line(raiz.get_right(), san.get_left(), color=INK, stroke_width=3)
        self.cadena = VGroup(v0, t1, v1, f01, f11, t2, f12, f22, perp)
        self.arbol = VGroup(raiz, enf, san, p165, p42, l_e, l_s)

        with self.narrar("b1"):
            # «¿Entonces el test no sirve?»
            self.en("nosirve")
            self.play(FadeIn(tira, shift=UP * 0.2), run_time=self.dur(0.4))
            self.pop(duda)

            # «Sí sirve»
            self.en("sisirve")
            self.play(FadeOut(tira), FadeOut(duda), run_time=0.25)
            self.play(FadeIn(v0), GrowArrow(f01), FadeIn(t1), run_time=self.dur(0.6))
            self.play(GrowArrow(f11), FadeIn(v1), run_time=self.dur(0.5))

            # «has pasado del uno al diecisiete»
            self.en("paso")
            self.play(Create(paso), run_time=self.dur(0.7))

            # «Y ese diecisiete»
            self.en("ese")
            self.resaltar(v1, color=ESTIMACION, escala=1.25)

            # «tu nueva probabilidad a priori»
            self.en("nueva")
            self.play(FadeOut(paso), FadeIn(apriori, shift=UP * 0.15), run_time=self.dur(0.5))

            # «Repite el test»
            self.en("repite")
            self.play(GrowArrow(f12), FadeIn(t2), run_time=self.dur(0.5))
            self.play(GrowArrow(f22), FadeIn(self.q2), run_time=self.dur(0.4))

            # «no dependen de la primera vez»
            self.en("indep")
            self.pop(perp)

            # «De mil personas como tú»
            self.en("mil")
            self.play(FadeIn(raiz, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «ciento sesenta y siete están enfermas»
            self.en("e167")
            self.play(Create(l_e), FadeIn(enf, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «ciento sesenta y cinco positivos»
            self.en("p165")
            self.play(FadeIn(p165, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «ochocientas treinta y tres»
            self.en("s833")
            self.play(Create(l_s), FadeIn(san, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «dan cuarenta y dos»
            self.en("p42")
            self.play(FadeIn(p42, shift=RIGHT * 0.2), run_time=self.dur(0.4))
        self.apriori = apriori

    # ------------------------------------------------------------ b2
    def tercera(self):
        xs = self.xs
        div = Text("165 / 207", color=TXT).scale(0.7).move_to([0, -2.9, 0])
        v2 = self._valor("80 %", xs["v2"], ESTIMACION)
        t3 = self._test(xs["t3"])
        f23 = self._flecha(xs["v2"] + 0.5, xs["t3"] - 0.8)
        f33 = self._flecha(xs["t3"] + 0.8, xs["v3"] - 0.4)
        q3 = self._valor("?", xs["v3"], ESTIMACION)
        v3 = self._valor("99 %", xs["v3"], VERDE)
        marco = SurroundingRectangle(v3, color=VERDE, buff=0.15, stroke_width=4)
        tiras = VGroup(tira_test07(0.6), tira_test07(0.6)).arrange(RIGHT, buff=1.2).move_to([0, -0.6, 0])
        oks = VGroup(*[tilde(VERDE, 0.5).next_to(t, DOWN, buff=0.2) for t in tiras])
        rng = np.random.default_rng(7)
        multitud = VGroup(*[Dot([x, y, 0], radius=0.04, color=INK)
                            for x, y in zip(rng.uniform(-3.4, 3.4, 400), rng.uniform(-1.9, 0.6, 400))])
        masiva = Text("Prueba masiva", color=TXT, weight=BOLD).scale(0.55).move_to([0, -2.6, 0])

        with self.narrar("b2"):
            # «Ciento sesenta y cinco de doscientos siete»
            self.en("div")
            self.play(Write(div), run_time=self.dur(0.6))

            # «un ochenta por ciento»
            self.en("ochenta")
            self.play(ReplacementTransform(self.q2, v2), run_time=self.dur(0.5))

            # «Con un tercer positivo»
            self.en("tercer")
            self.play(GrowArrow(f23), FadeIn(t3), run_time=self.dur(0.5))
            self.play(GrowArrow(f33), FadeIn(q3), run_time=self.dur(0.4))

            # «un noventa y nueve»
            self.en("v99")
            self.play(ReplacementTransform(q3, v3), run_time=self.dur(0.4))
            self.play(Create(marco), run_time=self.dur(0.3))

            # «se confirma con otra prueba»
            self.en("confirma")
            self.play(FadeOut(self.arbol), FadeOut(div), run_time=0.3)
            self.play(FadeIn(tiras, shift=UP * 0.2), run_time=self.dur(0.4))
            self.play(Create(oks), run_time=self.dur(0.4))

            # «pruebas masivas»
            self.en("masivas")
            self.play(FadeOut(tiras), FadeOut(oks), run_time=0.25)
            self.play(FadeIn(multitud, lag_ratio=0.005), FadeIn(masiva), run_time=self.dur(0.7))
            self.play(Create(tachar(masiva)), run_time=self.dur(0.3))

    # ------------------------------------------------------------ b3
    def leccion(self):
        radar = radar13().scale(1.0).move_to([-4.4, 1.9, 0])
        canal = canal9(centro=(3.9, 1.9), ancho=3.4, escala=0.65)
        fad = MathTex("P_{FA}", r"\quad", "P_D", color=TXT).scale(0.9).move_to([0, 1.9, 0])
        fad[0].set_color(ERROR)
        fad[2].set_color(VERDE)
        det = casilla9("El detector: Falsa alarma y Detección", INK, ancho=8.6, alto=0.9, escala=0.5).move_to([0, 0.0, 0])
        creer = casilla9("Cuánto creerle", ESTIMACION, ancho=8.6, alto=0.9, escala=0.5).move_to([0, -1.6, 0])
        frec = Text("Además, lo frecuente que es", color=ESTIMACION).scale(0.5).move_to([0, -2.75, 0])

        with self.narrar("b3"):
            # «un radar o un receptor»
            self.en("radar")
            self.corte()
            self.play(FadeIn(radar, shift=RIGHT * 0.2), FadeIn(canal, shift=LEFT * 0.2), run_time=self.dur(0.6))

            # «La falsa alarma y la detección»
            self.en("fad")
            self.play(Write(fad), run_time=self.dur(0.5))

            # «describen al detector»
            self.en("detector")
            self.play(FadeIn(det, shift=UP * 0.2), run_time=self.dur(0.5))

            # «cuánto creerle»
            self.en("creer")
            self.play(FadeIn(creer, shift=UP * 0.2), run_time=self.dur(0.5))

            # «lo frecuente que sea lo que busca»
            self.en("frec")
            self.play(FadeIn(frec, shift=UP * 0.15), run_time=self.dur(0.5))
