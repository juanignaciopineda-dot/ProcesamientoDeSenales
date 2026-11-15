"""Escena 10 — Tres maneras de enviar un bit con el mismo pulso: on-off, ortogonal y antipodal."""
from comun.escena import *

XC = [-4.6, 0.0, 4.6]
U = 0.4                      # pantalla por unidad de distancia (y de σ) en las campanas
DIST = [3.0, 4.24, 6.0]
QS = ["Q(1{,}5)", "Q(2{,}12)", "Q(3)"]
VALS = ["0{,}0668", "0{,}0170", "0{,}00135"]
NOMBRES = ["on-off", "ortogonal", "antipodal"]
Y_P = 1.55                   # altura de los puntos
Y_B = -3.2                   # base de las campanas


class TresManeras(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.dos_primeras()
        self.wait(0.5)
        self.tercera()
        self.wait(1.0)
        self.limpiar()

    # piezas de cada columna ---------------------------------------------------------
    def _col(self, i):
        c = {}
        x = XC[i]
        d = DIST[i] * 0.55
        c["head"] = etiqueta(NOMBRES[i], AMBAR, 0.7, BOLD).move_to([x, 2.95, 0])
        c["box"] = Rectangle(width=3.9, height=1.9, color=INK, stroke_width=2, stroke_opacity=0.5).move_to([x, Y_P - 0.15, 0])
        c["p0"] = Dot([x - d / 2, Y_P - 0.2, 0], radius=0.1, color=AZUL_C7)
        c["p1"] = Dot([x + d / 2, Y_P - 0.2, 0], radius=0.1, color=SENAL)
        c["seg"] = Line([x - d / 2, Y_P - 0.2, 0], [x + d / 2, Y_P - 0.2, 0], color=AMBAR, stroke_width=4)
        c["dist"] = MathTex(num_tex(DIST[i]), color=AMBAR).scale(0.9).move_to([x, Y_P + 0.3, 0])
        c["q"] = MathTex(QS[i], color=TXT).scale(1.0).move_to([x, 0.0, 0])
        c["val"] = MathTex(VALS[i], color=ERROR).scale(1.2).move_to([x, -0.8, 0])
        s = DIST[i] * U / 2
        sg = 1.0 * U
        c["b0"] = campana7(x - s, Y_B, sg, 1.2, RUIDO, k=2.4, ancho=3)
        c["b1"] = campana7(x + s, Y_B, sg, 1.2, SENAL, k=2.4, ancho=3)
        c["base"] = Line([x - 2.0, Y_B, 0], [x + 2.0, Y_B, 0], color=INK, stroke_width=2)
        return c

    def dos_primeras(self):
        cols = [self._col(i) for i in range(3)]
        self.cols = cols
        pulso = pulso7([2, 2, 1], centro=(-1.2, 3.3), color=SENAL, paso=0.5, unidad=0.2)
        e9 = MathTex("E=9", color=AMBAR).scale(0.9).move_to([0.9, 3.5, 0])
        sg1 = MathTex(r"\sigma=1", color=RUIDO).scale(0.9).move_to([2.4, 3.5, 0])
        c0, c1 = cols[0], cols[1]
        with self.narrar("b1"):
            # «Comparemos tres maneras»
            self.en("tres")
            self.play(*[FadeIn(c["head"]) for c in cols], *[FadeIn(c["box"]) for c in cols], run_time=self.dur(0.7))
            # «el mismo pulso»
            self.paso("pulso", pulso, t=0.5)
            # «de energía nueve»
            self.paso("nueve", e9, t=0.4)
            # «sigma uno»
            self.paso("sigma", sg1, t=0.4)
            # «La primera, on-off»
            self.en("onoff")
            self.resaltar(c0["head"], run_time=0.5)
            # «enviamos el pulso o no enviamos nada»
            self.paso("pulsono", c0["p0"], c0["p1"], t=0.6)
            # «La distancia es tres»
            self.paso("tres3", c0["seg"], c0["dist"], t=0.6)
            # «cu de uno coma cinco»
            self.paso("q15", c0["q"], t=0.6)
            # «cero coma cero seis seis ocho»
            self.en("v668")
            self.play(FadeIn(c0["val"]), FadeIn(c0["base"]), Create(c0["b0"]), Create(c0["b1"]), run_time=self.dur(0.9))
            # «La segunda, ortogonal»
            self.en("orto")
            self.resaltar(c1["head"], run_time=0.5)
            # «el pulso contra el del ejemplo anterior»
            self.paso("ejant", c1["p0"], c1["p1"], t=0.6)
            # «Distancia cuatro coma dos cuatro»
            self.paso("d424", c1["seg"], c1["dist"], t=0.6)
            # «cero coma cero uno siete»
            self.en("v017")
            self.play(FadeIn(c1["q"]), FadeIn(c1["val"]), FadeIn(c1["base"]), Create(c1["b0"]), Create(c1["b1"]),
                      run_time=self.dur(0.9))
        # no se limpia: la tercera columna sigue en el mismo cuadro

    def tercera(self):
        c = self.cols
        c2 = c[2]
        short = [Line([XC[2] - 1.65 + 1.65 * k, Y_P - 0.55, 0], [XC[2] + 0.0 + 1.65 * k, Y_P - 0.55, 0],
                      color=ERROR, stroke_width=4) for k in range(2)]
        for k in range(2):
            short[k].move_to([XC[2] - 0.825 + 1.65 * k, Y_P - 0.55, 0])
        doble = Text("×2", color=ERROR, weight=BOLD).scale(0.6).move_to([XC[2], Y_P - 0.85, 0])
        cuantas = MathTex(r"\frac{0{,}0668}{0{,}00135}", "=", "?", color=TXT).scale(1.5).move_to([-0.6, -2.55, 0])
        cuantas[2].set_color(AMBAR)
        aprox = MathTex(r"\approx 50", color=VERDE).scale(1.6).move_to([3.2, -2.55, 0])
        rel = reloj_arena(TXT).scale(0.9).move_to([-3.7, -2.55, 0])
        bells = VGroup(*[VGroup(cc["base"], cc["b0"], cc["b1"]) for cc in c])
        with self.narrar("b2"):
            # «La tercera, antipodal»
            self.en("anti")
            self.resaltar(c2["head"], run_time=0.5)
            # «el mismo pulso cambiado de signo»
            self.paso("cambiado", c2["p0"], c2["p1"], t=0.6)
            # «La distancia es seis»
            self.paso("seis", c2["seg"], c2["dist"], t=0.6)
            # «el doble que en on-off»
            self.en("doble")
            self.play(*[FadeIn(s) for s in short], FadeIn(doble), run_time=self.dur(0.8))
            # «cu de tres»
            self.paso("q3", c2["q"], t=0.5)
            # «cero coma cero cero uno tres cinco»
            self.en("v135")
            self.play(FadeIn(c2["val"]), FadeIn(c2["base"]), Create(c2["b0"]), Create(c2["b1"]), run_time=self.dur(0.9))
            # «Piénsalo un momento»
            self.en("piensalo")
            self.play(FadeOut(bells), FadeIn(rel), run_time=self.dur(0.5))
            # «¿cuántas veces menos errores?»
            self.paso("cuantas", cuantas, t=0.7)
            # «Cerca de cincuenta»
            self.en("cincuenta")
            self.play(FadeOut(rel), run_time=0.3)
            self.pop(aprox)
