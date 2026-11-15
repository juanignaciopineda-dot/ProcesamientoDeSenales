"""Escena 05 — Las ecuaciones de Yule-Walker: predecir sin ruido con las L últimas muestras."""
from comun.escena import *


def _mat(tex, color=TXT, escala=1.10):
    return MathTex(tex, color=color).scale(escala)


class LasEcuacionesDeYuleWalker(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.planteo()
        self.una_y_dos()
        self.usos()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------------ b1
    def planteo(self):
        t, y, v, x = sensor12(60, 31)
        L = Lienzo(ancho=8.4, alto=2.0, t_rango=(0, 60), v_max=6.0, centro=(-1.6, 2.1))
        curva = L.curva(t, x, MEDIDA, 3)
        base = L.base()
        f_sensor = MathTex("x", "=", "y", "+", "v", color=TXT).scale(1.04).move_to([-1.6, 3.6, 0])
        f_sensor[0].set_color(MEDIDA), f_sensor[2].set_color(SENAL), f_sensor[4].set_color(RUIDO)
        f_x = MathTex("x[n]", color=MEDIDA).scale(1.04).move_to([-1.6, 3.6, 0])
        casilla = FilaMuestras([r"x[n+1]"], centro=(5.3, 2.1), lado=1.88, color=INK, escala=0.98)
        interr = Text("?", color=AMBAR, weight=BOLD).scale(1.04).next_to(casilla.cas[0], UP, buff=0.12)
        ven = Rectangle(width=2.0, height=2.0, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.18)
        ven.move_to([float(L.x(54)), 2.1, 0])
        mat = _mat(r"\begin{bmatrix}C[0]&C[1]\\C[1]&C[0]\end{bmatrix}")
        hv = _mat(r"\begin{bmatrix}h_0\\h_1\end{bmatrix}", ESTIMACION)
        igual = _mat("=")
        cv = _mat(r"\begin{bmatrix}c_0\\c_1\end{bmatrix}", AMBAR)
        fila = VGroup(mat, hv, igual, cv).arrange(RIGHT, buff=0.3).move_to([-1.0, -0.6, 0])
        recuadro = SurroundingRectangle(cv, color=AMBAR, buff=0.12, stroke_width=3)
        perp = MathTex(r"e", r"\perp", r"x[n-k]", color=TXT).scale(1.10).move_to([-1.0, -2.6, 0])
        perp[0].set_color(ERROR), perp[2].set_color(MEDIDA)
        cruzada = MathTex(r"C_{yx}[k]", color=INK).scale(1.04).move_to([5.2, -0.6, 0])
        cruz_t = tachar(cruzada)
        auto = _mat(r"\begin{bmatrix}C[1]\\C[2]\end{bmatrix}", AMBAR)
        auto.move_to(cv)
        hasta = MathTex(r"C[1],\,C[2],\ldots,C[L]", color=AMBAR).scale(0.98).next_to(cv, DOWN, buff=0.5)
        hasta.shift(LEFT * 0.4)
        for m in (casilla, interr):
            m.permitir_fuera = True

        with self.narrar("b1"):
            # «Ahora sin ruido»
            self.en("sinruido")
            self.play(Create(base), Create(curva), FadeIn(f_sensor), run_time=self.dur(0.8))
            # «el proceso equis»
            self.en("proceso")
            self.play(ReplacementTransform(f_sensor, f_x), run_time=0.5)
            # «la muestra que viene»
            self.en("viene")
            self.play(FadeIn(casilla), FadeIn(interr), run_time=0.4)
            # «equis de ene más uno»
            self.en("formula")
            self.resaltar(casilla.cas[0], color=AMBAR, run_time=0.5)
            # «con las ele últimas»
            self.en("ventana")
            self.play(FadeIn(ven), run_time=0.4)
            # «la misma cuenta»
            self.en("cuenta")
            self.play(FadeIn(mat), FadeIn(hv), FadeIn(igual), run_time=self.dur(0.6))
            # «perpendicular a cada muestra usada»
            self.en("perp")
            self.play(FadeIn(perp), run_time=self.dur(0.5))
            # «La única diferencia»
            self.en("dif")
            self.play(Create(recuadro), run_time=0.4)
            # «la correlación de la derecha»
            self.en("derecha")
            self.play(FadeIn(cv), run_time=0.4)
            # «ya no es la cruzada»
            self.en("cruzada")
            self.play(FadeIn(cruzada), run_time=0.3)
            self.play(Create(cruz_t), run_time=0.3)
            # «a distancia uno, dos,»
            self.en("auto")
            self.play(ReplacementTransform(cv, auto), FadeOut(recuadro), run_time=0.5)
            # «hasta ele»
            self.en("hastaele")
            self.play(FadeIn(hasta), run_time=0.4)

    # ------------------------------------------------------------------ b2
    def una_y_dos(self):
        uno = MathTex(r"C[0]\,h_0 = C[1]", color=TXT).scale(1.30).move_to([0, 2.2, 0])
        coc = formula("h_0", "=", "C[1]", "/", "C[0]", escala=1.43, colores={0: ESTIMACION}).move_to([0, 0.6, 0])
        rho = MathTex(r"=\ \rho", color=AMBAR).scale(1.43).next_to(coc, RIGHT, buff=0.3)
        cap10 = sello("Cap. 10", INK).scale(0.9).move_to([5.0, 0.6, 0])
        mat = _mat(r"\begin{bmatrix}C[0]&C[1]\\C[1]&C[0]\end{bmatrix}", escala=1.30)
        hv = _mat(r"\begin{bmatrix}h_0\\h_1\end{bmatrix}", ESTIMACION, 1.0)
        igual = _mat("=", escala=1.30)
        cv = _mat(r"\begin{bmatrix}C[1]\\C[2]\end{bmatrix}", AMBAR, 1.0)
        fila = VGroup(mat, hv, igual, cv).arrange(RIGHT, buff=0.35).move_to([0, 0.0, 0])
        marco_m = SurroundingRectangle(mat, color=AMBAR, buff=0.15, stroke_width=3)
        marco_t = SurroundingRectangle(fila, color=AMBAR, buff=0.25, stroke_width=4)
        yw = sello("Yule-Walker", AMBAR).scale(1.2).move_to([0, -2.3, 0])

        with self.narrar("b2"):
            # «Con una muestra»
            self.en("unamuestra")
            self.corte()
            self.play(FadeIn(uno), run_time=0.5)
            # «la autocorrelación en uno entre»
            self.en("cociente")
            self.play(LaggedStart(*[FadeIn(coc[i]) for i in range(4)], lag_ratio=0.35), run_time=self.dur(0.9))
            # «la autocorrelación en cero, es decir»
            self.en("cero")
            self.play(FadeIn(coc[4]), run_time=0.3)
            # «el coeficiente de correlación»
            self.en("rho")
            self.play(FadeIn(rho), run_time=0.4)
            # «el predictor del capítulo diez»
            self.en("cap10")
            self.pop(cap10)
            # «Con dos muestras»
            self.en("dos")
            self.corte()
            self.play(FadeIn(mat), FadeIn(hv), FadeIn(igual), run_time=0.5)
            # «la misma matriz de antes»
            self.en("matriz")
            self.play(Create(marco_m), run_time=0.4)
            # «la correlación en uno y la correlación en dos»
            self.en("vector")
            self.play(FadeIn(cv), run_time=0.5)
            # «Estas ecuaciones se llaman»
            self.en("estas")
            self.play(Create(marco_t), run_time=0.5)
            # «Yule-Walker»
            self.en("yw")
            self.pop(yw)

    # ------------------------------------------------------------------ b3
    def usos(self):
        izq = RoundedRectangle(corner_radius=0.2, width=6.2, height=3.6, color=INK, stroke_width=3).move_to([-3.6, 1.2, 0])
        der = RoundedRectangle(corner_radius=0.2, width=6.2, height=3.6, color=INK, stroke_width=3).move_to([3.6, 1.2, 0])
        mon = moneda("w", RUIDO).scale(0.55).move_to([-5.9, 1.6, 0])
        cj = caja("filtro", AZUL, ancho=1.6, alto=0.8, scale=0.5).move_to([-3.6, 1.6, 0])
        f1 = flecha([-5.3, 1.6, 0], [-4.45, 1.6, 0], INK, 3)
        L = Lienzo(ancho=1.6, alto=1.0, t_rango=(0, 40), v_max=3.0, centro=(-1.7, 1.6))
        _, _, _, xs = sensor12(40, 5)
        sal = L.curva(np.arange(40), xs, MEDIDA, 3)
        f2 = flecha([-2.75, 1.6, 0], [-2.55, 1.6, 0], INK, 3)
        ar = Text("modelo autorregresivo", color=AMBAR).scale(0.65).move_to([-3.6, -0.1, 0])
        mic = microfono(TXT).scale(1.0).move_to([1.4, 1.9, 0])
        pred = MathTex(r"\hat x[n+1]=h_0\,x[n]+h_1\,x[n-1]", color=TXT).scale(0.81).move_to([3.9, 0.7, 0])
        pred_f = flecha([2.1, 1.9, 0], [3.0, 1.9, 0], INK, 3)
        guarda = VGroup(Text("solo se guarda", color=TXT).scale(0.59),
                        MathTex("e[n]", color=ERROR).scale(0.91)).arrange(RIGHT, buff=0.2).move_to([3.9, -0.1, 0])
        eco_t, eco_y, eco_v, eco_x_ = sensor12(30, 11)
        Le = Lienzo(ancho=8.0, alto=1.8, t_rango=(0, 30), v_max=7.0, centro=(-1.5, 1.4))
        curva_eco = Le.curva(np.arange(30), eco_y, SENAL, 3)
        base_eco = Le.base()
        por06 = MathTex(r"\times 0{,}6", color=AMBAR).scale(1.17).move_to([5.0, 1.6, 0])
        flecha_eco = CurvedArrow([Le.x(20), Le.y(eco_y[20]) + 0.3, 0], [Le.x(21), Le.y(eco_y[21]) + 0.3, 0],
                                 angle=-PI / 2, color=AMBAR, stroke_width=3, tip_length=0.15)
        tit_eco = Text("el eco del 0,6", color=TXT, weight=BOLD).scale(0.78).move_to([-1.5, 3.2, 0])
        vals = [4, 2.4, 1.44]
        T = Tallos(vals, centro=(-3.2, -3.0), paso=2.5, unidad=0.5, color=SENAL)
        etqs = [MathTex(s, color=TXT).scale(1.04).move_to([T.x(i), -3.0 - 0.45, 0]) for i, s in
                enumerate([r"C[0]=4", r"C[1]=2{,}4", r"C[2]=1{,}44"])]
        for m in etqs:
            m.permitir_fuera = True

        with self.narrar("b3"):
            # «Aparecen en muchos sitios»
            self.en("sitios")
            self.corte()
            self.play(Create(izq), Create(der), run_time=self.dur(0.6))
            # «modelar una señal»
            self.en("modelar")
            self.play(FadeIn(mon), FadeIn(cj), run_time=0.4)
            # «filtrar ruido»
            self.en("filtrar")
            self.play(Create(f1), Create(f2), Create(sal), run_time=self.dur(0.8))
            # «un modelo autorregresivo»
            self.en("ar")
            self.play(FadeIn(ar), run_time=0.4)
            # «la codificación de la voz»
            self.en("voz")
            self.play(FadeIn(mic), run_time=0.4)
            # «cada muestra se predice con las anteriores»
            self.en("predice")
            self.play(Create(pred_f), FadeIn(pred), run_time=self.dur(0.7))
            # «solo se guarda lo que falta»
            self.en("guarda")
            self.play(FadeIn(guarda), run_time=0.5)
            # «Probémoslas con el eco del cero coma seis»
            self.en("eco")
            self.corte()
            self.play(FadeIn(tit_eco), Create(base_eco), Create(curva_eco), run_time=self.dur(0.8))
            self.play(Create(flecha_eco), FadeIn(por06), run_time=0.4)
            # «autocorrelación cuatro»
            self.en("c4")
            self.play(FadeIn(T.base), FadeIn(T.palito(0)), FadeIn(etqs[0]), run_time=self.dur(0.4))
            # «dos coma cuatro»
            self.en("c24")
            self.play(FadeIn(T.palito(1)), FadeIn(etqs[1]), run_time=self.dur(0.4))
            # «uno coma cuatro cuatro»
            self.en("c144")
            self.play(FadeIn(T.palito(2)), FadeIn(etqs[2]), run_time=self.dur(0.4))
