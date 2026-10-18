"""Escena 07 — Test pregunta: el test que acierta el 99 % y las mil personas."""
from comun.escena import *


class TestPregunta(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.planteo()
        self.mil()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def planteo(self):
        c1 = caja("1 de cada 100 enfermo", ROJO, ancho=4.2, alto=0.9, scale=0.55).move_to([-4.6, 3.0, 0])
        c2 = caja("Enfermo: positivo 99 %", ROJO, ancho=4.2, alto=0.9, scale=0.55).move_to([0, 3.0, 0])
        c3 = caja("Sano: positivo 5 %", VERDE, ancho=4.2, alto=0.9, scale=0.55).move_to([4.6, 3.0, 0])
        # cien personas, una enferma
        cien = VGroup(*[Square(side_length=0.19, stroke_width=0).set_fill(VERDE, 0.9) for _ in range(100)])
        cien.arrange_in_grid(rows=10, cols=10, buff=0.05).move_to([-4.6, 1.0, 0])
        cien[0].set_fill(ROJO, 1)
        p_enf = persona(ROJO).scale_to_fit_height(1.0).move_to([-1.2, 1.0, 0])
        p_san = persona(VERDE).scale_to_fit_height(1.0).move_to([3.4, 1.0, 0])
        b2 = Rectangle(width=2.4, height=0.3, color=VERDE, stroke_width=3).move_to([0.9, 1.0, 0])
        r2 = Rectangle(width=2.4 * 0.99, height=0.3, stroke_width=0).set_fill(VERDE, 0.8).align_to(b2, LEFT)
        r2.match_y(b2)
        b3 = Rectangle(width=2.4, height=0.3, color=VERDE, stroke_width=3).move_to([5.6, 1.0, 0])
        r3 = Rectangle(width=2.4 * 0.05, height=0.3, stroke_width=0).set_fill(ROJO, 0.8).align_to(b3, LEFT)
        r3.match_y(b3)
        tira = tira_test07(0.7).move_to([-5.2, -2.1, 0])
        mas = Text("+", color=ERROR, weight=BOLD).scale(1.5).move_to(tira.ventana)
        preg = MathTex(r"P(\text{enfermo}\mid +)=\,?", color=AMBAR).scale(1.5).move_to([0.2, -1.6, 0])
        opciones = VGroup(*[caja(t, INK, ancho=1.9, alto=0.8, scale=0.7)
                            for t in ("99 %", "95 %", "50 %", "17 %")]).arrange(RIGHT, buff=0.5).move_to([0.5, -3.2, 0])
        self.opciones = opciones

        with self.narrar("b1"):
            # «una persona de cada cien»
            self.en("uno_cien")
            self.play(FadeIn(c1), FadeIn(cien), run_time=self.dur(0.7))
            self.play(cien[0].animate.scale(1.6), run_time=self.dur(0.4))

            # «Existe un test muy bueno»
            self.en("test")
            self.play(FadeIn(tira, shift=UP * 0.3), run_time=self.dur(0.5))

            # «si estás enfermo»
            self.en("enfermo")
            self.play(FadeIn(c2), FadeIn(p_enf), run_time=self.dur(0.5))

            # «el noventa y nueve por ciento»
            self.en("99")
            self.play(FadeIn(b2), GrowFromEdge(r2, LEFT), run_time=self.dur(0.6))

            # «Si estás sano»
            self.en("sano")
            self.play(FadeIn(c3), FadeIn(p_san), run_time=self.dur(0.5))

            # «solo un cinco por ciento»
            self.en("5")
            self.play(FadeIn(b3), GrowFromEdge(r3, LEFT), run_time=self.dur(0.6))

            # «Te haces el test y da positivo»
            self.en("positivo")
            self.pop(mas, sonido="error")

            # «¿Qué probabilidad hay de que estés enfermo?»
            self.en("pregunta")
            self.play(FadeIn(preg), run_time=self.dur(0.6))

            # «Elige una respuesta»
            self.en("elige")
            self.play(LaggedStart(*[FadeIn(o, shift=UP * 0.2) for o in opciones], lag_ratio=0.2),
                      run_time=self.dur(0.9))

    # ------------------------------------------------------------ b2
    def mil(self):
        ops = self.opciones
        t99 = Text("99 %", color=VERDE, weight=BOLD).scale(1.0)
        barra99 = barra_h(0.99, 2.9, -5.5, 5.5, VERDE, 0.5)
        barra95 = barra_h(0.95, 2.2, -5.5, 5.5, VERDE, 0.5)
        l99 = Text("99 %", color=TXT).scale(0.6).next_to(barra99, RIGHT, buff=0.2)
        l95 = Text("95 %", color=TXT).scale(0.6).next_to(barra95, RIGHT, buff=0.2)
        mayoria = Text("La mayoría", color=AMBAR, weight=BOLD).scale(0.7).move_to([-5.7, 3.7, 0])
        g = GrillaMil07(centro=(0, -0.3))
        etq_mil = Text("1.000 personas", color=TXT, weight=BOLD).scale(0.8).move_to([0, 1.3, 0])
        porc = Text("Porcentajes", color=INK).scale(0.8).move_to([-3.4, -2.7, 0])
        pers = Text("Personas", color=VERDE, weight=BOLD).scale(0.9).move_to([3.4, -2.7, 0])
        diez = Text("10 enfermas", color=ROJO, weight=BOLD).scale(0.75).move_to([-5.3, 0.6, 0])
        sanas = Text("990 sanas", color=VERDE, weight=BOLD).scale(0.75).move_to([5.3, -1.0, 0])
        tg = VGroup(g, etq_mil)

        with self.narrar("b2"):
            # «noventa y nueve, o noventa y cinco»
            self.en("encuesta")
            self.corte()
            self.play(FadeIn(mayoria), GrowFromEdge(barra99, LEFT), GrowFromEdge(barra95, LEFT),
                      FadeIn(l99), FadeIn(l95), run_time=self.dur(0.9))

            # «con mil personas»
            self.en("mil")
            self.play(FadeOut(VGroup(mayoria, barra99, barra95, l99, l95)), run_time=0.25)
            self.play(FadeIn(g), FadeIn(etq_mil), run_time=self.dur(0.8))

            # «más fácil que con porcentajes»
            self.en("facil")
            self.play(FadeIn(porc), run_time=self.dur(0.3))
            self.play(Create(tachar(porc)), FadeIn(pers), run_time=self.dur(0.5))

            # «Una de cada cien está enferma»
            self.en("una_cien")
            self.play(*[p.animate.set_fill(ROJO, 1) for p in g.pts[:10]], run_time=self.dur(0.6))

            # «son diez»
            self.en("diez")
            self.pop(diez)

            # «novecientas noventa están sanas»
            self.en("sanas")
            self.pop(sanas)
