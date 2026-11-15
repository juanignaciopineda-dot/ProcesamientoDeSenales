"""Escena 08 — La distancia entre señales, en desvíos del ruido; y la pregunta de X."""
from comun.escena import *

SIG = 0.95                     # σ en pantalla
CY = -1.5                      # altura de los puntos


class DistanciaEnDesvios(EscenaCurso):
    ESCENA = "08"

    def construct(self):
        self.geometria()
        self.wait(0.6)
        self.equis()
        self.wait(1.0)
        self.limpiar()

    def geometria(self):
        q_old = MathTex("Q(2{,}12)=0{,}017", color=INK).scale(0.8).move_to([-5.2, 3.5, 0])
        izq = MathTex("P_e", "=", r"Q\big(", color=TXT).scale(1.3).move_to([-3.0, 2.8, 0])
        izq[0].set_color(ERROR)
        num = MathTex(r"\|s_1-s_0\|", color=TXT).scale(1.3).move_to([0.2, 3.1, 0])
        den = MathTex(r"2\sigma", color=RUIDO).scale(1.3).move_to([0.2, 2.35, 0])
        raya = Line([-1.1, 2.72, 0], [1.5, 2.72, 0], color=TXT, stroke_width=3)
        der = MathTex(r"\big)", color=TXT).scale(1.3).move_to([2.0, 2.8, 0])
        regla = VGroup(Line([-1.9, 0.9, 0], [1.9, 0.9, 0], color=INK, stroke_width=2),
                       *[Line([-1.9 + SIG * k, 0.75, 0], [-1.9 + SIG * k, 1.05, 0], color=INK, stroke_width=2)
                         for k in range(5)])
        sig_r = MathTex(r"\sigma", color=RUIDO).scale(0.8).move_to([-1.9 + SIG / 2, 1.3, 0])
        plano = Rectangle(width=9.0, height=3.5, color=INK, stroke_width=2, stroke_opacity=0.5).move_to([0, CY, 0])
        p0 = Dot([-1.9, CY, 0], radius=0.11, color=AZUL_C7)
        p1 = Dot([1.9, CY, 0], radius=0.11, color=SENAL)
        r0 = MathTex("s_0", color=AZUL_C7).scale(0.8).next_to(p0, DOWN, buff=0.15)
        r1 = MathTex("s_1", color=SENAL).scale(0.8).next_to(p1, DOWN, buff=0.15)
        n0 = Circle(radius=SIG, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.15).move_to(p0)
        n1 = Circle(radius=SIG, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.15).move_to(p1)
        medio = Dot([0, CY, 0], radius=0.09, color=AMBAR)
        front = Line([0, CY - 1.6, 0], [0, CY + 1.6, 0], color=AMBAR, stroke_width=5)
        recto = VGroup(Line([0.25, CY, 0], [0.25, CY + 0.25, 0], color=AMBAR, stroke_width=3),
                       Line([0, CY + 0.25, 0], [0.25, CY + 0.25, 0], color=AMBAR, stroke_width=3))
        mit = VGroup(MathTex("=", color=AMBAR).scale(0.8).move_to([-0.95, CY + 1.3, 0]),
                     MathTex("=", color=AMBAR).scale(0.8).move_to([0.95, CY + 1.3, 0]))
        with self.narrar("b1"):
            # «la misma cuenta de siempre»
            self.paso("misma", q_old, t=0.5)
            # «y generaliza»
            self.paso("generaliza", izq, der, t=0.6)
            # «cu de la longitud de la diferencia»
            self.paso("longitud", num, t=0.6)
            # «entre dos sigma»
            self.en("dossigma")
            self.play(FadeIn(den), Create(raya), run_time=self.dur(0.6))
            # «la distancia entre las señales»
            self.en("distancia")
            self.resaltar(num, color=AMBAR, run_time=0.6)
            # «medida en desvíos del ruido»
            self.paso("desvios", regla, sig_r, t=0.7)
            # «Geométricamente»
            self.paso("geo", plano, t=0.5)
            # «dos puntos»
            self.paso("puntos", p0, p1, r0, r1, t=0.6)
            # «una nube redonda de ruido»
            self.paso("nubes", n0, n1, t=0.7)
            # «La regla óptima»
            self.paso("optima", medio, t=0.4)
            # «una frontera perpendicular»
            self.en("frontera")
            self.play(Create(front), Create(recto), run_time=self.dur(0.7))
            # «por el punto medio»
            self.paso("medio", mit, t=0.5)
        self.corte()

    def equis(self):
        f_x = MathTex("X", "=", "s_0", r"\cdot", "s_1", color=TXT).scale(1.2).move_to([-3.6, 3.2, 0])
        f_x[0].set_color(AMBAR)
        f_x[2].set_color(AZUL_C7)
        f_x[4].set_color(SENAL)
        # dos flechas con un ángulo
        o = np.array([-5.2, -1.2, 0.0])
        a1 = flecha_c(o, 2.4, 25, SENAL, 6)
        a0 = flecha_c(o, 2.4, 80, AZUL_C7, 6)
        ang = Arc(radius=0.8, start_angle=np.deg2rad(25), angle=np.deg2rad(55), arc_center=o, color=AMBAR, stroke_width=4)
        ang2 = Arc(radius=0.8, start_angle=np.deg2rad(25), angle=np.deg2rad(90), arc_center=o, color=AMBAR, stroke_width=4)
        f_l = MathTex(r"\|s_1-s_0\|^2", "=", "2E", "-2X", color=TXT).scale(1.2).move_to([2.2, 2.0, 0])
        f_l[3].set_color(AMBAR)
        f_l[2].set_color(AMBAR)
        # plano de la derecha: dos puntos que se separan
        c = np.array([3.3, -0.9, 0.0])
        q1 = Dot(c + LEFT * 0.7, radius=0.1, color=AZUL_C7)
        q2 = Dot(c + RIGHT * 0.7, radius=0.1, color=SENAL)
        m1 = Circle(radius=0.8, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.15).move_to(q1)
        m2 = Circle(radius=0.8, color=RUIDO, stroke_width=3).set_fill(RUIDO, 0.15).move_to(q2)
        mal = MathTex("P_e", r"\ \downarrow", color=ERROR).scale(1.2).move_to([3.3, -3.0, 0])
        # recta numérica para X
        yr = -3.2
        recta = Line([-6.4, yr, 0], [-0.8, yr, 0], color=INK, stroke_width=2)
        cero = MathTex("0", color=INK).scale(0.8).move_to([-1.0, yr - 0.4, 0])
        punto = Dot([-1.6, yr, 0], radius=0.12, color=AMBAR)
        xr = MathTex("X", color=AMBAR).scale(0.9).move_to([-1.6, yr + 0.4, 0])
        hasta = Text("?", color=AMBAR, weight=BOLD).scale(1.2).move_to([-6.5, yr + 0.55, 0])
        with self.narrar("b2"):
            # «Llamemos equis»
            self.paso("equis", f_x, t=0.6)
            # «cuánto se parecen»
            self.en("parecen")
            self.play(GrowArrow(a1), GrowArrow(a0), Create(ang), run_time=self.dur(0.8))
            # «La longitud al cuadrado de la diferencia»
            self.paso("long2", f_l[0], f_l[1], t=0.6)
            # «dos veces la energía»
            self.paso("dos_e", f_l[2], t=0.5)
            # «menos dos equis»
            self.paso("menos_x", f_l[3], t=0.5)
            # «Cuanto menos se parezcan»
            self.en("menos")
            self.play(a0.animate.rotate(np.deg2rad(35), about_point=o), Transform(ang, ang2), run_time=self.dur(0.8))
            # «más lejos están los puntos»
            self.en("lejos")
            self.play(FadeIn(m1), FadeIn(m2), FadeIn(q1), FadeIn(q2), run_time=0.4)
            self.play(q1.animate.shift(LEFT * 0.9), m1.animate.shift(LEFT * 0.9),
                      q2.animate.shift(RIGHT * 0.9), m2.animate.shift(RIGHT * 0.9), run_time=self.dur(0.8))
            # «menos nos equivocamos»
            self.paso("menoserror", mal, t=0.5)
            # «hay que hacer equis lo más negativo posible»
            self.en("negativo")
            self.play(FadeIn(recta), FadeIn(cero), FadeIn(punto), FadeIn(xr), run_time=0.4)
            self.play(punto.animate.shift(LEFT * 3.2), xr.animate.shift(LEFT * 3.2), run_time=self.dur(1.0))
            # «¿Hasta dónde puede bajar?»
            self.paso("hasta", hasta, t=0.5)
