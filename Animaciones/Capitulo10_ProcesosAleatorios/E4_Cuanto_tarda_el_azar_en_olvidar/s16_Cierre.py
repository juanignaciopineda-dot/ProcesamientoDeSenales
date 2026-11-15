"""Escena 16 — Cierre: anuncia el E5, «¿Basta con una sola grabación?»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        L = Lienzo(ancho=7.0, alto=2.4, t_rango=(-2, 2), v_max=1.0, centro=(-2.2, 1.3))
        tau = np.linspace(-2, 2, 220)
        eje = Line(L.p(0, -0.1), L.p(0, 1.15), color=INK, stroke_width=2)
        curva = L.curva(tau, np.exp(-1.3 * np.abs(tau)), SENAL, 5)
        f = MathTex(r"e^{-2\lambda|\tau|}", color=AMBAR).scale(1.5).move_to([4.2, 2.4, 0])
        Lr = Lienzo(ancho=6.0, alto=1.3, t_rango=(0, 8), v_max=2.0, centro=(-2.6, -1.9))
        t = np.linspace(0, 8, 240)
        real = Lr.curva(t, 0.6 * serie(41, 240, 0.96), SENAL, 4)
        llana = Lr.curva(t, 0.45 + 0 * t, SENAL, 4)
        interrog = MathTex(r"?", color=AMBAR).scale(2.0).move_to([1.4, -1.9, 0])
        w = self.palabra("ergódico", AMBAR, 1.3).move_to([4.2, -1.9, 0])
        tach = tachar(w)
        prox = etiqueta("Próximo episodio", INK, 0.6).move_to([0, 1.7, 0])
        a = self.palabra("¿Basta con una", TXT, 1.6).move_to([0, 0.5, 0])
        b = self.palabra("sola grabación?", AMBAR, 1.6).move_to([0, -1.0, 0])

        with self.narrar("b1"):
            # «cómo olvida un proceso»
            self.en("olvida")
            self.play(Create(L.base()), Create(eje), Create(curva), run_time=self.dur(1.2))

            # «una exponencial»
            self.en("expo")
            self.pop(f)

            # «una sola grabación quizá baste»
            self.en("una")
            self.play(Create(Lr.base()), Create(real), run_time=self.dur(1.0))
            self.pop(interrog)

            # «si el proceso es ergódico»
            self.en("ergodico")
            self.pop(w)

            # «¿y si no lo es?»
            self.en("y_si_no")
            self.play(Create(tach), run_time=0.4)

            # «una grabación larga engaña»
            self.en("engana")
            self.play(ReplacementTransform(real, llana), run_time=self.dur(1.0))

            # «En el próximo episodio»
            self.en("proximo")
            self.limpiar(0.25)
            self.play(FadeIn(prox), run_time=0.3)

            # «¿basta con una sola grabación?»
            self.en("titulo_e5")
            self.pop(a, b)
        self.wait(1.0)
        self.limpiar()
