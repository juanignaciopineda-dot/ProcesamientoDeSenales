"""Escena 06 — La resolución: los tonos de 50 y 50,5 Hz con una ventana de 1 s y de 4 s."""
from comun.escena import *

F_ = np.linspace(49.0, 51.5, 700)


class ResolucionDeLosTonos(EscenaCurso):
    ESCENA = "06"

    def construct(self):
        self.tonos()
        self.regla()
        self.wait(1.0)
        self.limpiar()

    def tonos(self):
        P = Lienzo(ancho=10.5, alto=3.4, t_rango=(49, 51.5), v_max=2.0, centro=(0, -2.1))
        base = P.base()
        ray1 = VGroup(Line(P.p(F_TONO_1, 0), P.p(F_TONO_1, 1.5), color=SENAL, stroke_width=7), Dot(P.p(F_TONO_1, 1.5), radius=0.09, color=SENAL))
        ray2 = VGroup(Line(P.p(F_TONO_2, 0), P.p(F_TONO_2, 1.5), color=SENAL, stroke_width=7), Dot(P.p(F_TONO_2, 1.5), radius=0.09, color=SENAL))
        e50 = etiqueta("50 Hz", INK, 0.5).move_to(P.p(F_TONO_1, 0) + DOWN * 0.4)
        e505 = etiqueta("50,5 Hz", INK, 0.5).move_to(P.p(F_TONO_2, 0) + DOWN * 0.4 + RIGHT * 0.2)
        pal = self.palabra("desenfoque", AMBAR, 0.95).move_to([0, 3.3, 0])

        def ventana_t(seg, color=AMBAR):
            return Rectangle(width=0.7 * seg, height=0.55, color=color, stroke_width=3.5).set_fill(color, 0.18).move_to(
                [-6.4 + 0.35 * seg, 2.1, 0])

        v1, v4 = ventana_t(1), ventana_t(4)
        t1 = MathTex(r"1\,\mathrm{s}", color=AMBAR).scale(0.8).move_to([-5.0, 1.45, 0])
        t4 = MathTex(r"4\,\mathrm{s}", color=AMBAR).scale(0.8).move_to([-5.0, 1.45, 0])
        c1a = P.curva(F_, 0.9 * np.sinc(1 * (F_ - F_TONO_1)) ** 2, MEDIDA, 3.0, 0.9)
        c1b = P.curva(F_, 0.9 * np.sinc(1 * (F_ - F_TONO_2)) ** 2, MEDIDA, 3.0, 0.9)
        suma1 = P.curva(F_, tonos_medidos(F_, 1), ESTIMACION, 5)
        c4a = P.curva(F_, 0.9 * np.sinc(4 * (F_ - F_TONO_1)) ** 2, MEDIDA, 3.0, 0.9)
        c4b = P.curva(F_, 0.9 * np.sinc(4 * (F_ - F_TONO_2)) ** 2, MEDIDA, 3.0, 0.9)
        suma4 = P.curva(F_, tonos_medidos(F_, 4), ESTIMACION, 5)
        h = 0.45
        ancho1 = DoubleArrow(P.p(49.55, h), P.p(50.45, h), color=VERDE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        l_ancho1 = MathTex(r"1\,\mathrm{Hz}", color=VERDE).scale(0.7).move_to(P.p(50.0, h) + UP * 0.45)
        ancho4 = DoubleArrow(P.p(49.887, h), P.p(50.113, h), color=VERDE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.3)
        l_ancho4 = MathTex(r"0{,}25\,\mathrm{Hz}", color=VERDE).scale(0.7).move_to(P.p(50.0, h) + UP * 0.55 + LEFT * 0.9)
        ok = tilde(VERDE, 0.6).move_to([5.8, 0.6, 0])
        with self.narrar("b1"):
            self.en("conse")
            self.play(Create(base), run_time=0.4)
            self.pop(pal)
            self.en("tonos")
            self.play(Create(ray1), Create(ray2), run_time=self.dur(0.6))
            self.en("r50")
            self.play(FadeIn(e50), run_time=0.3)
            self.en("r505")
            self.play(FadeIn(e505), run_time=0.3)
            self.en("un_s")
            self.play(FadeIn(v1), FadeIn(t1), run_time=self.dur(0.5))
            self.en("campanas")
            self.play(FadeOut(ray1), FadeOut(ray2), Create(c1a), Create(c1b), run_time=self.dur(0.8))
            self.play(Create(ancho1), FadeIn(l_ancho1), run_time=self.dur(0.6))
            self.en("bulto")
            self.play(FadeOut(ancho1), FadeOut(l_ancho1), c1a.animate.set_stroke(opacity=0.3), c1b.animate.set_stroke(opacity=0.3),
                      Create(suma1), run_time=self.dur(0.8))
            self.en("cuatro_s")
            self.play(FadeOut(c1a), FadeOut(c1b), FadeOut(suma1), ReplacementTransform(v1, v4), ReplacementTransform(t1, t4),
                      Create(c4a), Create(c4b), run_time=self.dur(0.9))
            self.en("cuarto")
            self.play(Create(ancho4), FadeIn(l_ancho4), run_time=self.dur(0.5))
            self.en("dos_picos")
            self.play(FadeOut(ancho4), FadeOut(l_ancho4), Create(suma4), run_time=self.dur(0.6))
            self.pop(ok)

    def regla(self):
        P = Lienzo(ancho=10.5, alto=3.4, t_rango=(49, 51.5), v_max=2.0, centro=(0, -2.1))
        base = P.base()
        ray1 = VGroup(Line(P.p(F_TONO_1, 0), P.p(F_TONO_1, 1.5), color=SENAL, stroke_width=7), Dot(P.p(F_TONO_1, 1.5), radius=0.09, color=SENAL))
        ray2 = VGroup(Line(P.p(F_TONO_2, 0), P.p(F_TONO_2, 1.5), color=SENAL, stroke_width=7), Dot(P.p(F_TONO_2, 1.5), radius=0.09, color=SENAL))
        e50 = etiqueta("50 Hz", INK, 0.5).move_to(P.p(F_TONO_1, 0) + DOWN * 0.4)
        e505 = etiqueta("50,5 Hz", INK, 0.5).move_to(P.p(F_TONO_2, 0) + DOWN * 0.4 + RIGHT * 0.2)
        f_ele = etiqueta("ventana de L segundos", AMBAR, 0.6).move_to([-3.2, 3.2, 0])
        res = formula(r"\text{resolución}", r"\approx", r"\frac{1}{L}", escala=1.0, colores={0: AMBAR, 2: AMBAR}).move_to([3.5, 3.2, 0])
        sep = DoubleArrow(P.p(F_TONO_1, 1.8), P.p(F_TONO_2, 1.8), color=VERDE, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.2)
        l_sep = MathTex(r"0{,}5\,\mathrm{Hz}", color=VERDE).scale(0.75).move_to(P.p(50.25, 1.8) + UP * 0.4)
        cuenta = MathTex(r"\frac{1}{0{,}5}=2\,\mathrm{s}", color=AMBAR).scale(1.0).move_to([0, 1.2, 0])
        igual = formula(r"\text{resolución}", "=", r"\text{tiempo de grabación}", escala=0.8,
                        colores={0: AMBAR, 2: AMBAR}).move_to([0, 2.3, 0])
        relo = reloj(TXT).scale(0.9).move_to([5.8, 1.3, 0])
        sombra = Rectangle(width=14.2, height=8, stroke_width=0).set_fill(ROJO, 0.14)
        sombra.move_to([0, 0, 0])
        pr = etiqueta("un problema peor", ROJO, 0.7).move_to([0, 0.2, 0])
        larga = Rectangle(width=6.0, height=0.5, color=AMBAR, stroke_width=3.5).set_fill(AMBAR, 0.18).move_to([-3.4, 1.6, 0])
        x = cruz(ROJO, 1.0).move_to([-3.4, 1.6, 0])
        with self.narrar("b2"):
            self.en("ele")
            self.corte()
            self.play(Create(base), Create(ray1), Create(ray2), FadeIn(e50), FadeIn(e505), FadeIn(f_ele), run_time=self.dur(0.8))
            self.en("nodist")
            self.play(Create(sep), FadeIn(l_sep), run_time=self.dur(0.6))
            self.en("unosobre")
            self.play(FadeIn(res[0]), FadeIn(res[1]), FadeIn(res[2]), run_time=self.dur(0.7))
            self.en("separar")
            self.resaltar(sep, color=VERDE)
            self.en("dos_s")
            self.pop(cuenta)
            self.en("tiempo")
            self.play(FadeOut(f_ele), FadeIn(igual), FadeIn(relo), run_time=self.dur(0.6))
            self.en("peor")
            self.play(FadeIn(sombra, shift=LEFT * 2), run_time=self.dur(0.6))
            self.en("noarregla")
            self.play(FadeIn(larga), run_time=0.3)
            self.pop(x)
