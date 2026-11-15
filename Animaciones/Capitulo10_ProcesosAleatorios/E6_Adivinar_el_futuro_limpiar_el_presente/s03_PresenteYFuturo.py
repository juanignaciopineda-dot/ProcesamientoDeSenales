"""Escena 03 — Presente y futuro: el sensor marca 23 y hay que apostar por la muestra siguiente."""
from comun.escena import *


def tarjeta(cx, cy, tipo):
    """Tarjeta pequeña con una recta, una parábola o una curva rara."""
    r = RoundedRectangle(corner_radius=0.1, width=1.5, height=0.85, color=INK, stroke_width=2.5).set_fill(FONDO, 1)
    u = np.linspace(-1, 1, 60)
    y = [0.28 * u, 0.42 * u ** 2 - 0.2, 0.22 * np.sin(3.1 * np.pi * u) * (0.6 + 0.4 * u)][tipo]
    curva = traza(cx + 0.55 * u, cy + y, SENAL, 3.5)
    g = VGroup(r.move_to([cx, cy, 0]), curva)
    g.marco = r
    return g


class PresenteYFuturo(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        P = PanelSensor(centro=(-0.4, -0.6), ancho=9.0, alto=3.4, n=44, n0=30)
        n0, n = P.n0, P.n
        cara = caja("3.ª cara de la memoria: predecir", AMBAR, alto=0.8, scale=0.6).move_to([0, 3.4, 0])
        pal = Palitos(range(5), [1, .6, .36, .22, .13], ancho=2.8, alto=1.3, v_max=1.0, centro=(5.4, 2.0))

        d23 = P.punto(n0, 3.0, TXT, 0.11)
        r23 = Text("23 °C", color=TXT).scale(0.5).next_to(d23, UR, buff=0.12)
        f3 = Arrow(P.p(n0 + 0.8, 0), P.p(n0 + 0.8, 3.0), buff=0, color=SENAL, stroke_width=5,
                   max_tip_length_to_length_ratio=0.2)
        t3 = Text("+3", color=SENAL, weight=BOLD).scale(0.5).next_to(f3, RIGHT, buff=0.1)

        x0, x1 = float(P.L.x(n0 + 5.6)), float(P.L.x(n - 1))
        region = Rectangle(width=x1 - x0, height=3.2, stroke_width=0, stroke_opacity=0).set_fill(INK, 0.14)
        region.move_to([(x0 + x1) / 2, -0.6, 0])
        interrogante = Text("?", color=TXT, weight=BOLD).scale(1.3).move_to(P.p(n0 + 7.2, 0.6))
        candidatos = VGroup(*[Circle(radius=0.09, color=INK, stroke_width=3).move_to(P.p(n0 + 10.5, v))
                              for v in (-3.0, -1.0, 1.0, 2.6, 4.2)])
        elegido = P.punto(n0 + 10.5, 1.8, AMBAR, 0.13)
        halo = Circle(radius=0.3, color=AMBAR, stroke_width=3).move_to(elegido)

        t1 = tarjeta(-5.4, -3.45, 0)
        t2 = tarjeta(-3.8, -3.45, 1)
        t3c = tarjeta(-2.2, -3.45, 2)
        f = formula(r"\hat x", "=", "a", r"\cdot", r"x[n_0]", "+", "b", escala=0.9).move_to([2.6, -3.45, 0])
        f[0].set_color(ESTIMACION)

        with self.narrar("b1"):
            # «La tercera cara»
            self.en("cara")
            self.pop(cara)

            # «si un proceso recuerda»
            self.en("recuerda")
            self.play(FadeIn(pal), run_time=0.6)

            # «El sensor marca ahora»
            self.en("sensor")
            self.play(Create(P.media), FadeIn(P.rotulo_media), Create(P.pasado), run_time=self.dur(1.1))

            # «veintitrés grados»
            self.en("v23")
            self.play(FadeIn(d23), FadeIn(r23), run_time=0.4)

            # «tres por encima de su media»
            self.en("media")
            self.play(Create(f3), FadeIn(t3), run_time=0.6)

            # «¿Cuánto marcará en el paso siguiente?»
            self.en("pregunta")
            self.play(FadeIn(region), FadeIn(interrogante), run_time=0.6)

            # «No podemos saberlo seguro»
            self.en("seguro")
            self.play(FadeIn(candidatos, lag_ratio=0.25), run_time=self.dur(1.0))

            # «la mejor apuesta»
            self.en("apuesta")
            self.play(candidatos.animate.fade(0.6), FadeIn(elegido), Create(halo), run_time=0.6)

            # «las más sencillas»
            self.en("sencillas")
            self.play(FadeIn(t1), FadeIn(t2), FadeIn(t3c), run_time=0.6)

            # «una recta»
            self.en("recta")
            self.play(FadeOut(t2), FadeOut(t3c), t1.marco.animate.set_stroke(AMBAR, 4),
                      t1[1].animate.set_color(AMBAR), run_time=0.4)
            self.play(FadeIn(f[:5]), run_time=self.dur(0.8))

            # «más be»
            self.en("masb")
            self.play(FadeIn(f[5:]), run_time=0.4)
            self.resaltar(f[2], f[6], color=AMBAR, escala=1.25)
        self.wait(1.0)
        self.limpiar()
