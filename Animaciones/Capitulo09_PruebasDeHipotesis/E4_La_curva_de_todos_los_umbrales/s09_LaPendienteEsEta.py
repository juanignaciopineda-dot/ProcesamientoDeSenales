"""Escena 09 — La pendiente de la ROC es la razón de verosimilitud en el umbral: eta. Comprobación con cuatro umbrales."""
from comun.escena import *
from comun.figuras_c9e4 import *

UMBRALES = [(1.5, "1{,}5", "e^{1}", "2{,}72"), (1.0, "1", "e^{0}", "1"),
            (0.5, "0{,}5", "e^{-1}", "0{,}37"), (0.0, "0", "e^{-2}", "0{,}135")]


class LaPendienteEsEta(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.P = PlanoRoc9(origen=(1.2, -3.3), lado=4.0, escala=0.4)
        self.cociente()
        self.comprobar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def cociente(self):
        P = self.P
        with self.narrar("b1"):
            # «lo que sube entre lo que avanza»
            self.en("cociente")
            izq = MathTex(r"\text{Pendiente} =", color=TXT).scale(0.9)
            arriba = MathTex("f_1", r"\cdot", r"\text{Ancho}", color=DET).scale(0.9)
            abajo = MathTex("f_0", r"\cdot", r"\text{Ancho}", color=FA).scale(0.9)
            barra = Line(LEFT * 1.2, RIGHT * 1.2, color=TXT, stroke_width=3)
            frac = VGroup(arriba, barra, abajo).arrange(DOWN, buff=0.15)
            fila = VGroup(izq, frac).arrange(RIGHT, buff=0.3).move_to([0, 2.35, 0])
            self.play(FadeIn(izq), run_time=self.dur(0.3))
            self.play(FadeIn(arriba, shift=DOWN * 0.15), run_time=self.dur(0.35))
            self.play(Create(barra), FadeIn(abajo, shift=UP * 0.15), run_time=self.dur(0.4))

            # «Los anchos se cancelan»
            self.en("cancela")
            tc = VGroup(tachar(VGroup(arriba[1], arriba[2])), tachar(VGroup(abajo[1], abajo[2])))
            self.play(Create(tc), run_time=self.dur(0.4))
            self.play(FadeOut(tc), FadeOut(arriba[1:]), FadeOut(abajo[1:]), run_time=self.dur(0.3))
            f1, f0 = arriba[0], abajo[0]
            barra2 = Line(LEFT * 0.35, RIGHT * 0.35, color=TXT, stroke_width=3).move_to(barra)
            self.play(f1.animate.move_to(barra.get_center() + UP * 0.38),
                      f0.animate.move_to(barra.get_center() + DOWN * 0.38),
                      Transform(barra, barra2), run_time=self.dur(0.5))

            # «la altura de la campana del uno»
            self.en("f1")
            self.play(f1.animate(rate_func=there_and_back).scale(1.3), run_time=self.dur(0.45))

            # «la altura de la campana del cero»
            self.en("f0")
            self.play(f0.animate(rate_func=there_and_back).scale(1.3), run_time=self.dur(0.45))

            # «La razón de verosimilitud»
            self.en("lambda")
            lam = MathTex(r"= \Lambda(\text{umbral})", color=ROC).scale(0.9).next_to(barra, RIGHT, buff=0.3)
            self.pop(lam)
            self.fila = VGroup(izq, arriba, barra, abajo, lam)

            # «en cada punto»
            self.en("punto")
            cur = P.curva()
            self.play(FadeIn(P), Create(cur), run_time=self.dur(0.6))
            tg = P.tangente(1.0, largo=0.5, color=TXT, ancho=4)
            dot = P.punto(*roc9(1.0), color=TXT)
            self.play(FadeIn(dot, scale=0.4), Create(tg), run_time=self.dur(0.3))
            self.tg1 = VGroup(tg, dot)

            # «el umbral eta»
            self.en("eta")
            final = MathTex(r"\text{Pendiente} = \Lambda \text{ en el umbral} = \eta", color=ROC).scale(0.9)
            final.move_to([0, 2.6, 0])
            marco = SurroundingRectangle(final, color=ROC, buff=0.18, stroke_width=4)
            self.play(FadeOut(self.fila), FadeIn(final), run_time=self.dur(0.6))
            self.play(Create(marco), run_time=self.dur(0.4))

    # ------------------------------------------------------------ b2
    def comprobar(self):
        P = self.P
        x_u, x_l = -5.6, -2.9
        y0, paso = 1.0, 0.72
        with self.narrar("b2"):
            # «Comprobémoslo»
            self.en("tabla")
            h1 = Text("Umbral", color=ROC).scale(0.45).move_to([x_u, y0 + 0.05, 0])
            h2 = MathTex(r"\Lambda = e^{2r-2}", color=TXT).scale(0.75).move_to([x_l, y0 + 0.05, 0])
            linea = Line([x_u - 0.9, y0 - 0.33, 0], [x_l + 1.5, y0 - 0.33, 0], color=INK, stroke_width=2)
            self.play(FadeOut(self.tg1), FadeIn(h1), FadeIn(h2), Create(linea), run_time=self.dur(0.5))

            filas, tangentes = [], []
            marcas = [("u15", "l15"), ("u1", None), ("u05", None), ("u0", None)]
            for i, ((u, ut, ex, val), (m_u, m_v)) in enumerate(zip(UMBRALES, marcas)):
                y = y0 - paso * (i + 1)
                self.en(m_u)
                cu = MathTex(ut, color=ROC).scale(0.75).move_to([x_u, y, 0])
                ce = MathTex(ex, color=TXT).scale(0.75).move_to([x_l - 0.55, y, 0])
                cv = MathTex("= " + val, color=TXT).scale(0.75).next_to(ce, RIGHT, buff=0.15)
                tg = P.tangente(u, largo=0.42, color=TXT, ancho=3.5)
                dot = P.punto(*roc9(u), color=TXT, radio=0.07)
                if m_v:
                    self.play(FadeIn(cu), FadeIn(ce), run_time=self.dur(0.4))
                    self.en(m_v)
                    self.play(FadeIn(cv), FadeIn(dot, scale=0.4), Create(tg), run_time=self.dur(0.5))
                else:
                    self.play(FadeIn(cu), FadeIn(ce), FadeIn(cv), run_time=self.dur(0.4))
                    self.play(FadeIn(dot, scale=0.4), Create(tg), run_time=self.dur(0.4))
                filas.append(VGroup(cu, ce, cv))
                tangentes.append((u, tg))

            # «Si mides las pendientes»
            self.en("mides")
            tris = VGroup(*[triangulo9(P, roc9(u), 0.05, lam9(u), ancho=3.5) for u, _ in tangentes])
            self.play(LaggedStart(*[Create(t) for t in tris], lag_ratio=0.25), run_time=self.dur(1.2))

            # «salen esos mismos números»
            self.en("mismos")
            ok = tilde(tam=0.6).next_to(VGroup(*filas), RIGHT, buff=0.3)
            self.sfx("exito")
            self.play(Create(ok), run_time=self.dur(0.4))
