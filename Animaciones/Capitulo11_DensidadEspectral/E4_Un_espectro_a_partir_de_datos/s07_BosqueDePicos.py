"""Escena 07 — El periodograma de la moneda: un bosque de picos que no baja aunque grabes más."""
from comun.escena import *


class BosqueDePicos(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.bosque()
        self.promedio_y_temblor()
        self.wait(1.0)
        self.limpiar()

    def bosque(self):
        P = Lienzo(ancho=11.0, alto=3.2, t_rango=(0, 1), v_max=5.0, centro=(0, -2.7))
        monedas = tira_pm1([1, -1, -1, 1, -1, 1, 1, -1], lado=0.5, color=SENAL, escala_txt=0.32).move_to([-3.0, 3.3, 0])
        t1s = etiqueta("1 s", AMBAR, 0.6).move_to([0.6, 3.3, 0])
        t10s = etiqueta("10 s", AMBAR, 0.6).move_to([0.6, 3.3, 0])
        plano = P.curva([0, 1], [1, 1], SENAL, 5)
        uno = MathTex("1", color=SENAL).scale(0.7).move_to(P.p(0, 1) + LEFT * 0.35)
        vals = periodograma_blanco(7, 80)
        bos = bosque_f(P, vals, MEDIDA, 2.6)
        orden = np.argsort(vals)
        xs = np.linspace(0, 1, 80)
        altos = VGroup(*[Dot(P.p(xs[i], min(vals[i], 4.9)), radius=0.1, color=VERDE) for i in orden[-2:]])
        ceros = VGroup(*[Dot(P.p(xs[i], vals[i]), radius=0.1, color=ROJO) for i in orden[:2]])
        nada = etiqueta("ninguno significa nada", ROJO, 0.6).move_to([4.2, 3.3, 0])
        opa = etiqueta("A) se aplana", TXT, 0.65).move_to([0, 2.0, 0])
        opb = etiqueta("B) picos más finos, igual de altos", TXT, 0.65).move_to([0, 1.2, 0])
        opc = etiqueta("C) no cambia nada", TXT, 0.65).move_to([0, 0.4, 0])
        with self.narrar("b1"):
            self.en("moneda")
            self.play(Create(P.base()), FadeIn(monedas), FadeIn(t1s), run_time=self.dur(0.7))
            self.en("plano")
            self.play(Create(plano), run_time=self.dur(0.6))
            self.en("uno")
            self.pop(uno)
            self.en("bosque")
            self.play(Create(bos, rate_func=linear), run_time=self.dur(1.6))
            self.en("alto")
            self.play(FadeIn(altos), run_time=0.4)
            self.en("cero")
            self.play(FadeIn(ceros), run_time=0.4)
            self.en("nada")
            self.play(FadeIn(nada), run_time=0.4)
            self.en("diez")
            self.play(ReplacementTransform(t1s, t10s), FadeOut(nada), run_time=0.4)
            self.en("opa")
            self.play(FadeIn(opa), run_time=0.4)
            self.en("opb")
            self.play(FadeIn(opb), run_time=0.4)
            self.en("opc")
            self.play(FadeIn(opc), run_time=0.4)
        self.opa, self.opb, self.opc = opa, opb, opc
        self.P, self.bos = P, bos
        self.altos, self.ceros = altos, ceros

    def promedio_y_temblor(self):
        P, bos = self.P, self.bos
        opa, opb, opc = self.opa, self.opb, self.opc
        t_a, t_c = tachar(opa), tachar(opc)
        bos10 = bosque_f(P, periodograma_blanco(8, 320), MEDIDA, 2.2)
        tope = DashedLine(P.p(0, 3), P.p(1, 3), color=ROJO, stroke_width=3.5)
        denso = etiqueta("más denso", VERDE, 0.65).move_to([-3.2, 1.9, 0])
        no_bajo = etiqueta("no más bajo", ROJO, 0.65).move_to([3.2, 1.9, 0])
        x_f = 0.5
        vert = Line(P.p(x_f, 0), P.p(x_f, 5.0), color=AMBAR, stroke_width=4)
        media = etiqueta("media 1", VERDE, 0.6).move_to([-4.4, 0.4, 0])
        flechas = DoubleArrow(P.p(x_f + 0.04, 0.0), P.p(x_f + 0.04, 2.0), color=ROJO, buff=0, stroke_width=4, max_tip_length_to_length_ratio=0.12)
        desv = etiqueta("desviación 1", ROJO, 0.6).move_to([4.4, 0.4, 0])
        tanto = self.palabra("tiembla tanto como vale", ROJO, 0.9).move_to([0, 1.5, 0])
        with self.narrar("b2"):
            self.en("finos")
            self.play(Create(t_a), Create(t_c), run_time=0.3)
            self.play(FadeOut(self.altos), FadeOut(self.ceros), ReplacementTransform(bos, bos10), run_time=self.dur(0.9))
            self.en("altos")
            self.play(FadeOut(opa), FadeOut(opb), FadeOut(opc), FadeOut(t_a), FadeOut(t_c), Create(tope), run_time=self.dur(0.6))
            self.en("denso")
            self.play(FadeIn(denso), FadeIn(no_bajo), run_time=0.5)
            self.en("cadafrec")
            self.play(FadeOut(denso), FadeOut(no_bajo), Create(vert), run_time=self.dur(0.5))
            self.en("media1")
            self.play(FadeIn(media), run_time=0.4)
            self.en("alrededor")
            self.play(Create(flechas), run_time=self.dur(0.5))
            self.en("desv1")
            self.play(FadeIn(desv), run_time=0.4)
            self.en("tanto")
            self.pop(tanto)
