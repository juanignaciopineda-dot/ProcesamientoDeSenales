"""Escena 05 — La fórmula de Wiener no causal H = S_yx / S_xx, y su parecido con la medición única."""
from comun.escena import *


class LaFormulaDeWiener(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        self.parte_b1()
        self.parte_b2()
        self.wait(1.0)
        self.limpiar()

    def parte_b1(self):
        fr = fraccion(MathTex(r"S_{yx}(\Omega)", color=TXT), MathTex(r"S_{xx}(\Omega)", color=MEDIDA)).scale(1.3)
        fh = MathTex(r"H(\Omega)=", color=ESTIMACION).scale(1.4)
        grupo = VGroup(fh, fr).arrange(RIGHT, buff=0.3).move_to([0, 0.9, 0])
        marco = SurroundingRectangle(grupo, color=AMBAR, buff=0.3, stroke_width=3)
        sel = sello("filtro de Wiener no causal", AMBAR).move_to([0, -1.2, 0])
        # el eje del tiempo con «ahora» y el futuro
        base = Line([-4.5, -3.0, 0], [4.5, -3.0, 0], color=INK, stroke_width=2)
        ahora = Dot([0, -3.0, 0], radius=0.12, color=AMBAR)
        t_pas = etiqueta("pasado", INK, 0.65).move_to([-2.4, -3.45, 0])
        t_fut = etiqueta("futuro", INK, 0.65).move_to([2.4, -3.45, 0])
        a_fut = flecha([0.4, -2.65, 0], [4.3, -2.65, 0], AMBAR, 4)
        fila = MathTex(r"\ldots\;h[-2]\;\;h[-1]\;\;h[0]\;\;h[1]\;\;h[2]\;\ldots", color=AMBAR).scale(1.15)
        fila.move_to([0, 3.1, 0])
        lu = lupa(TXT).scale(1.0).move_to([5.3, 0.9, 0])
        lu.permitir_encima = True
        nueva = Text("¿nueva?", color=AMBAR, weight=BOLD).scale(0.8).move_to([5.0, 2.2, 0])
        with self.narrar("b1"):
            self.en("filtro")                                # «Ya tenemos el filtro»
            self.play(Create(marco), run_time=0.5)
            self.en("h")                                     # «hache de omega es»
            self.play(FadeIn(fh), run_time=0.4)
            self.en("num")                                   # «la densidad cruzada entre i griega y equis»
            self.play(FadeIn(fr.num, shift=DOWN * 0.2), run_time=0.5)
            self.en("raya")                                  # «dividida entre»
            self.play(Create(fr.barra), run_time=0.4)
            self.en("den")                                   # «la densidad espectral de equis»
            self.play(FadeIn(fr.den, shift=UP * 0.2), run_time=0.5)
            self.en("sello")                                 # «filtro de Wiener no causal»
            self.pop(sel)
            self.en("futuro")                                # «porque usa también el futuro»
            self.play(Create(base), FadeIn(ahora), FadeIn(t_pas), FadeIn(t_fut), run_time=0.5)
            self.play(Create(a_fut), run_time=0.5)
            self.en("corta")                                 # «una fórmula muy corta»
            self.play(VGroup(grupo, marco).animate.scale(1.12), run_time=0.5)
            self.en("infinitos")                             # «infinitos coeficientes»
            self.play(FadeIn(fila, shift=DOWN * 0.2), run_time=0.6)
            self.en("despacio")                              # «la miremos despacio»
            self.play(FadeIn(lu), run_time=0.3)
            self.play(lu.animate.move_to(grupo.get_center() + RIGHT * 1.2), run_time=self.dur(1.0))
            self.en("nueva")                                 # «no es nueva»
            self.play(FadeOut(lu), run_time=0.2)
            self.pop(nueva)
            self.play(Create(tachar(nueva, ROJO)), run_time=0.3)

    def parte_b2(self):
        F, rt = flechas_xy(origen=(-6.2, 0.5), largo=3.6, angulo=45.0)
        fh1 = MathTex("h=", color=ESTIMACION).scale(1.4)
        fr1 = fraccion(MathTex(r"E[y\,x]", color=TXT), MathTex(r"E[x^2]", color=MEDIDA)).scale(1.2)
        cuenta = MathTex(r"=\frac{4}{5}=0{,}8", color=TXT).scale(1.2)
        izq = VGroup(fh1, fr1, cuenta).arrange(RIGHT, buff=0.2).move_to([-3.9, -1.5, 0])
        l_cov = Text("covarianza cruzada", color=AMBAR).scale(0.55).next_to(fr1.num, UP, buff=0.3)
        l_var = Text("varianza", color=AMBAR).scale(0.55).next_to(fr1.den, DOWN, buff=0.3)
        fr2 = fraccion(MathTex(r"S_{yx}(\Omega)", color=TXT), MathTex(r"S_{xx}(\Omega)", color=MEDIDA)).scale(1.2)
        fh2 = MathTex(r"H(\Omega)=", color=ESTIMACION).scale(1.4)
        der = VGroup(fh2, fr2).arrange(RIGHT, buff=0.2).move_to([4.4, -1.5, 0])
        puente = flecha([-0.7, -1.5, 0], [1.6, -1.5, 0], AMBAR, 4)
        La = lienzo_omega(ancho=5.6, alto=1.0, v_max=1.0, centro=(4.1, 2.4))
        cajas = rebanadas_omega(La, 7, alto=1.1)
        r_cov = Text("covarianza", color=AMBAR).scale(0.55).next_to(fr2.num, UP, buff=0.3)
        r_var = Text("varianza", color=AMBAR).scale(0.55).next_to(fr2.den, DOWN, buff=0.3)
        with self.narrar("b2"):
            self.en("unica")                                 # «la medición única»
            self.corte()
            self.play(Create(F.presente), Create(F.futuro), FadeIn(rt["x"]), FadeIn(rt["y"]), run_time=0.7)
            self.play(Create(F.sombra), Create(F.error), run_time=0.4)
            self.en("coef")                                  # «El coeficiente era»
            self.play(FadeIn(fh1), run_time=0.4)
            self.en("num1")                                  # «la media de i griega por equis»
            self.play(FadeIn(fr1.num), run_time=0.5)
            self.en("den1")                                  # «entre la media de equis al cuadrado»
            self.play(Create(fr1.barra), FadeIn(fr1.den), run_time=0.5)
            self.en("cuenta")                                # «cuatro entre cinco, cero coma ocho»
            self.play(FadeIn(cuenta), run_time=0.7)
            self.en("cov")                                   # «Una covarianza cruzada»
            self.play(FadeIn(l_cov), run_time=0.4)
            self.resaltar(fr1.num, color=AMBAR)
            self.en("var")                                   # «dividida entre una varianza»
            self.play(FadeIn(l_var), run_time=0.4)
            self.resaltar(fr1.den, color=AMBAR)
            self.en("misma")                                 # «la misma división»
            self.play(Create(puente), run_time=0.4)
            self.play(FadeIn(fh2), FadeIn(fr2.num), Create(fr2.barra), FadeIn(fr2.den), run_time=0.7)
            self.en("cada")                                  # «en cada frecuencia»
            self.play(LaggedStart(*[FadeIn(c) for c in cajas], lag_ratio=0.12), run_time=self.dur(1.2))
            self.en("covf")                                  # «la covarianza entre los dos procesos en esa frecuencia»
            self.play(FadeIn(r_cov), cajas[3].animate.set_fill(AMBAR, 0.3), run_time=0.4)
            self.resaltar(fr2.num, color=AMBAR)
            self.en("denf")                                  # «entre la densidad de equis»
            self.resaltar(fr2.den, color=AMBAR)
            self.en("varf")                                  # «su varianza»
            self.play(FadeIn(r_var), run_time=0.4)
