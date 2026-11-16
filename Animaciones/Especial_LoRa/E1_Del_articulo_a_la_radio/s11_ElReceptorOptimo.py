"""Escena 11 — El receptor óptimo: 128 productos internos y gana el mayor (y lo que cuesta)."""
from comun.escena import *
from comun.figuras_lora import *


class ElReceptorOptimo(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.banco()
        self.coste()
        self.wait(1.0)
        self.limpiar()

    def banco(self):
        r = MathTex("r", color=MEDIDA).scale(2.2).move_to([-6.3, -0.4, 0])
        sh = MathTex(r"\hat{s}", "=", "?", color=TXT).scale(1.6).move_to([5.3, 0.1, 0])
        sh[0].set_color(AMBAR)
        fin = MathTex(r"\hat{s}", "=", r"\arg\max", color=AMBAR).scale(1.2).move_to([5.1, 0.1, 0])
        fichas = [bloque(t, INK, alto=0.8, escala=0.55) for t in ("Equiprobables", "Igual energía", "Ruido blanco")]
        for f, x in zip(fichas, (-4.4, 0.0, 4.4)):
            f.move_to([x, 3.3, 0])
        opt = Text("Receptor óptimo", color=AMBAR, weight=BOLD).scale(0.9).move_to([0, 2.25, 0])
        ys = (1.1, 0.1, -0.9, -1.9)
        cajas = [caja_tex(tx, AZUL, ancho=2.6, alto=0.8, escala=0.85).move_to([-2.6, y, 0]) for tx, y in
                 zip((r"\langle r, c_{0}\rangle", r"\langle r, c_{20}\rangle", None, r"\langle r, c_{127}\rangle"), ys)
                 if tx]
        pts = MathTex(r"\vdots", color=INK).scale(1.2).move_to([-2.6, -0.9, 0])
        fl = Arrow([-5.9, -0.4, 0], [-4.75, -0.4, 0], color=INK, stroke_width=4, buff=0)
        llave = cota([-4.45, 1.5, 0], [-4.45, -2.3, 0], "", INK)
        n128 = Text("128", color=AMBAR, weight=BOLD).scale(0.7).move_to([-5.3, -1.2, 0])
        anchos = (0.35, 3.2, 0.3)
        barras = [Rectangle(width=w, height=0.5, color=c, stroke_width=2.5).set_fill(c, 0.5)
                  .move_to([-1.1 + w / 2, y, 0]) for w, y, c in zip(anchos, (1.1, 0.1, -1.9), (INK, AMBAR, INK))]
        gana = Arrow([2.3, 0.1, 0], [3.4, 0.1, 0], color=AMBAR, stroke_width=4, buff=0)
        with self.narrar("b1"):
            # «qué símbolo llegó»
            self.en("que")
            self.pop(r)
            self.play(FadeIn(sh), run_time=self.dur(0.4))
            # «igual de probables», «la misma energía», «ruido blanco»
            for marca, f in zip(("prob", "ener", "ruido"), fichas):
                self.en(marca)
                self.play(FadeIn(f, shift=DOWN * 0.2), run_time=self.dur(0.4))
            # «el receptor óptimo»
            self.en("optimo")
            self.pop(opt)
            # «con cada onda posible»
            self.en("cada")
            self.play(GrowArrow(fl), FadeIn(llave.linea), run_time=0.3)
            self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.2) for c in (cajas[0], cajas[1], pts, cajas[2])],
                                  lag_ratio=0.25), run_time=self.dur(1.2))
            # «la que más se parece»
            self.en("parece")
            self.play(*[GrowFromEdge(b, LEFT) for b in barras], run_time=self.dur(0.8))
            # «Ciento veintiocho productos internos»
            self.en("n128")
            self.pop(n128)
            # «gana el mayor»
            self.en("mayor")
            self.play(GrowArrow(gana), FadeOut(sh), run_time=0.3)
            self.pop(fin)

    def coste(self):
        m = MathTex(r"128 \times 128", "=", "16.384", color=TXT).scale(1.8).move_to([0, 2.0, 0])
        m[2].set_color(ROJO)
        sf = MathTex("SF", "=", "12", color=TXT).scale(1.3).move_to([-4.9, -0.4, 0])
        sf[0].set_color(AMBAR)
        mm = MathTex(r"4096 \times 4096", "=", "16.777.216", color=TXT).scale(1.3).move_to([1.4, -0.4, 0])
        mm[2].set_color(ROJO)
        ray = rayo().scale(1.4).move_to([-1.5, -2.6, 0])
        ata = Text("Atajo", color=AMBAR, weight=BOLD).scale(1.2).move_to([0.4, -2.6, 0])
        with self.narrar("b2"):
            # «ciento veintiocho multiplicaciones»
            self.en("mult")
            self.corte()
            self.play(Write(m[0]), run_time=self.dur(0.9))
            # «más de dieciséis mil»
            self.en("mil")
            self.play(FadeIn(m[1]), run_time=0.2)
            self.pop(m[2], sonido="impacto")
            # «un factor de doce»
            self.en("doce")
            self.play(Write(sf), run_time=self.dur(0.6))
            # «casi diecisiete millones»
            self.en("millones")
            self.play(Write(mm[:2]), run_time=0.7)
            self.pop(mm[2], sonido="impacto")
            # «un atajo»
            self.en("atajo")
            self.pop(ray, ata)
