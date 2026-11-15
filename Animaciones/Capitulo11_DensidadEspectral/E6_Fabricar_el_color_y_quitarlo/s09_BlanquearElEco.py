"""Escena 09 — Blanquear el eco: u[n] = x[n] − 0,6 x[n−1] devuelve la moneda, con datos simulados."""
from comun.escena import *


class BlanquearElEco(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        puntos = fila_puntos(6, ancho=4.2, centro=(-4.2, 3.4), color=SENAL, radio=0.09)
        hilos = hilos_entre(puntos, INK, 3)
        t_eco = etiqueta("el eco", INK, 0.55).move_to([-1.2, 3.4, 0])
        f1 = formula("x[n]", "=", num_tex(0.6), "x[n-1]", "+", "w[n]", escala=1.2,
                     colores={0: SENAL, 3: SENAL, 5: RUIDO}).move_to([0, 2.0, 0])
        f2 = formula("u[n]", "=", "x[n]", "-", num_tex(0.6), "x[n-1]", escala=1.2,
                     colores={0: ESTIMACION, 2: SENAL, 5: SENAL}).move_to([0, 0.5, 0])
        f3 = formula("u[n]", "=", "(", num_tex(0.6), "x[n-1]", "+", "w[n]", ")", "-", num_tex(0.6), "x[n-1]",
                     escala=1.2, colores={0: ESTIMACION, 4: SENAL, 6: RUIDO, 10: SENAL}).move_to([0, -1.1, 0])
        fl = Arrow([5.4, 0.7, 0], [5.4, -0.9, 0], color=INK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.2)
        f4 = formula("u[n]", "=", "w[n]", escala=1.6, colores={0: ESTIMACION, 2: RUIDO}).move_to([0, -2.7, 0])
        ok = tilde(VERDE, 0.7).move_to([2.8, -2.7, 0])
        with self.narrar("b1"):
            # «Con el eco se ve a mano»
            self.en("eco")
            self.play(LaggedStart(*[FadeIn(p) for p in puntos], lag_ratio=0.1), Create(hilos), FadeIn(t_eco),
                      run_time=self.dur(0.9))

            # «el modelador hacía»
            self.en("modelador")
            self.play(FadeIn(f1[0:2]), run_time=self.dur(0.6))

            # «por la equis anterior»
            self.en("por")
            self.play(FadeIn(f1[2:4]), run_time=self.dur(0.7))

            # «más la moneda»
            self.en("masmoneda")
            self.play(FadeIn(f1[4:6]), run_time=self.dur(0.6))

            # «el blanqueador hace»
            self.en("blanqueador")
            self.play(FadeIn(f2[0:3]), run_time=self.dur(0.8))

            # «menos cero coma seis»
            self.en("menos")
            self.play(FadeIn(f2[3:6]), run_time=self.dur(0.8))

            # «Sustituye la primera ecuación en la segunda»
            self.en("sustituye")
            self.play(GrowArrow(fl), run_time=0.4)
            self.play(FadeIn(f3), run_time=self.dur(1.0))

            # «se cancela»
            self.en("cancela")
            x1 = Line(f3[3].get_corner(DL), f3[4].get_corner(UR), color=ROJO, stroke_width=5)
            x2 = Line(f3[9].get_corner(DL), f3[10].get_corner(UR), color=ROJO, stroke_width=5)
            x1.permitir_encima = True
            x2.permitir_encima = True
            self.play(Create(x1), Create(x2), run_time=0.5)

            # «lo que queda es la moneda»
            self.en("queda")
            self.play(FadeIn(f4), run_time=self.dur(0.6))

            # «Exacta»
            self.en("exacta")
            self.pop(ok)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        t400 = etiqueta("400.000 muestras", INK, 0.7).move_to([0, 3.3, 0])
        xs = [-2.4, -0.6, 1.2, 3.0]
        cab = VGroup(*[Text(str(k), color=INK).scale(0.55).move_to([x, 1.8, 0]) for k, x in zip((1, 2, 3, 4), xs)])
        t_dist = etiqueta("distancia", INK, 0.5).move_to([-5.0, 1.8, 0])
        fx = etiqueta("x", SENAL, 0.8).move_to([-5.0, 0.4, 0])
        fu = etiqueta("u", ESTIMACION, 0.8).move_to([-5.0, -1.2, 0])
        vx = ["0,60", "0,36", "0,22", "0,13"]
        vu = ["0,00", "0,003", "−0,001", "0,00"]
        nx = [etiqueta(s, SENAL, 0.75).move_to([x, 0.4, 0]) for s, x in zip(vx, xs)]
        nu = [etiqueta(s, ESTIMACION, 0.75).move_to([x, -1.2, 0]) for s, x in zip(vu, xs)]
        marco = SurroundingRectangle(VGroup(fu, *nu), color=VERDE, buff=0.3, corner_radius=0.1)
        ok = tilde(VERDE, 0.7).move_to([5.4, -1.2, 0])
        with self.narrar("b2"):
            # «cuatrocientas mil muestras simuladas»
            self.en("simuladas")
            self.corte()
            self.pop(t400)

            # «Antes del blanqueador»
            self.en("antes")
            self.play(FadeIn(t_dist), FadeIn(cab), FadeIn(fx), run_time=self.dur(0.8))

            # «cero coma seis, cero coma tres seis»
            self.en("primeras")
            self.play(FadeIn(nx[0]), run_time=0.4)
            self.play(FadeIn(nx[1]), run_time=0.4)

            # «cero coma dos dos, cero coma uno tres»
            self.en("siguientes")
            self.play(FadeIn(nx[2]), run_time=0.4)
            self.play(FadeIn(nx[3]), run_time=0.4)

            # «Después»
            self.en("despues")
            self.play(FadeIn(fu), run_time=0.4)

            # «cero, cero coma cero cero tres»
            self.en("ceros1")
            self.play(FadeIn(nu[0]), run_time=0.3)
            self.play(FadeIn(nu[1]), run_time=0.3)

            # «menos cero coma cero cero uno, cero»
            self.en("ceros2")
            self.play(FadeIn(nu[2]), run_time=0.3)
            self.play(FadeIn(nu[3]), run_time=0.3)

            # «Toda la memoria, borrada»
            self.en("borrada")
            self.play(FadeIn(marco), run_time=0.5)
            self.pop(ok)

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        g, b, ent, sal = cadena_bloques("blanco", "H", "coloreado", centro=(-1.0, 2.7), color=CIAN)
        g2, b2, ent2, sal2 = cadena_bloques("coloreado", "1/H", "blanco", centro=(-1.0, 1.1), color=AMBAR)
        q = MathTex("?", color=AMBAR).scale(1.8).move_to(b.caja.get_center() + [0, 1.0, 0])
        t_u = formula(r"\sqrt{S_{xx}}", escala=1.0).move_to([5.0, 2.7, 0])
        t_fac = etiqueta("factor espectral", AMBAR, 0.7).move_to([5.0, 3.4, 0])
        t_unico = etiqueta("¿único?", AMBAR, 0.8).move_to([5.0, 1.5, 0])
        tach = Line(t_unico.get_corner(DL), t_unico.get_corner(UR), color=ROJO, stroke_width=5)
        h1 = BloqueLTI("H_1", centro=(-3.5, -1.4), ancho=1.6, alto=0.9, largo=1.2, color=CIAN, escala=0.75)
        h2 = BloqueLTI("H_2", centro=(-3.5, -3.0), ancho=1.6, alto=0.9, largo=1.2, color=AMBAR, escala=0.75)
        L1 = Lienzo(ancho=3.0, alto=1.0, t_rango=(0, 3), v_max=1.0, centro=(2.4, -1.4))
        L2 = Lienzo(ancho=3.0, alto=1.0, t_rango=(0, 3), v_max=1.0, centro=(2.4, -3.0))
        r1 = ruido_t(L1, semilla=9, amp=0.8)
        r2 = ruido_t(L2, semilla=9, amp=0.8)
        ok = tilde(VERDE, 0.5).move_to([5.6, -1.4, 0])
        qq = MathTex("?", color=AMBAR).scale(1.2).move_to([5.6, -3.0, 0])
        with self.narrar("b3"):
            # «uno el inverso del otro»
            self.en("inverso")
            self.corte()
            self.play(FadeIn(g), FadeIn(g2), run_time=self.dur(0.8))

            # «un detalle que hemos pasado por alto»
            self.en("detalle")
            self.pop(q)

            # «El factor espectral»
            self.en("factor")
            self.pop(t_fac)

            # «la raíz cuadrada del espectro»
            self.en("raizesp")
            self.play(FadeIn(t_u), run_time=self.dur(0.6))

            # «no es único»
            self.en("unico")
            self.play(FadeIn(t_unico), run_time=0.4)
            self.play(Create(tach), run_time=0.3)

            # «más de un filtro»
            self.en("mas")
            self.play(FadeIn(h1), FadeIn(h2), run_time=self.dur(0.7))

            # «el mismo proceso»
            self.en("mismo")
            self.play(Create(L1.base()), Create(r1), Create(L2.base()), Create(r2), run_time=self.dur(1.2),
                      rate_func=linear)

            # «no todos sirven»
            self.en("sirven")
            self.play(FadeIn(ok), FadeIn(qq), run_time=0.5)
