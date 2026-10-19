"""Escena 13 — Cierre: dos errores que son colas, el umbral que los reparte, y anuncio de «Un número y un umbral»."""
from comun.escena import *
from comun.figuras_c9e2 import *


class Cierre(EscenaCurso):
    ESCENA = "13"

    def construct(self):
        self.resumen()
        self.anuncio()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def resumen(self):
        T = Tabla22_9(("Solo ruido", "Hay avión"), ("Nada", "Avión"), centro=(-4.0, 2.2), ancho=1.1, alto=0.9,
                      escala=0.36)
        cruces = {(0, 1): T.marca(0, 1, tam=0.26), (1, 0): T.marca(1, 0, tam=0.26)}
        C = Campanas9(centro=(1.2, -2.6), ancho=8.5, alto=4.4, r_rango=(-3.0, 5.0))
        base = Line(C.p(-3), C.p(5), color=INK, stroke_width=2.4)
        c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        u = ValueTracker(CRUCE9)

        def colas_vivas():
            return VGroup(C.area(0, 1, u.get_value(), 5), C.area(2, 1, -3, u.get_value()))

        def umbral_vivo():
            return Line(C.p(u.get_value()), C.p(u.get_value()) + UP * 2.4, color=ESTIMACION, stroke_width=4)

        colas = always_redraw(colas_vivas)
        umb = always_redraw(umbral_vivo)
        creer = VGroup(MathTex("+", color=ERROR).scale(0.9), MathTex(r"\to\ ?", color=ESTIMACION).scale(0.9))
        creer.arrange(RIGHT, buff=0.15).move_to([4.5, 3.4, 0])
        V = CurvaVPP9(x0=2.4, x1=6.4, y0=0.5, y1=2.6, etiquetas=False)
        curva = V.curva()

        with self.narrar("b1"):
            # «dos maneras de equivocarse»
            self.en("dos")
            self.play(FadeIn(T), Create(cruces[(0, 1)]), Create(cruces[(1, 0)]), run_time=self.dur(0.6))

            # «la falsa alarma»
            self.en("fa")
            self.resaltar(T.cel[(0, 1)], color=ERROR)

            # «el fallo»
            self.en("fallo")
            self.resaltar(T.cel[(1, 0)], color=ERROR)

            # «colas de campana»
            self.en("colas")
            self.play(Create(base), Create(c0), Create(c1), run_time=self.dur(0.5))
            destinos = [C.p(2.4, 0.04), C.p(-0.4, 0.04)]
            self.play(*[cruces[k].copy().animate.move_to(d).set_opacity(0) for k, d in zip(((0, 1), (1, 0)), destinos)],
                      FadeIn(colas), FadeIn(umb), run_time=self.dur(0.7))

            # «Mover el umbral»
            self.en("umbral")
            self.play(u.animate.set_value(2.0), run_time=self.dur(0.8))

            # «una por otra»
            self.en("cambia")
            self.play(u.animate.set_value(0.9), run_time=self.dur(0.9))

            # «cuánto creerle a un positivo»
            self.en("creer")
            self.play(FadeIn(creer, shift=DOWN * 0.2), run_time=self.dur(0.4))

            # «lo raro que sea lo que buscas»
            self.en("raro")
            self.play(Create(V.ejes), Create(curva), run_time=self.dur(0.9))
        colas.clear_updaters()
        umb.clear_updaters()

    # ------------------------------------------------------------ b2
    def anuncio(self):
        C = Campanas9()
        eje = C.eje(marcas=(0, 1, 2))
        c0, c1 = C.campana(0, P0, C0), C.campana(2, P1, C1)
        cruce = Dot(C.p(CRUCE9, C.f(0, CRUCE9, P0)), radius=0.11, color=ESTIMACION)
        v142 = Text("1,42", color=ESTIMACION).scale(0.45).move_to(C.p(CRUCE9) + DOWN * 0.32 + RIGHT * 0.12)
        guia = DashedLine(C.p(CRUCE9), cruce.get_center(), color=ESTIMACION, stroke_width=3)
        duda = Text("?", color=ESTIMACION, weight=BOLD).scale(2.2).move_to([0, 2.6, 0])
        numero = casilla9("Un número", ESTIMACION, ancho=3.0, alto=0.9, escala=0.55).move_to([-2.3, 1.1, 0])
        umbral = VGroup(MathTex(r"\gtrless", color=TXT).scale(1.1),
                        casilla9("Umbral", ESTIMACION, ancho=2.6, alto=0.9, escala=0.55)).arrange(RIGHT, buff=0.3)
        umbral.next_to(numero, RIGHT, buff=0.3)
        ep = Text("Episodio 3", color=INK).scale(0.6).move_to([0, 1.3, 0])
        titulo = Text("Un número y un umbral", color=ESTIMACION, weight=BOLD).scale(1.15).move_to([0, 0.0, 0])

        with self.narrar("b2"):
            # «dónde se cruzan dos curvas»
            self.en("cruce")
            self.corte()
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.7))
            self.play(FadeIn(cruce, scale=0.4), Create(guia), FadeIn(v142), run_time=self.dur(0.5))

            # «¿Y si cualquier buena decisión»
            self.en("pregunta")
            plano = VGroup(eje, c0, c1, cruce, v142, guia)
            self.play(plano.animate.fade(0.7), run_time=self.dur(0.4))
            self.pop(duda)

            # «un solo número»
            self.en("numero")
            self.play(FadeOut(duda), FadeIn(numero, shift=UP * 0.2), run_time=self.dur(0.4))

            # «con un umbral»
            self.en("umbral")
            self.play(FadeIn(umbral, shift=LEFT * 0.2), run_time=self.dur(0.4))

            # «en el próximo episodio»
            self.en("proximo")
            self.play(FadeOut(plano), FadeOut(numero), FadeOut(umbral), FadeIn(ep), run_time=self.dur(0.5))

            # «un número y un umbral»
            self.en("titulo")
            self.pop(titulo, sonido="exito")
