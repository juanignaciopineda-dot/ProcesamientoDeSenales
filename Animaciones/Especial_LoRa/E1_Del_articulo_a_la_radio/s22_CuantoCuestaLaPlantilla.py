"""Escena 22 — Cuánto cuesta (tiempo y memoria) alargar la plantilla del detector y qué se gana."""
from comun.escena import *
from comun.figuras_lora import *


def _plantilla(n_sube, con_bajada, x_izq, y, u=0.5, alto=0.6):
    """Tira de una plantilla: `n_sube` chirps (y los 2,25 que bajan), alineada a la izquierda en x_izq."""
    n = n_sube + (2.25 if con_bajada else 0)
    P = PlanoTF(centro=(x_izq + n * u / 2, y), ancho=n * u, alto=alto, n=n, rotulos=False)
    g = VGroup(P, *[P.rampa(0, i, grosor=3) for i in range(n_sube)])
    if con_bajada:
        g.add(P.bajada(n_sube, 1, CIAN, 3), P.bajada(n_sube + 1, 1, CIAN, 3), P.bajada(n_sube + 2, 0.25, CIAN, 3))
    g.marco = P.marco
    return g


class CuantoCuestaLaPlantilla(EscenaCurso):
    ESCENA = "22"

    def construct(self):
        self.coste()
        self.memoria()
        self.ganancia()
        self.curvas()
        self.sorpresa()
        self.atajos()
        self.wait(1.0)
        self.limpiar()

    def coste(self):
        pl = [_plantilla(1, False, -6.5, 3.2), _plantilla(8, False, -6.5, 2.35), _plantilla(8, True, -6.5, 1.5)]
        rots = [Text(t, color=INK, weight=BOLD).scale(0.45).next_to(p, RIGHT, buff=0.25) for t, p in
                zip(("1 chirp", "8 chirps", "10,25 chirps"), pl)]
        coste = Text("Coste", color=AMBAR, weight=BOLD).scale(1.1).move_to([4.6, 3.1, 0])
        xs = [-6.2 + 0.52 * i for i in range(10)]
        f1 = VGroup(*[Dot([x, 0.1, 0], radius=0.09, color=AMBAR) for x in xs])
        f2 = VGroup(*[Dot([x, -0.9, 0], radius=0.09, color=MEDIDA) for x in xs])
        un = VGroup(*[Line([x, 0.0, 0], [x, -0.8, 0], color=INK, stroke_width=2) for x in xs])
        por = MathTex(r"\times", color=TXT).scale(1.1).move_to([-6.75, -0.4, 0])
        sig = MathTex(r"\Sigma", color=TXT).scale(1.8).move_to([-0.7, -0.4, 0])
        u = 5.6 / 2624
        datos = (("1 chirp: 256", 256, 0.35), ("8 chirps: 2.048", 2048, -0.5), ("10,25 chirps: 2.624", 2624, -1.35))
        barras, textos = [], []
        for txt, n, y in datos:
            b = Rectangle(width=n * u, height=0.6, color=AMBAR, stroke_width=2.5).set_fill(AMBAR, 0.35)
            b.move_to([0.6 + n * u / 2, y, 0])
            t = Text(txt, color=TXT, weight=BOLD).scale(0.45)
            t.move_to(b) if n > 1000 else t.next_to(b, RIGHT, buff=0.2)
            barras.append(b)
            textos.append(t)
        cada = Text("× cada muestra", color=TXT, weight=BOLD).scale(0.7).move_to([-3.9, -2.2, 0])
        seg = Text("× 125.000 por segundo", color=TXT, weight=BOLD).scale(0.6).move_to([-3.9, -3.0, 0])
        mill = Text("256.000.000 por segundo", color=ERROR, weight=BOLD).scale(0.75).move_to([3.4, -2.7, 0])
        with self.narrar("b1"):
            # «ocho chirps y no uno»
            self.en("pregunta")
            self.play(LaggedStart(*[FadeIn(VGroup(p, r), shift=RIGHT * 0.2) for p, r in zip(pl, rots)], lag_ratio=0.2),
                      run_time=self.dur(1.0))
            # «los diez y cuarto del preámbulo entero»
            self.en("entero")
            self.play(pl[2].marco.animate(rate_func=there_and_back).set_stroke(AMBAR, 6), run_time=self.dur(0.9))
            # «el coste»
            self.en("coste")
            self.pop(coste)
            # «multiplicar cada muestra de la plantilla»
            self.en("mult")
            self.play(FadeIn(f1), FadeIn(f2), FadeIn(por), run_time=0.5)
            self.play(LaggedStart(*[Create(l) for l in un], lag_ratio=0.1), run_time=self.dur(1.2))
            # «sumar»
            self.en("suma")
            self.pop(sig)
            # las tres barras
            for marca, b, t in zip(("n256", "n2048", "n2624"), barras, textos):
                self.en(marca)
                self.play(GrowFromEdge(b, LEFT), run_time=self.dur(0.6))
                self.play(FadeIn(t), run_time=self.dur(0.3))
            # «por cada muestra que llega»
            self.en("cada")
            self.pop(cada)
            # «ciento veinticinco mil por segundo»
            self.en("seg")
            self.play(FadeIn(seg, shift=UP * 0.15), run_time=self.dur(0.5))
            # «doscientos cincuenta y seis millones»
            self.en("millones")
            self.pop(mill, sonido="impacto")
            # «cada segundo»
            self.en("cadaseg")
            self.resaltar(mill, color=ERROR, escala=1.1, run_time=self.dur(0.6))

    def memoria(self):
        t1 = MathTex(r"\text{Tiempo}", r"\propto", r"\text{Largo}", color=TXT).scale(1.4).move_to([-3.5, 2.7, 0])
        d1 = MathTex(r"\times 2", r"\ \to\ ", r"\times 2", color=AMBAR).scale(1.4).move_to([-3.5, 1.6, 0])
        t2 = MathTex(r"\text{Memoria}", r"\propto", r"\text{Largo}", color=TXT).scale(1.4).move_to([3.5, 2.7, 0])
        cas = VGroup(*[Square(side_length=0.5, color=MEDIDA, stroke_width=2.5).set_fill(MEDIDA, 0.2) for _ in range(16)])
        cas.arrange(RIGHT, buff=0.08).move_to([0, -0.2, 0])
        pla = Rectangle(width=cas.width, height=0.6, color=AMBAR, stroke_width=3).set_fill(AMBAR, 0.25).move_to([0, -1.1, 0])
        rp = Text("Plantilla", color=TXT, weight=BOLD).scale(0.45).move_to(pla)
        ru = Text("Últimas muestras recibidas", color=MEDIDA, weight=BOLD).scale(0.45).move_to([0, 0.5, 0])
        m8 = Text("SF 8: 2.048 muestras", color=TXT, weight=BOLD).scale(0.7).move_to([-3.4, -2.7, 0])
        m12 = Text("SF 12: 32.768 muestras", color=ERROR, weight=BOLD).scale(0.7).move_to([3.4, -2.7, 0])
        with self.narrar("b2"):
            # «en proporción al largo»
            self.en("prop")
            self.corte()
            self.play(Write(t1), run_time=self.dur(0.9))
            # «el doble de chirps, el doble de cuentas»
            self.en("doble")
            self.pop(d1)
            # «la memoria también»
            self.en("mem")
            self.play(Write(t2), run_time=self.dur(0.9))
            # «las últimas muestras recibidas»
            self.en("ultimas")
            self.play(FadeIn(cas), FadeIn(ru), run_time=0.4)
            self.play(cas.animate(rate_func=there_and_back).shift(LEFT * 0.58), run_time=self.dur(1.2))
            # «tantas como mide»
            self.en("tantas")
            self.play(FadeIn(pla, shift=UP * 0.2), FadeIn(rp), run_time=self.dur(0.6))
            # «dos mil muestras»
            self.en("dosmil")
            self.pop(m8)
            # «treinta y dos mil»
            self.en("tmil")
            self.pop(m12)

    def ganancia(self):
        sens = Text("Sensibilidad", color=VERDE, weight=BOLD).scale(1.0).move_to([0, 3.3, 0])
        x0, paso = -6.4, 0.95
        fl = [flecha_v([x0 + paso * i, 2.0, 0], [x0 + paso * (i + 1), 2.0, 0]) for i in range(8)]
        c8 = cota([x0, 1.55, 0], [x0 + 8 * paso, 1.55, 0], "8", SENAL, DOWN, 0.6)
        e64 = MathTex(r"\text{Señal: }", "8^{2} = 64", color=SENAL).scale(1.2).move_to([-3.6, 0.0, 0])
        r8 = MathTex(r"\text{Ruido: }", "8", color=RUIDO).scale(1.2).move_to([-3.6, -0.9, 0])
        db9 = MathTex(r"64 / 8 = 8", r"\ \to\ ", r"9\ \mathrm{dB}", color=VERDE).scale(1.3).move_to([-3.6, -2.2, 0])
        cab = Text("Chirps → Ganancia", color=INK, weight=BOLD).scale(0.5).move_to([4.5, 1.2, 0])
        filas = [MathTex(a, r"\ \to\ ", b, color=TXT).scale(1.1).move_to([4.5, 0.5 - 0.7 * i, 0]) for i, (a, b) in
                 enumerate((("1", r"0\ \mathrm{dB}"), ("2", r"3\ \mathrm{dB}"), ("4", r"6\ \mathrm{dB}"), ("8", r"9\ \mathrm{dB}"),
                            ("10{,}25", r"10{,}1\ \mathrm{dB}")))]
        filas[3].set_color(AMBAR)
        filas[4].set_color(CIAN)
        doble = Text("Coste × 2 en cada paso", color=ERROR, weight=BOLD).scale(0.5).move_to([4.5, -3.2, 0])
        with self.narrar("b3"):
            # «Sensibilidad»
            self.en("sens")
            self.corte()
            self.pop(sens)
            # «se suman en fase»
            self.en("fase")
            self.play(LaggedStart(*[GrowArrow(f) for f in fl], lag_ratio=0.12), run_time=self.dur(1.3))
            # «ocho veces en amplitud»
            self.en("amp8")
            self.play(FadeIn(c8), run_time=self.dur(0.5))
            # «sesenta y cuatro en energía»
            self.en("e64")
            self.play(Write(e64), run_time=self.dur(0.9))
            # «el ruido solo crece ocho»
            self.en("r8")
            self.play(Write(r8), run_time=self.dur(0.8))
            # «nueve decibelios»
            self.en("db9")
            self.play(Write(db9[:2]), run_time=0.6)
            self.pop(db9[2])
            # «tres decibelios»
            self.en("tres")
            self.play(FadeIn(cab), LaggedStart(*[FadeIn(f, shift=UP * 0.1) for f in filas[:4]], lag_ratio=0.2),
                      run_time=self.dur(1.0))
            # «se paga el doble»
            self.en("doble")
            self.pop(doble)
            # «un decibelio más»
            self.en("uno")
            self.pop(filas[4])

    def curvas(self):
        E = EjesXY(centro=(-1.7, -0.5), ancho=8.2, alto=4.8, x=(-26, -8), y=(0, 1), x_marcas=(-26, -22, -18, -14, -10),
                   y_marcas=(0, 0.5, 1), rot_x="SNR (dB)", rot_y="Probabilidad de detectar", escala=0.45)
        E.rots[1].shift(RIGHT * 1.6)
        col = {"1": INK, "2": CIAN, "4": MAGENTA, "8": AMBAR, "10,25": VERDE}
        cs = {k: E.curva(PDET_SNR, PDET[k], c, 4.5) for k, c in col.items()}
        for c in cs.values():
            c.permitir_encima = True
        ley = {k: Text(f"{k} chirps" if k != "1" else "1 chirp", color=c, weight=BOLD).scale(0.55).move_to([5.1, 1.6 - 0.75 * i, 0])
               for i, (k, c) in enumerate(col.items())}
        fl = Arrow([1.0, 2.75, 0], [-2.6, 2.75, 0], color=TXT, stroke_width=5, buff=0)
        menos = Text("Menos señal", color=TXT, weight=BOLD).scale(0.6).move_to([-0.8, 3.3, 0])
        with self.narrar("b4"):
            # «La simulación lo muestra»
            self.en("sim")
            self.corte()
            self.play(FadeIn(E.todo), run_time=self.dur(0.7))
            # «la probabilidad de detectar la trama»
            self.en("prob")
            self.resaltar(E.rots[1], color=AMBAR, escala=1.2, run_time=self.dur(0.7))
            # «según el nivel de señal»
            self.en("nivel")
            self.resaltar(E.rots[0], color=AMBAR, escala=1.2, run_time=self.dur(0.7))
            for marca, k in zip(("c1", "c2", "c4", "c8", "c10"), col):
                self.en(marca)
                self.play(Create(cs[k], rate_func=linear), FadeIn(ley[k]), run_time=self.dur(0.4))
            # «a la izquierda de la anterior»
            self.en("izq")
            self.play(GrowArrow(fl), run_time=self.dur(0.8))
            # «con menos señal»
            self.en("menos")
            self.pop(menos)

    def sorpresa(self):
        ex = Text("!", color=AMBAR, weight=BOLD).scale(2.0).move_to([-6.4, 3.0, 0])
        sabe = Text("¿Hay trama?", color=TXT, weight=BOLD).scale(0.8).move_to([-3.6, 3.0, 0])
        ok = tilde(VERDE, 0.7).move_to([-1.6, 3.0, 0])
        nos = Text("¿Dónde empieza?", color=TXT, weight=BOLD).scale(0.8).move_to([2.6, 3.0, 0])
        q = Text("?", color=ERROR, weight=BOLD).scale(1.3).move_to([5.3, 3.0, 0])
        P = PlanoTF(centro=(0, 0.9), ancho=10.4, alto=1.5, n=13, rotulos=False)
        ram = VGroup(*[P.rampa(0, 2 + i, grosor=4) for i in range(8)])
        baj = VGroup(P.bajada(10, 1, CIAN, 4), P.bajada(11, 1, CIAN, 4), P.bajada(12, 0.25, CIAN, 4))
        u = P.ancho / P.n
        chico = Rectangle(width=u, height=1.8, color=ERROR, stroke_width=5).move_to(P.p(2.5, 0.5))
        chico.permitir_encima = True
        grande = Rectangle(width=8 * u, height=1.8, color=VERDE, stroke_width=5).move_to(P.p(6, 0.5))
        grande.permitir_encima = True
        sob = MathTex(r"\mathrm{SNR} = -8\ \mathrm{dB}", color=INK).scale(0.9).move_to([-4.6, -0.9, 0])
        mit = Text("1 chirp: acierta el 54 %", color=ERROR, weight=BOLD).scale(0.75).move_to([0, -1.9, 0])
        uni = Text("8 chirps: acierta el 100 %", color=VERDE, weight=BOLD).scale(0.75).move_to([0, -2.9, 0])
        with self.narrar("b5"):
            # «una sorpresa»
            self.en("sorpresa")
            self.corte()
            self.pop(ex)
            # «sabe que hay trama»
            self.en("sabe")
            self.play(FadeIn(sabe), Create(ok), run_time=self.dur(0.6))
            # «no sabe dónde empieza»
            self.en("nosabe")
            self.play(FadeIn(nos), run_time=0.3)
            self.pop(q)
            # «ocho chirps iguales»
            self.en("iguales")
            self.play(FadeIn(P), LaggedStart(*[Create(r) for r in ram], lag_ratio=0.1), FadeIn(baj), run_time=self.dur(1.2))
            # «encaja igual de bien en cualquiera»
            self.en("cualquiera")
            self.play(FadeIn(chico), run_time=0.3)
            for i in (5.5, 3.5, 8.5, 6.5):
                self.play(chico.animate.move_to(P.p(i, 0.5)), run_time=0.45)
                self.wait(0.25)
            # «con señal de sobra»
            self.en("sobra")
            self.play(Write(sob), run_time=self.dur(0.7))
            # «la plantilla de un chirp»
            self.en("unchirp")
            self.play(chico.animate(rate_func=there_and_back).set_stroke(width=10), run_time=self.dur(0.8))
            # «solo la mitad de las veces»
            self.en("mitad")
            self.pop(mit)
            # «la plantilla de ocho»
            self.en("ocho")
            self.play(FadeOut(chico), Create(grande), run_time=self.dur(0.8))
            # «un único punto»
            self.en("unico")
            self.pop(uni, sonido="exito")

    def atajos(self):
        i1 = insignia(1, AMBAR).move_to([-6.4, 2.9, 0])
        i2 = insignia(2, AMBAR).move_to([-6.4, -1.6, 0])
        toda = Rectangle(width=6.4, height=0.55, color=MEDIDA, stroke_width=2.5).set_fill(MEDIDA, 0.2).move_to([-2.5, 1.9, 0])
        rtoda = Text("Toda la grabación", color=TXT, weight=BOLD).scale(0.42).move_to(toda)
        fft = Text("Correlación por FFT", color=TXT, weight=BOLD).scale(0.7).move_to([-3.4, 2.9, 0])
        # barras de tiempo medido
        xb, yb, u = 2.4, 0.3, 0.24
        bd = VGroup(*[Rectangle(width=0.3, height=t * u, stroke_width=0).set_fill(AMBAR, 0.9).move_to([xb + 0.95 * i, yb + t * u / 2, 0])
                      for i, t in enumerate(TIEMPO_DIRECTA_MS)])
        bf = VGroup(*[Rectangle(width=0.3, height=t * u, stroke_width=0).set_fill(VERDE, 0.9).move_to([xb + 0.35 + 0.95 * i, yb + t * u / 2, 0])
                      for i, t in enumerate(TIEMPO_FFT_MS)])
        nb = VGroup(*[Text(n, color=INK).scale(0.4).move_to([xb + 0.17 + 0.95 * i, yb - 0.25, 0])
                      for i, n in enumerate(("1", "2", "4", "8", "10,25"))])
        base = Line([xb - 0.4, yb, 0], [xb + 4.6, yb, 0], color=INK, stroke_width=2)
        ld = Text("Directa: 1,1 → 10,3 ms", color=AMBAR, weight=BOLD).scale(0.45).move_to([3.4, 3.5, 0])
        lf = Text("FFT: 0,5 ms", color=VERDE, weight=BOLD).scale(0.45).move_to([2.6, 3.0, 0])
        ent = Text("Necesita toda la grabación", color=INK, weight=BOLD).scale(0.5).move_to([-2.5, 1.1, 0])
        Pm = PlanoTF(centro=(-4.9, -1.6), ancho=1.3, alto=1.0, rotulos=False)
        rm = Pm.rampa(0, grosor=4)
        uno = MathTex("256", color=TXT).scale(1.4).move_to([-3.1, -1.6, 0])
        sum_ = MathTex("+\\ 8", r"\text{ sumas}", color=TXT).scale(1.4).move_to([-0.7, -1.6, 0])
        tot = Text("≈ 264 por muestra, no 2.048", color=VERDE, weight=BOLD).scale(0.6).move_to([-2.6, -2.8, 0])
        fl = Arrow([1.4, -1.6, 0], [2.6, -1.6, 0], color=INK, stroke_width=5, buff=0)
        otros = Text("Detectores 2 y 3", color=AMBAR, weight=BOLD).scale(0.65).move_to([4.6, -1.6, 0])
        with self.narrar("b6"):
            # «dos atajos»
            self.en("atajos")
            self.corte()
            self.play(FadeIn(i1, scale=0.5), FadeIn(i2, scale=0.5), run_time=self.dur(0.7))
            # «toda la grabación de una vez»
            self.en("toda")
            self.play(GrowFromEdge(toda, LEFT), FadeIn(rtoda), run_time=self.dur(0.8))
            # «con transformadas rápidas»
            self.en("fft")
            self.pop(fft)
            # «casi no depende del largo»
            self.en("nodep")
            self.play(Create(base), FadeIn(nb), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bd], lag_ratio=0.15),
                      FadeIn(ld), run_time=1.2)
            self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bf], lag_ratio=0.1), FadeIn(lf), run_time=self.dur(0.9))
            # «la grabación entera en memoria»
            self.en("entera")
            self.pop(ent)
            # «el mismo chirp»
            self.en("mismo")
            self.play(FadeIn(Pm), Create(rm), run_time=self.dur(0.6))
            # «correlar con un solo chirp»
            self.en("uno")
            self.pop(uno)
            # «sumar ocho resultados»
            self.en("sumar")
            self.play(Write(sum_), run_time=0.6)
            self.play(FadeIn(tot, shift=UP * 0.15), run_time=self.dur(0.5))
            # «los otros dos detectores»
            self.en("otros")
            self.play(GrowArrow(fl), run_time=0.4)
            self.pop(otros)
