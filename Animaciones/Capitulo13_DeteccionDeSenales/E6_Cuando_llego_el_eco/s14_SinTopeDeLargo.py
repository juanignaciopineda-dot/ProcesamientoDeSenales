"""Escena 14 — Sesenta y cuatro muestras: pico de un solo desplazamiento, sin el tope de Barker."""
from comun.escena import *


def _ac_chirp(x):
    # dibujo esquemático: pico fino y lóbulos pequeños (unos −21 dB)
    return np.exp(-(x / 0.55) ** 2) + 0.085 * np.abs(np.sin(2.6 * x)) * np.exp(-np.abs(x) / 9.0) * (np.abs(x) > 1.2)


class SinTopeDeLargo(EscenaCurso):
    ESCENA = "14"

    def construct(self):
        Lc = Lienzo(ancho=8.0, alto=1.3, t_rango=(0, 1), v_max=1.0, centro=(-1.5, 3.1))
        t = np.linspace(0, 1, 600)
        ch = Lc.curva(t, np.cos(2 * np.pi * (3 * t + 6 * t ** 2)), SENAL, 3.0)
        n64 = Text("64 muestras", color=TXT).scale(0.55).move_to([5.0, 3.1, 0])
        La = Lienzo(ancho=11.0, alto=2.6, t_rango=(-10, 10), v_max=1.1, centro=(0.0, 0.4))
        ac = curva_f(La, _ac_chirp, -10, 10, AMBAR, 4.0, n=400)
        ejeh = La.base()
        solo = BraceBetweenPoints(La.p(-0.6, -0.05), La.p(0.6, -0.05), direction=DOWN, color=AMBAR)
        solot = Text("un solo desplazamiento", color=AMBAR).scale(0.45).next_to(solo, DOWN, buff=0.05)
        lob = VGroup(DashedLine(La.p(-10, 0.085), La.p(10, 0.085), color=ROJO, stroke_width=3),
                     Text("lóbulos", color=ROJO).scale(0.45).move_to(La.p(7.4, 0.3)))
        db = MathTex(r"-21\,\text{dB}", color=VERDE).scale(0.9).move_to(La.p(-6.8, 0.55))
        fdb = Arrow(La.p(-6.8, 0.42), La.p(-6.8, 0.1), color=VERDE, buff=0, stroke_width=4)
        largo = Text("128 · 256 · 512 …", color=AMBAR, weight=BOLD).scale(0.6).move_to([5.0, 2.2, 0])
        bk = Tallos(list(BARKER13), centro=(-5.0, -2.9), paso=0.25, unidad=0.3, color=SENAL)
        mu = muro(0.9, 0.3).move_to([-2.9, -2.9, 0])
        t13 = Text("13", color=ERROR, weight=BOLD).scale(0.6).move_to([-2.3, -2.9, 0])
        est = Star(color=AMBAR, fill_opacity=0.9).scale(0.28).move_to([0.2, -2.9, 0])
        comp = Text("comprimir el pulso", color=AMBAR, weight=BOLD).scale(0.5).move_to([2.2, -2.9, 0])
        nom = Text("medir D", color=INK).scale(0.5).move_to([5.3, -2.9, 0])
        cr = cruz(ROJO, 0.55).move_to([6.3, -2.9, 0])
        with self.narrar("b1"):
            # «Con sesenta y cuatro muestras»
            self.en("n64")
            self.play(Create(ch), FadeIn(n64), run_time=self.dur(0.9))
            # «el pico ocupa un solo desplazamiento»
            self.en("solo")
            self.play(Create(ejeh), Create(ac), run_time=self.dur(0.9))
            self.play(Create(solo), FadeIn(solot), run_time=0.4)
            # «los lóbulos laterales quedan»
            self.en("lobulos")
            self.play(Create(lob[0]), FadeIn(lob[1]), run_time=self.dur(0.8))
            # «unos veintiún decibelios más abajo»
            self.en("db21")
            self.play(FadeIn(db), GrowArrow(fdb), run_time=self.dur(0.8))
            # «tan largo como se quiera»
            self.en("largo")
            self.play(FadeIn(largo), run_time=self.dur(0.6))
            # «cosa que no pasa con Barker»
            self.en("barker")
            self.play(FadeIn(bk), FadeIn(mu), FadeIn(t13), run_time=self.dur(0.8))
            # «Pero la ventaja mayor»
            self.en("ventaja")
            self.pop(est)
            # «de comprimir el pulso»
            self.en("comprimir")
            self.play(FadeIn(comp), run_time=self.dur(0.5))
            # «no es medir mejor un retardo»
            self.en("nomedir")
            self.play(FadeIn(nom), FadeIn(cr), run_time=self.dur(0.5))
        self.wait(1.0)
        self.limpiar()
