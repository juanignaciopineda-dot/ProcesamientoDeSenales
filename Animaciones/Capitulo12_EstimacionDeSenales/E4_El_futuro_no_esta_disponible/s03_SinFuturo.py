"""Escena 03 — Sin futuro: el filtro causal solo ve presente y pasado, y el error solo es perpendicular a m ≥ 0."""
from comun.escena import *


class SinFuturo(EscenaCurso):
    ESCENA = "03"

    def construct(self):
        t_dif = self.palabra("lo difícil", AMBAR, 1.0).move_to([0, 3.2, 0])
        rel = reloj().scale(1.5).move_to([-5.6, 1.6, 0])
        fl = flecha([-4.6, 1.6, 0], [-3.2, 1.6, 0], INK, 3)
        txt_f = etiqueta("el futuro no ha llegado", INK, 0.55).move_to([-0.2, 1.6, 0])
        tach = Line([-4.4, 1.35, 0], [-3.4, 1.85, 0], color=ROJO, stroke_width=7)
        eje = eje_muestras(y=0.0)
        ahora = etiqueta("ahora", INK, 0.45).move_to([eje.pasado[-1].get_x(), -0.55, 0])
        blq = BloqueLTI("h", centro=(0, -1.9), ancho=2.2, alto=1.1, color=CIAN, largo=2.2)
        cau = self.palabra("causal", AMBAR, 0.8).move_to([5.2, -1.9, 0])
        f = oculta(formula("h[j]", "=", "0", r"\quad\text{para } j<0", escala=1.0, colores={3: ROJO}))
        f.move_to([-2.0, -3.3, 0])
        self.add(f)
        with self.narrar("b1"):
            # «lo difícil»
            self.en("dificil")
            self.pop(t_dif)

            # «tiempo real»
            self.en("real")
            self.play(FadeIn(rel, scale=0.7), run_time=self.dur(0.5))

            # «no puede usar el futuro»
            self.en("nofuturo")
            self.play(GrowArrow(fl), FadeIn(txt_f), run_time=self.dur(0.6))
            self.play(Create(tach), run_time=0.3)
            self.sfx("error")

            # «solo tiene el presente y el pasado»
            self.en("presente")
            self.play(Create(eje.base), FadeIn(ahora), run_time=self.dur(0.4))
            self.play(LaggedStart(*[FadeIn(d) for d in eje.pasado + eje.futuro], lag_ratio=0.15), run_time=self.dur(1.2))

            # «El filtro tiene que ser»
            self.en("filtro")
            self.play(FadeIn(blq), run_time=self.dur(0.6))

            # «causal»
            self.en("causal")
            self.pop(cau)

            # «hache de jota vale cero»
            self.en("hj")
            self.play(*revelar(f[0], f[1], f[2]), run_time=self.dur(0.6))

            # «para jota negativa»
            self.en("jneg")
            self.play(*revelar(f[3]), run_time=self.dur(0.6))

            # «la condición cambia»
            self.en("cambia")
            self.corte(eje)
            fe = formula("e", r"\perp", "x[n-m]", escala=1.3, colores={0: ERROR, 2: MEDIDA}).move_to([0, 2.2, 0])
            self.pop(fe)

            # «perpendicular a las muestras que tenemos»
            self.en("perp")
            anillos = [Circle(radius=0.24, color=VERDE, stroke_width=4).move_to(d) for d in eje.pasado]
            cruces = [cruz(ROJO, 0.35).move_to(d) for d in eje.futuro]
            self.play(LaggedStart(*[Create(a) for a in anillos], lag_ratio=0.12), run_time=self.dur(1.0))
            self.play(LaggedStart(*[Create(c) for c in cruces], lag_ratio=0.12), run_time=self.dur(0.8))

            # «eme mayor o igual que cero»
            self.en("mpos")
            marco = Rectangle(width=5.9, height=1.5, color=AMBAR, stroke_width=4).set_fill(AMBAR, 0.06)
            marco.move_to([(eje.pasado[0].get_x() + eje.pasado[-1].get_x()) / 2, -0.2, 0])
            fm = formula(r"m\geq 0", escala=1.2, colores={0: AMBAR}).move_to([marco.get_center()[0], -1.5, 0])
            self.play(Create(marco), run_time=self.dur(0.5))
            self.pop(fm)

        self.wait(1.0)
        self.limpiar()
