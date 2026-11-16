"""Escena 26 — Por el aire la señal llega demasiado bien: cómo se la lleva por debajo del ruido térmico."""
from comun.escena import *
from comun.figuras_lora import *


class BajarLaSenal(EscenaCurso):
    ESCENA = "26"

    def construct(self):
        a1 = antena_simple(TXT, 1.0).move_to([-5.2, 3.2, 0])
        a2 = antena_simple(TXT, 1.0).move_to([-1.2, 3.2, 0])
        onda = onda_radio([-4.7, 3.2, 0], [-1.7, 3.2, 0], CIAN, 5, 0.25, 3.5)
        bien = Text("Demasiado bien", color=VERDE, weight=BOLD).scale(0.8).move_to([3.0, 3.2, 0])
        E = EjesXY(centro=(-1.9, -0.9), ancho=7.2, alto=4.6, x=(-5, -95), y=(-25, 20),
                   x_marcas=ATEN_DB, y_marcas=(-20, -10, 0, 10, 20), rot_x="Atenuación del TX (dB)",
                   rot_y="SNR (dB)", escala=0.45)
        nx = VGroup(*E.marcas[:5])
        ny = VGroup(*E.marcas[5:])
        pts = E.puntos(ATEN_DB, ATEN_SNR, AMBAR, 0.13)
        linea = E.curva(ATEN_DB, ATEN_SNR, AMBAR, 3)
        linea.permitir_encima = True      # los rótulos de ganancia van pegados a los puntos
        agc = Text("AGC", color=CIAN, weight=BOLD).scale(1.0).move_to([4.9, 1.3, 0])
        gan = VGroup(*[Text(str(g), color=CIAN, weight=BOLD).scale(0.45).move_to(E.p(a, s) + DOWN * 0.42)
                       for a, s, g in zip(ATEN_DB, ATEN_SNR, ATEN_GANANCIA)])
        rgan = Text("Ganancia del RX (dB)", color=CIAN, weight=BOLD).scale(0.48).move_to([4.9, 0.55, 0])
        banda = Rectangle(width=7.2, height=(12 / 45) * 4.6, color=ERROR, stroke_width=2).set_fill(ERROR, 0.2)
        banda.move_to((E.p(-5, -22) + E.p(-95, -10)) / 2)
        rb = Text("Aquí cambia el FER", color=ERROR, weight=BOLD).scale(0.5).move_to(banda.get_center() + LEFT * 1.2)
        cua = cuaderno_lora().scale(0.95).move_to([4.9, 2.9, 0])
        enc = Text("Muestras × escala", color=AMBAR, weight=BOLD).scale(0.58).move_to([4.9, -0.7, 0])
        fl = Arrow(E.p(-89, 10.6) + DOWN * 0.75, E.p(-89, -14), color=AMBAR, stroke_width=6, buff=0,
                   max_tip_length_to_length_ratio=0.2)
        ter = Text("Ruido térmico del RX", color=RUIDO, weight=BOLD).scale(0.5).move_to([4.9, -1.9, 0])
        que = Text("No cambia", color=RUIDO, weight=BOLD).scale(0.7).move_to([4.5, -2.7, 0])
        ok = tilde(VERDE, 0.8).move_to([6.3, -2.7, 0])
        with self.narrar("b1"):
            # «por el aire»
            self.en("aire")
            self.play(FadeIn(a1), FadeIn(a2), Create(onda, rate_func=linear), run_time=self.dur(0.9))
            # «llega demasiado bien»
            self.en("bien")
            self.pop(bien)
            # «se atenúe el transmisor»
            self.en("atenua")
            self.play(FadeIn(E.ejes), FadeIn(E.guias), FadeIn(E.rots), FadeIn(ny), run_time=self.dur(0.7))
            # «desde diez hasta ochenta y nueve decibelios»
            self.en("rango")
            self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.1) for n in nx], lag_ratio=0.3), run_time=self.dur(1.5))
            # «la relación señal a ruido medida»
            self.en("snr")
            self.resaltar(E.rots[1], color=AMBAR, escala=1.3, run_time=self.dur(0.6))
            # «no baja de diez»
            self.en("nobaja")
            self.play(LaggedStart(*[FadeIn(p, scale=2.0) for p in pts], lag_ratio=0.15), Create(linea),
                      run_time=self.dur(0.9))
            # «El control automático de ganancia»
            self.en("agc")
            self.pop(agc)
            # «sube lo mismo que baja la señal»
            self.en("sube")
            self.play(LaggedStart(*[FadeIn(g, shift=UP * 0.1) for g in gan], lag_ratio=0.25), FadeIn(rgan),
                      run_time=self.dur(1.4))
        with self.narrar("b2"):
            # «entre menos veintidós y menos diez»
            self.en("zona")
            self.play(*[FadeOut(m) for m in (a1, a2, onda, bien)], FadeIn(banda), FadeIn(rb), run_time=self.dur(0.7))
            # «La solución del cuaderno»
            self.en("solucion")
            self.play(FadeIn(cua, shift=UP * 0.2), run_time=self.dur(0.5))
            # «la atenuación al máximo»
            self.en("max")
            self.resaltar(pts[4], color=TXT, escala=2.0, run_time=self.dur(0.6))
            # «encoger las muestras»
            self.en("encoger")
            self.pop(enc)
            # «La señal baja»
            self.en("baja")
            self.play(GrowArrow(fl), run_time=self.dur(0.9))
            # «el ruido térmico del receptor»
            self.en("termico")
            self.play(FadeIn(ter, shift=UP * 0.15), run_time=self.dur(0.5))
            # «se queda donde estaba»
            self.en("queda")
            self.pop(que)
            # «el ruido de verdad»
            self.en("verdad")
            self.play(Create(ok), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
