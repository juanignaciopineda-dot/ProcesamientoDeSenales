"""Escena 22 — Cierre del episodio y anuncio del E7, «¿Cuál de ellas mandaron?»."""
from comun.escena import *


class Cierre(EscenaCurso):
    ESCENA = "22"

    def construct(self):
        self.repaso()
        self.anuncio()
        self.wait(1.0)
        self.limpiar()

    def repaso(self):
        rad = radar13().scale(1.0).move_to([-5.5, 2.4, 0])
        dq = formula("D", "=", "?", escala=1.0, colores={0: AMBAR, 2: AMBAR}).move_to([-3.6, 2.4, 0])
        sal = Tallos([2, 6, 9, 6, 2], centro=(0.5, 2.0), paso=0.5, unidad=0.2, color=ESTIMACION)
        anillo = Circle(radius=0.2, color=AMBAR, stroke_width=4).move_to(sal.pos(2))
        dd = MathTex("D", color=AMBAR).scale(0.9).move_to([3.0, 2.4, 0])
        fl = Arrow(sal.pos(2) + RIGHT * 0.3 + UP * 0.1, [2.7, 2.4, 0], color=AMBAR, buff=0, stroke_width=4)
        largo = Tallos([1] * 13, centro=(-4.2, -0.2), paso=0.25, unidad=0.5, color=SENAL)
        fino = Tallos([0] * 6 + [4] + [0] * 6, centro=(-4.2, -1.9), paso=0.25, unidad=0.3, color=AMBAR)
        dos = Tallos([0, 0, 0, 13, 0, 0, 13, 0, 0, 0], centro=(2.5, -1.0), paso=0.4, unidad=0.12, color=AMBAR)
        tira = celdas13(40, ancho=6.0, centro=(-2.0, -3.3), alto=0.45)
        db = MathTex(r"+2{,}8\,\text{dB}", color=AMBAR).scale(1.1).move_to([2.6, -3.3, 0])
        with self.narrar("b1"):
            # «si no sabes cuándo llega el eco»
            self.en("eco")
            self.play(FadeIn(rad), FadeIn(dq), run_time=self.dur(0.7))
            # «el pico de la salida lo mide»
            self.en("pico")
            self.play(FadeIn(sal), run_time=0.4)
            self.play(Create(anillo), GrowArrow(fl), FadeIn(dd), run_time=self.dur(0.7))
            # «un pulso largo»
            self.en("largo")
            self.play(FadeIn(largo), run_time=self.dur(0.5))
            # «con la autocorrelación estrecha»
            self.en("estrecha")
            self.play(FadeIn(fino), run_time=self.dur(0.6))
            # «separa dos ecos»
            self.en("separa")
            self.play(FadeIn(dos), run_time=self.dur(0.6))
            # «buscar en muchos sitios»
            self.en("buscar")
            self.play(FadeIn(tira), run_time=self.dur(0.6))
            # «cuesta señal»
            self.en("cuesta")
            self.pop(db)

    def anuncio(self):
        h0 = caja("solo ruido  H₀", RUIDO, ancho=3.4, alto=0.9, scale=0.5).move_to([-3.0, 2.0, 0])
        h1 = caja("hay señal  H₁", SENAL, ancho=3.4, alto=0.9, scale=0.5).move_to([3.0, 2.0, 0])
        tres = VGroup(Tallos([2, 2, 1], paso=0.35, unidad=0.35), Tallos([2, -1, -2], paso=0.35, unidad=0.35),
                      Tallos([-2, -2, -1], paso=0.35, unidad=0.35)).arrange(RIGHT, buff=1.6).move_to([0, -0.5, 0])
        q = Text("¿cuál?", color=ROJO, weight=BOLD).scale(0.9).move_to([0, 0.9, 0])
        fl = flecha([-1.0, -2.2, 0], [1.0, -2.2, 0], AMBAR)
        t1 = self.palabra("¿Cuál de ellas", TXT, 1.4).move_to([0, 0.7, 0])
        t2 = self.palabra("mandaron?", AMBAR, 1.4).move_to([0, -0.7, 0])
        with self.narrar("b2"):
            # «decidíamos solo entre»
            self.en("antes")
            self.play(*[FadeOut(m) for m in self.mobjects if m is not self.camera.frame], run_time=0.3)
            self.play(FadeIn(h0), FadeIn(h1), run_time=self.dur(0.6))
            # «hay señal»
            self.en("hay")
            self.resaltar(h1, color=AMBAR, run_time=0.5)
            # «no hay»
            self.en("nohay")
            self.resaltar(h0, color=AMBAR, run_time=0.5)
            # «una entre varias señales posibles»
            self.en("varias")
            self.play(FadeIn(tres), run_time=self.dur(0.9))
            # «hay que decir cuál»
            self.en("cual")
            self.pop(q)
            # «el próximo episodio»
            self.en("proximo")
            self.play(GrowArrow(fl), run_time=self.dur(0.6))
            # «¿cuál de ellas mandaron?»
            self.en("titulo")
            self.play(*[FadeOut(m) for m in (h0, h1, tres, q, fl)], run_time=0.3)
            self.pop(t1)
            self.pop(t2)
