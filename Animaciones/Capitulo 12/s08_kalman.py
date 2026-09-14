"""Escena 8 - Observadores optimos y el filtro de Kalman.

Si la senal que quiero estimar sale de un sistema en espacio de estados
excitado con ruido blanco, el filtro de Wiener causal queda determinado
por una unica ecuacion de factorizacion espectral, y se implementa como
un observador de ese sistema. Eso es un filtro de Kalman.

    manim -pql s08_kalman.py Kalman
"""
from manim import *
import numpy as np
from comun import *


class Kalman(Scene):
    def construct(self):
        configurar()

        tit = titulo("Del Wiener causal al filtro de Kalman")
        self.play(FadeIn(tit, shift=DOWN * 0.2))
        self.wait(0.3)

        # ------------------------------------------------ el planteo en estados
        sub = Text("La señal sale de un sistema en espacio de estados",
                   color=TXT).scale(0.54)
        sub.next_to(tit, DOWN, buff=0.4)
        self.play(FadeIn(sub))

        modelo = VGroup(
            MathTex(r"q[n+1] = A\,q[n] + b\,w[n]", color=TXT),
            MathTex(r"y[n] = c^{T} q[n]", color=TXT),
            MathTex(r"x[n] = y[n] + v[n]", color=TXT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).scale(0.7)
        modelo.next_to(sub, DOWN, buff=0.4)
        self.play(Write(modelo))
        n_wv = nota("w y v son blancos y no están correlacionados entre sí",
                    scale=0.46)
        n_wv.next_to(modelo, DOWN, buff=0.3)
        self.play(FadeIn(n_wv))
        self.wait(1.6)

        gz = MathTex(r"G(z)=c^{T}(zI-A)^{-1}b=\frac{\beta(z)}{a(z)}",
                     color=AMBAR).scale(0.66)
        gz.next_to(n_wv, DOWN, buff=0.35)
        n_gz = nota("a(z) = det(zI − A): el característico, mónico, de grado L",
                    scale=0.44)
        n_gz.next_to(gz, DOWN, buff=0.2)
        self.play(FadeIn(gz), FadeIn(n_gz))
        self.wait(2.0)
        self.play(FadeOut(VGroup(sub, modelo, n_wv, gz, n_gz)))

        # ------------------------------------------------ la factorizacion espectral
        f1 = MathTex(r"D_{xx}(z)=\sigma_v^2\,"
                     r"\frac{\alpha(z)\,\alpha(z^{-1})}{a(z)\,a(z^{-1})}"
                     r"\qquad r=\frac{\sigma_w^2}{\sigma_v^2}",
                     color=TXT).scale(0.66)
        f1.next_to(tit, DOWN, buff=0.55)
        self.play(Write(f1))
        self.wait(0.8)

        fac = MathTex(r"\alpha(z)\,\alpha(z^{-1}) \;=\; "
                      r"r\,\beta(z)\,\beta(z^{-1}) + a(z)\,a(z^{-1})",
                      color=AZUL).scale(0.78)
        fac.next_to(f1, DOWN, buff=0.5)
        cja = SurroundingRectangle(fac, color=AZUL, buff=0.25)
        self.play(Write(fac), Create(cja))
        n_fac = nota("α(z): mónico de grado L, con TODAS sus raíces\n"
                     "dentro del círculo unidad", scale=0.46, color=AZUL)
        n_fac.next_to(cja, DOWN, buff=0.3)
        self.play(FadeIn(n_fac))
        self.wait(1.8)

        # ------------------------------------------------ el resultado sorprendente
        self.play(FadeOut(VGroup(f1, n_fac)),
                  VGroup(fac, cja).animate.scale(0.85)
                  .next_to(tit, DOWN, buff=0.5))

        Hz = MathTex(r"H(z)=1-\frac{a(z)}{\alpha(z)}"
                     r"=\frac{\alpha(z)-a(z)}{\alpha(z)}",
                     color=VERDE).scale(0.9)
        Hz.next_to(fac, DOWN, buff=0.8)
        self.play(Write(Hz))
        self.play(Circumscribe(Hz, color=VERDE, buff=0.2, run_time=1.4))
        n_hz = nota("todo el filtro queda determinado por la factorización:\n"
                    "resolvés para α(z) y ya tenés el filtro", scale=0.48)
        n_hz.next_to(Hz, DOWN, buff=0.4)
        self.play(FadeIn(n_hz))
        self.wait(2.2)
        self.play(FadeOut(VGroup(fac, cja, Hz, n_hz)))

        # ------------------------------------------------ el mismo filtro, observador
        obs_t = Text("El mismo filtro, implementado como observador",
                     color=TXT).scale(0.56)
        obs_t.next_to(tit, DOWN, buff=0.4)
        self.play(FadeIn(obs_t))

        obs = MathTex(r"\hat{q}[n+1]=(A+\ell\,c^{T})\,\hat{q}[n]-\ell\,x[n]",
                      r"\qquad \hat{y}[n]=c^{T}\hat{q}[n]",
                      color=TXT).scale(0.58)
        obs.next_to(obs_t, DOWN, buff=0.35)
        self.play(Write(obs))
        self.wait(0.8)

        # diagrama de bloques
        planta = bloque(r"\text{planta}", color=AMBAR, ancho=1.9, alto=0.8,
                        scale=0.45)
        suma = Circle(radius=0.2, color=INK, stroke_width=2.5)
        mas = MathTex("+", color=INK).scale(0.55).move_to(suma)
        nodo = VGroup(suma, mas)
        observ = bloque(r"\text{observador}", color=AZUL, ancho=2.1,
                        alto=0.8, scale=0.45)
        cadena = VGroup(planta, nodo, observ).arrange(RIGHT, buff=1.15)
        cadena.next_to(obs, DOWN, buff=0.9)
        w_lbl = MathTex(r"w[n]", color=MAGENTA).scale(0.5)
        w_lbl.next_to(planta, LEFT, buff=0.5)
        v_lbl = MathTex(r"v[n]", color=ROJO).scale(0.5)
        v_lbl.next_to(nodo, UP, buff=0.4)
        yh_lbl = MathTex(r"\hat{y}[n]", color=VERDE).scale(0.5)
        yh_lbl.next_to(observ, RIGHT, buff=0.5)
        f0 = flecha(w_lbl.get_right(), planta.get_left())
        fa = flecha(planta.get_right(), nodo.get_left())
        fb = flecha(v_lbl.get_bottom(), nodo.get_top(), color=ROJO)
        fc = flecha(nodo.get_right(), observ.get_left())
        fd = flecha(observ.get_right(), yh_lbl.get_left())
        yn = MathTex(r"y[n]", color=INK).scale(0.42).next_to(fa, UP, buff=0.05)
        xn = MathTex(r"x[n]", color=INK).scale(0.42).next_to(fc, UP, buff=0.05)
        diag = VGroup(cadena, w_lbl, v_lbl, yh_lbl, f0, fa, fb, fc, fd, yn, xn)
        self.play(FadeIn(cadena),
                  *[GrowArrow(a) for a in (f0, fa, fb, fc, fd)],
                  FadeIn(VGroup(w_lbl, v_lbl, yh_lbl, yn, xn)))
        self.wait(0.8)

        clave = nota("elegí la ganancia ℓ para que el polinomio característico\n"
                     "del observador sea α(z)", scale=0.46, color=AZUL)
        clave.next_to(cadena, DOWN, buff=0.45)
        self.play(FadeIn(clave))
        self.wait(1.4)
        result = MathTex(r"\Rightarrow\quad "
                         r"H(z)=\frac{\alpha(z)-a(z)}{\alpha(z)}",
                         color=VERDE).scale(0.62)
        result.next_to(clave, DOWN, buff=0.3)
        self.play(FadeIn(result, shift=UP * 0.1))
        n_r = nota("exactamente el mismo filtro de Wiener causal", scale=0.44)
        n_r.next_to(result, DOWN, buff=0.2)
        self.play(FadeIn(n_r))
        self.wait(2.0)
        self.play(FadeOut(VGroup(obs_t, obs, diag, clave, result, n_r)))

        # ------------------------------------------------ y esto es un Kalman
        kt = Text("Y esto es un filtro de Kalman", color=TXT).scale(0.62)
        kt.next_to(tit, DOWN, buff=0.5)
        self.play(FadeIn(kt, scale=1.1))

        col_w = VGroup(
            subtitulo("vía Wiener", scale=0.5, color=AZUL),
            nota("parto de la PSD de la medición;\n"
                 "factorización espectral → α(z) → ganancia ℓ", scale=0.44),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        col_k = VGroup(
            subtitulo("vía Kalman", scale=0.5, color=VERDE),
            nota("parto del modelo de estados;\n"
                 "busco el LMMSE del estado y aparece el observador",
                 scale=0.44),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        cols = VGroup(col_w, col_k).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        cols.next_to(kt, DOWN, buff=0.6)
        self.play(FadeIn(col_w, shift=RIGHT * 0.1))
        self.play(FadeIn(col_k, shift=RIGHT * 0.1))
        self.wait(1.6)

        gen = nota("el Kalman general va más lejos: sistemas variantes en el "
                   "tiempo,\ninestables, sin estacionariedad; ahí la "
                   "factorización\nse reemplaza por una ecuación de Riccati",
                   scale=0.44)
        gen.next_to(cols, DOWN, buff=0.55)
        self.play(FadeIn(gen))
        self.wait(2.2)
        self.play(FadeOut(VGroup(kt, cols, gen)))

        # ------------------------------------------------ cierre
        cierre = VGroup(
            Text("Si la señal nace de un sistema de estados con ruido blanco,",
                 color=INK).scale(0.52),
            Text("el Wiener causal ES un observador de ese sistema.",
                 color=VERDE).scale(0.58),
            nota("la ganancia se elige para que el observador tenga\n"
                 "los polos del factor espectral α(z)", scale=0.48),
        ).arrange(DOWN, buff=0.3)
        cierre.move_to(ORIGIN)
        self.play(FadeIn(cierre[0]))
        self.play(FadeIn(cierre[1], shift=UP * 0.12))
        self.wait(0.5)
        self.play(FadeIn(cierre[2]))
        self.wait(2.2)
        self.play(FadeOut(VGroup(tit, cierre)))
        self.wait(0.3)
