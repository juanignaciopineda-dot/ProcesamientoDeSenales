"""Escena 25 — El experimento: un solo Pluto, un bloque de tramas en bucle y el lazo digital."""
from comun.escena import *
from comun.figuras_lora import *

HUECOS = (0.5, 0.9, 0.35, 0.7)     # silencios antes de cada trama (largos distintos)
LARGO = 1.0                         # largo de una trama en el dibujo


def _tira(x0, y, color, opacidad=0.45):
    """Cuatro tramas con sus silencios, a partir de x0. Devuelve (tramas, inicios)."""
    tramas, inicios, x = VGroup(), [], x0
    for h in HUECOS:
        x += h
        inicios.append(x)
        tramas.add(Rectangle(width=LARGO, height=0.6, color=color, stroke_width=2.5).set_fill(color, opacidad)
                   .move_to([x + LARGO / 2, y, 0]))
        x += LARGO
    return tramas, inicios


class ElExperimento(EscenaCurso):
    ESCENA = "25"

    def construct(self):
        pl = pluto().scale(1.5).move_to([-4.7, 1.2, 0])
        lazo_ = CurvedArrow(pl.punta_tx() + UP * 0.1, pl.punta_rx() + UP * 0.1, angle=-PI / 2, color=CIAN,
                            stroke_width=4, tip_length=0.2)
        osc = Text("Un solo oscilador", color=TXT, weight=BOLD).scale(0.6).move_to([-4.7, -0.7, 0])
        df = MathTex(r"\Delta f = 0", color=VERDE).scale(1.3).move_to([-4.7, -1.6, 0])
        y_tx, y_rx, x0 = 2.3, -0.3, 0.0
        bucle = Arc(radius=0.4, start_angle=PI / 2, angle=-1.6 * PI, color=AMBAR, stroke_width=4).add_tip(tip_length=0.18)
        bucle.move_to([-1.0, y_tx, 0])
        rtx = Text("TX", color=AMBAR, weight=BOLD).scale(0.6).move_to([-1.0, y_tx + 0.85, 0])
        rrx = Text("RX", color=CIAN, weight=BOLD).scale(0.6).move_to([-1.0, y_rx, 0])
        base_tx = Line([x0, y_tx - 0.3, 0], [6.9, y_tx - 0.3, 0], color=INK, stroke_width=2)
        base_rx = Line([x0, y_rx - 0.3, 0], [6.9, y_rx - 0.3, 0], color=INK, stroke_width=2)
        tx, ini_tx = _tira(x0, y_tx, AZUL)
        sil = VGroup()
        x = x0
        for h in HUECOS:
            sil.add(Line([x + 0.05, y_tx - 0.55, 0], [x + h - 0.05, y_tx - 0.55, 0], color=AMBAR, stroke_width=6))
            x += h + LARGO
        rsil = Text("Silencios al azar", color=AMBAR, weight=BOLD).scale(0.5).move_to([3.4, y_tx - 1.05, 0])
        rx, ini_rx = _tira(x0 + 0.25, y_rx, CIAN, 0.2)
        g = np.random.default_rng(2)
        xs = np.linspace(x0, 6.9, 260)
        ruido = traza(xs, y_rx + 0.22 * g.normal(0, 1, xs.size), RUIDO, 1.8, 0.8)
        preg = VGroup(*[Text("?", color=AMBAR, weight=BOLD).scale(0.7).move_to([xi + LARGO / 2, y_rx + 0.85, 0])
                        for xi in ini_rx])
        lz = Text("Lazo digital", color=AMBAR, weight=BOLD).scale(0.85).move_to([-4.7, -0.9, 0])
        ana = bloque("Analógico", INK, ancho=2.8, alto=0.9, escala=0.6).move_to([-4.7, -2.2, 0])
        tac = tachar(ana)
        marcas = VGroup(*[DashedLine([xi, y_rx + 0.6, 0], [xi, y_rx - 0.75, 0], color=VERDE, stroke_width=4,
                                     dash_length=0.08) for xi in ini_rx])
        d10 = MathTex(r"10\ /\ 10", color=VERDE).scale(1.8).move_to([3.0, -2.4, 0])
        ok = tilde(VERDE, 1.0).move_to([5.4, -2.4, 0])
        with self.narrar("b1"):
            # «el mismo Pluto transmite y recibe»
            self.en("mismo")
            self.play(FadeIn(pl, shift=UP * 0.2), run_time=0.4)
            self.play(Create(lazo_), run_time=self.dur(0.8))
            # «comparten oscilador»
            self.en("osc")
            self.play(FadeIn(osc, shift=UP * 0.15), run_time=self.dur(0.5))
            # «no hay desajuste de frecuencia»
            self.en("desaj")
            self.pop(df)
            # «repite sin parar»
            self.en("repite")
            self.play(Create(bucle), FadeIn(rtx), run_time=self.dur(0.7))
            # «un bloque de tramas»
            self.en("bloque")
            self.play(Create(base_tx), LaggedStart(*[FadeIn(t, shift=RIGHT * 0.15) for t in tx], lag_ratio=0.25),
                      run_time=self.dur(1.1))
            # «un silencio de largo al azar»
            self.en("silencio")
            self.play(LaggedStart(*[Create(s) for s in sil], lag_ratio=0.2), FadeIn(rsil), run_time=self.dur(0.9))
            # «El receptor graba»
            self.en("graba")
            self.play(FadeIn(rrx), Create(base_rx), FadeIn(rx), Create(ruido, rate_func=linear), run_time=self.dur(1.2))
            # «sin saber dónde están»
            self.en("sinsaber")
            self.play(LaggedStart(*[FadeIn(q, scale=0.5) for q in preg], lag_ratio=0.2), run_time=self.dur(0.8))
        with self.narrar("b2"):
            # «el lazo digital»
            self.en("lazo")
            self.play(FadeOut(osc), FadeOut(df), run_time=0.3)
            self.pop(lz)
            # «sin pasar por la parte analógica»
            self.en("sinana")
            self.play(FadeIn(ana), run_time=0.4)
            self.play(Create(tac), run_time=self.dur(0.4))
            # «sin ruido»
            self.en("sinruido")
            self.play(FadeOut(ruido), FadeOut(preg), *[t.animate.set_fill(CIAN, 0.5) for t in rx], run_time=self.dur(0.7))
            # «en la muestra exacta»
            self.en("exacta")
            self.play(LaggedStart(*[Create(m) for m in marcas], lag_ratio=0.2), run_time=self.dur(0.9))
            # «Diez de diez»
            self.en("diez")
            self.pop(d10)
            # «el programa funciona»
            self.en("funciona")
            self.play(Create(ok), run_time=self.dur(0.5))
            self.sfx("exito")
        self.wait(1.0)
        self.limpiar()
