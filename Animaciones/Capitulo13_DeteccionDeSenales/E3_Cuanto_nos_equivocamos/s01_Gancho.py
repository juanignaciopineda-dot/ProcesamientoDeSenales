"""Escena 01 — Gancho: un radar se equivoca una de cada quince y la cuenta cabe en un papel."""
from comun.escena import *


class Gancho(EscenaCurso):
    ESCENA = "01"

    def construct(self):
        rng = np.random.default_rng(3)
        n = 160
        t = np.arange(n)
        eco = np.zeros(n)
        eco[70:86] = [0.4, 0.8, 1.2, 1.6, 1.8, 1.8, 1.6, 1.4, 1.4, 1.6, 1.8, 1.6, 1.2, 0.8, 0.4, 0.2]
        L = Lienzo(ancho=6.6, alto=2.6, t_rango=(0, n - 1), v_max=6, centro=(0.4, 1.3))
        ruido = L.curva(t, eco + rng.normal(0, 1.4, n), MEDIDA, 2.6)
        base = L.base()
        ant = antena(TXT).scale(1.3).move_to([-5.6, 1.3, 0])
        duda = Text("¿avión o ruido?", color=ESTIMACION).scale(0.6).move_to([0.4, -0.6, 0])
        pe_q = MathTex(r"P_e=\;?", color=ERROR).scale(1.0).move_to([5.5, 1.3, 0])

        cas = casillas(15, rojas=(7,), centro=(-0.9, 1.5), lado=0.5, hueco=0.1)
        val = MathTex(r"0{,}0668", color=ERROR).scale(0.95).move_to([5.0, 1.5, 0])
        hoja = hoja3(ancho=4.4, alto=3.0, renglones=4).move_to([0, -1.9, 0])
        qq = MathTex(r"Q(1{,}5)", color=ESTIMACION).scale(0.8).move_to(hoja.hoja.get_center() + DOWN * 0.95)
        raro = interrogante13(AMBAR, 1.5).move_to([3.4, -1.7, 0])
        barras = Barras((2, 2, 1), centro=(-5.2, -1.9), paso=1.0, unidad=0.42, color=SENAL, ancho=0.6)
        tacha = Line(barras.get_corner(DL) + DL * 0.1, barras.get_corner(UR) + UR * 0.1, color=ERROR, stroke_width=7)

        with self.narrar("b1"):
            # «¿Cuántas veces se equivoca un radar?»
            self.en("radar")
            self.play(FadeIn(ant), run_time=self.dur(0.4))
            self.play(Create(ant.ondas.set_color(TXT)), run_time=self.dur(0.3))
            self.play(Create(base), Create(ruido), run_time=self.dur(1.1))
            self.play(FadeIn(duda), run_time=self.dur(0.3))
            self.pop(pe_q)

            # «Una de cada quince»
            self.en("quince")
            self.play(*[FadeOut(m) for m in (ant, ruido, base, duda, pe_q)], run_time=self.dur(0.3))
            self.play(LaggedStart(*[FadeIn(c) for c in cas], lag_ratio=0.05), run_time=self.dur(0.7))
            self.pop(val)

            # «la cuenta cabe en un papel»
            self.en("papel")
            self.play(FadeIn(hoja), run_time=self.dur(0.5))
            self.play(FadeIn(qq, shift=UP * 0.1), run_time=self.dur(0.4))

            # «algo raro»
            self.en("raro")
            self.pop(raro)

            # «la forma del pulso»
            self.en("forma")
            self.play(FadeIn(barras), run_time=self.dur(0.5))

            # «no entra en ella»
            self.en("noentra")
            self.play(Create(tacha), barras.animate.fade(0.6), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
