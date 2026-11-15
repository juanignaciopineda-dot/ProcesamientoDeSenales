"""Escena 12 — En cada frecuencia, dos procesos son dos variables: las dos flechas del capítulo 7."""
from comun.escena import *

ANGULOS = [25, 70, 40, 100, 15, 60]      # ángulo entre las dos flechas en cada rebanada


class DosVariablesPorFrecuencia(EscenaCurso):
    ESCENA = "12"

    def construct(self):
        marco = caja("la idea del capítulo", AMBAR, ancho=4.4, alto=0.8).move_to([0, 3.4, 0])
        L = Lienzo(ancho=12.0, alto=1.7, t_rango=(-6, 6), v_max=1.0, centro=(0, 1.6))
        base = L.base(INK, 2.5)
        c_xx = curva_f(L, psd_tele, -6, 6, SENAL, 4.0)
        c_yy = curva_f(L, lambda w: 0.7 * 4.0 / (4.0 + (np.asarray(w) - 1.5) ** 2), -6, 6, MEDIDA, 4.0)
        cortes = VGroup(*[Line([x, 2.7, 0], [x, -2.0, 0], color=INK, stroke_width=2, stroke_opacity=0.7)
                          for x in (-6, -4, -2, 0, 2, 4, 6)])
        centros = [-5, -3, -1, 1, 3, 5]
        pares = VGroup()
        for xc, ang in zip(centros, ANGULOS):
            o = [xc - 0.6, -1.0]
            pares.add(VGroup(flecha_c(o, 1.1, 0, SENAL, ancho=5), flecha_c(o, 1.1, ang, MEDIDA, ancho=5)))
        o3 = np.array([centros[2] - 0.6, -1.0, 0.0])
        arco = Arc(radius=0.45, start_angle=0, angle=np.deg2rad(ANGULOS[2]), color=AMBAR, stroke_width=4
                   ).move_arc_center_to(o3)
        th = MathTex(r"\theta", color=AMBAR).scale(0.6).move_to(o3 + np.array([0.75, 0.2, 0]))
        rho = formula(r"\rho=\cos\theta", escala=0.9, colores={0: AMBAR}).move_to([-1.0, -2.8, 0])
        desig = formula(r"|\rho|\le 1", escala=0.9, colores={0: AMBAR}).move_to([3.0, -2.8, 0])
        q = etiqueta("¿qué se hace con dos variables?", AMBAR, 0.6).move_to([0, -3.5, 0])
        F = Flechas(origen=(-3.2, -1.2), largo=3.4, angulo=50, largo_objetivo=3.4)
        l_dato = etiqueta("dato", AZUL, 0.55).move_to([1.2, -1.2, 0])
        l_obj = etiqueta("lo que quiero", INK, 0.55).move_to([1.1, 1.8, 0])
        l_err = etiqueta("error", ROJO, 0.55).move_to([0.4, 0.3, 0])
        with self.narrar("b1"):
            # «la idea que se lleva el capítulo»
            self.en("idea")
            self.corte()
            self.play(FadeIn(marco), run_time=self.dur(0.5))

            # «dos procesos»
            self.en("procesos")
            self.play(Create(base), Create(c_xx), Create(c_yy), run_time=self.dur(1.3))

            # «en cada frecuencia por separado»
            self.en("rebanadas")
            self.play(Create(cortes), run_time=self.dur(0.8))

            # «dos variables aleatorias»
            self.en("variables")
            self.play(LaggedStart(*[FadeIn(p) for p in pares], lag_ratio=0.2), run_time=self.dur(1.6))

            # «Mismo rho»
            self.en("rho")
            self.pop(rho)

            # «misma desigualdad»
            self.en("desig")
            self.pop(desig)

            # «las mismas dos flechas con un ángulo»
            self.en("flechas")
            self.play(Create(arco), FadeIn(th), run_time=self.dur(0.7))

            # «qué se hace con dos variables»
            self.en("quehace")
            self.play(FadeIn(q), run_time=self.dur(0.6))

            # «estimar una a partir de la otra»
            self.en("estimar")
            self.corte()
            self.play(GrowArrow(F.presente), GrowArrow(F.futuro), FadeIn(l_dato), FadeIn(l_obj),
                      run_time=self.dur(1.0))

            # «proyectando una flecha sobre la otra»
            self.en("proyecta")
            self.play(Create(F.sombra), run_time=self.dur(0.6))
            self.play(Create(F.error), Create(F.recto), FadeIn(l_err), run_time=self.dur(0.6))

        self.wait(1.0)
        self.limpiar()
