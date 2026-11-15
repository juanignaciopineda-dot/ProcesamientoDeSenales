"""Escena 09 — Contraejemplo: gaussianas en los instantes pares, uniformes en los impares; WSS pero no SSS."""
from comun.escena import *


class Contraejemplo(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.xs = [-4.9 + 1.4 * k for k in range(8)]
        self.fila_y = 1.0
        self.cuerpo1()
        self.cuerpo2()
        self.wait(1.0)
        self.limpiar()

    def cuerpo1(self):
        xs, y = self.xs, self.fila_y
        with self.narrar("b1"):
            # «Al revés no funciona»
            self.en("reves")
            f = MathTex(r"\text{WSS}", r"\Rightarrow", r"\text{SSS}", color=TXT).scale(1.1).move_to([-3.2, 3.3, 0])
            self.play(FadeIn(f), run_time=0.3)
            self.tacha = Line(f.get_corner(DL) + DL * 0.05, f.get_corner(UR) + UR * 0.05, color=ROJO, stroke_width=7)
            self.play(Create(self.tacha), run_time=0.3)
            self.formula_top = f

            # «un contraejemplo»
            self.en("contra")
            self.palabra_c = self.palabra("contraejemplo", AMBAR, 0.9).move_to([3.2, 3.3, 0])
            self.pop(self.palabra_c)

            # «muestras independientes»
            self.en("indep")
            self.bases = VGroup(*[Line([x - 0.55, y - 0.45, 0], [x + 0.55, y - 0.45, 0], color=INK, stroke_width=2) for x in xs])
            self.idx = VGroup(*[MathTex(f"X_{k}", color=INK).scale(0.6).move_to([x, y - 0.85, 0]) for k, x in enumerate(xs)])
            self.play(LaggedStart(*[FadeIn(b) for b in self.bases], lag_ratio=0.08), FadeIn(self.idx), run_time=self.dur(1.0))

            # «media cero y varianza uno»
            self.en("mu0")
            self.mv = MathTex(r"\mu = 0,\qquad \sigma^2 = 1", color=AMBAR).scale(0.85).move_to([0, -0.3, 0])
            self.pop(self.mv)

            # «los instantes pares»
            self.en("pares")
            self.campanas = VGroup(*[campana_mini((xs[k], y), 1.0, 0.9, SENAL, 3.5) for k in range(0, 8, 2)])
            self.play(LaggedStart(*[Create(c) for c in self.campanas], lag_ratio=0.2), run_time=self.dur(1.0))

            # «gaussiana»
            self.en("gauss")
            self.resaltar(*self.campanas, color=VERDE, escala=1.15)

            # «los impares»
            self.en("impares")
            self.rects = VGroup(*[rectangulo_mini((xs[k], y), 1.0, 0.9 * 0.55, AMBAR, 3.5).shift(DOWN * 0.19) for k in range(1, 8, 2)])
            self.play(LaggedStart(*[Create(c) for c in self.rects], lag_ratio=0.2), run_time=self.dur(1.0))

            # «uniforme entre menos raíz de tres y raíz de tres»
            self.en("unif")
            self.big = rectangulo_mini((-3.6, -2.2), 2.6, 1.1, AMBAR, 4.5)
            self.linea_b = Line([-5.2, -2.75, 0], [-2.0, -2.75, 0], color=INK, stroke_width=2)
            self.e1 = MathTex(r"-\sqrt{3}", color=TXT).scale(0.8).move_to([-4.9, -3.15, 0])
            self.e2 = MathTex(r"\sqrt{3}", color=TXT).scale(0.8).move_to([-2.3, -3.15, 0])
            self.play(Create(self.big), Create(self.linea_b), FadeIn(self.e1), FadeIn(self.e2), run_time=self.dur(1.0))

            # «¿Por qué ese intervalo?»
            self.en("porque")
            q = Text("¿?", color=ROJO, weight=BOLD).scale(1.0).move_to([-3.6, -1.2, 0])
            self.pop(q)

            # «la varianza de una uniforme»
            self.en("var_unif")
            self.play(FadeOut(q), run_time=0.15)
            self.vu = etiqueta("varianza de la uniforme", INK, 0.5).move_to([3.0, -1.3, 0])
            self.play(FadeIn(self.vu), run_time=0.4)

            # «el ancho al cuadrado entre doce»
            self.en("ancho")
            self.fa = MathTex(r"\frac{\text{ancho}^2}{12}", color=TXT).scale(0.95).move_to([3.0, -2.15, 0])
            self.play(FadeIn(self.fa), run_time=0.5)

            # «dos raíz de tres, al cuadrado, es doce»
            self.en("doce")
            self.fd = MathTex(r"(2\sqrt{3})^2 = 12", color=TXT).scale(0.95).move_to([3.0, -3.0, 0])
            self.play(FadeIn(self.fd), run_time=0.5)

            # «entre doce, uno»
            self.en("uno")
            self.fu = MathTex(r"\frac{12}{12} = 1", color=AMBAR).scale(0.95).move_to([5.6, -2.6, 0])
            self.pop(self.fu)
        self.play(*[FadeOut(m) for m in (self.big, self.linea_b, self.e1, self.e2, self.vu, self.fa, self.fd, self.fu)],
                  run_time=0.3)

    def cuerpo2(self):
        xs, y = self.xs, self.fila_y
        with self.narrar("b2"):
            # «La media es cero siempre»
            self.en("media0")
            cero = Line([xs[0] - 0.7, y + 0.75, 0], [xs[-1] + 0.7, y + 0.75, 0], color=AMBAR, stroke_width=4)
            self.play(Create(cero), run_time=self.dur(0.6))
            self.cero = cero

            # «vale uno en el mismo instante»
            self.en("uno_ins")
            self.pal = Palitos(range(0, 6), [1, 0, 0, 0, 0, 0], ancho=4.0, alto=1.8, v_max=1.0, centro=(-4.0, -2.2))
            self.play(FadeIn(self.pal.base), FadeIn(self.pal.eje), Create(self.pal.tallos[0]), FadeIn(self.pal.puntos[0]),
                      run_time=self.dur(0.6))

            # «cero entre instantes distintos»
            self.en("cero_dist")
            self.play(*[FadeIn(p, scale=0.5) for p in self.pal.puntos[1:]], run_time=self.dur(0.7))

            # «porque son independientes»
            self.en("porque2")
            s1 = sello("independientes", AMBAR).move_to([2.6, -1.3, 0])
            self.pop(s1)

            # «estacionario en sentido amplio»
            self.en("wss")
            s2 = sello("WSS", VERDE).move_to([2.6, -2.6, 0])
            self.pop(s2)

            # «desplaza un solo paso»
            self.en("un_paso")
            fl = CurvedArrow([xs[2], y + 1.05, 0], [xs[3], y + 1.05, 0], color=AMBAR, angle=-TAU / 6, stroke_width=4)
            self.play(Create(fl), run_time=self.dur(0.6))

            # «una campana se convierte en un rectángulo»
            self.en("convierte")
            copia = self.campanas[1].copy()
            self.add(copia)
            nuevo = self.rects[1].copy()
            self.play(Transform(copia, nuevo), copia.animate.set_color(ROJO), run_time=self.dur(1.0))

            # «en sentido estricto, no lo es»
            self.en("no_sss")
            n = MathTex(r"\text{WSS} \;\not\Rightarrow\; \text{SSS}", color=ROJO).scale(0.95).move_to([4.7, -3.6, 0])
            self.pop(n)

            # «solo mira la media y la autocorrelación»
            self.en("solo_mira")
            lp = lupa().scale(1.3).move_to([5.9, 2.55, 0])
            mr = MathTex(r"\mu \quad R_{XX}", color=TXT).scale(0.9).move_to([4.1, 2.55, 0])
            self.play(FadeIn(lp), FadeIn(mr), run_time=self.dur(0.6))

            # «la forma de la densidad»
            self.en("forma")
            self.resaltar(self.campanas[0], self.rects[0], color=AMBAR, escala=1.2)

            # «invisible»
            self.en("invisible")
            self.play(*[m.animate.set_stroke(opacity=0.12) for m in (*self.campanas, *self.rects, copia)], run_time=self.dur(0.9))
