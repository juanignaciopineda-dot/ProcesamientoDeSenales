"""Escena 13 — Medir por el tamaño da la mediana; acertar o fallar da la moda."""
from comun.escena import *


class MedianaYModa(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.B = BarrasLlamadas8(centro=(0, -1.0), ancho=10.0, alto=2.6)
        B = self.B
        self.add(B.base, *B.barras.values(), *B.nums.values(), *[B.pct(v) for v in B.PROBS])
        self.mediana()
        self.moda()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def mediana(self):
        B = self.B
        tam = Text("|Error|", color=ESTIMACION, weight=BOLD).scale(1.0).move_to([-5.9, 3.6, 0])
        cuad = Text("Error²", color=INK, weight=BOLD).scale(1.0).move_to([-3.7, 3.6, 0])
        tach = tachar(cuad, ROJO)
        med = Text("Mediana", color=VERDE, weight=BOLD).scale(1.0).move_to([0.4, 3.6, 0])
        izq = Brace(Line(B.p(-0.4) + UP * 3.2, B.p(0.6) + UP * 3.2), direction=UP, color=INK)
        der = Brace(Line(B.p(1.4) + UP * 3.2, B.p(10.4) + UP * 3.2), direction=UP, color=INK)
        l_izq = Text("0,4", color=TXT, weight=BOLD).scale(0.7).next_to(izq, UP, buff=0.1)
        l_der = Text("0,3", color=TXT, weight=BOLD).scale(0.7).next_to(der, UP, buff=0.1)
        mk_med = B.marcador(1, VERDE)
        et_med = Text("Mediana = 1", color=VERDE, weight=BOLD).scale(0.6).next_to(mk_med, DOWN, buff=0.12)
        mk = B.marcador(1, ESTIMACION)
        e15 = Text("Error medio = 1,5", color=VERDE, weight=BOLD).scale(0.8).move_to([3.2, 1.5, 0])
        e178 = Text("Error medio = 1,78", color=ERROR, weight=BOLD).scale(0.8).move_to([3.2, 0.8, 0])

        with self.narrar("b1"):
            # «se mide por su tamaño»
            self.en("tamano")
            self.pop(tam)

            # «sin cuadrado»
            self.en("sin")
            self.play(FadeIn(cuad), run_time=self.dur(0.3))
            self.play(Create(tach), run_time=self.dur(0.3))

            # «la mejor apuesta es la mediana»
            self.en("mediana")
            self.pop(med)

            # «deja la mitad de la probabilidad a cada lado»
            self.en("mitad")
            self.play(FadeIn(izq), FadeIn(l_izq), FadeIn(der), FadeIn(l_der), run_time=self.dur(0.7))

            # «Aquí es una llamada»
            self.en("llamada")
            self.play(FadeIn(mk_med, shift=UP * 0.3), FadeIn(et_med), run_time=self.dur(0.5))

            # «Apostando uno»
            self.en("apostando1")
            self.play(FadeOut(mk_med), FadeOut(et_med), FadeIn(mk), FadeOut(izq), FadeOut(der), FadeOut(l_izq),
                      FadeOut(l_der), run_time=self.dur(0.4))

            # «uno coma cinco»
            self.en("e15")
            self.play(FadeIn(e15, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «apostando uno coma siete»
            self.en("a17")
            self.play(mk.animate.move_to(B.p(1.7) + DOWN * 0.72), run_time=self.dur(0.5))

            # «uno coma siete ocho»
            self.en("e178")
            self.play(FadeIn(e178, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «el diez raro pesa mucho menos»
            self.en("pesa")
            self.play(B.barras[10].animate.set_opacity(0.25), run_time=self.dur(0.6))
        self.wait(0.3)
        self.mk = mk
        self.limpio = VGroup(tam, cuad, tach, med, e15, e178)

    # ------------------------------------------------------------ b2
    def moda(self):
        B = self.B
        mk = self.mk
        acertar = Text("¿Acierto o fallo?", color=ESTIMACION, weight=BOLD).scale(1.1).move_to([0, 3.4, 0])
        a_corta = Arrow([2.0, 2.7, 0], [3.0, 2.7, 0], buff=0, color=ERROR, stroke_width=5)
        a_larga = Arrow([2.0, 2.15, 0], [5.0, 2.15, 0], buff=0, color=ERROR, stroke_width=5)
        f1 = Text("Fallo", color=ERROR, weight=BOLD).scale(0.6).next_to(a_corta, RIGHT, buff=0.15)
        f2 = Text("Fallo", color=ERROR, weight=BOLD).scale(0.6).next_to(a_larga, RIGHT, buff=0.15)
        ac = Text("Acierta el 40 %", color=VERDE, weight=BOLD).scale(0.8).move_to([3.2, 1.5, 0])
        cero0 = Text("0 %", color=ERROR, weight=BOLD).scale(0.8).move_to([3.2, 0.8, 0])
        cas = [casilla8(-4.6, 0.0, "Cuadrado", "Media", ESTIMACION), casilla8(0.0, 0.0, "Tamaño", "Mediana", VERDE),
               casilla8(4.6, 0.0, "Acierto", "Moda", CIAN)]
        rects = VGroup(*[c.rect for c in cas])

        with self.narrar("b2"):
            # «acertar o fallar»
            self.en("acertar")
            self.play(FadeOut(self.limpio), run_time=0.25)
            self.pop(acertar)

            # «sin importar por cuánto»
            self.en("importar")
            self.play(GrowArrow(a_corta), FadeIn(f1), run_time=self.dur(0.4))
            self.play(GrowArrow(a_larga), FadeIn(f2), run_time=self.dur(0.5))

            # «el valor más probable»
            self.en("probable")
            self.play(FadeOut(a_corta), FadeOut(a_larga), FadeOut(f1), FadeOut(f2), B.barras[10].animate.set_opacity(0.45),
                      run_time=0.3)
            self.resaltar(B.barras[0], color=ESTIMACION, escala=1.1, run_time=0.6)

            # «cero llamadas»
            self.en("cero")
            self.play(mk.animate.move_to(B.p(0) + DOWN * 0.72), run_time=self.dur(0.5))

            # «el cuarenta por ciento de las veces»
            self.en("cuarenta")
            self.play(FadeIn(ac, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Apostar uno coma siete»
            self.en("apostar17")
            self.play(mk.animate.move_to(B.p(1.7) + DOWN * 0.72), run_time=self.dur(0.6))

            # «no acertaría nunca»
            self.en("nunca")
            self.play(FadeIn(cero0, shift=LEFT * 0.2), run_time=self.dur(0.5))

            # «Tres formas de medir el error»
            self.en("tres")
            self.corte()
            self.play(FadeIn(rects, lag_ratio=0.3), run_time=self.dur(0.8))

            # «la media»
            self.en("t_media")
            self.play(FadeIn(cas[0].forma), FadeIn(cas[0].resp), run_time=self.dur(0.4))

            # «la mediana»
            self.en("t_mediana")
            self.play(FadeIn(cas[1].forma), FadeIn(cas[1].resp), run_time=self.dur(0.4))

            # «la moda»
            self.en("t_moda")
            self.play(FadeIn(cas[2].forma), FadeIn(cas[2].resp), run_time=self.dur(0.4))
