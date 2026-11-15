"""Escena 14 — Cierre: resumen del episodio y anuncio del E6, «Fabricar el color y quitarlo»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        # arriba a la izquierda: un trozo cortado con campana, sin salto
        L1 = Lienzo(ancho=5.4, alto=1.5, t_rango=(0, 1), v_max=1.2, centro=(-3.6, 2.0))
        t = np.linspace(0, 1, 300, endpoint=False)
        trozo = L1.curva(t, np.cos(2 * np.pi * 10.5 * t) * valores_ventana("hann", 300), SENAL, 2.8)
        tij = tijeras().scale(0.7).move_to([-6.3, 3.2, 0])
        ok = tilde().scale(0.9).move_to([-0.9, 3.0, 0])
        # arriba a la derecha: las faldas de la rectangular contra las de Hann
        L2 = lienzo_db(ancho=5.2, alto=2.2, x_max=8, top=3.0, cx=3.6, db=60)
        c_rect = curva_f(L2, lambda x: nucleo_db("rect", x, piso=60), 0, 8, COLOR_VENTANA["rect"], 2.6, n=500)
        c_hann = curva_f(L2, lambda x: nucleo_db("hann", x, piso=60), 0, 8, COLOR_VENTANA["hann"], 3.2, n=500)
        # abajo a la izquierda: el tiempo compra resolución
        reloj_ = reloj().scale(0.9).move_to([-5.6, -1.9, 0])
        fl = flecha([-4.8, -1.9, 0], [-3.0, -1.9, 0], INK, 4)
        cartel = caja("resolución", AMBAR, ancho=2.8, alto=0.9, scale=0.6).move_to([-1.6, -1.9, 0])
        # abajo a la derecha: Welch
        fs = fichas(["media", "trozos", "Hann", "promedio"], AMBAR, ancho=2.4, alto=0.65, escala=0.45, buff=0.12,
                    direccion=DOWN, encendidas=True).move_to([4.2, -1.9, 0])
        # título del próximo episodio
        prox = etiqueta("próximo episodio", INK, 0.6).move_to([0, 2.4, 0])
        t1 = self.palabra("Fabricar el color", TXT, 1.3).move_to([0, 0.9, 0])
        t2 = self.palabra("y quitarlo", AMBAR, 1.3).move_to([0, -0.4, 0])
        e_blanco = Espectro(w_max=4, y_max=1.2, ancho=3.4, alto=1.3, centro=(-5.0, -2.2))
        plano = e_blanco.curva(lambda w: 0.6 + 0 * np.asarray(w), SENAL, 4.0)
        blq1 = BloqueLTI(r"H", centro=(0.0, -1.7), ancho=1.4, alto=0.9, largo=1.8, escala=0.8)
        e_color = Espectro(w_max=4, y_max=1.2, ancho=3.4, alto=1.3, centro=(4.9, -2.2))
        coloreado = e_color.curva(lambda w: 0.15 + 0.9 * np.exp(-(np.asarray(w) / 1.3) ** 2), AMBAR, 4.0)
        plano_der = e_color.curva(lambda w: 0.6 + 0 * np.asarray(w), SENAL, 4.0)
        blq2 = BloqueLTI(r"1/H", centro=(0.0, -1.7), ancho=1.4, alto=0.9, largo=1.8, escala=0.8)

        with self.narrar("b1"):
            # «cortar sin romper»
            self.en("cortar")
            self.play(FadeIn(tij, shift=RIGHT * 0.3), Create(L1.base()), Create(trozo), run_time=self.dur(1.0))
            self.play(FadeIn(ok, scale=0.5), run_time=0.3)

            # «una ventana suave frena la fuga»
            self.en("ventana")
            self.play(Create(L2.base()), Create(c_rect), Create(c_hann), run_time=self.dur(1.2))

            # «el tiempo grabado compra la resolución»
            self.en("tiempo")
            self.play(FadeIn(reloj_, scale=0.7), GrowArrow(fl), FadeIn(cartel, scale=0.8), run_time=self.dur(1.2))

            # «Welch junta todo en un método»
            self.en("welch")
            self.play(LaggedStart(*[FadeIn(f) for f in fs], lag_ratio=0.15), run_time=self.dur(1.2))

            # «En el próximo episodio»
            self.en("proximo")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.4)
            self.play(FadeIn(prox), run_time=0.3)

            # «Fabricar el color y quitarlo»
            self.en("titulo")
            self.pop(t1, t2)

            # «un filtro que pinta el ruido blanco del color que quieras»
            self.en("pinta")
            self.play(FadeOut(prox), t1.animate.scale(0.6).move_to([0, 3.4, 0]), t2.animate.scale(0.6).move_to([0, 2.7, 0]),
                      run_time=0.5)
            self.play(Create(e_blanco.ejes), Create(plano), FadeIn(blq1), run_time=self.dur(0.9))
            self.play(Create(e_color.ejes), Create(coloreado), run_time=self.dur(0.7))

            # «otro que lo deja blanco otra vez»
            self.en("blanquea")
            self.play(FadeOut(blq1), FadeIn(blq2), Transform(coloreado, plano_der), run_time=self.dur(1.2))

        self.wait(1.0)
        self.limpiar()
