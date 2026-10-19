"""Escena 03 — Un punto por cada umbral: cuatro umbrales llevados al plano (falsa alarma, detección)."""
from comun.escena import *
from comun.figuras_c9e4 import *

DX = 3.75          # cuánto se corren las campanas del centro a la izquierda


class UnPuntoPorUmbral(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        self.C = campanas_izq9()
        self.P = PlanoRoc9()
        self.familia()
        self.umbral_tres()
        self.otros_umbrales()
        self.wait(1.0)
        self.B.quieto()
        self.limpiar()

    # ------------------------------------------------------------ b1
    def familia(self):
        C, P = self.C, self.P
        eje = eje_izq9(C)
        c0, c1 = C.campana(0, 1, C0), C.campana(2, 1, C1)
        u0 = C.regla(CRUCE9, color=ROC, alto=2.9)
        camp = VGroup(eje, c0, c1).shift(RIGHT * DX)
        u0.shift(RIGHT * DX)
        self.camp = camp
        with self.narrar("b1"):
            # «Un detector no es»
            self.en("par")
            tarj = rotulo_par9("0,077", "0,72", escala=0.6).move_to(u0.get_top() + UP * 0.45)
            self.play(FadeIn(camp), FadeIn(u0), run_time=self.dur(0.4))
            self.pop(tarj)

            # «una familia entera»
            self.en("familia")
            otros = [("0,16", "0,84"), ("0,023", "0,5"), ("0,5", "0,98")]
            pila = VGroup(*[rotulo_par9(a, b, escala=0.6) for a, b in otros])
            for i, t in enumerate(pila):
                t.move_to(tarj.get_center() + RIGHT * (2.3 if i % 2 == 0 else -2.3) + UP * (0.55 * (i // 2) + 0.1))
            pila[1].shift(DOWN * 0.1)
            self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in pila], lag_ratio=0.3),
                      run_time=self.dur(0.9))

            # «Vamos a dibujarla»
            self.en("dibujar")
            self.play(FadeOut(tarj), FadeOut(pila), run_time=self.dur(0.3))
            self.play(camp.animate.shift(LEFT * DX), u0.animate.shift(LEFT * DX), run_time=self.dur(0.8))
            self.u0 = u0

            # «en horizontal»
            self.en("horiz")
            self.play(Create(P.ejes[0]), FadeIn(P.rot_x), FadeIn(P.nums[0]), FadeIn(P.nums[1]),
                      run_time=self.dur(0.6))

            # «en vertical»
            self.en("vert")
            self.play(Create(P.ejes[1]), FadeIn(P.rot_y), FadeIn(P.nums[2]), FadeIn(P.ejes[2]),
                      run_time=self.dur(0.6))

            # «Cada umbral es un»
            self.en("punto")
            fl = CurvedArrow(u0.get_top() + RIGHT * 0.15, P.p(0.25, 0.6), color=ROC, angle=-PI / 4,
                             stroke_width=4)
            self.play(u0.animate.set_stroke(width=7), Create(fl), run_time=self.dur(0.6))
            self.play(u0.animate.set_stroke(width=4), run_time=self.dur(0.3))
            self.flecha = fl

    # ------------------------------------------------------------ b2
    def lectura(self, fa: str, pd: str) -> VGroup:
        """Las dos lecturas del umbral actual, arriba de las campanas."""
        a = MathTex(r"P_{FA} = " + fa, color=FA).scale(0.75)
        b = MathTex(r"P_D = " + pd, color=DET).scale(0.75)
        a.move_to([-5.15, 2.45, 0], aligned_edge=LEFT)
        b.move_to([-5.15, 1.75, 0], aligned_edge=LEFT)
        return VGroup(a, b)

    def rot_umbral(self, u: str) -> Text:
        return Text(f"Umbral {u}", color=ROC, weight=BOLD).scale(0.5).move_to([-3.75, 3.35, 0])

    def umbral_tres(self):
        C, P = self.C, self.P
        B = Barrido9(C, P, u=CRUCE9)
        self.B = B
        with self.narrar("b2"):
            # «el umbral en tres voltios»
            self.en("u3")
            self.remove(self.u0)
            self.add(B.linea)
            ru = self.rot_umbral("3")
            self.play(FadeOut(self.flecha), B.u.animate.set_value(3.0), FadeIn(ru), run_time=self.dur(0.6))
            self.ru = ru

            # «La falsa alarma es»
            self.en("fa3")
            B.fresco()
            # la cola a la derecha de 3 es diminuta: una flecha la señala
            fl_fa = Arrow(C.p(4.1, 0.13), C.p(3.25, 0.012), color=FA, buff=0.05, stroke_width=4,
                          max_tip_length_to_length_ratio=0.25)
            self.play(FadeIn(B.cola0), GrowArrow(fl_fa), run_time=self.dur(0.4))

            # «una milésima»
            self.en("q3")
            fa = MathTex(r"P_{FA} = Q(3) = 0{,}001", color=FA).scale(0.75)
            fa.move_to([-5.15, 2.45, 0], aligned_edge=LEFT)
            self.play(FadeIn(fa, shift=DOWN * 0.15), run_time=self.dur(0.5))

            # «del tres al dos»
            self.en("desvio")
            br = BraceBetweenPoints(C.p(2) + DOWN * 0.6, C.p(3) + DOWN * 0.6, DOWN, color=INK)
            bt = Text("1 desvío", color=INK).scale(0.42).next_to(br, DOWN, buff=0.1)
            self.play(GrowFromCenter(br), FadeIn(bt), FadeOut(fl_fa), run_time=self.dur(0.5))

            # «cero coma dieciséis»
            self.en("pd3")
            pd = MathTex(r"P_D = Q(1) = 0{,}16", color=DET).scale(0.75)
            pd.move_to([-5.15, 1.75, 0], aligned_edge=LEFT)
            B.fresco()
            self.play(FadeIn(B.cola1), FadeIn(pd, shift=DOWN * 0.15), FadeOut(br), FadeOut(bt),
                      run_time=self.dur(0.5))
            self.lect = VGroup(fa, pd)

            # «Un punto pegado»
            self.en("p3")
            self.marcar(3.0, "3")

            # «Casi no hay falsas»
            self.en("pocas")
            aro = Ellipse(width=1.0, height=0.45, color=FA, stroke_width=4).move_to(C.p(3.45, 0.02))
            self.play(Create(aro), run_time=self.dur(0.4))
            self.play(FadeOut(aro), run_time=self.dur(0.3))

            # «se escapan casi todos»
            self.en("escapan")
            esc = C.area(2, 1, C.r0, 3.0, ERROR, 0.45)
            self.play(FadeIn(esc), run_time=self.dur(0.35))
            self.play(FadeOut(esc), run_time=self.dur(0.35))

    def marcar(self, u: float, txt: str):
        """Deja el punto del umbral u en el plano, con su rótulo."""
        P = self.P
        d = P.punto(*roc9(u))
        r = Text(txt, color=ROC, weight=BOLD).scale(0.42).next_to(d, RIGHT, buff=0.12)
        if u <= 0.5:
            r.next_to(d, DOWN, buff=0.12)
        self.sfx("tick")
        self.play(FadeIn(d, scale=0.4), FadeIn(r), run_time=self.dur(0.4))

    # ------------------------------------------------------------ b3
    def nueva_lectura(self, fa: str, pd: str, solo: int | None = None):
        nueva = self.lectura(fa, pd)
        if solo is None:
            self.play(ReplacementTransform(self.lect, nueva), run_time=self.dur(0.4))
            self.lect = nueva
        else:
            self.play(ReplacementTransform(self.lect[solo], nueva[solo]), run_time=self.dur(0.4))
            self.lect = VGroup(*[nueva[i] if i == solo else self.lect[i] for i in range(2)])

    def otros_umbrales(self):
        B = self.B
        with self.narrar("b3"):
            # «Bajamos el umbral a dos»
            self.en("u2")
            ru = self.rot_umbral("2")
            self.play(B.u.animate.set_value(2.0), ReplacementTransform(self.ru, ru), run_time=self.dur(0.8))
            self.ru = ru

            # «cero coma cero veintitrés»
            self.en("fa2")
            self.nueva_lectura("0{,}023", "", solo=0)

            # «justo media campana»
            self.en("media")
            self.nueva_lectura("0{,}023", "0{,}5", solo=1)

            # «cero coma cinco.»
            self.en("p2")
            self.marcar(2.0, "2")

            # «Con el umbral en uno»
            self.en("u1")
            ru = self.rot_umbral("1")
            self.play(B.u.animate.set_value(1.0), ReplacementTransform(self.ru, ru), run_time=self.dur(0.7))
            self.ru = ru
            self.nueva_lectura("0{,}16", "0{,}84")

            # «cero coma ochenta y cuatro»
            self.en("p1")
            self.marcar(1.0, "1")

            # «con el umbral en cero»
            self.en("u0")
            ru = self.rot_umbral("0")
            self.play(B.u.animate.set_value(0.0), ReplacementTransform(self.ru, ru), run_time=self.dur(0.7))
            self.ru = ru
            self.nueva_lectura("0{,}5", "0{,}98")

            # «cero coma noventa y ocho»
            self.en("p0")
            self.marcar(0.0, "0")
