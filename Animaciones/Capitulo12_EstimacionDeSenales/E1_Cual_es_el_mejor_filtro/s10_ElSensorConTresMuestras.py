"""Escena 10 — El sensor con tres muestras: la matriz, el vector, los coeficientes y el error."""
from comun.escena import *


class ElSensorConTresMuestras(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.resolver()
        self.el_error()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resolver(self):
        t, y, v, x = sensor12(40)
        termo = termometro(1.3, ROJO, 0.6).move_to([-6.0, 2.6, 0])
        L = Lienzo(ancho=4.0, alto=1.2, t_rango=(0, 39), v_max=7, centro=(-3.3, 2.6))
        curva = L.curva(t, x, MEDIDA, 2.8)
        circs = VGroup(*[Circle(radius=0.13, color=AMBAR, stroke_width=3).move_to(L.p(k, x[k])) for k in (24, 25, 26)])
        M = MatrizT([["5", "2,4", "1,44"], ["2,4", "5", "2,4"], ["1,44", "2,4", "5"]],
                    centro=(-3.6, -0.5), lado=1.5, escala=0.7)
        cxx = MathTex(r"C_{xx}", color=MEDIDA).scale(0.9).move_to([-3.6, 1.8, 0])
        uno = MathTex("5", "=", "4", "+", "1", color=TXT).scale(0.9).move_to([0.1, 1.8, 0])
        uno[2].set_color(SENAL)
        uno[4].set_color(RUIDO)
        cyx = MathTex(r"C_{yx}", color=SENAL).scale(0.9).move_to([2.3, 1.8, 0])
        vec = VGroup(*[Text(s, color=SENAL).scale(0.7).move_to([2.3, -0.5 - (i - 1) * 1.2, 0])
                       for i, s in enumerate(["4", "2,4", "1,44"])])
        hcol = VGroup(*[MathTex(f"h_{i}", color=ESTIMACION).scale(0.9).move_to([-0.3, -0.5 - (i - 1) * 1.2, 0])
                        for i in range(3)])
        igual = MathTex("=", color=TXT).scale(1.1).move_to([1.0, -0.5, 0])
        tl = Tallos([0.739, 0.116, 0.020], centro=(5.1, -1.6), paso=1.4, unidad=2.6, color=ESTIMACION)
        etq = [MathTex(s, color=MEDIDA).scale(0.75).move_to([tl.x(i), -2.2, 0])
               for i, s in enumerate(["x[n]", "x[n-1]", "x[n-2]"])]
        nums = [Text(s, color=ESTIMACION).scale(0.62).move_to([tl.x(i), -1.6 + tl.valores[i] * 2.6 + 0.35, 0])
                for i, s in enumerate(["0,739", "0,116", "0,020"])]
        cols = [AMBAR, CIAN, VERDE]
        self._barras = (tl, etq, nums)

        with self.narrar("b1"):
            # «Con el sensor»
            self.en("sensor")
            self.play(FadeIn(termo), Create(curva), run_time=self.dur(0.6))

            # «tres muestras»
            self.en("tres")
            self.play(Create(circs), run_time=self.dur(0.4))

            # «La autocorrelación de lo medido»
            self.en("auto")
            self.play(FadeIn(M.corchetes), FadeIn(cxx), run_time=self.dur(0.6))

            # «cinco en cero»
            self.en("c5")
            d0 = M.diag(0).set_color(cols[0])
            self.play(FadeIn(d0), run_time=self.dur(0.4))

            # «dos coma cuatro a un paso»
            self.en("c24")
            d1 = M.diag(1).set_color(cols[1])
            self.play(FadeIn(d1), run_time=self.dur(0.4))

            # «uno coma cuatro cuatro a dos»
            self.en("c144")
            d2 = M.diag(2).set_color(cols[2])
            self.play(FadeIn(d2), run_time=self.dur(0.4))

            # «más el uno del ruido en el cero»
            self.en("uno")
            self.play(FadeIn(uno, shift=DOWN * 0.1), run_time=self.dur(0.6))

            # «La correlación cruzada es solo la de la temperatura»
            self.en("cruz")
            self.play(FadeIn(cyx), run_time=self.dur(0.5))

            # «cuatro, dos coma cuatro, uno coma cuatro cuatro»
            self.en("vec")
            self.play(LaggedStart(*[FadeIn(m) for m in vec], lag_ratio=0.3), run_time=self.dur(1.0))

            # «Resolvemos»
            self.en("resolver")
            self.play(FadeIn(hcol), FadeIn(igual), run_time=self.dur(0.6))

            # «cero coma siete tres nueve»
            self.en("h0")
            self.play(Create(tl.base), Create(tl.tallos[0]), FadeIn(tl.puntos[0]), FadeIn(etq[0]),
                      FadeIn(nums[0]), run_time=self.dur(0.5))

            # «cero coma uno uno seis»
            self.en("h1")
            self.play(Create(tl.tallos[1]), FadeIn(tl.puntos[1]), FadeIn(etq[1]), FadeIn(nums[1]),
                      run_time=self.dur(0.5))

            # «cero coma cero dos cero»
            self.en("h2")
            self.play(Create(tl.tallos[2]), FadeIn(tl.puntos[2]), FadeIn(etq[2]), FadeIn(nums[2]),
                      run_time=self.dur(0.5))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def el_error(self):
        tl, etq, nums = self._barras
        err = self.palabra("error", ERROR, 0.9).move_to([0, 3.3, 0])
        resta = formula(r"\sigma_y^2", "-", r"\text{lo que explica el filtro}", escala=1.0).move_to([0, 2.3, 0])
        base_y = -3.0
        esc = 0.7

        def barra(valor, cx, color):
            r = Rectangle(width=1.4, height=valor * esc, stroke_width=0).set_fill(color, 0.85)
            r.move_to([cx, base_y + valor * esc / 2, 0])
            return r

        b3 = barra(0.74, 3.0, ERROR)
        b1 = barra(0.8, 0.0, ERROR)
        b0 = barra(4.0, -3.0, ERROR)
        v3 = MathTex("0{,}74", color=ERROR).scale(1.3).move_to([3.0, base_y + 0.74 * esc + 0.5, 0])
        v1 = MathTex("0{,}8", color=ERROR).scale(1.0).move_to([0.0, base_y + 0.8 * esc + 0.45, 0])
        v0 = MathTex("4", color=ERROR).scale(1.0).move_to([-3.0, base_y + 4.0 * esc + 0.4, 0])
        l3 = MathTex("L = 3", color=INK).scale(0.7).move_to([3.0, base_y - 0.4, 0])
        l1 = MathTex("L = 1", color=INK).scale(0.7).move_to([0.0, base_y - 0.4, 0])
        l0 = MathTex("L = 0", color=INK).scale(0.7).move_to([-3.0, base_y - 0.4, 0])
        eje = Line([-4.4, base_y, 0], [4.4, base_y, 0], color=INK, stroke_width=2)

        with self.narrar("b2"):
            # «La muestra de ahora manda»
            self.en("manda")
            self.resaltar(tl.palito(0), color=AMBAR, escala=1.3)

            # «la anterior aporta un poco»
            self.en("poco")
            self.resaltar(tl.palito(1), color=AMBAR, escala=1.3)

            # «casi nada»
            self.en("nada")
            self.resaltar(tl.palito(2), color=AMBAR, escala=1.5)

            # «El error que queda»
            self.en("error")
            self.corte()
            self.pop(err)

            # «la varianza menos lo que el filtro explica»
            self.en("resta")
            self.play(*[FadeIn(resta[i]) for i in range(len(resta))], run_time=self.dur(0.9))

            # «cero coma siete cuatro»
            self.en("e074")
            self.play(Create(eje), GrowFromEdge(b3, DOWN), FadeIn(l3), run_time=self.dur(0.5))
            self.pop(v3)

            # «Con una muestra eran cero coma ocho»
            self.en("e08")
            self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=self.dur(0.5))
            self.play(FadeIn(v1), run_time=0.3)

            # «sin mirar nada, cuatro»
            self.en("e4")
            self.play(GrowFromEdge(b0, DOWN), FadeIn(l0), run_time=self.dur(0.8))
            self.play(FadeIn(v0), run_time=0.3)
