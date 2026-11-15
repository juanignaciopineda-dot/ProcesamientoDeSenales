"""Escena 10 — El error es no negativo, vale 0,94 · 0,65 · 0,5 en el sensor y su media 0,686 es lo mejor posible."""
from comun.escena import *


class ElErrorDelSensor(EscenaCurso):
    ESCENA = "10"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        g1 = MathTex(r"|\gamma|\le 1", color=AMBAR).scale(1.6).move_to([-4.2, 3.2, 0])
        par = parabola_l(centro=(-4.2, 0.9), ancho=4.6, alto=2.8, fondo=0.35, color=AMBAR)
        pos = MathTex(r"S_{ee}\ge 0", color=ERROR).scale(1.5).move_to([-4.6, -1.6, 0])
        ok = tilde(VERDE, 0.4).next_to(pos, RIGHT, buff=0.3)
        tm = termometro(alto=1.1, color=ROJO, nivel=0.6).move_to([6.2, 3.1, 0])
        L = lienzo_omega(ancho=6.6, alto=6.4, v_max=1.1, centro=(3.3, -2.7))
        eje = eje_omega(L, 1.05, escala=0.75)
        ruido = Line(L.p(0, 1.0), L.p(np.pi, 1.0), color=RUIDO, stroke_width=3)
        t_r = MathTex(r"S_{vv}=1", color=RUIDO).scale(0.85).move_to(L.p(2.4, 1.0) + UP * 0.35)
        h = curva_f(L, h_wiener, 0.0, np.pi, AMBAR, 5, n=200)
        t_h = MathTex(r"S_{ee}=H", color=ERROR).scale(1.0).move_to(L.p(1.3, 0.15))
        pts = [(0.0, "0,94"), (np.pi / 2, "0,65"), (np.pi, "0,5")]
        dots = [Dot(L.p(w, h_wiener(w)), radius=0.1, color=AMBAR) for w, _ in pts]
        txts = [Text(t, color=AMBAR, weight=BOLD).scale(0.65).next_to(L.p(0, h_wiener(w)), LEFT, buff=0.2) for (w, t) in pts]
        guias = [DashedLine(L.p(0, h_wiener(w)), L.p(w, h_wiener(w)), color=AMBAR, stroke_width=2) for w, _ in pts]
        media = Line(L.p(0, 0.686), L.p(np.pi, 0.686), color=AMBAR, stroke_width=4)
        l_tot = Text("error total", color=INK).scale(0.6).move_to(L.p(2.75, 0.686) + UP * 0.32)
        v686 = Text("0,686", color=AMBAR, weight=BOLD).scale(1.3).move_to([3.3, 1.6, 0])
        self.todo = VGroup(g1, par, pos, ok, tm, ruido, t_r, h, t_h, *dots, *txts, *guias, media, l_tot, eje)
        with self.narrar("b1"):
            self.en("gamma1")                                # «la coherencia nunca pasa de uno»
            self.pop(g1)
            self.en("parabola")                              # «la parábola de Cauchy-Schwarz»
            self.play(Create(par), run_time=0.7)
            self.en("positivo")                              # «el error nunca es negativo»
            self.pop(pos)
            self.play(FadeIn(ok, scale=0.5), run_time=0.3)
            self.en("consensor")                             # «Con el sensor»
            self.pop(tm)
            self.en("ruido1")                                # «el ruido vale uno»
            self.play(Create(eje.h), Create(eje.v), FadeIn(eje.rotulos), run_time=0.4)
            self.play(Create(ruido), FadeIn(t_r), run_time=0.5)
            self.en("coincide")                              # «el error en cada frecuencia coincide con la ganancia»
            self.play(Create(h), FadeIn(t_h), run_time=self.dur(1.2))
            self.en("t94")                                   # «cero coma nueve cuatro»
            self.play(FadeIn(dots[0], scale=2), FadeIn(txts[0]), Create(guias[0]), run_time=0.3)
            self.en("t65")                                   # «cero coma seis cinco»
            self.play(FadeIn(dots[1], scale=2), FadeIn(txts[1]), Create(guias[1]), run_time=0.3)
            self.en("t5")                                    # «y cero coma cinco»
            self.play(FadeIn(dots[2], scale=2), FadeIn(txts[2]), Create(guias[2]), run_time=0.3)
            self.en("total")                                 # «El error total»
            self.play(FadeIn(l_tot), run_time=0.4)
            self.en("media")                                 # «la media de esa curva»
            self.play(Create(media), run_time=0.5)
            self.en("v686")                                  # «cero coma seis ocho seis»
            self.pop(v686)
        self.v686 = v686

    def parte_b2(self):
        Lp1 = Lienzo(ancho=5.6, alto=1.9, t_rango=(0, 1), v_max=2.5, centro=(-3.7, 2.4))
        Lp2 = Lienzo(ancho=5.6, alto=1.9, t_rango=(0, 1), v_max=2.5, centro=(3.7, 2.4))
        t = np.linspace(0, 1, 100)
        y, v, x = registro_e3(100, 13)
        a1 = Lp1.curva(t, 0.35 * y, SENAL, 3.5)
        b1 = Lp1.curva(t, 0.35 * (y + 0.12 * v), ESTIMACION, 2.0)
        a2 = Lp2.curva(t, 0.35 * y, SENAL, 3.5)
        b2 = Lp2.curva(t, np.zeros(100), ESTIMACION, 3.0)
        g1 = MathTex(r"\gamma\approx 1", color=AMBAR).scale(1.2).move_to([-3.7, 3.55, 0])
        g0 = MathTex(r"\gamma\approx 0", color=AMBAR).scale(1.2).move_to([3.7, 3.55, 0])
        big = MathTex(r"0{,}686", color=AMBAR).scale(2.4).move_to([-1.0, 0.4, 0])
        sel = sello("el mínimo", AMBAR).scale(1.2).move_to([4.2, 0.4, 0])
        big2 = MathTex(r"0{,}686", color=AMBAR).scale(1.9).move_to([-3.2, -0.9, 0])
        ventana_e = Rectangle(width=4.4, height=0.8, color=MEDIDA, stroke_width=3).set_fill(MEDIDA, 0.25).move_to([-3.2, -2.4, 0])
        l_ent = etiqueta("registro entero", MEDIDA, 0.65).next_to(ventana_e, DOWN, buff=0.2)
        n2 = MathTex(r"0{,}7386", color=AMBAR).scale(1.9).move_to([3.4, -0.9, 0])
        ventana_p = Rectangle(width=2.2, height=0.8, color=MEDIDA, stroke_width=3).set_fill(MEDIDA, 0.25).move_to([2.3, -2.4, 0])
        borde_f = Rectangle(width=2.2, height=0.8, color=INK, stroke_width=2).move_to([4.5, -2.4, 0])
        l_pas = etiqueta("solo el pasado", MEDIDA, 0.65).next_to(VGroup(ventana_p, borde_f), DOWN, buff=0.2)
        flecha_a = flecha([1.3, -0.9, 0], [-0.9, -0.9, 0], AMBAR, 4)
        peq = MathTex(r"\approx 0{,}05", color=AMBAR).scale(1.0).move_to([0.2, -0.3, 0])
        with self.narrar("b2"):
            self.play(FadeOut(self.todo), FadeOut(self.v686), run_time=0.3)
            self.en("cerca1")                                # «cercana a uno»
            self.pop(g1)
            self.en("buena")                                 # «la estimación es buena»
            self.play(Create(a1), Create(b1), run_time=0.8)
            self.en("cerca0")                                # «cercana a cero»
            self.pop(g0)
            self.en("nada")                                  # «no puede hacer nada»
            self.play(Create(a2), Create(b2), run_time=0.8)
            self.en("ese686")                                # «ese cero coma seis ocho seis»
            self.pop(big)
            self.en("mejor")                                 # «lo mejor que puede hacer cualquier filtro lineal»
            self.pop(sel)
            self.en("entero")                                # «con el registro entero»
            self.play(FadeOut(big, scale=0.5), FadeIn(big2), FadeIn(ventana_e), FadeIn(l_ent), run_time=0.6)
            self.en("pasado")                                # «el cero coma siete tres ocho seis del pasado»
            self.play(FadeIn(n2), FadeIn(ventana_p), Create(borde_f), FadeIn(l_pas), run_time=0.6)
            self.en("ayuda")                                 # «mirar el futuro ayuda»
            self.play(Create(flecha_a), run_time=0.5)
            self.en("parece")                                # «menos de lo que parece»
            self.pop(peq)
