"""Escena 06 — La nave de osciladores: se elige uno al azar y sale un seno."""
from comun.escena import *


class NaveMaestra(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        rng = np.random.default_rng(6)
        xs = [-5.5 + 2.2 * k for k in range(6)]
        pos = [(x, 2.55) for x in xs] + [(x, 0.95) for x in xs]
        elegido = 8
        params = [(float(rng.uniform(0.5, 1.0)), float(rng.choice([1.0, 1.5, 2.0, 2.5, 3.0])),
                   float(rng.uniform(0, 6.28))) for _ in range(12)]
        params[elegido] = (0.8, 1.5, -0.9)
        gens = VGroup(*[generador(a, f, ph).move_to([x, y, 0]) for (a, f, ph), (x, y) in zip(params, pos)])

        with self.narrar("b1"):
            # «una nave con cientos de osciladores»
            self.en("nave")
            self.play(LaggedStart(*[FadeIn(g, scale=0.7) for g in gens], lag_ratio=0.1), run_time=self.dur(2.2))

            # «su propia amplitud», «su propia frecuencia», «su propia fase»
            tags = {}
            for marca, k, txt in (("amp", 0, "amplitud"), ("frec", 1, "frecuencia"), ("fase", 2, "fase")):
                self.en(marca)
                tags[marca] = etiqueta(txt, AMBAR, 0.6, BOLD).next_to(gens[k], UP, buff=0.2)
                self.play(FadeIn(tags[marca], shift=DOWN * 0.15), gens[k].seno.animate.set_stroke(AMBAR, width=5),
                          run_time=self.dur(0.5))
            self.play(LaggedStart(*[g.seno.animate(rate_func=there_and_back).set_stroke(AMBAR, width=5)
                                    for g in gens[3:]], lag_ratio=0.15), run_time=self.dur(2.2))

            # «elegir uno al azar»
            self.en("elige")
            self.play(*[FadeOut(t) for t in tags.values()], run_time=0.2)
            aro = RoundedRectangle(corner_radius=0.15, width=1.85, height=1.35, color=AMBAR, stroke_width=5)
            aro.move_to(gens[10])
            self.play(FadeIn(aro), run_time=0.15)
            for k in (3, 6, elegido):
                self.play(aro.animate.move_to(gens[k]), run_time=0.27, rate_func=linear)
                self.sfx("tick", gain=-20)

            # «conectarlo al osciloscopio»
            self.en("osc")
            esc = RoundedRectangle(corner_radius=0.25, width=7.6, height=3.1, color=INK, stroke_width=3.5)
            esc.set_fill("#0b0d12", 1).move_to([0, -2.0, 0])
            copia = gens[elegido].seno.copy()
            self.play(FadeIn(esc), run_time=0.3)
            self.add(copia)
            self.play(copia.animate.scale(2.6).move_to([0, -2.0, 0]), run_time=self.dur(0.7))

            # «En cuanto lo eliges»
            self.en("eliges")
            self.play(aro.animate(rate_func=there_and_back).scale(1.15), run_time=self.dur(0.6))

            # «un seno de toda la vida»
            self.en("seno")
            L = Lienzo(ancho=6.8, alto=2.4, t_rango=(0, 1), v_max=1.2, centro=(0, -2.0))
            t = np.linspace(0, 1, 200)
            a, f, ph = params[elegido]
            grande = L.curva(t, a * np.sin(2 * np.pi * f * t + ph), SENAL, 4.5)
            base = L.base()
            self.play(ReplacementTransform(copia, grande), Create(base), run_time=self.dur(1.0))

            # «cuánto vale en cada instante»
            self.en("vale")
            tr = ValueTracker(0.0)
            punto = always_redraw(lambda: Dot(L.p(tr.get_value(), a * np.sin(2 * np.pi * f * tr.get_value() + ph)),
                                              radius=0.13, color=AMBAR))

            def lectura():
                v = a * np.sin(2 * np.pi * f * tr.get_value() + ph)
                return Text("x(t) = " + num(v).replace("-", "−"), color=AMBAR).scale(0.6).move_to([5.3, -2.0, 0])

            texto = always_redraw(lectura)
            self.add(punto, texto)
            self.play(tr.animate.set_value(1.0), run_time=self.dur(3.0), rate_func=linear)
            punto.clear_updaters()
            texto.clear_updaters()
        self.wait(1.0)
        self.limpiar()
