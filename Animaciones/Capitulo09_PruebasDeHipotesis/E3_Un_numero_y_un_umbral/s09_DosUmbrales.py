"""Escena 09 — Dos umbrales y tres regiones: lejos del centro gana la campana ancha."""
from comun.escena import *
from comun.figuras_c9e3 import *

RA, RB = -2.571, 1.238
YR = -3.45                      # altura de los rótulos de región, bajo los números del eje


class DosUmbrales(EscenaCurso):
    ESCENA = "09"

    def construct(self):
        self.C = CampanasS9(centro=(0, -2.6), ancho=12.0, alto=5.6, r_rango=(-5.5, 6.0), v_max=0.45)
        self.regiones()
        self.honestos()
        self.wait(1.0)
        self.limpiar()

    def rotulos(self, cortes, nombres, colores) -> VGroup:
        C = self.C
        bordes = [C.r0] + list(cortes) + [C.r1]
        return VGroup(*[Text(n, color=c, weight=BOLD).scale(0.45).move_to([C.p((a + b) / 2)[0], YR, 0])
                        for n, c, a, b in zip(nombres, colores, bordes[:-1], bordes[1:])])

    # ------------------------------------------------------------------ b1
    def regiones(self):
        C = self.C
        with self.narrar("b1"):
            # «La región del uno»
            self.en("reg1")
            eje = C.eje((-4, -2, 0, 2, 4))
            c0, c1 = C.campana_s(0, 1, C0), C.campana_s(2, 2, C1)
            self.play(FadeIn(eje), Create(c0), Create(c1), run_time=self.dur(0.8))
            ra = C.region(C.r0, RA, C1)
            self.play(FadeIn(ra), run_time=self.dur(0.4))

            # «las dos colas»
            self.en("colas")
            rb = C.region(RB, C.r1, C1)
            self.play(FadeIn(rb), run_time=self.dur(0.4))

            # «el intervalo del medio»
            self.en("medio")
            rm = C.region(RA, RB, C0)
            rots = self.rotulos((RA, RB), ("Uno", "Cero", "Uno"), (C1, C0, C1))
            self.play(FadeIn(rm), LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in rots], lag_ratio=0.25),
                      run_time=self.dur(0.7))

            # «lejos del centro»
            self.en("lejos")
            fi = Arrow(C.p(-1.5) + UP * 3.3, C.p(-5.0) + UP * 3.3, color=INK, buff=0, stroke_width=4)
            fd = Arrow(C.p(2.5) + UP * 3.3, C.p(5.5) + UP * 3.3, color=INK, buff=0, stroke_width=4)
            self.play(GrowArrow(fi), GrowArrow(fd), run_time=self.dur(0.5))

            # «gana siempre la campana más ancha»
            self.en("ancha")
            ai = C.area_s(2, 2, C.r0, RA, C1, 0.4)
            ad = C.area_s(2, 2, RB, C.r1, C1, 0.4)
            self.play(FadeIn(ai), FadeIn(ad), Indicate(c1, color=C1, scale_factor=1.0), run_time=self.dur(0.7))

            # «las dos anchuras son iguales»
            self.en("iguales")
            c1n = C.campana_s(2, 1, C1)
            self.play(FadeOut(VGroup(ai, ad, fi, fd)), Transform(c1, c1n), run_time=self.dur(0.8))

            # «desaparece el término al cuadrado»
            self.en("sinr2")
            Q = formula("3r^2", "+4r", r"-9{,}55", r"\geq 0", escala=1.0).move_to([0, 2.85, 0])
            self.play(FadeIn(Q), run_time=self.dur(0.3))
            t = tachar(Q[0])
            self.play(Create(t), run_time=self.dur(0.4))

            # «queda un único umbral»
            self.en("unico")
            r0n, r1n = C.region(C.r0, 1, C0), C.region(1, C.r1, C1)
            rots2 = self.rotulos((1,), ("Cero", "Uno"), (C0, C1))
            self.play(FadeOut(VGroup(ra, rb, rm)), FadeIn(r0n), FadeIn(r1n), FadeOut(rots), FadeIn(rots2),
                      run_time=self.dur(0.7))
        self.c1, self.eje = c1, eje
        self.quitar = VGroup(Q, t, r0n, r1n, rots2)

    # ------------------------------------------------------------------ b2
    def honestos(self):
        C = self.C
        with self.narrar("b2"):
            # «Siendo honestos»
            self.en("honestos")
            ra, rb, rm = C.region(C.r0, RA, C1), C.region(RB, C.r1, C1), C.region(RA, RB, C0)
            rots = self.rotulos((RA, RB), ("Uno", "Cero", "Uno"), (C1, C0, C1))
            self.play(FadeOut(self.quitar), Transform(self.c1, C.campana_s(2, 2, C1)),
                      FadeIn(VGroup(ra, rb, rm, rots)), run_time=self.dur(0.7))

            # «la cola izquierda casi nunca ocurre»
            self.en("cola")
            area = C.area_s(0, 1, C.r0, RA, ERROR, 0.8)
            self.zoom(C.p(-3.6) + UP * 0.9, 5.0, run_time=self.dur(0.7))
            self.play(FadeIn(area), Indicate(ra, color=ERROR, scale_factor=1.0), run_time=self.dur(0.6))

            # «El error baja»
            self.en("error")
            self.zoom_reset(run_time=self.dur(0.6))
            err = Text("Error", color=ERROR, weight=BOLD).scale(0.6).move_to([0, 3.15, 0])
            self.play(FadeIn(err, shift=DOWN * 0.1), run_time=self.dur(0.3))

            # «cero coma doscientos treinta»
            self.en("e230")
            e1 = Text("Solo el derecho: 0,230", color=TXT).scale(0.5).move_to([0, 2.45, 0])
            self.play(FadeIn(e1, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «cero coma doscientos veintisiete»
            self.en("e227")
            e2 = Text("Dos umbrales: 0,227", color=VERDE, weight=BOLD).scale(0.5).move_to([0, 1.8, 0])
            self.play(FadeIn(e2, shift=DOWN * 0.1), run_time=self.dur(0.4))

            # «la lección importa»
            self.en("leccion")
            self.play(FadeOut(VGroup(err, e1, e2, area)), run_time=self.dur(0.4))

            # «el umbral no se pone a ojo»
            self.en("ojo")
            o = ojo().scale(0.9).move_to([-3.0, 2.5, 0])
            to = tachar(o)
            self.play(FadeIn(o), run_time=self.dur(0.3))
            self.play(Create(to), run_time=self.dur(0.3))

            # «Se calcula la razón de verosimilitud»
            self.en("calc")
            lam = MathTex(LAMBDA, color=MEDIDA).scale(1.2).move_to([1.4, 2.5, 0])
            self.pop(lam)

            # «dónde supera a eta»
            self.en("supera")
            sup = formula(LAMBDA, ">", r"\eta", escala=1.2, colores={0: MEDIDA, 2: ESTIMACION}).move_to([1.4, 2.5, 0])
            marco = SurroundingRectangle(sup, color=ESTIMACION, buff=0.2, stroke_width=4)
            self.play(ReplacementTransform(lam, sup[0]), FadeIn(sup[1:]), run_time=self.dur(0.5))
            self.play(Create(marco), run_time=self.dur(0.4))
