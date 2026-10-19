"""Escena 09 — El test médico como problema de hipótesis: el diccionario médico y el valor predictivo."""
from comun.escena import *
from comun.figuras_c9e2 import *


class ElTestMedicoVuelve(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.hipotesis()
        self.diccionario()
        self.valor_predictivo()
        self.trampa()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def hipotesis(self):
        tira = tira_test07(0.85).move_to([0, 1.0, 0])
        cap = Text("Capítulo 7", color=INK).scale(0.4).move_to([0, 2.55, 0])
        hosp = cruz_hospital().scale(0.5).move_to([1.25, 1.7, 0])
        card1 = casilla9("1 de cada 100", INK, ancho=3.6, alto=0.75, escala=0.42).move_to([-4.6, -2.3, 0])
        card2 = casilla9("Enfermo → Positivo 99 %", C1, ancho=4.2, alto=0.75, escala=0.4).move_to([0, -2.3, 0])
        card3 = casilla9("Sano → Positivo 5 %", C0, ancho=4.0, alto=0.75, escala=0.4).move_to([4.6, -2.3, 0])
        enf = persona(C1).scale(1.1).move_to([0, -1.1, 0])
        sano = persona(C0).scale(1.1).move_to([4.6, -1.1, 0])
        h0 = casilla_h3(0, "Sano", centro=(-4.4, 3.2), ancho=2.8)
        h1 = casilla_h3(1, "Enfermo", centro=(4.4, 3.2), ancho=2.8)
        dec = Text("Decisión: + / −", color=ESTIMACION, weight=BOLD).scale(0.5).move_to([3.7, 1.0, 0])
        fl = Arrow([0.65, 1.0, 0], dec.get_left(), buff=0.12, color=ESTIMACION, stroke_width=3)

        with self.narrar("b1"):
            # «Vuelve el test médico»
            self.en("test")
            self.play(FadeIn(tira, shift=UP * 0.3), FadeIn(cap), run_time=self.dur(0.6))

            # «Una enfermedad»
            self.en("enfermedad")
            self.play(FadeIn(hosp, scale=0.5), run_time=self.dur(0.4))

            # «una persona de cada cien»
            self.en("cien")
            self.play(FadeIn(card1, shift=UP * 0.2), run_time=self.dur(0.5))

            # «Si estás enfermo»
            self.en("enfermo")
            self.play(FadeIn(enf, shift=UP * 0.2), run_time=self.dur(0.4))

            # «noventa y nueve por ciento»
            self.en("p99")
            self.play(FadeIn(card2, shift=UP * 0.2), run_time=self.dur(0.5))

            # «Si estás sano»
            self.en("sano")
            self.play(FadeIn(sano, shift=UP * 0.2), run_time=self.dur(0.4))

            # «un cinco por ciento»
            self.en("p5")
            self.play(FadeIn(card3, shift=UP * 0.2), run_time=self.dur(0.5))

            # «hache cero, sano»
            self.en("h0")
            self.play(FadeIn(h0, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «hache uno, enfermo»
            self.en("h1")
            self.play(FadeIn(h1, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «la decisión es lo que dice el test»
            self.en("decision")
            self.play(GrowArrow(fl), FadeIn(dec, shift=RIGHT * 0.2), run_time=self.dur(0.6))

    # ------------------------------------------------------------ b2
    def diccionario(self):
        ys = [2.1, 1.1, 0.1, -0.9, -1.9]
        izq_txt = ["Detección", "Falsa alarma", "1 − Falsa alarma", "Fallo", None]
        der_txt = ["Sensibilidad · 99 %", "Falso positivo · 5 %", "Especificidad · 95 %", "Falso negativo · 1 %",
                   "Prevalencia · 1 %"]
        izq = []
        for t, y in zip(izq_txt, ys):
            m = Text(t, color=TXT).scale(0.5) if t else MathTex("p_1", color=C1).scale(0.9)
            izq.append(m.move_to([-3.2, y, 0]))
        der = [Text(t, color=ESTIMACION).scale(0.5).move_to([2.8, y, 0]) for t, y in zip(der_txt, ys)]
        flechas = [Arrow([-1.2, y, 0], [0.4, y, 0], buff=0, color=INK, stroke_width=2.5) for y in ys]
        enc = VGroup(Text("Nosotros", color=INK, weight=BOLD).scale(0.5).move_to([-3.2, 3.2, 0]),
                     Text("Médicos", color=INK, weight=BOLD).scale(0.5).move_to([2.8, 3.2, 0]))
        self.izq, self.der, self.flechas, self.enc = izq, der, flechas, enc

        with self.narrar("b2"):
            # «otros nombres»
            self.en("dicc")
            self.corte()
            self.play(FadeIn(enc, shift=DOWN * 0.2), run_time=self.dur(0.5))

            # «La probabilidad de detección»
            self.en("det")
            self.play(FadeIn(izq[0], shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «es la sensibilidad»
            self.en("sens")
            self.play(GrowArrow(flechas[0]), FadeIn(der[0], shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «La de falsa alarma»
            self.en("fa")
            self.play(FadeIn(izq[1], shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «falso positivo»
            self.en("fp")
            self.play(GrowArrow(flechas[1]), FadeIn(der[1], shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «es la especificidad»
            self.en("esp")
            self.play(FadeIn(izq[2]), GrowArrow(flechas[2]), FadeIn(der[2], shift=RIGHT * 0.2), run_time=self.dur(0.6))

            # «el falso negativo»
            self.en("fn")
            self.play(FadeIn(izq[3]), GrowArrow(flechas[3]), FadeIn(der[3], shift=RIGHT * 0.2), run_time=self.dur(0.6))

            # «la probabilidad a priori de estar enfermo»
            self.en("apriori")
            self.play(FadeIn(izq[4], shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «es la prevalencia»
            self.en("prev")
            self.play(GrowArrow(flechas[4]), FadeIn(der[4], shift=RIGHT * 0.2), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b3
    def valor_predictivo(self):
        dicc = VGroup(*self.izq, *self.der, *self.flechas, self.enc)
        pac = persona(TXT).scale(1.6).move_to([-4.6, -1.4, 0])
        contenido = VGroup(MathTex("+", color=ERROR).scale(0.9), Text("→ ¿Enfermo?", color=TXT).scale(0.42))
        contenido.arrange(RIGHT, buff=0.15)
        burbuja = burbuja_pensamiento(None).scale(2.4).move_to([-1.6, 0.9, 0])
        contenido.move_to(burbuja.globo)
        vpp = Text("Valor predictivo positivo", color=ESTIMACION, weight=BOLD).scale(0.55).move_to([3.4, 0.9, 0])
        G = GrillaMil07(centro=(0, 0.3), color=C0)
        et10 = Text("10 enfermos +", color=C1).scale(0.45).move_to([-2.4, 2.0, 0])
        et50 = Text("≈ 50 sanos +", color=ERROR).scale(0.45).move_to([1.8, 2.0, 0])
        caja = G.recuadro(0, 60)
        div = Text("10 / 60", color=TXT).scale(0.7).move_to([-0.8, -1.5, 0])
        res = Text("≈ 17 %", color=ESTIMACION, weight=BOLD).scale(0.9).move_to([1.4, -1.5, 0])

        with self.narrar("b3"):
            # «al paciente»
            self.en("paciente")
            mini = VGroup(*[t.copy().scale(0.6) for t in self.der]).arrange(DOWN, buff=0.15).move_to([3.6, -1.2, 0])
            self.play(FadeOut(dicc), FadeIn(pac, shift=RIGHT * 0.3), FadeIn(mini), run_time=self.dur(0.5))

            # «no le interesa ninguna de esas»
            self.en("ninguna")
            tachas = VGroup(*[tachar(m) for m in mini])
            self.play(LaggedStart(*[Create(t) for t in tachas], lag_ratio=0.2), run_time=self.dur(0.8))

            # «Le interesa esto»
            self.en("esto")
            self.play(FadeOut(mini), FadeOut(tachas), run_time=0.25)
            self.play(pac.animate(rate_func=there_and_back).scale(1.15).shift(RIGHT * 0.3), run_time=self.dur(0.6))

            # «he dado positivo, ¿estoy enfermo?»
            self.en("pregunta")
            self.play(FadeIn(burbuja, scale=0.6), run_time=self.dur(0.4))
            self.play(FadeIn(contenido), run_time=self.dur(0.3))

            # «el valor predictivo positivo»
            self.en("vpp")
            self.pop(vpp)

            # «Ya hicimos la cuenta»
            self.en("cuenta")
            self.corte()
            self.play(FadeIn(G), run_time=self.dur(0.6))

            # «diez enfermas dan positivo»
            self.en("diez")
            self.play(*[p.animate.set_fill(C1, 1) for p in G.pts[:10]], FadeIn(et10), run_time=self.dur(0.5))

            # «unas cincuenta también»
            self.en("cincuenta")
            self.play(LaggedStart(*[p.animate.set_fill(ERROR, 1) for p in G.pts[10:60]], lag_ratio=0.03),
                      FadeIn(et50), run_time=self.dur(0.9))

            # «Diez de sesenta»
            self.en("sesenta")
            self.play(Create(caja), Write(div), run_time=self.dur(0.6))

            # «un diecisiete por ciento»
            self.en("diecisiete")
            self.pop(res)

    # ------------------------------------------------------------ b4
    def trampa(self):
        T = Tabla22_9(("Sano", "Enfermo"), ("−", "+"), centro=(-1.6, 0.3), ancho=1.9, alto=1.2,
                      titulo_f="Realidad", titulo_c="Test", escala=0.5)
        valores = [T.texto(0, 0, "940", TXT, dy=0, escala=0.55), T.texto(0, 1, "50", ERROR, dy=0, escala=0.55),
                   T.texto(1, 0, "0", TXT, dy=0, escala=0.55), T.texto(1, 1, "10", C1, dy=0, escala=0.55)]
        y1 = T.c(1, 0)[1]
        x1 = T.c(0, 1)[0]
        f_fila = Arrow([T.cx - T.w - 0.05, y1 - 0.4, 0], [T.cx + T.w + 0.3, y1 - 0.4, 0], buff=0,
                       color=ESTIMACION, stroke_width=4)
        f_col = Arrow([x1 + 0.55, T.cy + T.h + 0.05, 0], [x1 + 0.55, T.cy - T.h - 0.3, 0], buff=0,
                      color=VERDE, stroke_width=4)
        senst = Text("Sensibilidad", color=ESTIMACION, weight=BOLD).scale(0.48).move_to([2.4, y1, 0])
        filacuenta = Text("10 de 10 ≈ 99 %", color=ESTIMACION).scale(0.48).move_to([4.2, -1.6, 0])
        vp = Text("Valor predictivo", color=VERDE, weight=BOLD).scale(0.48).move_to([x1 + 0.3, 2.95, 0])
        colcuenta = Text("10 de 60 ≈ 17 %", color=VERDE).scale(0.48).move_to([-0.6, -1.6, 0])
        neq = MathTex(r"\neq", color=TXT).scale(1.3).move_to([1.8, -1.6, 0])
        prev = casilla9("Prevalencia · 1 %", ESTIMACION, ancho=3.6, alto=0.7, escala=0.45).move_to([1.8, -2.9, 0])

        with self.narrar("b4"):
            # «Aquí está la trampa»
            self.en("trampa")
            self.corte()
            self.play(FadeIn(T), LaggedStart(*[FadeIn(v) for v in valores], lag_ratio=0.2), run_time=self.dur(0.8))

            # «La sensibilidad recorre la tabla»
            self.en("senst")
            self.play(FadeIn(senst, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «por filas»
            self.en("filas")
            self.play(GrowArrow(f_fila), run_time=self.dur(0.5))

            # «de los enfermos, cuántos dan positivo»
            self.en("filacuenta")
            self.play(FadeIn(filacuenta, shift=UP * 0.15), run_time=self.dur(0.5))

            # «El valor predictivo»
            self.en("vp")
            self.play(FadeIn(vp, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «por columnas»
            self.en("columnas")
            self.play(GrowArrow(f_col), run_time=self.dur(0.5))

            # «cuántos están enfermos»
            self.en("colcuenta")
            self.play(FadeIn(colcuenta, shift=UP * 0.15), run_time=self.dur(0.5))

            # «Son preguntas distintas»
            self.en("distintas")
            self.pop(neq)

            # «hace falta la prevalencia»
            self.en("prev")
            self.play(FadeIn(prev, shift=UP * 0.2), run_time=self.dur(0.5))
