"""Escena 12 — La probabilidad de un intervalo es el área bajo la densidad (la integral)."""
from comun.escena import *


class AreaBajoLaCurva(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        c = Curva(lambda x: float(gaussiana(x)), x_rango=(-4, 4), y_max=0.5, ancho=9.5, alto=3.8,
                  x_label="x", y_label="f_X(x)").move_to([0, -0.8, 0])
        ax, a, b = c.ejes, -0.8, 1.2
        self.add(c.ejes, c.etiquetas, c.grafica)

        with self.narrar("b1"):
            self.en("entre")                                  # «entre a y b»
            va = DashedLine(ax.c2p(a, 0), ax.c2p(a, float(gaussiana(a))), color=AMBAR, stroke_width=3)
            vb = DashedLine(ax.c2p(b, 0), ax.c2p(b, float(gaussiana(b))), color=VERDE, stroke_width=3)
            ta = formula("a", colores={0: AMBAR}).next_to(ax.c2p(a, 0), DOWN, buff=0.15)
            tb = formula("b", colores={0: VERDE}).next_to(ax.c2p(b, 0), DOWN, buff=0.15)
            self.play(Create(va), Create(vb), FadeIn(ta), FadeIn(tb), run_time=self.dur(0.8))
            self.en("area")                                   # «el área bajo la densidad»
            area = c.area(a, b, AMBAR, 0.5)
            self.play(FadeIn(area), run_time=self.dur(0.8))
            self.en("valores")                                # «entre el valor de a y el valor de b»
            self.play(ta.animate(rate_func=there_and_back).scale(1.6), tb.animate(rate_func=there_and_back).scale(1.6),
                      run_time=self.dur(0.8))
            self.en("imagina")                                # «Imagina el área cortada»
            self.play(area.animate(rate_func=there_and_back).set_fill(AMBAR, 0.9), run_time=self.dur(0.8))
            self.en("rectangulos")                            # «rectángulos muy finos»
            r1 = ax.get_riemann_rectangles(c.grafica, x_range=[a, b], dx=0.25, color=AMBAR, fill_opacity=0.6,
                                           stroke_width=1.5, stroke_color=FONDO)
            self.play(FadeOut(area), FadeIn(r1), run_time=self.dur(0.8))
            self.en("sumados")                                # «y sumados»
            suma = formula(r"\sum", "f(x_i)", r"\,\Delta x", escala=1.1, colores={0: AMBAR}).move_to([-4.2, 3.2, 0])
            self.play(Write(suma), run_time=self.dur(1.0))
            self.en("finos")                                  # «infinitamente finos»
            r2 = ax.get_riemann_rectangles(c.grafica, x_range=[a, b], dx=0.08, color=AMBAR, fill_opacity=0.6,
                                           stroke_width=1, stroke_color=FONDO)
            r3 = ax.get_riemann_rectangles(c.grafica, x_range=[a, b], dx=0.02, color=AMBAR, fill_opacity=0.6,
                                           stroke_width=0.3, stroke_color=AMBAR)
            self.play(ReplacementTransform(r1, r2), run_time=self.dur(0.9))
            self.play(ReplacementTransform(r2, r3), run_time=self.dur(0.9))
            self.en("integral")                               # «integral»
            pal = Text("Integral = área", color=AMBAR, weight=BOLD).scale(0.65).move_to([-4.9, 3.4, 0])
            self.play(FadeOut(suma), run_time=0.25)
            self.pop(pal)
            self.en("formula")                                # «la integral de la densidad»
            f = formula("P", "(", "a", "<", "X", r"\le", "b", ")", "=", r"\int_a^b", "f_X(x)", r"\,dx",
                        escala=0.95, colores={2: AMBAR, 6: VERDE, 9: AMBAR}).move_to([2.2, 3.3, 0])
            self.play(LaggedStart(*[Write(p) for p in f], lag_ratio=0.15), run_time=self.dur(2.4))
            self.en("limites")                                # «entre el valor de a y el valor de b»
            self.play(f[2].animate(rate_func=there_and_back).scale(1.6), f[6].animate(rate_func=there_and_back).scale(1.6),
                      run_time=self.dur(0.8))
        self.wait(1.0)
        self.limpiar()
