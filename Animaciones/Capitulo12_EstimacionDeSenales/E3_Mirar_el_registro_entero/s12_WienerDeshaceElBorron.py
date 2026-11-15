"""Escena 12 — Wiener de la deconvolución: primero limpiar el ruido, después deshacer el borroneo."""
from comun.escena import *


class WienerDeshaceElBorron(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        ref = MathTex(r"H=\frac{S_{yx}}{S_{xx}}", color=INK).scale(0.9).move_to([-5.4, 3.3, 0])
        h = MathTex("H", "=", color=ESTIMACION).scale(1.6)
        inv = fraccion(MathTex("1", color=AMBAR), MathTex("G", color=AMBAR)).scale(1.25)
        punto = MathTex(r"\cdot", color=TXT).scale(1.6)
        fac = fraccion(MathTex(r"S_{rr}", color=TXT), MathTex(r"S_{rr}+S_{vv}", color=TXT)).scale(1.25)
        fila = VGroup(h, inv, punto, fac).arrange(RIGHT, buff=0.25).move_to([0, 2.1, 0])
        datos = MathTex(r"S_{rr}=|G|^{2},\;\; S_{vv}=0{,}1", color=INK).scale(1.0).move_to([4.2, 3.5, 0])
        L = lienzo_omega(ancho=8.8, alto=5.4, v_max=7.0, centro=(0.0, -2.9))
        eje = eje_omega(L, 6.8)
        c_inv = curva_f(L, lambda w: h_inverso(w, 7.0), 0.0, np.pi, ROJO, 4, n=300)
        c_wie = curva_f(L, h_wiener_dec, 0.0, np.pi, AMBAR, 5, n=200)
        w9 = 0.9 * np.pi
        guia = DashedLine(L.p(w9, 0), L.p(w9, 6.8), color=INK, stroke_width=3)
        t_f = Text("factor 0,2", color=AMBAR).scale(0.7).move_to(L.p(0.52 * np.pi, 3.9))
        d_i = Dot(L.p(w9, 6.39), radius=0.1, color=ROJO)
        t_i = Text("6,39", color=ROJO, weight=BOLD).scale(0.6).move_to(L.p(0.72 * np.pi, 6.2))
        d_w = Dot(L.p(w9, 1.256), radius=0.1, color=AMBAR)
        t_w = Text("1,26", color=AMBAR, weight=BOLD).scale(0.5).next_to(d_w, UP, buff=0.15)
        d_09 = Dot(L.p(0.1 * np.pi, float(h_wiener_dec(0.1 * np.pi))), radius=0.1, color=AMBAR)
        t_09 = Text("0,91 de factor", color=AMBAR).scale(0.6).next_to(d_09, UP, buff=0.5).shift(RIGHT * 0.8)
        self.b1 = VGroup(ref, fila, datos, eje, c_inv, c_wie, guia, t_f, d_i, t_i, d_w, t_w, d_09, t_09)
        self.L = L
        with self.narrar("b1"):
            self.en("mismo")                                 # «El filtro de Wiener sale de la misma fórmula»
            self.pop(ref)
            self.en("inv")                                   # «el inverso, uno entre ge»
            self.play(FadeIn(h), FadeIn(inv.num), Create(inv.barra), FadeIn(inv.den), run_time=0.6)
            self.en("factor")                                # «por un factor»
            self.play(FadeIn(punto), run_time=0.3)
            self.en("srr")                                   # «la potencia de la señal emborronada»
            self.play(FadeIn(fac.num), Create(fac.barra), run_time=0.5)
            self.resaltar(fac.num, color=AMBAR)
            self.en("suma")                                  # «esa potencia más la del ruido»
            self.play(FadeIn(fac.den), run_time=0.5)
            self.resaltar(fac.den, color=AMBAR)
            self.en("datos")                                 # «Con señal uno y ruido cero coma uno»
            self.play(FadeIn(datos), Create(eje.h), Create(eje.v), FadeIn(eje.rotulos), run_time=0.5)
            self.play(Create(c_inv), run_time=self.dur(1.2))
            self.en("en09")                                  # «en cero coma nueve pi»
            self.play(Create(guia), FadeIn(d_i, scale=2), FadeIn(t_i), run_time=0.5)
            self.en("f02")                                   # «cero coma dos»
            self.pop(t_f)
            self.en("g126")                                  # «uno coma dos seis»
            self.play(Create(c_wie), FadeIn(d_w, scale=2), FadeIn(t_w), run_time=self.dur(1.2))
            self.en("f09")                                   # «cero coma uno pi vale cero coma nueve»
            self.play(FadeIn(d_09, scale=2), FadeIn(t_09), run_time=0.4)
            self.en("puro")                                  # «casi el inverso puro»
            self.resaltar(c_wie, color=AMBAR, escala=1.02)

    def parte_b2(self):
        L = self.L
        c1 = Text("1 · quitar el ruido", color=CIAN, weight=BOLD).scale(0.75).move_to([-4.2, 3.4, 0])
        c2 = Text("2 · deshacer el borroneo", color=AMBAR, weight=BOLD).scale(0.75).move_to([4.0, 3.4, 0])
        factor = curva_f(L, lambda w: 6.5 * g_prom(w) ** 2 / (g_prom(w) ** 2 + 0.1), 0.0, np.pi, CIAN, 5, n=200)
        t_fac = MathTex(r"\frac{S_{rr}}{S_{rr}+S_{vv}}", color=CIAN).scale(1.0).move_to([-4.2, 2.1, 0])
        inv2 = curva_f(L, lambda w: h_inverso(w, 7.0), 0.0, np.pi, ROJO, 3, n=300)
        t_inv = MathTex(r"\frac{1}{G}", color=ROJO).scale(1.2).move_to([4.0, 2.1, 0])
        stop = cruz(ROJO, 0.4).move_to(L.p(0.93 * np.pi, 6.0))
        Ls = Lienzo(ancho=2.6, alto=0.7, t_rango=(0, 1), v_max=2.0, centro=(5.6, 0.8))
        t = np.linspace(0, 1, 100)
        se = Ls.curva(t, 1.2 * np.exp(-3 * t) * np.cos(30 * t), SENAL, 3)
        t_s = etiqueta("la señal", SENAL, 0.6).next_to(Ls.p(0.5, -1.0), DOWN, buff=0.1)
        wie = curva_f(L, h_wiener_dec, 0.0, np.pi, AMBAR, 5, n=200)
        with self.narrar("b2"):
            self.play(FadeOut(self.b1), run_time=0.3)
            self.play(Create(L.base()), FadeIn(eje_omega(L, 6.8).rotulos), run_time=0.2)
            self.en("primero")                               # «primero limpiar el ruido»
            self.play(FadeIn(c1), FadeIn(t_fac), run_time=0.5)
            self.en("apaga")                                 # «se apaga donde la señal se perdió»
            self.play(Create(factor), run_time=self.dur(1.2))
            self.en("despues")                               # «después deshacer el emborronado»
            self.play(FadeIn(c2), FadeIn(t_inv), Create(inv2), run_time=0.7)
            self.en("parar")                                 # «Nadie le ha dicho al filtro dónde parar»
            self.pop(stop)
            self.en("desaparece")                            # «cuando la señal desaparece»
            self.play(Create(se), FadeIn(t_s), run_time=0.7)
            self.en("deja")                                  # «deja de invertir»
            self.play(Create(wie), run_time=self.dur(1.0))
