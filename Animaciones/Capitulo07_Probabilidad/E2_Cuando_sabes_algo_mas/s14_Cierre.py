"""Escena 14 — Cierre: de eventos sueltos a números aleatorios; anuncia «La forma del azar»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        e = EspacioDado07(centro=(0, 2.4), lado=1.0)
        sob = sobre(AMBAR).scale_to_fit_height(1.3).move_to([-4.6, 0.3, 0])
        nueva = Text("Información nueva", color=AMBAR, weight=BOLD).scale(0.7).next_to(sob, DOWN, buff=0.3)
        bay = MathTex(r"P(A\mid B)=\dfrac{P(B\mid A)\,P(A)}{P(B)}", color=TXT).scale(1.3).move_to([1.8, 0.3, 0])
        giro = CurvedArrow([6.4, -0.4, 0], [6.4, 1.0, 0], angle=PI / 1.5, color=AMBAR)
        marco_e = e.marco.copy()
        t = np.linspace(0, 10, 90)
        rng = np.random.default_rng(14)
        v = np.cumsum(rng.normal(0, 0.35, 90)) * 0.5
        v = (v - v.mean()) * 2.4
        curva = traza(-6.5 + t * 0.6, v - 0.4, color=SENAL, ancho=4)
        puntos = VGroup(*[Dot([-6.5 + t[k] * 0.6, v[k] - 0.4, 0], radius=0.07, color=AMBAR) for k in range(0, 90, 6)])
        pt = Dot([3.5, -0.4, 0], radius=0.14, color=ESTIMACION)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.8).next_to(pt, UP, buff=0.2)
        proximo = Text("Próximo episodio", color=INK).scale(0.7).move_to([0, -3.4, 0])
        titulo_ = self.palabra("La forma del azar", AMBAR, 1.5).move_to([0, 0.5, 0])
        etq = etiqueta("Capítulo 7 · Modelos probabilísticos", INK, 0.55).move_to([0, -0.9, 0])

        with self.narrar("b1"):
            # «información nueva»
            self.en("nueva")
            self.play(FadeIn(e), run_time=self.dur(0.5))
            self.pop(sob)
            self.play(FadeIn(nueva), run_time=self.dur(0.4))

            # «darle la vuelta con Bayes»
            self.en("bayes")
            self.play(FadeIn(bay), Create(giro), run_time=self.dur(0.8))

            # «caras de un dado»
            self.en("dado")
            self.corte()
            self.play(FadeIn(e), run_time=self.dur(0.6))
            self.play(Rotate(e.caras[5], TAU), run_time=self.dur(0.6))

            # «Una señal es un número en cada instante»
            self.en("senal")
            self.corte()
            self.play(Create(curva), run_time=self.dur(1.2))
            self.play(LaggedStart(*[FadeIn(p) for p in puntos], lag_ratio=0.1), run_time=self.dur(0.9))

            # «¿Cómo se describe un número»
            self.en("pregunta")
            self.play(FadeIn(pt), run_time=self.dur(0.3))
            self.pop(interr)

            # «cuánto va a valer»
            self.en("valer")
            for y in (1.6, -1.0, 0.8):
                self.play(pt.animate.move_to([3.5, y, 0]), interr.animate.move_to([3.5, y + 0.6, 0]),
                          run_time=self.dur(0.45))

            # «En el próximo episodio»
            self.en("proximo")
            self.play(FadeIn(proximo), run_time=self.dur(0.4))

            # «La forma del azar»
            self.en("titulo")
            self.corte()
            self.pop(titulo_)
            self.play(FadeIn(etq), run_time=0.4)
        self.wait(1.0)
        self.limpiar()
