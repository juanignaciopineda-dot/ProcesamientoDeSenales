"""Escena 11 — La escalera de energía: 18 · 36 · 73 para un error de 10⁻⁵, y la comparación honesta."""
from comun.escena import *

K = 0.095                    # pantalla por unidad de energía
X0 = -3.6                    # donde empiezan las barras
NOM = ["antipodal", "ortogonal", "on-off"]
COL = [VERDE, AMBAR, ERROR]
ENE = [18, 36, 73]


def barra(valor, y, color, alto=0.55):
    r = Rectangle(width=valor * K, height=alto, color=color, stroke_width=3).set_fill(color, 0.35)
    r.move_to([X0 + valor * K / 2, y, 0])
    return r


class LaEscaleraDeEnergia(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.escalera()
        self.wait(0.5)
        self.honesta()
        self.wait(1.0)
        self.limpiar()

    def escalera(self):
        ys = [1.4, 0.2, -1.0]
        nombres = [etiqueta(NOM[i], COL[i], 0.6, BOLD).move_to([-5.3, ys[i], 0]) for i in range(3)]
        barras = [barra(ENE[i], ys[i], COL[i]) for i in range(3)]
        vals = [MathTex(f"E\\approx {ENE[i]}", color=TXT).scale(0.85).move_to([X0 + ENE[i] * K + 0.9, ys[i], 0])
                for i in range(3)]
        pe = MathTex("P_e=10^{-5}", color=ERROR).scale(1.3).move_to([0, 3.2, 0])
        x2 = Text("×2", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.4, 0.8, 0])
        x4 = Text("×4", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.4, -0.1, 0])
        db1 = MathTex(r"3\ \mathrm{dB}", color=AMBAR).scale(0.8).move_to([5.9, 0.8, 0])
        db2 = MathTex(r"3\ \mathrm{dB}", color=AMBAR).scale(0.8).move_to([5.9, -0.1, 0])
        sa = Line([-5.2, -2.7, 0], [-4.2, -2.7, 0], color=SENAL, stroke_width=6)
        sb = Line([-3.6, -2.7, 0], [-1.6, -2.7, 0], color=AMBAR, stroke_width=6)
        la = MathTex("d", color=SENAL).scale(0.9).move_to([-4.7, -2.3, 0])
        lb = MathTex("2d", color=AMBAR).scale(0.9).move_to([-2.6, -2.3, 0])
        fin = MathTex(r"\text{distancia}\times 2\ =\ \mathrm{SNR}\times 4", color=TXT).scale(1.0).move_to([2.6, -2.7, 0])
        with self.narrar("b1"):
            # «Otra manera de verlo»
            self.paso("otra", *nombres, t=0.6)
            # «un error de uno entre cien mil»
            self.paso("error", pe, t=0.7)
            # «Con antipodal, dieciocho»
            self.en("d18")
            self.play(GrowFromEdge(barras[0], LEFT), FadeIn(vals[0]), run_time=self.dur(0.7))
            # «Con ortogonal, treinta y seis»
            self.en("d36")
            self.play(GrowFromEdge(barras[1], LEFT), FadeIn(vals[1]), run_time=self.dur(0.7))
            # «el doble»
            self.paso("doble", x2, t=0.4)
            # «Con on-off, setenta y tres»
            self.en("d73")
            self.play(GrowFromEdge(barras[2], LEFT), FadeIn(vals[2]), run_time=self.dur(0.8))
            # «el cuádruple»
            self.paso("cuadruple", x4, t=0.4)
            # «Tres decibelios»
            self.paso("tresdb", db1, t=0.5)
            # «entre cada escalón»
            self.paso("escalon", db2, t=0.5)
            self.resaltar(db1, db2, run_time=0.5)
            # «Duplicar la distancia»
            self.paso("duplicar", sa, sb, la, lb, t=0.7)
            # «cuadruplicar la relación señal-ruido»
            self.paso("cuadruplicar", fin, t=0.8)
        self.corte()

    def honesta(self):
        ys = [0.5, -0.6, -1.7]
        nom = [etiqueta(NOM[i], COL[i], 0.6, BOLD).move_to([-5.3, ys[i], 0]) for i in range(3)]
        ojo = caja("una advertencia", AMBAR, ancho=3.4, alto=0.7, scale=0.5).move_to([-5.0, 3.4, 0])
        # una tira de bits: el on-off no transmite la mitad del tiempo
        tira = VGroup()
        for k in range(8):
            llena = k % 2 == 0
            c = Square(side_length=0.5, color=SENAL if llena else INK, stroke_width=2.5 if llena else 1.5)
            c.set_fill(SENAL, 0.45 if llena else 0.0).move_to([-2.4 + 0.6 * k, 2.4, 0])
            tira.add(c)
        t_on = etiqueta("on-off", ERROR, 0.55, BOLD).move_to([-5.0, 2.4, 0])
        gasta = MathTex(r"E_{\text{media}}=\frac{E}{2}", color=AMBAR).scale(1.0).move_to([4.2, 2.4, 0])
        barras = [barra(ENE[i], ys[i], COL[i]) for i in range(3)]
        nueva = barra(36, ys[2], ERROR)
        v73 = MathTex("73", color=TXT).scale(0.85).move_to([X0 + 73 * K + 0.5, ys[2], 0])
        v36 = MathTex("36", color=TXT).scale(0.85).move_to([X0 + 36 * K + 0.5, ys[1], 0])
        v18 = MathTex("18", color=TXT).scale(0.85).move_to([X0 + 18 * K + 0.5, ys[0], 0])
        v36b = MathTex("36", color=TXT).scale(0.85).move_to([X0 + 36 * K + 0.5, ys[2], 0])
        igual = MathTex("=", color=AMBAR).scale(1.2).move_to([X0 + 36 * K + 1.3, (ys[1] + ys[2]) / 2, 0])
        db = MathTex(r"3\ \mathrm{dB}", color=VERDE).scale(0.9).move_to([X0 + 36 * K + 1.5, (ys[0] + ys[1]) / 2, 0])
        iconos = VGroup(modem7(INK).scale(0.8), ordenador(INK).scale(0.7), chip(INK).scale(0.6)).arrange(RIGHT, buff=0.9)
        iconos.move_to([-2.0, -3.1, 0])
        anti = self.palabra("antipodal", VERDE, 0.8).move_to([3.4, -3.0, 0])
        with self.narrar("b2"):
            # «Una advertencia honesta»
            self.paso("honesta", ojo, t=0.5)
            # «On-off no transmite nada la mitad del tiempo»
            self.en("mitad")
            self.play(FadeIn(t_on), FadeIn(tira), run_time=self.dur(0.8))
            # «gasta la mitad de energía»
            self.paso("gasta", gasta, t=0.6)
            # «a igual energía media»
            self.en("igual")
            self.play(*[FadeIn(n) for n in nom], *[GrowFromEdge(b, LEFT) for b in barras],
                      FadeIn(v73), FadeIn(v36), FadeIn(v18), run_time=self.dur(0.9))
            # «on-off empata con ortogonal»
            self.en("empata")
            self.play(ReplacementTransform(barras[2], nueva), ReplacementTransform(v73, v36b), FadeIn(igual),
                      run_time=self.dur(0.9))
            # «antipodal sigue ganando»
            self.en("sigue")
            self.resaltar(barras[0], color=VERDE, run_time=0.6)
            # «tres decibelios»
            self.paso("tres", db, t=0.5)
            # «casi todos los sistemas digitales»
            self.paso("digitales", iconos, t=0.7)
            # «antipodal, o alguna variante suya»
            self.en("variante")
            self.pop(anti)
