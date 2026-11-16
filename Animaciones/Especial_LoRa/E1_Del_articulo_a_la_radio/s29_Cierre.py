"""Escena 29 — Cierre: la cadena completa y lo que el episodio junta del curso."""
from comun.escena import *
from comun.figuras_lora import *


class Cierre(EscenaCurso):
    ESCENA = "29"

    def construct(self):
        self.cadena()
        self.curso()
        self.wait(1.5)
        self.limpiar()

    def cadena(self):
        arriba, fa = fila_bloques(["Bits → 20", "Chirp desplazado", "+ Ruido"], [AZUL, AMBAR, RUIDO],
                                  centro=(0, 2.7), hueco=0.9, alto=1.0, escala=0.62)
        # la fila del receptor va de derecha a izquierda, debajo de «+ Ruido»
        abajo = [bloque(x, c, None, 1.0, 0.62) for x, c in
                 (("Máximo → 20", AMBAR), ("FFT", AZUL), ("× Chirp que baja", CIAN))]
        VGroup(*abajo).arrange(RIGHT, buff=0.9)
        VGroup(*abajo).shift([arriba[2].get_center()[0] - abajo[2].get_center()[0], 0.7 - abajo[2].get_center()[1], 0])
        abajo = abajo[::-1]                     # en el orden en que se nombran
        fb = [Arrow(a.get_left(), b.get_right(), color=INK, stroke_width=3, buff=0.06,
                    max_tip_length_to_length_ratio=0.35) for a, b in zip(abajo[:-1], abajo[1:])]
        codo = Arrow(arriba[2].get_bottom(), abajo[0].get_top(), color=INK, stroke_width=3, buff=0.06,
                     max_tip_length_to_length_ratio=0.35)
        pre = Text("Preámbulo: 8 chirps", color=AMBAR, weight=BOLD).scale(0.6).move_to([-3.9, -2.0, 0])
        P = PlanoTF(centro=(2.3, -2.0), ancho=6.4, alto=1.3, n=8, rotulos=False)
        rampas = VGroup(*[P.rampa(0, i, grosor=4) for i in range(8)])
        with self.narrar("b1"):
            # «Los bits se agrupan en un número»
            self.en("bits")
            self.play(FadeIn(arriba[0], shift=RIGHT * 0.2), run_time=self.dur(0.5))
            # «El número desplaza un chirp»
            self.en("chirp")
            self.play(GrowArrow(fa[0]), FadeIn(arriba[1]), run_time=self.dur(0.5))
            # «El aire le suma ruido»
            self.en("ruido")
            self.play(GrowArrow(fa[1]), FadeIn(arriba[2]), run_time=self.dur(0.5))
            # «deshace el chirp»
            self.en("des")
            self.play(GrowArrow(codo), FadeIn(abajo[0]), run_time=self.dur(0.5))
            # «transforma»
            self.en("fft")
            self.play(GrowArrow(fb[0]), FadeIn(abajo[1]), run_time=self.dur(0.4))
            # «busca el pico»
            self.en("pico")
            self.play(GrowArrow(fb[1]), FadeIn(abajo[2]), run_time=self.dur(0.4))
            # «un preámbulo»
            self.en("pre")
            self.play(FadeIn(pre), FadeIn(P), LaggedStart(*[Create(r) for r in rampas], lag_ratio=0.12),
                      run_time=self.dur(1.2))

    def curso(self):
        docs = VGroup(*[documento(TXT).scale(1.2) for _ in range(4)]).arrange(RIGHT, buff=0.25).move_to([-4.6, 2.2, 0])
        cua = cuaderno_lora().scale(1.1).move_to([0, 2.2, 0])
        pl = pluto().scale(1.1).move_to([4.6, 2.0, 0])
        f1 = Arrow([-2.6, 2.2, 0], [-1.6, 2.2, 0], color=INK, stroke_width=4, buff=0)
        f2 = Arrow([1.6, 2.2, 0], [2.9, 2.2, 0], color=INK, stroke_width=4, buff=0)
        pal = [Text(t, color=c, weight=BOLD).scale(0.62).move_to([x, 0.0, 0]) for t, c, x in
               (("Estimar", ESTIMACION, -5.4), ("Detectar", VERDE, -3.0), ("Filtro adaptado", CIAN, 0.2),
                ("Densidad espectral", MAGENTA, 4.4))]
        sen = sensor_campo().scale(1.9).move_to([-0.7, -2.3, 0])
        pil = pila_icono().scale(1.0).move_to([0.9, -2.7, 0])
        with self.narrar("b2"):
            # «Cuatro páginas de ecuaciones»
            self.en("paginas")
            self.corte()
            self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.15) for d in docs], lag_ratio=0.2), run_time=self.dur(0.9))
            # «un cuaderno»
            self.en("cuaderno")
            self.play(GrowArrow(f1), FadeIn(cua), run_time=self.dur(0.5))
            # «una radio»
            self.en("radio")
            self.play(GrowArrow(f2), FadeIn(pl), run_time=self.dur(0.5))
            # «Estimar», «detectar», «filtros adaptados», «densidad espectral»
            for marca, p in zip(("est", "det", "fa", "psd"), pal):
                self.en(marca)
                self.pop(p)
            # «un sensor que funciona con una pila»
            self.en("sensor")
            self.play(FadeIn(sen, shift=UP * 0.2), run_time=0.4)
            self.pop(pil)
