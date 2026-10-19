"""Escena 10 — Medir contando: la fracción de fallos tiene su propio error, raíz de p(1 − p)/N."""
from comun.escena import *
from comun.figuras_c9e6 import *

P_ERR = Q(1.0)          # 0,159: umbral en 1 con a priori iguales


def fraccion_fallos(n: int = 10000, semilla: int = 7) -> np.ndarray:
    """Fracción acumulada de fallos en n pruebas con probabilidad 0,159."""
    rng = np.random.default_rng(semilla)
    f = rng.random(n) < P_ERR
    return np.cumsum(f) / np.arange(1, n + 1)


class MedirContando(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.contar()
        self.error_tipico()
        self.diez_mil()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def contar(self):
        with self.narrar("b1"):
            # «Una última cuestión práctica»
            self.en("practica")
            C = campanas_izq9()
            eje = eje_izq9(C)
            c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
            u = Line(C.p(1) + DOWN * 0.1, C.p(1) + UP * 2.9, color=ESTIMACION, stroke_width=4)
            self.play(FadeIn(eje), Create(c0), Create(c1), Create(u), run_time=self.dur(0.7))
            self.camp = VGroup(eje, c0, c1, u)
            self.C = C

            # «Las probabilidades de error»
            self.en("perror")
            pe = MathTex(r"P(\text{error}) = \ ?", color=ERROR).scale(0.85).move_to([-3.75, 3.3, 0])
            self.play(Write(pe), run_time=self.dur(0.5))
            self.pe = pe

            # «se miden contando»
            self.en("contando")
            rng = np.random.default_rng(11)
            # veinte pruebas, mitad de cada bit; tres caen del lado equivocado del umbral (fallos)
            malos = {3, 8, 15}
            bits = []
            for i in range(20):
                b = i % 2
                r = float(rng.normal(2 * b, 0.8))
                bien = (r > 1) == bool(b)
                if (i in malos) == bien:            # forzar el lado que toca
                    r = 2 - r if abs(r - 1) > 0.15 else (1.4 if (i in malos) != bool(b) else 0.6)
                    if (i in malos) == ((r > 1) == bool(b)):
                        r = 1.4 if ((i in malos) != bool(b)) else 0.6
                bits.append((b, float(np.clip(r, -2.6, 4.6))))
            puntos = VGroup(*[Dot(C.p(r, 0.42), radius=0.08, color=C1 if b else C0) for b, r in bits])
            anims = [Succession(FadeIn(d, run_time=0.3),
                                d.animate(run_time=0.4).move_to(C.p(r, 0.02)).set_color(ERROR if i in malos else VERDE))
                     for i, (d, (b, r)) in enumerate(zip(puntos, bits))]
            self.play(LaggedStart(*anims, lag_ratio=0.12), run_time=self.dur(1.8))
            self.puntos = puntos

            # «cuántas salen mal»
            self.en("contador")
            cont = MathTex(r"\frac{\text{Fallos}}{\text{Pruebas}} = \frac{3}{20}", color=TXT).scale(0.75)
            cont.move_to([-3.75, 2.3, 0])
            self.play(FadeIn(cont, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «el promedio del capítulo siete»
            self.en("cap7")
            c7 = etiqueta("Grandes números · Capítulo 7", INK, 0.4).move_to([3.6, 3.3, 0])
            self.play(FadeIn(c7), run_time=self.dur(0.35))

            # «al crecer el número de pruebas»
            self.en("crece")
            L = Lienzo(ancho=5.2, alto=8.0, t_rango=(1.0, 4.0), v_max=0.4, centro=(3.75, -2.3))
            base = L.base()
            vert = Line(L.p(1.0, 0), L.p(1.0, 0.4), color=INK, stroke_width=1.6)
            nums = VGroup(*[Text(t, color=INK).scale(0.36).next_to(L.p(k, 0), DOWN, buff=0.12)
                            for k, t in ((1, "10"), (2, "100"), (3, "1.000"), (4, "10.000"))])
            rn = Text("Pruebas", color=INK).scale(0.4).next_to(nums, DOWN, buff=0.12)
            fr = fraccion_fallos()
            ks = np.unique(np.geomspace(10, 10000, 260).astype(int))
            curva = L.curva(np.log10(ks), fr[ks - 1], ERROR, 3.5)
            self.play(FadeIn(base), FadeIn(vert), FadeIn(nums), FadeIn(rn), self.puntos.animate.set_opacity(0.4),
                      run_time=self.dur(0.35))
            self.play(Create(curva), run_time=self.dur(2.4), rate_func=linear)

            # «se acerca a la probabilidad real»
            self.en("real")
            ref = DashedLine(L.p(1.0, P_ERR), L.p(4.0, P_ERR), color=TXT, stroke_width=2.5, dash_length=0.1)
            rr = Text("0,159", color=TXT).scale(0.42).next_to(ref, RIGHT, buff=0.1).shift(LEFT * 0.4 + UP * 0.25)
            self.play(Create(ref), FadeIn(rr), run_time=self.dur(0.5))
            self.graf = VGroup(base, vert, nums, rn, curva, ref, rr)

            # «La pregunta es»
            self.en("pregunta")
            self.play(FadeOut(c7), self.graf.animate.scale(0.5).move_to([4.9, 2.2, 0]), run_time=self.dur(0.5))

            # «cuántas pruebas hacen falta»
            self.en("cuantas")
            nq = MathTex(r"N = \ ?", color=ESTIMACION).scale(1.0).move_to([3.0, -0.5, 0])
            self.pop(nq)
            self.nq, self.cont = nq, cont

    # ------------------------------------------------------------ b2
    def error_tipico(self):
        with self.narrar("b2"):
            # «su propio error»
            self.en("error")
            self.play(FadeOut(self.camp), FadeOut(self.puntos), FadeOut(self.pe), FadeOut(self.cont), FadeOut(self.nq),
                      run_time=self.dur(0.35))
            et = Text("Error típico =", color=ERROR, weight=BOLD).scale(0.6).move_to([-4.6, 1.8, 0])
            self.play(FadeIn(et, shift=RIGHT * 0.15), run_time=self.dur(0.3))

            x0 = et.get_right() + RIGHT * 0.25

            def raiz(tex):
                return MathTex(tex, color=TXT).scale(1.05).move_to(x0, aligned_edge=LEFT)

            # «la raíz cuadrada»
            self.en("raiz")
            f = raiz(r"\sqrt{\quad\ \ }")
            self.play(Write(f), run_time=self.dur(0.4))
            # «de pe»
            self.en("p")
            g = raiz(r"\sqrt{p\ \ }")
            self.play(ReplacementTransform(f, g), run_time=self.dur(0.3))
            # «uno menos pe»
            self.en("unomenos")
            h = raiz(r"\sqrt{p\,(1-p)}")
            self.play(ReplacementTransform(g, h), run_time=self.dur(0.4))
            # «el número de pruebas»
            self.en("n")
            k = raiz(r"\sqrt{p\,(1-p)\,/\,N}")
            self.play(ReplacementTransform(h, k), run_time=self.dur(0.4))
            self.f = k

            # «nuestro cero coma ciento cincuenta y nueve»
            self.en("p159")
            p159 = MathTex(r"p = 0{,}159", color=TXT).scale(0.8).move_to([-5.0, 0.5, 0])
            self.play(FadeIn(p159, shift=UP * 0.1), run_time=self.dur(0.35))

            # «con cien pruebas»
            self.en("cien")
            n100 = MathTex(r"N = 100", color=TXT).scale(0.8).move_to([-5.0, -0.2, 0])
            self.play(FadeIn(n100, shift=UP * 0.1), run_time=self.dur(0.35))

            # «cero coma cero treinta y siete»
            self.en("e037")
            e = MathTex(r"\pm\, 0{,}037", color=ERROR).scale(0.9).move_to([-2.4, -0.2, 0])
            self.pop(e)
            x0e, x1e, y = -3.6, 3.6, -1.7
            px = lambda v: np.array([x0e + (v - 0.10) / 0.12 * (x1e - x0e), y, 0])
            self.px = px
            eje = Line(px(0.10), px(0.22), color=INK, stroke_width=2.5)
            centro = Dot(px(P_ERR), radius=0.08, color=TXT)
            rc = Text("0,159", color=TXT).scale(0.38).next_to(centro, UP, buff=0.25)
            barra = Rectangle(width=px(P_ERR + 0.037)[0] - px(P_ERR - 0.037)[0], height=0.22, stroke_width=0)
            barra.set_fill(ERROR, 0.55).move_to(px(P_ERR))
            self.play(Create(eje), FadeIn(barra), FadeIn(centro), FadeIn(rc), run_time=self.dur(0.5))

            # «un doce por ciento»
            self.en("doce")
            r12 = Text("0,12", color=ERROR).scale(0.42).next_to(px(P_ERR - 0.037), DOWN, buff=0.25)
            self.play(FadeIn(r12, shift=UP * 0.1), run_time=self.dur(0.3))
            # «o un veinte»
            self.en("veinte")
            r20 = Text("0,20", color=ERROR).scale(0.42).next_to(px(P_ERR + 0.037), DOWN, buff=0.25)
            self.play(FadeIn(r20, shift=UP * 0.1), run_time=self.dur(0.3))

    # ------------------------------------------------------------ b3
    def diez_mil(self):
        px = self.px
        with self.narrar("b3"):
            # «Con diez mil pruebas»
            self.en("diezmil")
            y = -3.1
            n2 = MathTex(r"N = 10.000", color=TXT).scale(0.7).move_to([-5.3, y, 0])
            eje = Line([px(0.10)[0], y, 0], [px(0.22)[0], y, 0], color=INK, stroke_width=2.5)
            ancha = Rectangle(width=px(P_ERR + 0.037)[0] - px(P_ERR - 0.037)[0], height=0.22, stroke_width=0)
            ancha.set_fill(ERROR, 0.55).move_to([px(P_ERR)[0], y, 0])
            self.play(FadeIn(n2), Create(eje), FadeIn(ancha), run_time=self.dur(0.5))

            # «cero coma cero cero cuatro»
            self.en("e004")
            fina = Rectangle(width=px(P_ERR + 0.004)[0] - px(P_ERR - 0.004)[0], height=0.22, stroke_width=0)
            fina.set_fill(ERROR, 0.85).move_to(ancha)
            e2 = MathTex(r"\pm\, 0{,}004", color=ERROR).scale(0.8).next_to(fina, RIGHT, buff=0.5).shift(UP * 0.45)
            self.play(ReplacementTransform(ancha, fina), FadeIn(e2), run_time=self.dur(0.6))

            # «Por la raíz cuadrada»
            self.en("porraiz")
            self.play(self.f.animate(rate_func=there_and_back).set_color(ESTIMACION).scale(1.12), run_time=self.dur(0.6))

            # «diez veces más precisión»
            self.en("precision")
            pr = Text("Precisión × 10", color=VERDE, weight=BOLD).scale(0.55).move_to([3.6, 0.6, 0])
            self.pop(pr)
            # «cien veces más pruebas»
            self.en("pruebas")
            pb = Text("= Pruebas × 100", color=ESTIMACION, weight=BOLD).scale(0.55).next_to(pr, DOWN, buff=0.25)
            self.pop(pb)
