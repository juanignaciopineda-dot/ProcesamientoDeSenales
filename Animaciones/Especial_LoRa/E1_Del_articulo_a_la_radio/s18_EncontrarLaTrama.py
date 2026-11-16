"""Escena 18 — El preámbulo y el detector: correlación con los ocho chirps (filtro adaptado)."""
from comun.escena import *
from comun.figuras_lora import *

M = M_DEMO        # muestras por símbolo en el dibujo (SF = 6, para que la curva sea ligera)
N0 = 5            # símbolos de solo ruido antes de la trama
DATOS = DATOS_DEMO


class EncontrarLaTrama(EscenaCurso):
    ESCENA = "18"

    def construct(self):
        P = self.P = PlanoTF(centro=(0, 2.2), ancho=13.2, alto=1.5, n=26, rotulos=False)
        r, sigma2 = senal_demo(N0, 26)
        T = correlacion_preambulo(r, M)
        self.T = T
        self.tmax, self.y0, self.alto = float(T.max()), -3.1, 2.9
        self.pos = ValueTracker(0.0)
        self.trama()
        self.detector()
        self.umbral()
        self.wait(1.0)
        self.limpiar()

    def xy(self, k):
        """Punto de la curva T[k] (k en muestras): alineado con el borde izquierdo de la plantilla."""
        return np.array([self.P.p(k / M, 0)[0], self.y0 + self.T[k] / self.tmax * self.alto, 0.0])

    def trama(self):
        P = self.P
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.3).move_to(P.marco)
        g = np.random.default_rng(4)
        ruido = VGroup(*[Dot(P.p(g.uniform(0.1, N0 - 0.1), g.uniform(0.08, 0.92)), radius=0.035, color=RUIDO,
                             fill_opacity=0.8) for _ in range(70)])
        sube, baja, datos = trama_tf(P, N0, DATOS, M, 3.5)
        ct = cota(P.p(N0, 1) + UP * 0.3, P.p(25.25, 1) + UP * 0.3, "Trama", TXT, UP, 0.55)
        pre = Text("Preámbulo", color=AMBAR, weight=BOLD).scale(0.55).move_to(P.p(N0 + 5.1, 0) + DOWN * 0.35)
        dat = Text("Datos", color=AZUL, weight=BOLD).scale(0.55).move_to(P.p(20.25, 0) + DOWN * 0.35)
        with self.narrar("b1"):
            # «dónde empieza cada símbolo»
            self.en("donde")
            self.play(FadeIn(P), run_time=0.4)
            self.pop(q)
            # «escucha ruido»
            self.en("ruido")
            self.play(FadeOut(q), LaggedStart(*[FadeIn(d) for d in ruido], lag_ratio=0.02), run_time=self.dur(1.0))
            # «llega una trama»
            self.en("trama")
            self.play(FadeIn(ct), run_time=self.dur(0.6))
            # «un preámbulo»
            self.en("pre")
            self.pop(pre)
            # «ocho chirps del símbolo cero»
            self.en("ocho")
            self.play(LaggedStart(*[Create(s) for s in sube], lag_ratio=0.25), run_time=self.dur(1.8))
            # «dos y cuarto que bajan»
            self.en("bajan")
            self.play(LaggedStart(*[Create(b) for b in baja], lag_ratio=0.3), run_time=self.dur(1.2))
            # «la carga con los datos»
            self.en("carga")
            self.play(LaggedStart(*[Create(d) for d in datos], lag_ratio=0.12), FadeIn(dat), run_time=self.dur(1.4))

    def detector(self):
        P, pos = self.P, self.pos
        ancho = 8 * P.ancho / P.n

        def _marco():
            m = Rectangle(width=ancho, height=1.8, color=AMBAR, stroke_width=5)
            m.move_to(P.p(pos.get_value() + 4, 0.5))
            m.permitir_encima = True
            return m

        def _curva():
            k = max(2, int(pos.get_value() * M))
            pts = [self.xy(i) for i in range(0, k, 2)]
            m = VMobject(stroke_color=ESTIMACION, stroke_width=3).set_fill(opacity=0)
            m.set_points_as_corners(pts)
            m.permitir_encima = True
            return m

        marco = self.marco = always_redraw(_marco)
        curva = self.curva = always_redraw(_curva)
        base = Line([P.p(0, 0)[0], self.y0, 0], [P.p(26, 0)[0], self.y0, 0], color=INK, stroke_width=2)
        rt = MathTex("T[k]", color=ESTIMACION).scale(0.9).move_to([-6.3, 0.2, 0])
        ada = self.ada = Text("Filtro adaptado", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.7, 0.1, 0])
        con = self.con = Text("Señal conocida + Ruido", color=TXT, weight=BOLD).scale(0.5).move_to([4.7, -0.7, 0])
        k5 = N0 * M
        ok = self.ok = tilde(VERDE, 0.7).move_to(self.xy(k5) + RIGHT * 0.65 + DOWN * 0.2)
        vert = self.vert = DashedLine(self.xy(k5), P.p(N0, 0), color=AMBAR, stroke_width=3, dash_length=0.1)
        with self.narrar("b2"):
            # «desliza los ocho chirps»
            self.en("desliza")
            self.play(FadeIn(marco), run_time=self.dur(0.5))
            # «muestra a muestra»
            self.en("mam")
            self.play(pos.animate.set_value(1.2), run_time=self.dur(1.2), rate_func=linear)
            # «mide el parecido»
            self.en("parecido")
            self.add(curva)
            self.play(FadeIn(base), FadeIn(rt), pos.animate.set_value(2.2), run_time=self.dur(1.1), rate_func=linear)
            # «un filtro adaptado»
            self.en("adaptado")
            self.pop(ada)
            # «una señal conocida en ruido»
            self.en("conocida")
            self.play(FadeIn(con, shift=UP * 0.15), run_time=self.dur(0.5))
            # «Donde el preámbulo encaja»
            self.en("encaja")
            self.play(pos.animate.set_value(4.4), run_time=max(0.5, self.margen() - 0.2), rate_func=linear)
            # «el parecido se dispara»
            self.en("dispara")
            self.sfx("impacto", offset=0.9)
            self.play(pos.animate.set_value(N0 + 2 / M), run_time=self.dur(1.1), rate_func=linear)
            # «hay trama»
            self.en("hay")
            self.play(Create(ok), run_time=self.dur(0.4))
            # «en qué muestra empieza»
            self.en("empieza")
            self.play(Create(vert), run_time=self.dur(0.7))

    def umbral(self):
        pos = self.pos
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.6).move_to([4.2, -1.6, 0])
        sino = Text("Sí / No", color=TXT, weight=BOLD).scale(0.9).move_to([5.6, -1.6, 0])
        with self.narrar("b3"):
            # «el ruido también produce parecido»
            self.en("ruidop")
            self.play(FadeOut(self.ada), FadeOut(self.con), FadeOut(self.ok), run_time=0.3)
            self.play(pos.animate.set_value(8.0), run_time=max(0.5, self.margen() - 0.2), rate_func=linear)
            # «¿Cuánto hace falta»
            self.en("cuanto")
            self.pop(q)
            self.play(pos.animate.set_value(11.0), run_time=max(0.5, self.margen() - 0.3), rate_func=linear)
            # «ir despacio»
            self.en("despacio")
            self.pop(sino)
        self.marco.clear_updaters()
        self.curva.clear_updaters()
