"""Escena 13 — Cierre: resumen y anuncio del E4, «El futuro no está disponible»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        col = columna_ecuaciones(centro=(-5.0, 0.4), escala=0.5, paso=0.62)
        frac = MathTex(r"H=\frac{S_{yx}}{S_{xx}}", color=TXT).scale(1.8).move_to([0.5, 2.8, 0])
        L = lienzo_omega(ancho=7.0, alto=1.0, v_max=1.0, centro=(0.5, 1.3))
        sl = rebanadas_omega(L, 7, alto=0.9)
        barrido = Line([L.cx - L.ancho / 2, 1.9, 0], [L.cx - L.ancho / 2, 0.7, 0], color=AMBAR, stroke_width=5)
        c8 = MathTex(r"a=C_{xx}^{-1}c", color=TXT).scale(1.2).move_to([-1.6, -0.2, 0])
        c8t = Text("Cap. 8", color=INK).scale(0.6).next_to(c8, RIGHT, buff=0.25)
        tm = termometro(alto=1.3, color=ROJO, nivel=0.6).move_to([2.6, -0.2, 0])
        sel = sello("el mínimo", AMBAR).move_to([5.3, 0.9, 0])
        v686 = MathTex(r"0{,}686", color=AMBAR).scale(1.8).move_to([5.3, -0.6, 0])
        ej = eje_muestras(y=-2.2, n_pasado=6, n_futuro=5, paso=0.8)
        cruces = VGroup(*[cruz(ROJO, 0.25).move_to(d.get_center() + UP * 0.45) for d in ej.futuro])
        e4 = caja("Episodio 4", AZUL, ancho=3.2, alto=0.9, scale=0.6).move_to([0, 1.6, 0])
        titulo = VGroup(self.palabra("El futuro", TXT, 1.5), self.palabra("no está disponible", AMBAR, 1.5))
        titulo.arrange(DOWN, buff=0.3).move_to([0, -0.5, 0])
        with self.narrar("b1"):
            self.en("sistema")                               # «un sistema infinito»
            self.play(FadeIn(col), run_time=0.6)
            self.en("division")                              # «una división en cada frecuencia»
            self.play(FadeIn(frac, shift=UP * 0.2), FadeIn(sl), run_time=0.7)
            self.en("cap8")                                  # «la misma cuenta del capítulo ocho»
            self.play(FadeIn(c8), FadeIn(c8t), run_time=0.5)
            self.en("fxf")                                   # «frecuencia a frecuencia»
            self.play(FadeIn(barrido), run_time=0.2)
            self.play(barrido.animate(rate_func=linear).shift(RIGHT * 6.9), run_time=self.dur(1.8, 0.3))
            self.en("consensor")                             # «Con el sensor»
            self.pop(tm)
            self.en("mejor")                                 # «lo mejor que se puede conseguir»
            self.pop(sel)
            self.en("v686")                                  # «cero coma seis ocho seis»
            self.pop(v686)
            self.en("verdad")                                # «un filtro de verdad»
            self.play(FadeIn(ej), run_time=0.5)
            self.en("nover")                                 # «no puede ver el futuro»
            self.play(LaggedStart(*[FadeIn(c, scale=0.4) for c in cruces], lag_ratio=0.1), run_time=self.dur(1.0))
            self.en("deja")                                  # «la división deja de valer»
            self.play(Create(tachar(frac, ROJO)), run_time=0.4)
            self.en("proximo")                               # «En el próximo episodio»
            self.limpiar()
            self.pop(e4)
            self.en("titulo")                                # «el futuro no está disponible»
            self.pop(titulo)
