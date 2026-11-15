"""Escena 09 — Las regiones de decisión y el error con dos mediciones (3/16)."""
from comun.escena import *


def cubo(centro, lado: float, color) -> VGroup:
    """Cubo en perspectiva oblicua: cara de delante, cara de detrás y cuatro aristas."""
    d = 0.45 * lado
    cx, cy = centro
    h = lado / 2
    delante = Square(side_length=lado, color=color, stroke_width=3, fill_color=color, fill_opacity=0.12).move_to(
        [cx - d / 2, cy - d / 2, 0])
    atras = Square(side_length=lado, color=color, stroke_width=3).move_to([cx + d / 2, cy + d / 2, 0])
    aristas = VGroup(*[Line(delante.get_corner(c), atras.get_corner(c), color=color, stroke_width=3)
                       for c in (UL, UR, DL, DR)])
    return VGroup(atras, aristas, delante)


class RegionesYError(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.P = Plano2(centro=(-3.0, -0.3), u=1.7)
        self.regiones()
        self.error()
        self.comparacion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def regiones(self):
        P = self.P
        R = RectaR(centro=(0.0, -0.2), ancho=9.5, x_rango=(-1.5, 1.5))
        tramo = Line(R.p(-1), R.p(1), color=RUIDO, stroke_width=12)
        lab_r = MathTex(r"\text{decido }H_0", color=RUIDO).scale(1.2).move_to(R.p(0) + DOWN * 0.8)
        lab1 = Text("hay señal", color=SENAL, weight=BOLD).scale(0.75).move_to(P.p(-1.0, -1.75))
        lab0 = Text("solo ruido", color=INK, weight=BOLD).scale(0.75).move_to(P.p(1.0, -1.75))
        eje3 = Arrow(P.p(0, 0), P.p(0, 0) + np.array([2.0, 1.6, 0]), buff=0, color=INK, stroke_width=3,
                     tip_length=0.2, max_tip_length_to_length_ratio=0.15)
        r3 = MathTex("r_3", color=INK).scale(0.9).next_to(eje3.get_end(), UR, buff=0.05)
        c_grande = cubo((4.4, -0.8), 2.8, RUIDO)
        c_peq = cubo((4.4, -0.8), 1.4, SENAL)
        c_peq.shift(LEFT * 0.0)
        F = formula("p_1", r"f(\mathbf{r}\mid H_1)", r"\gtrless", "p_0", r"f(\mathbf{r}\mid H_0)", escala=1.1,
                    colores={0: SENAL, 1: SENAL, 3: RUIDO, 4: RUIDO}).move_to([3.8, 3.1, 0])
        self.F = F

        with self.narrar("b1"):
            # «tramos de una recta»
            self.en("recta")
            self.corte()
            self.play(FadeIn(R), Create(tramo), FadeIn(lab_r), run_time=self.dur(0.7))

            # «regiones de un plano»
            self.en("plano")
            self.play(FadeOut(R), FadeOut(tramo), FadeOut(lab_r), run_time=0.25)
            P.grande.set_fill(INK, 0.3).set_stroke(INK, 3)
            P.pequeno.set_fill(SENAL, 0.8)
            self.play(FadeIn(P.ejes), FadeIn(P.rot1), FadeIn(P.rot2), FadeIn(P.grande), FadeIn(P.pequeno),
                      run_time=self.dur(0.7))

            # «hay señal»
            self.en("haysenal")
            self.pop(lab1)

            # «solo ruido»
            self.en("solo")
            self.pop(lab0)

            # «tres mediciones»
            self.en("tres")
            self.play(Create(eje3), FadeIn(r3), run_time=self.dur(0.6))

            # «tres dimensiones»
            self.en("tresd")
            self.play(FadeIn(c_grande), run_time=self.dur(0.5))
            self.play(FadeIn(c_peq), run_time=self.dur(0.5))

            # «La regla no cambia»
            self.en("nocambia")
            self.play(*[FadeIn(F[i], shift=UP * 0.1) for i in range(5)], run_time=self.dur(1.2))

            # «dónde vive la medición»
            self.en("vive")
            self.play(F[1].animate(rate_func=there_and_back).set_color(AMBAR).scale(1.15),
                      F[4].animate(rate_func=there_and_back).set_color(AMBAR).scale(1.15),
                      run_time=self.dur(0.8))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def error(self):
        P = self.P
        pregunta = MathTex(r"P_e=\,?", color=ROJO).scale(1.7).move_to([4.3, 3.0, 0])
        # nube azul: cuatro puntos dentro del cuadrado pequeño
        azules = VGroup(*[Dot(P.p(x, y), radius=0.11, color=MEDIDA)
                          for x, y in [(-0.3, -0.25), (0.25, 0.3), (0.3, -0.2), (-0.2, 0.35), (0.0, 0.0)]])
        # nube magenta: rejilla de 16 puntos; cuatro caen dentro del pequeño
        pts = [(-0.75, -0.75), (-0.25, -0.75), (0.25, -0.75), (0.75, -0.75),
               (-0.75, -0.25), (-0.25, -0.25), (0.25, -0.25), (0.75, -0.25),
               (-0.75, 0.25), (-0.25, 0.25), (0.25, 0.25), (0.75, 0.25),
               (-0.75, 0.75), (-0.25, 0.75), (0.25, 0.75), (0.75, 0.75)]
        magentas = VGroup(*[Dot(P.p(x + 0.06, y - 0.05), radius=0.11, color=RUIDO) for x, y in pts])
        dentro = [i for i, (x, y) in enumerate(pts) if abs(x) < 0.5 and abs(y) < 0.5]
        cero_txt = Text("0 errores", color=VERDE, weight=BOLD).scale(1.0).move_to([4.6, 1.9, 0])
        tl = tilde(VERDE, 0.7).next_to(cero_txt, LEFT, buff=0.25)
        cuatro = casillas(4, rojas=(), centro=(4.3, 0.7), lado=0.65)
        for c in cuatro.cas[:3]:
            c.set_color(RUIDO).set_fill(RUIDO, 0.6)
        uno4 = MathTex(r"\tfrac14\ \text{de los puntos}", color=ROJO).scale(1.1).move_to([4.3, -0.5, 0])
        cuentas = MathTex(r"\tfrac34\cdot\tfrac14+\tfrac14\cdot 0", color=TXT).scale(1.15).move_to([4.3, -1.6, 0])
        res = MathTex(r"=\tfrac{3}{16}", color=ROJO).scale(1.9).move_to([4.3, -2.9, 0])
        self.res_pos = res

        with self.narrar("b2"):
            # «¿Cuánto nos equivocamos ahora?»
            self.en("cuanto")
            self.corte()
            self.add(P.ejes, P.rot1, P.rot2, P.grande, P.pequeno)
            self.play(FadeIn(pregunta), run_time=self.dur(0.4))

            # «Si es hache uno»
            self.en("esh1")
            self.play(FadeIn(azules, lag_ratio=0.2), run_time=self.dur(0.8))

            # «así que acertamos»
            self.en("acertamos")
            self.play(FadeIn(tl, scale=0.5), run_time=self.dur(0.4))

            # «cero errores»
            self.en("cero")
            self.pop(cero_txt)

            # «Si es hache cero»
            self.en("esh0")
            self.play(FadeOut(azules), FadeIn(magentas, lag_ratio=0.05), run_time=self.dur(0.9))

            # «tres de cada cuatro veces»
            self.en("tres4")
            self.play(FadeIn(cuatro), run_time=self.dur(0.5))

            # «nos equivocamos cuando el par cae»
            self.en("cae")
            self.play(*[magentas[i].animate.set_color(ROJO).scale(1.5) for i in dentro], run_time=self.dur(0.6))

            # «una de cada cuatro»
            self.en("uno4")
            self.play(FadeIn(uno4), run_time=self.dur(0.5))

            # «Tres cuartos por un cuarto»
            self.en("cuentas")
            self.play(FadeIn(cuentas, shift=UP * 0.1), run_time=self.dur(0.8))

            # «tres dieciseisavos»
            self.en("d3")
            self.pop(res)
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def comparacion(self):
        dec = MathTex(r"\tfrac{3}{16}=0{,}1875", color=ROJO).scale(1.8).move_to([0, 3.0, 0])
        menos = MathTex(r"0{,}1875<0{,}25", color=ROJO).scale(1.8).move_to([0, 3.0, 0])
        l1 = Text("con una medición", color=INK).scale(0.8).move_to([-4.9, 0.8, 0])
        l2 = Text("con dos", color=INK).scale(0.8).move_to([-4.9, -0.4, 0])
        b1 = barra_h(0.25, 0.8, -2.0, 16.0, alto=0.6)
        b2 = barra_h(0.1875, -0.4, -2.0, 16.0, alto=0.6)
        t1 = MathTex("0{,}25", color=ROJO).scale(1.0).next_to(b1, RIGHT, buff=0.2)
        t2 = MathTex("0{,}1875", color=ROJO).scale(1.0).next_to(b2, RIGHT, buff=0.2)
        ok = tilde(VERDE, 1.2).move_to([5.6, 0.2, 0])
        interrog = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to([-2.4, -2.3, 0])
        prom = MathTex(r"\frac{r_1+r_2}{2}", color=AMBAR).scale(1.9).move_to([1.6, -2.4, 0])

        with self.narrar("b3"):
            # «cero coma uno ocho siete cinco»
            self.en("decimal")
            self.corte()
            self.play(FadeIn(dec), run_time=self.dur(0.5))

            # «menos que un cuarto»
            self.en("menos")
            self.play(FadeOut(dec), FadeIn(menos), run_time=self.dur(0.5))

            # «Con una medición»
            self.en("con1")
            self.play(FadeIn(l1), GrowFromEdge(b1, LEFT), FadeIn(t1), run_time=self.dur(0.8))

            # «con dos»
            self.en("con2")
            self.play(FadeIn(l2), GrowFromEdge(b2, LEFT), FadeIn(t2), run_time=self.dur(0.8))

            # «Más datos, mejor decisión»
            self.en("mejor")
            self.pop(ok)

            # «la pregunta obvia»
            self.en("obvia")
            self.pop(interrog)

            # «¿no bastaría con promediarlas?»
            self.en("promediarlas")
            self.play(FadeIn(prom, shift=LEFT * 0.3), run_time=self.dur(0.7))
        self.wait(0.3)
