"""Escena 11 — La densidad desde las medidas: un histograma que se vuelve campana."""
from comun.escena import *


class Histograma(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.c = Curva(lambda x: float(gaussiana(x)), x_rango=(-4, 4), y_max=0.5, ancho=9.0, alto=3.8,
                       color=AMBAR, x_label="V", y_label="").move_to([0, -0.7, 0])
        rng = np.random.default_rng(7)
        self.muestras = rng.normal(0, 1, 10000)
        self.bordes = np.linspace(-3.6, 3.6, 25)
        with self.narrar("b1"):
            self.cuerpo()
        self.wait(1.0)
        self.limpiar()

    def barras(self, datos):
        """Barras (rectángulos) de un histograma normalizado (área 1) sobre los ejes de `self.c`."""
        cuentas, bordes = np.histogram(datos, bins=self.bordes)
        dens = cuentas / (len(datos) * np.diff(bordes))
        ax = self.c.ejes
        g = VGroup()
        for d, a, b in zip(dens, bordes[:-1], bordes[1:]):
            p0, p1 = ax.c2p(a, 0), ax.c2p(b, min(d, 0.49))
            r = Rectangle(width=p1[0] - p0[0], height=max(p1[1] - p0[1], 0.01), stroke_color=FONDO,
                          stroke_width=1.5, fill_color=SENAL, fill_opacity=0.75)
            r.move_to([(p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2, 0])
            g.add(r)
        return g

    def cuerpo(self):
        c, ax = self.c, self.c.ejes
        with_voltimetro = caja("Tensión", MEDIDA, ancho=2.0, alto=0.8, scale=0.5).move_to([-5.4, 3.0, 0])
        lecturas = ["1,02", "−0,31", "0,64", "−1,20"]

        self.en("otra")                                       # «otra forma de llegar»
        self.play(FadeIn(ax), run_time=self.dur(0.7))
        self.en("mide")                                       # «Mide una tensión con ruido»
        self.play(FadeIn(with_voltimetro), run_time=self.dur(0.4))
        lect = Text(lecturas[0], color=TXT, weight=BOLD).scale(0.6).next_to(with_voltimetro, RIGHT, buff=0.3)
        self.play(FadeIn(lect), run_time=0.3)
        for t in lecturas[1:]:
            nuevo = Text(t, color=TXT, weight=BOLD).scale(0.6).move_to(lect)
            self.play(ReplacementTransform(lect, nuevo), run_time=0.35)
            lect = nuevo
        self.en("apila")                                      # «apila cada medida en una columna»
        cuentas = {}
        cuad = VGroup()
        for v in self.muestras[:22]:
            k = int(np.clip(np.digitize(v, self.bordes) - 1, 0, len(self.bordes) - 2))
            cuentas[k] = cuentas.get(k, 0) + 1
            ancho = ax.c2p(self.bordes[1], 0)[0] - ax.c2p(self.bordes[0], 0)[0]
            q = Square(side_length=ancho * 0.9, stroke_width=1.5, stroke_color=FONDO,
                       fill_color=SENAL, fill_opacity=0.9)
            q.move_to([ax.c2p((self.bordes[k] + self.bordes[k + 1]) / 2, 0)[0],
                       ax.c2p(0, 0)[1] + ancho * 0.9 * (cuentas[k] - 0.5), 0])
            cuad.add(q)
        self.play(FadeOut(lect), FadeOut(with_voltimetro), run_time=0.3)
        self.play(LaggedStart(*[FadeIn(q, shift=DOWN * 1.2) for q in cuad], lag_ratio=0.1), run_time=self.dur(2.4))
        self.en("cien")                                       # «Con cien medidas»
        b100 = self.barras(self.muestras[:100])
        n100 = Text("100 medidas", color=TXT, weight=BOLD).scale(0.6).move_to([5.0, 3.0, 0])
        self.play(FadeOut(cuad), FadeIn(b100), FadeIn(n100), run_time=self.dur(0.8))
        self.en("irregular")                                  # «un dibujo irregular»
        self.play(LaggedStart(*[b.animate(rate_func=there_and_back).set_fill(AMBAR, 0.95) for b in b100],
                              lag_ratio=0.04), run_time=self.dur(1.5))
        self.en("diez_mil")                                   # «diez mil»
        n10k = Text("10.000 medidas", color=TXT, weight=BOLD).scale(0.6).move_to([5.0, 3.0, 0])
        self.play(ReplacementTransform(n100, n10k), run_time=self.dur(0.5))
        self.en("suave")                                      # «una forma suave»
        b10k = self.barras(self.muestras)
        self.play(ReplacementTransform(b100, b10k), run_time=self.dur(1.6))
        self.en("es_densidad")                                # «Esa forma es la densidad»
        self.play(Create(c.grafica), run_time=self.dur(1.4))
        self.en("muchas")                                     # «caen muchas medidas»
        pico = Circle(radius=0.55, color=VERDE, stroke_width=4).move_to(ax.c2p(0, float(gaussiana(0))))
        self.play(Create(pico), run_time=self.dur(0.5))
        self.en("ninguna")                                    # «casi ninguna»
        col = VGroup(*[Circle(radius=0.4, color=CIAN, stroke_width=4).move_to(ax.c2p(x, 0.03)) for x in (-3.0, 3.0)])
        self.play(FadeOut(pico), Create(col), run_time=self.dur(0.6))
