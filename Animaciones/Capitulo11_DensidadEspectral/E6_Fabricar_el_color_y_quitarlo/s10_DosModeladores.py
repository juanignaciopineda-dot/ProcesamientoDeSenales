"""Escena 10 — Dos modeladores: (2, 1)/√5 y (1, 2)/√5 fabrican el mismo proceso (potencia 1, vecinas 0,4)."""
from comun.escena import *


class DosModeladores(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        rho = MathTex(r"\rho=0{,}4", color=AMBAR).scale(1.0).move_to([-5.0, 3.5, 0])
        c1 = caja_tex(r"y[n]=\frac{2\,w[n]+w[n-1]}{\sqrt5}", SENAL, ancho=5.6, alto=1.3, escala=0.8).move_to([-3.0, 2.2, 0])
        c2 = caja_tex(r"y[n]=\frac{w[n]+2\,w[n-1]}{\sqrt5}", AMBAR, ancho=5.6, alto=1.3, escala=0.8).move_to([-3.0, 0.2, 0])
        t5 = etiqueta("÷ √5", AMBAR, 0.6).move_to([0.4, 3.1, 0])
        vuelta = DoubleArrow([-0.4, 1.9, 0], [-0.4, 0.5, 0], color=CIAN, stroke_width=4, buff=0,
                             max_tip_length_to_length_ratio=0.2)
        t_21 = etiqueta("(2, 1) ⇄ (1, 2)", CIAN, 0.5).move_to([1.3, 1.2, 0])
        t_pot = etiqueta("potencia", INK, 0.6).move_to([3.0, 3.3, 0])
        p1 = formula(r"\frac{4+1}{5}", "=", "1", escala=0.8).move_to([3.0, 2.2, 0])
        p2 = formula(r"\frac{1+4}{5}", "=", "1", escala=0.8).move_to([3.0, 0.2, 0])
        t_vec = etiqueta("vecinas", INK, 0.6).move_to([5.7, 3.3, 0])
        v1 = formula(r"\frac{2\cdot1}{5}", "=", num_tex(0.4), escala=0.8).move_to([5.7, 2.2, 0])
        v2 = formula(r"\frac{1\cdot2}{5}", "=", num_tex(0.4), escala=0.8).move_to([5.7, 0.2, 0])
        E = Lienzo(ancho=4.6, alto=1.7, t_rango=(-np.pi, np.pi), v_max=2.0, centro=(-3.2, -2.5))
        ej = ejes_L(E, 0, 2.0)
        c = curva_f(E, espectro_3b(0.4), -np.pi, np.pi, AMBAR, 5)
        res = formula("1", "+", num_tex(0.8), r"\cos\Omega", escala=1.1, colores={0: AMBAR}).move_to([2.2, -2.5, 0])
        with self.narrar("b1"):
            # «rho igual a cero coma cuatro»
            self.en("rho")
            self.pop(rho)

            # «dos veces la moneda de ahora más la anterior»
            self.en("primero")
            self.play(FadeIn(c1), run_time=self.dur(1.0))

            # «entre raíz de cinco»
            self.en("raiz5")
            self.pop(t5)

            # «dale la vuelta a los coeficientes»
            self.en("vuelta")
            self.play(GrowFromCenter(vuelta), FadeIn(t_21), run_time=self.dur(0.8))

            # «una vez la de ahora más dos veces la anterior»
            self.en("segundo")
            self.play(FadeIn(c2), run_time=self.dur(1.0))

            # «Potencia»
            self.en("potencia")
            self.play(FadeIn(t_pot), run_time=0.4)

            # «uno más cuatro, entre cinco, uno»
            self.en("cuenta1")
            self.play(FadeIn(p1), FadeIn(p2), run_time=self.dur(1.0))

            # «Vecinas»
            self.en("vecinas")
            self.play(FadeIn(t_vec), run_time=0.4)

            # «uno por dos, entre cinco, cero coma cuatro»
            self.en("cuenta2")
            self.play(FadeIn(v1), FadeIn(v2), run_time=self.dur(1.0))

            # «El mismo proceso, con otro filtro»
            self.en("mismo")
            self.play(Create(ej), Create(c), run_time=self.dur(1.0))
            self.play(FadeIn(res), run_time=0.5)
        self.wait(1.0)
        self.limpiar()
