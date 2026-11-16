"""Escena 09 — Ec. 4 a 9: las ondas son ortogonales (las flechas del producto cierran un polígono)."""
from comun.escena import *
from comun.figuras_lora import *


def _flecha(a, b, color=SENAL):
    return Arrow(a, b, color=color, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.22)


class OndasOrtogonales(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.producto()
        self.flechas()
        self.base()
        self.wait(1.0)
        self.limpiar()

    def producto(self):
        P = PlanoTF(centro=(-4.4, 0.9), ancho=4.2, alto=3.4, rotulos=False)
        rampas = VGroup(*[P.rampa(s, color=c, grosor=3.5) for s, c in
                          zip(range(0, 128, 16), [AMBAR, CIAN, VERDE, MAGENTA, AZUL, AMBAR, CIAN, VERDE])])
        rots = VGroup(*[MathTex(x, color=INK).scale(0.9) for x in ("s=0", "s=1", "s=2", r"\vdots")])
        rots.arrange(DOWN, buff=0.28).move_to([-1.2, 0.9, 0])
        q = Text("?", color=AMBAR, weight=BOLD).scale(1.5).move_to([-4.4, -1.6, 0])
        orto = Text("Ortogonales", color=AMBAR, weight=BOLD).scale(1.0).move_to([3.4, 3.0, 0])
        f = MathTex(r"\sum_{k}", r"c_i[k]\; c_q^{*}[k]", "=", "0", color=TXT).scale(1.4).move_to([3.4, 1.2, 0])
        f[3].set_color(VERDE)
        pi_ = MathTex(r"\langle c_i,\, c_q\rangle", "=", "0", r"\quad (i \neq q)", color=TXT).scale(1.2).move_to([3.4, -0.9, 0])
        pi_[0].set_color(AMBAR)
        par = Text("Parecido", color=INK, weight=BOLD).scale(0.7).next_to(pi_[0], DOWN, buff=0.35)
        with self.narrar("b1"):
            # «ciento veintiocho ondas»
            self.en("ondas")
            self.play(FadeIn(P), run_time=0.3)
            self.play(LaggedStart(*[Create(r) for r in rampas], lag_ratio=0.15), run_time=self.dur(1.4))
            # «una por símbolo»
            self.en("unapor")
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in rots], lag_ratio=0.25), run_time=self.dur(1.0))
            # «no las confunda»
            self.en("confunda")
            self.pop(q)
            # «ortogonales»
            self.en("orto")
            self.pop(orto)
            # «multiplicas dos ondas distintas»
            self.en("mult")
            self.play(Write(f[1]), run_time=self.dur(0.9))
            # «muestra a muestra»
            self.en("mam")
            self.resaltar(f[1], color=CIAN, escala=1.08, run_time=self.dur(0.6))
            # «sumas»
            self.en("sumas")
            self.play(FadeIn(f[0], shift=RIGHT * 0.15), run_time=self.dur(0.4))
            # «da cero»
            self.en("cero")
            self.play(FadeIn(f[2]), run_time=0.2)
            self.pop(f[3], sonido=None)
            # «producto interno»
            self.en("pi")
            self.play(Write(pi_), run_time=self.dur(0.9))
            # «cuánto se parecen»
            self.en("parecen")
            self.play(FadeIn(par, shift=UP * 0.15), run_time=self.dur(0.4))

    def flechas(self):
        tit = MathTex(r"c_i[k]\; c_q^{*}[k]", color=TXT).scale(1.2).move_to([-4.6, 3.1, 0])
        O = np.array([-3.6, -0.6, 0])
        org = Dot(O, radius=0.08, color=TXT)
        largo = 1.9
        abanico = [_flecha(O, O + largo * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0])) for i in range(8)]
        arco = Arc(radius=0.8, start_angle=0, angle=PI / 4, color=AMBAR, stroke_width=4).shift(O)
        Q = np.array([2.4, -2.4, 0])
        lado = 1.45
        pts = [Q]
        for i in range(8):
            pts.append(pts[-1] + lado * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]))
        cadena = [_flecha(pts[i], pts[i + 1], AMBAR) for i in range(8)]
        cierre = Dot(Q, radius=0.13, color=VERDE)
        s0 = Text("Suma = 0", color=VERDE, weight=BOLD).scale(0.95).move_to([3.1, 2.6, 0])
        with self.narrar("b2"):
            # «Se ve con flechas»
            self.en("flechas")
            self.corte()
            self.play(FadeIn(tit), FadeIn(org), run_time=self.dur(0.5))
            # «Cada producto es una flecha»
            self.en("una")
            self.play(GrowArrow(abanico[0]), run_time=self.dur(0.6))
            # «gira un ángulo fijo»
            self.en("gira")
            self.play(GrowArrow(abanico[1]), Create(arco), run_time=self.dur(0.7))
            # «vueltas completas»
            self.en("vueltas")
            self.play(LaggedStart(*[GrowArrow(a) for a in abanico[2:]], lag_ratio=0.2), run_time=self.dur(1.6))
            # «una detrás de otra»
            self.en("detras")
            self.play(FadeOut(arco), LaggedStart(*[TransformFromCopy(a, c) for a, c in zip(abanico[:7], cadena[:7])],
                                                 lag_ratio=0.12), run_time=self.dur(1.1))
            # «cierran un polígono»
            self.en("cierran")
            self.play(TransformFromCopy(abanico[7], cadena[7]), run_time=0.5)
            self.pop(cierre)
            # «Suma cero»
            self.en("suma0")
            self.pop(s0)

    def base(self):
        f = MathTex(r"\langle c_i,\, c_i\rangle", "=", "1", color=TXT).scale(1.5).move_to([-3.6, 2.7, 0])
        f[0].set_color(AMBAR)
        f[2].set_color(VERDE)
        x0, paso = -5.6, 1.0
        fila = [_flecha([x0 + paso * i, 1.2, 0], [x0 + paso * (i + 1), 1.2, 0]) for i in range(8)]
        celdas, lado = VGroup(), 0.75
        for i in range(4):
            for j in range(4):
                t = Text("1" if i == j else "0", color=VERDE if i == j else INK, weight=BOLD).scale(0.7)
                t.move_to([-4.6 + lado * j, -0.8 - lado * i, 0])
                celdas.add(t)
        diag = VGroup(*[celdas[5 * i] for i in range(4)])
        resto = VGroup(*[c for k, c in enumerate(celdas) if k % 5])
        marco = Rectangle(width=4 * lado + 0.2, height=4 * lado + 0.2, color=INK, stroke_width=2)
        marco.move_to([-4.6 + 1.5 * lado, -0.8 - 1.5 * lado, 0])
        base = Text("Base ortogonal", color=AMBAR, weight=BOLD).scale(0.95).move_to([2.6, -1.6, 0])
        rx = Text("→ Receptor", color=TXT, weight=BOLD).scale(0.85).move_to([2.6, -2.8, 0])
        with self.narrar("b3"):
            # «consigo misma»
            self.en("misma")
            self.corte()
            self.play(Write(f[0]), run_time=self.dur(0.7))
            # «todas las flechas apuntan igual»
            self.en("igual")
            self.play(LaggedStart(*[GrowArrow(a) for a in fila], lag_ratio=0.12), run_time=self.dur(1.2))
            # «suman uno»
            self.en("uno")
            self.play(FadeIn(f[1]), run_time=0.2)
            self.pop(f[2], sonido=None)
            # «Cero con las demás»
            self.en("ceros")
            self.play(FadeIn(marco), FadeIn(resto), run_time=self.dur(0.6))
            # «uno consigo misma»
            self.en("unos")
            self.play(LaggedStart(*[FadeIn(d, scale=1.6) for d in diag], lag_ratio=0.2), run_time=self.dur(0.8))
            # «una base ortogonal»
            self.en("base")
            self.pop(base)
            # «el receptor»
            self.en("rx")
            self.play(FadeIn(rx, shift=RIGHT * 0.3), run_time=self.dur(0.5))
