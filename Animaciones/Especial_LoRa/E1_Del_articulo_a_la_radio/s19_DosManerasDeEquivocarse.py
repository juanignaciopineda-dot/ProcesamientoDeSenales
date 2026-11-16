"""Escena 19 — Neyman-Pearson (1): las dos hipótesis, cómo se reparte el parecido y los dos errores."""
from comun.escena import *
from comun.figuras_lora import *

X0, ANCHO, Y0 = -5.8, 11.6, -2.6     # eje del parecido T (en unidades de su media con solo ruido, 8σ²)
LAM = 20.5                            # con −20 dB (SF = 8): 64 / (8σ²)
ETA = LN_PFA                          # umbral de Neyman-Pearson en esas unidades: 15,8


def _hipotesis(tex, texto, color):
    """Casilla de una hipótesis: «H₀ · Solo ruido»."""
    h = MathTex(tex, color=color).scale(1.3)
    tx = Text("· " + texto, color=TXT, weight=BOLD).scale(0.6)
    fila = VGroup(h, tx).arrange(RIGHT, buff=0.2)
    marco = RoundedRectangle(corner_radius=0.15, width=fila.width + 0.6, height=1.1, color=color,
                             stroke_width=3).set_fill(color, 0.12).move_to(fila)
    return VGroup(marco, fila)


