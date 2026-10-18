"""Escena 05 — Repaso de probabilidad: experimento aleatorio y probabilidad como frecuencia."""
from comun.escena import *


class RepasoExperimento(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.bloque_experimento()
        self.bloque_frecuencia()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bloque_experimento(self):
        with self.narrar("b1"):
            # «el repaso de Probabilidad y Estadística»
            self.en("repaso2")
            tit = Text("Probabilidad y Estadística", color=TXT, weight=BOLD).scale(0.8)
            ic = dado_n(4).scale(0.6)
            cab = VGroup(ic, tit).arrange(RIGHT, buff=0.35).move_to([0, 3.3, 0])
            self.pop(cab)

            # «Un experimento aleatorio»
            self.en("experimento")
            exp = caja("Experimento aleatorio", AMBAR, ancho=4.6, alto=1.1, scale=0.6).move_to([0, 1.3, 0])
            self.pop(exp)

            # «no puedes saber de antemano»
            self.en("no_saber")
            q = Text("?", color=ROJO, weight=BOLD).scale(1.6).move_to([3.4, 1.3, 0])
            self.pop(q)

            # «en las mismas condiciones»
            self.en("mismas")
            res = VGroup(*[caja(txt, SENAL, ancho=1.5, alto=0.7, scale=0.5) for txt in ("Cara", "Cruz", "Cruz")])
            res.arrange(RIGHT, buff=0.8).move_to([0, -0.6, 0])
            flechas = VGroup(*[Arrow(exp.get_bottom(), r.get_top(), color=INK, stroke_width=3, buff=0.1,
                                     max_tip_length_to_length_ratio=0.2) for r in res])
            self.play(LaggedStart(*[GrowArrow(f) for f in flechas], lag_ratio=0.2),
                      LaggedStart(*[FadeIn(r) for r in res], lag_ratio=0.2), run_time=self.dur(0.9))

            # «lanzar una moneda»
            self.en("moneda")
            mon = moneda().scale(0.9).move_to([-3.8, -2.7, 0])
            self.pop(mon)

            # «tirar un dado»
            self.en("dado")
            dd = dado_n(5).move_to([0, -2.7, 0])
            self.pop(dd)

            # «medir el ruido de un aparato»
            self.en("ruido")
            Lr = Lienzo(ancho=2.6, alto=1.0, t_rango=(0, 1), v_max=1.5, centro=(3.8, -2.7))
            cr = Lr.curva(np.linspace(0, 1, 120), serie(3, 120, 0.4), RUIDO, 3.0)
            self.play(Create(cr), run_time=self.dur(0.8), rate_func=linear)

    # ------------------------------------------------------------ b2
    def bloque_frecuencia(self):
        lx, fx = fraccion_caras7()
        L = Lienzo(ancho=7.0, alto=3.0, t_rango=(1, 4), v_max=0.5, centro=(2.6, -0.5))

        with self.narrar("b2"):
            # «La probabilidad de un resultado»
            self.en("prob")
            self.corte()
            mon = moneda().scale(1.5).move_to([-4.8, 0.9, 0])
            pro = Text("Probabilidad", color=AMBAR, weight=BOLD).scale(0.65).move_to([-4.8, 2.1, 0])
            self.pop(VGroup(mon, pro))

            # «la fracción de veces»
            self.en("fraccion")
            num_ = Text("Veces que sale", color=TXT).scale(0.5)
            lin = Line(LEFT * 1.4, RIGHT * 1.4, color=TXT, stroke_width=3)
            den = Text("Veces que repites", color=TXT).scale(0.5)
            fr = VGroup(num_, lin, den).arrange(DOWN, buff=0.12).move_to([-4.8, -1.0, 0])
            self.pop(fr)

            # «muchísimas veces»
            self.en("muchas")
            ejes_ = VGroup(Line(L.p(1, -0.5), L.p(1, 0.5), color=INK, stroke_width=2.5),
                           Line(L.p(1, -0.5), L.p(4, -0.5), color=INK, stroke_width=2.5))
            xl = Text("Lanzamientos", color=INK).scale(0.45).move_to([2.6, -2.55, 0])
            self.play(Create(ejes_), FadeIn(xl), run_time=self.dur(0.6))

            # «diez veces»
            self.en("diez")
            fila = fila_monedas7(7, 10, centro=(2.6, 3.2), paso=0.5)
            self.play(LaggedStart(*[GrowFromCenter(m) for m in fila.monedas], lag_ratio=0.06), run_time=self.dur(0.8))

            # «siete caras»
            self.en("siete")
            t7 = Text("7/10 = 0,7", color=AMBAR, weight=BOLD).scale(0.6).move_to([2.6, 2.4, 0])
            p0 = Dot(L.p(lx[0], fx[0] - 0.5), radius=0.1, color=AMBAR)
            self.pop(t7)
            self.play(FadeIn(p0), run_time=0.25)

            # «Lánzala diez mil»
            self.en("diez_mil")
            curva = L.curva(lx, fx - 0.5, AMBAR, 4.0)
            n10k = Text("10.000", color=INK).scale(0.45).move_to(L.p(4, -0.5) + DOWN * 0.3)
            self.play(FadeOut(fila), FadeOut(t7), Create(curva), FadeIn(n10k), run_time=self.dur(1.6), rate_func=linear)

            # «se pega al cincuenta por ciento»
            self.en("cincuenta")
            lin5 = DashedLine(L.p(1, 0), L.p(4, 0), color=VERDE, stroke_width=3)
            l5 = Text("0,5", color=VERDE, weight=BOLD).scale(0.5).next_to(L.p(1, 0), LEFT, buff=0.15)
            self.play(Create(lin5), FadeIn(l5), run_time=self.dur(0.5))

            # «Ese número»
            self.en("ese_numero")
            self.play(lin5.animate(rate_func=there_and_back).set_stroke(width=8),
                      l5.animate(rate_func=there_and_back).scale(1.4), run_time=self.dur(0.8))

            # «es la probabilidad»
            self.en("es_prob")
            ep = Text("Probabilidad = 0,5", color=VERDE, weight=BOLD).scale(0.65).move_to([2.6, -3.3, 0])
            self.pop(ep)
