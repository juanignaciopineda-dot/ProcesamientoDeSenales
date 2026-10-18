"""Escena 05 — La esperanza como punto de equilibrio: pesas sobre una regla y placa sobre un filo."""
from comun.escena import *


class PuntoDeEquilibrio(EscenaCurso):
    ESCENA = "05"

    def construct(self):
        R = Regla7(centro=(0, 0.3), ancho=9.6, rotulos=False)
        R.base.set_stroke(width=8, color=INK)
        pesas = VGroup(*[VGroup(Circle(radius=0.24, color=SENAL, stroke_width=3).set_fill(SENAL, 0.5),
                                Text(str(v), color=TXT, weight=BOLD).scale(0.4)).move_to(R.p(v) + UP * 0.4)
                         for v in range(1, 7)])
        viga = VGroup(R, pesas)             # solo para girar: no se agrega a la escena
        filo = Triangle(color=INK, stroke_width=3).set_fill(INK, 0.4).scale(0.3)

        def pos(v):
            return R.p(v) + DOWN * (0.06 + filo.height / 2)

        # la densidad recortada como una placa
        vs = np.linspace(0.6, 6.4, 120)
        alto = 5.5
        borde = [R.p(v) + UP * (0.1 + alto * float(gaussiana(v, 3.5, 1.1))) for v in vs]
        dens = VMobject(stroke_color=SENAL, stroke_width=4)
        dens.set_fill(opacity=0)
        dens.set_points_as_corners(borde)
        placa = VMobject(stroke_width=0)
        placa.set_fill(SENAL, 0.45)
        placa.set_points_as_corners(borde + [R.p(6.4) + UP * 0.1, R.p(0.6) + UP * 0.1, borde[0]])

        with self.narrar("b1"):
            # «una imagen física»
            self.en("imagen")
            filo.move_to(pos(3.5))
            self.play(Create(R), FadeIn(filo), run_time=self.dur(0.8))

            # «seis pesas iguales»
            self.en("pesas")
            self.play(LaggedStart(*[FadeIn(p, shift=DOWN * 0.4) for p in pesas], lag_ratio=0.15),
                      run_time=self.dur(1.5))

            # «en las posiciones del uno al seis»
            self.en("posiciones")
            self.play(*[m.animate.set_color(AMBAR) for m in R.marcas], run_time=self.dur(0.8))

            # «¿Dónde tienes que apoyarla»
            self.en("donde")
            for v, ang in ((5.5, 0.11), (1.5, -0.11)):
                self.play(filo.animate.move_to(pos(v)), run_time=0.45)
                self.play(Rotate(viga, angle=ang, about_point=R.p(v)), run_time=0.45)
                self.play(Rotate(viga, angle=-ang, about_point=R.p(v)), run_time=0.4)

            # «En tres coma cinco»
            self.en("equilibrio")
            self.play(filo.animate.move_to(pos(3.5)), R.base.animate.set_color(VERDE), run_time=self.dur(0.7))
            self.sfx("exito")

            # «el punto de equilibrio de la distribución»
            self.en("punto")
            mu = MathTex(r"\mu", color=AMBAR).scale(1.4).move_to(R.p(3.5) + DOWN * 1.0)
            self.pop(mu)

            # «Si la variable es continua»
            self.en("continua")
            self.play(FadeOut(pesas), Create(dens), run_time=self.dur(1.0))

            # «se recorta la densidad como una placa»
            self.en("placa")
            self.play(FadeIn(placa), run_time=self.dur(0.8))

            # «con una integral»
            self.en("integral")
            F = MathTex("E[X]", "=", r"\int", r"x\,f_X(x)", r"\,dx", color=TXT).scale(1.3).move_to([0, -2.6, 0])
            F[0].set_color(AMBAR)
            self.play(FadeIn(F[0:3], shift=DOWN * 0.15), run_time=self.dur(0.7))
            nota_ = nota("Suma de rectángulos finos", scale=0.5).move_to([0, 3.6, 0])
            self.play(FadeIn(nota_), run_time=0.4)

            # «equis por la densidad»
            self.en("xf")
            self.play(FadeIn(F[3], shift=DOWN * 0.15), run_time=self.dur(0.6))

            # «a lo largo de todo el eje»
            self.en("eje")
            eje = DoubleArrow(R.p(0.5) + DOWN * 1.8, R.p(6.5) + DOWN * 1.8, color=INK, stroke_width=3, buff=0)
            self.play(GrowFromCenter(eje), FadeIn(F[4], shift=DOWN * 0.15), run_time=self.dur(0.9))
        self.wait(1.0)
        self.limpiar()
