"""Escena 21 — Cuánto cuesta buscar: casi el doble de energía (2,8 dB). Comparaciones múltiples."""
from comun.escena import *


def _g(x):
    return gaussiana(x, 0.0, 1.0)


class ElPrecioEnEnergia(EscenaCurso):
    ESCENA = "21"

    def construct(self):
        self.parte_a()
        self.parte_b()
        self.wait(1.0)
        self.limpiar()

    def parte_a(self):
        L = Lienzo(ancho=11.0, alto=2.6, t_rango=(-4, 9), v_max=0.45, centro=(0.0, -1.3))
        base = L.base()
        h0 = curva_f(L, _g, -4, 9, RUIDO, 4.0, n=240)
        h1 = curva_f(L, lambda x: gaussiana(x, 4.37, 1.0), -4, 9, SENAL, 4.0, n=240)
        h1b = curva_f(L, lambda x: gaussiana(x, 6.03, 1.0), -4, 9, SENAL, 4.0, n=240)
        t0 = MathTex("H_0", color=RUIDO).scale(0.8).move_to(L.p(0.0, 0.47))
        t1 = MathTex("H_1", color=SENAL).scale(0.8).move_to(L.p(4.37, 0.47))
        u1 = DashedLine(L.p(3.09, 0), L.p(3.09, 0.42), color=AMBAR, stroke_width=4)
        u2 = DashedLine(L.p(4.75, 0), L.p(4.75, 0.42), color=AMBAR, stroke_width=4)
        rad = radar13().scale(0.9).move_to([-6.2, 3.0, 0])
        en = Text("energía", color=AMBAR, weight=BOLD).scale(0.5).move_to([-6.2, 2.0, 0])
        pd = formula(r"P_D", "=", r"0{,}9", escala=0.95, colores={0: VERDE, 2: VERDE}).move_to([-3.2, 3.2, 0])
        zona = area_f(L, lambda x: gaussiana(x, 4.37, 1.0), 3.09, 9, VERDE, 0.25, n=60)
        arr = DoubleArrow(L.p(3.09, 0.30), L.p(4.37, 0.30), color=AMBAR, buff=0, stroke_width=4,
                          max_tip_length_to_length_ratio=0.2)
        a128 = MathTex(r"1{,}28\,\sigma", color=AMBAR).scale(0.7).move_to(L.p(3.73, -0.1))
        d1 = formula("d", "=", r"3{,}09", "+", r"1{,}28", "=", r"4{,}37", escala=0.85, colores={0: AMBAR, 6: AMBAR}).move_to([-3.0, 2.2, 0])
        d2 = formula("d", "=", r"4{,}75", "+", r"1{,}28", "=", r"6{,}03", escala=0.85, colores={0: AMBAR, 6: AMBAR}).move_to([-3.0, 1.4, 0])
        c19 = formula(r"4{,}37^2", r"\approx", "19", escala=0.85, colores={2: SENAL}).move_to([4.2, 3.4, 0])
        c36 = formula(r"6{,}03^2", r"\approx", "36", escala=0.85, colores={2: ERROR}).move_to([4.2, 2.7, 0])
        b19 = Rectangle(width=1.9, height=0.4, color=SENAL, stroke_width=2).set_fill(SENAL, 0.5).move_to([4.2, 1.9, 0])
        b36 = Rectangle(width=3.6, height=0.4, color=ERROR, stroke_width=2).set_fill(ERROR, 0.5).move_to([5.1, 1.3, 0])
        b19.align_to(b36, LEFT)
        db = MathTex(r"+2{,}8\,\text{dB}", color=AMBAR).scale(1.2).move_to([5.0, 0.5, 0])
        with self.narrar("b1"):
            # «Y eso cuesta señal»
            self.en("cuesta")
            self.play(FadeIn(rad), FadeIn(en), run_time=self.dur(0.6))
            # «detectar el noventa por ciento»
            self.en("noventa")
            self.play(FadeIn(pd), run_time=self.dur(0.7))
            # «separar las dos campanas»
            self.en("campanas")
            self.play(FadeIn(base), Create(h0), Create(h1), FadeIn(t0), FadeIn(t1), run_time=self.dur(1.2))
            self.play(FadeIn(zona), run_time=0.3)
            # «el umbral más uno coma dos ocho desvíos»
            self.en("mas128")
            self.play(Create(u1), GrowArrow(arr), FadeIn(a128), run_time=self.dur(1.0))
            # «Con el umbral de una posición»
            self.en("unapos")
            self.resaltar(u1, color=AMBAR, run_time=0.5)
            # «cuatro coma tres siete»
            self.en("v437")
            self.play(FadeIn(d1), run_time=self.dur(0.9))
            # «seis coma cero tres»
            self.en("v603")
            self.play(Transform(u1, u2), FadeOut(arr), FadeOut(a128), FadeOut(zona), Transform(h1, h1b), FadeIn(d2),
                      FadeOut(t1), run_time=self.dur(1.2))
            # «Al cuadrado»
            self.en("cuadrado")
            self.play(FadeIn(c19), FadeIn(c36), run_time=self.dur(0.7))
            # «diecinueve contra treinta y seis»
            self.en("v1936")
            self.play(FadeIn(b19), FadeIn(b36), run_time=self.dur(0.8))
            # «casi el doble de energía»
            self.en("doble")
            self.resaltar(b36, color=AMBAR, run_time=0.6)
            # «unos dos coma ocho decibelios»
            self.en("db28")
            self.pop(db)

    def parte_b(self):
        tit = Text("1.000 análisis", color=TXT, weight=BOLD).scale(0.8).move_to([0, 3.2, 0])
        mats = VGroup(*[matraz().scale(0.65) for _ in range(12)]).arrange(RIGHT, buff=0.4).move_to([0, 0.6, 0])
        elegidos = [mats[2], mats[6], mats[10]]
        dd = dado().scale(0.9).move_to([0, -2.0, 0])
        cr = Text("umbral", color=ROJO).scale(0.5).move_to([-6.2, -0.4, 0])
        lin = DashedLine([-6.8, -0.7, 0], [6.8, -0.7, 0], color=ROJO, stroke_width=3)
        mult = Text("comparaciones múltiples", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -3.3, 0])
        # «Es un fenómeno muy general»
        with self.narrar("b2"):
            self.en("general")
            self.corte()
            self.play(FadeIn(tit), run_time=self.dur(0.5))
            # «si haces muchas pruebas»
            self.en("pruebas")
            self.play(LaggedStart(*[FadeIn(m) for m in mats], lag_ratio=0.08), run_time=self.dur(1.0))
            # «alguna saldrá positiva»
            self.en("positiva")
            self.play(*[m.liquido.animate.set_fill(ROJO, 0.9) for m in elegidos], run_time=self.dur(0.7))
            # «por puro azar»
            self.en("azar")
            self.pop(dd)
            # «hay que endurecer el criterio»
            self.en("endurecer")
            self.play(FadeIn(lin), FadeIn(cr), run_time=0.3)
            self.play(lin.animate.shift(UP * 1.2), cr.animate.shift(UP * 1.2), run_time=self.dur(0.8))
            # «comparaciones múltiples»
            self.en("multiples")
            self.pop(mult)
