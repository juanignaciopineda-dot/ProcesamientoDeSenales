"""Escena 17 — Cierre: anuncia el E4, «¿Cuánto tarda el azar en olvidar?»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "17"

    def construct(self):
        L = Lienzo(ancho=7.0, alto=2.4, t_rango=(-2, 2), v_max=1.0, centro=(0, -0.1))
        tau = np.linspace(-2, 2, 220)
        Lt = Lienzo(ancho=7.0, alto=1.0, t_rango=(0, 1), v_max=1.3, centro=(0, -2.9))

        with self.narrar("b1"):
            # «mirar sin reloj»
            self.en("sin_reloj")
            r = reloj().scale(1.3).move_to([-5.2, 2.7, 0])
            self.play(FadeIn(r), run_time=0.3)
            tach = tachar(r)
            self.play(Create(tach), run_time=0.3)

            # «depende solo de la separación»
            self.en("separacion")
            rf = MathTex(r"R_{XX}(\tau)", color=AMBAR).scale(1.4).move_to([-1.3, 2.7, 0])
            mini = Lienzo(ancho=3.0, alto=0.5, t_rango=(0, 1), v_max=1.0, centro=(3.2, 2.5))
            b_mini = mini.base()
            m1, m2 = mini.vertical(0.2, AMBAR, 3.0, mitad=0.35), mini.vertical(0.8, AMBAR, 3.0, mitad=0.35)
            llave = BraceBetweenPoints(mini.p(0.8, -0.35), mini.p(0.2, -0.35), color=AMBAR)
            self.play(FadeIn(rf), Create(b_mini), Create(m1), Create(m2), Create(llave), run_time=self.dur(0.8))

            # «es par»
            self.en("par")
            base = L.base()
            eje_v = Line(L.p(0, -0.25), L.p(0, 1.1), color=INK, stroke_width=2)
            curva = L.curva(tau, np.exp(-1.3 * np.abs(tau)), SENAL, 5)
            self.play(Create(base), Create(eje_v), Create(curva), run_time=self.dur(0.9))

            # «tiene su máximo en cero»
            self.en("maximo")
            d0 = Dot(L.p(0, 1.0), radius=0.13, color=AMBAR)
            self.play(FadeIn(d0, scale=0.5), run_time=0.3)
            self.resaltar(d0, escala=2.0)

            # «a qué velocidad cae»
            self.en("cae")
            cae = Arrow(L.p(0.15, 1.0) + UP * 0.3, L.p(1.25, 0.25) + UP * 0.3, color=ROJO, buff=0, stroke_width=5)
            q = etiqueta("¿cuánto tarda?", ROJO, 0.6, BOLD).move_to([3.6, 1.6, 0])
            self.play(Create(cae), FadeIn(q), run_time=self.dur(0.7))

            # «desde ese máximo»
            self.en("desde")
            self.resaltar(d0, escala=2.2)

            # «Un interruptor que salta al azar»
            self.en("interruptor")
            tt = np.linspace(0, 1, 8)
            nivel = [1, -1, -1, 1, -1, 1, 1]
            xs, ys = [], []
            for a, b, n in zip(tt[:-1], tt[1:], nivel):
                xs += [a, b]
                ys += [n, n]
            tel = Lt.curva(np.array(xs), np.array(ys), AMBAR, 4)
            self.play(Create(Lt.base()), Create(tel), run_time=self.dur(1.0), rate_func=linear)

            # «nos lo va a decir»
            self.en("decir")
            der = L.curva(tau[tau >= 0], np.exp(-1.3 * tau[tau >= 0]), AMBAR, 7)
            self.play(Create(der), run_time=self.dur(1.2), rate_func=linear)

            # «¿cuánto tarda el azar en olvidar?»
            self.en("titulo_e4")
            self.limpiar(0.25)
            prox = etiqueta("Próximo episodio", INK, 0.6).move_to([0, 1.7, 0])
            a = self.palabra("¿Cuánto tarda", TXT, 1.6).move_to([0, 0.5, 0])
            b = self.palabra("el azar en olvidar?", AMBAR, 1.6).move_to([0, -1.0, 0])
            self.play(FadeIn(prox), run_time=0.3)
            self.pop(a, b)
        self.wait(1.0)
        self.limpiar()
