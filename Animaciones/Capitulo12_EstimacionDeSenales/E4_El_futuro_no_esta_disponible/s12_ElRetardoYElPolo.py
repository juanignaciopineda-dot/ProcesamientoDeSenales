"""Escena 12 — z⁻¹ como retardo, el filtro como suma de retardos y el eco del 0,6 como cociente con polo en 0,6."""
from comun.escena import *


class ElRetardoYElPolo(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        nota_ = self.palabra("notación", AMBAR, 0.8).move_to([0, 3.4, 0])
        z = formula("z^{-1}", escala=1.5, colores={0: AMBAR}).move_to([-5.6, 2.4, 0])
        ent = Tallos([0, 1, 2, 1, 0, 0], centro=(-4.0, 1.1), paso=0.5, unidad=0.4, color=SENAL)
        bz = caja_tex(r"z^{-1}", AMBAR, ancho=1.3, alto=0.9, escala=0.8).move_to([-1.2, 1.1, 0])
        sal = Tallos([0, 0, 1, 2, 1, 0], centro=(1.7, 1.1), paso=0.5, unidad=0.4, color=SENAL)
        a1 = flecha([-2.2, 1.1, 0], bz.get_left(), INK, 3)
        a2 = flecha(bz.get_right(), [0.0, 1.1, 0], INK, 3)
        f = oculta(formula("F(z)", "=", "h_0", "+", "h_1", "z^{-1}", "+", "h_2", "z^{-2}", r"+\cdots",
                           escala=1.1, colores={0: ESTIMACION, 4: AMBAR, 7: AMBAR, 2: AMBAR}))
        f.move_to([0.4, -0.4, 0])
        self.add(f)
        L = Lienzo(ancho=3.2, alto=1.0, t_rango=(0, 5), v_max=1.2, centro=(-4.6, -1.9))
        tt = np.linspace(0, 5, 60)
        eco = L.curva(tt, 0.8 * serie(7, 60, 0.6), SENAL, 3.0)
        fc = formula("F(z)=", r"\frac{1}{1-0{,}6\,z^{-1}}", escala=0.95, colores={0: ESTIMACION}).move_to([-0.3, -1.9, 0])
        fs = oculta(formula("=", "1", "+", r"0{,}6\,z^{-1}", "+", r"0{,}36\,z^{-2}", r"+\cdots",
                            escala=0.95, colores={3: AMBAR, 5: AMBAR}))
        fs.move_to([0.8, -3.1, 0])
        self.add(fs)
        polo = caja("polo = 0,6", AMBAR, ancho=2.8, alto=0.8, scale=0.55).move_to([5.0, -1.9, 0])
        with self.narrar("b1"):
            # «Un poco de notación»
            self.en("nota")
            self.pop(nota_)

            # «Zeta a la menos uno»
            self.en("z")
            self.pop(z)

            # «un retardo de una muestra»
            self.en("retardo")
            self.play(FadeIn(ent), FadeIn(a1), FadeIn(bz), run_time=self.dur(0.7))
            self.play(GrowArrow(a2), FadeIn(sal), run_time=self.dur(0.7))

            # «suma de retardos»
            self.en("suma")
            self.play(*revelar(f[0], f[1], f[5], f[8]), run_time=self.dur(0.7))

            # «con sus coeficientes»
            self.en("coefs")
            self.play(*revelar(f[4], f[7]), run_time=self.dur(0.6))

            # «hache cero»
            self.en("h0")
            self.play(*revelar(f[2]), run_time=self.dur(0.5))

            # «más hache uno zeta a la menos uno»
            self.en("h1")
            self.play(*revelar(f[3], f[6], f[9]), run_time=self.dur(0.7))

            # «El eco del cero coma seis»
            self.en("eco")
            self.play(Create(L.base()), Create(eco), run_time=self.dur(1.0))

            # «uno entre uno menos cero coma seis zeta a la menos uno»
            self.en("cociente")
            self.play(FadeIn(fc, shift=UP * 0.15), run_time=self.dur(0.8))

            # «uno, más cero coma seis retardado»
            self.en("s1")
            self.play(*revelar(fs[0], fs[1], fs[2], fs[3]), run_time=self.dur(0.6))

            # «más cero coma treinta y seis retardado dos veces»
            self.en("s2")
            self.play(*revelar(fs[4], fs[5]), run_time=self.dur(0.6))

            # «y así»
            self.en("yasi")
            self.play(*revelar(fs[6]), run_time=self.dur(0.4))

            # «Tiene un polo en cero coma seis»
            self.en("polo")
            self.play(FadeIn(polo, scale=0.7), run_time=self.dur(0.5))

        self.wait(1.0)
        self.limpiar()
