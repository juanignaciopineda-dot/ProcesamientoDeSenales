"""Escena 8 - Discriminacion entre senales: on-off contra antipodal.

Con M senales, un banco de M adaptados y se elige la salida mas grande.
El caso binario se reduce a un unico adaptado a la senal diferencia. Por
Cauchy-Schwarz, la mejor eleccion (misma potencia de pico) es la
antipodal: duplica el argumento de la Q, cuadruplicando el SNR efectivo.

    manim -pql s08_antipodal.py OnOffAntipodal
"""
from manim import *
import numpy as np
from comun import *


class OnOffAntipodal(Scene):
    def construct(self):
        configurar()

        tit = titulo("Discriminación entre señales")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        planteo = MathTex(r"H_i:\ R[n]=s_i[n]+W[n],\quad i=0,1,\dots,M-1",
                          color=TXT).scale(0.62)
        planteo.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(Write(planteo))
        self.wait(1.0)

        regla = MathTex(r"\text{elegir }i\text{ que maximiza }\ "
                        r"\sum_n r[n]s_i[n]+\sigma^2\ln P(H_i)-\frac{E_i}{2}",
                        color=AZUL).scale(0.6)
        regla.next_to(planteo, DOWN, buff=0.35)
        self.play(Write(regla))
        self.wait(1.4)

        # banco de filtros
        r_lbl = MathTex("r[n]", color=INK).scale(0.45)
        bancos = VGroup(*[
            bloque(fr"\text{{adap.}} s_{i}", color=AZUL, ancho=1.7, alto=0.7,
                  scale=0.32)
            for i in range(3)
        ])
        bancos.arrange(DOWN, buff=0.22)
        max_b = bloque(r"\max_i", color=VERDE, ancho=1.3, alto=0.9, scale=0.5)
        grupo = VGroup(r_lbl, bancos, max_b).arrange(RIGHT, buff=0.7)
        grupo.next_to(regla, DOWN, buff=0.5)
        self.play(FadeIn(r_lbl), FadeIn(bancos))
        self.play(FadeIn(max_b))
        n_simple = nota("si todas las energías y a priori son iguales:\n"
                        "elegí el $i$ cuyo adaptado dé la salida más grande",
                        scale=0.42)
        n_simple.next_to(grupo, DOWN, buff=0.35)
        self.play(FadeIn(n_simple))
        self.wait(2.0)
        self.play(FadeOut(VGroup(planteo, regla, grupo, n_simple)))

        # ------------------------------------------------ el caso binario
        bin_tit = Text("El caso binario: un único filtro", color=TXT).scale(0.58)
        bin_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(bin_tit))

        g_bin = MathTex(r"g=\sum_n r[n]\big(s_1[n]-s_0[n]\big)"
                        r"\underset{H_0}{\overset{H_1}{\gtrless}}"
                        r"\sigma^2\ln\frac{p_0}{p_1}+\frac{E_1-E_0}{2}",
                        color=AZUL).scale(0.58)
        g_bin.next_to(bin_tit, DOWN, buff=0.4)
        self.play(Write(g_bin))
        n_bin = nota("adaptado a la señal DIFERENCIA: lo que importa no es "
                     "cada señal, es en qué se distinguen", scale=0.44)
        n_bin.next_to(g_bin, DOWN, buff=0.3)
        self.play(FadeIn(n_bin))
        self.wait(2.0)
        self.play(FadeOut(VGroup(bin_tit, g_bin, n_bin)))

        # ------------------------------------------------ el diseno optimo
        dis_tit = Text("Diseño óptimo: energías iguales, a priori iguales",
                       color=TXT).scale(0.54)
        dis_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(dis_tit))

        Pe = MathTex(r"P_e=Q\!\left(\sqrt{\frac{\mathcal E-X}{2\sigma^2}}\right)"
                     r"\qquad X=\sum_n s_0[n]s_1[n]", color=TXT).scale(0.62)
        Pe.next_to(dis_tit, DOWN, buff=0.35)
        self.play(Write(Pe))
        n_X = nota("minimizar $P_e$ pide $X$ lo más negativo posible;\n"
                   "por Cauchy-Schwarz, $X\\geq-\\mathcal E$", scale=0.44)
        n_X.next_to(Pe, DOWN, buff=0.28)
        self.play(FadeIn(n_X))
        self.wait(1.6)

        antip = MathTex(r"s_1[n]=-s_0[n]\quad(\text{señalización ANTIPODAL})",
                        color=VERDE).scale(0.62)
        antip.next_to(n_X, DOWN, buff=0.35)
        self.play(Write(antip))
        self.wait(1.8)
        self.play(FadeOut(VGroup(dis_tit, Pe, n_X, antip)))

        # ------------------------------------------------ constelaciones
        const_tit = Text("On-off contra antipodal", color=TXT).scale(0.58)
        const_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(const_tit))

        eje = NumberLine(x_range=[-2.2, 2.2, 1], length=6.5, color=INK,
                        include_tip=False)
        eje.next_to(const_tit, DOWN, buff=0.7)
        self.play(Create(eje))

        # on-off: 0 y sqrt(E)
        E_sqrt = 1.5
        oo0 = Dot(eje.n2p(0), color=AMBAR, radius=0.08)
        oo1 = Dot(eje.n2p(E_sqrt), color=AMBAR, radius=0.08)
        oo_lbl = MathTex(r"\text{on-off: } 0,\ \sqrt E", color=AMBAR).scale(0.5)
        oo_lbl.next_to(eje, UP, buff=0.35)
        self.play(FadeIn(oo0), FadeIn(oo1), FadeIn(oo_lbl))
        dist_oo = Line(eje.n2p(0), eje.n2p(E_sqrt), color=AMBAR, stroke_width=2)
        self.play(Create(dist_oo))
        self.wait(1.0)
        self.play(FadeOut(VGroup(oo0, oo1, oo_lbl, dist_oo)))

        an0 = Dot(eje.n2p(-E_sqrt), color=VERDE, radius=0.08)
        an1 = Dot(eje.n2p(E_sqrt), color=VERDE, radius=0.08)
        an_lbl = MathTex(r"\text{antipodal: } -\sqrt E,\ +\sqrt E",
                         color=VERDE).scale(0.5)
        an_lbl.next_to(eje, UP, buff=0.35)
        self.play(FadeIn(an0), FadeIn(an1), FadeIn(an_lbl))
        dist_an = Line(eje.n2p(-E_sqrt), eje.n2p(E_sqrt), color=VERDE,
                      stroke_width=2)
        self.play(Create(dist_an))
        n_dob = nota("el doble de distancia, con la MISMA potencia de pico",
                     scale=0.46)
        n_dob.next_to(eje, DOWN, buff=0.5)
        self.play(FadeIn(n_dob))
        self.wait(2.0)
        self.play(FadeOut(VGroup(const_tit, eje, an0, an1, an_lbl, dist_an,
                                 n_dob)))

        # ------------------------------------------------ curvas de Pe
        curvas_tit = Text("El precio y el premio, en números", color=TXT).scale(0.56)
        curvas_tit.next_to(tit, DOWN, buff=0.4).set_x(0)
        self.play(FadeIn(curvas_tit))

        snr_db = np.linspace(-4, 10, 300)
        snr_lin = 10 ** (snr_db / 10)
        pe_oo = np.array([Q(np.sqrt(s) / 2) for s in snr_lin])
        pe_an = np.array([Q(np.sqrt(s)) for s in snr_lin])

        ax_pe, lab_pe = ejes([-4, 10, 14], [0, 0.5, 0.5], ancho=8.0, alto=2.8,
                             x_label=r"\text{SNR (dB)}")
        ax_pe.next_to(curvas_tit, DOWN, buff=0.45)
        lab_pe.next_to(ax_pe.x_axis.get_end(), DR, buff=0.1)
        self.play(Create(ax_pe), FadeIn(lab_pe))

        c_oo = linea_datos(ax_pe, snr_db, pe_oo, color=AMBAR, ancho=3.2)
        c_an = linea_datos(ax_pe, snr_db, pe_an, color=VERDE, ancho=3.2)
        l_oo = MathTex(r"\text{on-off}", color=AMBAR).scale(0.48)
        l_oo.next_to(ax_pe.c2p(6, np.interp(6, snr_db, pe_oo)), UR, buff=0.05)
        l_an = MathTex(r"\text{antipodal}", color=VERDE).scale(0.48)
        l_an.next_to(ax_pe.c2p(2, np.interp(2, snr_db, pe_an)), DR, buff=0.15)
        self.play(Create(c_oo), FadeIn(l_oo))
        self.play(Create(c_an), FadeIn(l_an))

        despl = DoubleArrow(ax_pe.c2p(4, 0.16), ax_pe.c2p(10, 0.16),
                            color=INK, stroke_width=2.5, buff=0,
                            max_tip_length_to_length_ratio=0.06)
        despl_lbl = MathTex(r"6\text{ dB}", color=INK).scale(0.45)
        despl_lbl.next_to(despl, UP, buff=0.08)
        self.play(Create(despl), FadeIn(despl_lbl))
        n_6db = nota("antipodal corrida 6 dB respecto de on-off, con la "
                     "misma potencia de PICO", scale=0.44)
        n_6db.next_to(ax_pe, DOWN, buff=0.3)
        self.play(FadeIn(n_6db))
        self.wait(2.2)
        self.play(FadeOut(VGroup(curvas_tit, ax_pe, lab_pe, c_oo, c_an, l_oo,
                                 l_an, despl, despl_lbl, n_6db)))

        # ------------------------------------------------ cierre del capitulo
        cierre = VGroup(
            Text("Es gratis en potencia de pico:", color=INK).scale(0.54),
            Text("solo sube la potencia media.", color=AMBAR).scale(0.56),
            Text("Por eso casi todo sistema digital usa antipodal.",
                 color=VERDE).scale(0.6),
        ).arrange(DOWN, buff=0.26)
        cierre.move_to(ORIGIN)
        for m in cierre:
            self.play(FadeIn(m, shift=UP * 0.1), run_time=0.6)
        self.wait(2.4)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
