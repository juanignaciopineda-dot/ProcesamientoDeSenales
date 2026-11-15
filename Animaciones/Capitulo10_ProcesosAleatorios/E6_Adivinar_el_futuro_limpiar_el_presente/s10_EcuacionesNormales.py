"""Escena 10 — Las ecuaciones normales: con L muestras, L condiciones de ortogonalidad."""
from comun.escena import *


class EcuacionesNormales(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        filas = VGroup(MathTex(r"e\perp r[n]", color=TXT), MathTex(r"e\perp r[n-1]", color=TXT),
                       MathTex(r"e\perp r[n-2]", color=TXT), MathTex(r"\vdots", color=INK),
                       MathTex(r"e\perp r[n-L+1]", color=TXT)).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        filas.scale(1.25).move_to([-4.3, 0.6, 0])
        llave = Brace(filas, RIGHT, color=AMBAR)
        ele = Text("L condiciones", color=AMBAR, weight=BOLD).scale(0.55).next_to(llave, RIGHT, buff=0.2)

        c0 = MathTex(r"E\big[(s-\hat s)\,r[n-m]\big]", "=", "0", color=TXT).scale(1.3).move_to([0.6, 2.7, 0])
        c1 = MathTex("E[s\\,r[n-m]]", "-", r"\sum_k h[k]\,E[r[n-k]\,r[n-m]]", "=", "0", color=TXT).scale(1.05)
        c1.move_to([0.6, 1.2, 0])
        suma = MathTex(r"\sum_k", "h[k]", color=TXT)
        rrr = MathTex(r"R_{rr}[m-k]", color=MEDIDA)
        igual = MathTex("=", color=AMBAR)
        rsr = MathTex(r"R_{sr}[m]", color=TXT)
        suma[1].set_color(ESTIMACION)
        fin = VGroup(suma, rrr, igual, rsr).arrange(RIGHT, buff=0.22).scale(1.4).move_to([0.6, -0.8, 0])
        self.fin = fin

        with self.narrar("b1"):
            # «perpendicular a cada una de ellas»
            self.en("cada")
            self.play(FadeIn(filas[0]), FadeIn(filas[1]), FadeIn(filas[2]), run_time=self.dur(1.2))
            self.play(FadeIn(filas[3]), FadeIn(filas[4]), run_time=0.5)

            # «ele condiciones»
            self.en("ele")
            self.play(Create(llave), FadeIn(ele), run_time=0.6)

            # «cada condición»
            self.en("condicion")
            self.play(FadeOut(filas), FadeOut(llave), FadeOut(ele), run_time=0.3)
            self.play(FadeIn(c0), run_time=0.6)

            # «aparecen autocorrelaciones»
            self.en("auto")
            self.play(FadeIn(c1), run_time=self.dur(1.0))

            # «La suma de cada coeficiente»
            self.en("suma")
            self.play(FadeIn(suma), run_time=0.5)

            # «la autocorrelación de lo recibido en eme menos ka»
            self.en("rrr")
            self.play(FadeIn(rrr), run_time=0.6)

            # «tiene que ser igual»
            self.en("igual")
            self.play(FadeIn(igual), run_time=0.3)

            # «la correlación cruzada entre la señal y lo recibido»
            self.en("sr")
            self.play(FadeIn(rsr), run_time=0.6)
        self.arriba = VGroup(c0, c1)

    def parte_b2(self):
        fin = self.fin
        norm = caja("ecuaciones normales", AMBAR, alto=0.8, scale=0.6).move_to([0, 3.4, 0])
        sis = MathTex(r"m=0,\dots,L-1", r"\qquad", r"h[0],\dots,h[L-1]", color=TXT).scale(1.1).move_to([0.6, 0.5, 0])
        s = MathTex("s", color=SENAL).scale(1.2)
        perp = MathTex(r"\perp", color=TXT).scale(1.2)
        d = MathTex("d", color=RUIDO).scale(1.2)
        fila_ind = VGroup(s, perp, d).arrange(RIGHT, buff=0.3).move_to([-4.6, -1.3, 0])
        rss = MathTex(r"R_{sr}", "=", r"R_{ss}", color=TXT).scale(1.3).move_to([0.6, -1.3, 0])
        rss[2].set_color(SENAL)
        rrr2 = MathTex(r"R_{rr}", "=", r"R_{ss}", "+", r"R_{dd}", color=TXT).scale(1.3).move_to([0.6, -2.5, 0])
        rrr2[0].set_color(MEDIDA)
        rrr2[2].set_color(SENAL)
        rrr2[4].set_color(RUIDO)
        flecha1 = Arrow([-3.3, -1.3, 0], [-2.0, -1.3, 0], buff=0, color=INK, stroke_width=3)

        with self.narrar("b2"):
            # «ecuaciones normales»
            self.en("normales")
            self.play(FadeOut(self.arriba), fin.animate.move_to([0.6, 1.8, 0]), run_time=0.6)
            self.pop(norm)

            # «ele ecuaciones con ele incógnitas»
            self.en("sistema")
            self.play(FadeIn(sis), run_time=0.7)

            # «Y como la señal y el ruido»
            self.en("ycomo")
            self.play(FadeIn(s), FadeIn(d), run_time=0.5)

            # «no están relacionados»
            self.en("indep")
            self.play(FadeIn(perp), run_time=0.4)

            # «se simplifican»
            self.en("simplifican")
            self.play(Create(flecha1), run_time=0.5)

            # «La correlación cruzada entre la señal y lo recibido»
            self.en("ccruz")
            self.play(FadeIn(rss[0]), run_time=0.4)

            # «es la autocorrelación de la señal»
            self.en("rss")
            self.play(FadeIn(rss[1:]), run_time=0.6)

            # «Y la autocorrelación de lo recibido»
            self.en("rrecib")
            self.play(FadeIn(rrr2[0]), FadeIn(rrr2[1]), run_time=0.5)

            # «es la de la señal más la del ruido»
            self.en("rrr2")
            self.play(FadeIn(rrr2[2:]), run_time=0.7)
