"""Escena 4 - El filtro adaptado: h[k] = s[-k].

g = suma r[n]s[n] es lineal en las mediciones, y todo lo lineal se puede
calcular con un filtro LTI. Comparando con la salida de un filtro se ve
que h[k] = s[-k]: la respuesta al impulso es la señal objetivo invertida
en el tiempo. Muestreando en n=0 se obtiene R_ss[0] = E, el maximo de la
autocorrelacion.

    manim -pql s04_filtro_adaptado.py FiltroAdaptado
"""
from manim import *
import numpy as np
from comun import *


class FiltroAdaptado(Scene):
    def construct(self):
        configurar()

        tit = titulo("El filtro adaptado: h[k] = s[−k]")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        lineal = MathTex(r"g=\sum_k r[k]\,s[k]", color=TXT).scale(0.68)
        lineal.next_to(tit, DOWN, buff=0.4).set_x(0)
        n_lineal = nota("es LINEAL en las mediciones → se puede calcular "
                        "con un filtro LTI", scale=0.46)
        n_lineal.next_to(lineal, DOWN, buff=0.25)
        self.play(Write(lineal), FadeIn(n_lineal))
        self.wait(1.4)

        salida = MathTex(r"g[0]=\sum_k r[k]\,h[-k]", color=AZUL).scale(0.68)
        salida.next_to(n_lineal, DOWN, buff=0.4)
        self.play(Write(salida))
        n_sal = nota("salida de un filtro h[·] con entrada r[·], "
                     "muestreada en n=0", scale=0.44)
        n_sal.next_to(salida, DOWN, buff=0.2)
        self.play(FadeIn(n_sal))
        self.wait(1.6)

        comparar = Text("comparando término a término...", color=INK).scale(0.48)
        comparar.next_to(n_sal, DOWN, buff=0.35)
        self.play(FadeIn(comparar))
        self.wait(0.8)
        self.play(FadeOut(VGroup(lineal, n_lineal, salida, n_sal, comparar)))

        resultado = MathTex(r"h[k]=s[-k]", color=VERDE).scale(0.95)
        resultado.next_to(tit, DOWN, buff=0.6).set_x(0)
        caja = SurroundingRectangle(resultado, color=VERDE, buff=0.3)
        self.play(Write(resultado), Create(caja))
        n_res = nota("la respuesta al impulso es la señal objetivo "
                     "INVERTIDA en el tiempo — el \"filtro adaptado\"",
                     scale=0.48)
        n_res.next_to(caja, DOWN, buff=0.35)
        self.play(FadeIn(n_res))
        self.wait(2.0)
        self.play(FadeOut(VGroup(resultado, caja, n_res)))

        # ------------------------------------------------ s[n] y su espejo h[k]
        n = np.arange(-2, 8)
        vals = [0.5, 1.4, 1.9, 1.6, 0.9, 0.3]
        s = np.zeros_like(n, dtype=float)
        for i, v in enumerate(vals):
            s[np.where(n == i)[0][0]] = v

        ax_s, _ = ejes([-2, 7, 9], [-0.3, 2.4, 3], ancho=5.6, alto=2.0, tip=False)
        ax_h, _ = ejes([-7, 2, 9], [-0.3, 2.4, 3], ancho=5.6, alto=2.0, tip=False)
        cols = VGroup(
            VGroup(MathTex("s[n]", color=AMBAR).scale(0.5), ax_s).arrange(DOWN, buff=0.15),
            VGroup(MathTex("h[k]=s[-k]", color=MAGENTA).scale(0.5), ax_h).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=0.7)
        cols.next_to(tit, DOWN, buff=0.5).set_x(0)

        st_s = stem(ax_s, n, s, color=AMBAR, ancho=2.8, radio=0.04)
        st_h = stem(ax_h, -n, s, color=MAGENTA, ancho=2.8, radio=0.04)
        self.play(Create(cols[0][0]), Create(st_s))
        self.wait(0.3)
        self.play(TransformFromCopy(st_s, st_h), FadeIn(cols[1][0]))
        self.wait(0.4)
        self.play(Create(cols[0][1]), Create(cols[1][1]))
        self.wait(1.4)
        self.play(FadeOut(VGroup(cols, st_s, st_h)))

        # ------------------------------------------------ convolucion animada
        conv_tit = Text("Deslizando h sobre s: sale la autocorrelación",
                        color=TXT).scale(0.54)
        conv_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(conv_tit))

        ax_g, lab_g = ejes([-6, 6, 12], [-0.5, 10, 10.5], ancho=8.2, alto=2.6,
                           x_label="n")
        ax_g.next_to(conv_tit, DOWN, buff=0.45)
        lab_g.next_to(ax_g.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_g), FadeIn(lab_g))

        # R_ss[m] = suma_k s[k] s[k-m], calculada directo sobre el array s
        lags = np.arange(-6, 7)
        Rss = np.zeros_like(lags, dtype=float)
        for i, m in enumerate(lags):
            acc = 0.0
            for j, k in enumerate(n):
                idx = np.where(n == k - m)[0]
                if len(idx):
                    acc += s[j] * s[idx[0]]
            Rss[i] = acc

        tracker = ValueTracker(lags[0])
        curva_g = VMobject(color=AZUL, stroke_width=3.5)

        def actualizar_curva(mob):
            k = tracker.get_value()
            hechos = lags[lags <= k + 1e-6]
            if len(hechos) < 2:
                mob.set_points([])
                return
            pts = [ax_g.c2p(m, Rss[i]) for i, m in enumerate(lags) if m <= k + 1e-6]
            mob.set_points_as_corners(pts)

        curva_g.add_updater(actualizar_curva)
        self.add(curva_g)

        marca = always_redraw(lambda: Dot(
            ax_g.c2p(tracker.get_value(),
                    Rss[np.argmin(np.abs(lags - tracker.get_value()))]),
            color=AZUL, radius=0.06))
        self.add(marca)

        etiqueta_g = MathTex(r"g[n]=R_{ss}[n]", color=AZUL).scale(0.55)
        etiqueta_g.next_to(ax_g, UP, buff=0.12).align_to(ax_g, LEFT)
        self.play(FadeIn(etiqueta_g))

        self.play(tracker.animate.set_value(lags[-1]), run_time=3.5,
                  rate_func=linear)
        curva_g.clear_updaters()
        self.wait(0.4)

        maximo = ax_g.c2p(0, Rss[np.where(lags == 0)[0][0]])
        pico = DashedLine(ax_g.c2p(0, 0), maximo, color=VERDE, stroke_width=3)
        pico_lbl = MathTex(r"R_{ss}[0]=E", color=VERDE).scale(0.5)
        pico_lbl.next_to(maximo, UP, buff=0.12)
        self.play(Create(pico), FadeIn(pico_lbl))
        n_max = nota("máximo en n=0: la contribución de la señal es máxima ahí",
                     scale=0.44)
        n_max.next_to(ax_g, DOWN, buff=0.3)
        self.play(FadeIn(n_max))
        self.wait(2.0)
        self.play(FadeOut(VGroup(conv_tit, ax_g, lab_g, curva_g, marca,
                                 etiqueta_g, pico, pico_lbl, n_max)))

        # ------------------------------------------------ diagrama de bloques
        diag_tit = Text("El detector completo", color=TXT).scale(0.58)
        diag_tit.next_to(tit, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(diag_tit))

        r_lbl = MathTex("r[n]", color=INK).scale(0.55)
        adap = bloque(r"h[k]=s[-k]", color=AZUL, ancho=2.4, alto=0.9, scale=0.42)
        mues = bloque(r"n=0", color=AMBAR, ancho=1.5, alto=0.9, scale=0.42)
        comp = bloque(r"\gtrless\gamma", color=VERDE, ancho=1.5, alto=0.9, scale=0.5)
        dec = MathTex(r"\text{`}H_1\text{'}\ /\ \text{`}H_0\text{'}",
                     color=TXT).scale(0.5)
        cadena = VGroup(r_lbl, adap, mues, comp, dec).arrange(RIGHT, buff=0.6)
        cadena.next_to(diag_tit, DOWN, buff=0.6)
        flechas = VGroup(*[
            flecha(cadena[i].get_right(), cadena[i + 1].get_left())
            for i in range(len(cadena) - 1)
        ])
        self.play(FadeIn(r_lbl), FadeIn(adap))
        self.play(GrowArrow(flechas[0]))
        self.play(FadeIn(mues))
        self.play(GrowArrow(flechas[1]))
        self.play(FadeIn(comp))
        self.play(GrowArrow(flechas[2]))
        self.play(FadeIn(dec))
        self.play(GrowArrow(flechas[3]))
        self.wait(2.0)
        self.play(FadeOut(VGroup(diag_tit, cadena, flechas)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("El test óptimo es un filtro LTI:", color=INK).scale(0.56),
            Text("correlacionar con la señal buscada.", color=AZUL).scale(0.6),
            nota("filtrar, muestrear en n=0, comparar con γ", scale=0.48),
        ).arrange(DOWN, buff=0.28)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.4)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
