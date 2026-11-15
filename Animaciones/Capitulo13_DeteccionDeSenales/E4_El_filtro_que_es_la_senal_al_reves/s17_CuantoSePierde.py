"""Escena 17 — Cuánto se pierde con el promediador y con una sola muestra."""
from comun.escena import *


class CuantoSePierde(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        tit = self.palabra("¿cuánto se pierde?", AMBAR, 0.65).move_to([-2.5, 3.4, 0])
        y_ad, y_pr, y_mu = 2.0, 0.6, -0.8
        ad = Tallos(S13, centro=(-3.0, y_ad), paso=0.6, unidad=0.28, color=ESTIMACION)
        pr = Tallos([1, 1, 1], centro=(-3.0, y_pr), paso=0.6, unidad=0.28, color=ESTIMACION)
        mu = Tallos([2, 0, 0], centro=(-3.0, y_mu), paso=0.6, unidad=0.28, color=ESTIMACION)
        l_ad = etiqueta("adaptado", TXT, 0.45).move_to([-5.7, y_ad, 0])
        l_pr = etiqueta("promediador", TXT, 0.45).move_to([-5.7, y_pr, 0])
        l_mu = etiqueta("una muestra", TXT, 0.45).move_to([-5.7, y_mu, 0])
        c10 = caja("capítulo 10: (½, ½)", INK, ancho=3.2, alto=0.6, scale=0.38).move_to([4.0, 3.3, 0])
        perd = self.palabra("pérdida", ERROR, 0.6).move_to([4.6, 2.2, 0])
        pl = plano_c(centro=(3.6, 0.5), radio=0.9)
        fs = flecha_c(pl.o, 1.4, 0, SENAL, 6)
        fh = flecha_c(pl.o, 1.4, 28, ESTIMACION, 6)
        arco = Arc(radius=0.7, start_angle=0, angle=np.deg2rad(28), color=AMBAR, stroke_width=4).move_arc_center_to(pl.o)
        cos2 = MathTex(r"\cos^2\theta", color=AMBAR).scale(1.0).move_to([6.2, 1.2, 0])
        frac = MathTex(r"\cos^2\theta=\frac{\mathrm{SNR}_{\mathrm{filtro}}}{\mathrm{SNR}_{\mathrm{adaptado}}}",
                       color=TXT).scale(0.7).move_to([3.9, -1.5, 0])
        # segundo bloque (resultados)
        pulso = MathTex(r"s=(2,2,1)", color=SENAL).scale(1.0).move_to([3.4, 2.7, 0])
        fr1 = MathTex(r"\frac{25}{27}", color=TXT).scale(1.0).move_to([0.9, y_pr, 0])
        r1 = MathTex(r"=0{,}926", color=VERDE).scale(1.0).move_to([2.7, y_pr, 0])
        db1 = MathTex(r"-0{,}33\ \mathrm{dB}", color=VERDE).scale(0.85).move_to([5.2, y_pr, 0])
        ok1 = tilde(VERDE, 0.7).move_to([6.7, y_pr, 0])
        fr2 = MathTex(r"\frac{4}{9}", color=TXT).scale(1.0).move_to([0.9, y_mu, 0])
        r2 = MathTex(r"=0{,}444", color=ERROR).scale(1.0).move_to([2.7, y_mu, 0])
        db2 = MathTex(r"-3{,}52\ \mathrm{dB}", color=ERROR).scale(0.85).move_to([5.2, y_mu, 0])
        # tercer bloque (errores)
        e1 = MathTex(r"Q(1{,}5)=0{,}0668", color=VERDE).scale(0.95).move_to([3.0, y_ad, 0])
        e2 = MathTex(r"Q(1{,}44)=0{,}0745", color=VERDE).scale(0.95).move_to([3.0, y_pr, 0])
        e3 = MathTex(r"Q(1)", r"=0{,}159", color=TXT).scale(0.95).move_to([3.0, y_mu, 0])
        e3[1].set_color(ERROR)
        ape = Arrow([6.4, y_ad - 0.2, 0], [6.4, y_pr + 0.2, 0], color=AMBAR, buff=0, stroke_width=3,
                    max_tip_length_to_length_ratio=0.3)
        doble = MathTex(r"\times 2{,}4", color=ERROR).scale(0.95).move_to([6.1, y_mu, 0])
        xs = VGroup(cruz(ROJO, 0.5).move_to([mu.x(1), y_mu + 0.3, 0]), cruz(ROJO, 0.5).move_to([mu.x(2), y_mu + 0.3, 0]))

        with self.narrar("b1"):
            # «¿Cuánto se pierde»
            self.en("cuanto")
            self.pop(tit)

            # «Comparemos tres. El adaptado»
            self.en("tres")
            self.play(FadeIn(ad), FadeIn(l_ad), run_time=self.dur(0.6))

            # «El promediador, uno, uno, uno»
            self.en("prom")
            self.play(FadeIn(pr), FadeIn(l_pr), run_time=self.dur(0.6))

            # «como el promediador del capítulo diez»
            self.en("cap10")
            self.play(FadeIn(c10), run_time=self.dur(0.5))

            # «solo con una muestra»
            self.en("muestra")
            self.play(FadeIn(mu), FadeIn(l_mu), run_time=self.dur(0.6))

            # «La pérdida de un filtro»
            self.en("perdida")
            self.pop(perd)

            # «el coseno al cuadrado del ángulo»
            self.en("coseno")
            self.play(FadeIn(pl), GrowArrow(fs), GrowArrow(fh), Create(arco), run_time=self.dur(0.9))
            self.play(FadeIn(cos2), run_time=0.3)

            # «la fracción de relación señal-ruido que conserva»
            self.en("fraccion")
            self.play(Write(frac), run_time=self.dur(1.6))

        with self.narrar("b2"):
            # «Con el pulso dos, dos, uno»
            self.en("pulso")
            self.play(FadeOut(VGroup(pl, fs, fh, arco, cos2, frac, perd, c10)), FadeIn(pulso), run_time=self.dur(0.5))

            # «El promediador da»
            self.en("da")
            self.resaltar(pr, color=AMBAR, escala=1.1)

            # «veinticinco entre veintisiete»
            self.en("v27")
            self.play(Write(fr1), run_time=self.dur(0.7))

            # «cero coma nueve dos seis»
            self.en("r926")
            self.play(Write(r1), run_time=self.dur(0.8))

            # «menos de medio decibelio»
            self.en("db")
            self.play(FadeIn(db1), run_time=self.dur(0.5))

            # «casi nada»
            self.en("casi")
            self.play(Create(ok1), run_time=self.dur(0.4))

            # «La muestra suelta»
            self.en("suelta")
            self.resaltar(mu, color=AMBAR, escala=1.1)

            # «cuatro entre nueve»
            self.en("c49")
            self.play(Write(fr2), run_time=self.dur(0.6))

            # «cero coma cuatro cuatro cuatro»
            self.en("r444")
            self.play(Write(r2), run_time=self.dur(0.8))

            # «Pierde más de la mitad»
            self.en("mitad")
            self.resaltar(r2, color=ERROR, escala=1.2)

            # «tres coma cinco decibelios»
            self.en("db35")
            self.play(FadeIn(db2), run_time=self.dur(0.5))

        with self.narrar("b3"):
            # «Traducido a errores»
            self.en("trad")
            self.play(FadeOut(VGroup(pulso, fr1, r1, db1, ok1, fr2, r2, db2)), run_time=self.dur(0.4))

            # «cero coma cero seis seis ocho»
            self.en("e0668")
            self.play(Write(e1), run_time=self.dur(1.0))

            # «cero coma cero siete cuatro cinco»
            self.en("e0745")
            self.play(Write(e2), run_time=self.dur(1.0))

            # «apenas más»
            self.en("apenas")
            self.play(Create(ape), run_time=self.dur(0.4))

            # «cu de uno»
            self.en("q1")
            self.play(Write(e3[0]), run_time=self.dur(0.6))

            # «cero coma uno cinco nueve»
            self.en("e159")
            self.play(Write(e3[1]), run_time=self.dur(0.8))

            # «más del doble de errores»
            self.en("doble")
            self.play(FadeIn(doble, scale=1.3), run_time=self.dur(0.5))

            # «Tirar las otras dos muestras»
            self.en("tirar")
            self.play(Create(xs), run_time=self.dur(0.5))

            # «sale caro»
            self.en("caro")
            self.resaltar(e3, color=ERROR, escala=1.15)
            self.sfx("error", gain=-18)
        self.wait(1.0)
        self.limpiar()
