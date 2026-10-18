"""Escena 13 — Canal cuenta: Bayes con el canal que confunde bits (0,27 / 0,34 ≈ 0,79)."""
from comun.escena import *


class CanalCuenta(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.caminos()
        self.bayes()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def caminos(self):
        a = Arbol07("Envío", [("0", SENAL), ("1", SENAL)],
                    [[("Recibo 0", MEDIDA), ("Recibo 1", MEDIDA)], [("Recibo 0", MEDIDA), ("Recibo 1", MEDIDA)]],
                    [r"0{,}7", r"0{,}3"], [[r"0{,}9", r"0{,}1"], [r"0{,}1", r"0{,}9"]],
                    centro=(-2.2, 0.0), ancho=8.0, alto=4.6, escala=0.65)
        uno = Text("Recibo un 1", color=AMBAR, weight=BOLD).scale(0.8).move_to([2.0, 3.2, 0])
        bien = a.rama(1, 1, VERDE)
        cambio = a.rama(0, 1, ERROR)
        c1 = MathTex(r"0{,}3\cdot 0{,}9", color=VERDE).scale(1.0).next_to(a.hojas[1][1], RIGHT, buff=0.35)
        r1 = MathTex(r"=0{,}27", color=VERDE).scale(1.0).next_to(c1, RIGHT, buff=0.15)
        c2 = MathTex(r"0{,}7\cdot 0{,}1", color=ERROR).scale(1.0).next_to(a.hojas[0][1], RIGHT, buff=0.35)
        r2 = MathTex(r"=0{,}07", color=ERROR).scale(1.0).next_to(c2, RIGHT, buff=0.15)
        self.arbol = a

        with self.narrar("b1"):
            # «Hay dos caminos»
            self.en("dos")
            self.play(FadeIn(a), run_time=self.dur(1.0))

            # «recibir un uno»
            self.en("recibir")
            self.play(FadeIn(uno), a.hojas[0][1][0].animate.set_stroke(AMBAR, 5),
                      a.hojas[1][1][0].animate.set_stroke(AMBAR, 5), run_time=self.dur(0.7))

            # «se envió un uno y llegó bien»
            self.en("bien")
            self.play(Create(bien), run_time=self.dur(0.7))

            # «cero coma tres por cero coma nueve»
            self.en("c1")
            self.play(FadeIn(c1), run_time=self.dur(0.6))

            # «cero coma veintisiete»
            self.en("r1")
            self.play(FadeIn(r1), run_time=self.dur(0.5))

            # «se envió un cero y el ruido lo cambió»
            self.en("cambio")
            self.play(Create(cambio), run_time=self.dur(0.7))

            # «cero coma siete por cero coma uno»
            self.en("c2")
            self.play(FadeIn(c2), run_time=self.dur(0.6))

            # «cero coma cero siete»
            self.en("r2")
            self.play(FadeIn(r2), run_time=self.dur(0.5))

    # ------------------------------------------------------------ b2
    def bayes(self):
        suma = formula(r"0{,}27", "+", r"0{,}07", "=", r"0{,}34", escala=1.8, colores={4: AMBAR}).move_to([0, 2.5, 0])
        bay = formula(r"P(\text{enviado }1\mid \text{recibido }1)", "=", r"\dfrac{0{,}27}{0{,}34}", r"\approx", r"0{,}79",
                      escala=1.4, colores={4: AMBAR}).move_to([0, 0.2, 0])
        etq = Text("Bayes", color=AMBAR, weight=BOLD).scale(1.0).move_to([0, 1.4, 0])
        ficha = moneda("").scale(1.0).move_to([-1.5, -2.2, 0])
        uno = MathTex("1", color=SENAL).scale(2.4).move_to([0, -2.2, 0])
        dec = Text("Decisión: 1", color=AMBAR, weight=BOLD).scale(0.9).move_to([3.4, -2.2, 0])
        ojo_ = ojo().scale_to_fit_height(0.8).move_to([-4.3, -2.2, 0])
        sig = Text("Para detectar señales", color=AMBAR, weight=BOLD).scale(0.85).move_to([2.8, -3.4, 0])

        with self.narrar("b2"):
            # «de recibir un uno es la suma»
            self.en("suma")
            self.corte()
            self.play(FadeIn(suma[0]), FadeIn(suma[1]), FadeIn(suma[2]), run_time=self.dur(0.7))

            # «cero coma treinta y cuatro»
            self.en("c34")
            self.play(FadeIn(suma[3]), FadeIn(suma[4]), run_time=self.dur(0.5))

            # «Y Bayes dice»
            self.en("bayes")
            self.pop(etq)
            self.play(FadeIn(bay[0]), FadeIn(bay[1]), run_time=self.dur(0.8))

            # «cero coma veintisiete entre cero coma treinta y cuatro»
            self.en("cociente")
            self.play(FadeIn(bay[2]), run_time=self.dur(0.7))

            # «casi un ochenta por ciento»
            self.en("ochenta")
            self.play(FadeIn(bay[3]), FadeIn(bay[4]), run_time=self.dur(0.5))
            self.sfx("exito")

            # «si tuvieras que apostar»
            self.en("apostar")
            self.play(FadeIn(uno), FadeIn(ficha, shift=DOWN * 0.3), run_time=self.dur(0.5))
            self.play(ficha.animate.next_to(uno, LEFT, buff=0.3), run_time=self.dur(0.4))

            # «Elegir la explicación más probable»
            self.en("elegir")
            self.pop(dec)

            # «después de mirar»
            self.en("mirar")
            self.play(FadeIn(ojo_, scale=0.6), run_time=self.dur(0.4))

            # «lo que haremos»
            self.en("haremos")
            self.play(GrowArrow(Arrow([-3.4, -2.2, 0], [-0.9, -2.2, 0], color=INK, stroke_width=4, buff=0.0)),
                      run_time=self.dur(0.5))

            # «para detectar señales»
            self.en("detectar")
            self.pop(sig)