class DosManerasDeEquivocarse(EscenaCurso):
    ESCENA = "19"

    def construct(self):
        self.hipotesis()
        self.solo_ruido()
        self.con_trama()
        self.errores()
        self.criterio()
        self.wait(1.0)
        self.limpiar()

    # eje ampliado (0 a 8) y eje completo (0 a 36)
    def xa(self, t):
        return X0 + t * ANCHO / 8

    def xc(self, t):
        return X0 + t * ANCHO / 36

    def h0(self, x, t0=0.0, t1=8.0, alto=3.4, n=120):
        """Puntos de la exponencial e^(−t) (la forma del ruido) con el mapa de eje `x`."""
        t = np.linspace(t0, t1, n)
        return [np.array([x(v), Y0 + alto * np.exp(-v), 0.0]) for v in t]

    def h1(self, t0=0.0, t1=36.0, alto=2.2, n=160):
        t = np.linspace(max(t0, 1e-6), t1, n)
        f = densidad_h1(t, LAM) / 0.0627
        return [np.array([self.xc(v), Y0 + alto * w, 0.0]) for v, w in zip(t, f)]

    def hipotesis(self):
        preg = Text("¿Hay trama?", color=TXT, weight=BOLD).scale(1.2).move_to([0, 2.8, 0])
        c0 = _hipotesis("H_0", "Solo ruido", RUIDO).scale(1.25).move_to([-4.4, 0.9, 0])
        c1 = _hipotesis("H_1", "Empieza un preámbulo", SENAL).scale(1.25).move_to([2.8, 0.9, 0])
        T = MathTex("T", color=AMBAR).scale(3.0).move_to([0, -1.8, 0])
        with self.narrar("b1"):
            # «una pregunta de sí o no»
            self.en("pregunta")
            self.pop(preg)
            # «Hipótesis cero»
            self.en("h0")
            self.play(FadeIn(c0, shift=UP * 0.2), run_time=self.dur(0.6))
            # «Hipótesis uno»
            self.en("h1")
            self.play(FadeIn(c1, shift=UP * 0.2), run_time=self.dur(0.6))
            # «un número para decidir»
            self.en("numero")
            self.pop(T)

    def solo_ruido(self):
        eje = self.eje = Line([X0 - 0.2, Y0, 0], [X0 + ANCHO + 0.3, Y0, 0], color=INK, stroke_width=2.5)
        cero = self.cero = Text("0", color=INK).scale(0.5).move_to([X0, Y0 - 0.35, 0])
        rt = self.rt = MathTex("T", color=AMBAR).scale(1.2).move_to([X0 + ANCHO + 0.6, Y0, 0])
        g = np.random.default_rng(6)
        muestras = g.exponential(1.0, 4000)
        caen = VGroup(*[Dot([self.xa(v), Y0 + 0.14, 0], radius=0.09, color=RUIDO) for v in muestras[:14] if v < 7.5])
        cuentas, _ = np.histogram(muestras, bins=32, range=(0, 8))
        dens = cuentas / muestras.size / 0.25
        an = ANCHO / 32
        barras = VGroup(*[Rectangle(width=an * 0.9, height=max(3.4 * d, 0.02), stroke_width=1.5, color=RUIDO)
                          .set_fill(RUIDO, 0.45).move_to([self.xa((i + 0.5) * 0.25), Y0 + max(3.4 * d, 0.02) / 2, 0])
                          for i, d in enumerate(dens)])
        curva = self.c0 = VMobject(stroke_color=TXT, stroke_width=4).set_fill(opacity=0)
        curva.set_points_as_corners(self.h0(self.xa))
        curva.permitir_encima = True
        fl = Arrow([self.xa(6.2), 0.2, 0], [self.xa(6.2), Y0 + 0.35, 0], color=AMBAR, stroke_width=5, buff=0)
        lm = DashedLine([self.xa(1), Y0, 0], [self.xa(1), 1.6, 0], color=AMBAR, stroke_width=3, dash_length=0.1)
        med = MathTex(r"\text{Media}", "=", r"8\sigma^{2}", color=AMBAR).scale(1.2).move_to([self.xa(1) + 1.9, 1.6, 0])
        P = PlanoTF(centro=(3.4, 3.0), ancho=4.8, alto=0.9, n=8, rotulos=False)
        rampas = VGroup(*[P.rampa(0, i, grosor=3.5) for i in range(8)])
        self.zoom_cosas = (barras, lm, P, rampas)
        self.med = med
        with self.narrar("b2"):
            # «no vale cero»
            self.en("nocero")
            self.corte()
            self.play(Create(eje), FadeIn(cero), FadeIn(rt), run_time=self.dur(0.6))
            # «algo al azar»
            self.en("azar")
            self.play(LaggedStart(*[FadeIn(d, shift=DOWN * 1.5) for d in caen], lag_ratio=0.15), run_time=self.dur(2.4))
            # «miles de valores»
            self.en("miles")
            self.play(FadeOut(caen), LaggedStart(*[GrowFromEdge(b, DOWN) for b in barras], lag_ratio=0.04),
                      run_time=self.dur(1.6))
            # «casi siempre son pequeños»
            self.en("peq")
            self.play(*[b.animate(rate_func=there_and_back).set_fill(RUIDO, 0.95) for b in barras[:5]], run_time=self.dur(1.0))
            # «uno grande»
            self.en("grande")
            self.play(GrowArrow(fl), run_time=self.dur(0.6))
            # «una distribución exponencial»
            self.en("expo")
            self.play(FadeOut(fl), Create(curva, rate_func=linear), run_time=self.dur(1.2))
            # «su media»
            self.en("media")
            self.play(Create(lm), FadeIn(med), run_time=self.dur(0.5))
            # «ocho veces la potencia del ruido»
            self.en("ochoveces")
            self.resaltar(med[2], color=AMBAR, escala=1.35, run_time=self.dur(0.7))
            # «ocho chirps de energía uno»
            self.en("ocho")
            self.play(FadeIn(P), LaggedStart(*[Create(r) for r in rampas], lag_ratio=0.1), run_time=self.dur(1.2))

    def con_trama(self):
        c0n = VMobject(stroke_color=RUIDO, stroke_width=4).set_fill(RUIDO, 0.25)
        pts = self.h0(self.xc, 0, 12)
        c0n.set_points_as_corners([np.array([self.xc(0), Y0, 0.0])] + pts + [np.array([self.xc(12), Y0, 0.0])])
        c0n.permitir_encima = True
        c1 = self.c1 = VMobject(stroke_color=SENAL, stroke_width=4).set_fill(SENAL, 0.2)
        c1.set_points_as_corners(self.h1())
        c1.permitir_encima = True
        m1 = self.m1 = Text("Media", color=RUIDO, weight=BOLD).scale(0.42).move_to([self.xc(1) + 0.25, Y0 - 0.35, 0])
        t1 = Line([self.xc(1), Y0 - 0.1, 0], [self.xc(1), Y0 + 0.1, 0], color=RUIDO, stroke_width=3)
        flechas = VGroup(Arrow([self.xc(20), 0.2, 0], [self.xc(13), 0.2, 0], color=SENAL, stroke_width=5, buff=0),
                         Arrow([self.xc(21), 0.2, 0], [self.xc(28), 0.2, 0], color=SENAL, stroke_width=5, buff=0))
        m20 = self.m20 = MathTex(r"\mathrm{SNR} = -20\ \mathrm{dB}", color=SENAL).scale(1.0).move_to([4.2, 2.2, 0])
        t20 = Line([self.xc(20), Y0 - 0.1, 0], [self.xc(20), Y0 + 0.1, 0], color=SENAL, stroke_width=3)
        v20 = self.v20 = Text("20 × Media", color=SENAL, weight=BOLD).scale(0.42).move_to([self.xc(20), Y0 - 0.35, 0])
        zona = Rectangle(width=self.xc(13) - self.xc(3), height=1.2, stroke_width=0).set_fill(AMBAR, 0.25)
        zona.move_to([(self.xc(13) + self.xc(3)) / 2, Y0 + 0.6, 0])
        zona.permitir_encima = True
        noperf = self.noperf = Text("Sin decisión perfecta", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, 3.3, 0])
        self.marcas = VGroup(t1, t20)
        with self.narrar("b3"):
            # «sí hay un preámbulo»
            self.en("h1")
            self.play(*[FadeOut(m) for m in self.zoom_cosas], FadeOut(self.med), ReplacementTransform(self.c0, c0n),
                      FadeIn(m1), FadeIn(t1), run_time=0.8)
            self.c0 = c0n
            self.play(Create(c1, rate_func=linear), run_time=self.dur(1.4))
            # «tampoco es fijo»
            self.en("nofijo")
            self.play(c1.animate(rate_func=wiggle).shift(RIGHT * 0.35), run_time=self.dur(1.2))
            # «sumarle o restarle»
            self.en("sumres")
            self.play(GrowArrow(flechas[0]), GrowArrow(flechas[1]), run_time=self.dur(0.7))
            # «menos veinte decibelios»
            self.en("m20")
            self.play(Write(m20), run_time=self.dur(0.8))
            # «veinte veces la media»
            self.en("veinte")
            self.play(FadeIn(t20), FadeIn(v20, shift=UP * 0.1), run_time=self.dur(0.5))
            # «se solapan»
            self.en("solapan")
            self.play(FadeOut(flechas), FadeIn(zona), run_time=self.dur(0.6))
            # «no hay decisión perfecta»
            self.en("noperf")
            self.pop(noperf)
        self.zona = zona

    def errores(self):
        eta = self.eta = ValueTracker(2.0)
        x = lambda: self.xc(eta.get_value())
        linea = self.linea = always_redraw(lambda: Line([x(), Y0, 0], [x(), 1.0, 0], color=TXT, stroke_width=4))
        rot = self.rot_eta = MathTex(r"\eta", color=TXT).scale(1.4)
        rot.add_updater(lambda m: m.move_to([x(), 1.35, 0]))

        def _cola():
            a = area_bajo(self.h0(self.xc, eta.get_value(), 12.0, n=60), Y0, ERROR, 0.9)
            a.permitir_encima = True
            return a

        def _perd():
            a = area_bajo(self.h1(0.0, eta.get_value(), n=80), Y0, AMBAR, 0.75)
            a.permitir_encima = True
            return a

        cola = self.cola = always_redraw(_cola)
        perd = self.perd = always_redraw(_perd)
        regla = self.regla = MathTex(r"T > \eta", r"\ \Rightarrow\ ", r"\text{Hay trama}", color=TXT).scale(1.1).move_to([0, 3.3, 0])
        h1_, h2_ = [RoundedRectangle(corner_radius=0.12, width=3.4, height=0.75, color=INK, stroke_width=2).move_to([cx, 2.2, 0])
                    for cx in (-3.8, 3.4)]
        fa = Text("Falsa alarma", color=ERROR, weight=BOLD).scale(0.65).move_to(h1_)
        pe = Text("Pérdida", color=AMBAR, weight=BOLD).scale(0.65).move_to(h2_)
        nodos = self.nodos = Text("Una baja, la otra sube", color=TXT, weight=BOLD).scale(0.7).move_to([2.6, 0.5, 0])
        self.cajas = VGroup(h1_, h2_, fa, pe)
        with self.narrar("b4"):
            # «un umbral»
            self.en("umbral")
            self.play(FadeOut(self.noperf), FadeOut(self.zona), FadeOut(self.m20), FadeIn(linea), FadeIn(rot), run_time=self.dur(0.5))
            # «decimos que hay trama»
            self.en("decimos")
            self.play(Write(regla), run_time=self.dur(0.9))
            # «dos maneras de equivocarse»
            self.en("dos")
            self.play(Create(h1_), Create(h2_), run_time=self.dur(0.7))
            # «Falsa alarma»
            self.en("fa")
            self.pop(fa)
            # «el área de la cola»
            self.en("cola")
            cola.update()
            self.play(FadeIn(cola), run_time=self.dur(0.6))
            # «Pérdida»
            self.en("perdida")
            self.pop(pe)
            # «quedó por debajo»
            self.en("debajo")
            self.add(perd)
            self.play(eta.animate.set_value(11.0), run_time=self.dur(1.4))
            # «Si subes el umbral»
            self.en("subes")
            self.play(eta.animate.set_value(19.0), run_time=self.dur(1.6))
            # «Si lo bajas»
            self.en("bajas")
            self.play(eta.animate.set_value(3.0), run_time=self.dur(1.3))
            # «No se pueden bajar las dos»
            self.en("nodos")
            self.pop(nodos)

    def criterio(self):
        eta = self.eta
        np_ = Text("Neyman-Pearson", color=AMBAR, weight=BOLD).scale(0.95).move_to([0, 3.3, 0])
        p1 = Text("1.º Fijar la falsa alarma", color=ERROR, weight=BOLD).scale(0.6).move_to([-3.4, 2.2, 0])
        p2 = Text("2.º Pérdidas: las mínimas", color=AMBAR, weight=BOLD).scale(0.6).move_to([3.4, 2.2, 0])
        pfa = MathTex("P_{FA}", color=ERROR).scale(1.1).move_to([self.xc(ETA) + 1.0, 0.2, 0])
        fl = Arrow(pfa.get_bottom() + DOWN * 0.05, [self.xc(ETA) + 0.25, Y0 + 0.15, 0], color=ERROR, stroke_width=4, buff=0)
        with self.narrar("b5"):
            # «Neyman-Pearson»
            self.en("np")
            self.play(FadeOut(self.regla), FadeOut(self.nodos), FadeOut(self.cajas), run_time=0.3)
            self.pop(np_)
            # «cuántas falsas alarmas se toleran»
            self.en("tolera")
            self.pop(p1)
            # «justo donde la cola del ruido vale eso»
            self.en("justo")
            self.play(eta.animate.set_value(ETA), run_time=self.dur(1.6))
            # «Con ese precio fijado»
            self.en("precio")
            self.play(FadeIn(pfa), GrowArrow(fl), run_time=self.dur(0.6))
            # «la menor cantidad posible de pérdidas»
            self.en("menor")
            self.pop(p2)
        self.linea.clear_updaters()
        self.cola.clear_updaters()
        self.perd.clear_updaters()
        self.rot_eta.clear_updaters()
