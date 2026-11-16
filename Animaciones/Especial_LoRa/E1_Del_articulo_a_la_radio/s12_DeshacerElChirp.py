"""Escena 12 — Ec. 16, primer paso: multiplicar por el chirp que baja deja un tono de s vueltas."""
from comun.escena import *
from comun.figuras_lora import *


class DeshacerElChirp(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        ec = Text("Ec. 16", color=INK, weight=BOLD).scale(0.65).move_to([-5.9, 3.4, 0])
        pasos = VGroup(*[VGroup(RoundedRectangle(corner_radius=0.1, width=0.8, height=0.8, color=INK, stroke_width=2.5),
                                Text(n, color=TXT, weight=BOLD).scale(0.7)) for n in ("1", "2")])
        pasos.arrange(RIGHT, buff=0.4).move_to([0, 3.4, 0])
        Pa = PlanoTF(centro=(-4.6, 1.0), ancho=3.2, alto=2.7, rotulos=False)
        Pb = PlanoTF(centro=(0.0, 1.0), ancho=3.2, alto=2.7, rotulos=False)
        Pc = PlanoTF(centro=(4.6, 1.0), ancho=3.2, alto=2.7, rotulos=False)
        sube = Pa.rampa(S_EJEMPLO, grosor=6)
        baja = Pb.bajada(grosor=6)
        luz = Pb.bajada(color=TXT, grosor=9)
        por = MathTex(r"\times", color=TXT).scale(1.6).move_to([-2.3, 1.0, 0])
        igual = MathTex("=", color=TXT).scale(1.6).move_to([2.3, 1.0, 0])
        tono = Pc.tono(S_EJEMPLO, grosor=6)
        r20 = Text("20", color=AMBAR, weight=BOLD).scale(0.55).next_to(Pc.p(1, S_EJEMPLO / M7), RIGHT, buff=0.15)
        L = Lienzo(ancho=11.5, alto=1.5, t_rango=(0, 1), v_max=1.0, centro=(0, -2.1))
        t = np.linspace(0, 1, 1200)
        onda = L.curva(t, np.cos(2 * np.pi * (5.0 * t + 11.0 * t ** 2)), SENAL, 2.6)
        seno = L.curva(t, np.cos(2 * np.pi * 20 * t), AMBAR, 2.6)
        base = L.base()
        v20 = Text("20 vueltas", color=AMBAR, weight=BOLD).scale(0.75).move_to([0, -3.5, 0])
        with self.narrar("b1"):
            # «la ecuación dieciséis»
            self.en("ec16")
            self.pop(ec)
            # «dos pasos»
            self.en("dos")
            self.play(LaggedStart(*[FadeIn(p, scale=0.6) for p in pasos], lag_ratio=0.4), run_time=self.dur(0.8))
            # «multiplicar lo recibido»
            self.en("mult")
            self.play(pasos[0][0].animate.set_stroke(AMBAR, 5), FadeIn(Pa), run_time=0.4)
            self.play(Create(sube), run_time=self.dur(0.6))
            # «un chirp al revés»
            self.en("reves")
            self.play(FadeIn(por), FadeIn(Pb), run_time=0.4)
            self.play(Create(baja), run_time=self.dur(0.6))
            # «que baja en lugar de subir»
            self.en("baja")
            self.play(Create(luz), run_time=self.dur(0.8))
            self.play(FadeOut(luz), run_time=0.3)
            # «se cancelan»
            self.en("cancel")
            self.play(FadeIn(igual), FadeIn(Pc), run_time=self.dur(0.6))
            # «el desplazamiento»
            self.en("despl")
            self.play(Create(tono), FadeIn(r20), run_time=self.dur(0.7))
            # «El chirp del símbolo veinte»
            self.en("s20")
            self.play(FadeIn(base), Create(onda, rate_func=linear), run_time=self.dur(1.3))
            # «un tono puro»
            self.en("tono")
            self.play(Transform(onda, seno), run_time=self.dur(1.4))
            # «veinte vueltas por símbolo»
            self.en("v20")
            self.pop(v20)
        self.wait(1.0)
        self.limpiar()
