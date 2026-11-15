"""Escena 04 — Qué filtro buscamos: el error cuadrático medio, la linealidad y las tres versiones."""
from comun.escena import *


def _vent(L: Lienzo, k0: float, k1: float, color=AMBAR, opacidad: float = 0.22) -> Rectangle:
    """Ventana vertical que cubre las muestras k0..k1 de un lienzo."""
    a, b = L.p(k0, 0), L.p(k1, 0)
    r = Rectangle(width=abs(b[0] - a[0]), height=L.alto, stroke_width=2, color=color)
    r.set_fill(color, opacidad).move_to([(a[0] + b[0]) / 2, L.cy, 0])
    return r


class QueFiltroBuscamos(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.error_y_lineal()
        self.tres_versiones()
        self.sorpresa()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def error_y_lineal(self):
        t, y, v, x = sensor12(40)
        yh = suavizada(x)
        Lx = Lienzo(ancho=3.6, alto=1.6, t_rango=(0, 39), v_max=7, centro=(-4.8, 0.9))
        Ly = Lienzo(ancho=3.6, alto=1.6, t_rango=(0, 39), v_max=7, centro=(4.8, 0.9))
        cx = VGroup(Lx.base(INK, 1.4), Lx.curva(t, x, MEDIDA, 3))
        cyh = VGroup(Ly.base(INK, 1.4), Ly.curva(t, yh, ESTIMACION, 3.4))
        filtro = caja("filtro", AMBAR, ancho=2.0, alto=0.9).move_to([0, 0.9, 0])
        a1 = flecha([-2.9, 0.9, 0], [-1.15, 0.9, 0], INK)
        a2 = flecha([1.15, 0.9, 0], [2.9, 0.9, 0], INK)
        lx = MathTex("x[n]", color=MEDIDA).scale(0.8).move_to([-4.8, 2.35, 0])
        lyh = MathTex(r"\hat{y}[n]", color=ESTIMACION).scale(0.8).move_to([4.8, 2.35, 0])
        cual = Text("¿cuál es el mejor filtro?", color=AMBAR, weight=BOLD).scale(0.6).move_to([0, 3.3, 0])
        medida = Text("error", color=ERROR, weight=BOLD).scale(0.7).move_to([0, 3.3, 0])
        ecm = formula(r"E\big[", "(", "y", "-", r"\hat{y}", ")^2", r"\big]", escala=1.1,
                      colores={2: SENAL, 4: ESTIMACION, 5: ERROR}).move_to([0, -0.9, 0])
        Ld = Lienzo(ancho=6.0, alto=1.6, t_rango=(0, 19), v_max=7, centro=(-0.8, -2.9))
        c_y = Ld.curva(t[:20], y[:20], SENAL, 3.4)
        c_h = Ld.curva(t[:20], yh[:20], ESTIMACION, 3.4)
        difs = VGroup(*[Line(Ld.p(k, y[k]), Ld.p(k, yh[k]), color=ERROR, stroke_width=3.5) for k in range(0, 20, 2)])
        e_lab = MathTex(r"e = y - \hat{y}", color=ERROR).scale(0.8).move_to([4.5, -2.9, 0])
        lineal = Text("lineal", color=AMBAR, weight=BOLD).scale(0.8).move_to([5.3, -0.9, 0])
        suma = formula(r"\hat{y}[n]", "=", "h_0", "x[n]", "+", "h_1", "x[n-1]", r"+\cdots", escala=1.1,
                       colores={0: ESTIMACION, 2: ESTIMACION, 3: MEDIDA, 5: ESTIMACION, 6: MEDIDA})
        suma.move_to([0, -1.7, 0])
        r_h0 = SurroundingRectangle(suma[2], color=AMBAR, buff=0.06)
        r_h1 = SurroundingRectangle(suma[5], color=AMBAR, buff=0.06)

        with self.narrar("b1"):
            # «un filtro»
            self.en("filtro")
            self.play(FadeIn(cx), FadeIn(filtro), Create(a1), run_time=self.dur(0.6))
            self.play(FadeIn(lx), run_time=0.3)

            # «una estimación de i griega»
            self.en("est")
            self.play(Create(a2), FadeIn(cyh), run_time=self.dur(0.6))
            self.play(FadeIn(lyh), run_time=0.3)

            # «i griega con sombrero»
            self.en("sombrero")
            self.resaltar(lyh, color=AMBAR, escala=1.25)

            # «¿Cuál es la mejor?»
            self.en("cual")
            self.pop(cual)

            # «La medida de siempre»
            self.en("medida")
            self.play(FadeOut(cual), run_time=0.25)
            self.pop(medida)

            # «el error cuadrático medio»
            self.en("ecm")
            self.play(*[FadeIn(ecm[i], shift=UP * 0.1) for i in range(len(ecm))], run_time=self.dur(0.9))

            # «la diferencia entre la temperatura verdadera y la estimada»
            self.en("dif")
            self.play(Create(c_y), Create(c_h), run_time=self.dur(0.8))
            self.play(Create(difs), run_time=self.dur(0.8))

            # «y la estimada»
            self.en("estimada")
            self.pop(e_lab)

            # «Y el filtro tiene que ser lineal»
            self.en("lineal")
            self.pop(lineal)

            # «una suma de muestras de equis»
            self.en("suma")
            self.play(*[FadeOut(m) for m in [ecm, c_y, c_h, difs, e_lab, lineal]], run_time=0.3)
            self.play(LaggedStart(*[FadeIn(suma[i], shift=UP * 0.1) for i in range(len(suma))], lag_ratio=0.25),
                      run_time=self.dur(1.5))

            # «cada una multiplicada por un coeficiente»
            self.en("coef")
            self.play(Create(r_h0), Create(r_h1), run_time=self.dur(0.5))
        self.wait(0.3)
        self.limpiar()

    # ------------------------------------------------------------ b2
    def tres_versiones(self):
        t, y, v, x = sensor12(40)
        cxs = [-4.6, 0.0, 4.6]
        self.L3 = [Lienzo(ancho=3.2, alto=1.3, t_rango=(0, 39), v_max=7, centro=(c, 0.2)) for c in cxs]
        self.marcos = [RoundedRectangle(corner_radius=0.15, width=3.8, height=2.8, color=INK, stroke_width=2.5)
                       .move_to([c, 0.2, 0]) for c in cxs]
        curvas = [VGroup(L.curva(t, x, MEDIDA, 2.6), L.vertical(30, INK, 2, mitad=0.65)) for L in self.L3]
        ojos = [ojo(AMBAR).scale(0.5).move_to([c, 2.3, 0]) for c in cxs]
        flecha_d = Arrow([-6.2, 3.3, 0], [6.2, 3.3, 0], buff=0, color=INK, stroke_width=4,
                         max_tip_length_to_length_ratio=0.05)
        dificultad = Text("dificultad", color=INK).scale(0.5).move_to([0, 3.62, 0])
        w1 = _vent(self.L3[0], 27, 30)
        w2 = _vent(self.L3[1], 0, 39)
        w3 = _vent(self.L3[2], 8, 30)
        futuro = _vent(self.L3[2], 30, 39, ROJO, 0.3)
        cruz3 = cruz(ROJO, 0.7).move_to(self.L3[2].p(34.5, 0))
        lab = [Text(s, color=TXT).scale(0.45).move_to([c, -1.55, 0]) for s, c in
               zip(["unas pocas muestras (FIR)", "todo el registro", "presente y pasado"], cxs)]
        f_p = [Arrow(self.L3[1].p(30, 0) + UP * 1.0 + d * 0.1, self.L3[1].p(30, 0) + UP * 1.0 + d * 1.1, buff=0,
                     color=AMBAR, stroke_width=4, max_tip_length_to_length_ratio=0.3) for d in (LEFT, RIGHT)]
        rel = reloj(TXT).scale(0.7).move_to([6.1, 2.3, 0])
        dificil = Text("la difícil", color=AMBAR, weight=BOLD).scale(0.55).move_to([4.6, -2.25, 0])
        wiener = Text("Wiener", color=TXT, weight=BOLD).scale(0.6).move_to([4.6, -2.95, 0])
        anos = Text("años 40", color=INK).scale(0.5).move_to([4.6, -3.45, 0])
        fw = Text("filtro de Wiener", color=AMBAR, weight=BOLD).scale(0.6).move_to([4.6, -2.95, 0])
        self._doors = (curvas, self.marcos, lab, w1, w2, w3, futuro, cruz3, ojos, rel)

        with self.narrar("b2"):
            # «tres versiones»
            self.en("tres")
            self.play(*[FadeIn(m) for m in self.marcos], *[FadeIn(c) for c in curvas], run_time=self.dur(0.8))

            # «de dificultad creciente»
            self.en("creciente")
            self.play(Create(flecha_d), FadeIn(dificultad), run_time=self.dur(0.7))

            # «cuántas muestras pueda mirar el filtro»
            self.en("mirar")
            self.play(*[FadeIn(o) for o in ojos], run_time=self.dur(0.6))

            # «Primera»
            self.en("p1")
            self.play(FadeIn(w1), FadeIn(lab[0]), run_time=self.dur(0.5))
            self.resaltar(self.marcos[0], color=AMBAR, escala=1.04)

            # «Segunda»
            self.en("p2")
            self.play(FadeIn(w2), FadeIn(lab[1]), run_time=self.dur(0.5))
            self.resaltar(self.marcos[1], color=AMBAR, escala=1.04)

            # «pasado y futuro»
            self.en("pasfut")
            self.play(*[GrowArrow(a) for a in f_p], run_time=self.dur(0.5))

            # «Tercera»
            self.en("p3")
            self.play(FadeIn(w3), FadeIn(lab[2]), run_time=self.dur(0.5))
            self.resaltar(self.marcos[2], color=AMBAR, escala=1.04)

            # «nada del futuro»
            self.en("nofut")
            self.play(FadeIn(futuro), Create(cruz3), run_time=self.dur(0.5))

            # «tiempo real»
            self.en("tr")
            self.pop(rel)

            # «y es la difícil»
            self.en("dificil")
            self.pop(dificil)
            self.play(self.marcos[2].animate.set_stroke(AMBAR, 4), run_time=0.3)

            # «Norbert Wiener»
            self.en("wiener")
            self.pop(wiener)

            # «principios de los años cuarenta»
            self.en("cuarenta")
            self.play(FadeIn(anos), run_time=self.dur(0.4))

            # «filtro de Wiener»
            self.en("fw")
            self.play(FadeOut(wiener), FadeOut(anos), run_time=0.25)
            self.pop(fw)
        self.wait(0.3)

    # ------------------------------------------------------------ b3
    def sorpresa(self):
        curvas, marcos, lab, w1, w2, w3, futuro, cruz3, ojos, rel = self._doors
        L3 = self.L3
        cohete_i = cohete().scale(1.3).move_to([4.6, 0.3, 0])
        kalman = Text("Kalman", color=AMBAR, weight=BOLD).scale(0.7).move_to([4.6, -1.45, 0])
        excl = Text("!", color=AMBAR, weight=BOLD).scale(1.4).move_to([2.6, 1.6, 0])
        pred = caja("predice", AZUL, ancho=1.55, alto=0.7, scale=0.4).move_to([-0.2, 0.2, 0])
        corr = caja("corrige", AMBAR, ancho=1.55, alto=0.7, scale=0.4).move_to([-0.2, 0.2, 0])
        # en la puerta 3, que se corre al centro
        puerta3 = [marcos[2], curvas[2], w3, futuro, cruz3, ojos[2], rel]
        fl = flechas_xy(origen=(0.6, -1.7), largo=3.4, angulo=50)
        F, r = fl
        llave_i = llave(AMBAR).scale(1.0).move_to([-1.3, 3.1, 0])
        clave = Text("la clave", color=AMBAR, weight=BOLD).scale(0.6).move_to([0.5, 3.1, 0])
        filtro = caja("filtro lineal", AMBAR, ancho=3.0, alto=0.9, scale=0.5).move_to([-4.3, -0.6, 0])
        igual = MathTex("=", color=TXT).scale(1.4).move_to([-1.7, -0.6, 0])
        cap8 = Text("Capítulo 8", color=INK).scale(0.55).move_to([2.6, 2.2, 0])

        with self.narrar("b3"):
            # «una sorpresa»
            self.en("sorpresa")
            otros = [marcos[0], marcos[1], curvas[0], curvas[1], w1, w2, ojos[0], ojos[1]] + lab
            self.play(*[FadeOut(m) for m in otros], FadeOut(rel),
                      *[m.animate.shift(LEFT * 4.6) for m in puerta3 if m is not rel], run_time=self.dur(0.7))
            self.pop(excl)

            # «escrito de otra manera»
            self.en("otra")
            self.play(FadeOut(curvas[2]), FadeOut(w3), FadeOut(futuro), FadeOut(cruz3), FadeOut(ojos[2]),
                      run_time=0.3)
            pred.move_to([0.0, 0.8, 0])
            corr.move_to([0.0, -0.4, 0])
            self.play(FadeIn(pred), FadeIn(corr), run_time=self.dur(0.4))

            # «un cohete en pleno vuelo»
            self.en("cohete")
            self.play(FadeIn(cohete_i, shift=UP * 0.4), run_time=self.dur(0.6))

            # «el filtro de Kalman»
            self.en("kalman")
            self.pop(kalman)

            # «empecemos por algo que ya sabemos»
            self.en("empecemos")
            self.corte()
            self.play(Create(F.presente), Create(F.futuro), Create(F.sombra), Create(F.error), Create(F.recto),
                      FadeIn(r["x"]), FadeIn(r["y"]), FadeIn(r["yh"]), FadeIn(r["e"]), run_time=self.dur(1.2))

            # «la clave de todo el capítulo»
            self.en("clave")
            self.play(FadeIn(llave_i), run_time=0.3)
            self.pop(clave)

            # «este problema es, exactamente»
            self.en("exacto")
            self.play(FadeIn(filtro), FadeIn(igual), run_time=self.dur(0.5))

            # «el capítulo ocho»
            self.en("cap8")
            self.pop(cap8)
