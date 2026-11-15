"""Escena 03 — Todo el registro: pasado y futuro, infinitos coeficientes y ortogonalidad para todo m."""
from comun.escena import *


class TodoElRegistro(EscenaCurso):
    ESCENA = "03"
    N = 90          # muestras del registro
    N0 = 45         # la muestra «ahora»

    def construct(self):
        y, v, x = registro_e3(self.N)
        self.L = L = Lienzo(ancho=11.0, alto=2.2, t_rango=(0, self.N - 1), v_max=8.0, centro=(0.0, 2.3))
        self.curva = L.curva(np.arange(self.N), x, MEDIDA, 3.0)
        self.parte_b1(L, x)
        self.parte_b2(L)
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self, L, x):
        marco = Rectangle(width=11.2, height=2.5, color=AMBAR, stroke_width=3).move_to(L.p(self.N0, 0))
        xn = L.x(self.N0)
        pas = Rectangle(width=xn - L.x(0), height=2.5, color=MEDIDA, stroke_width=0).set_fill(MEDIDA, 0.2)
        pas.move_to([(xn + L.x(0)) / 2, L.cy, 0])
        fut = Rectangle(width=L.x(self.N - 1) - xn, height=2.5, color=MEDIDA, stroke_width=0).set_fill(MEDIDA, 0.2)
        fut.move_to([(xn + L.x(self.N - 1)) / 2, L.cy, 0])
        punto = Dot(L.p(self.N0, x[self.N0]), radius=0.1, color=AMBAR)
        rot = MathTex("x[n]", color=AMBAR).scale(0.9).move_to([xn, 3.8, 0])
        f = formula(r"\hat y[n]", "=", r"\sum", "h[j]", "x[n-j]", escala=1.4,
                    colores={0: ESTIMACION}).move_to([0, 0.3, 0])
        lim_a = MathTex(r"j=-\infty", color=INK).scale(0.6).next_to(f[2], DOWN, buff=0.04)
        lim_b = MathTex(r"\infty", color=INK).scale(0.6).next_to(f[2], UP, buff=0.04)
        mat = VGroup(*[Square(side_length=0.4, color=INK, stroke_width=2).set_fill(INK, 0.1)
                       for _ in range(25)]).arrange_in_grid(5, 5, buff=0).move_to([-4.0, -2.3, 0])
        cruz_m = VGroup(Line(mat.get_corner(UL) * 2.0 - mat.get_center(), mat.get_corner(DR) * 2.0 - mat.get_center(),
                             color=ROJO, stroke_width=7),
                        Line(mat.get_corner(UR) * 2.0 - mat.get_center(), mat.get_corner(DL) * 2.0 - mat.get_center(),
                             color=ROJO, stroke_width=7))
        txt = Text("no hay matriz que invertir", color=ROJO).scale(0.7).move_to([3.2, -2.3, 0])
        self.b1 = VGroup(f, lim_a, lim_b, mat, cruz_m, txt)
        self.marco, self.pas, self.fut, self.punto, self.rot = marco, pas, fut, punto, rot
        with self.narrar("b1"):
            self.en("grab")                                  # «la grabación ya está hecha»
            self.play(Create(self.curva), run_time=self.dur(1.2))
            self.en("todo")                                  # «todo el registro»
            self.play(GrowFromCenter(marco), run_time=self.dur(0.8))
            self.en("pasado")                                # «el pasado»
            self.play(FadeIn(pas), run_time=0.4)
            self.en("presente")                              # «el presente»
            self.play(FadeIn(punto, scale=2), FadeIn(rot), run_time=0.4)
            self.en("futuro")                                # «lo que vendrá después»
            self.play(FadeIn(fut), run_time=0.4)
            self.en("suma")                                  # «una suma con infinitos coeficientes»
            self.play(FadeIn(f[0:3]), run_time=0.6)
            self.play(FadeIn(f[3:5]), run_time=0.5)
            self.en("limites")                               # «de menos infinito a infinito»
            self.play(FadeIn(lim_a), FadeIn(lim_b), run_time=0.5)
            self.en("termino")                               # «hache de jota por equis de ene menos jota»
            self.play(f[3].animate.set_color(AMBAR), f[4].animate.set_color(MEDIDA), run_time=0.5)
            self.en("matriz")                                # «ninguna matriz finita»
            self.play(FadeIn(mat), run_time=0.4)
            self.play(mat.animate.scale(2.0), run_time=self.dur(1.2))
            self.en("tacha")                                 # «que valga»
            self.play(Create(cruz_m), FadeIn(txt), run_time=0.5)

    def parte_b2(self, L):
        # el error es perpendicular a cada muestra
        f = formula("e", r"\perp", "x[n-m]", escala=1.2, colores={0: ERROR, 2: MEDIDA}).move_to([-1.2, 0.5, 0])
        o = np.array([-6.2, -0.15, 0.0])
        fx = Arrow(o, o + RIGHT * 1.4, buff=0, color=MEDIDA, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        fe = Arrow(o, o + UP * 1.0, buff=0, color=ERROR, stroke_width=6, max_tip_length_to_length_ratio=0.2)
        xs = np.linspace(-5.0, 5.0, 21)
        marcas = [Line([a, 1.2, 0], [a, 1.5, 0], color=ERROR, stroke_width=4) for a in xs]
        centro = VGroup(*marcas[7:14])
        lados_ = [marcas[:7][::-1], marcas[14:]]
        resto = [m for par in zip(marcas[6::-1], marcas[14:]) for m in par]
        para = Text("para todo m", color=AMBAR, weight=BOLD).scale(0.75).move_to([3.0, 0.5, 0])
        fl_i = flecha([-0.3, 1.0, 0], [-5.4, 1.0, 0], AMBAR, 3)
        fl_d = flecha([0.3, 1.0, 0], [5.4, 1.0, 0], AMBAR, 3)
        previo = MathTex(r"E\big[(y-\hat y)\,x[n-m]\big]=0", color=INK).scale(0.9).move_to([0, -0.55, 0])
        g = formula(r"\sum_j h[j]", "C_{xx}[m-j]", "=", "C_{yx}[m]", escala=1.1,
                    colores={1: MEDIDA}).move_to([0, -1.7, 0])
        A = Tallos([1, 2, 1], centro=(-2.4, -3.45), paso=0.5, unidad=0.3, color=AMBAR)
        B = Tallos([1, 3, 2, 1], centro=(2.4, -3.45), paso=0.5, unidad=0.3, color=MEDIDA)
        h = formula("h", r"\ast", "C_{xx}", "=", "C_{yx}", escala=1.4, colores={2: MEDIDA}).move_to([0, -1.7, 0])
        with self.narrar("b2"):
            self.en("perp")                                  # «el error, perpendicular»
            self.play(FadeOut(self.b1), FadeIn(f), Create(fx), Create(fe), run_time=0.7)
            self.en("cada")                                  # «cada muestra que usamos»
            self.play(LaggedStart(*[Create(m) for m in centro], lag_ratio=0.15), run_time=self.dur(1.2))
            self.en("todas")                                 # «Y ahora usamos todas»
            self.play(LaggedStart(*[Create(m) for m in resto], lag_ratio=0.08), run_time=self.dur(1.6))
            self.en("todom")                                 # «para todo eme entero»
            self.pop(para)
            self.en("lados")                                 # «hacia los dos lados»
            self.play(Create(fl_i), Create(fl_d), run_time=0.6)
            self.en("desarrollo")                            # «el mismo desarrollo de antes»
            self.play(FadeIn(previo), run_time=0.5)
            self.en("sumah")                                 # «la suma de hache de jota»
            self.play(FadeIn(g[0]), run_time=0.5)
            self.en("autoc")                                 # «por la autocorrelación en eme menos jota»
            self.play(FadeIn(g[1]), run_time=0.5)
            self.en("cruz")                                  # «es la correlación cruzada en eme»
            self.play(FadeIn(g[2]), FadeIn(g[3]), run_time=0.5)
            self.en("conv")                                  # «una convolución»
            self.play(FadeIn(A), FadeIn(B), run_time=0.4)
            self.play(A.animate.shift(RIGHT * 4.8), run_time=self.dur(1.6, 0.3))
            self.en("hconv")                                 # «hache convolucionado con la autocorrelación de equis»
            self.play(FadeOut(g), FadeOut(A), FadeOut(B), FadeOut(previo), run_time=0.3)
            self.play(FadeIn(h[0:3]), run_time=0.5)
            self.en("igual")                                 # «es la correlación cruzada»
            self.play(FadeIn(h[3:5]), run_time=0.4)
            self.resaltar(para, color=AMBAR)
