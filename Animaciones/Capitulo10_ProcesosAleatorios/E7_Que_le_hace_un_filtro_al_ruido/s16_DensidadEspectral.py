"""Escena 16 — |H|² S_xx se parece a la densidad espectral de energía: S_xx es la densidad espectral de potencia."""
from comun.escena import *


class DensidadEspectral(EscenaCurso):
    ESCENA = "16"

    def construct(self):
        izq = formula(r"S_{yy}", "=", r"|H|^2", r"S_{xx}", escala=1.25).move_to([-3.6, 2.7, 0])
        tit_i = etiqueta("procesos", SENAL, 0.65).move_to([-3.6, 3.6, 0])
        tit_d = etiqueta("Señales y Sistemas", INK, 0.65).move_to([3.6, 3.6, 0])
        der = formula(r"E_y(\omega)", "=", r"|H|^2", r"E_x(\omega)", escala=1.25).move_to([3.6, 2.7, 0])
        t = np.linspace(0, 1, 100)
        L = Lienzo(ancho=2.0, alto=0.9, t_rango=(0, 1), v_max=1.3, centro=(-0.4, 1.0))
        sen = L.curva(t, np.sin(2 * PI * 3 * t) * np.exp(-2 * t), SENAL, 3)
        mini = BloqueLTI(r"h", centro=(2.6, 1.0), ancho=1.0, alto=0.7, largo=0.8, escala=0.6)
        sen_o = Lienzo(ancho=1.6, alto=0.9, t_rango=(0, 1), v_max=1.3, centro=(5.3, 1.0)).curva(t, 0.5 * np.sin(2 * PI * 3 * t) * np.exp(-2 * t), MEDIDA, 3)
        igual = formula(r"\approx", escala=2.0, colores={0: AMBAR}).move_to([0.05, 2.7, 0])
        ax, lab = ejes((0, 10), (0, 1.3), ancho=6.4, alto=2.0, x_label=r"\omega")
        g = VGroup(ax, lab).move_to([0.0, -1.0, 0])
        curva = ax.plot(lambda w: 0.15 + 0.85 * np.exp(-((w - 3.0) / 1.3) ** 2) + 0.45 * np.exp(-((w - 7.0) / 0.9) ** 2),
                        x_range=[0, 10], color=AMBAR, stroke_width=5)
        area = ax.get_area(curva, x_range=(0, 10), color=AMBAR, opacity=0.3)
        bandas = VGroup(*[Line(ax.c2p(w, 0), ax.c2p(w, 1.25), color=INK, stroke_width=1.5, stroke_opacity=0.6)
                          for w in np.linspace(0.5, 9.5, 10)])
        nombre = self.palabra("densidad espectral de potencia", AMBAR, 0.85).move_to([0, -3.6, 0])

        with self.narrar("b1"):
            # «el módulo de hache al cuadrado»
            self.en("modulo")
            self.play(FadeIn(izq[:3]), FadeIn(tit_i), run_time=self.dur(0.9))

            # «por ese sub equis equis»
            self.en("por_s")
            self.play(FadeIn(izq[3]), run_time=self.dur(0.5))

            # «Señales y Sistemas»
            self.en("sys")
            self.play(FadeIn(tit_d), run_time=self.dur(0.5))

            # «densidad espectral de energía»
            self.en("energia")
            self.play(FadeIn(der), run_time=self.dur(1.0))

            # «de una señal»
            self.en("de_senal")
            self.play(Create(sen), run_time=self.dur(0.8))

            # «al pasar por un filtro»
            self.en("pasa_filtro")
            self.play(FadeIn(mini), Create(sen_o), run_time=self.dur(0.8))

            # «No es casualidad»
            self.en("casualidad")
            self.pop(igual)

            # «Ese sub equis equis»
            self.en("s_xx")
            self.play(izq[3].animate.set_color(AMBAR), run_time=self.dur(0.5))

            # «cómo se reparte la potencia»
            self.en("reparte")
            self.play(FadeIn(g), Create(curva), FadeIn(area), run_time=self.dur(1.2))

            # «entre las frecuencias»
            self.en("entre")
            self.play(Create(bandas), run_time=self.dur(0.8))

            # «densidad espectral de potencia»
            self.en("nombre")
            self.pop(nombre)
        self.wait(1.0)
        self.limpiar()
