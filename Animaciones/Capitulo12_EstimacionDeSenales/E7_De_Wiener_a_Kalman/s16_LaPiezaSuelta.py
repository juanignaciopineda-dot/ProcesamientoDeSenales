"""Escena 16 — La factorización queda suelta a propósito: se usará para detectar en ruido con memoria."""
from comun.escena import *


class LaPiezaSuelta(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        pieza = VGroup(Square(side_length=1.0, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.2),
                       Circle(radius=0.16, color=AMBAR, stroke_width=4).set_fill(FONDO, 1).move_to([0.5, 0, 0]),
                       Text("F", color=TXT, weight=BOLD).scale(0.6)).move_to([-5.8, 2.4, 0])
        fact = formula("S_{xx}", "=", "F\\,F^{*}", escala=0.95, colores={0: MEDIDA, 2: AMBAR}).move_to([-2.9, 2.4, 0])
        pz = plano_c([-5.0, -0.5], radio=1.1)
        ceros = VGroup(*[Circle(radius=0.09, color=AMBAR, stroke_width=3).move_to([-5.0 + dx, -0.5 + dy, 0])
                         for dx, dy in ((0.35, 0.0), (-0.3, 0.3), (-0.3, -0.3))])
        fm = etiqueta("fase mínima", INK, 0.42).move_to([-5.0, -2.2, 0])
        blq = formula("1/F", escala=1.0, colores={0: AMBAR}).move_to([0.3, 2.4, 0])
        ar = flecha([1.0, 2.4, 0], [3.5, 2.4, 0])
        c13 = caja("capítulo 13", AMBAR, ancho=2.8, alto=0.8, scale=0.5).move_to([5.2, 2.4, 0])
        pulso = Tallos([2, 2, 1], centro=(-1.4, -0.4), paso=0.7, unidad=0.45, color=SENAL)
        lp = etiqueta("señal conocida", SENAL, 0.42).move_to([-1.4, -1.5, 0])
        Lr = Lienzo(ancho=4.0, alto=1.3, t_rango=(0, 4), v_max=1.0, centro=(3.0, -0.4))
        ruido = Lr.curva(np.linspace(0, 4, 200), 0.8 * serie(4, 200, 0.9), RUIDO, 2.6)
        lr = etiqueta("ruido con memoria", RUIDO, 0.42).move_to([3.0, -1.5, 0])
        cx = MathTex("x", color=MEDIDA).scale(0.9).move_to([-5.8, -3.1, 0])
        c1f = caja("1/F", AMBAR, ancho=1.4, alto=0.7, scale=0.5).move_to([-3.4, -3.1, 0])
        bl = etiqueta("ruido blanco", INK, 0.5).move_to([-0.7, -3.1, 0])
        fa = caja("filtro adaptado", VERDE, ancho=3.2, alto=0.7, scale=0.48).move_to([3.0, -3.1, 0])
        ars = [flecha([-5.4, -3.1, 0], [-4.2, -3.1, 0]), flecha([-2.6, -3.1, 0], [-1.9, -3.1, 0]),
               flecha([0.5, -3.1, 0], [1.3, -3.1, 0])]
        with self.narrar("b1"):
            # «una pieza se ha quedado suelta»
            self.en("suelta")
            self.play(FadeIn(pieza, shift=DOWN * 0.3), run_time=self.dur(0.7))
            self.play(Rotate(pieza, angle=0.25), run_time=0.5)
            # «la factorización»
            self.en("fact")
            self.play(FadeIn(fact), run_time=self.dur(0.8))
            # «fase mínima»
            self.en("fasemin")
            self.play(Create(pz), FadeIn(ceros), FadeIn(fm), run_time=self.dur(0.8))
            # «su blanqueador»
            self.en("blanq")
            self.pop(blq)
            # «Volverá»
            self.en("volvera")
            self.play(GrowArrow(ar), FadeIn(c13), run_time=self.dur(0.8))
            # «detectar una señal conocida»
            self.en("detectar")
            self.play(Create(pulso.base), *[Create(t) for t in pulso.tallos], *[FadeIn(p) for p in pulso.puntos],
                      FadeIn(lp), run_time=self.dur(0.9))
            # «un ruido con memoria»
            self.en("memoria")
            self.play(Create(Lr.base()), Create(ruido), FadeIn(lr), run_time=self.dur(1.0))
            # «blanquear con uno entre F»
            self.en("blanquear")
            self.play(FadeIn(cx), GrowArrow(ars[0]), FadeIn(c1f), GrowArrow(ars[1]), FadeIn(bl), run_time=self.dur(1.2))
            # «lo que ya sabemos sobre ruido blanco»
            self.en("blanco")
            self.play(GrowArrow(ars[2]), FadeIn(fa), run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
