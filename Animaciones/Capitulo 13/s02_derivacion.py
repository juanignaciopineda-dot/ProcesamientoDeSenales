"""Escena 2 - La derivacion: de la regla MAP a un solo numero.

Senal conocida en ruido gaussiano i.i.d. La regla MAP, tras tomar ln y
desarrollar el cuadrado, se reduce a comparar g = suma r[n]s[n] contra un
umbral. El paso clave: los terminos suma r^2[n] son iguales a los dos
lados y se cancelan.

    manim -pql s02_derivacion.py Derivacion
"""
from manim import *
import numpy as np
from comun import *


class Derivacion(Scene):
    def construct(self):
        configurar()

        tit = titulo("De la regla MAP a un solo número")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        hip = VGroup(
            MathTex(r"H_0:\ R[n]=W[n]", color=AZUL).scale(0.6),
            MathTex(r"H_1:\ R[n]=s[n]+W[n]", color=VERDE).scale(0.6),
        ).arrange(RIGHT, buff=0.8)
        hip.next_to(tit, DOWN, buff=0.35).set_x(0)
        n_hip = nota("$s[n]$ determinística y conocida; $W[n]$ gaussiano i.i.d., "
                     "media $0$, varianza $\\sigma^2$", scale=0.42)
        n_hip.next_to(hip, DOWN, buff=0.2).set_x(0)
        self.play(FadeIn(hip), FadeIn(n_hip))
        self.wait(1.4)
        self.play(VGroup(hip, n_hip).animate.scale(0.82)
                  .next_to(tit, DOWN, buff=0.3).set_x(0))

        # ------------------------------------------------ densidades conjuntas
        dens = MathTex(
            r"f(\mathbf r|H_0)=\frac{1}{(2\pi\sigma^2)^{L/2}}"
            r"\exp\!\Big(-\sum_n \frac{r^2[n]}{2\sigma^2}\Big)"
            r"\qquad{}"
            r"f(\mathbf r|H_1)=\frac{1}{(2\pi\sigma^2)^{L/2}}"
            r"\exp\!\Big(-\sum_n \frac{(r[n]-s[n])^2}{2\sigma^2}\Big)",
            color=TXT).scale(0.5)
        dens.next_to(n_hip, DOWN, buff=0.4)
        self.play(Write(dens))
        self.wait(1.6)

        # ------------------------------------------------ tomar ln
        paso_ln = Text("tomamos ln de la regla MAP; las constantes "
                       "(2πσ²)^(-L/2) se cancelan", color=INK).scale(0.44)
        paso_ln.next_to(dens, DOWN, buff=0.35)
        self.play(FadeIn(paso_ln))
        self.wait(1.2)

        ln_regla = MathTex(
            r"\ln p_1-\sum_n\frac{(r[n]-s[n])^2}{2\sigma^2}"
            r"\underset{H_0}{\overset{H_1}{\gtrless}}"
            r"\ln p_0 - \sum_n\frac{r^2[n]}{2\sigma^2}",
            color=AZUL).scale(0.62)
        ln_regla.next_to(paso_ln, DOWN, buff=0.35)
        self.play(Write(ln_regla))
        self.wait(1.8)
        self.play(FadeOut(VGroup(hip, n_hip, dens, paso_ln)),
                  ln_regla.animate.scale(0.9).next_to(tit, DOWN, buff=0.5)
                  .set_x(0))

        # ------------------------------------------------ desarrollar el cuadrado
        desarrollo = Text("desarrollamos (r[n]−s[n])² = r²[n] − 2r[n]s[n] + s²[n]",
                          color=INK).scale(0.46)
        desarrollo.next_to(ln_regla, DOWN, buff=0.4)
        self.play(FadeIn(desarrollo))
        self.wait(1.0)

        expandida = MathTex(
            r"\ln p_1", r"-\sum_n\frac{",
            r"r^2[n]", r"-2r[n]s[n]+s^2[n]",
            r"}{2\sigma^2}",
            r"\underset{H_0}{\overset{H_1}{\gtrless}}",
            r"\ln p_0 - \sum_n\frac{", r"r^2[n]", r"}{2\sigma^2}",
            color=TXT).scale(0.56)
        expandida.next_to(ln_regla, DOWN, buff=0.75)
        self.play(Write(expandida))
        self.wait(1.2)

        # marcar los dos terminos r^2[n] que se cancelan
        r2_izq = expandida[2]
        r2_der = expandida[7]
        self.play(r2_izq.animate.set_color(ROJO),
                  r2_der.animate.set_color(ROJO))
        tacha_izq = Line(r2_izq.get_left() + LEFT * 0.03,
                         r2_izq.get_right() + RIGHT * 0.03,
                         color=ROJO, stroke_width=3.5)
        tacha_der = Line(r2_der.get_left() + LEFT * 0.03,
                         r2_der.get_right() + RIGHT * 0.03,
                         color=ROJO, stroke_width=3.5)
        self.play(Create(tacha_izq), Create(tacha_der))
        n_cancela = nota("son idénticos a los dos lados: se cancelan",
                         scale=0.44, color=ROJO)
        n_cancela.next_to(expandida, DOWN, buff=0.35)
        self.play(FadeIn(n_cancela))
        self.wait(1.8)
        self.play(FadeOut(VGroup(ln_regla, desarrollo, expandida, tacha_izq,
                                 tacha_der, n_cancela)))

        # ------------------------------------------------ reagrupar
        reagrupada = MathTex(
            r"\ln p_1+\sum_n\frac{2r[n]s[n]-s^2[n]}{2\sigma^2}"
            r"\underset{H_0}{\overset{H_1}{\gtrless}}\ln p_0",
            color=AZUL).scale(0.66)
        reagrupada.next_to(tit, DOWN, buff=0.6).set_x(0)
        self.play(Write(reagrupada))
        n_reagr = nota("multiplicando por $\\sigma^2$ y pasando todo lo que "
                       "no depende de $\\mathbf r$ a la derecha", scale=0.46)
        n_reagr.next_to(reagrupada, DOWN, buff=0.3)
        self.play(FadeIn(n_reagr))
        self.wait(1.8)
        self.play(FadeOut(VGroup(reagrupada, n_reagr)))

        # ------------------------------------------------ el resultado
        resultado = MathTex(
            r"g=\sum_{n=0}^{L-1}r[n]\,s[n]"
            r"\underset{H_0}{\overset{H_1}{\gtrless}}"
            r"\gamma=\sigma^2\ln\!\Big(\frac{p_0}{p_1}\Big)+\frac{E}{2}",
            color=VERDE).scale(0.82)
        resultado.next_to(tit, DOWN, buff=0.7).set_x(0)
        caja = SurroundingRectangle(resultado, color=VERDE, buff=0.3)
        self.play(Write(resultado), Create(caja))
        n_E = nota("$E=\\sum_n s^2[n]$: la energía de la señal objetivo",
                   scale=0.46)
        n_E.next_to(caja, DOWN, buff=0.35)
        self.play(FadeIn(n_E))
        self.wait(1.6)

        clave = Text("Todo el problema se redujo a calcular UN número",
                     color=TXT).scale(0.56)
        clave.next_to(n_E, DOWN, buff=0.4)
        self.play(FadeIn(clave, scale=1.05))
        self.wait(1.8)
        self.play(FadeOut(VGroup(resultado, caja, n_E, clave)))

        # ------------------------------------------------ nota sobre otros criterios
        otros = VGroup(
            Text("Si el criterio cambia a Neyman-Pearson o riesgo mínimo,",
                 color=INK).scale(0.52),
            Text("la estructura NO cambia: sigue siendo g ≷ γ.",
                 color=AMBAR).scale(0.56),
            nota("solo cambia cómo se elige el umbral γ", scale=0.46),
        ).arrange(DOWN, buff=0.26)
        otros.next_to(tit, DOWN, buff=0.7).set_x(0)
        self.play(FadeIn(otros[0]))
        self.play(FadeIn(otros[1], shift=UP * 0.1))
        self.play(FadeIn(otros[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, otros)))
        self.wait(0.3)
