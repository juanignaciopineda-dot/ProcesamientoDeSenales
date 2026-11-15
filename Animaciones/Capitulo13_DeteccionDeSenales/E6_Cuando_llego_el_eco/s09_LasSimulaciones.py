"""Escena 09 — Las simulaciones: el rectangular falla el retardo exacto 56 veces de cada 100."""
from comun.escena import *


class LasSimulaciones(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        pc = ordenador().scale(1.9).move_to([-4.6, 2.0, 0])
        ok = tilde(VERDE, 0.7).move_to([-3.2, 2.0, 0])
        cuenta = ValueTracker(0)
        cont = always_redraw(lambda: Text(f"{int(cuenta.get_value()):,}".replace(",", "."), color=AMBAR, weight=BOLD)
                             .scale(0.9).move_to([-4.6, 0.3, 0]))
        pru = Text("pruebas", color=INK).scale(0.5).move_to([-4.6, -0.35, 0])
        snr = formula(r"\frac{E}{\sigma^2}", "=", "13", escala=0.95, colores={2: AMBAR}).move_to([-4.6, -1.5, 0])
        tira = celdas13(64, ancho=6.0, centro=(-3.9, -3.0), alto=0.4)
        n64 = Text("64 muestras", color=INK).scale(0.45).move_to([-3.9, -3.6, 0])
        rect = Tallos([1] * 13, centro=(3.8, 3.3), paso=0.2, unidad=0.35, color=SENAL)
        rl = Text("rectangular", color=INK).scale(0.45).move_to([3.8, 2.65, 0])
        gr = grilla13(100, 10, lado=0.3, centro=(3.8, 0.4))
        dia = VGroup(*[Circle(radius=r, color=VERDE, stroke_width=3) for r in (0.45, 0.28, 0.1)]).move_to([0.1, 2.3, 0])
        dl = Text("retardo exacto", color=VERDE).scale(0.45).next_to(dia, DOWN, buff=0.2)
        p56 = Text("56 %", color=ROJO, weight=BOLD).scale(0.9).move_to([3.8, -1.7, 0])
        hist = VGroup(*[Rectangle(width=0.32, height=h, color=RUIDO, stroke_width=2).set_fill(RUIDO, 0.5)
                        for h in (0.15, 0.35, 0.7, 0.35, 0.15)]).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        hist.move_to([0.4, -0.2, 0])
        hl = Text("errores", color=INK).scale(0.4).next_to(hist, DOWN, buff=0.15)
        sel = sello("falla", ROJO).move_to([0.5, 0.9, 0])
        with self.narrar("b1"):
            # «Las simulaciones»
            self.en("sims")
            self.play(FadeIn(pc), run_time=self.dur(0.5))
            # «lo confirman»
            self.en("confirman")
            self.pop(ok)
            # «cuarenta mil pruebas»
            self.en("pruebas")
            self.play(FadeIn(pru), FadeIn(cont), run_time=0.3)
            self.play(cuenta.animate.set_value(40000), run_time=self.dur(1.2))
            # «una relación señal-ruido de trece»
            self.en("snr")
            self.play(FadeIn(snr), run_time=self.dur(0.6))
            # «un registro de sesenta y cuatro muestras»
            self.en("registro")
            self.play(FadeIn(tira), FadeIn(n64), run_time=self.dur(0.7))
            # «el rectangular falla»
            self.en("falla")
            self.play(FadeIn(rect), FadeIn(rl), run_time=self.dur(0.6))
            # «el retardo exacto»
            self.en("exacto")
            self.play(FadeIn(dia), FadeIn(dl), run_time=self.dur(0.5))
            # «cincuenta y seis veces de cada cien»
            self.en("cincuenta")
            self.play(FadeIn(gr), run_time=0.4)
            self.play(LaggedStart(*[c.animate.set_fill(ROJO, 0.7).set_stroke(ROJO) for c in gr[:56]], lag_ratio=0.03),
                      FadeIn(p56), run_time=self.dur(1.6))
            # «Casi siempre falla por poco»
            self.en("poco")
            self.play(FadeIn(hist), FadeIn(hl), run_time=self.dur(0.7))
            # «pero falla»
            self.en("pero")
            self.pop(sel)
        self.wait(1.0)
        self.limpiar()
