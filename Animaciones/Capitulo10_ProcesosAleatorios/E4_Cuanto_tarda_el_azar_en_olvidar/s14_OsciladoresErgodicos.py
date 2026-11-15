"""Escena 14 — OsciladoresErgodicos: el promedio temporal de un coseno es 0 y coincide con la media del ensemble."""
from comun.escena import *


def area_entre(L: Lienzo, a: float, b: float, color, n: int = 40) -> Polygon:
    """Área entre el coseno (período 1) y la línea base, entre los instantes a y b."""
    t = np.linspace(a, b, n)
    v = np.cos(2 * np.pi * t)
    pts = [L.p(a, 0)] + [L.p(ti, vi) for ti, vi in zip(t, v)] + [L.p(b, 0)]
    return Polygon(*pts, color=color, stroke_width=0).set_fill(color, 0.55)


class OsciladoresErgodicos(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        cc = CuatroCosenos(ancho=9.0, paso=1.5, amp=0.55, t_rango=(-0.25, 1.75), centro=(0.8, -0.1))
        L = Lienzo(ancho=9.6, alto=2.6, t_rango=(-0.25, 1.75), v_max=1.3, centro=(0, 0.6))
        elegido = coseno(L, 0, 1, SENAL, 5)
        base = L.base()
        flecha_h = Arrow(L.p(-0.25, -1.3), L.p(1.75, -1.3), color=VERDE, buff=0, stroke_width=5)
        banda = Rectangle(width=float(L.x(1) - L.x(0)), height=2.8, color=AMBAR, stroke_width=0).set_fill(AMBAR, 0.1)
        banda.move_to([float((L.x(0) + L.x(1)) / 2), 0.6, 0])
        t_per = etiqueta("un período", AMBAR, 0.5).next_to(banda, UP, buff=0.05)
        areas_v = VGroup(area_entre(L, 0, 0.25, VERDE), area_entre(L, 0.75, 1.0, VERDE))
        area_r = area_entre(L, 0.25, 0.75, ROJO)
        t_cero = MathTex(r"\text{promedio temporal}=0", color=VERDE).scale(1.0).move_to([-3.4, -2.6, 0])
        t_ens = MathTex(r"=\ \text{media del ensemble}\ =\ 0", color=AMBAR).scale(1.0).next_to(t_cero, RIGHT, buff=0.3)
        ok = tilde(VERDE, 0.6).move_to([5.9, -2.6, 0])
        w_corr = etiqueta("ergódico en correlación", AMBAR, 0.8, BOLD).move_to([0, 3.4, 0])
        copia = coseno(L, -72, 1, RUIDO, 4)
        copia.set_stroke(opacity=0.9)
        f_prod = MathTex(r"x(t)\cdot x(t-\tau)", color=TXT).scale(1.0).move_to([-3.6, -3.4, 0])
        cont = Arrow(L.p(-0.25, -1.3), L.p(1.75, -1.3), color=AMBAR, buff=0, stroke_width=5)
        f_r = MathTex(r"\to\ R_{XX}(\tau)", color=AMBAR).scale(1.2).move_to([1.2, -3.4, 0])

        with self.narrar("b1"):
            # «los cuatro osciladores»
            self.en("cuatro")
            self.play(FadeIn(cc), run_time=self.dur(1.0))

            # «Coge uno cualquiera»
            self.en("uno")
            self.play(*[FadeOut(c) for c in cc.curvas[1:]], *[FadeOut(b) for b in cc.bases[1:]],
                      FadeOut(cc.rotulos), ReplacementTransform(cc.curvas[0], elegido),
                      ReplacementTransform(cc.bases[0], base), run_time=self.dur(1.0))

            # «a lo largo del tiempo»
            self.en("largo")
            self.play(Create(flecha_h), run_time=self.dur(1.2))

            # «En cada período»
            self.en("periodo")
            self.play(FadeIn(banda), FadeIn(t_per), run_time=self.dur(0.6))

            # «por encima del cero»
            self.en("encima")
            self.play(FadeIn(areas_v), run_time=self.dur(0.7))

            # «por debajo»
            self.en("debajo")
            self.play(FadeIn(area_r), run_time=self.dur(0.7))

            # «las áreas se cancelan»
            self.en("cancelan")
            self.play(areas_v.animate.set_fill(VERDE, 0.85), area_r.animate.set_fill(ROJO, 0.85), run_time=self.dur(0.4))
            self.play(Indicate(area_r, color=ROJO, scale_factor=1.05), run_time=self.dur(0.6))

            # «el promedio temporal es cero»
            self.en("cero")
            self.pop(t_cero)

            # «La media del ensemble también era cero»
            self.en("media_ens")
            self.play(Write(t_ens), run_time=self.dur(1.2))

            # «Coinciden»
            self.en("coinciden")
            self.pop(ok)

            # «ergodicidad en correlación»
            self.en("en_corr")
            self.play(FadeOut(VGroup(banda, t_per, areas_v, area_r, flecha_h, t_cero, t_ens, ok)), run_time=0.3)
            self.pop(w_corr)

            # «promediar en el tiempo»
            self.en("prom_t")
            self.play(Create(cont), run_time=self.dur(1.2))

            # «su copia retrasada»
            self.en("copia")
            self.play(Create(copia), run_time=self.dur(0.8))
            self.play(FadeIn(f_prod), run_time=0.4)

            # «da la autocorrelación»
            self.en("autocorr")
            self.pop(f_r)
        self.wait(1.0)
        self.limpiar()
