"""Escena 5 - Por que funciona: dos lecturas del filtro adaptado.

En frecuencia, H(e^jW) = S(e^-jW): el modulo acentua donde hay senal, la
fase cancela la fase de la senal para que todo llegue en fase a n=0. Y
sin suponer gaussianidad, Cauchy-Schwarz muestra que el adaptado maximiza
el SNR de salida, igualando el SNR de entrada.

    manim -pql s05_por_que.py PorQueFunciona
"""
from manim import *
import numpy as np
from comun import *


class PorQueFunciona(Scene):
    def construct(self):
        configurar()

        tit = titulo("¿Por qué funciona? Dos lecturas")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        Hz = MathTex(r"H(e^{j\Omega})=S(e^{-j\Omega})"
                     r"=|S(e^{j\Omega})|\,e^{-j\angle S(e^{j\Omega})}",
                     color=AZUL).scale(0.66)
        Hz.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(Write(Hz))
        self.wait(1.2)

        # ------------------------------------------------ el modulo
        mod_tit = subtitulo("el módulo: acentúa donde hay señal", scale=0.5,
                            color=VERDE)
        mod_tit.next_to(Hz, DOWN, buff=0.35)
        self.play(FadeIn(mod_tit))

        w = np.linspace(-np.pi, np.pi, 400)
        def Smag(x):
            return 1.0 + 1.6 * np.exp(-((x - 0.9) ** 2) / 0.12) \
                        + 1.6 * np.exp(-((x + 0.9) ** 2) / 0.12)

        ax_m, _ = ejes([-PI, PI, PI], [0, 3.2, 3.2], ancho=7.6, alto=2.2, tip=False)
        ax_m.next_to(mod_tit, DOWN, buff=0.3)
        curva_m = ax_m.plot(Smag, x_range=[-PI, PI, 0.01], color=VERDE,
                            stroke_width=3.5)
        area_m = ax_m.get_area(curva_m, x_range=(-PI, PI), color=VERDE,
                               opacity=0.14, stroke_width=0)
        lab_m = MathTex(r"|S(e^{j\Omega})|", color=VERDE).scale(0.5)
        lab_m.next_to(ax_m.c2p(0.9, Smag(0.9)), UP, buff=0.1)
        self.play(Create(ax_m), Create(curva_m), FadeIn(area_m), FadeIn(lab_m))
        n_ruido = nota("el ruido blanco es plano: donde $|S|$ es grande, "
                       "el SNR mejora", scale=0.42)
        n_ruido.next_to(ax_m, DOWN, buff=0.25)
        self.play(FadeIn(n_ruido))
        self.wait(1.8)
        self.play(FadeOut(VGroup(mod_tit, ax_m, curva_m, area_m, lab_m, n_ruido)))

        # ------------------------------------------------ la fase
        fase_tit = subtitulo("la fase: alinea todo en n = 0", scale=0.5,
                             color=MAGENTA)
        fase_tit.next_to(Hz, DOWN, buff=0.35)
        self.play(FadeIn(fase_tit))

        ax_f, lab_f = ejes([-3, 3, 6], [-1.6, 4.2, 5.8], ancho=7.6, alto=2.6,
                           x_label="n")
        ax_f.next_to(fase_tit, DOWN, buff=0.35)
        lab_f.next_to(ax_f.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_f), FadeIn(lab_f))

        freqs = [0.9, 1.6, 2.3]
        fases0 = [0.6, -1.9, 2.7]
        colores = [AMBAR, AZUL, MAGENTA]
        curvas_desfasadas = VGroup(*[
            ax_f.plot(lambda t, f=f, p=p: np.cos(f * t + p), x_range=[-3, 3, 0.02],
                      color=c, stroke_width=2.6)
            for f, p, c in zip(freqs, fases0, colores)
        ])
        self.play(*[Create(c) for c in curvas_desfasadas])
        n_desf = nota("cada componente de frecuencia llega con su propia fase",
                      scale=0.42)
        n_desf.next_to(ax_f, DOWN, buff=0.22)
        self.play(FadeIn(n_desf))
        self.wait(1.2)

        curvas_alineadas = VGroup(*[
            ax_f.plot(lambda t, f=f: np.cos(f * t), x_range=[-3, 3, 0.02],
                      color=c, stroke_width=2.6)
            for f, c in zip(freqs, colores)
        ])
        self.play(*[Transform(a, b) for a, b in
                    zip(curvas_desfasadas, curvas_alineadas)], run_time=1.6)
        suma = ax_f.plot(lambda t: sum(np.cos(f * t) for f in freqs),
                         x_range=[-3, 3, 0.02], color=TXT, stroke_width=4)
        self.play(Create(suma))
        pico = Dot(ax_f.c2p(0, sum(np.cos(0) for _ in freqs)), color=TXT,
                  radius=0.07)
        self.play(FadeIn(pico, scale=1.4))
        n_alin = nota("la fase de H cancela la de S: todas en fase en "
                      "n=0 → suma CONSTRUCTIVA", scale=0.44, color=MAGENTA)
        n_alin.move_to(n_desf)
        self.play(FadeOut(n_desf), FadeIn(n_alin))
        self.wait(2.0)
        self.play(FadeOut(VGroup(fase_tit, ax_f, lab_f, curvas_desfasadas,
                                 suma, pico, n_alin, Hz)))

        # ------------------------------------------------ sin gaussianidad
        cs_tit = Text("¿Y sin suponer que el ruido es gaussiano?",
                      color=TXT).scale(0.56)
        cs_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(cs_tit))
        pregunta = subtitulo("¿qué filtro LTI maximiza el SNR de salida?",
                             scale=0.5)
        pregunta.next_to(cs_tit, DOWN, buff=0.3)
        self.play(FadeIn(pregunta))
        self.wait(1.4)

        snr = MathTex(r"\text{SNR}_{out}=\frac{\big(\sum s[n]h[-n]\big)^2}"
                      r"{\sigma^2\sum h^2[-n]}", color=AZUL).scale(0.68)
        snr.next_to(pregunta, DOWN, buff=0.4)
        self.play(Write(snr))
        self.wait(1.2)
        self.play(FadeOut(VGroup(cs_tit, pregunta)),
                  snr.animate.scale(0.85).next_to(tit, DOWN, buff=0.5)
                  .set_x(0))

        cs = MathTex(r"\Big(\sum x[n]y[n]\Big)^2\leq"
                     r"\Big(\sum x^2[n]\Big)\Big(\sum y^2[n]\Big)",
                     color=VERDE).scale(0.68)
        cs.next_to(snr, DOWN, buff=0.45)
        cs_box = SurroundingRectangle(cs, color=VERDE, buff=0.22)
        self.play(Write(cs), Create(cs_box))
        n_cs = nota("Cauchy-Schwarz: igualdad sii $y[n]=K\\,x[n]$ "
                    "(vectores colineales)", scale=0.44)
        n_cs.next_to(cs_box, DOWN, buff=0.3)
        self.play(FadeIn(n_cs))
        self.wait(1.8)
        self.play(FadeOut(VGroup(cs, cs_box, n_cs)))

        cota = MathTex(r"\text{SNR}_{out}\leq\frac{E}{\sigma^2}=\text{SNR}_{in}",
                       color=VERDE).scale(0.75)
        cota.next_to(snr, DOWN, buff=0.45)
        self.play(Write(cota))
        n_igual = nota("con igualdad sii $h[-n]=K\\,s[n]$: otra vez el "
                       "filtro adaptado", scale=0.46)
        n_igual.next_to(cota, DOWN, buff=0.3)
        self.play(FadeIn(n_igual))
        self.wait(2.0)
        self.play(FadeOut(VGroup(snr, cota, n_igual)))

        # ------------------------------------------------ el angulo
        ang_tit = subtitulo("es un ángulo entre vectores", scale=0.5)
        ang_tit.next_to(tit, DOWN, buff=0.5).set_x(0)
        self.play(FadeIn(ang_tit))

        plano = Axes(x_range=[-0.3, 2.6, 1], y_range=[-0.3, 2.2, 1],
                    x_length=4.4, y_length=3.6,
                    axis_config={"color": INK, "stroke_width": 2,
                                "include_ticks": False})
        plano.next_to(ang_tit, DOWN, buff=0.4)
        vs = Arrow(plano.c2p(0, 0), plano.c2p(2.2, 1.3), color=AMBAR,
                  buff=0, stroke_width=3.5,
                  max_tip_length_to_length_ratio=0.1)
        vh = Arrow(plano.c2p(0, 0), plano.c2p(1.8, 1.9), color=AZUL,
                  buff=0, stroke_width=3.5,
                  max_tip_length_to_length_ratio=0.1)
        ls = MathTex("s", color=AMBAR).scale(0.55).next_to(vs.get_end(), DR, buff=0.05)
        lh = MathTex("h[-n]", color=AZUL).scale(0.5).next_to(vh.get_end(), UR, buff=0.05)
        self.play(Create(plano), GrowArrow(vs), FadeIn(ls))
        self.play(GrowArrow(vh), FadeIn(lh))
        formula_ang = MathTex(r"\text{SNR}_{out}=\text{SNR}_{in}\cos^2\theta",
                              color=TXT).scale(0.6)
        formula_ang.next_to(plano, RIGHT, buff=0.8)
        self.play(Write(formula_ang))
        self.wait(1.0)
        self.play(Rotate(vh, angle=-vh.get_angle() + vs.get_angle(),
                         about_point=plano.c2p(0, 0)), run_time=1.4)
        self.play(Transform(lh, MathTex(r"h[-n]=K\,s[n]", color=AZUL).scale(0.5)
                            .next_to(vs.get_end(), UR, buff=0.15)))
        maximo_ang = nota("colineales → θ=0 → máximo SNR posible",
                          scale=0.44, color=VERDE)
        maximo_ang.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(maximo_ang))
        self.wait(2.0)
        self.play(FadeOut(VGroup(ang_tit, plano, vs, vh, ls, lh, formula_ang,
                                 maximo_ang)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("El filtro adaptado tiene DOS justificaciones:",
                 color=INK).scale(0.54),
            Text("si el ruido es gaussiano, mínimo Pₑ.", color=AZUL).scale(0.56),
            Text("si solo es blanco, SNR máximo.", color=VERDE).scale(0.56),
            nota("y ese SNR máximo es exactamente el SNR de entrada: "
                 "no se pierde nada", scale=0.46),
        ).arrange(DOWN, buff=0.24)
        cierre.move_to(ORIGIN)
        for m in cierre:
            self.play(FadeIn(m, shift=UP * 0.1), run_time=0.6)
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
