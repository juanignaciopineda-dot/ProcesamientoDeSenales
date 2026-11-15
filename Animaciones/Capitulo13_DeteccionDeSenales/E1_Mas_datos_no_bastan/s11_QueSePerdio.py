"""Escena 11 — ¿Qué se perdió al promediar? La lección del capítulo y la pregunta del siguiente episodio."""
from comun.escena import *


class QueSePerdio(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.perdido()
        self.leccion()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def perdido(self):
        P = Plano2(centro=(-3.0, -0.3), u=1.7)
        diag = DashedLine(P.p(-1.5, -1.5), P.p(1.5, 1.5), color=AMBAR, stroke_width=3)
        A = Dot(P.p(1.0, -1.0), radius=0.16, color=MEDIDA)
        B = Dot(P.p(0.0, 0.0), radius=0.16, color=ESTIMACION)
        proy = DashedLine(A.get_center(), P.p(0, 0), color=INK, stroke_width=3)
        la = MathTex("(1,-1)", color=MEDIDA).scale(1.0).next_to(A, DR, buff=0.12)
        lb = MathTex("(0,0)", color=ESTIMACION).scale(1.0).move_to(P.p(-0.9, 1.35))
        cero = MathTex("a=0", color=AMBAR).scale(1.7).move_to([4.2, 2.6, 0])
        tira = Arrow(P.p(-1.0, 1.0), P.p(1.0, -1.0), buff=0, color=ROJO, stroke_width=5)
        tira.add_tip(at_start=True)
        lbl_tira = Text("lo que se tira", color=ROJO, weight=BOLD).scale(0.85).move_to([4.2, 0.4, 0])
        self.P1 = VGroup(P.ejes, P.rot1, P.rot2, P.grande, P.pequeno, diag, A, B, proy, la, lb, cero, tira, lbl_tira)

        with self.narrar("b1"):
            # «¿Qué ha pasado?»
            self.en("pasado")
            self.corte()
            self.play(FadeIn(P.ejes), FadeIn(P.rot1), FadeIn(P.rot2), FadeIn(P.grande), FadeIn(P.pequeno),
                      Create(diag), run_time=self.dur(0.8))

            # «Dos pares de mediciones muy distintos»
            self.en("pares")
            self.play(FadeIn(A, scale=0.5), FadeIn(B, scale=0.5), run_time=self.dur(0.6))

            # «el mismo promedio»
            self.en("mismo")
            self.play(Create(proy), run_time=self.dur(0.8))

            # «Uno y menos uno»
            self.en("um")
            self.play(FadeIn(la), run_time=self.dur(0.4))

            # «cero y cero»
            self.en("cc")
            self.play(FadeIn(lb), run_time=self.dur(0.4))

            # «promedian cero los dos»
            self.en("cero")
            self.pop(cero)

            # «el par entero»
            self.en("entero")
            self.play(B.animate.set_color(SENAL), A.animate.set_color(INK), run_time=self.dur(0.6))

            # «distinguir»
            self.en("distinguir")
            self.play(A.animate(rate_func=there_and_back).scale(1.8), B.animate(rate_func=there_and_back).scale(1.8),
                      run_time=self.dur(0.8))

            # «Con el promedio, ya no»
            self.en("yano")
            self.play(A.animate.move_to(P.p(0, 0)), FadeOut(proy), run_time=self.dur(0.8))

            # «tiramos»
            self.en("tiramos")
            self.play(Create(tira), run_time=self.dur(0.6))
            self.play(FadeIn(lbl_tira), run_time=self.dur(0.4))
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def leccion(self):
        leccion = self.palabra("lección", AMBAR, 1.7).move_to([0, 3.2, 0])
        mas = Text("más datos", color=TXT, weight=BOLD).scale(1.2)
        mejor = Text("mejor decisión", color=INK, weight=BOLD).scale(1.2)
        par = VGroup(mas, mejor).arrange(RIGHT, buff=0.7).move_to([0, 1.8, 0])
        tach = tachar(mejor)
        datos = Text("datos", color=MEDIDA, weight=BOLD).scale(1.1).move_to([-5.0, 0.2, 0])
        proc = caja("procesar", AMBAR, ancho=3.6, alto=1.3, scale=0.95).move_to([0, 0.2, 0])
        decis = Text("decisión", color=ESTIMACION, weight=BOLD).scale(1.1).move_to([5.4, 0.2, 0])
        f1 = flecha([-3.8, 0.2, 0], [-2.0, 0.2, 0], color=INK)
        f2 = flecha([2.0, 0.2, 0], [3.6, 0.2, 0], color=INK)
        fila = VGroup(datos, proc, decis, f1, f2)
        interrog = Text("?", color=AMBAR, weight=BOLD).scale(3.2).move_to([0, 1.0, 0])
        cas = casillas(3, rojas=(), centro=(-4.6, -2.4), lado=0.85)
        bars = barras_senal([2, 2, 1], centro=(-4.6, -3.2), ancho=0.8, hueco=0.25, unidad=0.85, color=SENAL)
        campana = campana_mini(centro=(-4.6, 0.1), ancho=2.8, alto=1.4, color=RUIDO)
        rg = Text("ruido gaussiano", color=RUIDO).scale(0.7).move_to([-4.6, -0.9, 0])
        caja_res = RoundedRectangle(corner_radius=0.15, width=3.0, height=2.2, color=AMBAR, stroke_width=4,
                                    fill_color=AMBAR, fill_opacity=0.08).move_to([3.4, -2.0, 0])
        flecha_r = flecha([-2.5, -2.0, 0], [1.6, -2.0, 0], color=AMBAR, ancho=4)
        unico = Text("?", color=AMBAR, weight=BOLD).scale(2.4).move_to(caja_res.get_center())
        ok = tilde(VERDE, 1.2).move_to([5.8, -0.4, 0])

        with self.narrar("b2"):
            # «la lección del capítulo»
            self.en("leccion")
            self.corte()
            self.pop(leccion)

            # «más datos no ayudan solos»
            self.en("nosolos")
            self.play(FadeIn(par), run_time=self.dur(0.5))
            self.play(Create(tach), run_time=self.dur(0.4))

            # «Hay que procesarlos bien»
            self.en("procesar")
            self.play(FadeIn(fila), run_time=self.dur(0.7))

            # «la pregunta importante»
            self.en("importante")
            self.play(FadeOut(fila), FadeOut(par), FadeOut(tach), FadeOut(leccion), run_time=0.25)
            self.pop(interrog)

            # «en el caso que de verdad nos interesa»
            self.en("interesa")
            self.play(interrog.animate.scale(0.55).move_to([0, 3.0, 0]), FadeIn(cas), run_time=self.dur(0.7))

            # «una señal conocida»
            self.en("conocida")
            self.play(FadeOut(cas), FadeIn(bars), run_time=self.dur(0.6))

            # «enterrada en ruido gaussiano»
            self.en("ruidog")
            self.play(Create(campana), FadeIn(rg), run_time=self.dur(0.8))

            # «¿hay un resumen que lo aproveche todo»
            self.en("resumen")
            self.play(FadeIn(caja_res), GrowArrow(flecha_r), run_time=self.dur(0.8))

            # «no tire nada»
            self.en("nada")
            self.pop(ok)

            # «Y es sorprendentemente sencillo»
            self.en("sencillo")
            self.play(caja_res.animate.scale(1.25), run_time=self.dur(0.6))

            # «un único número»
            self.en("unico")
            self.pop(unico)
        self.wait(0.3)
