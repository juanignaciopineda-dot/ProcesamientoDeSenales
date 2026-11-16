"""Escena 04 — Los dos parámetros: ancho de banda (una muestra cada 1/B) y factor de ensanchamiento."""
from comun.escena import *
from comun.figuras_lora import *


class DosParametros(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        h1 = RoundedRectangle(corner_radius=0.15, width=2.6, height=1.2, color=INK, stroke_width=2.5).move_to([-3.5, 3.0, 0])
        h2 = h1.copy().move_to([3.5, 3.0, 0])
        b = MathTex("B", color=AZUL).scale(1.6).move_to(h1)
        sf = MathTex("SF", color=AMBAR).scale(1.6).move_to(h2)
        # --- ancho de banda
        eje = Arrow([-6.4, -1.3, 0], [-0.8, -1.3, 0], color=INK, stroke_width=2.5, buff=0,
                    max_tip_length_to_length_ratio=0.04)
        rf = Text("Frecuencia", color=INK).scale(0.4).move_to([-1.6, -1.65, 0])
        franja = Rectangle(width=2.8, height=1.3, color=AZUL, stroke_width=3).set_fill(AZUL, 0.3)
        franja.move_to([-3.7, -0.65, 0])
        cb = cota([-5.1, 0.25, 0], [-2.3, 0.25, 0], "B", AZUL, UP, 0.5, tex=True)
        khz = MathTex("B", "=", r"125\ \mathrm{kHz}", color=TXT).scale(1.15).move_to([-3.5, 1.7, 0])
        khz[0].set_color(AZUL)
        pts = VGroup(*[Dot([1.0 + 0.7 * i, -0.65, 0], radius=0.1, color=SENAL) for i in range(8)])
        ct = cota(pts[3].get_center() + DOWN * 0.45, pts[4].get_center() + DOWN * 0.45, "T", INK, DOWN, 0.5, tex=True)
        tt = MathTex("T", "=", r"\frac{1}{B}", "=", r"8\ \mu\mathrm{s}", color=TXT).scale(1.2).move_to([3.5, -2.7, 0])
        chip = Text("Chip", color=AMBAR, weight=BOLD).scale(0.7).next_to(pts[5], UP, buff=0.35)
        # --- factor de ensanchamiento
        sf7 = MathTex("SF", "=", "7", color=TXT).scale(1.15).move_to([3.5, 1.7, 0])
        sf7[0].set_color(AMBAR)
        bits = fila_bits(BITS_EJEMPLO, centro=(0, 0.2), lado=0.85)
        pot = MathTex("2^{7}", color=AMBAR).scale(1.4).move_to([-2.4, -1.3, 0])
        n128 = MathTex("=", "128", r"\ \text{muestras}", color=TXT).scale(1.2).next_to(pot, RIGHT, buff=0.25)
        ts = MathTex("T_s", "=", r"128 \cdot 8\ \mu\mathrm{s}", "=", r"1{,}024\ \mathrm{ms}", color=TXT).scale(1.15)
        ts.move_to([0, -2.45, 0])
        ts[4].set_color(AMBAR)
        lento = Text("Lento a propósito", color=AMBAR, weight=BOLD).scale(0.8).move_to([0, -3.45, 0])
        with self.narrar("b1"):
            # «dos números»
            self.en("dos")
            self.play(Create(h1), Create(h2), run_time=self.dur(0.7))
            # «el ancho de banda»
            self.en("banda")
            self.pop(b)
            # «el trozo de espectro»
            self.en("trozo")
            self.play(GrowArrow(eje), FadeIn(rf), run_time=0.4)
            self.play(FadeIn(franja), FadeIn(cb), run_time=self.dur(0.6))
            # «ciento veinticinco kilohercios»
            self.en("khz")
            self.play(Write(khz), run_time=self.dur(0.8))
            # «una muestra cada ocho microsegundos»
            self.en("muestra")
            self.play(LaggedStart(*[FadeIn(p, scale=0.3) for p in pts], lag_ratio=0.15), run_time=1.0)
            self.play(FadeIn(ct), run_time=0.4)
            self.play(Write(tt), run_time=self.dur(1.2))
            # «A cada muestra»
            self.en("cada")
            self.play(pts[5].animate.set_color(AMBAR).scale(1.6), run_time=self.dur(0.4))
            # «chip»
            self.en("chip")
            self.pop(chip)
        with self.narrar("b2"):
            # «el factor de ensanchamiento»
            self.en("sf")
            self.play(*[FadeOut(m) for m in (eje, rf, franja, cb, pts, ct, tt, chip)], run_time=0.3)
            self.pop(sf)
            # «un factor de siete»
            self.en("siete")
            self.play(Write(sf7), run_time=self.dur(0.7))
            # «siete bits»
            self.en("bits")
            self.play(LaggedStart(*[FadeIn(VGroup(c, n), shift=UP * 0.15) for c, n in zip(bits.cas, bits.nums)],
                                  lag_ratio=0.12), run_time=self.dur(0.9))
            # «dos elevado a siete muestras»
            self.en("pot")
            self.pop(pot)
            # «ciento veintiocho»
            self.en("n128")
            self.play(Write(n128), run_time=self.dur(0.8))
            # «algo más de un milisegundo»
            self.en("ms")
            self.play(Write(ts), run_time=self.dur(1.2))
            # «Lento a propósito»
            self.en("lento")
            self.pop(lento)
        self.wait(1.0)
        self.limpiar()
