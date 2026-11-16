"""Escena 03 — Qué es LoRa (alcance a cambio de velocidad) y el artículo de Vangelista."""
from comun.escena import *
from comun.figuras_lora import *


class QueEsLoRa(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.campo()
        self.articulo()
        self.wait(1.0)
        self.limpiar()

    def campo(self):
        suelo = Line([-6.6, -1.3, 0], [6.6, -1.3, 0], color=INK, stroke_width=3)
        sen = sensor_campo().scale(2.3)
        sen.shift([-5.2, -1.3, 0] - sen.get_bottom())
        pil = pila_icono().scale(1.1).move_to([-3.3, -0.7, 0])
        torre = antena(TXT).scale(1.9)
        torre.shift([5.3, -1.3, 0] - torre.get_bottom())
        km = cota([-4.6, -2.0, 0], [4.9, -2.0, 0], "10 km", lado=DOWN, escala=0.75)
        nums = Text("21 · 7 · 20", color=AMBAR, weight=BOLD).scale(0.75).move_to(sen.punta() + UP * 0.45 + RIGHT * 1.1)
        vel = Text("Velocidad", color=INK, weight=BOLD).scale(0.95).move_to([-4.6, 3.4, 0])
        tac = tachar(vel)
        alc = Text("Alcance", color=VERDE, weight=BOLD).scale(0.95).move_to([-0.8, 3.4, 0])
        poc = Text("Poco consumo", color=VERDE, weight=BOLD).scale(0.95).move_to([2.8, 3.4, 0])
        lora = self.palabra("LoRa", AMBAR, 2.2).move_to([0, 1.7, 0])
        lr = Text("Long Range", color=TXT, weight=BOLD).scale(1.1).move_to([0, 0.0, 0])
        cam = VGroup(Text("Velocidad", color=INK, weight=BOLD).scale(0.9),
                     Arrow(ORIGIN, RIGHT * 1.4, color=AMBAR, stroke_width=5, buff=0),
                     Text("Distancia", color=VERDE, weight=BOLD).scale(0.9)).arrange(RIGHT, buff=0.35)
        cam.move_to([0, -1.9, 0])
        with self.narrar("b1"):
            # «un sensor en mitad del campo»
            self.en("sensor")
            self.play(Create(suelo), FadeIn(sen, shift=UP * 0.3), run_time=self.dur(0.8))
            # «una pila»
            self.en("pila")
            self.pop(pil)
            # «a kilómetros»
            self.en("km")
            self.play(FadeIn(torre), run_time=0.4)
            self.play(FadeIn(km), run_time=self.dur(0.6))
            # «unos pocos números al día»
            self.en("numeros")
            self.play(FadeIn(nums), run_time=0.3)
            self.play(nums.animate(path_arc=-0.5).move_to([2.2, 1.4, 0]), run_time=self.dur(1.2))
            # «No necesita velocidad»
            self.en("veloc")
            self.play(FadeOut(nums), FadeIn(vel), run_time=0.3)
            self.play(Create(tac), run_time=self.dur(0.4))
            # «alcance»
            self.en("alcance")
            self.pop(alc)
            # «gastar muy poco»
            self.en("poco")
            self.pop(poc)
            # «LoRa»
            self.en("lora")
            self.corte()
            self.pop(lora)
            # «largo alcance»
            self.en("largo")
            self.play(FadeIn(lr, shift=UP * 0.2), run_time=self.dur(0.5))
            # «cambia velocidad por distancia»
            self.en("cambia")
            self.play(FadeIn(cam[0]), run_time=0.3)
            self.play(GrowArrow(cam[1]), FadeIn(cam[2]), run_time=self.dur(0.5))

    def articulo(self):
        can = candado().scale(1.5).move_to([-4.8, 2.0, 0])
        ec = MathTex("c(t)", "=", "?", color=TXT).scale(1.5).move_to([-1.4, 2.0, 0])
        ec[2].set_color(AMBAR)
        anio = Text("2017", color=AMBAR, weight=BOLD).scale(1.3).move_to([3.6, 2.4, 0])
        autor = Text("L. Vangelista", color=TXT, weight=BOLD).scale(0.75).move_to([3.6, 1.4, 0])
        docs = VGroup(*[documento(TXT).scale(1.5) for _ in range(4)]).arrange(RIGHT, buff=0.5).move_to([-0.6, -1.6, 0])
        ok = tilde(VERDE, 0.9).move_to([3.6, -1.6, 0])
        fs = Text("Frequency Shift", color=TXT, weight=BOLD).scale(1.15).move_to([0, 2.0, 0])
        cm = Text("Chirp Modulation", color=TXT, weight=BOLD).scale(1.15).move_to([0, 0.6, 0])
        sig = Text("FSCM", color=AMBAR, weight=BOLD).scale(1.8).move_to([0, -1.6, 0])
        with self.narrar("b2"):
            # «está patentada»
            self.en("patente")
            self.corte()
            self.pop(can)
            # «nadie la describió con ecuaciones»
            self.en("nadie")
            self.play(FadeIn(ec[0]), FadeIn(ec[1]), run_time=0.4)
            self.pop(ec[2], sonido=None)
            # «dos mil diecisiete»
            self.en("anio")
            self.pop(anio)
            # «Lorenzo Vangelista»
            self.en("autor")
            self.play(FadeIn(autor, shift=UP * 0.2), run_time=self.dur(0.5))
            # «cuatro páginas»
            self.en("paginas")
            self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.2) for d in docs], lag_ratio=0.25), run_time=self.dur(0.9))
            # «la primera descripción rigurosa»
            self.en("rigurosa")
            self.play(Create(ok), run_time=self.dur(0.5))
            self.sfx("exito")
            # «un nombre mejor»
            self.en("nombre")
            self.play(*[FadeOut(m) for m in (can, ec, anio, autor, docs, ok)], run_time=self.dur(0.5))
            # «desplazamiento de frecuencia»
            self.en("fs")
            self.pop(fs)
            # «de un chirp»
            self.en("chirp")
            self.pop(cm)
            self.play(FadeIn(sig, scale=1.3), run_time=0.4)
