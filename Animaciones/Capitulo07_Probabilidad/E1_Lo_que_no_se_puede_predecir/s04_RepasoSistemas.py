"""Escena 04 — Repaso de sistemas lineales e invariantes, Fourier, espectro y filtro."""
from comun.escena import *


class RepasoSistemas(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.bloque_sistema()
        self.bloque_fourier()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def bloque_sistema(self):
        t = np.linspace(0, 2, 200)
        Lin = Lienzo(ancho=2.6, alto=1.3, t_rango=(0, 2), v_max=1.3, centro=(-4.9, 0.3))
        Lout = Lienzo(ancho=2.6, alto=1.3, t_rango=(0, 2), v_max=1.3, centro=(4.9, 0.3))
        v_in = 0.8 * voz_valores(200) + 0.18 * serie(5, 200, 0.2)
        v_out = 0.8 * voz_valores(200)

        with self.narrar("b1"):
            # «Un sistema es cualquier cosa»
            self.en("caja")
            S = CajaSistema7("Sistema", centro=(0, 0.3), ancho=3.0, alto=1.5, largo=1.0)
            self.play(FadeIn(S), run_time=self.dur(0.5))

            # «recibe una señal»
            self.en("entra")
            cin = Lin.curva(t, v_in, SENAL, 3.5)
            self.play(Create(cin), run_time=self.dur(0.8), rate_func=linear)

            # «entrega otra»
            self.en("sale")
            cout = Lout.curva(t, v_out, ESTIMACION, 3.5)
            self.play(Create(cout), run_time=self.dur(0.8), rate_func=linear)

            # «un amplificador»
            self.en("amp")
            r = S.nuevo_rotulo("Amplificador")
            self.play(ReplacementTransform(S.rot, r), run_time=self.dur(0.4))
            S.rot = r

            # «un altavoz»
            self.en("altavoz")
            r = S.nuevo_rotulo("Altavoz")
            self.play(ReplacementTransform(S.rot, r), run_time=self.dur(0.4))
            S.rot = r

            # «un programa que limpia una grabación»
            self.en("programa")
            r = S.nuevo_rotulo("Programa")
            self.play(ReplacementTransform(S.rot, r), run_time=self.dur(0.4))
            S.rot = r
            self.play(cout.animate(rate_func=there_and_back).set_stroke(width=7), run_time=self.dur(0.7))

            # «los lineales e invariantes»
            self.en("li")
            lin = Text("Lineal", color=VERDE, weight=BOLD).scale(0.65).move_to([-1.7, -1.6, 0])
            inv = Text("Invariante", color=CIAN, weight=BOLD).scale(0.65).move_to([1.7, -1.6, 0])
            self.pop(lin)
            self.pop(inv)

            # «Lineales son aquellos»
            self.en("lineales")
            self.resaltar(lin, color=VERDE, run_time=0.6)

            # «si sumas dos entradas»
            self.en("suma_in")
            Lin_a = Lienzo(ancho=2.2, alto=0.9, t_rango=(0, 2), v_max=1.3, centro=(-5.2, 1.5))
            Lin_b = Lienzo(ancho=2.2, alto=0.9, t_rango=(0, 2), v_max=1.3, centro=(-5.2, -0.9))
            a = Lin_a.curva(t, np.sin(2 * np.pi * 1.5 * t), SENAL, 3.0)
            b = Lin_b.curva(t, 0.8 * np.sin(2 * np.pi * 3.5 * t), AMBAR, 3.0)
            mas = Text("+", color=TXT, weight=BOLD).scale(0.9).move_to([-5.2, 0.3, 0])
            self.play(FadeOut(cin), FadeOut(cout), run_time=0.25)
            self.play(Create(a), Create(b), FadeIn(mas), run_time=self.dur(0.7))

            # «se suman sus salidas»
            self.en("suma_out")
            Lo_a = Lienzo(ancho=2.2, alto=0.9, t_rango=(0, 2), v_max=1.3, centro=(5.2, 1.5))
            Lo_b = Lienzo(ancho=2.2, alto=0.9, t_rango=(0, 2), v_max=1.3, centro=(5.2, -0.9))
            oa = Lo_a.curva(t, 0.6 * np.sin(2 * np.pi * 1.5 * t - 0.5), SENAL, 3.0)
            ob = Lo_b.curva(t, 0.5 * np.sin(2 * np.pi * 3.5 * t - 1.0), AMBAR, 3.0)
            mas2 = Text("+", color=TXT, weight=BOLD).scale(0.9).move_to([5.2, 0.3, 0])
            self.play(Create(oa), Create(ob), FadeIn(mas2), run_time=self.dur(0.7))

            # «los invariantes»
            self.en("invariantes")
            self.resaltar(inv, color=CIAN, run_time=0.6)

            # «la misma entrada más tarde»
            self.en("tarde")
            self.play(*[FadeOut(m) for m in (a, b, mas, oa, ob, mas2)], run_time=0.25)
            Lp = Lienzo(ancho=2.8, alto=1.2, t_rango=(0, 2), v_max=1.3, centro=(-4.9, 0.3))
            Lq = Lienzo(ancho=2.8, alto=1.2, t_rango=(0, 2), v_max=1.3, centro=(4.9, 0.3))
            pulso = np.exp(-0.5 * ((t - 0.5) / 0.15) ** 2)
            pulso_tarde = np.exp(-0.5 * ((t - 1.3) / 0.15) ** 2)
            p1 = Lp.curva(t, pulso, SENAL, 3.5)
            p2 = Lp.curva(t, pulso_tarde, AMBAR, 3.5)
            self.play(Create(p1), run_time=0.4)
            self.play(Create(p2), run_time=self.dur(0.4))

            # «sale lo mismo, pero más tarde»
            self.en("mismo")
            salida = np.exp(-0.5 * ((t - 0.8) / 0.2) ** 2) * 0.8
            salida_tarde = np.exp(-0.5 * ((t - 1.6) / 0.2) ** 2) * 0.8
            q1 = Lq.curva(t, salida, SENAL, 3.5)
            q2 = Lq.curva(t, salida_tarde, AMBAR, 3.5)
            self.play(Create(q1), Create(q2), run_time=self.dur(0.8))

    # ------------------------------------------------------------ b2
    def bloque_fourier(self):
        t = np.linspace(0, 2, 220)
        frecs = [(1.0, 1.0, AZUL), (3.0, 0.7, AMBAR), (5.0, 0.45, VERDE)]
        suma = sum(a * np.sin(2 * np.pi * f * t) for f, a, _ in frecs)

        with self.narrar("b2"):
            # «la gran idea de esa materia»
            self.en("idea")
            self.corte()
            bom = bombilla().scale(1.3).move_to([0, 3.0, 0])
            self.pop(bom)

            # «cualquier señal»
            self.en("cualquier")
            La = Lienzo(ancho=4.6, alto=2.0, t_rango=(0, 2), v_max=2.4, centro=(-3.6, 0.2))
            ca = La.curva(t, suma, SENAL, 4.0)
            self.play(Create(ca), run_time=self.dur(0.9), rate_func=linear)

            # «una suma de senos de distintas frecuencias»
            self.en("suma_senos")
            igual = Text("=", color=TXT, weight=BOLD).scale(1.0).move_to([-0.4, 0.2, 0])
            self.play(FadeIn(igual), run_time=0.2)
            senos = VGroup()
            for i, (f, a, col) in enumerate(frecs):
                Lb = Lienzo(ancho=4.0, alto=0.85, t_rango=(0, 2), v_max=1.1, centro=(3.0, 1.5 - 1.3 * i))
                senos.add(Lb.curva(t, a * np.sin(2 * np.pi * f * t), col, 3.0))
            self.play(LaggedStart(*[Create(s) for s in senos], lag_ratio=0.3), run_time=self.dur(1.0))

            # «la transformada de Fourier»
            self.en("fourier")
            self.play(FadeOut(senos), FadeOut(igual), FadeOut(bom), ca.animate.move_to([-4.4, 1.0, 0]).scale(0.6),
                      run_time=0.5)
            fl = Arrow([-2.5, 1.0, 0], [0.9, 1.0, 0], color=INK, stroke_width=4, buff=0.05)
            fou = Text("Fourier", color=AMBAR, weight=BOLD).scale(0.65).move_to([-0.8, 1.6, 0])
            self.play(GrowArrow(fl), run_time=0.3)
            self.pop(fou)

            # «cuánto hay de cada frecuencia»
            self.en("barras")
            barras = BarrasF([1, 3, 5], [1.0, 0.7, 0.45], f_max=6, ancho=4.6, alto=2.0, centro=(3.8, 0.8),
                             rotulos=["1 Hz", "3 Hz", "5 Hz"])
            for b, col in zip(barras.barras, (AZUL, AMBAR, VERDE)):
                b.set_color(col)
            for p, col in zip(barras.puntas, (AZUL, AMBAR, VERDE)):
                p.set_color(col)
            self.play(Create(barras.base), *[GrowFromEdge(b, DOWN) for b in barras.barras],
                      *[FadeIn(p) for p in barras.puntas], FadeIn(barras.rot), run_time=self.dur(1.0))

            # «es el espectro»
            self.en("espectro")
            esp = Text("Espectro", color=AMBAR, weight=BOLD).scale(0.65).move_to([3.8, -1.1, 0])
            self.pop(esp)

            # «Un filtro es un sistema»
            self.en("filtro")
            self.play(FadeOut(ca), FadeOut(fl), FadeOut(fou), run_time=0.3)
            cole = colador().scale(1.5).move_to([0, 2.4, 0])
            self.play(FadeIn(cole), VGroup(barras, esp).animate.move_to([0, -1.2, 0]), run_time=self.dur(0.7))
            self.cole, self.barras, self.esp = cole, barras, esp

            # «deja pasar unas frecuencias»
            self.en("pasa")
            self.play(self.barras.barras[0].animate.set_stroke(width=11),
                      self.barras.barras[1].animate.set_stroke(width=11), run_time=self.dur(0.6))

            # «frena otras»
            self.en("frena")
            b3, p3 = self.barras.barras[2], self.barras.puntas[2]
            self.play(b3.animate.set_stroke(opacity=0.15), p3.animate.set_fill(opacity=0.15).set_stroke(opacity=0.15),
                      run_time=self.dur(0.5))

            # «explicado con calma»
            self.en("calma")
            sel = sello("Con calma", AMBAR).move_to([4.6, 2.9, 0])
            self.pop(sel)
