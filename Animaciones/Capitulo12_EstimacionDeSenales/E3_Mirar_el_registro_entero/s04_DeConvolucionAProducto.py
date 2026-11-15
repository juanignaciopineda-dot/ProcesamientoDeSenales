"""Escena 04 — Fourier convierte la convolución en producto; la igualdad vale en todo el eje, así que se transforma."""
from comun.escena import *


class DeConvolucionAProducto(EscenaCurso):
    ESCENA = "04"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.parte_b3()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        cuadro = caja("Fourier", CIAN, ancho=2.6, alto=0.9, scale=0.6).move_to([0, 2.7, 0])
        izq = MathTex(r"h\ast g", color=TXT).scale(1.1).move_to([-4.4, 2.7, 0])
        der = MathTex(r"H\cdot G", color=TXT).scale(1.1).move_to([4.4, 2.7, 0])
        f1 = flecha(izq.get_right() + RIGHT * 0.15, cuadro.get_left(), INK, 3)
        f2 = flecha(cuadro.get_right(), der.get_left() + LEFT * 0.15, INK, 3)
        regla = MathTex(r"\ast\;\leftrightarrow\;\times", color=AMBAR).scale(1.3).move_to([0, 1.6, 0])
        L = Lienzo(ancho=10.0, alto=2.0, t_rango=(-np.pi, np.pi), v_max=2.0, centro=(0.0, -1.7))
        eje = eje_omega(L, 0.0, completo=True, escala=0.85)
        muestras = Tallos([0.3, 0.7, 1.0, 0.6, 0.9, 0.4, 0.8, 0.5, 0.2], centro=(0.0, 0.2), paso=0.5,
                          unidad=0.6, color=SENAL)
        om = MathTex(r"\Omega", color=AMBAR).scale(0.9).next_to(L.p(np.pi, 0), UR, buff=0.1)
        plana = Line(L.p(-0.7, 1.0), L.p(0.7, 1.0), color=SENAL, stroke_width=5)
        r_cont = etiqueta("continua", AMBAR, 0.7).next_to(plana, UP, buff=0.15)
        alt = Tallos([1, -1, 1, -1, 1, -1], centro=(4.0, -0.7), paso=0.35, unidad=0.35, color=SENAL)
        r_rap = etiqueta("la más rápida", AMBAR, 0.65).next_to(alt, UP, buff=0.15)
        marca_pi = DashedLine(alt.get_bottom() + DOWN * 0.1, L.p(np.pi, 0.0), color=INK, stroke_width=2)
        self.eje = eje
        with self.narrar("b1"):
            self.en("fourier")                               # «qué hace Fourier»
            self.pop(cuadro)
            self.en("conv")                                  # «una convolución»
            self.play(FadeIn(izq), Create(f1), run_time=0.5)
            self.en("prod")                                  # «la convierte en un producto»
            self.play(Create(f2), FadeIn(der), run_time=0.5)
            self.pop(regla)
            self.en("discreto")                              # «En tiempo discreto»
            self.play(FadeIn(muestras), run_time=0.6)
            self.en("omega")                                 # «omega mayúscula»
            self.play(FadeOut(muestras), Create(eje.h), run_time=0.5)
            self.pop(om)
            self.en("rango")                                 # «va de menos pi a pi»
            self.play(FadeIn(eje.rotulos[0]), FadeIn(eje.rotulos[2]), run_time=0.5)
            self.en("cero")                                  # «Cero es la continua»
            self.play(FadeIn(eje.rotulos[1]), Create(plana), FadeIn(r_cont), run_time=0.6)
            self.en("pi")                                    # «pi es la más rápida»
            self.play(FadeIn(alt), FadeIn(r_rap), Create(marca_pi), run_time=0.6)
            self.en("alterna")                               # «más, menos, más, menos»
            self.play(LaggedStart(*[VGroup(alt.tallos[i], alt.puntos[i]).animate.set_color(AMBAR)
                                    for i in range(6)], lag_ratio=0.2), run_time=self.dur(1.4))
            self.en("muestra")                               # «en cada muestra»
            self.resaltar(alt, color=AMBAR, escala=1.08)
            self.en("eje")                                   # «Ese es el eje»
            self.play(eje.h.animate.set_color(AMBAR), run_time=0.4)

    def parte_b2(self):
        f = formula("h", r"\ast", "C_{xx}", "=", "C_{yx}", escala=1.3, colores={2: MEDIDA}).move_to([0, 3.1, 0])
        para = Text("para todo m", color=AMBAR, weight=BOLD).scale(0.75).move_to([0, 2.4, 0])
        A = Tallos([1, 2, 3, 2, 1], centro=(-3.6, 1.2), paso=0.5, unidad=0.18, color=AMBAR)
        B = Tallos([1, 2, 3, 2, 1], centro=(-3.6, -0.15), paso=0.5, unidad=0.18, color=ESTIMACION)
        tildes = VGroup(*[tilde(VERDE, 0.22).move_to([A.x(i), 0.7, 0]) for i in range(5)])
        Lc = Lienzo(ancho=4.2, alto=1.8, t_rango=(-3, 3), v_max=2.0, centro=(3.6, 0.6))
        c1 = curva_f(Lc, lambda w: 0.9 + 0.8 * np.cos(w), -3, 3, AZUL, 5)
        c2 = curva_f(Lc, lambda w: 0.9 + 0.8 * np.cos(w), -3, 3, AMBAR, 2.5)
        tilde_c = tilde(VERDE, 0.3).move_to([3.6, -0.7, 0])
        g = formula(r"H(\Omega)", r"\cdot", r"S_{xx}(\Omega)", "=", r"S_{yx}(\Omega)", escala=1.2,
                    colores={2: MEDIDA}).move_to([0, -1.6, 0])
        a1 = flecha([f[2].get_x(), 2.45, 0], [g[1].get_x(), -1.1, 0], AMBAR, 3)
        a2 = flecha([f[4].get_x(), 2.7, 0], [g[4].get_x(), -1.1, 0], AMBAR, 3)
        four = etiqueta("Fourier", INK, 0.65).next_to(a1, LEFT, buff=0.15)
        with self.narrar("b2"):
            self.en("clave")                                 # «el punto clave»
            self.corte()
            self.play(FadeIn(f), run_time=0.6)
            self.en("izq")                                   # «hache convolucionado con la autocorrelación»
            self.resaltar(f[0], f[1], f[2], color=AMBAR)
            self.en("der")                                   # «la correlación cruzada»
            self.resaltar(f[4], color=AMBAR)
            self.en("cumple")                                # «se cumple para todo eme»
            self.pop(para)
            self.en("secs")                                  # «Si dos secuencias»
            self.play(FadeIn(A), FadeIn(B), run_time=0.5)
            self.en("muestras")                              # «iguales en todas sus muestras»
            self.play(LaggedStart(*[FadeIn(t, scale=0.4) for t in tildes], lag_ratio=0.2), run_time=self.dur(1.2))
            self.en("frecs")                                 # «iguales en todas las frecuencias»
            self.play(Create(c1), run_time=0.7)
            self.play(Create(c2), FadeIn(tilde_c), run_time=0.7)
            self.en("lados")                                 # «transformar los dos lados»
            self.play(FadeOut(A), FadeOut(B), FadeOut(tildes), FadeOut(c1), FadeOut(c2), FadeOut(tilde_c),
                      Create(a1), Create(a2), FadeIn(four), run_time=0.6)
            self.en("lado1")                                 # «el producto de hache por la densidad espectral de equis»
            self.play(FadeIn(g[0:3]), run_time=0.6)
            self.en("lado2")                                 # «la densidad cruzada de i griega con equis»
            self.play(FadeIn(g[3:5]), run_time=0.5)
        self.g = g
        self.a = VGroup(a1, a2, four, f, para)

    def parte_b3(self):
        cajas = VGroup(*[VGroup(RoundedRectangle(corner_radius=0.1, width=2.3, height=0.95, color=INK,
                                                 stroke_width=2).set_fill(INK, 0.08),
                                MathTex(r"H\,S_{xx}=S_{yx}", color=TXT).scale(0.7))
                         for _ in range(5)]).arrange(RIGHT, buff=0.15).move_to([0, 2.6, 0])
        for c in cajas:
            c[1].move_to(c[0])
        f = MathTex(r"H(\Omega)=\frac{S_{yx}(\Omega)}{S_{xx}(\Omega)}", color=TXT).scale(1.4).move_to([0, 0.5, 0])
        col = columna_ecuaciones(centro=(-5.0, -1.5), escala=0.5, paso=0.6)
        para = Text("para todo m", color=AMBAR, weight=BOLD).scale(0.8).move_to([-4.4, -3.0, 0])
        e4 = caja("E4", AZUL, ancho=1.2, alto=0.7, scale=0.6).move_to([5.0, -3.0, 0])
        interr = Text("¿?", color=ROJO, weight=BOLD).scale(0.8).move_to([-4.6, -2.3, 0])
        with self.narrar("b3"):
            self.en("unaincog")                              # «una ecuación con una sola incógnita»
            self.corte()
            self.play(LaggedStart(*[FadeIn(c, scale=0.7) for c in cajas], lag_ratio=0.15), run_time=self.dur(1.2))
            self.en("despeja")                               # «se despeja dividiendo»
            self.pop(f)
            self.en("infinito")                              # «Un sistema infinito»
            self.play(FadeIn(col), run_time=0.5)
            self.en("unadiv")                                # «resuelto con una división»
            self.play(col.animate.scale(0.15).move_to(f.get_center()).set_opacity(0), run_time=0.7)
            self.resaltar(f, color=AMBAR, escala=1.05)
            self.en("guarda")                                # «guarda esto»
            self.pop(para)
            self.en("vale")                                  # «la igualdad vale para todo eme»
            self.resaltar(para, color=AMBAR, escala=1.2)
            self.en("proximo")                               # «En el próximo episodio»
            self.pop(e4)
            self.en("novale")                                # «cuando no vale»
            self.play(Create(tachar(para)), FadeIn(interr), run_time=0.5)
