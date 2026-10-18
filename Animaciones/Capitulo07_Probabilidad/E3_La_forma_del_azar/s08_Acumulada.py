"""Escena 08 — La función de distribución acumulada: definición, continua, mixta y dos propiedades."""
from comun.escena import *


class Acumulada(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.bloque1()
        self.corte()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    def escalera(self):
        A = AcumDado(centro=(0.5, -0.6))
        A.add(A.peldanos, A.llenos, A.huecos)
        return A

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        A = self.escalera()
        with self.narrar("b1"):
            self.play(FadeIn(A), run_time=0.7)
            self.en("nombre")                                 # «función de distribución acumulada»
            nombre = Text("Función de distribución acumulada", color=AMBAR, weight=BOLD).scale(0.7)
            nombre.move_to([0, 3.5, 0])
            self.play(Write(nombre), run_time=self.dur(1.4))
            self.en("formula")                                # «efe mayúscula sub equis de equis»
            f = formula("F_X", "(", "x", ")", "=", "P", "(", "X", r"\le", "x", ")", escala=1.15,
                        colores={0: AMBAR, 5: AMBAR})
            f.move_to([0, 2.55, 0])
            self.play(LaggedStart(*[Write(p) for p in f], lag_ratio=0.2), run_time=self.dur(1.5))
            self.en("prob_que")                               # «la probabilidad de que la variable»
            self.play(f[5].animate(rate_func=there_and_back).scale(1.6), run_time=self.dur(0.6))
            self.en("no_pase")                                # «no pase de equis»
            cur = A.cursor(2.5)
            self.play(Create(cur), run_time=self.dur(0.3))
            self.play(cur.animate.set_x(float(A.p(4.7, 0)[0])), run_time=self.dur(1.2))
            self.play(FadeOut(cur), run_time=0.25)
            self.en("continua")                               # «una variable continua»
            self.clear()
            c = Curva(lambda x: float(cdf_normal(x)), x_rango=(-4, 4), y_max=1.0, ancho=8.0, alto=3.6,
                      x_label="x", y_label="F_X(x)").move_to([0, -0.6, 0])
            self.add(c.ejes, c.etiquetas)
            self.add(nombre, f)
            self.play(FadeIn(c.ejes), run_time=self.dur(0.4))
            self.en("suave")                                  # «sube suave de cero a uno»
            self.play(Create(c.grafica), run_time=self.dur(1.6))
            self.en("mezcla")                                 # «una mezcla»
            ax = c.ejes

            def g(x):
                return 0.55 * float(cdf_normal(x, -0.4, 0.9)) + (0.45 if x >= 1.2 else 0.0)

            s1 = ax.plot(g, x_range=[-4, 1.19, 0.02], color=SENAL, stroke_width=4)
            s2 = ax.plot(g, x_range=[1.2, 4, 0.02], color=SENAL, stroke_width=4)
            salto = DashedLine(ax.c2p(1.2, g(1.19)), ax.c2p(1.2, g(1.2)), color=ERROR, stroke_width=4)
            self.play(FadeOut(c.grafica), Create(s1), Create(s2), run_time=self.dur(1.2))
            self.en("sensor")                                 # «un sensor que a veces se satura»
            sen = caja("Sensor", MEDIDA, ancho=1.9, alto=0.7, scale=0.5).move_to([5.4, 2.2, 0])
            luz = Dot(sen.get_right() + RIGHT * 0.3, radius=0.14, color=ROJO)
            self.play(FadeIn(sen), FadeIn(luz, scale=2), run_time=self.dur(0.6))
            self.en("mismo_valor")                            # «siempre el mismo valor»
            self.play(Create(salto), run_time=self.dur(0.5))
            self.play(Flash(salto, color=ERROR, flash_radius=0.35), run_time=0.5)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        A = self.escalera()
        dos = VGroup(*[Text(f"{i}", color=AMBAR, weight=BOLD).scale(0.8) for i in (1, 2)])
        with self.narrar("b2"):
            self.play(FadeIn(A), run_time=0.5)
            self.en("dos_cosas")                              # «dos cosas que se cumplen siempre»
            dos[0].move_to([-5.2, 3.1, 0])
            dos[1].move_to([1.0, 3.1, 0])
            self.pop(dos[0])
            self.en("nunca_baja")                             # «nunca baja»
            fl = Arrow(A.p(1.2, 0.5), A.p(5.4, 1.12), color=VERDE, stroke_width=5, buff=0)
            self.play(Create(fl), run_time=self.dur(0.8))
            self.en("tres")                                   # «no pasa de tres»
            self.play(FadeOut(fl), run_time=0.25)
            cur3 = A.cursor(3.0, VERDE)
            h3 = DashedLine(A.p(3, 0.5), A.p(0, 0.5), color=VERDE, stroke_width=3)
            self.play(Create(cur3), Create(h3), run_time=self.dur(0.6))
            self.en("cuatro")                                 # «tampoco pasa de cuatro»
            cur4 = A.cursor(4.0, AMBAR)
            h4 = DashedLine(A.p(4, 4 / 6), A.p(0, 4 / 6), color=AMBAR, stroke_width=3)
            self.play(Create(cur4), Create(h4), run_time=self.dur(0.6))
            self.en("segunda")                                # «la segunda probabilidad»
            self.play(h4.animate.set_stroke(width=7), run_time=self.dur(0.5))
            self.en("primera")                                # «por lo menos la primera»
            ge = formula("F(4)", r"\ge", "F(3)", escala=1.0, colores={0: AMBAR, 2: VERDE}).move_to([4.2, 3.0, 0])
            self.play(h3.animate.set_stroke(width=7), Write(ge), run_time=self.dur(0.9))
            self.en("cero_izq")                               # «empieza en cero»
            self.play(FadeOut(VGroup(cur3, cur4, h3, h4, ge)), run_time=0.3)
            anillo0 = Circle(radius=0.3, color=CIAN, stroke_width=4).move_to(A.p(0.4, 0))
            cero = formula("0", escala=1.0, colores={0: CIAN}).next_to(anillo0, UP, buff=0.3)
            self.play(Create(anillo0), FadeIn(cero), run_time=self.dur(0.6))
            self.en("uno_der")                                # «termina en uno»
            l1 = DashedLine(A.p(0, 1), A.p(8, 1), color=VERDE, stroke_width=3)
            anillo1 = Circle(radius=0.3, color=VERDE, stroke_width=4).move_to(A.p(7.4, 1))
            self.play(Create(l1), Create(anillo1), run_time=self.dur(0.7))
            self.en("todo")                                   # «muy a la derecha está todo»
            t = Text("Toda la probabilidad", color=VERDE, weight=BOLD).scale(0.5).next_to(anillo1, UP, buff=0.15)
            t.shift(LEFT * 1.0)
            self.play(FadeIn(t, shift=UP * 0.1), run_time=self.dur(0.5))
