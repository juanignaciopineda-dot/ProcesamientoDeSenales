"""Escena 06 — La densidad cruzada del micrófono tardío: módulo = la voz, ángulo = el retardo."""
from comun.escena import *


class ModuloYAngulo(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        o = np.array([-3.0, -0.8, 0.0])
        plano = plano_c((o[0], o[1]), radio=1.9)
        F = oculta(formula(r"S_{yx}(j\omega)", "=", r"S_{xx}(j\omega)", r"\cdot", r"e^{-j\omega\,0{,}5}",
                           escala=1.0, colores={0: MEDIDA, 2: SENAL}).move_to([0.5, 3.2, 0]))
        pers = persona(AZUL).scale(0.9).move_to([-6.4, 3.2, 0])
        mic = microfono(CIAN).scale(1.0).move_to([-5.3, 3.2, 0])
        z = flecha_c(o, 1.9, 0, AMBAR)
        l_mod = etiqueta("módulo = cuánto comparten", AMBAR, 0.55).move_to([3.9, 1.0, 0])
        eje = Line([1.6, -2.6, 0], [6.6, -2.6, 0], color=INK, stroke_width=2.5)
        l_w = MathTex(r"\omega", color=INK).scale(0.6).move_to([6.8, -2.35, 0])
        marca = Dot([3.0, -2.6, 0], radius=0.1, color=AMBAR)
        arco = Arc(radius=0.8, start_angle=0, angle=-np.deg2rad(60), color=CIAN, stroke_width=4).move_arc_center_to(o)
        l_ang = formula(r"-0{,}5\,\omega", escala=0.75, colores={0: CIAN}).move_to(o + np.array([2.8, -0.25, 0]))
        hz = formula(r"1\,\mathrm{Hz}", r"\Rightarrow", r"\omega=2\pi", escala=0.85).move_to([4.1, -0.7, 0])
        arco2 = Arc(radius=0.8, start_angle=0, angle=-PI, color=CIAN, stroke_width=4).move_arc_center_to(o)
        l_pi = formula(r"-\pi", escala=0.85, colores={0: CIAN}).move_to(o + np.array([0, -1.2, 0]))
        with self.narrar("b1"):
            # «En el ejemplo»
            self.en("ejemplo")
            self.add(F)
            self.play(FadeIn(pers), FadeIn(mic), *revelar(F[0], F[1]), run_time=self.dur(0.7))

            # «la densidad de la voz»
            self.en("sxx")
            self.play(*revelar(F[2]), run_time=self.dur(0.6))

            # «por e elevado a menos jota omega»
            self.en("exp")
            self.play(*revelar(F[3], F[4]), run_time=self.dur(0.8))

            # «por cero coma cinco»
            self.en("medio")
            self.play(F[4].animate.set_color(AMBAR), run_time=0.5)

            # «El módulo es la densidad de la voz»
            self.en("modulo")
            self.play(Create(plano), GrowArrow(z), run_time=self.dur(1.0))

            # «cuánta potencia comparten»
            self.en("comparten")
            self.pop(l_mod)

            # «en esa frecuencia»
            self.en("esafreq")
            self.play(Create(eje), FadeIn(l_w), FadeIn(marca), run_time=self.dur(0.7))

            # «El ángulo es menos cero coma cinco por omega»
            self.en("angulo")
            self.play(Rotate(z, -np.deg2rad(60), about_point=o), Create(arco), run_time=self.dur(1.0))
            self.play(FadeIn(l_ang), run_time=0.4)

            # «en un hercio, omega es dos pi»
            self.en("hz")
            self.play(FadeIn(hz), marca.animate.move_to([5.0, -2.6, 0]), run_time=self.dur(0.9))

            # «gira media vuelta»
            self.en("media")
            self.play(Rotate(z, -np.deg2rad(120), about_point=o), FadeOut(arco), FadeOut(l_ang),
                      run_time=self.dur(1.0))
            self.play(Create(arco2), FadeIn(l_pi), run_time=0.5)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        o = np.array([-3.8, 0.1, 0.0])
        plano = plano_c((o[0], o[1]), radio=1.7)
        z = flecha_c(o, 1.7, 40, AMBAR)
        arco = Arc(radius=0.7, start_angle=0, angle=np.deg2rad(40), color=CIAN, stroke_width=4).move_arc_center_to(o)
        l_mod = etiqueta("módulo", AMBAR, 0.5).move_to([-3.8, -3.0, 0])
        l_ang = etiqueta("ángulo", CIAN, 0.5).move_to([-3.8, -3.55, 0])
        l_mod2 = etiqueta("módulo = parecido", AMBAR, 0.5).move_to([-3.8, -3.0, 0])
        l_ang2 = etiqueta("ángulo = desfase", CIAN, 0.5).move_to([-3.8, -3.55, 0])
        o7 = np.array([2.3, -0.9, 0.0])
        fx = flecha_c(o7, 2.4, 0, SENAL)
        fy = flecha_c(o7, 2.4, 55, MEDIDA)
        a7 = Arc(radius=0.8, start_angle=0, angle=np.deg2rad(55), color=TXT, stroke_width=3).move_arc_center_to(o7)
        t7 = etiqueta("capítulo 7", INK, 0.5).move_to([5.7, 1.5, 0])
        l_lim = etiqueta("límite", ROJO, 0.55).move_to([-3.8, 2.7, 0])
        par = parabola_l(centro=(3.9, -0.8), ancho=4.0, alto=2.6, fondo=0.25)
        with self.narrar("b2"):
            # «dice dos cosas en cada frecuencia»
            self.en("dos")
            self.corte()
            self.play(Create(plano), GrowArrow(z), Create(arco), run_time=self.dur(0.8))
            self.play(FadeIn(l_mod), FadeIn(l_ang), run_time=0.4)

            # «cuánto se parecen las dos señales, en el módulo»
            self.en("parecen")
            self.play(ReplacementTransform(l_mod, l_mod2), run_time=self.dur(0.6))

            # «cuánto están desfasadas, en el ángulo»
            self.en("desfase")
            self.play(ReplacementTransform(l_ang, l_ang2), run_time=self.dur(0.6))

            # «las variables del capítulo siete»
            self.en("var7")
            self.play(GrowArrow(fx), GrowArrow(fy), Create(a7), FadeIn(t7), run_time=self.dur(1.0))

            # «hay un límite»
            self.en("limite")
            self.play(plano.circ.animate.set_stroke(ROJO, opacity=1.0), FadeIn(l_lim), run_time=self.dur(0.7))

            # «Recuerda la parábola»
            self.en("parabola")
            self.play(FadeOut(fx), FadeOut(fy), FadeOut(a7), FadeOut(t7), run_time=0.3)
            self.play(Create(par), run_time=self.dur(0.9))
