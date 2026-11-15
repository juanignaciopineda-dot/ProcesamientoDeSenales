"""Escena 13 — El criterio ergódico: WSS + varianza finita + C(τ) → 0."""
from comun.escena import *


class Criterio(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        piezas = [Text(t, color=c, weight=BOLD).scale(0.62) for t, c in
                  (("WSS", AZUL), ("+", INK), ("σ² < ∞", CIAN), ("+", INK), ("C(τ) → 0", AMBAR),
                   ("⇒", TXT), ("ergódico en media", VERDE))]
        fila = VGroup(*piezas).arrange(RIGHT, buff=0.3).move_to([0, 3.1, 0])
        marco = RoundedRectangle(corner_radius=0.15, width=fila.width + 0.8, height=1.1, color=INK,
                                 stroke_width=3).move_to(fila)

        Lt = Lienzo(ancho=5.6, alto=2.2, t_rango=(-1, 1), v_max=1.0, centro=(-3.6, -1.0))
        Lc = Lienzo(ancho=5.6, alto=2.2, t_rango=(-1, 1), v_max=1.0, centro=(3.6, -1.0))
        tau = np.linspace(-1, 1, 160)

        with self.narrar("b1"):
            # «El criterio»
            self.en("criterio")
            self.play(Create(marco), run_time=0.5)

            # «estacionario en sentido amplio»
            self.en("wss")
            self.pop(piezas[0])

            # «varianza finita»
            self.en("finita")
            self.play(FadeIn(piezas[1]), run_time=0.2)
            self.pop(piezas[2])

            # «tiende a cero»
            self.en("tiende")
            self.play(FadeIn(piezas[3]), run_time=0.2)
            self.pop(piezas[4])

            # «es ergódico en media»
            self.en("ergo")
            self.play(FadeIn(piezas[5]), run_time=0.2)
            self.pop(piezas[6])
            self.play(marco.animate.set_stroke(VERDE), run_time=0.3)

            # «La idea»
            self.en("idea")
            tri = Polygon(Lt.p(-1, 0), Lt.p(0, 1.0), Lt.p(1, 0), color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.12)
            et = etiqueta("pesos", AMBAR, 0.55).move_to(Lt.p(0, 1.0) + UP * 0.35)
            cur = Lc.curva(tau, np.exp(-7 * np.abs(tau)), SENAL, 5)
            ec = MathTex(r"C(\tau)", color=SENAL).scale(0.8).move_to(Lc.p(0.5, 1.3))
            self.play(Create(Lt.base()), Create(Lc.base()), Create(tri), FadeIn(et), run_time=self.dur(0.8))
            self.play(Create(cur), FadeIn(ec), run_time=self.dur(0.6))

            # «el triángulo se estira»
            self.en("estira")
            self.play(tri.animate.stretch(1.7, 0), FadeOut(et), run_time=self.dur(1.2))

            # «solo es grande cerca del cero»
            self.en("cerca")
            zona = Rectangle(width=0.9, height=2.2 * 0.55, color=SENAL, stroke_width=0).set_fill(SENAL, 0.35)
            zona.move_to(Lc.p(0, 0)).align_to(Lc.p(0, 0), DOWN)
            self.play(FadeIn(zona), run_time=0.5)

            # «Esa zona»
            self.en("zona")
            self.resaltar(zona, color=SENAL, escala=1.15)

            # «pesa cada vez menos»
            self.en("menos")
            chica = Rectangle(width=0.5, height=0.55, color=SENAL, stroke_width=0).set_fill(SENAL, 0.45)
            chica.move_to(Lt.p(0, 0)).align_to(Lt.p(0, 0), DOWN)
            self.play(FadeIn(chica), run_time=0.5)
            self.play(chica.animate.scale(0.5, about_point=chica.get_bottom()), run_time=self.dur(0.8))

            # «frente al total»
            self.en("total")
            self.resaltar(tri, escala=1.0)

            # «se va a cero»
            self.en("cero")
            v0 = MathTex(r"\mathrm{Var}\to0", color=VERDE).scale(1.4).move_to([0, -3.3, 0])
            self.pop(v0)
        self.wait(1.0)
        self.limpiar()
