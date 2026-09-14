"""Escena 7 - El filtro de Wiener causal: blanquear, resolver, deshacer.

Si el filtro tiene que ser causal, la ortogonalidad solo se puede pedir
para m >= 0, y eso rompe el truco de transformar los dos lados. La salida
es blanquear las mediciones con un factor espectral de fase minima,
resolver el problema facil y deshacer el blanqueo.

    manim -pql s07_causal.py WienerCausal
"""
from manim import *
import numpy as np
from comun import *


class WienerCausal(Scene):
    def construct(self):
        configurar()

        tit = titulo("Wiener causal: blanquear, resolver, deshacer")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ por que se rompe
        p1 = MathTex(r"h[m] * C_{xx}[m] = C_{yx}[m]",
                     r"\quad\text{solo para } m \ge 0", color=TXT).scale(0.7)
        p1[1].set_color(AMBAR)
        p1.next_to(tit, DOWN, buff=0.5)
        self.play(Write(p1))
        self.wait(1.0)

        roto = Text("y ese “solo m ≥ 0” arruina todo", color=ROJO).scale(0.56)
        roto.next_to(p1, DOWN, buff=0.4)
        self.play(FadeIn(roto, scale=1.1))
        n_roto = nota("la igualdad ya no vale en todo el eje:\n"
                      "no se pueden transformar los dos lados", scale=0.46)
        n_roto.next_to(roto, DOWN, buff=0.3)
        self.play(FadeIn(n_roto))
        self.wait(2.0)
        self.play(FadeOut(VGroup(roto, n_roto)))

        # ------------------------------------------------ el caso facil
        facil = VGroup(
            Text("El caso fácil: mediciones blancas", color=VERDE).scale(0.56),
            MathTex(r"C_{xx}[m]=\sigma_x^2\,\delta[m]"
                    r"\ \Rightarrow\ h[m]=\tfrac{1}{\sigma_x^2}\,C_{yx}[m]"
                    r"\ \ (m\ge0)", color=TXT).scale(0.6),
            nota("calculás la solución no causal y le cortás la cola:\n"
                 "los m < 0 no participan", scale=0.46),
        ).arrange(DOWN, buff=0.28)
        facil.next_to(p1, DOWN, buff=0.5)
        self.play(FadeIn(facil[0]))
        self.play(Write(facil[1]))
        self.play(FadeIn(facil[2]))
        self.wait(2.0)

        idea = Text("¿Y si las mediciones NO son blancas? Blanqueémoslas.",
                    color=AMBAR).scale(0.54)
        idea.next_to(facil, DOWN, buff=0.45)
        self.play(FadeIn(idea, shift=UP * 0.12))
        self.wait(1.8)
        self.play(FadeOut(VGroup(p1, facil, idea)))

        # ------------------------------------------------ factorizacion fase minima
        sub = Text("Factorización espectral de fase mínima",
                   color=TXT).scale(0.58)
        sub.next_to(tit, DOWN, buff=0.4)
        fac = MathTex(r"D_{xx}(z) = F(z)\,F(z^{-1})", color=AZUL).scale(0.8)
        fac.next_to(sub, DOWN, buff=0.32)
        self.play(FadeIn(sub), Write(fac))
        self.wait(0.8)

        # plano z: circulo unidad con polos/ceros de F adentro
        plano = Circle(radius=1.3, color=INK, stroke_width=2)
        ejx = Line(plano.get_left() + LEFT * 0.4, plano.get_right() + RIGHT * 0.4,
                   color=INK, stroke_width=1.5)
        ejy = Line(plano.get_bottom() + DOWN * 0.4, plano.get_top() + UP * 0.4,
                   color=INK, stroke_width=1.5)
        planoz = VGroup(plano, ejx, ejy)
        planoz.next_to(fac, DOWN, buff=0.5).shift(LEFT * 3.3)
        cu = MathTex(r"|z|=1", color=INK).scale(0.42).next_to(plano, UL, buff=0.02)

        cen = plano.get_center()

        def polo(dx, dy):
            p = cen + np.array([dx, dy, 0.0])
            return VGroup(
                Line(p + [-0.1, -0.1, 0], p + [0.1, 0.1, 0],
                     color=VERDE, stroke_width=3),
                Line(p + [-0.1, 0.1, 0], p + [0.1, -0.1, 0],
                     color=VERDE, stroke_width=3))

        polos_F = VGroup(polo(0.5, 0.28), polo(-0.42, -0.5))
        ceros_F = VGroup(
            Circle(radius=0.12, color=AZUL, stroke_width=3)
            .move_to(cen + np.array([0.1, 0.72, 0.0])))

        self.play(Create(planoz), FadeIn(cu))
        self.play(FadeIn(polos_F), FadeIn(ceros_F))
        n_fm = nota("F(z): todos los polos y ceros\nDENTRO del círculo unidad",
                    scale=0.46, color=VERDE)
        n_fm.next_to(planoz, DOWN, buff=0.3)
        self.play(FadeIn(n_fm))
        self.wait(1.6)

        props = VGroup(
            Text("– estable y causal", color=VERDE).scale(0.46),
            Text("– con inversa estable y causal", color=VERDE).scale(0.46),
            nota("existe si D_xx no se anula en ninguna banda\n"
                 "(condición de Paley–Wiener)", scale=0.42),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        props.next_to(planoz, RIGHT, buff=0.9)
        for m in props:
            self.play(FadeIn(m, shift=RIGHT * 0.12), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(VGroup(sub, fac, planoz, cu, polos_F, ceros_F,
                                 n_fm, props)))

        # ------------------------------------------------ la formula
        formula = MathTex(r"H(z)=\frac{1}{F(z)}"
                          r"\left[\frac{D_{yx}(z)}{F(z^{-1})}\right]_{+}",
                          color=AZUL).scale(0.95)
        formula.next_to(tit, DOWN, buff=0.7)
        self.play(Write(formula))
        self.play(Circumscribe(formula, color=AZUL, buff=0.2, run_time=1.4))
        self.wait(0.6)

        pasos = VGroup(
            VGroup(MathTex(r"\tfrac{1}{F(z^{-1})}", color=VERDE).scale(0.62),
                   Text("blanquear (la parte anticausal)",
                        color=INK).scale(0.46)).arrange(RIGHT, buff=0.3),
            VGroup(MathTex(r"[\ \cdot\ ]_{+}", color=AMBAR).scale(0.62),
                   Text("resolver el problema fácil: quedarse con lo causal",
                        color=INK).scale(0.46)).arrange(RIGHT, buff=0.3),
            VGroup(MathTex(r"\tfrac{1}{F(z)}", color=AZUL).scale(0.62),
                   Text("deshacer el blanqueo",
                        color=INK).scale(0.46)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        pasos.next_to(formula, DOWN, buff=0.55)
        der_izq = nota("se lee de derecha a izquierda", scale=0.44)
        der_izq.next_to(pasos, DOWN, buff=0.3)
        for m in pasos:
            self.play(FadeIn(m, shift=RIGHT * 0.15), run_time=0.7)
        self.play(FadeIn(der_izq))
        self.wait(2.2)
        self.play(FadeOut(VGroup(formula, pasos, der_izq)))

        # ------------------------------------------------ el precio de la causalidad
        precio = Text("El precio de la causalidad", color=TXT).scale(0.6)
        precio.next_to(tit, DOWN, buff=0.5)
        dmmse = MathTex(r"\Delta\text{MMSE}=\frac{1}{2\pi}\int_{-\pi}^{\pi}"
                        r"\left|\left[\frac{D_{yx}(e^{j\Omega})}{F(e^{-j\Omega})}"
                        r"\right]_{-}\right|^2 d\Omega", color=ROJO).scale(0.7)
        dmmse.next_to(precio, DOWN, buff=0.45)
        self.play(FadeIn(precio), Write(dmmse))
        self.wait(1.0)
        n_precio = nota("lo que perdés es exactamente lo que tiraste\n"
                        "al quedarte solo con la parte causal", scale=0.48)
        n_precio.next_to(dmmse, DOWN, buff=0.35)
        self.play(FadeIn(n_precio))
        self.wait(2.2)
        self.play(FadeOut(VGroup(precio, dmmse, n_precio)))

        # ------------------------------------------------ innovaciones
        innov = Text("La interpretación por innovaciones", color=TXT).scale(0.6)
        innov.next_to(tit, DOWN, buff=0.5)
        self.play(FadeIn(innov))

        desc = MathTex(r"x[n+1]=",
                       r"\underbrace{f_0\,w[n+1]}_{\text{lo nuevo}}",
                       r"+",
                       r"\underbrace{\sum_{j\le n} f_{n-j+1}\,w[j]}"
                       r"_{\text{lo que ya sé}}", color=TXT).scale(0.6)
        desc[1].set_color(MAGENTA)
        desc[3].set_color(VERDE)
        desc.next_to(innov, DOWN, buff=0.5)
        self.play(Write(desc))
        self.wait(1.2)

        b1 = nota("como 1/F(z) es causal, conocer x hasta n equivale a\n"
                  "conocer w hasta n  →  ese término lo sé entero",
                  scale=0.46, color=VERDE)
        b1.next_to(desc, DOWN, buff=0.4)
        self.play(FadeIn(b1))
        self.wait(1.8)
        b2 = nota("la innovación f₀·w[n+1] es blanca: no está correlacionada\n"
                  "con nada de lo que sé  →  imposible de predecir",
                  scale=0.46, color=MAGENTA)
        b2.next_to(b1, DOWN, buff=0.3)
        self.play(FadeIn(b2))
        self.wait(2.0)

        self.play(FadeOut(VGroup(desc, b1, b2)))
        res = MathTex(r"\hat{x}[n+1]=\sum_{j\le n} f_{n-j+1}\,w[j]"
                      r"\qquad \text{MMSE}=f_0^2", color=AZUL).scale(0.72)
        res.next_to(innov, DOWN, buff=0.6)
        self.play(Write(res))
        n_res = nota("la mejor predicción es tirar lo impredecible;\n"
                     "el error es la potencia de lo que tiraste", scale=0.48)
        n_res.next_to(res, DOWN, buff=0.35)
        self.play(FadeIn(n_res))
        self.wait(2.2)
        self.play(FadeOut(VGroup(innov, res, n_res)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("El filtro de fase mínima separa la señal en dos:",
                 color=INK).scale(0.56),
            Text("lo que ya sabías   y   lo genuinamente nuevo.",
                 color=AZUL).scale(0.6),
            nota("blanquear, resolver, deshacer: esa es toda la receta",
                 scale=0.5),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
