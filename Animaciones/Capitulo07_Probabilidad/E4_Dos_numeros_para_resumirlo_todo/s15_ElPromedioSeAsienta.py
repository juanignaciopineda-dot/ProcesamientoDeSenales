"""Escena 15 — El promedio de medidas con ruido se asienta cuanto más medidas (eje en escala logarítmica)."""
from comun.escena import *


class ElPromedioSeAsienta(EscenaCurso):
    ESCENA = "15"

    def construct(self):
        L = Lienzo(ancho=10.0, alto=4.6, t_rango=(0, 4), v_max=1.5, centro=(1.0, -0.4))
        ns = np.unique(np.round(np.logspace(0, 4, 260)).astype(int))
        t = np.log10(ns)
        colores = ((3, SENAL), (11, MEDIDA), (21, ESTIMACION))
        corridas = VGroup(*[L.curva(t, np.clip(promedios_ruido(10000, s)[ns - 1], -1.45, 1.45), c, 3.5)
                            for s, c in colores])
        verdadero = DashedLine(L.p(0, 0), L.p(4, 0), color=AMBAR, stroke_width=3)
        leyenda = VGroup(DashedLine([-0.6, 0, 0], [0.4, 0, 0], color=AMBAR, stroke_width=3),
                         Text("Valor verdadero", color=AMBAR).scale(0.55)).arrange(RIGHT, buff=0.2)
        leyenda.move_to([2.5, -3.5, 0])
        tension = Text("Tensión medida", color=INK).scale(0.55).move_to([-5.2, 2.6, 0])
        rng = np.random.default_rng(5)
        medidas = VGroup(*[Dot([-6.0 + rng.uniform(-0.45, 0.45), float(L.y(rng.normal(0, 0.9))), 0],
                               radius=0.07, color=MEDIDA) for _ in range(28)])
        marcas = {}
        for clave, n, txt in (("dos", 2, "n = 2"), ("cien", 100, "n = 100"), ("diezmil", 10000, "n = 10.000")):
            x = np.log10(n)
            lin = L.vertical(x, INK, 2.5, mitad=1.8)
            lab = Text(txt, color=TXT).scale(0.55).move_to(L.p(x, 0) + UP * 2.6 + (LEFT * 0.0 if x < 3 else LEFT * 0.4))
            marcas[clave] = VGroup(lin, lab)
        sello_ = tilde(VERDE, 0.9).move_to([6.2, 2.9, 0])
        demo = self.palabra("Demostrarlo", AMBAR, 1.3).move_to([0, 3.5, 0])
        with self.narrar("b1"):
            # «la misma tensión con ruido»
            self.en("tension")
            self.play(FadeIn(tension), Create(verdadero), FadeIn(leyenda), run_time=self.dur(1.0))
            # «muchas veces»
            self.en("veces")
            self.play(LaggedStart(*[FadeIn(m, scale=0.3) for m in medidas], lag_ratio=0.04), run_time=self.dur(1.2))
            # «haz el promedio»
            self.en("promedio")
            self.play(*[Create(c) for c in corridas], run_time=self.dur(1.6), rate_func=linear)
            # «Con dos medidas»
            self.en("dos")
            self.play(Create(marcas["dos"][0]), FadeIn(marcas["dos"][1]), run_time=self.dur(0.7))
            # «Con cien»
            self.en("cien")
            self.play(FadeOut(marcas["dos"]), Create(marcas["cien"][0]), FadeIn(marcas["cien"][1]),
                      run_time=self.dur(0.7))
            # «Con diez mil»
            self.en("diezmil")
            self.play(FadeOut(marcas["cien"]), Create(marcas["diezmil"][0]), FadeIn(marcas["diezmil"][1]),
                      run_time=self.dur(0.7))
            # «alrededor del valor verdadero»
            self.en("verdadero")
            self.play(Indicate(verdadero, color=AMBAR), run_time=self.dur(0.9))
            # «Todos lo hemos visto»
            self.en("visto")
            self.pop(sello_, sonido="exito")
            # «Vamos a demostrarlo»
            self.en("demostrar")
            self.pop(demo)
        self.wait(1.0)
        self.limpiar()
