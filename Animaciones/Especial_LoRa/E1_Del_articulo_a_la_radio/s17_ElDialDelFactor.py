"""Escena 17 — El factor de ensanchamiento como dial: velocidad a cambio de sensibilidad (y de alcance)."""
from comun.escena import *
from comun.figuras_lora import *


class ElDialDelFactor(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        self.un_paso()
        self.velocidad()
        self.sensibilidad()
        self.distancia()
        self.dial_final()
        self.wait(1.0)
        self.limpiar()

    def un_paso(self):
        D = Dial(centro=(-3.9, -0.6), radio=2.3)
        filas = [Text(t, color=c, weight=BOLD).scale(0.65).move_to([3.3, y, 0]) for t, c, y in
                 (("Bits por símbolo: 7 → 8", TXT, 2.2), ("Muestras: 128 → 256", TXT, 1.2),
                  ("Duración: 1,02 → 2,05 ms", ERROR, 0.2), ("Casillas: 128 → 256", TXT, -0.8),
                  ("Ganancia: 21 → 24 dB", VERDE, -1.8))]
        with self.narrar("b1"):
            # «el dial»
            self.en("dial")
            self.play(FadeIn(D, scale=0.8), run_time=self.dur(0.7))
            # «Sube el factor en uno»
            self.en("sube")
            self.sfx("tick")
            self.play(D.girar(8), run_time=self.dur(0.8))
            for marca, f in zip(("bit", "muestras", "tiempo", "casillas", "db3"), filas):
                self.en(marca)
                self.pop(f)

    def velocidad(self):
        vel = Text("Velocidad", color=AMBAR, weight=BOLD).scale(1.0).move_to([-4.9, 3.3, 0])
        f = MathTex("R_b", "=", r"\frac{SF}{T_s}", "=", r"\frac{SF \cdot B}{2^{SF}}", color=TXT).scale(1.1).move_to([2.2, 3.0, 0])
        u = 8.4 / 6836
        ys = [1.5 - 0.85 * i for i in range(6)]
        rots = [Text(f"SF {s}", color=TXT, weight=BOLD).scale(0.6).move_to([-5.9, y, 0]) for s, y in zip(SF_DIAL, ys)]
        barras = [Rectangle(width=max(b * u, 0.08), height=0.55, color=SENAL, stroke_width=2.5).set_fill(SENAL, 0.4)
                  .move_to([-5.0 + max(b * u, 0.08) / 2, y, 0]) for b, y in zip(SF_BPS, ys)]
        txt = ("6.836 bit/s", "3.906", "2.197", "1.221", "671", "366 bit/s")
        vals = [Text(t, color=TXT, weight=BOLD).scale(0.55) for t in txt]
        vals[0].move_to(barras[0])
        for v, b in zip(vals[1:], barras[1:]):
            v.next_to(b, RIGHT, buff=0.25)
        barras[5].set_color(ERROR).set_fill(ERROR, 0.6)
        x19 = MathTex(r"\div\, 19", color=ERROR).scale(1.6).move_to([3.6, -2.6, 0])
        with self.narrar("b2"):
            # «la velocidad»
            self.en("vel")
            self.corte()
            self.pop(vel)
            # «los bits de cada símbolo divididos por lo que dura»
            self.en("formula")
            self.play(Write(f), run_time=self.dur(1.6))
            # «Con factor siete» / «seis mil ochocientos»
            self.en("f7")
            self.pop(rots[0])
            self.en("v7")
            self.play(GrowFromEdge(barras[0], LEFT), run_time=0.6)
            self.play(FadeIn(vals[0]), run_time=self.dur(0.3))
            # «Con factor ocho» / «tres mil novecientos»
            self.en("f8")
            self.pop(rots[1])
            self.en("v8")
            self.play(GrowFromEdge(barras[1], LEFT), FadeIn(vals[1]), run_time=self.dur(0.6))
            # «casi parte la velocidad por la mitad»
            self.en("mitad")
            self.play(LaggedStart(*[AnimationGroup(FadeIn(rots[i]), GrowFromEdge(barras[i], LEFT), FadeIn(vals[i]))
                                    for i in (2, 3, 4)], lag_ratio=0.3), run_time=self.dur(1.6))
            # «Con factor doce» / «trescientos sesenta y seis»
            self.en("f12")
            self.pop(rots[5])
            self.en("v12")
            self.play(GrowFromEdge(barras[5], LEFT), FadeIn(vals[5]), run_time=self.dur(0.6))
            # «diecinueve veces más lento»
            self.en("x19")
            self.pop(x19, sonido="impacto")

    def sensibilidad(self):
        E = EjesXY(centro=(-2.0, -0.3), ancho=7.0, alto=5.0, x=(6.5, 12.5), y=(-25, -5), x_marcas=SF_DIAL,
                   y_marcas=(-5, -10, -15, -20, -25), rot_x="SF", rot_y="SNR mínimo (dB)", escala=0.45)
        E.rots[1].shift(RIGHT * 1.2)
        ber = MathTex(r"\mathrm{BER} = 10^{-3}", color=TXT).scale(1.1).move_to([4.6, 3.0, 0])
        pts = E.puntos(SF_DIAL, SF_SNR_MIN, AMBAR, 0.14)
        linea = E.curva(SF_DIAL, SF_SNR_MIN, AMBAR, 3)
        linea.permitir_encima = True
        d8 = MathTex(r"-8{,}2\ \mathrm{dB}", color=AMBAR).scale(0.9).move_to(E.p(7, -8.2) + RIGHT * 1.3 + UP * 0.25)
        d22 = MathTex(r"-22{,}1\ \mathrm{dB}", color=AMBAR).scale(0.9).move_to(E.p(12, -22.1) + LEFT * 1.4 + DOWN * 0.25)
        x160 = Text("Señal = Ruido ÷ 160", color=ERROR, weight=BOLD).scale(0.6).move_to([4.7, 1.6, 0])
        ct = cota(E.p(9.35, -13.7), E.p(9.35, -16.5), "", TXT)
        sit = Text("≈ 2,8 dB por paso", color=VERDE, weight=BOLD).scale(0.65).move_to([4.7, 0.2, 0])
        with self.narrar("b3"):
            # «la otra cara»
            self.en("otra")
            self.corte()
            self.play(FadeIn(E.todo), run_time=self.dur(0.8))
            # «un bit de cada mil»
            self.en("mil")
            self.play(Write(ber), run_time=self.dur(0.8))
            # «Con factor siete»
            self.en("s7")
            self.pop(pts[0])
            # «ocho decibelios por debajo»
            self.en("d8")
            self.play(FadeIn(d8, shift=LEFT * 0.2), run_time=self.dur(0.5))
            # «casi tres decibelios más abajo»
            self.en("paso")
            self.play(LaggedStart(*[FadeIn(p, scale=2.0) for p in pts[1:5]], lag_ratio=0.3), run_time=self.dur(1.4))
            # «Con factor doce»
            self.en("s12")
            self.pop(pts[5])
            self.play(Create(linea), run_time=self.dur(0.4))
            # «veintidós decibelios»
            self.en("d22")
            self.play(FadeIn(d22, shift=RIGHT * 0.2), run_time=self.dur(0.5))
            # «ciento sesenta veces menos potencia»
            self.en("x160")
            self.pop(x160)
            # «No son exactamente tres»
            self.en("notres")
            self.play(FadeIn(ct), run_time=self.dur(0.6))
            # «más sitios donde el ruido puede ganar»
            self.en("sitios")
            self.pop(sit)

    def distancia(self):
        dist = Text("Distancia", color=AMBAR, weight=BOLD).scale(1.0).move_to([-4.8, 3.3, 0])
        ant = antena_simple(TXT, 1.2).move_to([-6.2, 1.9, 0])
        x = np.linspace(0, 1, 400)
        onda = traza(-5.6 + 11.8 * x, 1.9 + 0.6 * np.exp(-3.2 * x) * np.sin(2 * np.pi * 14 * x), CIAN, 3)
        seis = MathTex(r"\text{Distancia} \times 2", r"\ \to\ ", r"-6\ \mathrm{dB}", color=TXT).scale(1.1).move_to([-3.2, 0.3, 0])
        cat = MathTex(r"SF\ 7 \to SF\ 12:", r"\ 14\ \mathrm{dB}", color=TXT).scale(1.1).move_to([3.4, 0.3, 0])
        cat[1].set_color(VERDE)
        b7 = Rectangle(width=2.2, height=0.5, color=SENAL, stroke_width=2.5).set_fill(SENAL, 0.4).move_to([-5.4 + 1.1, -1.1, 0])
        b12 = Rectangle(width=11.0, height=0.5, color=VERDE, stroke_width=2.5).set_fill(VERDE, 0.4).move_to([-5.4 + 5.5, -1.9, 0])
        r7 = Text("SF 7", color=TXT, weight=BOLD).scale(0.45).move_to(b7)
        r12 = Text("SF 12: × 5 de alcance", color=TXT, weight=BOLD).scale(0.45).move_to(b12)
        alt = [Text(t, color=INK, weight=BOLD).scale(0.6).move_to([x_, -3.2, 0]) for t, x_ in
               (("Más ruido", -4.2), ("Paredes", 0.0), ("Menos potencia", 4.0))]
        with self.narrar("b4"):
            # «Distancia»
            self.en("dist")
            self.corte()
            self.pop(dist)
            # «la señal se debilita»
            self.en("debil")
            self.play(FadeIn(ant), Create(onda, rate_func=linear), run_time=self.dur(1.6))
            # «seis decibelios»
            self.en("seis")
            self.play(Write(seis), run_time=self.dur(1.2))
            # «catorce decibelios»
            self.en("catorce")
            self.play(Write(cat), run_time=self.dur(1.2))
            # «cinco veces más alcance»
            self.en("cinco")
            self.play(GrowFromEdge(b7, LEFT), FadeIn(r7), run_time=0.4)
            self.play(GrowFromEdge(b12, LEFT), FadeIn(r12), run_time=self.dur(1.0))
            for marca, a in zip(("ruido", "paredes", "potencia"), alt):
                self.en(marca)
                self.pop(a)

    def dial_final(self):
        D = Dial(centro=(0, 0.4), radio=2.2, sf=9)
        cerca = Text("Cerca · Poco ruido", color=VERDE, weight=BOLD).scale(0.6).move_to([-4.9, 2.2, 0])
        rap = Text("Rápido", color=TXT, weight=BOLD).scale(0.7).move_to([-4.9, 1.2, 0])
        bat = Text("Poca batería", color=TXT, weight=BOLD).scale(0.7).move_to([-4.9, 0.3, 0])
        lejos = Text("Lejos · Mucho ruido", color=ERROR, weight=BOLD).scale(0.6).move_to([4.9, 2.2, 0])
        lle = Text("Lento, pero llega", color=TXT, weight=BOLD).scale(0.7).move_to([4.9, 1.2, 0])
        pre = Text("El precio: tiempo", color=AMBAR, weight=BOLD).scale(1.0).move_to([0, -2.6, 0])
        with self.narrar("b5"):
            # «un dial»
            self.en("dial")
            self.corte()
            self.play(FadeIn(D, scale=0.8), run_time=0.4)
            # «Cerca de la antena»
            self.en("cerca")
            self.pop(cerca)
            # «factor bajo»
            self.en("bajo")
            self.play(D.girar(7), run_time=self.dur(0.7))
            # «rápido»
            self.en("rapido")
            self.pop(rap)
            # «poca batería»
            self.en("bateria")
            self.pop(bat)
            # «Lejos o con mucho ruido»
            self.en("lejos")
            self.pop(lejos)
            # «factor alto»
            self.en("alto")
            self.play(D.girar(12), run_time=self.dur(0.8))
            # «lento, pero llega»
            self.en("llega")
            self.pop(lle)
            # «el punto justo»
            self.en("justo")
            self.play(D.girar(10), run_time=self.dur(1.0))
            # «tiempo»
            self.en("tiempo")
            self.pop(pre, sonido="exito")
