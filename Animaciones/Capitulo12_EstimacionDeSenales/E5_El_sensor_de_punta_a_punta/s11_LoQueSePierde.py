"""Escena 11 — Lo que cuesta no ver el futuro: la pérdida es la energía de la cola cortada; con el sensor, 0,0526."""
from comun.escena import *


class LoQueSePierde(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.bloque1()
        self.bloque2()
        self.bloque3()
        self.wait(1.0)
        self.limpiar()

    # ---------------------------------------------------------------- b1
    def bloque1(self):
        e_nc = formula(r"\text{no causal}", r":\ \sigma_y^2-\frac{1}{\sigma^2}\sum_{\text{todo }m}R[m]^2", escala=0.85,
                       colores={0: VERDE}).move_to([-0.4, 3.2, 0])
        e_c = formula(r"\text{causal}", r":\ \sigma_y^2-\frac{1}{\sigma^2}\sum_{m\ge 0}R[m]^2", escala=0.85,
                      colores={0: AMBAR}).move_to([-0.4, 1.8, 0])
        dif = formula(r"\text{diferencia}", "=", r"\sum R[m]^2", escala=1.15, colores={0: ERROR})
        dif[2].set_color(ERROR)
        dif.move_to([-3.0, 0.4, 0])
        oculta(dif)
        dif_full = MathTex(r"\frac{1}{\sigma^2}\sum_{m<0}R[m]^2", color=ERROR).scale(1.15).next_to(dif[1], RIGHT, buff=0.2)
        t = dos_colas(centro=(-2.6, -2.1), paso=0.5, unidad=0.4, m_min=-5, m_max=6, indices=False)
        cola = VGroup(*[t.palito(t.m(m)) for m in range(-5, 0)])
        cola_rojo = [t.palito(t.m(m)) for m in range(-5, 0)]
        bal = balancin().scale(0.8).move_to([2.2, -2.1, 0])
        l_en = etiqueta("energía", ERROR, 0.5).next_to(bal, UP, buff=0.2)
        Lf = Lienzo(ancho=2.6, alto=1.5, t_rango=(-PI, PI), v_max=2.0, centro=(5.2, -2.6))
        esp = lambda w: 0.2 + 0.7 * np.exp(-(w / 1.2) ** 2)
        c_esp = curva_f(Lf, esp, -PI, PI, RUIDO, 3.5)
        ar_esp = area_f(Lf, esp, -PI, PI, ERROR, 0.5)
        base_f = Lf.base(INK, 2.0)
        l_parseval = etiqueta("Parseval: energía en el tiempo = área en frecuencia", INK, 0.45).move_to([1.2, -0.7, 0])
        l_fut = etiqueta("futuro", ERROR, 0.55, BOLD).move_to(t.pos(t.m(-2)) + UP * 0.9)
        with self.narrar("b1"):
            # «La diferencia entre los dos errores»
            self.en("diferencia")
            self.play(FadeIn(e_nc, shift=DOWN * 0.2), FadeIn(e_c, shift=DOWN * 0.2), run_time=self.dur(1.0))

            # «la suma de la correlación al cuadrado»
            self.en("suma")
            self.add(dif)
            self.play(*revelar(dif[0], dif[1], dif[2]), run_time=self.dur(1.0))

            # «para eme negativo»
            self.en("neg")
            self.play(ReplacementTransform(dif[2], dif_full), run_time=self.dur(0.7))

            # «la energía de la cola que hemos cortado»
            self.en("cola")
            self.play(Create(t.base), *[FadeIn(t.palito(i)) for i in range(len(t.valores))], run_time=0.6)
            self.play(*[p.animate.set_color(ERROR) for g in cola_rojo for p in g], FadeIn(bal), FadeIn(l_en),
                      run_time=self.dur(0.8))

            # «por Parseval»
            self.en("parseval")
            self.play(FadeIn(l_parseval), run_time=self.dur(0.7))

            # «el área de su espectro»
            self.en("area")
            self.play(Create(base_f), Create(c_esp), FadeIn(ar_esp), run_time=self.dur(0.9))

            # «lo que habrías aprovechado del futuro»
            self.en("futuro")
            self.play(FadeIn(l_fut, shift=DOWN * 0.2), run_time=self.dur(0.6))
            self.play(Flash(dif[0], color=ERROR, flash_radius=0.6), run_time=0.5)

    # ---------------------------------------------------------------- b2
    def bloque2(self):
        self.corte()
        t = dos_colas(centro=(-3.6, -2.0), paso=0.5, unidad=0.4, m_min=-5, m_max=6, indices=False)
        cola_rojo = [t.palito(t.m(m)) for m in range(-5, 0)]
        for g in cola_rojo:
            for p in g:
                p.set_color(ERROR)
        l_cola = formula(r"K\cdot 0{,}157^{|m|}", escala=1.0, colores={0: ERROR}).move_to([-5.2, -0.4, 0])
        l_cola.set_color(ERROR)
        A = oculta(formula(r"\frac{2{,}826^2}{3{,}826}", "=", r"2{,}087", escala=1.15, colores={0: ERROR, 2: ERROR})
                   .move_to([-3.5, 3.0, 0]))
        B = oculta(formula(r"\times", r"\sum 0{,}157^{\,2|m|}", "=", r"0{,}0252", escala=1.15,
                           colores={1: ERROR, 3: ERROR}).move_to([2.6, 3.0, 0]))
        llave = Brace(B[1], DOWN, color=AMBAR, buff=0.1)
        l_razon = formula(r"0{,}157^2=0{,}025", escala=0.85, colores={0: AMBAR}).next_to(llave, DOWN, buff=0.1)
        l_razon.set_color(AMBAR)
        res = oculta(formula(r"2{,}087", r"\cdot", r"0{,}0252", "=", r"0{,}0526", escala=1.5, colores={4: ERROR})
                     .move_to([2.5, 0.2, 0]))
        marco = SurroundingRectangle(res, color=ERROR, buff=0.2, corner_radius=0.1, stroke_width=3)
        with self.narrar("b2"):
            # «la cola de la izquierda cae»
            self.en("colaizq")
            self.play(Create(t.base), *[FadeIn(t.palito(i)) for i in range(len(t.valores))], run_time=0.6)
            self.play(*[p.animate.set_opacity(0.25) for m in range(0, 7) for p in t.palito(t.m(m))],
                      FadeIn(l_cola), run_time=self.dur(0.7))

            # «elevado a eme»
            self.en("elevado")
            self.play(Flash(l_cola, color=ERROR, flash_radius=0.7), run_time=0.5)

            # «Su energía»
            self.en("energia")
            self.add(A, B)
            self.play(FadeIn(etiqueta("energía", ERROR, 0.5).move_to([-6.2, 3.0, 0])), run_time=self.dur(0.4))

            # «dos coma ocho dos seis al cuadrado entre tres coma ocho dos seis»
            self.en("cuenta1")
            self.play(*revelar(A[0]), run_time=self.dur(1.0))

            # «que es dos coma cero ocho siete»
            self.en("v2087")
            self.play(*revelar(A[1], A[2]), run_time=self.dur(0.7))

            # «por la suma de los cuadrados de la cola»
            self.en("cuadrados")
            self.play(*revelar(B[0], B[1]), run_time=self.dur(0.9))

            # «una progresión de razón cero coma cero dos cinco»
            self.en("razon")
            self.play(GrowFromCenter(llave), FadeIn(l_razon), run_time=self.dur(0.8))

            # «que da cero coma cero dos cinco dos»
            self.en("v0252")
            self.play(*revelar(B[2], B[3]), run_time=self.dur(0.7))

            # «Resultado: cero coma cero cinco dos seis»
            self.en("resultado")
            self.add(res)
            self.play(*revelar(res), run_time=self.dur(0.9))
            self.play(Create(marco), run_time=0.4)
            self.sfx("impacto")

    # ---------------------------------------------------------------- b3
    def bloque3(self):
        self.corte()
        resta = oculta(formula(r"0{,}7386", "-", r"0{,}0526", "=", r"0{,}686", escala=1.5,
                               colores={0: ESTIMACION, 2: ERROR, 4: VERDE}).move_to([0, 2.7, 0]))
        be = barras_error([0.7386, 0.686], ["causal", "no causal"], centro=(-4.0, -0.9), ancho=3.0, alto=2.6, v_max=0.8,
                          colores=[ESTIMACION, VERDE])
        ok = tilde(VERDE, 0.5).move_to([-2.0, -0.6, 0])
        # una barra de error total, con la porción que se gana por mirar el futuro
        total = Rectangle(width=6.4, height=0.7, color=ESTIMACION, stroke_width=0).set_fill(ESTIMACION, 0.8).move_to([1.4, -0.4, 0])
        gana = Rectangle(width=6.4 * 0.0712, height=0.7, color=VERDE, stroke_width=0).set_fill(VERDE, 0.95)
        gana.align_to(total, RIGHT).align_to(total, DOWN)
        l_7 = formula(r"7\,\%", escala=1.3, colores={0: VERDE}).next_to(total, DOWN, buff=0.35).align_to(total, RIGHT)
        l_7.set_color(VERDE)
        l_fut = etiqueta("lo que gana mirar todo el futuro", VERDE, 0.45).next_to(total, UP, buff=0.35).align_to(total, RIGHT)
        interr = Text("¿dónde está la diferencia grande?", color=AMBAR, weight=BOLD).scale(0.55).move_to([1.6, -2.3, 0])
        dec_a = caja("con x[n]", MEDIDA, ancho=2.4, alto=0.9, scale=0.55).move_to([-2.0, -3.2, 0])
        dec_b = caja("sin x[n]", RUIDO, ancho=2.4, alto=0.9, scale=0.55).move_to([2.0, -3.2, 0])
        sig = MathTex("?", color=AMBAR).scale(1.4).move_to([0, -3.2, 0])
        with self.narrar("b3"):
            # «Cero coma siete tres ocho seis menos cero coma cero cinco dos seis»
            self.en("resta")
            self.add(resta)
            self.play(*revelar(resta[0], resta[1], resta[2]), run_time=self.dur(1.5))

            # «cero coma seis ocho seis»
            self.en("v0686")
            self.play(*revelar(resta[3], resta[4]), run_time=self.dur(0.7))

            # «justo el error del filtro no causal»
            self.en("nocausal")
            self.play(Create(be.base), *[FadeIn(e) for e in be.etiquetas], GrowFromEdge(be.barras[0], DOWN),
                      GrowFromEdge(be.barras[1], DOWN), run_time=self.dur(0.9))
            self.play(Create(ok), run_time=0.3)

            # «Todo encaja»
            self.en("encaja")
            self.play(Flash(resta, color=VERDE, flash_radius=1.2), run_time=self.dur(0.6))
            self.sfx("exito")

            # «mirar todo el futuro solo mejora un siete por ciento»
            self.en("siete")
            self.play(FadeIn(total), run_time=0.4)
            self.play(FadeIn(gana), FadeIn(l_7), FadeIn(l_fut), run_time=self.dur(0.9))

            # «¿Dónde está, entonces, la diferencia grande?»
            self.en("dondeesta")
            self.pop(interr)

            # «En una decisión mucho más pequeña»
            self.en("decision")
            self.play(FadeIn(dec_a, shift=UP * 0.2), FadeIn(dec_b, shift=UP * 0.2), run_time=self.dur(0.8))

            # «usar o no la muestra de ahora»
            self.en("ahora")
            self.pop(sig)
