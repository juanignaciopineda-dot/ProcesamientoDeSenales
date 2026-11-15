"""Escena 07 — Todo depende de lo nítido que sea el pico: compresión de pulso."""
from comun.escena import *


def _ancho(x):
    return np.clip(1 - np.abs(x) / 3.0, 0, 1)


def _estrecho(x):
    return np.exp(-(x / 0.35) ** 2)


class LoNitidoDelPico(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        L1 = Lienzo(ancho=5.0, alto=2.4, t_rango=(-4, 4), v_max=1.2, centro=(-3.6, 0.0))
        L2 = Lienzo(ancho=5.0, alto=2.4, t_rango=(-4, 4), v_max=1.2, centro=(3.6, 0.0))
        b1, b2 = L1.base(), L2.base()
        c1 = curva_f(L1, _ancho, -4, 4, SENAL, 4.0)
        c2 = curva_f(L2, _estrecho, -4, 4, SENAL, 4.0)
        rng = np.random.default_rng(5)
        x = np.linspace(-4, 4, 80)
        r1 = L1.curva(x, _ancho(x) + 0.09 * rng.normal(size=80), MEDIDA, 3.0)
        r2 = L2.curva(x, _estrecho(x) + 0.09 * rng.normal(size=80), MEDIDA, 3.0)
        l1 = Text("pico ancho", color=TXT).scale(0.55).move_to([-3.6, -1.9, 0])
        l2 = Text("pico estrecho", color=TXT).scale(0.55).move_to([3.6, -1.9, 0])
        m1 = Dot(L1.p(0, 1.0), radius=0.13, color=AMBAR)
        m2 = Dot(L2.p(0, 1.0), radius=0.13, color=AMBAR)
        mal = Text("distancia ✗", color=ROJO, weight=BOLD).scale(0.6).move_to([-3.6, -2.7, 0])
        bien = tilde(VERDE, 0.5).move_to([3.6, -2.7, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to([0, 0.3, 0])
        pre = Text("¿Qué pulso da el pico más estrecho posible?", color=TXT, weight=BOLD).scale(0.7).move_to([0, 1.6, 0])
        ops = VGroup(Tallos([1] * 7, paso=0.25, unidad=0.4), Tallos([1, -1, 1, 1, -1, 1, -1], paso=0.25, unidad=0.4),
                     Tallos([1, 0.4, -1, 0.7, -0.5, 1, 0.2], paso=0.25, unidad=0.4)).arrange(RIGHT, buff=1.0)
        ops.move_to([0, -1.2, 0]).set_opacity(0.5)
        resp = Text("compresión de pulso", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, 1.9, 0])
        largo = Tallos([1] * 13, centro=(-3.0, -0.8), paso=0.3, unidad=0.7, color=SENAL)
        fino = Tallos([0] * 6 + [3.3] + [0] * 6, centro=(3.0, -0.8), paso=0.3, unidad=0.7, color=AMBAR)
        fl = flecha([-0.7, -0.5, 0], [0.7, -0.5, 0], AMBAR)
        with self.narrar("b1"):
            # «Todo depende»
            self.en("depende")
            self.play(FadeIn(b1), FadeIn(b2), run_time=0.4)
            # «lo nítido que sea el pico»
            self.en("nitido")
            self.play(Create(c1), Create(c2), run_time=self.dur(1.0))
            # «Si el pico es ancho»
            self.en("ancho")
            self.play(FadeIn(l1), Transform(c1, r1), run_time=self.dur(0.8))
            self.play(FadeIn(m1), run_time=0.3)
            # «el máximo resbala a un vecino»
            self.en("resbala")
            self.play(m1.animate.move_to(L1.p(0.9, 1.0)).set_color(ROJO), run_time=self.dur(0.9))
            # «la distancia sale mal»
            self.en("mal")
            self.pop(mal)
            # «Si es estrecho, no»
            self.en("estrecho")
            self.play(FadeIn(l2), Transform(c2, r2), FadeIn(m2), run_time=self.dur(0.8))
            self.play(FadeIn(bien), run_time=0.3)
            # «Pregunta»
            self.en("pregunta")
            self.play(*[FadeOut(m) for m in (b1, b2, c1, c2, l1, l2, m1, m2, mal, bien)], run_time=0.3)
            self.pop(q)
            # «¿qué pulso da el pico más estrecho posible?»
            self.en("quepulso")
            self.play(q.animate.scale(0.5).move_to([0, 3.2, 0]), FadeIn(pre), FadeIn(ops), run_time=self.dur(0.9))
            # «La respuesta»
            self.en("respuesta")
            self.play(FadeOut(ops), FadeOut(pre), FadeOut(q), run_time=0.4)
            # «compresión de pulso»
            self.en("compresion")
            self.pop(resp)
            self.play(FadeIn(largo), GrowArrow(fl), run_time=0.5)
            self.play(FadeIn(fino), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
