"""Escena 09 — El filtro de Kalman: mismo resultado que Wiener, distinto camino."""
from comun.escena import *


class ElFiltroDeKalman(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        kal = self.palabra("Kalman", AMBAR, 1.1).move_to([0, 3.4, 0])
        cw = etiqueta("Wiener: densidad → factorización → α(z)", AZUL, 0.5).move_to([-3.6, 2.4, 0])
        ck = etiqueta("Kalman: modelo de estados → observador", AMBAR, 0.5).move_to([3.6, 2.4, 0])
        res = formula("0{,}443\\,z^{-1}", "\\Big/", "(1-0{,}157\\,z^{-1})", escala=0.95).move_to([0, 1.2, 0])
        aw = flecha([-3.0, 2.05, 0], [-0.9, 1.8, 0])
        ak = flecha([3.0, 2.05, 0], [0.9, 1.8, 0])
        hw = etiqueta("Wiener", AZUL, 0.45, BOLD).move_to([2.4, 0.45, 0])
        hk = etiqueta("Kalman", AMBAR, 0.45, BOLD).move_to([4.8, 0.45, 0])
        filas = [("cambian con el tiempo", -0.3), ("inestables", -1.1), ("varias entradas y salidas", -1.9)]
        rotulos = [etiqueta(t, TXT, 0.5).move_to([-3.4, y, 0]) for t, y in filas]
        for r in rotulos:
            r.align_to([-6.6, 0, 0], LEFT)
        cruces = [cruz(ROJO, 0.22).move_to([2.4, y, 0]) for _, y in filas]
        ticks = [tilde(VERDE, 0.28).move_to([4.8, y, 0]) for _, y in filas]
        r_como = etiqueta("cómo se resuelve", TXT, 0.5).move_to([-3.4, -2.8, 0]).align_to([-6.6, 0, 0], LEFT)
        r_fac = etiqueta("factorización", AZUL, 0.42).move_to([2.4, -2.8, 0])
        r_ric = etiqueta("Riccati", AMBAR, 0.42).move_to([4.8, -2.8, 0])
        coh = cohete().scale(1.2).move_to([-3.0, -0.2, 0])
        pv = etiqueta("posición y velocidad", INK, 0.5).move_to([-3.0, -1.9, 0])
        term = termometro(1.5).move_to([2.6, -0.2, 0])
        kk = formula("K", "=", "0{,}7386", escala=0.9, colores={0: AMBAR}).move_to([4.3, -0.2, 0])
        tabla = [hw, hk, *rotulos, *cruces, *ticks, r_como, r_fac, r_ric]
        with self.narrar("b1"):
            # «de Kalman»
            self.en("kalman")
            self.pop(kal)
            # «Desde Wiener se llega por la factorización»
            self.en("wiener")
            self.play(FadeIn(cw), run_time=self.dur(0.8))
            # «Kalman parte del modelo de estados»
            self.en("kcol")
            self.play(FadeIn(ck), run_time=self.dur(0.8))
            # «la forma de observador»
            self.en("obs")
            self.play(GrowArrow(aw), GrowArrow(ak), FadeIn(res), run_time=self.dur(0.9))
            # «Kalman va más lejos»
            self.en("lejos")
            self.play(FadeIn(hw), FadeIn(hk), run_time=self.dur(0.5))
            # «cambian con el tiempo»
            self.en("variante")
            self.play(FadeIn(rotulos[0]), FadeIn(cruces[0]), FadeIn(ticks[0]), run_time=self.dur(0.6))
            # «inestables»
            self.en("inest")
            self.play(FadeIn(rotulos[1]), FadeIn(cruces[1]), FadeIn(ticks[1]), run_time=self.dur(0.5))
            # «varias entradas y salidas»
            self.en("mimo")
            self.play(FadeIn(rotulos[2]), FadeIn(cruces[2]), FadeIn(ticks[2]), run_time=self.dur(0.6))
            # «la ecuación de Riccati»
            self.en("riccati")
            self.play(FadeIn(r_como), FadeIn(r_fac), FadeIn(r_ric), run_time=self.dur(0.7))
            # «sigue a un cohete»
            self.en("cohete")
            self.play(*[FadeOut(m) for m in tabla], FadeOut(cw), FadeOut(ck), FadeOut(aw), FadeOut(ak),
                      FadeOut(res), run_time=0.4)
            self.play(FadeIn(coh, shift=UP * 0.3), FadeIn(pv), run_time=self.dur(0.6))
            # «lo que acabamos de hacer con un sensor»
            self.en("sensor")
            self.play(FadeIn(term), FadeIn(kk), run_time=self.dur(0.7))
        self.wait(1.0)
        self.limpiar()
