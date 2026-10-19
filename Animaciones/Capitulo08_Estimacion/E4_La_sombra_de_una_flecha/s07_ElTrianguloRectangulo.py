"""Escena 07 — Pitágoras con las flechas: 4 = 3,2 + 0,8."""
from comun.escena import *
from comun.figuras_c8e4 import *


class ElTrianguloRectangulo(EscenaCurso):
    ESCENA = "07"

    def construct(self):
        self.triangulo()
        self.cuentas()
        self.wait(1.0)
        self.limpiar()

    # ------------------------------------------------------------ b1
    def triangulo(self):
        F, r = flechas8()
        self.F = F
        self.add(F.presente, F.futuro, F.sombra, F.error, F.recto, r["x"], r["y"])
        zona = Polygon(F.o, F.fin_futuro, F.fin_sombra, stroke_width=0, stroke_opacity=0).set_fill(SENAL, 0.14)
        n = np.array([-np.sin(np.deg2rad(ANG8)), np.cos(np.deg2rad(ANG8)), 0])
        t_hipo = Text("Hipotenusa", color=SENAL).scale(0.55).move_to((F.o + F.fin_futuro) / 2 + n * 0.6)
        t_cat1 = Text("Cateto", color=ESTIMACION).scale(0.55).move_to((F.o + F.fin_sombra) / 2 + DOWN * 0.45)
        t_cat2 = Text("Cateto", color=ERROR).scale(0.55).move_to((F.fin_sombra + F.fin_futuro) / 2 + RIGHT * 0.75)
        p1 = formula(r"\text{hipotenusa}^2", escala=1.1, color=SENAL).move_to([3.7, 2.7, 0])
        p2 = formula("=", r"\text{cateto}^2", "+", r"\text{cateto}^2", escala=1.1,
                     colores={1: ESTIMACION, 3: ERROR}).move_to([3.7, 1.7, 0])

        with self.narrar("b1"):
            # «Ahora el error»
            self.en("ahora")
            self.resaltar(F.error, color=ERROR, escala=1.08)

            # «la sombra y el error forman»
            self.en("som1")
            self.resaltar(F.sombra, F.error, color=AMBAR, escala=1.04)

            # «un triángulo rectángulo»
            self.en("triang")
            self.play(FadeIn(zona), run_time=self.dur(0.7))

            # «es la hipotenusa»
            self.en("hipo")
            self.play(FadeIn(t_hipo), run_time=self.dur(0.5))
            self.resaltar(F.futuro, color=SENAL, escala=1.04)

            # «la sombra y el error»
            self.en("cat")
            self.play(FadeIn(t_cat1), FadeIn(t_cat2), run_time=self.dur(0.5))

            # «Pitágoras dice»
            self.en("pit")
            self.play(FadeIn(p1), run_time=self.dur(0.5))

            # «al cuadrado es la suma»
            self.en("igual")
            self.play(FadeIn(p2[0]), run_time=self.dur(0.4))

            # «de los catetos al cuadrado»
            self.en("suma")
            self.play(*[FadeIn(p2[i]) for i in (1, 2, 3)], run_time=self.dur(0.7))
        self.p1, self.p2 = p1, p2

    # ------------------------------------------------------------ b2
    def cuentas(self):
        F = self.F
        a = formula(r"\sigma_Y^2", "=", "4", escala=1.15, colores={0: SENAL}).move_to([2.6, 0.4, 0])
        b1 = formula(r"\text{Sombra}", "=", num_tex(1.79), escala=1.15, colores={0: ESTIMACION}).move_to([2.6, -0.4, 0])
        b2 = formula(r"\text{Sombra}^2", "=", num_tex(3.2), escala=1.15, colores={0: ESTIMACION}).move_to([2.6, -0.4, 0])
        c1 = formula(r"\text{Error}^2", "=", "4-" + num_tex(3.2), escala=1.15, colores={0: ERROR}).move_to([2.6, -1.2, 0])
        c2 = formula("=", num_tex(0.8), escala=1.15, colores={1: ERROR}).next_to(c1, RIGHT, buff=0.2)
        igual = Text("Igual que la parábola", color=VERDE).scale(0.5).move_to([2.6, -1.85, 0])
        ok = tilde(VERDE, 0.4).next_to(igual, LEFT, buff=0.15)
        d1 = formula(r"\text{Error}", "=", r"\sqrt{" + num_tex(0.8) + "}", escala=1.15, colores={0: ERROR}).move_to([2.6, -2.7, 0])
        d2 = formula(r"\approx", num_tex(0.89), escala=1.15, colores={1: ERROR}).next_to(d1, RIGHT, buff=0.2)

        with self.narrar("b2"):
            # «la varianza de la temperatura»
            self.en("var")
            self.play(FadeIn(a), run_time=self.dur(0.7))
            self.resaltar(self.F.futuro, color=SENAL, escala=1.04)

            # «La sombra mide»
            self.en("sombra")
            self.play(FadeIn(b1), run_time=self.dur(0.7))

            # «tres coma dos»
            self.en("s32")
            self.play(ReplacementTransform(b1, b2), run_time=self.dur(0.7))

            # «cuatro menos tres coma dos»
            self.en("resta")
            self.play(FadeIn(c1), run_time=self.dur(0.9))

            # «cero coma ocho»
            self.en("e08")
            self.play(FadeIn(c2), run_time=self.dur(0.5))

            # «Otra vez el mismo número»
            self.en("mismo")
            self.play(FadeIn(igual), FadeIn(ok, scale=0.4), run_time=self.dur(0.6))
            self.resaltar(c2, color=VERDE, escala=1.15)

            # «raíz de cero coma ocho»
            self.en("raiz")
            self.play(FadeIn(d1), run_time=self.dur(0.8))

            # «unos cero coma nueve»
            self.en("e089")
            self.play(FadeIn(d2), run_time=self.dur(0.5))
