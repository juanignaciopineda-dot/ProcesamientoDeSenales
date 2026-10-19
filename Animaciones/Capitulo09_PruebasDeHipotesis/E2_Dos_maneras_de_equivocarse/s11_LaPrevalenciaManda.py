"""Escena 11 — El mismo test da un valor predictivo del 2 % al 95 % según la prevalencia."""
from comun.escena import *
from comun.figuras_c9e2 import *


class LaPrevalenciaManda(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.uno_de_mil()
        self.la_curva()
        self.montones()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def uno_de_mil(self):
        prev = casilla9("Prevalencia", ESTIMACION, ancho=2.8, alto=0.75, escala=0.48).move_to([-4.7, 3.1, 0])
        aro = Circle(radius=0.35, color=ESTIMACION, stroke_width=4).move_to([-2.65, 3.1, 0])
        aguja = Line(aro.get_center(), aro.get_center() + UP * 0.3, color=ESTIMACION, stroke_width=5)
        sens = casilla9("Sensibilidad 99 %", C1, ancho=2.6, alto=0.7, escala=0.38).move_to([2.3, 3.1, 0])
        fp = casilla9("Falso positivo 5 %", C0, ancho=2.6, alto=0.7, escala=0.38).move_to([5.45, 3.1, 0])
        cand = candado(INK).scale(0.38).move_to([3.88, 3.1, 0])
        mil = Text("1 de cada 1.000", color=ESTIMACION).scale(0.45).move_to([-4.0, 2.25, 0])
        raiz = casilla9("100.000 personas", INK, ancho=3.0, alto=0.7, escala=0.45).move_to([-4.6, 0.3, 0])
        enf = casilla9("100 enfermas", C1, ancho=2.6, alto=0.7, escala=0.45).move_to([-0.4, 1.2, 0])
        san = casilla9("99.900 sanas", C0, ancho=2.6, alto=0.7, escala=0.45).move_to([-0.4, -0.6, 0])
        p99 = Text("→ 99 positivos", color=C1).scale(0.48).move_to([3.4, 1.2, 0])
        p5000 = Text("→ 4.995 positivos", color=ERROR).scale(0.48).move_to([3.5, -0.6, 0])
        l_e = Line(raiz.get_right(), enf.get_left(), color=INK, stroke_width=3)
        l_s = Line(raiz.get_right(), san.get_left(), color=INK, stroke_width=3)
        div = Text("99 / 5.094", color=TXT).scale(0.7).move_to([-0.8, -2.3, 0])
        dos = Text("≈ 2 %", color=ESTIMACION, weight=BOLD).scale(0.9).move_to([1.6, -2.3, 0])

        with self.narrar("b1"):
            # «Cambiemos solo la prevalencia»
            self.en("prev")
            self.play(FadeIn(prev), Create(aro), Create(aguja), run_time=self.dur(0.5))
            self.play(Rotate(aguja, -PI / 2, about_point=aro.get_center()), run_time=self.dur(0.6))

            # «con el mismo test»
            self.en("mismo")
            self.play(FadeIn(sens), FadeIn(fp), FadeIn(cand, scale=0.5), run_time=self.dur(0.5))

            # «una persona de cada mil»
            self.en("mil")
            self.play(Rotate(aguja, PI, about_point=aro.get_center()), FadeIn(mil, shift=DOWN * 0.15),
                      run_time=self.dur(0.6))

            # «de cien mil personas»
            self.en("cienmil")
            self.play(FadeIn(raiz, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «cien están enfermas»
            self.en("enf")
            self.play(Create(l_e), FadeIn(enf, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «noventa y nueve positivos»
            self.en("p99")
            self.play(FadeIn(p99, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «noventa y nueve mil novecientas»
            self.en("sanas")
            self.play(Create(l_s), FadeIn(san, shift=RIGHT * 0.2), run_time=self.dur(0.5))

            # «casi cinco mil positivos»
            self.en("p5000")
            self.play(FadeIn(p5000, shift=RIGHT * 0.2), run_time=self.dur(0.4))

            # «Noventa y nueve de unos cinco mil cien»
            self.en("div")
            self.play(Write(div), run_time=self.dur(0.6))

            # «un dos por ciento»
            self.en("dos")
            self.pop(dos)

    # ------------------------------------------------------------ b2
    def la_curva(self):
        V = CurvaVPP9()
        p0 = V.punto(0.001)
        e0 = Text("0,1 % → 2 %", color=TXT).scale(0.42).next_to(V.pt(0.001), UP, buff=0.25)
        datos = [(0.01, "1 % → 17 %"), (0.1, "10 % → 69 %"), (0.5, "50 %")]
        puntos = [V.punto(p) for p, _ in datos]
        etiq = [Text(t, color=TXT).scale(0.42) for _, t in datos]
        etiq[0].next_to(V.pt(0.01), RIGHT, buff=0.2).shift(DOWN * 0.2)
        etiq[1].next_to(V.pt(0.1), RIGHT, buff=0.2).shift(DOWN * 0.25)
        v95 = Text("→ 95 %", color=VERDE, weight=BOLD).scale(0.42)
        par = VGroup(etiq[2], v95).arrange(RIGHT, buff=0.12)
        par.move_to([4.3 - par.width / 2, -0.3, 0])
        curva = V.curva()
        cand = VGroup(candado(INK).scale(0.35), Text("99 % · 5 %", color=INK).scale(0.4)).arrange(RIGHT, buff=0.15)
        cand.move_to([5.9, -1.9, 0])
        rango_f = DoubleArrow([4.95, V.y(0.02), 0], [4.95, V.y(0.95), 0], buff=0, color=ESTIMACION, stroke_width=3,
                              tip_length=0.18, max_tip_length_to_length_ratio=0.2)
        rango_t = Text("Del 2 % al 95 %", color=ESTIMACION, weight=BOLD).scale(0.48).move_to([5.4, 3.0, 0])

        with self.narrar("b2"):
            # «Con una de cada cien»
            self.en("cien")
            self.corte()
            self.play(Create(V.ejes), FadeIn(V.etq), FadeIn(p0), FadeIn(e0), run_time=self.dur(0.6))
            self.play(FadeIn(puntos[0], scale=0.4), FadeIn(etiq[0]), run_time=self.dur(0.4))

            # «Con una de cada diez»
            self.en("p10")
            self.play(FadeIn(puntos[1], scale=0.4), FadeIn(etiq[1]), run_time=self.dur(0.5))

            # «Con la mitad»
            self.en("p50")
            self.play(FadeIn(puntos[2], scale=0.4), FadeIn(etiq[2]), run_time=self.dur(0.5))

            # «un noventa y cinco»
            self.en("v95")
            self.play(puntos[2].animate.set_color(VERDE).scale(1.4), FadeIn(v95, shift=RIGHT * 0.15),
                      run_time=self.dur(0.5))

            # «mismo test, con la misma sensibilidad»
            self.en("curva")
            self.play(Create(curva), run_time=self.dur(1.2))

            # «la misma especificidad»
            self.en("candado")
            self.play(FadeIn(cand, shift=UP * 0.2), run_time=self.dur(0.5))

            # «del dos al noventa y cinco por ciento»
            self.en("rango")
            self.play(GrowFromCenter(rango_f), FadeIn(rango_t), run_time=self.dur(0.7))

    # ------------------------------------------------------------ b3
    def montones(self):
        mas = VGroup(MathTex("+", color=ESTIMACION).scale(1.3), Text("?", color=ESTIMACION, weight=BOLD).scale(0.9))
        mas.arrange(RIGHT, buff=0.15).move_to([0, 3.2, 0])
        grande = monton9(260, centro=(-3.6, -2.6), radio=2.1, color=C0, semilla=4)
        chico = monton9(6, centro=(3.6, -2.6), radio=0.3, color=C1, r_punto=0.06, semilla=2)
        tira_f = Rectangle(width=0.22, height=3.0, color=ERROR, stroke_width=2).set_fill(ERROR, 0.8)
        tira_f.move_to([-3.6, -0.95 + 1.5, 0])
        tira_v = Rectangle(width=0.22, height=0.06, color=C1, stroke_width=2).set_fill(C1, 0.9)
        tira_v.move_to([3.6, -2.0 + 0.03, 0])
        peq = Text("5 % de 99.900 = 4.995", color=ERROR).scale(0.45).move_to([-3.6, -3.25, 0])
        gr = Text("99 % de 100 = 99", color=C1).scale(0.45).move_to([3.6, -3.25, 0])

        with self.narrar("b3"):
            # «de dónde sale cada positivo»
            self.en("donde")
            self.corte()
            self.pop(mas)

            # «un montón enorme de sanos»
            self.en("sanos")
            self.play(LaggedStart(*[FadeIn(p) for p in grande], lag_ratio=0.004), run_time=self.dur(0.9))
            self.play(GrowFromEdge(tira_f, DOWN), run_time=self.dur(0.6))

            # «un montón minúsculo de enfermos»
            self.en("enfermos")
            self.play(FadeIn(chico), run_time=self.dur(0.4))
            self.play(*[p.animate.set_color(ESTIMACION) for p in chico], GrowFromEdge(tira_v, DOWN),
                      run_time=self.dur(0.5))

            # «Un porcentaje pequeño de muchísimos»
            self.en("pequeno")
            self.play(FadeIn(peq, shift=UP * 0.15), run_time=self.dur(0.5))

            # «un porcentaje grande de muy pocos»
            self.en("grande")
            self.play(FadeIn(gr, shift=UP * 0.15), run_time=self.dur(0.5))
            self.play(tira_f.animate.move_to([-0.35, -2.6 + 1.5, 0]), tira_v.animate.move_to([0.35, -2.6 + 0.03, 0]),
                      run_time=self.dur(0.8))
