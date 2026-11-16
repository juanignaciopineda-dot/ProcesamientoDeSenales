"""Escena 21 — El umbral sobre la curva T[k]: lo que se ignora, el cruce, la falsa alarma y la pérdida."""
from comun.escena import *
from comun.figuras_lora import *

M = M_DEMO
N0 = 13            # símbolos de silencio antes de la trama (para tener un tramo de puro ruido)
NT = 34            # símbolos dibujados
DATOS = DATOS_DEMO


class ElUmbralEnAccion(EscenaCurso):
    ESCENA = "21"

    def construct(self):
        P = self.P = PlanoTF(centro=(0, 2.9), ancho=13.4, alto=1.0, n=NT, rotulos=False)
        r, sigma2 = senal_demo(N0, NT, -14.0, 5)
        T = self.T = correlacion_preambulo(r, M)
        self.eta = umbral_demo(sigma2)
        self.y0, self.esc = -3.3, 3.6 / 115.0          # el pico (≈ 100) y un umbral más alto caben en pantalla
        self.k0 = N0 * M
        self.kc = int(np.flatnonzero(T >= self.eta)[0])
        self.n_ruido = (N0 - 8) * M - M // 2            # hasta aquí la plantilla no toca la trama
        self.kr = int(np.argmax(T[: self.n_ruido]))
        self.normal()
        self.subida()
        self.falsa_alarma()
        self.perdida()
        self.wait(1.0)
        self.limpiar()

    def xy(self, k, v=None):
        v = self.T[k] if v is None else v
        return np.array([self.P.p(k / M, 0)[0], self.y0 + v * self.esc, 0.0])

    def nivel(self, v, hasta=26.0, color=ERROR):
        return DashedLine(self.xy(0, v), self.xy(int(hasta * M), v), color=color, stroke_width=3.5, dash_length=0.12)

    def normal(self):
        P, T = self.P, self.T
        sube, baja, datos = trama_tf(P, N0, DATOS, M, 2.5)
        g = np.random.default_rng(4)
        ruido = VGroup(*[Dot(P.p(g.uniform(0.1, N0 - 0.1), g.uniform(0.1, 0.9)), radius=0.03, color=RUIDO,
                             fill_opacity=0.8) for _ in range(110)])
        self.tira = VGroup(P, ruido, sube, baja, datos)
        ks = np.arange(0, T.size, 2)
        curva = self.curva = VMobject(stroke_color=ESTIMACION, stroke_width=2.6).set_fill(opacity=0)
        curva.set_points_as_corners([self.xy(int(k)) for k in ks])
        curva.permitir_encima = True
        base = Line(self.xy(0, 0), self.xy(T.size, 0), color=INK, stroke_width=2)
        rt = MathTex("T[k]", color=ESTIMACION).scale(0.9).move_to([5.9, -2.8, 0])
        linea = self.linea = self.nivel(self.eta)
        re = self.re = MathTex(r"\eta", color=ERROR).scale(1.2).next_to(linea, RIGHT, buff=0.15)
        llave = cota(self.xy(0, 0) + DOWN * 0.3, self.xy(self.n_ruido, 0) + DOWN * 0.3, "Solo ruido", RUIDO, DOWN, 0.45, 0.08)
        ct = cota(self.xy(self.kr) + UP * 0.08, self.xy(self.kr, self.eta), "", TXT)
        nofa = Text("No son falsas alarmas", color=VERDE, weight=BOLD).scale(0.6).move_to([-3.6, 0.9, 0])
        self.pc = Dot(self.xy(self.kc, self.eta), radius=0.13, color=VERDE)
        self.pc.permitir_encima = True
        decl = Text("Trama", color=VERDE, weight=BOLD).scale(0.7).move_to(self.xy(self.kc, self.eta) + LEFT * 0.95 + UP * 0.3)
        self.b1 = (llave, ct, nofa, decl)
        with self.narrar("b1"):
            # «la curva del parecido»
            self.en("curva")
            self.play(FadeIn(self.tira), FadeIn(base), FadeIn(rt), Create(curva, rate_func=linear), run_time=self.dur(1.6))
            # «el umbral dibujado»
            self.en("umbral")
            self.play(Create(linea), FadeIn(re), run_time=self.dur(0.8))
            # «los bultos del ruido»
            self.en("bultos")
            self.play(FadeIn(llave), run_time=self.dur(0.6))
            # «no llegan al umbral»
            self.en("nollegan")
            self.play(FadeIn(ct), run_time=self.dur(0.6))
            # «No son falsas alarmas»
            self.en("nofa")
            self.pop(nofa)
            # «los ignora»
            self.en("ignora")
            self.play(llave.animate.fade(0.6), ct.animate.fade(0.6), run_time=self.dur(0.6))
            # «cruza el umbral»
            self.en("cruza")
            self.pop(self.pc)
            # «se declara la trama»
            self.en("declara")
            self.pop(decl)

    def subida(self):
        P = self.P
        guia = DashedLine(self.xy(self.k0 - 8 * M, 0), self.xy(self.k0), color=TXT, stroke_width=2.5, dash_length=0.1)
        ancho = 8 * P.ancho / P.n
        marco = Rectangle(width=ancho, height=1.25, color=AMBAR, stroke_width=4)
        marco.permitir_encima = True
        marco.move_to(P.p((self.k0 - 5 * M) / M + 4, 0.5))
        ini = DashedLine(P.p(N0, 1) + UP * 0.1, self.xy(self.k0, 0), color=AMBAR, stroke_width=2.5, dash_length=0.1)
        fl = Arrow(self.xy(self.kc, self.eta), self.xy(self.k0), color=VERDE, stroke_width=5, buff=0.05)
        franja = Rectangle(width=ancho, height=self.T[self.k0] * self.esc + 0.2, stroke_width=0).set_fill(VERDE, 0.12)
        franja.move_to([self.xy(self.kc)[0] + ancho / 2, self.y0 + franja.height / 2, 0])
        franja.permitir_encima = True
        pico = Dot(self.xy(self.k0), radius=0.14, color=AMBAR)
        pico.permitir_encima = True
        self.b2 = (guia, marco, ini, fl, franja, pico)
        with self.narrar("b2"):
            # «Va creciendo»
            self.en("crece")
            self.play(*[FadeOut(m) for m in self.b1], Create(guia), run_time=self.dur(1.2))
            # «cubre más chirps del preámbulo»
            self.en("cubre")
            self.play(FadeIn(marco), run_time=self.dur(0.5))
            # «cruza el umbral»
            self.en("cruce")
            self.play(self.pc.animate(rate_func=there_and_back).scale(1.8), run_time=self.dur(0.6))
            # «un poco antes del inicio»
            self.en("antes")
            self.play(Create(ini), run_time=self.dur(0.7))
            # «cuando ya cubre casi todos»
            self.en("casi")
            self.play(marco.animate.move_to(P.p(self.kc / M + 4, 0.5)), run_time=self.dur(1.4))
            # «no se queda con el cruce»
            self.en("noqueda")
            self.play(self.pc.animate.fade(0.6), run_time=self.dur(0.5))
            # «busca el máximo»
            self.en("busca")
            self.play(GrowArrow(fl), run_time=self.dur(0.6))
            # «los ocho símbolos siguientes»
            self.en("ocho")
            self.play(FadeIn(franja), run_time=self.dur(0.6))
            # «Ese máximo es el inicio»
            self.en("inicio")
            self.play(marco.animate.move_to(P.p(N0 + 4, 0.5)), run_time=0.4)
            self.pop(pico)

    def falsa_alarma(self):
        T = self.T
        bajo = 0.8 * T[self.kr]
        preg = Text("¿Falsa alarma?", color=ERROR, weight=BOLD).scale(0.75).move_to([-3.4, 1.2, 0])
        circ = Circle(radius=0.22, color=ERROR, stroke_width=4).move_to(self.xy(self.kr))
        circ.permitir_encima = True
        lejos = cota(self.xy(self.kr, 0) + DOWN * 0.3, self.xy(self.k0, 0) + DOWN * 0.3, "Sin trama", INK, DOWN, 0.45, 0.08)
        fa = Text("Falsa alarma", color=ERROR, weight=BOLD).scale(0.75).move_to([-3.4, 1.2, 0])
        basura = Text("201 · 37 · 5 …", color=INK, weight=BOLD).scale(0.6).move_to([-3.4, 0.45, 0])
        minuto = Text("Bien puesto: 1 por minuto", color=VERDE, weight=BOLD).scale(0.55).move_to([3.2, 1.2, 0])
        # otros bultos de puro ruido que también cruzan el umbral bajo (máximos separados medio símbolo)
        otros, k = [], 0
        while k < self.n_ruido:
            j = k + int(np.argmax(T[k:k + M // 2]))
            if T[j] >= bajo and abs(j - self.kr) > M // 4:
                otros.append(j)
            k += M // 2
        mas = VGroup(*[Circle(radius=0.2, color=ERROR, stroke_width=4).move_to(self.xy(j)) for j in otros[:6]])
        for m in mas:
            m.permitir_encima = True
        self.b3 = (circ, lejos, fa, basura, minuto, mas)
        with self.narrar("b3"):
            # «una falsa alarma»
            self.en("pregunta")
            self.play(*[FadeOut(m) for m in self.b2], FadeOut(self.pc), run_time=0.3)
            self.pop(preg)
            # «Bajemos el umbral»
            self.en("bajemos")
            self.play(self.linea.animate.shift(DOWN * (self.eta - bajo) * self.esc),
                      self.re.animate.shift(DOWN * (self.eta - bajo) * self.esc), run_time=self.dur(1.4))
            # «un bulto de puro ruido lo cruza»
            self.en("cruza")
            self.play(Create(circ), run_time=self.dur(0.5))
            self.sfx("error")
            # «lejos de cualquier trama»
            self.en("lejos")
            self.play(FadeIn(lejos), run_time=self.dur(0.6))
            # «donde no la hay»
            self.en("nohay")
            self.play(FadeOut(preg), run_time=0.2)
            self.pop(fa)
            # «demodular ruido»
            self.en("demod")
            self.play(FadeIn(basura, shift=DOWN * 0.15), run_time=self.dur(0.5))
            # «una vez por minuto»
            self.en("minuto")
            self.pop(minuto)
            # «a cada rato»
            self.en("rato")
            self.play(LaggedStart(*[Create(m) for m in mas], lag_ratio=0.2), run_time=self.dur(0.9))
        self.bajo = bajo

    def perdida(self):
        T = self.T
        alto = 1.1 * T[self.k0]
        ct = cota(self.xy(self.k0) + UP * 0.05, self.xy(self.k0, alto), "", TXT)
        per = Text("Pérdida", color=AMBAR, weight=BOLD).scale(0.8).move_to(self.xy(self.k0, alto) + RIGHT * 1.4 + DOWN * 0.35)
        tol = Text("1 falsa alarma por minuto", color=VERDE, weight=BOLD).scale(0.6).move_to([-3.4, 1.2, 0])
        d1 = (alto - self.bajo) * self.esc
        d2 = (alto - self.eta) * self.esc
        with self.narrar("b4"):
            # «lo subimos demasiado»
            self.en("subimos")
            self.play(*[FadeOut(m) for m in self.b3], self.linea.animate.shift(UP * d1), self.re.animate.shift(UP * d1),
                      run_time=self.dur(1.2))
            # «ni el pico del preámbulo llega»
            self.en("nollega")
            self.play(FadeIn(ct), run_time=self.dur(0.6))
            # «una pérdida»
            self.en("perdida")
            self.pop(per)
            # «entre los dos extremos»
            self.en("entre")
            self.play(FadeOut(ct), FadeOut(per), self.linea.animate.shift(DOWN * d2), self.re.animate.shift(DOWN * d2),
                      run_time=self.dur(1.2))
            # «la tolerancia»
            self.en("tol")
            self.pop(tol)
