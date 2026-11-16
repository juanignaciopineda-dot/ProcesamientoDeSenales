"""Escena 28 — La Ec. 2 (dos pasadas) contra el chirp corregido (una pasada): demodula igual, sincroniza peor."""
from comun.escena import *
from comun.figuras_lora import *


def _peine(E, corregida, color):
    """La curva del parecido sin ruido para corrimientos de −2 a +2 símbolos."""
    M = 64
    T = peine_preambulo(corregida, M)
    xs = np.arange(-2 * M, 2 * M + 1) / M
    c = E.curva(xs, T[M:5 * M + 1], color, 3.5)
    c.permitir_encima = True
    return c


def _ejes_peine(centro, ancho, alto):
    return EjesXY(centro=centro, ancho=ancho, alto=alto, x=(-2, 2), y=(0, 1.15), x_marcas=(-2, -1, 0, 1, 2),
                  y_marcas=(0.5, 1), rot_x="Corrimiento de la plantilla (símbolos)", rot_y="Parecido")


class DosPasadasContraUna(EscenaCurso):
    ESCENA = "28"

    def construct(self):
        self.pregunta()
        self.demodulacion()
        self.medio_simbolo()
        self.pico_falso()
        self.una_pasada()
        self.numeros()
        self.respuesta()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1 y b2
    def pregunta(self):
        lup = lupa().scale(1.4).move_to([-6.2, 3.2, 0])
        self.r_ec2 = Text("Ec. 2", color=AMBAR, weight=BOLD).scale(0.75).move_to([-3.6, 3.3, 0])
        self.r_cor = Text("Corregida", color=VERDE, weight=BOLD).scale(0.75).move_to([3.6, 3.3, 0])
        self.PL = PlanoTF(centro=(-3.6, 1.4), ancho=4.4, alto=2.2, n=1)
        self.PR = PlanoTF(centro=(3.6, 1.4), ancho=4.4, alto=2.2, n=1)
        self.ramL = self.PL.rampa(0, 0, pend=2.0, color=AMBAR)
        self.ramR = self.PR.rampa(0, 0, color=VERDE)
        fL = MathTex(r"2\pi\,", r"\frac{(s+k)\,k}{2^{SF}}", color=TXT).scale(1.1).move_to([-3.6, -1.5, 0])
        fR = MathTex(r"2\pi\,", r"\frac{(s+\frac{k}{2})\,k}{2^{SF}}", color=TXT).scale(1.1).move_to([3.6, -1.5, 0])
        marco = SurroundingRectangle(fR, color=VERDE, buff=0.18, stroke_width=3)
        marco.permitir_encima = True
        fase = Text("Fase", color=INK).scale(0.5).move_to([0, -1.5, 0])
        q = Text("?", color=TXT, weight=BOLD).scale(1.8).move_to([0, 1.4, 0])
        with self.narrar("b1"):
            # «la letra pequeña»
            self.en("letra")
            self.pop(lup)
            # «la ecuación dos»
            self.en("ec2")
            self.play(FadeIn(self.r_ec2, shift=DOWN * 0.2), run_time=self.dur(0.5))
            # «al pie de la letra»
            self.en("pie")
            self.play(FadeIn(self.PL), run_time=self.dur(0.6))
            # «dos veces por símbolo»
            self.en("dos")
            self.play(LaggedStart(*[Create(t) for t in self.ramL], lag_ratio=0.9), run_time=self.dur(1.6))
            # «la corregida»
            self.en("corr")
            self.play(FadeIn(self.r_cor, shift=DOWN * 0.2), FadeIn(self.PR), run_time=self.dur(0.6))
            self.play(Create(self.ramR), run_time=self.dur(1.2))
            # «el índice dividido por dos»
            self.en("k2")
            self.play(FadeIn(fL), FadeIn(fR), FadeIn(fase), run_time=self.dur(0.7))
            self.play(Create(marco), run_time=self.dur(0.6))
            # «¿Cambia algo»
            self.en("cambia")
            self.pop(q)
        self.play(FadeOut(VGroup(lup, fL, fR, marco, fase, q)), run_time=0.3)

    def demodulacion(self):
        igual = Text("Demodulación: igual", color=VERDE, weight=BOLD).scale(0.8).move_to([0, -0.7, 0])
        orto = Text("Ortogonales", color=TXT).scale(0.6).move_to([-2.4, -1.6, 0])
        ener = Text("Misma energía", color=TXT).scale(0.6).move_to([2.4, -1.6, 0])
        opt = bloque("Receptor óptimo", AZUL, None, 0.8, 0.5).move_to([0, -2.6, 0])
        v = np.full(M7, 0.02)
        v[S_EJEMPLO] = 1.0
        CL = CasillasFFT(v, centro=(-3.6, 0.5), ancho=5.0, alto=2.0, v_max=1.1)
        CR = CasillasFFT(v, centro=(3.6, 0.5), ancho=5.0, alto=2.0, v_max=1.1)
        picos = []
        for C in (CL, CR):
            b = C.barras[S_EJEMPLO]
            b.set_stroke(color=AMBAR, width=6)
            b.save_state()
            b.put_start_and_end_on(C.pie(S_EJEMPLO), C.pie(S_EJEMPLO) + UP * 0.02)
            picos.append(b)
        n20 = VGroup(*[Text("20", color=AMBAR, weight=BOLD).scale(0.5).next_to(C.cima(S_EJEMPLO), UP, buff=0.1)
                       for C in (CL, CR)])
        ber = MathTex(r"\text{BER a }-9\text{ dB:}\quad 0{,}005", "=", "0{,}005", color=TXT).scale(1.0)
        ber.move_to([0, -3.4, 0])
        with self.narrar("b2"):
            # «En la demodulación, nada»
            self.en("nada")
            self.pop(igual)
            # «ortogonales»
            self.en("orto")
            self.play(FadeIn(orto, shift=UP * 0.2), run_time=self.dur(0.5))
            # «la misma energía»
            self.en("ener")
            self.play(FadeIn(ener, shift=UP * 0.2), run_time=self.dur(0.5))
            # «el receptor óptimo»
            self.en("optimo")
            self.play(FadeIn(opt, shift=UP * 0.2), run_time=self.dur(0.5))
            # «Al deshacer el chirp»
            self.en("deshacer")
            self.play(FadeOut(VGroup(self.PL, self.ramL, self.PR, self.ramR)), run_time=self.dur(0.5))
            self.play(FadeIn(CL), FadeIn(CR), run_time=self.dur(0.7))
            # «el mismo tono en la misma casilla»
            self.en("tono")
            self.play(Restore(picos[0]), Restore(picos[1]), run_time=self.dur(0.9))
            self.play(FadeIn(n20), run_time=self.dur(0.4))
            # «coincide»
            self.en("coincide")
            self.play(FadeIn(ber, shift=UP * 0.2), run_time=self.dur(0.6))
        self.wait(0.3)
        self.corte()

    # ------------------------------------------------------------ b3 y b4
    def medio_simbolo(self):
        tit = Text("Inicio de la trama", color=TXT, weight=BOLD).scale(0.8).move_to([0, 3.5, 0])
        P = PlanoTF(centro=(-2.2, 1.6), ancho=5.6, alto=2.2, n=1)
        ram = P.rampa(0, 0, pend=2.0, color=AMBAR)
        mitad = P.division(0.5)
        s0 = Text("Ec. 2, símbolo 0", color=AMBAR, weight=BOLD).scale(0.6).move_to([3.9, 2.3, 0])
        copia = ram[0].copy().set_color(CIAN).set_stroke(width=8)
        copia.permitir_encima = True
        rep = MathTex(r"c\!\left[k+\tfrac{M}{2}\right]", "=", "c[k]", color=CIAN).scale(1.2).move_to([3.9, 1.2, 0])
        self.PS = PlanoTF(centro=(0, -1.7), ancho=12.0, alto=1.3, n=8, rotulos=False)
        self.div = VGroup(*[self.PS.division(i) for i in range(1, 8)])
        self.medias = VGroup(*[self.PS.rampa(0, i / 2, pend=2.0, dur=0.5, color=AMBAR, grosor=3.5) for i in range(16)])
        c8 = cota(self.PS.p(0, 0) + DOWN * 0.3, self.PS.p(8, 0) + DOWN * 0.3, "8 símbolos", INK, DOWN, 0.45)
        self.n16 = Text("16 medios chirps iguales", color=AMBAR, weight=BOLD).scale(0.6).move_to([0, -3.5, 0])
        with self.narrar("b3"):
            # «al buscar el inicio»
            self.en("inicio")
            self.pop(tit)
            # «el chirp de la ecuación dos»
            self.en("chirp")
            self.play(FadeIn(P), run_time=self.dur(0.6))
            # «el del preámbulo»
            self.en("pre")
            self.play(FadeIn(s0), LaggedStart(*[Create(t) for t in ram], lag_ratio=0.9), run_time=self.dur(1.5))
            # «su segunda mitad es idéntica a la primera»
            self.en("mitad")
            self.play(FadeIn(mitad), FadeIn(copia), run_time=self.dur(0.5))
            self.play(copia.animate.shift(RIGHT * P.ancho / 2), run_time=self.dur(1.3))
            # «se repite cada medio símbolo»
            self.en("repite")
            self.play(FadeIn(rep, shift=UP * 0.2), run_time=self.dur(0.6))
            # «ocho chirps iguales»
            self.en("ocho")
            self.play(FadeIn(self.PS), FadeIn(self.div), FadeIn(c8), run_time=self.dur(0.7))
            # «dieciséis medios chirps»
            self.en("dieciseis")
            self.play(LaggedStart(*[Create(m) for m in self.medias], lag_ratio=0.08), run_time=self.dur(1.3))
            self.play(FadeOut(c8), FadeIn(self.n16), run_time=0.4)
        self.wait(0.3)
        self.corte(self.PS, self.div, self.medias, self.n16)

    def pico_falso(self):
        PS = self.PS
        marco = Rectangle(width=PS.ancho, height=PS.alto + 0.24, color=CIAN, stroke_width=5).move_to(PS.marco)
        marco.permitir_encima = True
        plant = Text("Plantilla", color=CIAN, weight=BOLD).scale(0.5).next_to(marco, UP, buff=0.1).align_to(marco, RIGHT)
        q15 = Text("Encajan 15 de 16", color=CIAN, weight=BOLD).scale(0.6).move_to([0, -3.5, 0])
        E = _ejes_peine((0, 1.55), 9.0, 2.3)
        peine = _peine(E, False, AMBAR)
        v88 = VGroup(*[MathTex("0{,}88", color=ERROR).scale(0.8).next_to(E.p(x, 0.879), UP, buff=0.12).shift(RIGHT * d)
                       for x, d in ((-0.5, -0.25), (0.5, 0.25))])
        falsos = VGroup(*[Line(E.p(x, 0), E.p(x, 0.879), color=ERROR, stroke_width=6) for x in (-0.5, 0.5)])
        banda = Rectangle(width=9.0, height=E.p(0, 1.06)[1] - E.p(0, 0.8)[1], stroke_width=0).set_fill(RUIDO, 0.28)
        banda.move_to([0, (E.p(0, 1.06)[1] + E.p(0, 0.8)[1]) / 2, 0])
        banda.permitir_encima = True
        det = Text("Trama detectada", color=VERDE, weight=BOLD).scale(0.55).move_to([-5.2, 3.72, 0])
        fl = CurvedArrow(E.p(0, 1.0) + UP * 0.12, E.p(-0.5, 0.879) + UP * 0.62 + LEFT * 0.25, color=ERROR, stroke_width=5,
                         angle=0.9, tip_length=0.22)
        fl.permitir_encima = True
        perd = Text("Trama perdida", color=ERROR, weight=BOLD).scale(0.55).move_to([5.2, 3.72, 0])
        with self.narrar("b4"):
            # «desliza la plantilla»
            self.en("desliza")
            self.play(Create(marco), FadeIn(plant), run_time=self.dur(0.9))
            # «medio símbolo»
            self.en("medio")
            self.play(VGroup(marco, plant).animate.shift(LEFT * PS.ancho / 16), run_time=self.dur(1.2))
            # «quince de los dieciséis»
            self.en("quince")
            self.play(FadeOut(self.n16), run_time=0.2)
            self.pop(q15)
            # «ochenta y ocho por ciento»
            self.en("p88")
            self.play(FadeIn(E.todo), run_time=self.dur(0.5))
            self.play(Create(peine), run_time=self.dur(1.2))
            self.play(FadeIn(v88), run_time=self.dur(0.4))
            # «un pico falso pegado al verdadero»
            self.en("falso")
            self.play(LaggedStart(*[Create(f) for f in falsos], lag_ratio=0.3), run_time=self.dur(0.8))
            # «con ruido basta muy poco»
            self.en("ruido")
            self.play(FadeIn(banda), run_time=self.dur(0.7))
            self.play(banda.animate(rate_func=there_and_back).set_fill(opacity=0.5), run_time=self.dur(1.2))
            # «encuentra la trama»
            self.en("encuentra")
            self.pop(det)
            # «medio símbolo corrida»
            self.en("corrida")
            self.play(Create(fl), run_time=self.dur(0.9))
            # «una trama perdida»
            self.en("perdida")
            self.pop(perd)
        self.wait(0.3)
        self.corte()

    # ------------------------------------------------------------ b5
    def una_pasada(self):
        tit = Text("Corregida: una pasada", color=VERDE, weight=BOLD).scale(0.7).move_to([-3.6, 3.55, 0])
        P = PlanoTF(centro=(-3.6, 1.9), ancho=4.6, alto=2.2, n=1)
        ram = P.rampa(0, 0, color=VERDE)
        cor = P.rampa(M7 / 2, 0, color=CIAN)
        r_c = Text("Corrida ½ símbolo", color=CIAN, weight=BOLD).scale(0.5).move_to([1.2, 2.7, 0])
        b2 = cota(P.p(0.25, 0.25), P.p(0.25, 0.75), "B/2", TXT, RIGHT, 0.45)
        b2.rot.permitir_encima = True
        orto = Text("Ortogonales", color=TXT, weight=BOLD).scale(0.7).move_to([1.2, 1.8, 0])
        E = _ejes_peine((0.6, -1.75), 9.0, 2.2)
        peine = _peine(E, True, VERDE)
        ceros = VGroup(*[MathTex("0", color=VERDE).scale(1.0).next_to(E.p(x, 0), UP, buff=0.25) for x in (-0.5, 0.5)])
        pts = VGroup(*[Dot(E.p(x, 0.766), radius=0.11, color=AMBAR) for x in (-1, 1)])
        for d in pts:
            d.permitir_encima = True
        v77 = VGroup(*[MathTex("0{,}77", color=AMBAR).scale(0.8).next_to(E.p(x, 0.766), UP, buff=0.15).shift(RIGHT * d)
                       for x, d in ((-1, -0.35), (1, 0.35))])
        with self.narrar("b5"):
            # «una sola pasada»
            self.en("una")
            self.play(FadeIn(tit), FadeIn(P), run_time=self.dur(0.5))
            self.play(Create(ram), run_time=self.dur(1.0))
            # «Corrido medio símbolo»
            self.en("corrido")
            self.play(LaggedStart(*[Create(t) for t in cor], lag_ratio=0.9), FadeIn(r_c), run_time=self.dur(1.4))
            # «desplazado media banda»
            self.en("media")
            self.play(FadeIn(b2), run_time=self.dur(0.7))
            # «ortogonales»
            self.en("orto")
            self.pop(orto)
            # «el parecido es cero»
            self.en("cero")
            self.play(FadeIn(E.todo), run_time=self.dur(0.5))
            self.play(Create(peine), run_time=self.dur(1.2))
            self.play(FadeIn(ceros), run_time=self.dur(0.4))
            # «a un símbolo entero»
            self.en("entero")
            self.play(LaggedStart(*[FadeIn(d, scale=2.5) for d in pts], lag_ratio=0.3), run_time=self.dur(0.9))
            # «setenta y siete por ciento»
            self.en("p77")
            self.play(FadeIn(v77), run_time=self.dur(0.5))
        self.wait(0.3)
        self.corte()

    # ------------------------------------------------------------ b6
    def numeros(self):
        snr = MathTex(r"\text{SNR} = -18\ \text{dB}", color=TXT).scale(0.95).move_to([-5.2, 3.5, 0])
        n15 = Text("1.500 tramas", color=TXT).scale(0.55).move_to([-2.2, 3.5, 0])
        xa, xb, xr = -3.3, -1.3, -5.6
        ys = (2.6, 1.8, 1.0, 0.2)
        cab = VGroup(Text("Ec. 2", color=AMBAR, weight=BOLD).scale(0.55).move_to([xa, ys[0], 0]),
                     Text("Corregida", color=VERDE, weight=BOLD).scale(0.55).move_to([xb, ys[0], 0]))
        raya = Line([-6.9, ys[0] - 0.4, 0], [-0.4, ys[0] - 0.4, 0], color=INK, stroke_width=2)
        filas = [Text(t, color=TXT).scale(0.5).move_to([xr, y, 0])
                 for t, y in zip(("No detectadas", "Mal colocadas", "A medio símbolo"), ys[1:])]

        def num(v, x, y, color):
            return MathTex(v, color=color).scale(1.0).move_to([x, y, 0])

        a = [num("12", xa, ys[1], TXT), num("295", xa, ys[2], ERROR), num("227", xa, ys[3], ERROR)]
        b = [num("11", xb, ys[1], TXT), num("75", xb, ys[2], VERDE), num("0", xb, ys[3], VERDE)]
        E = EjesXY(centro=(3.9, 1.5), ancho=4.8, alto=3.2, x=(-24, -10), y=(1e-3, 1), log_y=True,
                   x_marcas=(-24, -20, -16, -12), y_marcas=(1, 1e-1, 1e-2, 1e-3), rot_x="SNR (dB)",
                   rot_y="Tramas perdidas (FER)")
        c1 = E.curva(CMP_SNR, CMP_FER_EC2, AMBAR, 4.5)
        c2 = E.curva(CMP_SNR, CMP_FER_CORR, VERDE, 4.5)
        for c in (c1, c2):
            c.permitir_encima = True
        dif = cota(E.p(-18.7, 0.1), E.p(-16.0, 0.1), r"\approx 2{,}5\ \text{dB}", TXT, UP, 0.42, 0.55, tex=True)
        dif.rot.shift(RIGHT * 1.5)
        dif.rot.permitir_encima = True
        plu = pluto().scale(0.55).move_to([-5.7, -2.6, 0])
        e2 = Text("Ec. 2:", color=AMBAR, weight=BOLD).scale(0.55).move_to([-3.4, -2.2, 0])
        t128 = Text("81 tramas a ±128 muestras", color=ERROR).scale(0.55).next_to(e2, RIGHT, buff=0.25)
        cor = Text("Corregida:", color=VERDE, weight=BOLD).scale(0.55)
        cor.move_to([0, -3.1, 0]).align_to(e2, LEFT)
        t0 = Text("0", color=VERDE, weight=BOLD).scale(0.7).next_to(cor, RIGHT, buff=0.25)
        with self.narrar("b6"):
            # «menos dieciocho decibelios»
            self.en("m18")
            self.play(FadeIn(snr, shift=DOWN * 0.2), run_time=self.dur(0.5))
            # «mil quinientas tramas»
            self.en("n1500")
            self.play(FadeIn(n15), FadeIn(cab), Create(raya), run_time=self.dur(0.8))
            # «sin detectar las mismas»
            self.en("mismas")
            self.play(FadeIn(filas[0]), FadeIn(a[0]), FadeIn(b[0]), run_time=self.dur(0.7))
            # «doscientas noventa y cinco»
            self.en("v295")
            self.play(FadeIn(filas[1]), run_time=self.dur(0.3))
            self.pop(a[1])
            # «medio símbolo corridas»
            self.en("medias")
            self.play(FadeIn(filas[2]), FadeIn(a[2]), run_time=self.dur(0.6))
            # «setenta y cinco»
            self.en("v75")
            self.pop(b[1])
            self.play(FadeIn(b[2]), run_time=self.dur(0.4))
            # «dos decibelios y medio»
            self.en("curvas")
            self.play(FadeIn(E.todo), run_time=self.dur(0.4))
            self.play(Create(c1), Create(c2), run_time=self.dur(1.0))
            self.play(FadeIn(dif), run_time=self.dur(0.4))
            # «las capturas del Pluto»
            self.en("pluto")
            self.pop(plu)
            # «con la ecuación dos hay»
            self.en("conec2")
            self.play(FadeIn(e2), run_time=self.dur(0.4))
            # «ciento veintiocho muestras»
            self.en("c128")
            self.play(FadeIn(t128, shift=RIGHT * 0.2), run_time=self.dur(0.6))
            # «ninguno»
            self.en("ninguno")
            self.play(FadeIn(cor), run_time=0.25)
            self.pop(t0)
        self.wait(0.4)
        self.corte()

    # ------------------------------------------------------------ b7
    def respuesta(self):
        d = Text("Demodular: igual", color=VERDE, weight=BOLD).scale(0.9).move_to([0, 3.2, 0])
        s = Text("Sincronizar: peor", color=ERROR, weight=BOLD).scale(0.9).move_to([0, 2.3, 0])
        PL = PlanoTF(centro=(-3.6, -0.3), ancho=4.4, alto=2.0, n=1, rotulos=False)
        PR = PlanoTF(centro=(3.6, -0.3), ancho=4.4, alto=2.0, n=1, rotulos=False)
        rl = PL.rampa(0, 0, pend=2.0, color=AMBAR)
        rr = PR.rampa(0, 0, color=VERDE)
        tl = Text("Ec. 2", color=AMBAR, weight=BOLD).scale(0.55).next_to(PL.marco, UP, buff=0.15)
        tr = Text("Corregida", color=VERDE, weight=BOLD).scale(0.55).next_to(PR.marco, UP, buff=0.15)
        pico = Text("Pico falso: 88 %", color=ERROR, weight=BOLD).scale(0.7).move_to([-3.6, -2.3, 0])
        ok = tilde(VERDE, 0.9).move_to([3.6, -2.3, 0])
        with self.narrar("b7"):
            # «no demodula peor»
            self.en("nodemod")
            self.pop(d)
            # «sincroniza peor»
            self.en("sinc")
            self.pop(s)
            # «se repite a mitad de símbolo»
            self.en("repite")
            self.play(FadeIn(PL), FadeIn(tl), run_time=self.dur(0.4))
            self.play(LaggedStart(*[Create(t) for t in rl], lag_ratio=0.9), run_time=self.dur(1.3))
            # «un pico falso»
            self.en("pico")
            self.pop(pico)
            # «Con una pasada»
            self.en("pasada")
            self.play(FadeIn(PR), FadeIn(tr), run_time=self.dur(0.4))
            self.play(Create(rr), run_time=self.dur(1.0))
            # «una sola forma de encajar»
            self.en("unica")
            self.pop(ok)
