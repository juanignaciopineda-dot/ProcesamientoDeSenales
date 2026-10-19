"""Escena 11 — El resultado leído como un suelo más una multa, y la comprobación con el dado."""
from comun.escena import *


class SueloYMulta(EscenaCurso):
    ESCENA = "11"

    def construct(self):
        self.lectura()
        self.comprobar()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def lectura(self):
        R = formula(r"E[(Y-\hat{y})^2]", "=", r"\sigma^2", "+", r"(\mu-\hat{y})^2", escala=1.6,
                    colores={0: TXT, 2: SENAL, 4: ESTIMACION}).move_to([0, 3.2, 0])
        self.add(R)
        P = ParabolaApuestas8(centro=(0.0, -0.9), ancho=8.0, alto=3.8)
        marco_s = SurroundingRectangle(R[2], buff=0.1, color=SENAL, stroke_width=4)
        marco_s.permitir_encima = True
        yt = MathTex(r"\hat{y}", color=INK).scale(1.8).next_to(R[2], DOWN, buff=0.45)
        tach_y = tachar(yt, ROJO)
        suelo = P.suelo(INK)
        et_suelo = Text("Suelo", color=INK, weight=BOLD).scale(0.65).move_to(P.xy(P.A1, P.SUELO) + RIGHT * 0.8)
        marco_m = SurroundingRectangle(R[4], buff=0.1, color=ESTIMACION, stroke_width=4)
        marco_m.permitir_encima = True
        a = ValueTracker(5.0)
        punto = always_redraw(lambda: Dot(P.p(a.get_value()), radius=0.12, color=ESTIMACION))
        seg = always_redraw(lambda: Line(P.xy(a.get_value(), P.SUELO),
                                         P.xy(a.get_value(), max(float(P.ecm(a.get_value())), P.SUELO + 0.03)),
                                         color=ERROR, stroke_width=6))
        mayor = MathTex(r"\geq 0", color=ERROR).scale(1.0).move_to(P.xy(5.0, (P.SUELO + float(P.ecm(5.0))) / 2) + RIGHT * 0.9)
        mejor = MathTex(r"\hat{y}=\mu", color=ESTIMACION).scale(1.4).move_to([5.4, 1.6, 0])
        error = Text("Error = σ²", color=ESTIMACION, weight=BOLD).scale(0.8).move_to([5.3, 0.4, 0])

        with self.narrar("b1"):
            # «El primer término»
            self.en("primer")
            self.play(FadeIn(marco_s), run_time=self.dur(0.4))

            # «no depende de lo que apuestes»
            self.en("nodepende")
            self.play(FadeIn(yt, shift=UP * 0.1), run_time=self.dur(0.4))
            self.play(Create(tach_y), run_time=self.dur(0.3))

            # «un suelo que no puedes perforar»
            self.en("suelo")
            self.play(FadeIn(P), Create(P.curva), run_time=self.dur(0.9))
            self.play(Create(suelo), FadeIn(et_suelo), run_time=self.dur(0.5))

            # «El segundo es una multa»
            self.en("multa")
            self.play(FadeOut(marco_s), FadeOut(yt), FadeOut(tach_y), FadeIn(marco_m), run_time=self.dur(0.3))
            self.add(punto, seg)
            self.sfx("pop")

            # «nunca es negativa»
            self.en("positiva")
            self.pop(mayor)

            # «vale cero solo si apuestas la media»
            self.en("cero")
            self.play(FadeOut(mayor), a.animate.set_value(3.5), run_time=self.dur(1.6))

            # «la mejor apuesta es la media»
            self.en("mejor")
            self.pop(mejor)

            # «el error que queda es la varianza»
            self.en("error")
            self.pop(error)
        punto.clear_updaters()
        seg.clear_updaters()
        self.wait(0.3)

    # ------------------------------------------------------------ b2
    def comprobar(self):
        d = dado_n(3).scale(0.9).move_to([-2.2, 3.0, 0])
        ap = Text("Apuesta 3", color=ESTIMACION, weight=BOLD).scale(0.8).next_to(d, RIGHT, buff=0.3)
        F = formula(r"2{,}92", "+", r"(3{,}5-3)^2", "=", r"2{,}92", "+", r"0{,}25", "=", r"3{,}17", escala=1.5,
                    colores={0: SENAL, 2: ESTIMACION, 8: ESTIMACION}).move_to([0, 0.7, 0])
        ok = tilde(VERDE, 0.9).move_to([-3.0, -0.9, 0])
        larga = Text("Igual que la cuenta larga", color=VERDE, weight=BOLD).scale(0.85).next_to(ok, RIGHT, buff=0.3)
        var = Text("Varianza", color=SENAL, weight=BOLD).scale(1.2)
        igual = Text("=", color=TXT, weight=BOLD).scale(1.2)
        queda = Text("Lo que queda", color=ESTIMACION, weight=BOLD).scale(1.2)
        lectura = VGroup(var, igual, queda).arrange(RIGHT, buff=0.4).move_to([0, 1.9, 0])
        mejor = VGroup(tilde(VERDE, 0.7), Text("Tras la mejor apuesta", color=VERDE, weight=BOLD).scale(0.85)
                       ).arrange(RIGHT, buff=0.35).move_to([0, 0.5, 0])
        o = ojo(TXT).scale(1.5).move_to([-2.8, -1.4, 0])
        tach = Line(o.get_corner(DL), o.get_corner(UR), color=ROJO, stroke_width=8)
        incer = Text("Incertidumbre", color=ESTIMACION, weight=BOLD).scale(1.0).move_to([2.2, -1.4, 0])

        with self.narrar("b2"):
            # «Comprobémoslo con el dado»
            self.en("dado")
            self.corte()
            self.play(FadeIn(d, scale=0.6), FadeIn(ap), run_time=self.dur(0.6))

            # «Si apostamos tres»
            self.en("apostamos3")
            self.resaltar(ap, color=ESTIMACION, escala=1.15, run_time=0.6)

            # «la varianza, dos coma nueve dos»
            self.en("v")
            self.play(FadeIn(F[0], shift=UP * 0.1), FadeIn(F[1]), run_time=self.dur(0.5))

            # «tres coma cinco menos tres al cuadrado»
            self.en("m")
            self.play(FadeIn(F[2], shift=UP * 0.1), run_time=self.dur(0.7))

            # «cero coma veinticinco»
            self.en("c")
            self.play(*[FadeIn(F[i]) for i in (3, 4, 5, 6)], run_time=self.dur(0.7))

            # «Tres coma uno siete»
            self.en("r")
            self.play(FadeIn(F[7]), FadeIn(F[8], scale=1.3), run_time=self.dur(0.5))

            # «lo mismo que con la cuenta larga»
            self.en("larga")
            self.sfx("exito")
            self.play(FadeIn(ok, scale=0.5), FadeIn(larga), run_time=self.dur(0.6))

            # «una lectura que usaremos mucho»
            self.en("lectura")
            self.play(*[FadeOut(m) for m in (d, ap, F, ok, larga)], run_time=0.3)
            self.play(FadeIn(var, shift=UP * 0.1), FadeIn(igual), FadeIn(queda, shift=UP * 0.1), run_time=self.dur(0.9))

            # «la incertidumbre que queda»
            self.en("incert")
            self.resaltar(queda, color=ESTIMACION, escala=1.15, run_time=0.6)

            # «cuando ya has hecho lo mejor que podías»
            self.en("mejorque")
            self.play(FadeIn(mejor, shift=UP * 0.1), run_time=self.dur(0.6))

            # «sin mirar nada más»
            self.en("nada")
            self.play(FadeIn(o, scale=0.6), run_time=self.dur(0.4))
            self.play(Create(tach), FadeIn(incer, shift=LEFT * 0.2), run_time=self.dur(0.5))
