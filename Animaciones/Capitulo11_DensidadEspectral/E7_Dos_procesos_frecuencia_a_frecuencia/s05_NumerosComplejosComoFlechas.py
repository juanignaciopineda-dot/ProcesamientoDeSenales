"""Escena 05 — Un número complejo es una flecha; multiplicar por e^{-jθ} es girarla."""
from comun.escena import *


class NumerosComplejosComoFlechas(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        o = np.array([-2.8, -0.3, 0.0])
        plano = plano_c((o[0], o[1]), radio=2.0)
        z = flecha_c(o, 2.0, 40, AMBAR)
        llave = Line(o + np.array([-0.05, 0.08, 0]), z.get_end() + np.array([-0.05, 0.08, 0]),
                     color=AMBAR, stroke_width=0)
        l_mod = etiqueta("módulo", AMBAR, 0.55).move_to(o + np.array([-0.35, 1.45, 0]))
        arco = Arc(radius=0.8, start_angle=0, angle=np.deg2rad(40), color=CIAN, stroke_width=4).move_arc_center_to(o)
        l_ang = etiqueta("ángulo", CIAN, 0.55).move_to(o + np.array([2.85, 0.3, 0]))
        F = oculta(formula(r"\times", r"e^{-j\theta}", escala=1.3, colores={1: AMBAR}).move_to([3.7, 2.4, 0]))
        l1 = etiqueta("módulo = largo", AMBAR, 0.55).move_to([3.9, 0.6, 0])
        l2 = etiqueta("ángulo = giro", CIAN, 0.55).move_to([3.9, -0.3, 0])
        with self.narrar("b1"):
            # «una flecha en el plano»
            self.en("flecha")
            self.corte()
            self.play(Create(plano), GrowArrow(z), run_time=self.dur(1.0))

            # «un largo, que se llama módulo»
            self.en("modulo")
            self.pop(l_mod)

            # «y un ángulo»
            self.en("angulo")
            self.play(Create(arco), FadeIn(l_ang), run_time=self.dur(0.6))

            # «multiplicar por e elevado a menos jota por un ángulo»
            self.en("exp")
            self.add(F)
            self.play(*revelar(F[0], F[1]), run_time=self.dur(0.9))

            # «es girar la flecha ese ángulo»
            self.en("gira")
            self.play(Rotate(z, -np.deg2rad(75), about_point=o), run_time=self.dur(1.2))

            # «sin cambiar su largo»
            self.en("largo")
            self.play(plano.circ.animate.set_stroke(AMBAR, opacity=1.0), run_time=self.dur(0.7))

            # «la forma más cómoda de pensar en ellos»
            self.en("comoda")
            self.pop(l1)
            self.pop(l2)

        self.wait(1.0)
        self.limpiar()
