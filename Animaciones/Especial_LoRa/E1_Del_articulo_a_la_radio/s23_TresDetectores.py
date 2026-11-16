"""Escena 23 — Los tres detectores del cuaderno, por dentro: coherente, no coherente y demodular y contar."""
from comun.escena import *
from comun.figuras_lora import *


def _titulo(n, texto, color):
    t = VGroup(insignia(n, color), Text(texto, color=color, weight=BOLD).scale(0.85)).arrange(RIGHT, buff=0.3)
    return t.move_to([0, 3.3, 0])


class TresDetectores(EscenaCurso):
    ESCENA = "23"

    def construct(self):
        self.coherente()
        self.no_coherente()
        self.umbral_gamma()
        self.contar()
        self.umbral_ceros()
        self.comparacion()
        self.wait(1.0)
        self.limpiar()

    def coherente(self):
        nums = VGroup(*[insignia(i, INK) for i in (1, 2, 3)]).arrange(RIGHT, buff=0.6).move_to([0, 3.3, 0])
        tit = _titulo(1, "Preámbulo completo", AMBAR)
        P = PlanoTF(centro=(0, 1.7), ancho=9.6, alto=1.1, n=8, rotulos=False)
        ram = VGroup(*[P.rampa(0, i, grosor=4) for i in range(8)])
        sueltas = [flecha_v(P.p(i + 0.15, 0) + DOWN * 0.6, P.p(i + 0.85, 0) + DOWN * 0.6) for i in range(8)]
        x0, paso, y = -4.8, 1.2, -1.2
        fila = [flecha_v([x0 + paso * i, y, 0], [x0 + paso * (i + 1), y, 0]) for i in range(8)]
        c8 = cota([x0, y - 0.4, 0], [x0 + 8 * paso, y - 0.4, 0], "8", SENAL, DOWN, 0.6)
        v64 = MathTex("T", "=", "8^{2}", "=", "64", color=AMBAR).scale(1.4).move_to([-4.0, -3.1, 0])
        sp = MathTex(r"\Sigma", r"\ \to\ ", r"|\cdot|^{2}", color=TXT).scale(1.4).move_to([0.5, -3.1, 0])
        coh = Text("Coherente", color=VERDE, weight=BOLD).scale(0.9).move_to([4.6, -3.1, 0])
        with self.narrar("b1"):
            # «tres detectores»
            self.en("tres")
            self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in nums], lag_ratio=0.3), run_time=self.dur(1.0))
            # «correlación con el preámbulo completo»
            self.en("full")
            self.play(FadeOut(nums), run_time=0.2)
            self.pop(tit)
            # «ocho correlaciones»
            self.en("ocho")
            self.play(FadeIn(P), LaggedStart(*[Create(r) for r in ram], lag_ratio=0.1), run_time=self.dur(1.2))
            # «Cada una es una flecha»
            self.en("flecha")
            self.play(LaggedStart(*[GrowArrow(f) for f in sueltas], lag_ratio=0.1), run_time=self.dur(1.2))
            # «llegan en fase»
            self.en("enfase")
            self.play(*[f.animate(rate_func=there_and_back).set_color(AMBAR) for f in sueltas], run_time=self.dur(0.9))
            # «apuntan igual»
            self.en("igual")
            self.play(LaggedStart(*[TransformFromCopy(a, b) for a, b in zip(sueltas, fila)], lag_ratio=0.1),
                      run_time=self.dur(1.4))
            # «se mide el largo»
            self.en("largo")
            self.play(FadeIn(c8), run_time=self.dur(0.6))
            # «sesenta y cuatro al cuadrado»
            self.en("v64")
            self.play(Write(v64), run_time=self.dur(0.9))
            # «Sumar primero y medir después»
            self.en("sumarprimero")
            self.play(Write(sp), run_time=self.dur(0.9))
            # «integración coherente»
            self.en("coh")
            self.pop(coh)

    def no_coherente(self):
        tit = _titulo(2, "Ocho picos", CIAN)
        orden = Text("Medir y después sumar", color=TXT, weight=BOLD).scale(0.6).move_to([0, 2.5, 0])
        xs = [-5.3 + 1.42 * i for i in range(8)]
        fl = [flecha_v([x, 1.5, 0], [x + 0.9, 1.5, 0], CIAN) for x in xs]
        unos = VGroup(*[MathTex("1^{2}", color=CIAN).scale(1.0).move_to([x + 0.45, 0.8, 0]) for x in xs])
        mas = VGroup(*[MathTex("+", color=TXT).scale(0.9).move_to([x + 1.16, 0.8, 0]) for x in xs[:-1]])
        v8 = MathTex("S", "=", r"8 \times 1", "=", "8", color=CIAN).scale(1.4).move_to([-0.6, -0.2, 0])
        n64 = MathTex("64", color=INK).scale(1.4).move_to([5.4, -0.2, 0])
        tac = tachar(n64)
        ven = Text("Ventaja", color=VERDE, weight=BOLD).scale(0.75).move_to([-5.6, -1.3, 0])
        nof = Text("No depende de la fase", color=VERDE, weight=BOLD).scale(0.6).move_to([-2.1, -1.3, 0])
        osc = oscilador(AMBAR, 0.4).move_to([5.9, -1.4, 0])
        ini = np.array([1.9, -3.7, 0])
        pts = [ini]
        for i in range(8):
            a = i * 12 * DEGREES
            pts.append(pts[-1] + 0.5 * np.array([np.cos(a), np.sin(a), 0]))
        cadena = [flecha_v(pts[i], pts[i + 1], CIAN, 4, 0.3) for i in range(8)]
        suma = flecha_v(pts[0], pts[-1], ERROR, 5, 0.12)
        enc = Text("Suma coherente: se encoge", color=ERROR, weight=BOLD).scale(0.5).move_to([-3.4, -2.5, 0])
        est = Text("S sigue valiendo 8", color=VERDE, weight=BOLD).scale(0.6).move_to([-3.4, -3.3, 0])
        noc = Text("No coherente", color=CIAN, weight=BOLD).scale(0.75).move_to([5.5, -3.55, 0])
        with self.narrar("b2"):
            # «la búsqueda de ocho picos»
            self.en("picos")
            self.corte()
            self.pop(tit)
            # «cambia el orden»
            self.en("orden")
            self.play(FadeIn(orden, shift=UP * 0.15), run_time=self.dur(0.5))
            # «el largo de cada flecha»
            self.en("cada")
            self.play(LaggedStart(*[GrowArrow(f) for f in fl], lag_ratio=0.1), run_time=1.0)
            self.play(LaggedStart(*[FadeIn(u, shift=UP * 0.1) for u in unos], lag_ratio=0.1), run_time=self.dur(1.2))
            # «después suma»
            self.en("suma")
            self.play(FadeIn(mas), run_time=self.dur(0.5))
            # «Ocho veces uno»
            self.en("v8")
            self.play(Write(v8), run_time=self.dur(1.0))
            # «ya no se multiplica por sesenta y cuatro»
            self.en("no64")
            self.play(FadeIn(n64), run_time=0.3)
            self.play(Create(tac), run_time=self.dur(0.4))
            # «una ventaja»
            self.en("ventaja")
            self.pop(ven)
            # «no necesita que la fase se mantenga»
            self.en("nofase")
            self.play(FadeIn(nof, shift=LEFT * 0.2), run_time=self.dur(0.5))
            # «Si el oscilador deriva»
            self.en("deriva")
            self.pop(osc)
            # «las flechas giran un poco»
            self.en("giran")
            self.play(*[Rotate(f, angle=i * 12 * DEGREES, about_point=f.get_start()) for i, f in enumerate(fl)],
                      run_time=self.dur(1.4))
            # «la suma coherente se encoge»
            self.en("encoge")
            self.play(LaggedStart(*[TransformFromCopy(a, b) for a, b in zip(fl, cadena)], lag_ratio=0.08), run_time=1.0)
            self.play(GrowArrow(suma), FadeIn(enc), run_time=self.dur(0.6))
            # «esta no»
            self.en("estano")
            self.pop(est)
            # «integración no coherente»
            self.en("nocoh")
            self.pop(noc)

    def umbral_gamma(self):
        cri = Text("Mismo criterio, misma tolerancia", color=TXT, weight=BOLD).scale(0.7).move_to([0, 3.3, 0])
        t = np.linspace(0, 5, 40)
        minis = VGroup()
        for i in range(8):
            xi = -5.6 + 1.45 * i
            m = VMobject(stroke_color=RUIDO, stroke_width=3).set_fill(opacity=0)
            m.set_points_as_corners([np.array([xi + v * 0.2, 1.6 + 0.9 * np.exp(-v), 0]) for v in t])
            minis.add(m)
        mas = VGroup(*[MathTex("+", color=TXT).scale(0.8).move_to([-5.6 + 1.45 * i + 1.2, 1.9, 0]) for i in range(7)])
        x0, y0, an, al, tmax = -5.6, -2.7, 9.6, 2.6, 40.0
        X = lambda v: x0 + v / tmax * an
        eje = Line([x0, y0, 0], [x0 + an + 0.2, y0, 0], color=INK, stroke_width=2.5)
        v = np.linspace(0, tmax, 200)
        g = v ** 7 * np.exp(-v) / 5040
        gam = VMobject(stroke_color=RUIDO, stroke_width=4).set_fill(RUIDO, 0.2)
        gam.set_points_as_corners([np.array([X(a), y0 + al * b / g.max(), 0]) for a, b in zip(v, g)])
        gam.permitir_encima = True
        med = VGroup(Line([X(8), y0 - 0.1, 0], [X(8), y0 + 0.1, 0], color=RUIDO, stroke_width=3),
                     Text("Media", color=RUIDO, weight=BOLD).scale(0.42).move_to([X(8), y0 - 0.35, 0]))
        nod = MathTex(r"\eta", "=", "?", color=AMBAR).scale(1.5).move_to([5.3, 0.3, 0])
        prob = VGroup(*[Line([X(a), y0 + 0.5, 0], [X(a), y0, 0], color=AMBAR, stroke_width=4) for a in (16, 36, 26)])
        inter = VGroup(*[Line([X(a), y0 - 0.65 - 0.22 * i, 0], [X(b), y0 - 0.65 - 0.22 * i, 0], color=AMBAR, stroke_width=5)
                         for i, (a, b) in enumerate(((16, 40), (28, 40), (28, 34), (31, 34)))])
        um = DashedLine([X(31.7), y0, 0], [X(31.7), y0 + 2.0, 0], color=AMBAR, stroke_width=3.5, dash_length=0.1)
        fin = MathTex(r"\eta", r"\approx", r"4 \times \text{Media}", color=VERDE).scale(1.2).move_to([4.6, 0.3, 0])
        with self.narrar("b3"):
            # «también sale de Neyman-Pearson»
            self.en("np")
            self.corte()
            self.pop(cri)
            # «la suma de ocho exponenciales»
            self.en("suma8")
            self.play(LaggedStart(*[Create(m) for m in minis], lag_ratio=0.1), FadeIn(mas), run_time=self.dur(1.4))
            # «una distribución gamma»
            self.en("gamma")
            self.play(Create(eje), FadeIn(med), Create(gam, rate_func=linear), run_time=self.dur(1.4))
            # «no se despeja con una fórmula»
            self.en("nodesp")
            self.pop(nod)
            # «probando valores»
            self.en("probando")
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.4) for p in prob], lag_ratio=0.4), run_time=self.dur(1.0))
            # «por bisección»
            self.en("bisec")
            self.play(FadeOut(prob), LaggedStart(*[Create(s) for s in inter], lag_ratio=0.5), run_time=self.dur(1.4))
            # «cuatro veces la media»
            self.en("cuatro")
            self.play(Create(um), FadeOut(nod), run_time=0.4)
            self.pop(fin)

    def contar(self):
        tit = _titulo(3, "Demodular y contar", MAGENTA)
        P = self.P3 = PlanoTF(centro=(0, 1.6), ancho=12.1, alto=1.3, n=11, rotulos=False)
        div = VGroup(*[P.division(i) for i in range(1, 11)])
        g = np.random.default_rng(4)
        ruido = VGroup(*[Dot(P.p(g.uniform(0.05, 2.95), g.uniform(0.1, 0.9)), radius=0.035, color=RUIDO, fill_opacity=0.8)
                         for _ in range(60)])
        ram = VGroup(*[P.rampa(0, 3 + i, grosor=4) for i in range(8)])
        cajas, fl = fila_bloques(["× Chirp que baja", "FFT", "Máximo"], [CIAN, AZUL, AMBAR], centro=(0, -2.6), hueco=0.8,
                                 alto=0.95, escala=0.58)
        nums = VGroup(*[Text(n, color=INK, weight=BOLD).scale(0.55).move_to(P.p(i + 0.5, 0) + DOWN * 0.45)
                        for i, n in enumerate(("137", "52", "201"))])
        ceros = VGroup(*[Text("0", color=AMBAR, weight=BOLD).scale(0.7).move_to(P.p(3.5 + i, 0) + DOWN * 0.45) for i in range(8)])
        s0 = Text("Rampa = símbolo 0", color=AMBAR, weight=BOLD).scale(0.6).move_to([3.4, -0.6, 0])
        cuenta = MathTex("V", "=", r"8\ \text{ceros}", color=AMBAR).scale(1.3).move_to([-3.6, -0.7, 0])
        with self.narrar("b4"):
            # «trabaja en frecuencia»
            self.en("frec")
            self.corte()
            self.pop(tit)
            # «ventanas de un símbolo»
            self.en("ventanas")
            self.play(FadeIn(P), FadeIn(div), FadeIn(ruido), FadeIn(ram), run_time=self.dur(0.9))
            # «demodula cada una»
            self.en("demod")
            self.play(FadeIn(cajas[0]), run_time=0.3)
            self.play(GrowArrow(fl[0]), FadeIn(cajas[1]), GrowArrow(fl[1]), FadeIn(cajas[2]), run_time=self.dur(0.7))
            # «deshacer el chirp»
            self.en("des")
            self.resaltar(cajas[0], color=CIAN, escala=1.1, run_time=self.dur(0.6))
            # «casilla del máximo»
            self.en("casilla")
            self.play(LaggedStart(*[FadeIn(n, shift=DOWN * 0.15) for n in nums], lag_ratio=0.3), run_time=self.dur(0.9))
            # «Un chirp del preámbulo es el símbolo cero»
            self.en("simb0")
            self.pop(s0)
            # «ceros seguidos»
            self.en("ceros")
            self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.15) for c in ceros], lag_ratio=0.12), run_time=self.dur(1.2))
            # «cuenta cuántos ceros»
            self.en("cuenta")
            self.pop(cuenta)

    def umbral_ceros(self):
        sr = Text("Solo ruido", color=RUIDO, weight=BOLD).scale(0.8).move_to([-4.9, 3.3, 0])
        cas = VGroup(*[Square(side_length=0.5, color=INK, stroke_width=2) for _ in range(16)]).arrange(RIGHT, buff=0.1)
        cas.move_to([0, 2.3, 0])
        luz = Square(side_length=0.5, stroke_width=0).set_fill(AMBAR, 0.9).move_to(cas[11])
        p256 = MathTex(r"P(\text{cero})", "=", r"\frac{1}{256}", color=TXT).scale(1.2).move_to([0, 1.1, 0])
        dos = MathTex(r"\text{2 ceros o más: }", r"4 \cdot 10^{-4}", color=TXT).scale(1.0).move_to([-0.6, -0.1, 0])
        xd = cruz(ERROR, 0.5).next_to(dos, RIGHT, buff=0.4)
        tol = MathTex(r"\text{Tolerancia: }", r"3{,}4 \cdot 10^{-5}", r"\text{ por símbolo}", color=INK).scale(0.85).move_to([0, -0.85, 0])
        tres = MathTex(r"\text{3 ceros o más: }", r"3 \cdot 10^{-6}", color=TXT).scale(1.0).move_to([-0.6, -1.6, 0])
        ok = tilde(VERDE, 0.5).next_to(tres, RIGHT, buff=0.4)
        k3 = Text("Umbral: 3 de 8", color=AMBAR, weight=BOLD).scale(0.85).move_to([-3.8, -2.6, 0])
        bar = Text("El más barato", color=VERDE, weight=BOLD).scale(0.7).move_to([3.4, -2.5, 0])
        f1 = Text("1 FFT por símbolo", color=TXT, weight=BOLD).scale(0.55).move_to([3.4, -3.1, 0])
        f2 = Text("en vez de 1 correlación por muestra", color=INK, weight=BOLD).scale(0.4).move_to([3.4, -3.6, 0])
        gan = Text("Solo el máximo", color=INK, weight=BOLD).scale(0.55).move_to([-3.8, -3.2, 0])
        tira = Text("Pierde información", color=ERROR, weight=BOLD).scale(0.55).move_to([-3.8, -3.65, 0])
        with self.narrar("b5"):
            # «Con solo ruido»
            self.en("ruido")
            self.corte()
            self.pop(sr)
            # «cualquiera de las doscientas cincuenta y seis casillas»
            self.en("cualq")
            self.play(FadeIn(cas), FadeIn(luz), run_time=0.4)
            for i in (3, 14, 7, 0):
                self.play(luz.animate.move_to(cas[i]), run_time=0.3)
                self.wait(0.3)
            # «una vez de cada doscientas cincuenta y seis»
            self.en("p256")
            self.play(Write(p256), run_time=self.dur(1.0))
            # «dos ceros»
            self.en("dos")
            self.play(Write(dos), run_time=self.dur(1.0))
            # «demasiado a menudo»
            self.en("amenudo")
            self.play(FadeIn(tol), Create(xd), run_time=self.dur(0.7))
            # «tres, tres veces en un millón»
            self.en("tres")
            self.play(Write(tres), run_time=1.0)
            self.play(Create(ok), run_time=self.dur(0.4))
            # «tres ceros de ocho»
            self.en("k3")
            self.pop(k3)
            # «el más barato»
            self.en("barato")
            self.pop(bar)
            # «una transformada por símbolo»
            self.en("fft")
            self.play(FadeIn(f1, shift=UP * 0.1), run_time=self.dur(0.5))
            # «una correlación por muestra»
            self.en("corr")
            self.play(FadeIn(f2, shift=UP * 0.1), run_time=self.dur(0.5))
            # «la casilla ganadora»
            self.en("ganadora")
            self.play(FadeIn(gan, shift=UP * 0.1), run_time=self.dur(0.5))
            # «tira información»
            self.en("tira")
            self.pop(tira)

    def comparacion(self):
        E = EjesXY(centro=(3.2, -0.3), ancho=6.4, alto=5.4, x=(-24, -11), y=(1e-3, 1), log_y=True,
                   x_marcas=(-24, -20, -16, -12), y_marcas=(1, 1e-1, 1e-2, 1e-3), rot_x="SNR (dB)", rot_y="FER",
                   escala=0.45)
        curvas = [E.curva(FER3_SNR, v, c, 4.5) for v, c in
                  zip((FER3_COMPLETO, FER3_PICOS, FER3_DEMOD), (AMBAR, CIAN, MAGENTA))]
        for c in curvas:
            c.permitir_encima = True
        c1 = cota(E.p(-20.6, 0.5), E.p(-18.8, 0.5), "", TXT)
        c2 = cota(E.p(-18.6, 0.5), E.p(-16.6, 0.5), "", TXT)
        r2 = Text("≈ 2 dB cada salto", color=TXT, weight=BOLD).scale(0.5).move_to(E.p(-20.3, 0.006))
        info = Text("Información usada", color=INK, weight=BOLD).scale(0.6).move_to([-4.1, 3.0, 0])
        filas = [Text(t, color=c, weight=BOLD).scale(0.62).move_to([-4.1, y, 0]) for t, c, y in
                 (("1 · Fase y amplitud", AMBAR, 1.9), ("2 · Solo amplitud", CIAN, 0.3), ("3 · Solo el máximo", MAGENTA, -1.3))]
        cu = [Text(t, color=INK, weight=BOLD).scale(0.48).move_to([-4.1, y - 0.6, 0]) for t, y in
              (("≈ 2.048 mult. por muestra", 1.9), ("≈ 264 mult. por muestra", 0.3), ("≈ 8 mult. por muestra", -1.3))]
        with self.narrar("b6"):
            # «las tramas perdidas»
            self.en("fer")
            self.corte()
            self.play(FadeIn(E.todo), run_time=self.dur(0.7))
            # «en ese orden»
            self.en("orden")
            self.play(LaggedStart(*[Create(c, rate_func=linear) for c in curvas], lag_ratio=0.3), run_time=self.dur(1.2))
            # «dos decibelios entre cada uno»
            self.en("db2")
            self.play(FadeIn(c1.linea), FadeIn(c2.linea), FadeIn(r2), run_time=self.dur(0.6))
            # «Cuanta más información»
            self.en("info")
            self.pop(info)
            # «la fase»
            self.en("fase")
            self.pop(filas[0])
            # «la amplitud»
            self.en("amp")
            self.play(FadeIn(filas[1], shift=UP * 0.15), FadeIn(filas[2], shift=UP * 0.15), run_time=self.dur(0.7))
            # «más cuentas hace»
            self.en("cuentas")
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in cu], lag_ratio=0.25), run_time=self.dur(1.0))
